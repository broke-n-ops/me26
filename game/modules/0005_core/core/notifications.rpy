init -100 python:
  class NotificationsManager(object):
    def __init__(self):
      super(NotificationsManager,self).__init__()
      self.counters={}
    def enable(self,counter=None,delta=1):
      val=self.counters.get(counter,0)-int(delta)
      if val<0:
        raise Exception("Set notification counter for <{}> below zero, likely logical error".format(counter))
      self.counters[counter]=val
    def disable(self,counter=None,delta=1):
      self.counters[counter]=self.counters.get(counter,0)+int(delta)
    def visible(self,counter=None):
      return self.counters.get(None,0)<=0 and self.counters.get(counter,0)<=0
    def reset(self,counter=None):
      self.counters[counter]=0
    def notify(self,message,category=None):
      if self.visible(category):
        if hasattr(act,"notify"):
          message=preprocess_text(message)
          act.notify(message)
    def __call__(self,*args,**kwargs):
      return self.notify(*args,**kwargs)

default notify=NotificationsManager()
