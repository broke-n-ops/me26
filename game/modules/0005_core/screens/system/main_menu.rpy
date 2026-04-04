style main_menu_text is cs_center

style main_menu_title is main_menu_text:
  size 64

screen main_menu():
  style_prefix "main_menu"
  tag menu
  add "menu_bg"
  use game_menu(in_main_menu=True):
    vbox:
      align (0.5,0.5)
      text "Welcome to"
      use vdiv
      text "[game_name]" style "main_menu_title"
      use vdiv
      text "version [config.version]"
      text ""
      text "{size=24}(A fork of SR24 by Squirrel24){/}"
      text "{size=24}(A variant of Defective Sexbot Chop Shop by Radnor){/}"
      text ""
      text ""
      text "Check out Discord!"
