style help_text is cs_center

screen help():
  style_prefix "help"
  tag menu
  use game_menu(scroll=True):
    vbox:
      xfill True
      null height 32
      label "Help" xalign 0.5
      use vdiv
      text "how to play"
      null height 32
