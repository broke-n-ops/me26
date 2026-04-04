screen preferences_system():
  style_prefix "preferences"
  if renpy.variant("pc") or renpy.variant("web"):
    side "c r":
      xfill True
      text "Display" yalign 0.5
      hbox:
        align (1.0,0.5)
        use ui_choice(Preference("display","window"),title="Windowed",size=pref_btn_size,style_suffix="med")
        use ui_choice(Preference("display","fullscreen"),title="Fullscreen",size=pref_btn_size,style_suffix="med")
    null height 16
  side "c r":
    xfill True
    text "Transitions speed" yalign 0.5
    hbox:
      align (1.0,0.5)
      $val=FieldValue(persistent,"transition_speed_factor",range=transition_speed_max-transition_speed_min+0.25,offset=transition_speed_min)
      bar value val yalign 0.75 xsize 400
      fixed:
        xsize 100
        yfit True
        yalign 0.5
        text " "
        if val.get_adjustment().get_value()>transition_speed_max-transition_speed_min:
          text "{size=-4}Instant{/}" align (1.0,0.5)
        else:
          text "{0:.0%}".format(val.get_adjustment().get_value()/2.0+0.5) align (1.0,0.5)
  side "c r":
    xfill True
    text "In-game transitions" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.in_game_transitions",False),title="Disabled",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.in_game_transitions",True),title="Enabled",size=pref_btn_size,style_suffix="med")
  side "c r":
    xfill True
    text "Frames opacity" yalign 0.5
    hbox:
      align (1.0,0.5)
      $val=FieldValue(persistent,"ui_frame_alpha",range=ui_frame_alpha_max-ui_frame_alpha_min,offset=ui_frame_alpha_min)
      bar value val yalign 0.75 xsize 400
      fixed:
        xsize 100
        yfit True
        yalign 0.5
        text " "
        text "{}%".format(100-(val.get_adjustment().get_value()+ui_frame_alpha_min)) align (1.0,0.5)
  null height 32
  for pref_title,pref_id in [("Sound volume","sound"),("Music volume","music"),("Voice/Movie volume","voice")]:
    if getattr(config,"has_"+pref_id,False):
      $vol=Preference(pref_id+" volume")
      side "c r":
        xfill True
        text pref_title yalign 0.5
        hbox:
          align (1.0,0.5)
          bar value vol yalign 0.75 xsize 400
          fixed:
            xsize 100
            yfit True
            yalign 0.5
            text "{0:.0%}".format(vol.get_adjustment().get_value()) xalign 1.0
  side "c r":
    xfill True
    text "Play maximized movie audio" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.play_maximized_movie_audio",False),title="Disabled",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.play_maximized_movie_audio",True),title="Enabled",size=pref_btn_size,style_suffix="med")
## 0.9.2 addition suggested by 'MikasaTanikawa' to create setting for increasing size of images or leave as is - 1 of 1 change
  null height 16
  side "c r":
    xfill True
    text "Maximize images and videos to full screen" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.maximize_to_fullscreen",False),title="Disabled",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.maximize_to_fullscreen",True),title="Enabled",size=pref_btn_size,style_suffix="med")
## end of addition
  null height 32
  side "c r":
    xfill True
    text "Preload assets ({info}requires restart{/})" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.preload_assets",False),title="Disabled",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.preload_assets",True),title="Enabled",size=pref_btn_size,style_suffix="med")
  null height 16
  side "c r":
    xfill True
    text "Time format" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.time_format",None),title="24 hours",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.time_format","12"),title="12 AM/PM",size=pref_btn_size,style_suffix="med")
  null height 16
  side "c r":
    xfill True
    text "Confirm QuickLoad" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.confirm_quick_load",False),title="Disabled",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.confirm_quick_load",True),title="Enabled",size=pref_btn_size,style_suffix="med")
  null height 16
  side "c r":
    xfill True
    text "Limit keyboard navigation to choices" yalign 0.5
    hbox:
      align (1.0,0.5)
      use ui_choice(SetVariable("persistent.force_keyboard_focus",True),title="Disabled",size=pref_btn_size,style_suffix="med")
      use ui_choice(SetVariable("persistent.force_keyboard_focus",False),title="Enabled",size=pref_btn_size,style_suffix="med")
