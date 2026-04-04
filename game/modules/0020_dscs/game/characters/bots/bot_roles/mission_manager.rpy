##=========INIT VARIABLES=========
init python:
  mgr_integrity_min=90          ## must be 90% integrity
  mgr_stability_min=75          ## must be "stable" which is >75%
  managers=[]                   ## subset of 'assistants' that meet minimums
  active_manager=None           ## will hold the active mission manager bot so they don't go on a mission
  sendbot_integrity_min=75      ## minimum integrity to be sent on mission
  sendbot_stability_min=75      ## minimum stability to be sent on mission
  bot_tech_level=0              ## minimum of electronic and mechanic skill levels
  mgr_fight_money_check=100000  ## if mc.money (player's money) is less than this bots are not sent on fights by the mission manager
  mgr_bot_new_assignment=0      ## 0.10.n - counter for bots just assigned
  mgr_missions_assigned=0       ## 0.10.n - count of missions assigned this turn

## Requirements: INTEGRITY=90%, STABILITY>=75%
## 'mission manager' cannot assign themselves to a mission
## 'mission manager' can assign other managers to missions, only the randomly selected manager cannot go on a mission

##============FUNCTIONS============

label role_mission_manager_schedule:
  $assistants=active_bots_with_role_tag("mission_manager")   ## find all active mission_manager bots

## 0.10.n change to avoid 'double dipping' roles
  $mgr_bot_new_assignment=0             ## reset bot just assigned counter
  $mgr_missions_assigned=0              ## reset mission counter
  $bot_count=0
  while bot_count<len(assistants):    ## go through assistants to remove ones just assigned

##    $print "BEGIN LOOP - bot_count: ",bot_count, "len(assistants): ",len(assistants)

    $temp_bot=assistants[bot_count]

##    $print "bot_count: ",bot_count,"temp_bot[0]: ",temp_bot[0],"temp_bot[0].mt_just_assigned: ",temp_bot[0].mt_just_assigned

    if temp_bot[0].mgr_just_assigned==1:  ## if assigned role this turn
      $mgr_bot_new_assignment+=1          ## increment count of bots just assigned
##      $temp_bot[0].mgr_just_assigned=0    ## reset flag - MOVED TO REST, SLEEP, WORK
      $assistants.pop(bot_count)          ## remove bot from assistants - do not increment counter
    else:
      $bot_count+=1                       ## increment bot count for while loop

##    $print "END LOOP - bot_count: ",bot_count, "len(assistants): ",len(assistants)

## 0.10.n end of insertion

  if assistants:                  ## you have at least one mission manager bot
    $managers=[]                  ## clear bot managers that meet integrity and stability requirements
    $active_manager=None          ## clear list of all bot managers

## BEGIN WHILE LOOP
    $while_end=len(assistants)
    $while_counter=0
    while while_counter<while_end:
      $assistant=find_character(assistants[while_counter][0])
      if assistant.psychocore.stability>=mgr_stability_min and assistant.chassis.integrity>=mgr_integrity_min:  ## requirements met
        $managers.append(assistant)                           ## add bot that met requirements
      $while_counter+=1                                       ## increment the loop counter
## END OF WHILE LOOP
    $assistants=[]                                            ## clear assistants, no longer needed
    if managers:
      $active_manager=randchoice(managers)                    ## select 1 'mission manager' bot for the picture and not to be sent on a mission
      $act.start_block("l:250 c:content_width-250")
      $action_image="roles mission_manager rmgr_1"            ##  HARD CODE - SINGLE USE
      center "{image=[action_image]@150x225}"
      $act.set_block("c")
      "{mark}[active_manager]{/}"

## BEGIN WHILE LOOP
      $while_end=len(home.sexbots)
      $while_counter=0
      $m_bot=None

##      $print ""
##      $print "Day/Time: ",now.dow_name,now.tod_name

      while while_counter<while_end:
        $m_bot=find_character(home.sexbots[while_counter])

##        $print "testing bot ",m_bot

        if m_bot and m_bot!=active_manager:                                                                           ## skip empty capsules and the active manager!
          if m_bot.action_allowed("mission") and m_bot.allow_manage and not m_bot["mission"]:                         ## missions allowed, manage allowed, not on mission
            if m_bot.chassis.integrity>=sendbot_integrity_min and m_bot.psychocore.stability>=sendbot_stability_min:  ## >= integrity and stability limits
              call mgr_select_mission(m_bot)
        $while_counter+=1                                                                                             ## increment the loop counter
## END OF WHILE LOOP

## 0.10.n add line with mission count
      if mgr_missions_assigned==0:
        extend " tried to schedule missions but the bots available did not match the available missions."
      elif mgr_missions_assigned==1:
        extend " scheduled a mission for {mark}1{/} bot."                        ## 1 bot on mission
      else:
        extend " scheduled missions for {mark}[mgr_missions_assigned]{/} bots."  ## multiple bots on missions
      $act.end_block()                                                           ## end custom block
    else:
      "All bots assigned the role {mark}Bot Manager{/} were unable to complete their assignment. Perhaps you should check their {mark}status{/}?"
##    if now("night"):                 ## LINE FEED FOR SLEEP ONLY
##        ""
  else:    ## no bots assigned to mission manager role_mission_manager_schedule

## 0.10.n conditional text for bot(s) just assigned (only when no managers)
    if mgr_bot_new_assignment==0:    ## no bots just assigned
      "Managing bot missions takes a lot of time. Maybe I should have {mark}Bot Manager{/} bots at home in capsules to do it for me."
    elif mgr_bot_new_assignment==1:  ## 1 bot just assigned 
      "I just assigned a bot the {mark}Bot Manager{/} role so they in the future will send bots on missions and I won't have to keep track of them."
    else:                            ## > 1 bot just assigned
      "I just assigned bots the {mark}Bot Manager{/} role so in the future they will send bots on missions and I won't have to keep track of them."

##    if now("night"):                                          ## LINE FEED FOR SLEEP ONLY
##      ""
## clean up
  $assistant=None
  $assistants=None
  return

label mgr_select_mission(bot):
  $bot_tech_level=min(bot.bot_mechanics.level,bot.bot_electronics.level)  ## TECH level is minimum of electronics and mechanics levels

  if bot.mgr_priority=="sex":
    if now("night"):                       ## sex missions are available during night only
      if bot.gender=="female":
        call send_on_whore_mission(bot)
      else:
        call send_on_gigolo_mission(bot)
    elif now("morning"):                   ## if sex bot is qualified for scavenging they can do it in the morning
      if bot_tech_level>=4:
        call send_on_scavenge_mission(bot)
  elif bot.mgr_priority=="tech":
    if not now("night"):                   ## bots don't go scavenging at night, they need to recharge some time (removed all the time with 50% chance)
      call send_on_scavenge_mission(bot)
  elif bot.mgr_priority=="combat":
    if now("monday")or now("wednesday"):
      if bot.rate=="D" or bot.rate=="B":
        $allow_alternate_mission=0
        if now("evening"):
          call send_on_ufc_mission(bot)
      else:                                        ## bots not D or B not fight day
        $allow_alternate_mission=1
    elif now("tuesday") or now("thursday"):
      if bot.rate=="C" or bot.rate=="A":
        $allow_alternate_mission=0
        if now("evening"):
          call send_on_ufc_mission(bot)
      else:                                        ## bots not C or A not fight day
        $allow_alternate_mission=1
    elif now("friday") or now("saturday"):
      if bot.rate=="S":
        $allow_alternate_mission=0
        if now("evening"):
          call send_on_ufc_mission(bot)
      else:                                        ## bots not S not fight day
        $allow_alternate_mission=1
    else:                                          ## must be sunday, no fights
      $allow_alternate_mission=1
    if allow_alternate_mission==1:                 ## not fight day, can send bot on other missions
      if now("morning") and bot_tech_level>=4:     ## on non-fight days send combat bots on scavenge missions in the morning if qualified
        call send_on_scavenge_mission(bot)
      elif now("night") and bot.bot_sex.level>=4 : ## on non-fight days send combat bots on whore/gigolo missions at night if qualified
        if bot.gender=="female":
          call send_on_whore_mission(bot)
        else:
          call send_on_gigolo_mission(bot)
  else:                                              ## MUST BE 'default'
    if bot.bot_sex.level>=4 and bot.bot_sex.level>=bot_tech_level and bot.bot_sex.level>=bot.bot_combat.level:  ## SEX 1st priority and >=C
      if now("night"):                               ## sex missions are available during night only
        if bot.gender=="female":
          call send_on_whore_mission(bot)
        else:
          call send_on_gigolo_mission(bot)
      elif now("morning"):                           ## if sex bot is qualified for scavenging they can do it in the morning
        if bot_tech_level>=4:
          call send_on_scavenge_mission(bot)
    elif bot_tech_level>=4 and bot_tech_level>=bot.bot_sex.level and bot_tech_level>=bot.bot_combat.level:  ## TECH 2nd priority and >=C
      if not now("night"):                           ## bots don't go scavenging at night, they need to recharge some time (removed all the time with 50% chance)
        call send_on_scavenge_mission(bot)
    elif bot.bot_combat.level>=4 and bot.bot_combat.level>=bot.bot_sex.level and bot.bot_combat.level>=bot_tech_level:  ## COMBAT 3rd priority and >=C
      if now("monday")or now("wednesday"):
        if bot.rate=="D" or bot.rate=="B":
          $allow_alternate_mission=0
          if now("evening"):
            call send_on_ufc_mission(bot)
        else:                                        ## bots not D or B not fight day
          $allow_alternate_mission=1
      elif now("tuesday") or now("thursday"):
        if bot.rate=="C" or bot.rate=="A":
          $allow_alternate_mission=0
          if now("evening"):
            call send_on_ufc_mission(bot)
        else:                                        ## bots not C or A not fight day
          $allow_alternate_mission=1
      elif now("friday") or now("saturday"):
        if bot.rate=="S":
          $allow_alternate_mission=0
          if now("evening"):
            call send_on_ufc_mission(bot)
        else:                                        ## bots not S not fight day
          $allow_alternate_mission=1
      else:                                          ## must be sunday, no fights
        $allow_alternate_mission=1
      if allow_alternate_mission==1:                 ## not fight day, can send bot on other missions
        if now("morning") and bot_tech_level>=4:     ## on non-fight days send combat bots on scavenge missions in the morning if qualified
          call send_on_scavenge_mission(bot)
        elif now("night") and bot.bot_sex.level>=4 : ## on non-fight days send combat bots on whore/gigolo missions at night if qualified
          if bot.gender=="female":
            call send_on_whore_mission(bot)
          else:
            call send_on_gigolo_mission(bot)
  return

label send_on_gigolo_mission(bot):         ## COPIED SELECTED LINES FROM 'interact_missions.rpy'
  $mission="gigolo"                        ## this is the 'mission.id'
  $mission=modded_missions[mission]
  python hide:
    bot["mission"]=mission.id
    duration=mission.duration
    if isinstance(duration,(list,tuple)):
      duration=randint(*duration)
    bot["mission_timer"]=duration
  $mission=None
  $mgr_missions_assigned+=1                ## increment mission count

##  $print "XXX - gigolo - XXX",mgr_missions_assigned

  return

label send_on_whore_mission(bot):          ## COPIED SELECTED LINES FROM 'interact_missions.rpy'
  $mission="whore"                         ## this is the 'mission.id'
  $mission=modded_missions[mission]
  python hide:
    bot["mission"]=mission.id
    duration=mission.duration
    if isinstance(duration,(list,tuple)):
      duration=randint(*duration)
    bot["mission_timer"]=duration
  $mission=None
  $mgr_missions_assigned+=1                ## increment mission count

##  $print "XXX - whore - XXX",mgr_missions_assigned

  return

label send_on_scavenge_mission(bot):       ## COPIED SELECTED LINES FROM 'interact_missions.rpy'
  $mission="scavenge"                      ## this is the 'mission.id'
  $mission=modded_missions[mission]
  python hide:
    bot["mission"]=mission.id
    duration=mission.duration
    if isinstance(duration,(list,tuple)):
      duration=randint(*duration)
    bot["mission_timer"]=duration
  $mission=None
  $mgr_missions_assigned+=1                ## increment mission count

##  $print "XXX - scavenge - XXX",mgr_missions_assigned

  return

label send_on_ufc_mission(bot):       ## COPIED SELECTED LINES FROM 'interact_missions.rpy'
  if mc.money>=mgr_fight_money_check:
    if bot.gender=="female":                 ## UFC missions are day and gender specific
      if now("monday"):
        if bot.rate=="D":
          $mission="ufc_female_1a"
        elif bot.rate=="B":
          $mission="ufc_female_3a"
      if now("tuesday"):
        if bot.rate=="C":
          $mission="ufc_female_2a"
        elif bot.rate=="A":
          $mission="ufc_female_4a"
      if now("wednesday"):
        if bot.rate=="D":
          $mission="ufc_female_1b"
        elif bot.rate=="B":
          $mission="ufc_female_3b"
      if now("thursday"):
        if bot.rate=="C":
          $mission="ufc_female_2b"
        elif bot.rate=="A":
          $mission="ufc_female_4b"
      if now("friday") and bot.rate=="S":
        $mission="ufc_female_5a"
      if now("saturday") and bot.rate=="S":
        $mission="ufc_female_5b"
    else:                                   ## bot is male, UFC missions are day and gender specific
      if now("monday"):
        if bot.rate=="D":
          $mission="ufc_male_1a"
        elif bot.rate=="B":
          $mission="ufc_male_3a"
      if now("tuesday"):
        if bot.rate=="C":
          $mission="ufc_male_2a"
        elif bot.rate=="A":
          $mission="ufc_male_4a"
      if now("wednesday"):
        if bot.rate=="D":
          $mission="ufc_male_1b"
        elif bot.rate=="B":
          $mission="ufc_male_3b"
      if now("thursday"):
        if bot.rate=="C":
          $mission="ufc_male_2b"
        elif bot.rate=="A":
          $mission="ufc_male_4b"
      if now("friday") and bot.rate=="S":
        $mission="ufc_male_5a"
      if now("saturday") and bot.rate=="S":
        $mission="ufc_male_5b"
    $mission=modded_missions[mission]
    python hide:
      bot["mission"]=mission.id
      duration=mission.duration
      if isinstance(duration,(list,tuple)):
        duration=randint(*duration)
      bot["mission_timer"]=duration
    $mission=None
    $mgr_missions_assigned+=1                            ## increment mission count

##    $print "XXX - UFC - XXX",mgr_missions_assigned

## NEXT 2 LINES ARE FOR DEBUGGING ONLY
##  else:
##    $print bot, "money < 'mgr_fight_money_check', DO NOT send bot to UFC - value: ",mgr_fight_money_check  ##DEBUGGING LINE

  return