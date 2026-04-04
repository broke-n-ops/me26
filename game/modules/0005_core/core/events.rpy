default pending_events=[]

init -500 python:
  event_handlers_by_event_id={}

  class event_handler(object):
    def __init__(self,event_id,priority=0):
      super(event_handler,self).__init__()
      self.event_id=event_id
      self.priority=priority
    def __call__(self,f):
      event_handlers_by_event_id.setdefault(self.event_id,[]).append((self.priority,f))
      return f

  def queue_event(event_label,*args,**kwargs):
    pending_events.append([event_label,args,kwargs])

  def process_event(event_id,*args,**kwargs):
    handlers=event_handlers_by_event_id.get(event_id,[])
    if kwargs.pop("all_rv",False):
      default_rv=kwargs.pop("default_rv",None)
      rv=[]
      for priority,handler in handlers:
        rv.append(handler(*args,**kwargs))
      if not rv:
        rv=default_rv
    else:
      rv=kwargs.pop("default_rv",None)
      for priority,handler in handlers:
        handler_rv=handler(*args,**kwargs)
        if handler_rv is not None:
          rv=handler_rv
    return rv

  def process_skipped_events(skipped_events):
    while skipped_events:
      event_label,event_label_args,event_label_kwargs=skipped_events.pop(0)
      event_skipped_callback=getattr(store,event_label+"_event_skipped",None)
      if callable(event_skipped_callback):
        event_skipped_callback(event_label,*event_label_args,**event_label_kwargs)

init 9999 python:
  ## finalize event handlers, sorting them by priority
  def finalize_event_handlers():
    rv={}
    for event_id,handlers in event_handlers_by_event_id.items():
      for priority,handler in handlers:
        rv.setdefault(event_id,[]).append((priority,handler))
    for event_id,event_handlers in rv.items():
      rv[event_id].sort(key=lambda x:x[0])
    return rv

  event_handlers_by_event_id=finalize_event_handlers()
