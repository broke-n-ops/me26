screen preferences_game():
  style_prefix "preferences"
  side "c r":
    xfill True
    text "\"Repeat action\" buttons" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.show_repeat_action","always"),title="Always",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.show_repeat_action",False),title="Disabled",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.show_repeat_action",True),title="Enabled",size=pref_btn_size,style_suffix="med")
  null height 32

## 0.12.n new game setting for 'Rest' and 'Work' to display during time advance: 
  side "c r":
    xfill True
    text "Advance Time Descriptions" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.full_descriptions",True),title="Full",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.full_descriptions",False),title="Concise",size=pref_btn_size,style_suffix="med")
  null height 32


  side "c r":
    xfill True
    text "Log loaded mods" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.log_loaded_mods",False),title="Disabled",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.log_loaded_mods",True),title="Enabled",size=pref_btn_size,style_suffix="med")
  side "c r":
    xfill True
    text "Log modded entries" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.log_modded_entries",False),title="Disabled",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.log_modded_entries",True),title="Enabled",size=pref_btn_size,style_suffix="med")
