init -100 python:
  automatic_bot_traits_by_id={}

  bot_traits_cls_by_id={}

  def find_bot_trait_cls(bot_trait_cls_id):
    return bot_traits_cls_by_id.get(bot_trait_cls_id)

  class BotTraitMeta(type):
    def __init__(cls,name,bases,dct):
      if "id" not in dct:
        cls.id=name[9:] if name.lower().startswith("bottrait_") else name
      if not dct.get("do_not_register",False):
        bot_traits_cls_by_id[cls.id]=cls
        if cls.automatic:
          automatic_bot_traits_by_id[cls.id]=cls
    def __str__(cls):
      return cls.name

  class BotTrait(object,metaclass=BotTraitMeta):
    do_not_register=True
    name="bot trait"
    description="- bot trait description -"
    category=None
    hidden=False
    inherent=False
    evolve_into=None
    devolve_into=None
    replace_traits=[]
    trait_type=None
    automatic=None
    repair_skills=[("computers",100)]
    difficulty=1.0
    notify_trait_gained=True
    notify_trait_lost=True
    def __init__(self,*args,**kwargs):
      super(BotTrait,self).__init__()
      self.owner=kwargs.get("owner")
      self.progress=kwargs.get("progress",0)

    def __str__(self):
      return self.name

    @classproperty
    def trait_color(cls):
      return cls.trait_type if cls.trait_type in ("good","bad") else "mark"

    @property
    def owner(self):
      return find_character(self._owner)
    @owner.setter
    def owner(self,owner):
      owner=find_character(owner)
      self._owner=getattr(find_character(owner),"id",None)

    @property
    def progress(self):
      return self._progress
    @progress.setter
    def progress(self,progress):
      self._progress=min(100,max(-100,progress))

    def evolve(self,progress):
      self.progress+=progress
      if self.progress==100:
        if self.evolve_into:
          evolve_into=randwchoice(self.evolve_into)
          if evolve_into!="keep":
            if evolve_into:
              return self.owner.psychocore.add_trait(evolve_into)
      elif self.progress==-100:
        if self.devolve_into:
          devolve_into=randwchoice(self.devolve_into)
          if devolve_into!="keep":
            if devolve_into:
              return self.owner.psychocore.add_trait(devolve_into)
        return self.owner.psychocore.remove_trait(self)
      return self

    def reset(self):
      trait=self
      while trait and not trait.inherent:
        if trait.devolve_into:
          trait=find_bot_trait_cls(randwchoice(trait.devolve_into))
        else:
          trait=None
      if trait:
        if trait is self:
          return self
        else:
          return self.owner.psychocore.add_trait(trait.id)
      else:
        self.owner.psychocore.remove_trait(self)
        return None
