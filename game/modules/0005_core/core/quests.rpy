default all_quests={}

default repeatable_quests_counter=0

init -500 python:
  quests_cls_by_id={}

  def find_quest(quest):
    if isinstance(quest,str):
      quest=all_quests.get(quest)
    return quest if isinstance(quest,Quest) else None

  def find_quest_cls(quest_id):
    return quests_cls_by_id.get(quest_id)

  class QuestMeta(type):
    def __new__(cls,name,bases,dct):
      phases={}
      new_dct={}
      for base in bases:
        if hasattr(base,"_phases"):
          phases.update(base._phases)
      for k,v in dct.items():
        if k.startswith("phase_"):
          num_id,str_id=k[6:].split("_",1)
          num_id=int(num_id)
          v.id=str_id
          v.num_id=num_id
          v.original_id=k
          for id in (num_id,str_id):
            if id in phases:
              raise Exception("Duplicate quest phase id: {}, {} clashes with {}".format(name,k,phases[id].original_id))
          force_staticmethod(v,"description")
          force_staticmethod(v,"hint")
          phases[num_id]=v
          phases[str_id]=v
        else:
          new_dct[k]=v
      new_dct["_phases"]=phases
      if "id" not in new_dct:
        new_dct["id"]=name[6:] if name.lower().startswith("quest_") else name
      return type.__new__(cls,name,bases,new_dct)
    def __init__(cls,name,bases,dct):
      set_default_property(cls,"name")
      if not dct.get("do_not_register",False):
        quests_cls_by_id[cls.id]=cls
    def __call__(cls,*args,**kwargs):
      rv=super(QuestMeta,cls).__call__(*args,**kwargs)
      rv.init(*args,**kwargs)
      return rv

  class Quest(FlagsMixin,EventProcessorMixin,GameObject,metaclass=QuestMeta):
    object_type="quest"
    do_not_register=True
    id=None
    name="- generic quest -"
    hidden=False
    repeatable=False
    keep_closed=True
    quest_type="quest"
    def __init__(self,*args,**kwargs):
      super(Quest,self).__init__(*args,**kwargs)
      if self.repeatable:
        store.repeatable_quests_counter+=1
        self.id="{}#{}".format(self.id,repeatable_quests_counter)
      all_quests[self.id]=self
      self.phase=0
      self.started=False
      self.finished=False
      self.failed=False
    def init(self,*args,**kwargs):
      pass
    def remove(self):
      if all_quests.get(self.id) is self:
        all_quests.pop(self.id)
      if self.id in quests_manager.quests_start_order:
        quests_manager.quests_start_order.remove(self.id)
    def __cmp__(self,other):
      other_phase=self._phases.get(other).num_id
      current_phase=self.phase.num_id
      return current_phase-other_phase
    def __eq__(self,other):
      return self.__cmp__(other)==0
    def __str__(self):
      description=getattr(self.phase,"description","")
      if callable(description):
        description=description(self)
      return description
    @property
    def phase(self):
      return self._phases[self._phase]
    @phase.setter
    def phase(self,phase):
      self._phase=self._phases.get(phase,phase).num_id
    @property
    def description(self):
      return str(self)
    @property
    def hint(self):
      hint=getattr(self.phase,"hint","")
      if callable(hint):
        hint=hint(self)
      return hint
    def start(self,start_phase=1):
      if not self.started:
        self.started=True
        self.phase=start_phase
        process_event("quest_started",self)
    def finish(self,finish_phase=1000):
      if not self.finished:
        self.finished=True
        self.phase=finish_phase
        process_event("quest_finished",self)
        if not self.keep_closed:
          self.remove()
    def fail(self,fail_phase=2000):
      if not self.failed:
        self.failed=True
        self.phase=fail_phase
        process_event("quest_failed",self)
        if not self.keep_closed:
          self.remove()
    @property
    def ended(self):
      return self.finished or self.failed
    @property
    def in_progress(self):
      return self.started and not self.ended
    def advance(self,new_phase=None):
      if new_phase is None:
        phases=sorted([v for v in self._phases if isinstance(v,(int,long))])
        cur_phase=phases.index(self.phase.num_id)
        if cur_phase+1<len(phases):
          new_phase=phases[cur_phase+1]
        else:
          return
      elif isinstance(new_phase,str):
        new_phase=self._phases[new_phase].num_id
      if self.phase.num_id!=new_phase:
        self.phase=new_phase
        process_event("quest_advanced",self)
    class phase_0_not_started:
      description=""
      hint=""

  class QuestsManager(object):
    def __init__(self):
      super(QuestsManager,self).__init__()
      self.quests_start_order=[]
    def start_quest(self,quest_id,*args,**kwargs):
      quest=all_quests.get(quest_id)
      if not quest:
        quest=find_quest_cls(quest_id)(*args,**kwargs)
      start_phase=kwargs.get("start_phase",None)
      if start_phase is None:
        quest.start()
      else:
        quest.start(start_phase=start_phase)
      return quest
    def __getattr__(self,name):
      rv=all_quests.get(name)
      if rv is None:
        raise AttributeError("Quest not found: "+str(name))
      return rv

init python hide:
  @event_handler("quest_started")
  def quest_manager_update_quest_order(started_quest):
    if started_quest.id not in quests.quests_start_order:
      quests.quests_start_order.append(started_quest.id)
