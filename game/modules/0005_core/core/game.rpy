init -100 python:
  class BaseGame(FlagsMixin,EventProcessorMixin):
    do_not_register=True
    default_pc=None
    start_day=1
    start_time=0
    def __init__(self):
      super(BaseGame,self).__init__()
      self._pc=None
      self.current_label=[None,(),{}]
      self.current_label_type=None
    @property
    def pc(self):
      return find_character(self._pc)
    @pc.setter
    def pc(self,pc):
      pc=find_character(pc)
      self._pc=pc.id if pc else None
    @property
    def location(self):
      return self.pc.location if self.pc else None
    @location.setter
    def location(self,location):
      if self.pc:
        self.pc.location=location
