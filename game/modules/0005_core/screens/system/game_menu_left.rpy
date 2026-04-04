style default_game_menu_left_panel_text is cs_center

screen game_menu_left_panel(in_main_menu=False):
  style_prefix "default_game_menu_left_panel"
  side "c":
    xsize 384
    yfill True
    spacing 8
    use ui_frame(ysize=True):
      $btn_size=(250,72)
      side "l c r":
        align (0.5,0.5)
        null width 16
        vbox:
          xfill True
          $pass
          text "Discuss the game or share your ideas?"
          text ""
          text "See if a new version is available?"
          text ""
          use ui_choice(OpenURL(url_discord),title="Discord",hint="Discuss game!",size=btn_size,align=0.5)
          use ui_choice(OpenURL(url_f95zone),title="F95zone",hint="Discuss game!",size=btn_size,align=0.5)
          use ui_choice(OpenURL(url_github),title="GitHub",hint="Report issues or contribute!",size=btn_size,align=0.5)
        null width 16
