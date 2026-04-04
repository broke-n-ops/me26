init -90 python:
  class InteractionEnding(InteractionDefault):
    id="ending"
    def finalize(self):
      return "interaction_ending",(self.data,),{}
