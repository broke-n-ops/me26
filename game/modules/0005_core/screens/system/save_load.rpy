default persistent.confirm_quick_load=True

screen load():
  tag menu
  use file_slots("Load Game",loading=True)

screen save():
  tag menu
  python:
    if not renpy.predicting():
      try:
        int(persistent._file_page)
      except:
        persistent._file_page="1"
  use file_slots("Save Game",loading=False)

style save_title is cs_header

style save_page_name is cs_center:
  layout "nobreak"

style save_slot_time:
  align (0.5,0.95)
  size 28

style save_slot_message is default:
  align (0.5,0.5)
  color "#666"

screen file_slots(title,loading=False):
  style_prefix "saveload"
  default page_name_value=FilePageNameInputValue(pattern="Page {}",auto="Automatic saves",quick="Quick saves")
##  $slot_btn_size=(config.thumbnail_width//2,56)
  $slot_btn_size=(config.thumbnail_width//3+18,56)  ## 0.11.3 reduce size of slot buttons for asthetics only
##  $page_btn_size=(137,56)
  $page_btn_size=(91,61)                            ## 0.11.3 reduce size of page buttons to add 4, saves was 36 now 60
  use game_menu():
    fixed:
      vbox:
        xalign 0.5
        null height 32
        text title style "save_title"
        text page_name_value.get_text() style "save_page_name"
        use vdiv
        use vdiv
        use vdiv
        grid 3 2:
          xalign 0.5
          xspacing 16
          yspacing 16
          for slot in range(1,7):
            python:
              slot_valid=FileLoadable(slot)
              slot_depricated=not slot_valid or version_number(FileJson(slot,"_version"))<minimal_supported_version
              slot_details="$save_slot_details:"+str(slot) if slot_valid else ""
            use ui_frame(xfill=False):
              vbox:
                null height 6
                use frame_border:
                  button:
                    keyboard_focus False
                    xysize (config.thumbnail_width,config.thumbnail_height)
                    if slot_valid:
                      add FileScreenshot(slot) align (0.5,0.5)
                      if slot_depricated:
                        text "{color=#A00}Unsupported\nsave version{/}" style "save_slot_message"
                    else:
                      add "#6668"
                      text "Empty Slot" style "save_slot_message"
                    if slot_valid:
                      key "save_delete" action FileDelete(slot)
                    if loading:
                      if slot_valid and not slot_depricated:
                        action [SelectedIf(False),FileAction(slot)]
                    else:
                      action [SelectedIf(False),FileAction(slot)]
                    if persistent.time_format=="12":
                      $slot_datetime=FileTime(slot,format="%Y-%m-%d - %I:%M %p")
                    else:
                      $slot_datetime=FileTime(slot,format="%Y-%m-%d - %H:%M")
                    add FitTextDisplayable(slot_datetime,"idle","save_slot_time",(config.thumbnail_width-16,config.thumbnail_height)) align (0.5,0.95)
#                    text slot_datetime style "save_slot_time"
                null height 4
                hbox:
                  xalign 0.5
                  if loading:
                    use ui_choice(None if not slot_valid or slot_depricated else [SelectedIf(False),FileAction(slot)],title="Load",size=slot_btn_size,style_suffix="med")
                  elif slot_valid:
                    use ui_choice([SelectedIf(False),FileAction(slot)],title="Overwrite",size=slot_btn_size,style_suffix="med")
                  else:
                    use ui_choice([SelectedIf(False),FileAction(slot)],title="Save",size=slot_btn_size,style_suffix="med")
                  use ui_choice([SelectedIf(False),FileDelete(slot)],title="Delete",size=slot_btn_size,style_suffix="med")
                null height 2
      hbox:
##        align (0.5,1.0)
        align (0.5,0.98)   ## 0.11.3 move buttons up to adjust for their height reduction
        use ui_choice((FilePage("auto") if loading else None),title="Auto",size=page_btn_size,style_suffix="med")
        use ui_choice((FilePage("quick") if loading else None),title="Quick",size=page_btn_size,style_suffix="med")
##        for page_n in range(1,7):
        for page_n in range(1,11):   ## 0.11.3 add 4 more pages of saves, was 6x6=36, is 6x10=60
          use ui_choice(FilePage(str(page_n)),title="Page {}".format(page_n),size=page_btn_size,style_suffix="med")
