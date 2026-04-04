init -10 python:
  class NonExistingBotPart(BotPart):
    do_not_register=True
    rate=None
    rate_level=0
    category_price_mult=0
    price_mult=0
    xp_mult=0
    is_disabled=True
    is_destroyed=False
    integrity=0

  non_existing_bot_part=NonExistingBotPart()

  class BotChassis(object):
    def __init__(self,owner,**kwargs):
      super(BotChassis,self).__init__()
      self.owner=owner

    @property
    def owner(self):
      return find_character(self._owner)
    @owner.setter
    def owner(self,owner):
      self._owner=find_character(owner).id

    @property
    def integrity(self):
      integrity=100
      for slot,part in sorted(self.owner.outfit.items()):
        integrity=min(integrity,(part.integrity if part else 0))
      return integrity

    @property
    def is_disabled(self):
      for slot,part in sorted(self.owner.outfit.items()):
        if not part or part.is_disabled:
          return True
      if self.integrity<=0:
        return True
      return False
    @property
    def has_destroyed_parts(self):
      for part in self.owner.outfit.values():
        if part.is_destroyed:
          return True
      return False
    @property
    def has_irrepairable_parts(self):
      for part in self.owner.outfit.values():
        if part.has_irrepairable_defects:
          return True
      return False
    @property
    def has_defects(self):
      for part in self.owner.outfit.values():
        if part.defects:
          return True
      return False

    @property
    def most_damaged_part(self):
      rv=None,9001
      bot=self.owner
      for slot in bot.outfit_slots:
        part=bot.item_on_slot(slot)
        if part.integrity<rv[1]:
          rv=part,part.integrity
      return rv[0]

    def apply_damage(self,event,base_damage,minimal_integrity=0,silent=False):
      for slot in self.owner.outfit_slots:
        self.apply_part_damage(slot,event,base_damage,minimal_integrity,silent)

    def apply_part_damage(self,slot,event,base_damage,minimal_integrity=0,silent=False):
      slot=find_item_slot(slot)
      slot_damage_mult=slot.event_damage.get(event,0)/100.0
      part=self.owner.item_on_slot(slot)
      if isinstance(base_damage,(list,tuple)):
        damage=randint(base_damage[0],base_damage[1])*slot_damage_mult
      elif isinstance(base_damage,(int,float)):
        damage=base_damage*slot_damage_mult
      else:
        damage=base_damage
      part.apply_damage(damage,minimal_integrity,silent)

    @property
    def cpu(self):
      for slot in self.owner.outfit_slots:
        slot=find_item_slot(slot)
        if "cpu" in slot.slot_tags:
          return self.owner.item_on_slot(slot)
    @property
    def powercore(self):
      for slot in self.owner.outfit_slots:
        slot=find_item_slot(slot)
        if "powercore" in slot.slot_tags:
          return self.owner.item_on_slot(slot)

    def __getitem__(self,key):
      slot=key if key.startswith("bot_") else ("bot_"+key)
      if slot in self.owner.outfit_slots:
        return self.owner.item_on_slot(slot)
      return non_existing_bot_part
#      raise AttributeError("Error while accessing bot part: "+str(key))

## revised by squirrel with Radnor's help
    def __setitem__(self,key,value):
      slot=key if key.startswith("bot_") else ("bot_"+key)
      if slot in self.owner.outfit_slots:
        if value:
          if isinstance(value,str):
            if not value.startswith("bot_part_"):
              value="bot_part_"+value
            item_cls=find_item_cls(value)
##            print "slot:",slot,"original 'value':",value,"item class:",item_cls
            if not item_cls:
              value=substitute_for_missing_part(self.owner,slot)
##              print "substitute - value:",value
            value=find_item_cls(value)(owner=self.owner)
            self.owner.add_item(value)
          value.owner=self.owner
          self.owner.equip(value)
        else:
          self.owner.unequip(slot)
        return
      raise AttributeError("Error while setting bot part: "+str(key))
    def calc_effective_stat(self,stat,level):
      ## done in inventory mixin code
      return level
    def calc_effective_xp(self,stat,xp):
      ## done in inventory mixin code
      return xp
    def calc_effective_part_damage(self,part,damage):
      char=self.owner
      damage=int(round(damage*char.part_damage_mult))
      for slot,part in sorted(char.outfit.items()):
        handler=getattr(part,"on_calc_effective_part_damage",None)
        if callable(handler):
          damage=handler(char,part,damage)
      return damage
    def calc_effective_stability_decay(self,decay):
      char=self.owner
      for slot,part in sorted(char.outfit.items()):
        handler=getattr(part,"on_calc_effective_stability_decay",None)
        if callable(handler):
          decay=handler(char,part,decay)
      return decay

## New function OUTSIDE OF 'BotChassis' class by squirrel to support revised function above
  def substitute_for_missing_part(temp_bot,temp_slot):
    if temp_slot=="bot_cpu":              ##CPU
      if temp_bot.rate=="S":
        return "bot_part_sr24_cpu_s"
      elif temp_bot.rate=="A":
        return "bot_part_neurotech7"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_cpu_b"
      elif temp_bot.rate=="C":
        return "bot_part_neurotech4"
      elif temp_bot.rate=="D":
        return "bot_part_sr24_cpu_d"
      elif temp_bot.rate=="E":
        return "bot_part_quadx"
      elif temp_bot.rate=="F":
        return "bot_part_sr24_cpu_f"
    elif temp_slot=="bot_eyes":           ##eyes
      if temp_bot.rate=="S":
        return "bot_part_sr24_eyes_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_eyes_a"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_eyes_b"
      elif temp_bot.rate=="C":
        return "bot_part_sr24_eyes_c"
      elif temp_bot.rate=="D":
        return "bot_part_irida"
      elif temp_bot.rate=="E":
        return "bot_part_ocu7"
      elif temp_bot.rate=="F":
        return "bot_part_sr24_eyes_f"
    elif temp_slot=="bot_vocoder":        ##vocoder
      if temp_bot.rate=="S":
        return "bot_part_sr24_vocoder_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_vocoder_a"
      elif temp_bot.rate=="B":
        return "bot_part_aria"
      elif temp_bot.rate=="C":
        return "bot_part_sr24_vocoder_c"
      elif temp_bot.rate=="D":
        return "bot_part_invox"
      elif temp_bot.rate=="E":
        return "bot_part_sr24_vocoder_e"
      elif temp_bot.rate=="F":
        return "bot_part_sr24_vocoder_f"
    elif temp_slot=="bot_powercore":      ##powercore
      if temp_bot.rate=="S":
        return "bot_part_sr24_powercore_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_powercore_a"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_powercore_b"
      elif temp_bot.rate=="C":
        return "bot_part_zeux5"
      elif temp_bot.rate=="D":
        return "bot_part_nova"
      elif temp_bot.rate=="E":
        return "bot_part_sr24_powercore_e"
      elif temp_bot.rate=="F":
        return "bot_part_sr24_powercore_f"
    elif temp_slot=="bot_arms":           ##arms
      if temp_bot.rate=="S":
        return "bot_part_sr24_arms_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_arms_a"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_arms_b"
      elif temp_bot.rate=="C":
        return "bot_part_arms_composite"
      elif temp_bot.rate=="D":
        return "bot_part_sr24_arms_d"
      elif temp_bot.rate=="E":
        return "bot_part_arms_plastan"
      elif temp_bot.rate=="F":
        return "bot_part_arms_plastic"
    elif temp_slot=="bot_legs":           ##legs
      if temp_bot.rate=="S":
        return "bot_part_sr24_legs_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_legs_a"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_legs_b"
      elif temp_bot.rate=="C":
        return "bot_part_legs_composite"
      elif temp_bot.rate=="D":
        return "bot_part_sr24_legs_d"
      elif temp_bot.rate=="E":
        return "bot_part_legs_plastan"
      elif temp_bot.rate=="F":
        return "bot_part_legs_plastic"
    elif temp_slot=="bot_skin":           ##skin
      if temp_bot.rate=="S":
        return "bot_part_sr24_skin_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_skin_a"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_skin_b"
      elif temp_bot.rate=="C":
        return "bot_part_sr24_skin_c"
      elif temp_bot.rate=="D":
        return "bot_part_hardskin"
      elif temp_bot.rate=="E":
        return "bot_part_ecoskin"
      elif temp_bot.rate=="F":
        return "bot_part_sr24_skin_f"
    elif temp_slot=="bot_vagina":         ##vagina
      if temp_bot.rate=="S":
        return "bot_part_sr24_vagina_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_vagina_a"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_vagina_b"
      elif temp_bot.rate=="C":
        return "bot_part_sr24_vagina_c"
      elif temp_bot.rate=="D":
        return "bot_part_sr24_vagina_d"
      elif temp_bot.rate=="E":
        return "bot_part_sr24_vagina_e"
      elif temp_bot.rate=="F":
        return "bot_part_sr24_vagina_f"
    elif temp_slot=="bot_penis":          ##penis
      if temp_bot.rate=="S":
        return "bot_part_sr24_penis_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_penis_a"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_penis_b"
      elif temp_bot.rate=="C":
        return "bot_part_sr24_penis_c"
      elif temp_bot.rate=="D":
        return "bot_part_sr24_penis_d"
      elif temp_bot.rate=="E":
        return "bot_part_sr24_penis_e"
      elif temp_bot.rate=="F":
        return "bot_part_sr24_penis_f"
    elif temp_slot=="bot_ears":           ##ears
      if temp_bot.rate=="S":
        return "bot_part_sr24_ears_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_ears_a"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_ears_b"
      elif temp_bot.rate=="C":
        return "bot_part_sr24_ears_c"
      elif temp_bot.rate=="D":
        return "bot_part_sr24_ears_d"
      elif temp_bot.rate=="E":
        return "bot_part_sr24_ears_e"
      elif temp_bot.rate=="F":
        return "bot_part_sr24_ears_f"
    elif temp_slot=="bot_implants":       ##implants
      if temp_bot.rate=="S":
        return "bot_part_sr24_implants_s"
      elif temp_bot.rate=="A":
        return "bot_part_sr24_implants_a"
      elif temp_bot.rate=="B":
        return "bot_part_sr24_implants_b"
      elif temp_bot.rate=="C":
        return "bot_part_sr24_implants_c"
      elif temp_bot.rate=="D":
        return "bot_part_sr24_implants_d"
      elif temp_bot.rate=="E":
        return "bot_part_sr24_implants_e"
      elif temp_bot.rate=="F":
        return "bot_part_sr24_implants_f"
    else:
      return "ERROR"