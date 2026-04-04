init -10 python:
  class BotPsychoCore(object):
    def __init__(self,owner):
      super(BotPsychoCore,self).__init__()
      self.owner=owner
      self.stability=100
      self._traits=[]
      self._software=[]

    @property
    def owner(self):
      return find_character(self._owner)
    @owner.setter
    def owner(self,owner):
      self._owner=find_character(owner).id

    @property
    def autonomy_cap(self):
      return self.owner.chassis.cpu.rate

    @property
    def max_roles(self):
      return (self.owner.autonomy.level-1)//3+1
    @property
    def max_roles_str(self):
      if self.max_roles==1:
        return str(self.max_roles)+" role"
      else:
        return str(self.max_roles)+" roles"

    @property
    def stability(self):
      return self._stability
    @stability.setter
    def stability(self,stability):
      self._stability=max(0,min(100,stability))

    @property
    def status(self):
      if self.stability<25:
        return "unstable"
      elif self.stability<50:
        return "glitchy"
      elif self.stability<75:
        return "quirky"
      else:
        return "stable"
    @property
    def status_str(self):
      r=(100-self.stability)/100.0
      g=self.stability/100.0
      b=0
      return "{color="+Color(rgb=(r,g,b)).hexcode+"}"+self.status+"{/}"

    @property
    def traits(self):
      rv=self._traits[:]
      for id,trait in sorted(automatic_bot_traits_by_id.items()):
        if callable(trait.automatic):
          if trait.automatic(self.owner):
            rv.append(trait(owner=self.owner))
        elif isinstance(trait.automatic,str):
          if eval(trait.automatic,{"bot":self.owner,"trait":trait}):
            rv.append(trait(owner=self.owner))
        elif trait.automatic:
          rv.append(trait(owner=self.owner))
      return rv
    @traits.setter
    def traits(self,traits):
      self._traits=[trait for trait in traits if not trait.automatic]      

    def has_trait(self,trait_id):
      if not isinstance(trait_id,str):
        trait_id=trait_id.id
      for trait in self.traits:
        if trait.id==trait_id:
          return trait
      return False
    def has_trait_category(self,trait_category):
      for trait in self.traits:
        if trait.category==trait_category:
          return trait
      return False
    def add_trait(self,trait,*args,**kwargs):
      if isinstance(trait,str):
        trait_cls=find_bot_trait_cls(trait)
        if trait_cls:
          trait=trait_cls(*args,owner=self.owner,**kwargs)
        else:
          print("ERROR: invalid trait class - "+trait)
          return
      else:
        trait.owner=self.owner
      replace_traits=trait.replace_traits or []
      traits=[]
      found_place=False
      for cur_trait in self._traits:
        if cur_trait.id in replace_traits or cur_trait.id==trait.id or (trait.category and cur_trait.category==trait.category):
          process_event("trait_lost",self.owner,cur_trait)
          if not found_place:
            traits.append(trait)
            found_place=True
        else:
          traits.append(cur_trait)
      if not found_place:
        traits.append(trait)
      self.traits=traits
      process_event("trait_gained",self.owner,trait)
      return trait
    def remove_trait(self,trait_id):
      rv=None
      if not isinstance(trait_id,str):
        trait_id=trait_id.id
      traits=[]
      for trait in self._traits:
        if trait.id==trait_id:
          process_event("trait_lost",self.owner,trait)
          rv=trait
        else:
          traits.append(trait)
      self.traits=traits
      return rv

    def calc_effective_stat(self,stat,level):
      char=self.owner
      for trait in self.traits:
        handler=getattr(trait,"on_calc_effective_stat",None)
        if callable(handler):
          level=handler(char,stat,level)
      return level
    def calc_effective_xp(self,stat,xp):
      char=self.owner
      for trait in self.traits:
        handler=getattr(trait,"on_calc_effective_xp",None)
        if callable(handler):
          xp=handler(char,stat,xp)
      return xp
    def calc_effective_part_damage(self,part,damage):
      char=self.owner
      for trait in self.traits:
        handler=getattr(trait,"on_calc_effective_part_damage",None)
        if callable(handler):
          damage=handler(char,part,damage)
      return damage
    def calc_effective_stability_decay(self,decay):
      char=self.owner
      decay=int(round(decay*char.psychocore_stability_decay_mult))
      for trait in self.traits:
        handler=getattr(trait,"on_calc_effective_stability_decay",None)
        if callable(handler):
          decay=handler(char,decay)
      return decay

init python hide:
  @event_handler("stat_xp_granted",99)
  def sexbot_psychocore_stability_decay(char,stat,xp):
    if isinstance(char,SexBot):
      if stat.stat_type=="bot_skill":
        if stat.id!="autonomy":
          decay=0
          while xp>0:
            xp_roll=min(100,xp)
            xp-=xp_roll
            if xp_roll>randint(0,200):
              decay+=1
          if decay:
            decay=char.process_event("calc_effective_stability_decay:0",decay)
## 0.9 addition: reduce stability decay as bot skill increases REVISED IN 0.14
## 0.14 changed from fixed percentage per level to a linear transition
##  B at 0% is 10% reduction, at 100% is 20% reduction
##  A at 0% is 20% reduction, at 100% is 40% reduction
##  S at 0% is 40% reduction, at 100% is 90% reduction
##            print "bot: ",char
##            print "stat: ",stat
##            print "stat.level:",stat.level
##            print "stat.progress_percent: ",stat.progress_percent
##            print "decay before:",decay
            if stat.level==5:
##              decay=decay*.9       ## 0.9 version
              decay=decay*(90-(stat.progress_percent*0.1))/100
            elif stat.level==6:
##              decay=decay*.8       ## 0.9 version
              decay=decay*(80-(stat.progress_percent*0.2))/100
            elif stat.level==7:
##              decay=decay*.6       ## 0.9 version
              decay=decay*(60-(stat.progress_percent*0.5))/100
##            print "decay after:",decay
## 0.9 end of addition
            decay=max(1,int(round(decay)))
##            print "decay final:",decay
            char.psychocore.stability-=decay
