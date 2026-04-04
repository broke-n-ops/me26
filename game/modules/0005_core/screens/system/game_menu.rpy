screen game_menu(title=None,scroll=None,yinitial=0.0,in_main_menu=False,left_panel="game_menu_left_panel",right_panel="game_menu_right_panel"):
  add "menu_bg"
  hbox:
    align (0.5,0.5)
    ysize (1080-32)
    spacing 8
    $renpy.use_screen(left_panel,in_main_menu)
    side "c b":
      xsize 1108
      yfill True
      spacing 8
      if scroll:
        use ui_frame(scroll=True):
          use ui_scrollbox(main_viewport=True):
            transclude
      else:
        use ui_frame(scroll=False):
          fixed:
            transclude
      use game_menu_choices(in_main_menu)
    $renpy.use_screen(right_panel,in_main_menu)
