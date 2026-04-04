init python:
  class Quest_ufc_too_many_losses(Quest):
    quest_type="note"
    name="Underground Fight Club"

    class phase_1_showsetting:
      description="The club owner will not buy bots with more than 5 losses."

    class phase_1000_finished:
      description="Finished"

    class phase_2000_failed:
      description="Failed"