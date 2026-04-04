default bot_parts_do_not_sell={}

init -100 python:
  base_bot_part_prices={
    "F": 25,
    "E": 100,
    "D": 250,
    "C": 500,
    "B": 1000,
    "A": 2500,
    "S": 5000,
    }

  class BotPartMeta(ItemMeta):
    def __init__(cls,name,bases,dct):
      if not dct.get("do_not_register",False):
        part_id=cls.id
        part_name=cls.name
        expertise_cls_id="expertise_"+part_id
        expertise_cls_name="Expertise_"+part_id
        expertise=type(expertise_cls_name,(Expertise,),{"id":expertise_cls_id,"name":part_name,"stat_type":"expertise_bot_part"})
        setattr(store,expertise_cls_name,expertise)
      super(BotPartMeta,cls).__init__(name,bases,dct)

  class BotPart(Item,metaclass=BotPartMeta):
    do_not_register=True
    custom_item=True
    category="bot_parts"

    notify_inventory_changed=False
    notify_chassis_part_integrity_changed=True
    notify_chassis_part_defect_added=True

    name="bot part"
    description="- bot part description -"

    rate="F"
    category_price_mult=1.0
    price_mult=1.0
    xp_mult=1

    slot=None

    damage_mult=1.0
    damage_on_remove=0
    possible_defects=[] ## (defect_id or None,weight)

    power_consumption=0

    effect_slots=0
    possible_effects=[]

    repair_skills=[("mechanics",100)]
    difficulty=1.0

    list_target_chances={}
    list_target_tag_chances={}

    def __init__(self,*args,**kwargs):
      super(BotPart,self).__init__(*args,**kwargs)
      self.owner=kwargs.get("owner")
      self.defects=[]
      self.effects=[]
      self.integrity=100

    @property
    def base_price(self):
      return int(round(base_bot_part_prices[self.rate]*self.category_price_mult*self.price_mult))

    @property
    def rate_level(self):
      return "FEDCBAS".index(self.rate.upper())+1

    @property
    def owner(self):
      return find_character(self._owner)
    @owner.setter
    def owner(self,owner):
      owner=find_character(owner)
      self._owner=getattr(find_character(owner),"id",None)

    @property
    def integrity(self):
      return self._integrity
    @integrity.setter
    def integrity(self,integrity):
      self._integrity=min(self.integrity_cap,max(0,integrity))
    @property
    def integrity_cap(self):
      rv=100
      for defect in self.defects:
        rv=min(rv,defect.integrity_cap)
      rv=min(100,max(0,rv))
      return rv

    @property
    def is_disabled(self):
      for defect in self.defects:
        if defect.disabling:
          return True
      if self.integrity<=0:
        return True
      return False
    @property
    def is_destroyed(self):
      for defect in self.defects:
        if defect.destroyed:
          return True
      return False
    @property
    def has_irrepairable_defects(self):
      for defect in self.defects:
        if not defect.repairable:
          return True
      return False

    @property
    def do_not_sell(self):
      return bot_parts_do_not_sell.get(self.id,False)
    @do_not_sell.setter
    def do_not_sell(self,dns):
      bot_parts_do_not_sell[self.id]=bool(dns)

    def apply_damage(self,damage,minimal_integrity=0,silent=False):
      notify.disable("chassis_part_integrity_changed",silent)
      notify.disable("chassis_part_defect_added",silent)
      if damage=="destroy":
        damage=self.integrity
      elif damage=="max":
        damage=minimal_integrity
      else:
        if damage>0:
          damage=damage*self.damage_mult
          if self.owner:
            damage=self.owner.process_event("calc_effective_part_damage:1",self,damage)
          damage=max(1,int(round(damage)))
        damage=min(damage,max(0,self.integrity-minimal_integrity))
      if damage>0:
        process_event("chassis_part_integrity_changed",self.owner,self,-damage)
        current_defects=set([defect.id for defect in self.defects])
        for n in range(0,damage):
          self.integrity-=1
          possible_defects={}
          for defect_id,integrity_cap,weight in self.possible_defects:
            if integrity_cap>=self.integrity:
              defect=find_bot_part_defect_cls(defect_id) if defect_id else None
              if defect and defect_id in current_defects and not defect.can_apply_multiple:
                continue
              if defect_id in possible_defects:
                if possible_defects[defect_id][0]<integrity_cap:
                  continue
              possible_defects[defect_id]=(integrity_cap,weight)
          if possible_defects:
            possible_defects=[((defect_id,integrity_cap),weight) for defect_id,(integrity_cap,weight) in possible_defects.items() if weight]
            defect,integrity_cap=renpy.random.wchoice(possible_defects)
            if defect:
              defect=find_bot_part_defect_cls(defect)
              defect=defect(integrity_cap=integrity_cap)
              self.defects.append(defect)
              process_event("chassis_part_defect_added",self.owner,self,defect)
              current_defects=set([defect.id for defect in self.defects])
      notify.enable("chassis_part_integrity_changed",silent)
      notify.enable("chassis_part_defect_added",silent)

    def on_calc_effective_xp(self,char,part,stat,xp):
      if xp>0:
        if isinstance(char,SexBot):
          if stat.id!="autonomy":
            if not part.is_disabled:
              xp_mult=part.xp_mult
              if isinstance(xp_mult,dict):
                xp_mult=xp_mult.get(stat.id)
              if isinstance(xp_mult,str):
                xp_mult=eval(xp_mult,{"bot":char,"part":part,"stat":stat,"xp":xp})
              if xp_mult:
                xp=xp*xp_mult
              for defect in part.defects:
                xp_mult=defect.xp_mult
                if isinstance(xp_mult,dict):
                  xp_mult=xp_mult.get(stat.id)
                if isinstance(xp_mult,str):
                  xp_mult=eval(xp_mult,{"bot":char,"part":part,"defect":defect,"stat":stat,"xp":xp})
                if xp_mult:
                  xp=xp*xp_mult
      return xp

init python hide:
  @event_handler("generate_bot_part")
  def list_modded_parts(parts,target,tags):
    for part_id,part_cls in modded_bot_part_classes.items():
      target_weight=part_cls.list_target_chances.get(target)
      if target_weight is not None:
        parts.append((part_id,target_weight))
        continue
      max_tag_weight=0
      for tag in tags:
        tag_weight=part_cls.list_target_tag_chances.get(tag) or 0
        if tag_weight>max_tag_weight:
          max_tag_weight=tag_weight
      if max_tag_weight>0:
        parts.append((part_id,max_tag_weight))

init 80 python:
  modded_bot_part_classes={}

  def load_bot_parts_from_mods():
    parts_info=load_info_table_from_mods("bot_parts")
    for part_base_id,bot_part in sorted(parts_info.items()):
      if bot_part:
        part_id="bot_part_"+part_base_id
        part_cls_dct=bot_part.copy()
        part_cls_dct["id"]=part_id
        part_cls_name="BotPart_"+part_base_id
        part_cls=type(part_cls_name,(BotPart,),part_cls_dct)
        setattr(store,part_cls_name,part_cls)
        modded_bot_part_classes[part_id]=part_cls
        if log_modded_entries():
          print("Loaded modded bot part:",part_base_id)

  load_bot_parts_from_mods()
