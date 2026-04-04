define label_home_sleep_action_info={"title":"Sleep","cost":[("time",0),"AP+++"]}

label home_sleep:
  $game_bg="home bedroom"
  header "[home] - Bed Time!"
  $mc.energy=0                        ##  added in SR24 version 0.2.0 to force AP to 0 when you go to sleep at night like resting does during the day
  call role_mission_manager_schedule  ## ADDED ON 0.7.n FOR 'Mission Manager' ROLE
  "{size=-16} "
  call home_sleep_bedroom_toys
  call role_shopkeeper_sell_items     ## strangely the function itself doesn't work at night so this call has no effect
  call random_event("home_sleep")
  if _return=="default":
    choice("home_sleep_finish") "Sleep"
  return

label home_sleep_bedroom_toys:
  $assistants=active_bots_with_role_tag("bedroom_toy")
  $assistants_bonus=sum((assistant.bot_sex.level*role_efficiency for assistant,role_efficiency in assistants))
  if assistants:              ## ONE OR MORE BEDROOM TOYS
    $assistant=randchoice(assistants)[0]
    if len(assistants)>1:     ## MORE THAN ONE
      "Time for some fun with {mark}[assistant]{/} and your other bedroom toys!"
    else:                     ## ONLY ONE
      "Time for some fun with {mark}[assistant]{/}, I love having a bedroom toy!"
    $action_image=find_game_image_variant("bots [assistant.model_id] :sex")
    center "{image=[action_image]@800x600}"
    "After a great session you're exhausted and sleep comes easily."
    call break_warranty_seals(assistant,by_mc=True)
    python:
      mc.mood.give_xp(randint(10*assistants_bonus,20*assistants_bonus))
      for assistant,role_efficiency in assistants:
        assistant.give_xp("bot_sex",max(0,randint(-75,10*assistants_bonus)))
    $mc.give_xp("sex",randint(5*assistants_bonus,10*assistants_bonus))
  else:                              ##  NO BEDROOM TOY
    "You toss and turn but finally fall asleep. After a restless sleep you wake up with morning wood!"
    ""
    $hw_imagenumber=random.randint(1,3)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@800x600}"
    ""
    "After taking care of it you decide that you need a bedroom toy!"
    ""
  $assistant=None
  $assistants=None
  return

label home_sleep_finish:
  header "[home] - Sleep"
  
##  in version SR24 0.2.0 moved now.advance() below calling hw_fitness_update and role_housekeeper_clean
  call hw_fitness_update
  $housekeeper_call_from=0         ##  INDICATES CALLED FROM "SLEEP" - a kluge!!
  call role_housekeeper_clean
  call capsule_stability_increase  ## ADDED IN VERSION 0.6.n FOR CAPSULE UPGRADE INCREASING BOT STABILITY

## 0.15.n date relationship loss done in 'update_relationsip_counters' function in 'mc_relationships.rpy' file in '0030-game-functions'
##        warning hints are put into the 'home_reminders.rpy' file in '0020-game-locations-home'
##        removed code from 0.11.3
  call update_relationship_counters

## 0.10.n new function to clear all role delay flags
  call clear_role_delay_flags
## 0.15.n moved resetting rays flags here
  $rays_already_visited=0                              ## reset visit flag for the next day
  $rays_online_bot_list=0                              ## reset flag so new bot list is generated when online store opened

  $now.advance()
  choice("<<<") "Continue"
  return

define label_home_rest_action_info={"title":"Rest","cost":[("time",0),"AP+++"]}

label home_rest:
  if now("morning"):
    $game_bg="squirrel botshop sq_4"
    header "[home] - Resting - Coffee Break"
## rests are segregated into 'morning', 'afternon', and 'evening' with different messages and images

## 'Mission Manager' at beginning of "Rest" to ensure bots cannot execute their roles
    call role_mission_manager_schedule  ## ADDED ON 0.7.n FOR 'Mission Manager' ROLE
    ""                                  ## line feed before next text
    if mc.energy>1:
      "You were anxious to get back to your book so you stopped work early, grabbed some coffee, and enjoyed a long break!"
      $mc.give_xp("mood",randint(35,150))
    elif mc.energy>0:
      "You decided to take your morning coffee break a few minutes early so you have more time to read your book."
      $mc.give_xp("mood",randint(5,50))
    else:
      "You worked hard all morning so you take a few minutes to relax with a cup of coffee and a good book."
##      $mc.give_xp("mood",randint(1,10))    ##deleted mood change when you used all energy in SR24 version 0.2.0
  elif now("afternoon"):
    $game_bg="squirrel botshop sq_5"
    header "[home] - Resting - Nap Time"

## 'Mission Manager' at beginning of "Rest" to ensure bots cannot execute their roles
    call role_mission_manager_schedule  ## ADDED ON 0.7.n FOR 'Mission Manager' ROLE
    ""                                  ## line feed before next text

    if mc.energy>1:
      "You take your afternoon break early today so you can enjoy a long nap."
      $mc.give_xp("mood",randint(35,150))
    elif mc.energy>0:
      "You decide to reward yourself and take a little bit longer nap today."
      $mc.give_xp("mood",randint(5,50))
    else:
      "You've been working all afternoon, it's time for a short nap."
##      $mc.give_xp("mood",randint(1,10))    ##deleted mood change when you used all energy in SR24 version 0.2.0
  else:      ##  MUST BE EVENING
    $game_bg="squirrel botshop sq_6"
    header "[home] - Resting - Game Time!"

## 'Mission Manager' at beginning of "Rest" to ensure bots cannot execute their roles
    call role_mission_manager_schedule  ## ADDED ON 0.7.n FOR 'Mission Manager' ROLE
    ""                                  ## line feed before next text

    if mc.energy>1:
      "You're anxious to get back to your video game so you stop work early to enjoy some serious gaming!"
      $mc.give_xp("mood",randint(35,150))
    elif mc.energy>0:
      "You decide to take your evening break a little early so you can play your video game longer."
      $mc.give_xp("mood",randint(5,50))
    else:
      "You enjoy your favorite video game for a few minutes."
##      $mc.give_xp("mood",randint(1,10))    ##deleted mood change when you used all energy in SR24 version 0.2.0

## 0.12.n new setting in 'Game' to allow a concise display when resting
  if hide_full_description():
##    $notify.disable()
    $notify.disable("stat_xp_granted")
##    $notify.disable("stat_level_changed")
    $notify.disable("stat_learned")
    $notify.disable("stat_unlearned")
    $notify.disable("chassis_part_integrity_changed")
    $notify.disable("chassis_part_defect_added")

  $mc.energy=0
  $housekeeper_call_from=1            ## indicates call made from "home_rest" - a kluge!!
  call role_housekeeper_clean         ## 0.2.2 added housekeeper bot role
  call role_shopkeeper_sell_items
  call role_bot_trainer_train         ## 0.12.n bot trainer role trains other bots, must be before 'master techie'
  call role_senior_techie_repair      ## 0.9.n senior techie role repairs parts in inventory, must be before 'master techie'
  call role_master_techie_repair      ## 0.6.n master techie role repairs other bots
  call capsule_stability_increase     ## 0.6.n capsule upgrade increasing bot stability

## 0.12.n new setting in 'Game' to allow a concise display when resting
  if hide_full_description():
##    $notify.enable()
    $notify.enable("stat_xp_granted")
##    $notify.enable("stat_level_changed")
    $notify.enable("stat_learned")
    $notify.enable("stat_unlearned")
    $notify.enable("chassis_part_integrity_changed")
    $notify.enable("chassis_part_defect_added")

## 0.10.n new function to clear all role delay flags
  call clear_role_delay_flags

  call random_event("home_rest")
  if _return=="default":
  ## ADD IN 0.8.n
    call random_event("good_neighbor")   ## if no 'home_rest' event try for a 'good_neighbor' event
    if _return=="default":               ## if no 'good_neighbor' event advance time - EVENTS MUST END WITH 'advance_time' FUNCTION CALL
      choice("advance_time") "Continue"  ## existing line with altered indentation
  return