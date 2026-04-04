style default:
  font "assets/fonts/Exo2-Regular.ttf"
  color "#FFF"
  size 28
  outlines [(2,"#000")]

style label_text is default:
  font "assets/fonts/Exo2-Regular.ttf"
  color "#FFF"
  size 48

style frame:
  padding (0,0)
  margin (0,0)
  background None

style button:
  margin (0,0)
  padding (0,0)
  background None

style button_text is default:
  font "assets/fonts/Exo2-Regular.ttf"
  size 28
  text_align 0.5
  color "#48F"
  hover_color "#6AF"
  insensitive_color "#666"
  selected_color "#FFF"

style button_disabled is button

style button_disabled_text is button_text:
  color "#666"
  hover_color "#666"

style vscrollbar:
  xsize 20
  base_bar Frame("ui scrollbar vbar",0,24)
  thumb "ui scrollbar vthumb_idle"
  hover_thumb "ui scrollbar vthumb_hover"
  insensitive_thumb "ui scrollbar vthumb_insensitive"
  top_gutter 22
  bottom_gutter 22
  thumb_offset 18
  keyboard_focus False
  unscrollable "hide"

style slider:
  ysize 28
  base_bar Frame("ui slider bar",24,0)
  thumb "ui slider thumb_idle"
  hover_thumb "ui slider thumb_hover"
  insensitive_thumb "ui slider thumb_insensitive"
  left_gutter 10
  right_gutter 10
  thumb_offset 10

style bar is slider
