default workshop_storage_page=0
default remember_current_bot=None    ## 0.12.8 remember bot to go back to after interacting with a bot in storage
default interacting_from_storage=0   ## 0.12.8 flag know that you are interacting with a bot in storage

label workshop_storage:

  $game_bg="workshop bg_storage"

  header "[workshop] - Bot Storage"
  "You go to the storage room and check the stored bots."  ##  NO PICTURE OF STORAGE ROOM, SHOULD I??
  "{size=-16} "
  $act.add_screen("workshop_storage")
  if workshop.max_sexbots//workshop_sexbots_storage_upgrade_space>1:
    choice(">>>workshop_storage_prev_page",pos=12,key="z") "Prev railing"
    choice(">>>workshop_storage_next_page",pos=13,key="x") "Next railing"
  else:
    choice(None,pos=12,key="z") "Prev railing"
    choice(None,pos=13,key="x") "Next railing"
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label workshop_storage_prev_page:
  $workshop_storage_page=(workshop_storage_page-1)%(workshop.max_sexbots//workshop_sexbots_storage_upgrade_space)
  return "<<<"

label workshop_storage_next_page:
  $workshop_storage_page=(workshop_storage_page+1)%(workshop.max_sexbots//workshop_sexbots_storage_upgrade_space)
  return "<<<"

label workshop_storage_move_to_capsule(bot_n):
  $bot_n=int(bot_n)
  $move_sexbot(workshop.sexbots[bot_n],home)
  return "<<<"

label workshop_storage_interact(bot_id):
  $remember_current_bot=current_side_info_bot    ## 0.12.8 remember current bot to go back to it
  $interacting_from_storage=1                    ## 0.12.8 flag to know you are interacting from storage
  $bot=find_character(bot_id)
  if bot.chassis.is_disabled:
    "You move {mark}[bot]{/} over to the workshop and plug [bot.himher] in. Unfortunately [bot.heshe] is disabled and inactive."
  else:
    "You move {mark}[bot]{/} over to the workshop and plug [bot.himher] in. Soon [bot.heshe] is fully online."
  ""
  $bot=None
  return "begin_bot_interaction:"+bot_id


## 0.14 trying to make it possible to move bots around in storage

label workshop_storage_move_up(bot_n):
  $bot_n=int(bot_n)
  $bot_n_to=(bot_n-1)%len(workshop.sexbots)
  $workshop.sexbots[bot_n],workshop.sexbots[bot_n_to]=workshop.sexbots[bot_n_to],workshop.sexbots[bot_n]
  return "<<<"

label workshop_storage_move_down(bot_n):
  $bot_n=int(bot_n)
  $bot_n_to=(bot_n+1)%len(workshop.sexbots)
  $workshop.sexbots[bot_n],workshop.sexbots[bot_n_to]=workshop.sexbots[bot_n_to],workshop.sexbots[bot_n]
  return "<<<"
