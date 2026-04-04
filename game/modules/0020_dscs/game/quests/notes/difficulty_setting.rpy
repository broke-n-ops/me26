init python:
  class Quest_show_difficulty_setting(Quest):
    quest_type="note"

    name="Difficulty Setting"

    class phase_1_showsetting:
      description="[sr_game_difficulty]"

    class phase_1000_finished:
      description="Finished"

    class phase_2000_failed:
      description="Failed"