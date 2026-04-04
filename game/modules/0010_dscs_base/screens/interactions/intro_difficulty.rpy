screen interaction_intro_info_difficulty_easy(act_data):
  vbox:
    text ""
    use info_row("Difficulty:","{mark}Easy{/}")
    text ""
    text "Do you just want to relax and have fun?" xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- {mark}debt: $250,000{/}"
      text "- {mark}interest: 1.00% per week{/}"
      text "- {mark}60 character points{/}"
      text "- you gain xp faster"
      text "- bots gain xp faster"
      text "- starting weekly expenses: $3,000"
      text "- good events happens more often"
      text "- more information will be visible"

screen interaction_intro_info_difficulty_normal(act_data):
  vbox:
    text ""
    use info_row("Difficulty:","{mark}Normal{/}")
    text ""
    text "Do you want some challenges to overcome while still having fun?" xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- {mark}debt: $500,000{/}"
      text "- {mark}interest: 1.00% per week{/}"
      text "- {mark}40 character points{/}"
      text "- you gain xp at average rate"
      text "- bots gain xp at average rate"
      text "- starting weekly expenses: $6,000"
      text "- average weekly expenses"

screen interaction_intro_info_difficulty_hard(act_data):
  vbox:
    text ""
    use info_row("Difficulty:","{mark}Hard{/}")
    text ""
    text "Do you want to have a lot of challenges to overcome?" xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- {mark}debt: $800,000{/}"
      text "- {mark}interest: 1.25% per week{/}"
      text "- {mark}24 character points{/}"
      text "- you gain xp slower"
      text "- bots gain xp slower"
      text "- starting weekly expenses: $9,000"
      text "- good events happens less often"

screen interaction_intro_info_difficulty_hardcore(act_data):
  vbox:
    text ""
    use info_row("Difficulty:","{bad}HARDCORE!{/}")
    text ""
    text "Do you want to make your life difficult just to get bragging rights?" xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- {mark}debt: $1,000,000{/}"
      text "- {mark}interest: 1.50% per week{/}"
      text "- {mark}10 character points{/}"
      text "- you gain xp much much slower"
      text "- bots gain xp much slower"
      text "- starting weekly expenses: $12,000"
      text "- good events are rare"
      text "- some information will be hidden, you will have to remember things yourself"
      text "- repeat actions usually not available (can be changed in settings)"
