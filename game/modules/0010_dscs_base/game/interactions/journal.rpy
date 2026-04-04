init -90 python:
  class InteractionJournal(InteractionDefault):
    id="mode_journal"
    def finalize(self):
      return "mode_journal",(self.data,),{}
