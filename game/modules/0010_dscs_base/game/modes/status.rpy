init python:
  def label_mode_status_action_info(**kwargs):
    rv={}
    char_id,sep,status_page=kwargs["action"].lstrip("~<> ").partition(":")[2].partition(",")
    if char_id:
      char=find_character(char_id)
      rv["title"]=char.name
      rv["selected_if"]=game.current_mode=="status" and char.id==store.char_id and status_page in (store.status_page,"")
    else:
      rv["title"]="Status"
      rv["sensitive_if"]="$not game.current_mode or game_current_label_type=='sub_mode'"
      rv["selected_if"]="$game.current_mode=='status'"
    return rv

default last_status_pages={}

init python hide:
  @event_handler("enter_mode")
  def enter_status_mode(mode_label):
    if mode_label.startswith("mode_status"):
      last_status_pages.clear()

label mode_status(status_id="mc,info"):
  $game.current_mode="status"
  $char_id,sep,status_page=status_id.partition(",")
  if not char_id:
    $char_id="mc"
  if not status_page:
    if game.pc==char_id:
      $status_page=last_status_pages.get("mc","info")
    else:
      $status_page=last_status_pages.get("bot","info")
  $last_status_pages["mc" if game.pc==char_id else "bot"]=status_page
  $set_interaction("mode_status")
  $act.data["char"]=char_id
  $act.data["status_page"]=status_page
  return
