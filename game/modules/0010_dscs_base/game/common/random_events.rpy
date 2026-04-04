label random_event(event_id,*args,**kwargs):
  $event=get_random_event(event_id,*args,**kwargs)
  if event:
    python:
      if isinstance(event,str):
        event=(event,(),{})
      event,event_args,event_kwargs=event
      args=tuple(event_args)+args
      kwargs.update(event_kwargs)
    call expression event pass (*args,**kwargs)
    return _return
  return "default"

init -100 python:
  random_events_by_event_id={}

  class random_event(object):
    def __init__(self,event_id):
      super(random_event,self).__init__()
      self.event_id=event_id
    def __call__(self,f):
      random_events_by_event_id.setdefault(self.event_id,[]).append(f)
      return f
    
  def get_random_event(event_id,*args,**kwargs):
    labels=[]
    for event in random_events_by_event_id.get(event_id,[]):
      event=event(*args,**kwargs)
      if event:
        label,weight=event
        if weight>0:
          labels.append((label,weight))
    if labels:
      label=randwchoice(labels)
      return label
