init -90 python:
  class InteractionIntro(InteractionDefault):
    id="intro"
    def finalize(self):
      return "interaction_intro",(self.data,),{}
