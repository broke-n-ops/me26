style game_mods_text:
  first_indent 60
  newline_indent True

screen game_mods():
  style_prefix "game_mods"
  tag menu
  $system_mods_priority_threshold=game_tunings["system_mods_priority_threshold"]
  use game_menu(scroll=True,right_panel="game_mods_right_panel"):
    vbox:
      xsize content_width
      xalign 0.5
      null height 32
      label "Game mods" xalign 0.5
      use vdiv
      text "List of loaded (and failed to load) mods, sorted by priority. Only user mods are listed."
      $user_mods=[mod for mod in game_mods if mod.get("mod_priority",0)>system_mods_priority_threshold]
      $system_mods=[mod for mod in game_mods if mod.get("mod_priority",0)<=system_mods_priority_threshold]
      if user_mods:
        for mod in reversed(user_mods):
          use vdiv
          $failed=bool(mod["mod_loading_error"])
          text "Mod id: "+("{bad}" if failed else "{mark}")+str(mod["mod_id"])+"{/}"
          text "{size=-4}{info}Mod filename:{/} {mark}"+str(mod["mod_filename"])+"{/}{/}"
          if failed:
            text "{size=-4}{info}Error:{/} {bad}"+str(mod["mod_loading_error"])+"{/}{/}"
          elif mod.get("mod_description"):
            text "{size=-4}{info}Description:{/} "+mod["mod_description"]+"{/}"
          else:
            text "{size=-4}{info}Description:{/} {hint}no description found{/}{/}"
      else:
        use vdiv
        text "{info}No user mods founds. Unzip/copy mods content to {mark}/game/mods/{/} folder.{/}"
      null height 32

style game_mods_right_text:
  xalign 0.5
  text_align 0.5

screen game_mods_right_panel(in_main_menu=False):
  style_prefix "game_mods_right"
  side "c":
    xsize 384
    yfill True
    spacing 8
    use ui_frame:
      fixed:
        vbox:
          align (0.5,0.5)
          text "Want to mod this game?"
          use vdiv
          text "Check instructions here:"
          text "{size=-4}{mark}/game/mods/modding.txt{/}{/}"
          use vdiv
          text "You can add new bot models, bot parts and defects, replace existing art and more!"
          use vdiv
          text "Discord server may have more info and some helpful people."
