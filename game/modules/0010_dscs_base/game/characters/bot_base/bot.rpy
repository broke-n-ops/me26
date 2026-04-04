init -5 python:
  base_bot_model_prices={
    "F": 1000,
    "E": 2500,
    "D": 5000,
    "C": 10000,
    "B": 25000,
    "A": 50000,
    "S": 180000,
    }

  for rate_n,rate in enumerate("FEDCBAS"):
    base_bot_model_prices[rate.lower()]=base_bot_model_prices[rate]
    base_bot_model_prices[rate_n+1]=base_bot_model_prices[rate]

  class SexBotMeta(CharMeta):
    def __init__(cls,name,bases,dct):
      if not dct.get("do_not_register",False):
        model_id=cls.model_id
        model_name=cls.model_name
        expertise_cls_id="expertise_"+model_id
        expertise_cls_name="Expertise_"+model_id
        expertise=type(expertise_cls_name,(Expertise,),{"id":expertise_cls_id,"name":model_name,"stat_type":"expertise_bot_model"})
        setattr(store,expertise_cls_name,expertise)
      super(SexBotMeta,cls).__init__(name,bases,dct)

  class SexBot(Char,metaclass=SexBotMeta):

    do_not_register=True

    gender="female"

    model_id=None
    model_name="model_name"
    model_description=None

    rate="F"
    price_mult=1.0
    
##==========squirrel: section adding stats, update here as needed==========

    ufc_wins=0              ## UFC win count
    ufc_losses=0            ## UFC loss count
    ufc_record="0 - 0"      ## UFC record as text needed for status display
    scavenge_success=0      ## Scavenge success count
    mt_just_assigned=0      ## master techie - if just assigned do not perform role (0.10.n)
    st_just_assigned=0      ## senior techie - if just assigned do not perform role (0.10.n)
    shpkpr_just_assigned=0  ## shopkeeper - if just assigned do not perform role (0.10.n)
    tech_just_assigned=0    ## techie - if just assigned do not perform role (0.10.n)
    clerk_just_assigned=0    ## clerk - if just assigned do not perform role (0.10.n)
    mgr_just_assigned=0     ## bot manager - if just assigned do not perform role (0.10.n)
    mgr_priority="default"  ## default is highest skill, ties broken by sex>tech>combat, otherwise set priority to "sex", "tech", "combat"
    trainer_subject=""      ## subject a bot trainer will teach (0.12.n)
    trainee_subject="never" ## subject a bot trainee will learn if set, can opt out and value will be "never" (0.12.n)
    bt_just_assigned=0      ## bot trainer - if just assigned do not perform role (0.12.n)
    task_req_integrity=0    ## integrity required to perform all roles and training assignments (0.14.n)
    task_req_stability=0    ## stability requiered to perform all roles and training assignments (0.14.n)

##==========squirrel: end added section====================================

    psychocore_stability_decay_mult=1.0
    part_damage_mult=1.0
    xp_mult=1

    status_screen="status_sexbot"
    status_side_screen="status_side_sexbot"

    notify_xp_granted=True
    notify_level_changed=True
    notify_stat_learned=True
    notify_stat_unlearned=True

    notify_chassis_part_integrity_changed=True
    notify_chassis_part_defect_added=True

    notify_trait_gained=True
    notify_trait_lost=True

    default_stats=[
      ["autonomy",None,0],
      ]

    def __init__(self,*args,**kwargs):
      super(SexBot,self).__init__(*args,**kwargs)
      self.chassis=BotChassis(self)
      self.psychocore=BotPsychoCore(self)
      self.roles=[]

    @property
    def base_price(self):
      return int(round(base_bot_model_prices[self.rate.upper()]*self.price_mult))

    @property
    def rate_level(self):
      return "FEDCBAS".index(self.rate.upper())+1

    def role_tag_efficiency(self,tag):
      bot_roles_tags={}
      for cur_role in self.roles:
        for role_tag,efficiency in cur_role.role_tags.items():
          bot_roles_tags[role_tag]=max(bot_roles_tags.get(role_tag,0),efficiency)
      return bot_roles_tags.get(tag,0)

    @property
    def do_not_sell(self):
      return self["do_not_sell"]
    @do_not_sell.setter
    def do_not_sell(self,dns):
      self["do_not_sell"]=bool(dns)

## INSERTED ON 0.7.n FOR THE 'mission_manager' BOT ROLE
    @property
    def allow_manage(self):
      return self["allow_manage"]
    @allow_manage.setter
    def allow_manage(self,mgr_allow):
      self["allow_manage"]=bool(mgr_allow)
## END INSERTED

    def has_role(self,role):
      for cur_role in self.roles:
        if cur_role is role or cur_role.id==role:
          return True
      return False
    def can_add_role(self,role):
      if self.action_allowed("change_role"):
        if isinstance(role,str):
          role=find_bot_role_cls(role)(owner=self)
        if len(self.roles)>=self.psychocore.max_roles:
          return False
        for cur_role in self.roles:
          if cur_role.id==role.id:
            return False
        if not role.can_add(self):
          return False
        return role
      return False
    def can_remove_role(self,role):
      if self.action_allowed("change_role"):
        for cur_role in self.roles:
          if cur_role is role or cur_role.id==role:
            if cur_role.can_remove(self):
              return cur_role
      return False
    def add_role(self,role):
      if isinstance(role,str):
        role=find_bot_role_cls(role)(owner=self)
      self.roles.append(role)
    def remove_role(self,role):
      for cur_role in self.roles:
        if cur_role is role or cur_role.id==role:
          self.roles.remove(cur_role)
          return cur_role
    def action_allowed(self,action):
      rv=True
      for role in self.roles:
        if role.allowed_actions is not None:
          rv=rv and (action in role.allowed_actions)
        elif role.blocked_actions is not None:
          rv=rv and (action not in role.blocked_actions)
      return rv
    def roles_actions(self):
      rv=[]
      for role in self.roles:
        role_actions=role.interact_actions
        if callable(role_actions):
          role_actions=role_actions()
        if isinstance(role_actions,(list,tuple)):
          for condition,action,action_info in role_actions:
            if callable(condition):
              condition=condition()
            elif isinstance(condition,str):
              condition=eval(condition,{"bot":self})
            if condition:
              rv.append((action,action_info))
      return rv

    def model_calc_effective_xp(self,stat,xp):
##      print "start specialist function, xp = ",xp
      if xp>0:
        if stat.id!="autonomy":
##          print "stat isn't autonomy"
          xp_mult=self.xp_mult
          if isinstance(xp_mult,dict):
##            print "xp_mult has a dict"
##            print "looking for stat.id: ",stat.id
            xp_mult=xp_mult.get(stat.id)
          if isinstance(xp_mult,str):
##            print "xp_mult has a str which is stat.id"
            xp_mult=eval(xp_mult,{"bot":self,"stat":stat,"xp":xp})
          if xp_mult:
##            print "a value for xp_mult was found"
            xp=xp*xp_mult
##      print "end specialist function, xp = ",xp
      return xp

    def on_calc_effective_stat(self,stat,level):
      level=self.chassis.calc_effective_stat(stat,level)
      level=self.psychocore.calc_effective_stat(stat,level)
      return level
    def on_calc_effective_xp(self,stat,xp):
      xp=xp*game.bot_xp_rate(self,stat,xp)
      xp=self.model_calc_effective_xp(stat,xp)
      xp=self.chassis.calc_effective_xp(stat,xp)
      xp=self.psychocore.calc_effective_xp(stat,xp)
      return xp
    def on_calc_effective_part_damage(self,part,damage):
      damage=self.chassis.calc_effective_part_damage(part,damage)
      damage=self.psychocore.calc_effective_part_damage(part,damage)
      return damage
    def on_calc_effective_stability_decay(self,decay):
      decay=self.chassis.calc_effective_stability_decay(decay)
      decay=self.psychocore.calc_effective_stability_decay(decay)
      return decay

    def on_time_advanced(self):
      if self["mission"] and self["mission_timer"]<=0:
        queue_event("mission_finished",self.id)

init -4 python:
  modded_bot_model_classes={}

  class ModdedSexBot(SexBot):
    do_not_register=True
    name_variants=name_tables["european_names"]
    default_traits=[]
    list_target_chances={}
    list_target_tag_chances={}
    generate_bot_mind_table="default"

    def init(self,*args,**kwargs):
      for slot,part in self.default_parts.items():
        self.chassis[slot]=part
      self.name=randchoice(self.name_variants)
      for trait in self.default_traits:
        self.psychocore.add_trait(trait)

init python hide:
  @event_handler("generate_bot")
  def list_modded_bots(models,target,tags):
    for model_id,model_cls in modded_bot_model_classes.items():
      target_weight=model_cls.list_target_chances.get(target)
      if target_weight is not None:
        models.append((model_id,target_weight))
        continue
      max_tag_weight=0
      for tag in tags:
        tag_weight=model_cls.list_target_tag_chances.get(tag) or 0
        if tag_weight>max_tag_weight:
          max_tag_weight=tag_weight
      if max_tag_weight>0:
        models.append((model_id,max_tag_weight))

  @event_handler("generate_bot_mind")
  def generate_modded_bot_mind(bot,target,default_table):
    if isinstance(bot,ModdedSexBot):
      mind_table=bot.generate_bot_mind_table
      if mind_table=="default":
        mind_table=default_table
      default_generate_bot_mind(bot,mind_table)

init 90 python:
  def load_bot_models_from_mods():
    bots_info=load_info_table_from_mods("bot_models","model_id")
    for model_id,bot_model in sorted(bots_info.items()):
      if bot_model:
        bot_cls_name="SexBot_"+model_id
        bot_cls_id="_"+model_id
        bot_cls_dct={"id":bot_cls_id}
        bot_cls_dct.update(bot_model)
        name_variants=bot_cls_dct.get("name_variants")
        if isinstance(name_variants,str):
          bot_cls_dct["name_variants"]=name_tables.get(name_variants,"european_names")
        bot_cls=type(bot_cls_name,(ModdedSexBot,),bot_cls_dct)
        slots=[find_item_slot(("" if slot.startswith("bot_") else "bot_")+slot) for slot in bot_cls.default_parts.keys()]
        slots=[slot for slot in slots if slot is not None]
        slots.sort(key=lambda slot: slot.list_priority)
        bot_cls.default_outfit_slots=[slot.id for slot in slots]
        setattr(store,bot_cls_name,bot_cls)
        modded_bot_model_classes[bot_cls_id]=bot_cls
        if log_modded_entries():
          print("Loaded modded bot model:",model_id)

  load_bot_models_from_mods()
