screen interaction_intro_info_skill_combat(act_data):
  vbox:
    text ""
    use info_row("Skill:","{mark}"+find_stat("combat").name+"{/}")
    text ""
    text "Knowledge of how to punch, kick, bash, stab, cut, chop, shoot, suppress, snipe, and generally make things cease existing." xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- allows you to train bots in {mark}"+find_stat("bot_combat").name+"{/}"
      text "- affects hostile events"

screen interaction_intro_info_skill_computers(act_data):
  vbox:
    text ""
    use info_row("Skill:","{mark}"+find_stat("computers").name+"{/}")
    text ""
    text "Knowledge of wide range of computer-related stuff. From programming to navigating GreyNet to hacking hostile turrets." xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- allows you to stabilize bot's PsychoCore"
      text "- allows you to remove unwanted PsychoCore quirks"

screen interaction_intro_info_skill_electronics(act_data):
  vbox:
    text ""
    use info_row("Skill:","{mark}"+find_stat("electronics").name+"{/}")
    text ""
    text "General knowledge of electronical devices, including bots and bot parts." xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- allows you to train bots in {mark}"+find_stat("bot_electronics").name+"{/}"
      text "- allows you to repair electronical bot parts"
      text "- allows you to fix defects of electronical bot parts"

screen interaction_intro_info_skill_mechanics(act_data):
  vbox:
    text ""
    use info_row("Skill:","{mark}"+find_stat("mechanics").name+"{/}")
    text ""
    text "General knowledge of mechanical devices, including bots and bot parts." xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- allows you to train bots in {mark}"+find_stat("bot_mechanics").name+"{/}"
      text "- allows you to repair mechanical bot parts"
      text "- allows you to fix defects of mechanical bot parts"

screen interaction_intro_info_skill_sex(act_data):
  vbox:
    text ""
    use info_row("Skill:","{mark}"+find_stat("sex").name+"{/}")
    text ""
    text "General understanding of how to please yourself and, occasionally, others." xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- allows you to train bots in {mark}"+find_stat("bot_sex").name+"{/}"

screen interaction_intro_info_skill_social(act_data):
  vbox:
    text ""
    use info_row("Skill:","{mark}"+find_stat("social").name+"{/}")
    text ""
    text "General understanding of human interactions, be it communication, seduction, intimidation, or haggling." xalign 0.5 text_align 0.5
    text ""
    vbox:
      style_prefix "intro_info_small"
      text "- allows you to train bots in {mark}"+find_stat("bot_social").name+"{/}"
      text "- allows you to negotiate better prices and deals"
