init -100 python:
  import datetime

  def time_str(hours,minutes):
    if persistent.time_format=="12":
      return datetime.time(hours,minutes).strftime("%I:%M %p")
    else:
      return datetime.time(hours,minutes).strftime("%H:%M")

  class CurrentDateTime(object):
    def __init__(self,start_day=1,start_tod=0):
      super(CurrentDateTime,self).__init__()
      self.day=start_day
      self.tod=start_tod
    @property
    def dow(self):
      return (self.day-1)%7
    @property
    def dow_name(self):
      return dow_names[self.dow]
    @property
    def dow_short_name(self):
      return dow_short_names[self.dow]
    @property
    def tod_name(self):
      return tod_names[self.tod%len(tod_names)]
    def advance(self,time_to_pass=1):
      while time_to_pass>0:
        skipped_events=store.pending_events
        store.pending_events=[]
        process_skipped_events(skipped_events)
        time_to_pass-=1
        self.tod+=1
        new_day=self.tod>=len(tod_names)
        if new_day:
          self.day+=1
          self.tod=0
        process_event("time_advanced")
        if new_day:
          process_event("new_day")
        process_event("update_state")
    def advance_day(self,days_to_pass=1):
      time_to_pass=days_to_pass*len(tod_names)-self.tod
      self.advance(time_to_pass)
    def __call__(self,*args):
      for arg in args:
        if isinstance(arg,str):
          arg=arg.lower()
          if arg not in (self.tod_name.lower(),self.dow_name.lower(),self.dow_short_name.lower()):
            return False
        elif isinstance(arg,(list,tuple)):
          arg_list=arg
          found=False
          for arg in arg_list:
            if isinstance(arg,str):
              arg=arg.lower()
              if arg in (self.tod_name.lower(),self.dow_name.lower(),self.dow_short_name.lower()):
                found=True
            else:
              if arg==self.day:
                found=True
          if not found:
            return False
        else:
          if arg!=self.day:
            return False
      return True
