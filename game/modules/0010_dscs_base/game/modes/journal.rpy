init python:
  def label_mode_journal_action_info(**kwargs):
    rv={}
    journal_page=kwargs["action"].lstrip("~<> ").partition(":")[2]
    rv["selected_if"]=game.current_mode=="journal" and journal_page in (store.journal_page,"")
    rv["sensitive_if"]="$not game.current_mode or game_current_label_type=='sub_mode'"
    return rv

label mode_journal(page=None):
  $game.current_mode="journal"
  $journal_page=page or "quests"
  $set_interaction("mode_journal")
  $act.data["journal_page"]=journal_page
  return
