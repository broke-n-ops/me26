init -100 python:
  def transition_time_warp(time):
    sf=persistent.transition_speed_factor
    if sf is not None:
      if sf<=transition_speed_max+0.01:
        time=max(0.0,min(1.0,time*sf))
      else:
        time=1.0 if time>0 else time
    return time

  class TunableDissolve(renpy.display.transition.Dissolve):
    def __init__(self,delay,*args,**kwargs):
      sf=persistent.transition_speed_factor
      if sf is not None:
        if sf<=transition_speed_max+0.01:
          delay=delay/float(sf)
        else:
          delay=0.0
      kwargs.setdefault("time_warp",transition_time_warp)
      super(TunableDissolve,self).__init__(delay,*args,**kwargs)

  Dissolve=renpy.curry(TunableDissolve)

  def do_screens_transition():
    renpy.transition(screen_transition,layer="screens")
    renpy.restart_interaction()
