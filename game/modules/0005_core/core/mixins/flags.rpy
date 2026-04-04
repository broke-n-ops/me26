init -700 python:
  class FlagsMixin(object):
    default_flag_value=0
    def __init__(self,*args,**kwargs):
      super(FlagsMixin,self).__init__()
      self.flags={}
    def __getitem__(self,name):
      return self.flags.get(name,self.default_flag_value)
    def __setitem__(self,name,value):
      self.flags[name]=value
    def on_time_advanced(self):
      updated_flags={}
      for k,v in self.flags.items():
        if k.endswith("_now"):
          continue
        elif k.endswith("_today") and now.tod==0:
          continue
        elif k.endswith("_timer") and v>0:
          v-=1
        updated_flags[k]=v
      self.flags=updated_flags
