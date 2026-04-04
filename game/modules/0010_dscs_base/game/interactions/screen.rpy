init -100 python:
  class InteractionShowScreen(Interaction):
    id="screen"
    def __init__(self,screen_name,*args,**kwargs):
      super(InteractionShowScreen,self).__init__()
      self.act_screen=screen_name
      self.act_args=args
      self.act_kwargs=kwargs
    def finalize(self):
      return (self.act_screen,self.act_args,self.act_kwargs)
