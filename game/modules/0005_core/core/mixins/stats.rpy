init -700 python:
  class StatsMixin(object):
    default_stats=[]
    notify_xp_granted=False
    notify_level_changed=False
    notify_stat_learned=False
    notify_stat_unlearned=False
    def __init__(self,*args,**kwargs):
      super(StatsMixin,self).__init__()
      self.stats={}
      self.stats_order=[]
      for stat_info in self.default_stats:
        self.add_stat(*stat_info)
    def has_stat(self,stat_id):
      stat=find_stat(stat_id)
      if stat and stat.id in self.stats:
        return True
      return False
    def give_xp(self,stat_id,xp=None,raw=False,silent=False):
      notify.disable("stat_xp_granted",silent)
      notify.disable("stat_level_changed",silent)
      if xp is None:
        xp=stat_id
        stat_id=self.default_stat
      if not isinstance(stat_id,str):
        stat_id=find_stat(stat_id).id
      if isinstance(xp,(list,tuple)) and xp[0]=="raw":
        raw,xp=True,xp[1]
      if stat_id.endswith("_raw"):
        raw,stat_id=True,stat_id[:-4]
      stat=find_stat(stat_id)
      if isinstance(xp,str):
        stat_obj=getattr(self,stat_id,None)
        stat_level=getattr(stat_obj,"level",stat.min_level)
        stat_xp=getattr(stat_obj,"xp",0)
        if xp=="next":
          xp=stat.xp_to_next_level[stat_level-stat.min_level]-stat_xp
          raw=True
        elif xp=="prev":
          xp=-stat_xp-stat.xp_to_next_level[stat_level-1-stat.min_level]
          raw=True
        elif xp=="zero":
          xp=-stat_xp
          raw=True
        else:
          xp=eval(xp,globals(),{"char":self,"stat":stat_obj,"level":stat_level,"xp":stat_xp})
        xp=int(xp)
      if stat.id in self.stats or (stat.can_learn_from_xp and xp>0):
        if stat.id not in self.stats:
          self.learn_stat(stat,silent)
        stat=self.stats[stat.id]
        if not raw and hasattr(self,"effective_xp"):
          xp=int(round(self.effective_xp(stat,xp)))
        if xp!=0:
          process_event("stat_xp_granted",self,stat,xp)
          old_level=stat.level
          old_xp=stat.xp
          level=old_level
          if xp>0:
            xp+=old_xp
            while level<stat.max_level:
              needed_xp=stat.xp_to_next_level[level-stat.min_level]
              if xp>=needed_xp:
                level+=1
                xp-=needed_xp
              else:
                break
          elif xp<0:
            xp+=old_xp
            while level>stat.min_level:
              if xp<0:
                level-=1
                xp+=stat.xp_to_next_level[level-stat.min_level]
              else:
                break
          xp=min(max(xp,0),stat.xp_to_next_level[level-stat.min_level])
          stat.level=level
          stat.xp=xp
          if level!=old_level:
            process_event("stat_level_changed",self,stat,old_level,level)
      notify.enable("stat_xp_granted",silent)
      notify.enable("stat_level_changed",silent)
    givexp=give_xp
    def __setattr__(self,name,value):
      stats=self.__dict__.get("stats")
      if stats is not None:
        stat=find_stat(name)
        if stat and stat.id in stats:
          stat=stats[stat.id]
          old_level=stat.level
          level=stat._normalize_level(value)
          level=min(max(level,stat.min_level),stat.max_level)
          if level!=old_level:
            stat.level=level
            stat.xp=0
            process_event("stat_level_changed",self,stat,old_level,level)
          return
      super(StatsMixin,self).__setattr__(name,value)
    def __getattr__(self,name):
      stats=self.__dict__.get("stats")
      if stats is not None:
        stat=find_stat(name)
        if stat:
          if stat.id in stats:
            return stats[stat.id]
          elif stat.default_level is not None:
            return stat(self)
      raise AttributeError("Entity \"{}\" has no defined \"{}\" stat".format(self.id,name))
    def learn_stat(self,stat,silent=False):
      notify.disable("stat_learned",silent)
      stat=find_stat(stat)
      if stat.id not in self.stats:
        stat=self.add_stat(stat.id,None,0)
        process_event("stat_learned",self,stat)
      notify.enable("stat_learned",silent)
    def unlearn_stat(self,stat,silent=False):
      notify.disable("stat_unlearned",silent)
      stat=find_stat(stat)
      if stat.id in self.stats:
        self.remove_stat(stat.id)
        process_event("stat_unlearned",self,stat)
      notify.enable("stat_unlearned",silent)
    def add_stat(self,stat_id,level=None,xp=0):
      stat=find_stat(stat_id)
      if not stat:
        raise Exception("Unknown stat: {}".format(stat_id))
      if stat.id in self.stats:
        stat=self.stats[stat.id]
      else:
        stat=stat(self,level,xp)
        self.stats[stat.id]=stat
        self.stats_order.append(stat.id)
      return stat
    def remove_stat(self,stat_id):
      stat=find_stat(stat_id)
      if not stat:
        raise Exception("Unknown stat: {}".format(stat_id))
      if stat.id in self.stats:
        self.stats.pop(stat.id)
        self.stats_order.pop(self.stats_order.index(stat.id))
    def on_calc_effective_stat(self,stat,level):
      for char_stat_id in self.stats_order:
        char_stat=self.stats[char_stat_id]
        handler=getattr(char_stat,"on_calc_effective_stat",None)
        if callable(handler):
          level=handler(self,stat,level)
      return level
    def on_calc_effective_xp(self,stat,xp):
      for char_stat_id in self.stats_order:
        char_stat=self.stats[char_stat_id]
        handler=getattr(char_stat,"on_calc_effective_xp",None)
        if callable(handler):
          xp=handler(self,stat,xp)
      return xp
