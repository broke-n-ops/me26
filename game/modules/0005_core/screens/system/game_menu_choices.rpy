screen game_menu_choices(in_main_menu=False):
  use ui_frame:
    python:
      choices=[None]*18
      ## new/save/load
      if main_menu:
        newest_slot=renpy.newest_slot("[^_]")
        if newest_slot:
          if version_number(FileJson(newest_slot,"_version",slot=True))>=minimal_supported_version:
            choices[1]=choice_info([SelectedIf(False),FileLoad(newest_slot,slot=True)],"Continue")
      if main_menu:
        choices[2]=choice_info(Start(),"New Game")
      choices[3]=choice_info(ShowMenu("load"),"Load Game")
      if not main_menu:
        choices[4]=choice_info(ShowMenu("save"),"Save Game")
      choices[6]=choice_info(ShowMenu("about"),"Credits")
      choices[12]=choice_info(ShowMenu("preferences"),"Settings")
      choices[13]=choice_info(ShowMenu("game_mods"),"Game Mods")
      choices[14]=choice_info(ShowMenu("modding_request"),"Modding")
      if main_menu:
        if not in_main_menu:
          choices[16]=choice_info(ShowMenu("main_menu"),"Return",key="cancel")
        if renpy.variant("pc"):
          choices[17]=choice_info(Quit(confirm=not main_menu),"Quit")
      else:
        choices[16]=choice_info(Return(),"Return",key="cancel")
        choices[17]=choice_info(MainMenu(),"Title")
    grid 6 3:
      align (0.5,0.5)
      for choice_n,choice in enumerate(choices):
        use ui_choice(choice)
