transform tf_notify:
  xalign 0.5
  yoffset -4
  on show:
    alpha 0
    linear 0.25 alpha 1.0
  on hide:
    linear 0.5 alpha 0.0

style notify_frame:
  padding (32,8)
  xminimum 400

style notify_text is cs_center:
  color "#AAA"

screen notify(message):
  style_prefix "notify"
  zorder 100
  fixed:
    fit_first True
    at tf_notify
    use ui_frame(False):
      frame:
        text "{mark}[message!tq]{/}"
  timer 3.25 action Hide("notify")
