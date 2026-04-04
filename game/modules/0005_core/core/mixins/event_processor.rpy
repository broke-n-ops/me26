init -700 python:
  class EventProcessorMixin(object):
    def process_event(self,event_id,*args,**kwargs):
      if ":" in event_id:
        event_id,rv_pos=event_id.split(":",1)
        rv_pos=int(rv_pos)
        args=list(args)
      else:
        rv_pos=None
      rv=None if rv_pos is None else args[rv_pos]
      for cls in reversed(self.__class__.__mro__):
        handler=cls.__dict__.get("on_"+event_id)
        if callable(handler):
          handler_rv=handler(self,*args,**kwargs)
          if handler_rv is not None:
            rv=handler_rv
          if rv_pos is not None:
            args[rv_pos]=rv
      return rv
