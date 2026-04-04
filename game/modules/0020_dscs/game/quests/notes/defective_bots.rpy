init python:
  class Quest_defective_bots(Quest):
    quest_type="note"
    name="Scavenging Defective Bots"

    class phase_1_showsetting:
      description="I need to look out for bots with defective psychocores. They might be useful for low stress roles but their defect makes them difficult to use for fighting and sex missions."
    class phase_1000_finished:
      description="Finished"

    class phase_2000_failed:
      description="Failed"