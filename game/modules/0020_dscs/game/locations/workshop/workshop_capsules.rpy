init python:
  sr24_capsules_screen_page=0    ## page number for capsules screen

label workshop_capsules(call_from):
  header "[workshop] - Bot Capsules"
  if call_from=="0":         ## all previous calls
    "You go to the back of the workshop where you keep your bot capsules."
  else:
    "You stay in the back of the workshop where you keep your bot capsules."
  ""
  $act.add_screen("workshop_capsules")
  if sr24_power_level!=1:      ## level 1 is like the original game, no pages needed
    $sr24_capsule_flag=True
    choice(">>>workshop_capsules_previous",pos=12) "Previous"
    choice(">>>workshop_capsules_next",pos=13) "Next"
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label workshop_capsules_move_up(bot_n):
  $bot_n=int(bot_n)
  $bot_n_to=(bot_n-1)%len(home.sexbots)
  $home.sexbots[bot_n],home.sexbots[bot_n_to]=home.sexbots[bot_n_to],home.sexbots[bot_n]
  return "<<<"

label workshop_capsules_move_down(bot_n):
  $bot_n=int(bot_n)
  $bot_n_to=(bot_n+1)%len(home.sexbots)
  $home.sexbots[bot_n],home.sexbots[bot_n_to]=home.sexbots[bot_n_to],home.sexbots[bot_n]
  return "<<<"

label workshop_capsules_move_to_storage(bot_n):
  $bot_n=int(bot_n)
  $move_sexbot(home.sexbots[bot_n],workshop)
  return "<<<"

label workshop_capsules_previous:
  $sr24_capsules_screen_page-=1                     ## decrement page number
  $sr24_capsule_page=sr24_capsules_screen_page      ## SYNC PAGE NUMBERS
  if sr24_capsules_screen_page<0:                   ## from page 0 you must loop
    if len(home.sexbots)<=10:                       ## pages 0,1
      $sr24_capsules_screen_page=1                  ## loop to max page of 1
      $sr24_capsule_page=sr24_capsules_screen_page  ## SYNC PAGE NUMBERS
    elif len(home.sexbots)<=15:                     ## pages 0,1,2
      $sr24_capsules_screen_page=2                  ## loop to max page of 2
      $sr24_capsule_page=sr24_capsules_screen_page  ## SYNC PAGE NUMBERS
    else:                                           ## pages 0,1,2,3
      $sr24_capsules_screen_page=3                  ## loop to max page of 3
      $sr24_capsule_page=sr24_capsules_screen_page  ## SYNC PAGE NUMBERS
  return "<<<"

label workshop_capsules_next:
  $sr24_capsules_screen_page+=1                                ## increment page number
  $sr24_capsule_page=sr24_capsules_screen_page                 ## SYNC PAGE NUMBERS
  if len(home.sexbots)<=10 and sr24_capsules_screen_page>1:    ## pages 0,1
    $sr24_capsules_screen_page=0                               ## loop to page 0
    $sr24_capsule_page=sr24_capsules_screen_page               ## SYNC PAGE NUMBERS
  elif len(home.sexbots)<=15 and sr24_capsules_screen_page>2:  ## pages 0,1,2
    $sr24_capsules_screen_page=0                               ## loop to page 0
    $sr24_capsule_page=sr24_capsules_screen_page               ## SYNC PAGE NUMBERS
  elif sr24_capsules_screen_page>3:                            ## pages 0,1,2,3
    $sr24_capsules_screen_page=0                               ## loop to page 0
    $sr24_capsule_page=sr24_capsules_screen_page               ## SYNC PAGE NUMBERS
  return "<<<"