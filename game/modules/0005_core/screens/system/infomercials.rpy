define infomercials_change_time=0.5
define infomercials_exposure_time=5.0

init python:
  def update_infomercials():
    global previous_infomercial
    global current_infomercial
    global infomercials_change_pending
    global infomercials_counter
    if infomercials_change_pending or not current_infomercial:
      infomercials_change_pending=False
      previous_infomercial=current_infomercial
      infomercials=list({s[0] for s in renpy.display.screen.screens if s[0].startswith("infomercial_")})
      renpy.random.shuffle(infomercials)
      infomercials_count=len(infomercials)
      while infomercials:
        new_infomercial=infomercials.pop()
        if new_infomercial not in seen_infomercials:
          break
      seen_infomercials.append(new_infomercial)
      while len(seen_infomercials)>max(1,infomercials_count//2):
        seen_infomercials.pop(0)
      current_infomercial=new_infomercial
      infomercials_counter+=1

  def infomercials_animation_finished(tf,st,at):
    if not renpy.predicting():
      if str(GetTooltip()).startswith("{#infomercial}"):
        return 1.0
      store.infomercials_change_pending=True
      renpy.restart_interaction()

transform tf_infomercial_hide(tag):
  alpha 1.0
  linear infomercials_change_time alpha 0

transform tf_infomercial_show(tag):
  alpha 0
  linear infomercials_change_time alpha 1.0
  infomercials_exposure_time
  function infomercials_animation_finished

define seen_infomercials=[]
define infomercials_change_pending=True
define previous_infomercial=None
define current_infomercial=None
define infomercials_counter=0

style infomercial_text is cs_center

screen infomercials():
  style_prefix "infomercial"
  if not renpy.predicting():
    $update_infomercials()
  button:
    keyboard_focus False
    tooltip "{#infomercial}"
    action NullAction()
    frame:
      xfill True
      yfill True
      padding (16,16)
      clipping True
      if previous_infomercial:
        fixed:
          fit_first True
          align (0.5,0.5)
          at tf_infomercial_hide("{}#{}".format(previous_infomercial,infomercials_counter))
          $renpy.use_screen(previous_infomercial)
      if current_infomercial:
        fixed:
          fit_first True
          align (0.5,0.5)
          at tf_infomercial_show("{}#{}".format(current_infomercial,infomercials_counter))
          $renpy.use_screen(current_infomercial)
