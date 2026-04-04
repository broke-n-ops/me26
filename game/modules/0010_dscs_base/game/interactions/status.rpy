init -90 python:
  class InteractionStatus(InteractionDefault):
    id="mode_status"
    def finalize(self):
      return "mode_status",(self.data,),{}
