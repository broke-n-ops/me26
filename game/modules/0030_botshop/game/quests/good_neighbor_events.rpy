## random events related to 'Good Neighbor' quest

## IMPORTANT!
##   RANDOM EVENTS ARE NOT CALLED AT NIGHT SO DON'T USE IT!!
##   AFTERNOONS ARE USED TO HAVE THE MC REMEMBER RUTHIE BEING ATTACKED EARLY IN THE QUEST SO DON'T USE IT!!
##   ONLY USE MORNINGS AND EVENINGS HERE!!

init python hide:
  @random_event("good_neighbor")
  def good_neighbor_none():
    return None,36                    ## 0.8.0 set to 46 - 0.8.1 reduce to 36

  @random_event("good_neighbor")
  def good_neighbor_bot_damaged():
    if now("morning") and quests.goodneighbor.started:
      if gn_damaged_bot_waiting==1:                  ## already a damaged bot waiting, don't build a waiting stack!
        return None,1
      elif gn_which_pair>0 and gn_repairing_bot+gn_damaged_bot_waiting==gn_which_pair:  ## at least 1 damaged bot allowed and sum of in repair and waiting pair equals number allowed, can't have another one
        return None,1
      elif quests.goodneighbor.phase.num_id==1:      ## haven't given any bots yet, no chance of damage
        return None,1
      elif quests.goodneighbor.phase.num_id==2:      ## store owner before diner robbery (no patrol), decided not to have damage here
        return None,1
      elif quests.goodneighbor.phase.num_id==3:      ## store owner after diner robbery (no patrol), decided not to have damage here
        return None,1
      elif quests.goodneighbor.phase.num_id==4:      ## store owner and patrols 1, low chance of damage
        return "good_neighbor_bot_damaged_init",4
      elif quests.goodneighbor.phase.num_id==5:      ## store owner and patrols 1&2, higher chance of damage
        return "good_neighbor_bot_damaged_init",8
      elif quests.goodneighbor.finished:             ## quest finished (can't fail), low chance of damage, thugs are afraid of patrol and avoid it
        return "good_neighbor_bot_damaged_init",4

    return None,1

  @random_event("good_neighbor")
  def good_neighbor_reputation_loss():
    if now("evening") and quests.goodneighbor.started:
      if quests.goodneighbor.phase.num_id==1:              ## haven't given any bots yet, no chance of loss
        return None,1
      elif quests.goodneighbor.phase.num_id==2:            ## store owner before diner robbery (no patrol), small chance of loss
        return "good_neighbor_reputation_loss_init",12
      elif quests.goodneighbor.phase.num_id==3:            ## store owner after diner robbery (no patrol), small chance of loss
        return "good_neighbor_reputation_loss_init",12
      elif quests.goodneighbor.phase.num_id==4:            ## store owner and patrols 1, large chance of loss, patrol visible 2/3 the time (assumption: 8 hrs in capsule, 16 hours on duty)
        return "good_neighbor_reputation_loss_init",16
      elif quests.goodneighbor.phase.num_id==5:            ## store owner and patrols 1&2, less chance of loss, 1 patrol visible 2/3 of the time, 2 patrols visible 1/3 of the time
        return "good_neighbor_reputation_loss_init",8
      elif quests.goodneighbor.finished:                   ## quest finished (can't fail), small chance of loss, 2 patrols visible all the time, thugs rarely around
        return "good_neighbor_reputation_loss_init",4

    return None,1

  @random_event("good_neighbor")
  def good_neighbor_reputation_gain():
    if now("evening") and quests.goodneighbor.started:
      if quests.goodneighbor.phase.num_id==1:              ## haven't given any bots yet, no chance of gain
        return None, 1
      elif quests.goodneighbor.phase.num_id==2:            ## store owner before diner robbery (no patrol), very low chance of gain
        return "good_neighbor_reputation_gain_init",4
      elif quests.goodneighbor.phase.num_id==3:            ## store owner after diner robbery (no patrol), very low chance of gain
        return "good_neighbor_reputation_gain_init",4
      elif quests.goodneighbor.phase.num_id==4:            ## store owner and patrols 1, good chance of gain, patrol visible 2/3 the time (assumption: 8 hrs in capsule, 16 hours on duty)
        return "good_neighbor_reputation_gain_init",12
      elif quests.goodneighbor.phase.num_id==5:            ## store owner and patrols 1&2, great chance of gain, 1 patrol visible 2/3 of the time, 2 patrols visible 1/3 of the time
        return "good_neighbor_reputation_gain_init",24
      elif quests.goodneighbor.finished:                   ## quest finished (can't fail) and patrols 1&2&3, great chance of gain, 2 patrols visible all the time increase but not doubled because people take it for granted
        return "good_neighbor_reputation_gain_init",42
    return None,1

  @random_event("good_neighbor")
  def good_neighbor_repairing_bot():

##    print "gn_repairing_bot: ",gn_repairing_bot
##    print "gn_damaged_bot_waiting: ",gn_damaged_bot_waiting

    if now("evening"):
      if gn_repairing_bot>0 or gn_damaged_bot_waiting==1:  ## 1st iscounter: >0 means there is a bot being repaired - 2nd is flag: 1 means damaged bot waiting for space
        return "good_neighbor_repairing_bot_init",99999    ## overwhelms the normal reputation gain and loss events, makes this event 99.9% when repairing a bot
      else:
        return None,1
    else:
      return None,1

label good_neighbor_bot_damaged_init:
  choice("good_neighbor_bot_damaged") "Continue"
  return

label good_neighbor_reputation_loss_init:
  choice("good_neighbor_reputation_loss") "Continue"
  return

label good_neighbor_reputation_gain_init:
  choice("good_neighbor_reputation_gain") "Continue"
  return

label good_neighbor_repairing_bot_init:
  choice("good_neighbor_repairing_bot") "Continue"
  return

##==========================================================================
## FINAL FUNCTION CALL WHEN THE EVENT IS OVER SHOULD BE: "advance_time"
## EVENT CALLING "Continue" BUTTON DOES THIS AS THE ONLY ACTIVITY AFTERWARDS
##==========================================================================

label good_neighbor_bot_damaged:
  $game_bg="workshop bg"
  $game_bgm="home bgm"
  header "Workshop - An Unexpected Visit"

  $temp_int= random.randint(1,2)                   ## used to select bot gender, must be saved for future use
  if temp_int==1:                                  ## female bot damaged
    $gn_damaged_bot_gender=0                       ## 0 indicates female bot
    $action_image= "quests good_neighbors sgn_50"
  else:                                            ## male bot damaged
    $gn_damaged_bot_gender=1                       ## 1 indicates male bot
    $action_image= "quests good_neighbors sgn_51"
  "{mark}[gn_store_owner_name]{/} came into the shop with a pair of bots, {bad}one of them damaged{/}. She said they fended off the thugs but it was quite a battle. I guess I have some repair work to do."
  ""
  center "{image=[action_image]@720x600}"
  ""
  $mc.give_xp("rep_neighborhood",randint(-50,-10))
  $mc.mood.give_xp(randint(-15,-5))
  choice("gn_receive_damaged_patrol_bot") "Continue"
  return

label good_neighbor_reputation_loss:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  $temp_int= random.randint(47,49)
  $action_image= "quests good_neighbors sgn_"+str(temp_int)
  "Your neighbors see a couple of thugs walking around the neighborhood this evening and they aren't very happy about it."
  if quests.goodneighbor.phase.num_id==2 or quests.goodneighbor.phase.num_id==3:                 ## store owner has bots, others wish they did too
    "They've seen the bots you gave {mark}[gn_store_owner_name]{/} and wish they had bots too."
  ""
  center "{image=[action_image]@750x600}"
  $mc.give_xp("rep_neighborhood",randint(-50,-10))
  if quests.goodneighbor.phase.num_id!=2 and quests.goodneighbor.phase.num_id!=3:  ## no mood loss if patrol hasn't started, only reputation loss
    $mc.mood.give_xp(randint(-15,-5))
  choice("advance_time") "Continue"
  return

label good_neighbor_reputation_gain:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  if quests.goodneighbor.phase.num_id==2:
    $temp_int= 43
  elif quests.goodneighbor.phase.num_id==3:  ## low chance of benefit from people seeing store owner's bots
    $temp_int= 43
  elif quests.goodneighbor.phase.num_id==4:
    $temp_int= random.randint(43,44)
  elif quests.goodneighbor.phase.num_id==5:
    $temp_int= random.randint(43,45)
  elif quests.goodneighbor.phase.num_id>5:
    $temp_int= random.randint(43,46)
  $action_image= "quests good_neighbors sgn_"+str(temp_int)
  if temp_int==43:
    "Your neighbors are very happy to see the bots you gave {mark}[gn_store_owner_name]{/} working in her store this evening."
  else:
    "Your neighbors are happy to see the bot patrol walking around the neighborhood. They keep thugs away and they feel safer."
  ""
  center "{image=[action_image]@750x600}"
  $mc.give_xp("rep_neighborhood",randint(10,50))
  $mc.mood.give_xp(randint(5,15))
  choice("advance_time") "Continue"
  return

label good_neighbor_repairing_bot:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  $temp_int= random.randint(47,49)
  $action_image= "quests good_neighbors sgn_"+str(temp_int)
  if gn_damaged_bot_waiting+gn_repairing_bot>1:              ## more than 1 bot needs repair
    "Thugs are more daring now because the {mark}Neighborhood Patrol{/} is short handed while you're repairing damaged bots. {mark}You need to fix all the bots and put them back to work protecting the neighborhood.{/}"
  else:                                                      ## only 1 bot needs repair
    "Thugs are more daring now because the {mark}Neighborhood Patrol{/} is short handed while you're repairing the damaged bot. {mark}You need to fix the bot and put it back to work protecting the neighborhood.{/}"
  ""
  center "{image=[action_image]@750x600}"
  ""
  $mc.give_xp("rep_neighborhood",randint(-50,-10))
  $mc.mood.give_xp(randint(-15,-5))
  choice("advance_time") "Continue"
  return

## called from 'good_neighbor' event handler (queued) afternoons when building bots for store owner
label good_neighbor_repeat_robbery:                  ## MC needs incentive to build bots for store owner
  $temp_integer=random.randint(1,5)                  ## 20% chance of repeat robbery but next line prevents it from happening more than every 5th day
  if temp_integer==1 and gn_repeat_store_robbed<=0:  ## <= because decrement will keep happening even when reaches 0
    $temp_int= random.randint(1,2)
    if temp_int==1:
      $game_bg="neighborhood nbg_1"
    else:
      $game_bg="neighborhood nbg_2"
    header "Neighborhood"
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_52" 
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests good_neighbors sgn_53"
    center "{image=[action_image]@400x600}"
    ""
    $act.set_block("c")
    " You learn that {mark}[gn_store_owner_name]{/} was beaten and robbed again. You imagine the scene and can't get the picture out of your head. After a while you realize you've been thinking about this long enough and you need to get to work."
    ""
    $mc.energy-=3
    "{bad} Lost 3 AP!{/}"
    $mood_loss=int(-1*abs(mc.mood.xp))
    $mc.mood.give_xp(mood_loss)
    $gn_repeat_store_robbed=4           ## set to 4 here, 5th day can happen again but only 20% chance
  else:
    $game_bg="home bg"
    $game_bgm="home bgm"
    header "[home]"
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_2" 
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests good_neighbors sgn_3"
    center "{image=[action_image]@400x600}"
    ""
    $act.set_block("c")
    "You remember the night you chased away thugs who were robbing {mark}[gn_store_owner_name]'s{/} store. They beat her up badly, who knows what they might do if they come back again. I better stop wasting time and finish the bots I promised her."
    ""    
    $mc.energy-=1
    "{bad} Lost 1 AP!{/}"
    $mood_loss=int(-0.5*abs(mc.mood.xp))
    $mc.mood.give_xp(mood_loss)
    $gn_repeat_store_robbed-=1            ## decrement counter each time repeat robbery doesn't happen, will be reset to 4 at next robbery, robberies can occur when <=0
  choice("<<<") "Continue"
  return

##========  supporting functions for damaged patrol bot =========

label gn_receive_damaged_patrol_bot:                       ## called when bot arrives AND when space IS available when time advances
  $game_bg="workshop bg"
  $game_bgm="home bgm"
  header "Workshop - Store Damaged Patrol Bot"

  if gn_damaged_bot_waiting==1:                            ## bot was waiting for space, none available when arrived
    $gn_damaged_bot_waiting=0                              ## reset flag
    
##    $print "removed bot from waiting"
##    $print "gn_repairing_bot: ",gn_repairing_bot
##    $print "gn_damaged_bot_waiting: ",gn_damaged_bot_waiting

    if gn_damaged_bot_gender==0:                           ## generate camilla female bot
      $bot_cls=store.SexBot_squirrel_camilla
      $gn_combat_xp=12000
      $gn_social_xp=22600
    else:                                                  ## generate male quinton bot
      $bot_cls=store.SexBot_squirrel_quinton
      $gn_combat_xp=33000
      $gn_social_xp=38000

    python:
      notify.disable()
      damaged_patrol_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))
      damaged_patrol_bot.name=randchoice(damaged_patrol_bot.name_variants)
      store.global_bots_counter+=1
      generate_bot_warranty_seals(damaged_patrol_bot,default_generate_bot_warranty_seals_table)
      for slot in damaged_patrol_bot.outfit_slots:
        damaged_patrol_bot.chassis[slot].apply_damage(randint(-10,99))
      damaged_patrol_bot.give_xp("bot_combat",gn_combat_xp)
      damaged_patrol_bot.give_xp("bot_social",gn_social_xp)
      for trait in damaged_patrol_bot.psychocore.traits[:]:  ## remove any traits learned, should leave inherent alone
        trait.reset()
      damaged_patrol_bot.psychocore.stability=0              ## must be after giving xp which influences stability - bot was waiting set to 0
      damaged_patrol_bot.add_role("repair_patrol_bot")

    if home.available_capsules>0:                            ## capsule available
      if gn_damaged_bot_gender==0:                           ## female bot picture
        $action_image= "quests good_neighbors sgn_69"
      else:                                                  ## male bot picture
        $action_image= "quests good_neighbors sgn_71"
      $home.add_sexbot(damaged_patrol_bot)                   ## put bot created above in capsule
      $damaged_patrol_bot["repair_patrol_bot_quest_id"]=quests.start_quest("repair_patrol_bot",damaged_patrol_bot.id).id
      $notify.enable()                                       ## re-enable notifications

      "You get the damaged bot named {mark}[damaged_patrol_bot]{/} from the empty room and put [damaged_patrol_bot.himher] into an empty capsule so you can begin repairs."
      "{size=-16} {/}"
      center "{image=[action_image]@680x600}"
      "{size=-16} {/}"
      "Unfortunately without a {mark}Bot Support System{/} I'm sure [damaged_patrol_bot.heshe] became unstable. I better get to work on [damaged_patrol_bot.himher] so [damaged_patrol_bot.heshe] can be returned to the {mark}Neighborhood Patrol{/}."

      $gn_repairing_bot+=1                                   ## counter: increment when bot received

##      $print "added a bot being repaired"
##      $print "gn_repairing_bot: ",gn_repairing_bot
##      $print "gn_damaged_bot_waiting: ",gn_damaged_bot_waiting

      $damaged_patrol_bot=None                                ## clear damaged bot for next time at end so text works
      choice("<<<") "Continue"                             ## might need to be 'goto_home'

    elif workshop.available_space>0:                       ## storage space available
      if gn_damaged_bot_gender==0:                           ## female bot picture
        $action_image= "quests good_neighbors sgn_70"
      else:                                                  ## male bot picture
        $action_image= "quests good_neighbors sgn_72"
      $workshop.add_sexbot(damaged_patrol_bot)             ## put bot created above in capsule
      $damaged_patrol_bot["repair_patrol_bot_quest_id"]=quests.start_quest("repair_patrol_bot",damaged_patrol_bot.id).id
      $notify.enable()                                     ## re-enable notifications

      "You move the damaged bot named {mark}[damaged_patrol_bot]{/} from the empty room to a storage room and connect [damaged_patrol_bot.himher] to the {mark}Bot Support System{/}."
      "{size=-16} {/}"
      center "{image=[action_image]@680x600}"
      "{size=-16} {/}"
      "The {mark}Bot Support System{/} can't stabilize {mark}[damaged_patrol_bot]{/} but at least [damaged_patrol_bot.heshe] won't get any worse. I better start repairing [damaged_patrol_bot.himher] soon!"

      $gn_repairing_bot+=1                                 ## counter: increment when bot received

##      $print "added a bot being repaired"
##      $print "gn_repairing_bot: ",gn_repairing_bot
##      $print "gn_damaged_bot_waiting: ",gn_damaged_bot_waiting

      $damaged_patrol_bot=None                             ## clear damaged bot for next time at end so text works
      choice("<<<") "Continue"                             ## might need to be 'goto_home'

  else:                                                    ## original call when bot arrives

    if home.available_capsules>0:                          ## capsule available

      if gn_damaged_bot_gender==0:                         ## generate camilla female bot
        $action_image= "quests good_neighbors sgn_63"      ## female bot picture placeholder!!!!
        $bot_cls=store.SexBot_squirrel_camilla
        $gn_combat_xp=12000
        $gn_social_xp=22600
      else:                                                ## generate male quinton bot
        $action_image= "quests good_neighbors sgn_66"      ## male bot picture placeholder!!!!
        $bot_cls=store.SexBot_squirrel_quinton
        $gn_combat_xp=33000
        $gn_social_xp=38000

      python:
        notify.disable()
        damaged_patrol_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))
        damaged_patrol_bot.name=randchoice(damaged_patrol_bot.name_variants)
        store.global_bots_counter+=1
        generate_bot_warranty_seals(damaged_patrol_bot,default_generate_bot_warranty_seals_table)
        for slot in damaged_patrol_bot.outfit_slots:
          damaged_patrol_bot.chassis[slot].apply_damage(randint(-10,99))
        damaged_patrol_bot.give_xp("bot_combat",gn_combat_xp)
        damaged_patrol_bot.give_xp("bot_social",gn_social_xp)
        for trait in damaged_patrol_bot.psychocore.traits[:]:  ## remove any traits learned, should leave inherent alone
          trait.reset()
        damaged_patrol_bot.psychocore.stability=90             ## must be after giving xp which influences stability - was in fight, lost 10 percent
        damaged_patrol_bot.add_role("repair_patrol_bot")
        home.add_sexbot(damaged_patrol_bot)                    ## put bot created above in capsule
        damaged_patrol_bot["repair_patrol_bot_quest_id"]=quests.start_quest("repair_patrol_bot",damaged_patrol_bot.id).id
        notify.enable()                                        ## re-enable notifications

      "You take the damaged bot named {mark}[damaged_patrol_bot]{/} to the back of the shop and put [damaged_patrol_bot.himher] into an empty capsule. {mark}[gn_store_owner_name]{/} is afraid that the thugs will take advantage of the patrol being shorthanded."
      "{size=-16} {/}"
      center "{image=[action_image]@680x600}"
      "{size=-16} {/}"
      "You reassure {mark}[gn_store_owner_name]{/} that you'll get {mark}[damaged_patrol_bot]{/} fixed quickly and [damaged_patrol_bot.heshe] will be back to the {mark}Neighborhood Patrol{/} very soon."

      $gn_repairing_bot+=1                                 ## counter: increment when bot received

##      $print "added a bot being repaired"
##      $print "gn_repairing_bot: ",gn_repairing_bot
##      $print "gn_damaged_bot_waiting: ",gn_damaged_bot_waiting

      $damaged_patrol_bot=None                             ## clear damaged bot for next time at end so text works
      choice("advance_time") "Continue"

    elif workshop.available_space>0:                       ## storage space available

      if gn_damaged_bot_gender==0:                         ## female bot
        $action_image= "quests good_neighbors sgn_64"      ## female bot picture placeholder!!!!
        $bot_cls=store.SexBot_squirrel_camilla
        $gn_combat_xp=12000
        $gn_social_xp=22600
      else:                                                ## generate male quinton bot
        $action_image= "quests good_neighbors sgn_67"      ## male bot picture placeholder!!!!
        $bot_cls=store.SexBot_squirrel_quinton
        $gn_combat_xp=33000
        $gn_social_xp=38000

      python:
        notify.disable()
        damaged_patrol_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))
        damaged_patrol_bot.name=randchoice(damaged_patrol_bot.name_variants)
        store.global_bots_counter+=1
        generate_bot_warranty_seals(damaged_patrol_bot,default_generate_bot_warranty_seals_table)
        for slot in damaged_patrol_bot.outfit_slots:
          damaged_patrol_bot.chassis[slot].apply_damage(randint(-10,99))
        damaged_patrol_bot.give_xp("bot_combat",gn_combat_xp)
        damaged_patrol_bot.give_xp("bot_social",gn_social_xp)
        for trait in damaged_patrol_bot.psychocore.traits[:]:  ## remove any traits learned, should leave inherent alone
          trait.reset()
        damaged_patrol_bot.psychocore.stability=90             ## must be after giving xp which influences stability - was in fight, lost 10 percent
        damaged_patrol_bot.add_role("repair_patrol_bot")
        workshop.add_sexbot(damaged_patrol_bot)                ## put bot created above in storage
        damaged_patrol_bot["repair_patrol_bot_quest_id"]=quests.start_quest("repair_patrol_bot",damaged_patrol_bot.id).id
        notify.enable()                                        ## re-enable notifications

      "You take the damaged bot named {mark}[damaged_patrol_bot]{/} to one of the storage rooms and connect [damaged_patrol_bot.himher] to the {mark}Bot Support System{/}. {mark}[gn_store_owner_name]{/} asks you how long it will take to repair {mark}[damaged_patrol_bot]{/}."
      "{size=-16} {/}"
      center "{image=[action_image]@680x600}"
      "{size=-16} {/}"
      "You tell {mark}[gn_store_owner_name]{/} that you'll get right to work but don't mention that repairing bots in storage takes longer. At least the {mark}Bot Support System{/} will keep {mark}[damaged_patrol_bot]{/} stable."

      $gn_repairing_bot+=1                                 ## counter: increment when bot received

##      $print "added a bot being repaired"
##      $print "gn_repairing_bot: ",gn_repairing_bot
##      $print "gn_damaged_bot_waiting: ",gn_damaged_bot_waiting

      $damaged_patrol_bot=None                             ## clear damaged bot for next time at end so text works
      choice("advance_time") "Continue"

    else:                                                  ## no space available, DO NOT CREATE BOT NOW

      if gn_damaged_bot_gender==0:                         ## female bot
        $action_image= "quests good_neighbors sgn_65"
      else:                                                ## male bot
        $action_image= "quests good_neighbors sgn_68"

      "Damn, I don't have any capsules or storage space for another bot. I'll have to put this damaged patrol bot into an empty room until I have space. {mark}[gn_store_owner_name]{/} is very worried about the patrol being shorthanded for a long time."
      "{size=-16} {/}"
      center "{image=[action_image]@680x600}"
      "{size=-16} {/}"
      "You promise {mark}[gn_store_owner_name]{/} that you'll get the damaged bot repaired as quickly as you can. You don't say that without a {mark}Bot Support System{/} the bot will become unstable making repairs more difficult."

      $gn_damaged_bot_waiting=1                            ## set flag for bot waiting for available space, bot will be created when space available

##      $print "set bot into waiting"
##      $print "gn_repairing_bot: ",gn_repairing_bot
##      $print "gn_damaged_bot_waiting: ",gn_damaged_bot_waiting

      choice("advance_time") "Continue"
  return