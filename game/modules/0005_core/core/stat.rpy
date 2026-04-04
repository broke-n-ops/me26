init -100 python:
  import re
  stat_level_name_clear_pattern=re.compile("{.*?}")

  stats_cls_by_id={}

  def find_stat(stat_id):
    if isinstance(stat_id,StatMeta):
      return stat_id
    elif isinstance(stat_id,BaseStat):
      return type(stat_id)
    else:
      return stats_cls_by_id.get(stat_id)

  class StatMeta(type):
    def __init__(cls,name,bases,dct):
      if "id" not in dct:
        cls.id=name[5:] if name.lower().startswith("stat_") else name
      level_names_map={}
      pattern=stat_level_name_clear_pattern
      for n,level_name_variants in enumerate(cls.level_names):
        level=n+cls.min_level
        if not isinstance(level_name_variants,(list,tuple)):
          level_name_variants=[level_name_variants]
        level_names_map[level]=level
        level_names_map[str(level)]=level
        for level_name in level_name_variants:
          level_name=re.sub(pattern,"",level_name).strip()
          level_names_map[level_name]=level
          level_names_map[level_name.lower()]=level
      cls._level_names_map=level_names_map
      if not dct.get("do_not_register",False):
        stats_cls_by_id[cls.id]=cls
    def __str__(cls):
      return str(cls.name)

  class BaseStat(object,metaclass=StatMeta):
    do_not_register=True
    owner_function=staticmethod(find_character)
    id=None
    name="- generic stat -"
    stat_type=None
    hidden=False
    min_level=1
    max_level=5
    default_level=None
    level_names=[str(n) for n in range(min_level,max_level+1)]
    can_learn_from_xp=False
    notify_xp_granted=False
    notify_level_changed=False
    notify_stat_learned=False
    notify_stat_unlearned=False
    xp_to_next_level=[
      1000, # 1->2
      2000, # 2->3
      3000, # 3->4
      4000, # 4->5
      9999, # 5, needed to allow losing xp and down-leveling
      ]
    def __init__(self,owner,level=None,xp=0):
      super(BaseStat,self).__init__()
      self.owner=owner
      self.level=self.default_level if level is None else level
      if isinstance(xp,float):
        self.progress=xp
      else:
        self.xp=xp
    @property
    def owner(self):
      return self.owner_function(self._owner)
    @owner.setter
    def owner(self,owner):
      self._owner=self.owner_function(owner).id
    def give_xp(self,xp,silent=False):
      return self.owner.give_xp(self,xp,silent=silent)
    givexp=give_xp
    @classmethod
    def _normalize_level(cls,level):
      if isinstance(level,BaseStat):
        level=level.level
      return cls._level_names_map.get(level,cls.default_level)
    def __cmp__(self,level):
      level=self._normalize_level(level)
      return self.level-level
    def __str__(self):
      return str(self.name)
    @property
    def level(self):
      return self._level
    @level.setter
    def level(self,level):
      level=self._normalize_level(level)
      self._level=min(self.max_level,max(self.min_level,level))
    @property
    def xp(self):
      return self._xp
    @xp.setter
    def xp(self,xp):
      self._xp=min(self.xp_to_next_level[self.level-self.min_level],max(0,xp))
    def level_name_str(self,level):
      level=self._normalize_level(level)
      level_name=self.level_names[level-self.min_level]
      if isinstance(level_name,(list,tuple)):
        level_name=level_name[0]
      return level_name
    @property
    def level_name(self):
      return self.level_name_str(self.level)
    @property
    def effective_level(self):
      return self.owner.effective_stat(self)
    @property
    def progress(self):
      return self.xp/float(self.xp_to_next_level[self.level-self.min_level])
    @property
    def progress_percent(self):
      progress=int(round(self.progress*100.0))
      if progress==0 and self.xp!=0:
        progress=1
      if progress==100 and self.level!=self.max_level:
        progress=99
      return progress
    @progress.setter
    def progress(self,progress):
      progress=min(1.0,max(0.0,float(progress)))
      self.xp=int(self.xp_to_next_level[self.level-self.min_level]*progress)
