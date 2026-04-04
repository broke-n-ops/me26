init python:
  def label_enter_mode_action_info(**kwargs):
    action=kwargs["action"]
    target=action.lstrip("~<> ").partition(":")[2].strip()
    kwargs["action"]=target
    rv=choice_info(**kwargs)
    rv["action"]=action
    if game.current_mode:
      rv["action"]=None
    return rv

label enter_mode(mode_label):
  $process_event("enter_mode",mode_label)
  $save_premode_interaction()
  return mode_label

init python:
  def label_leave_mode_action_info():
    rv={}
    rv["title"]="Return"
    if game.current_mode is None or game_current_label_type!="sub_mode":
      rv["action"]=None
    return rv

label leave_mode:
  $game.current_mode=None
  $replay_premode_interaction()
  return
