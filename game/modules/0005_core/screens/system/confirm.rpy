style confirm_text is cs_center

screen confirm(message,yes_action,no_action):
  style_prefix "confirm"
  modal True
  zorder 200
  add "#000A"
  fixed:
    fit_first True
    align (0.5,0.5)
    use ui_frame(xfill=False,bg="#000C"):
      vbox:
        xsize 800
        null height 32
        text message
        null height 32
        hbox:
          xalign 0.5
          use ui_choice(yes_action,title="Yes")
          use ui_choice(no_action,title="No",key="cancel")
