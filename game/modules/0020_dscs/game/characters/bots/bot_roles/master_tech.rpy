##=========INIT VARIABLES=========  NOT SURE THIS IS NECESSARY
init python:
  master_techie_count=0       ## counter to loop through bots using 'while' - DO NOT RESET, re-used for TechBot Trainer rep
  master_techie_bonus=0       ## sum of elec and mech skill
  master_techie_bots_fixed=0  ## counter for bots repaired
  master_techie_min=0         ## minimum xp gain *5 OR minimum stability loss
  master_techie_max=5         ## maximum xp gain *5 OR maximum stability loss
  master_techie_actual=0      ## actual xp gain OR maximum stability loss
  master_techie_repair=0      ## repair effect in % integrity gain
  master_techie_none=0        ## set to 1 when there are no bots to repair
  master_techie_some=0        ## set to 1 if there is at least one repair made, do not clear for each bot
  master_techie_some_bot=0    ## set to 1 if repair made, clear for each bot
  mt_integrity_min=90         ## must be 100% integrity to avoid worrying about working on yourself!
  mt_stability_min=75         ## must be "stable" which is >75%
  mt_damaged_bots=0           ## set to 1 if there are any bots to repair (affects picture)
  mt_bot_new_assignment=0     ## 0.10.n - counter for bots just assigned
  mt_repair_count=0           ## 0.12.n count of actual repairs made for 'TechBot Trainer' rep

## Requirements: INTEGRITY=100%, STABILITY>=75%
## 'master techie' bot cannot fix itself, if repair necessary they cannot function
## 'master techie' bot can be repaired by another 'master techie' bot

##============FUNCTIONS============

label role_master_techie_repair:
  if not now("night"):
    $mt_repair_count=0                                                   ## reset counter
    $master_techie_none=0                                                ## reset flag before starting
    $master_techie_some=0                                                ## reset flag before starting
    $master_techie_some_bot=0                                            ## reset flag before starting
    $assistants=active_bots_with_role_tag("master_techie")               ## find all active master_techie bots

## 0.10.n change to avoid 'double dipping' roles
    $mt_bot_new_assignment=0             ## clear flag before starting
    $bot_count=0
    while bot_count<len(assistants):    ## go through assistants to remove ones just assigned

##      $print "BEGIN LOOP - bot_count: ",bot_count, "len(assistants): ",len(assistants)

      $temp_bot=assistants[bot_count]

##      $print "bot_count: ",bot_count,"temp_bot[0]: ",temp_bot[0],"temp_bot[0].mt_just_assigned: ",temp_bot[0].mt_just_assigned

      if temp_bot[0].mt_just_assigned==1:  ## if assigned role this turn
        $mt_bot_new_assignment+=1          ## increment count of bots just assigned
##        $temp_bot[0].mt_just_assigned=0    ## reset flag - MOVED TO REST, SLEEP, WORK
        $assistants.pop(bot_count)         ## remove bot from assistants - do not increment counter
      else:
        $bot_count+=1                      ## increment bot count for while loop

##      $print "END LOOP - bot_count: ",bot_count, "len(assistants): ",len(assistants)

## 0.10.n end of insertion

    if assistants:                                                       ## you have at least one master techie bot
      $assistant=randchoice(assistants)[0]                               ## select 1 'Master Techie' bot for the picture
      $master_techie_count=len(assistants)                               ## number of master techie bots
## find out if there are any bots to repair
      $master_techie_repair_target=workshop_get_random_repairable_bot()  ## return format: bots.append("repair",bot.id,slot,[defect]) - defect included when 1st item is "defect"
      if master_techie_repair_target:
        $mt_damaged_bots=1
      else:
        $mt_damaged_bots=0
## rendom master techie picture on left, text on the right: shows up between housekeeper and shopkeeper bots on time advances
## GRAPHICS
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      if mt_damaged_bots==1:                                             ## there are bots to repair
        if assistant.gender=="female":
          $mt_imagenumber=randint(1,6)                                   ## 1-3 Penelope, 4-6 Techie
        else:
          $mt_imagenumber=randint(7,9)                                   ## 7-9 Simon
      else:
        $mt_imagenumber=randint(13,15)                                   ## 13-15 empty gurney
      $action_image="roles master_techie rmt_"+str(mt_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
## TEXT
      $act.set_block("c")
      if master_techie_count==1:
        "It's great that my {mark}Master Techie{/} bot can repair bots by themself!"
      else:
        "It's great that my {mark}Master Techie{/} bots can repair bots by themselves!"

## MAIN SECTION, THIS IS WHERE BOTS GET REPAIRED!
      $while_end=len(assistants)
      $while_counter=0
##      if hide_full_description():
##        $notify.disable()
## START OF WHILE LOOP
      while while_counter<while_end:
        $assistant=find_character(assistants[while_counter][0])
        if assistant.psychocore.stability>=mt_stability_min and assistant.chassis.integrity>=mt_integrity_min:  ## work requirements met
          $master_techie_bonus=assistant.bot_electronics.level+assistant.bot_mechanics.level                    ## S-S=14, A-S=13, A-A-12, B-A-11, B-B-10

##          $print "before master techie bonus: ",master_techie_bonus

## 0.10.n insert 2 lines - reduce bonus when multiple tech roles assigned
          $reduce_bonus=fn_tech_roles(assistant)
          $master_techie_bonus-=reduce_bonus

##          $print "after master techie bonus: ",master_techie_bonus

          $temp_min=(master_techie_bonus-7)*10         ## 0.10.n changed formula related to mult. tech role reduction
          $temp_max=(master_techie_bonus-4)*10
## 0.10.n insert 2 lines - minimum value cannot be < 1
          if temp_min<1:
            $temp_min=1
          $master_techie_repair=randint(temp_min,temp_max)                                    ## B-B:10-60, B-A:20-70, A-A:30-80, A-S:40-90, to S-S:50-100

##          $print "min-max-actual: ",temp_min,temp_max,master_techie_repair

## 1ST REPAIR HAPPENS FOR ALL MASTER TECHIE BOTS: function call in 'workshop_fix_random_bot'
          $master_techie_repair_target=None
          $master_techie_repair_target=mgr_get_random_repairable_bot(assistant)       ## 0.10.n new function, return format: bots.append("repair",bot.id,slot,[defect]) - defect included when 1st item is "defect"
          if master_techie_repair_target:
            $master_techie_some=1                                                     ## all bot flag: 1 means any bot made at least one repair
            $master_techie_some_bot=1                                                 ## this bot flag: 1 means bot made at least one repair
            if master_techie_repair_target[0]=="repair":
              call master_techie_fix_random_bot_part(master_techie_repair_target[1],master_techie_repair_target[2])
            else:
              call master_techie_fix_random_bot_part_defect(master_techie_repair_target[1],master_techie_repair_target[2],master_techie_repair_target[3])
            $mt_repair_count+=1                                                        ## increment counter
          else:
            $master_techie_none=1                                                     ## no bots to repair
## 2ND REPAIR FOR BOTS WITH AT LEAST ONE 'S' RATING: function call in 'workshop_fix_random_bot'
          if assistant.bot_electronics.level==7 or assistant.bot_mechanics.level==7:  ## second repair if either elec or mech is 'S'
            $master_techie_repair=randint(temp_min,temp_max)                          ## new random number
            $master_techie_repair_target=mgr_get_random_repairable_bot(assistant)     ## 0.10.n new function, return format: bots.append("repair",bot.id,slot,[defect]) - defect included when 1st item is "defect"
            if master_techie_repair_target:
              $master_techie_some=1                                                   ## all bot flag: 1 means any bot made at least one repair
              $master_techie_some_bot=1                                               ## this bot flag: 1 means bot made at least one repair
              if master_techie_repair_target[0]=="repair":
                call master_techie_fix_random_bot_part(master_techie_repair_target[1],master_techie_repair_target[2])
              else:
                call master_techie_fix_random_bot_part_defect(master_techie_repair_target[1],master_techie_repair_target[2],master_techie_repair_target[3])
              $mt_repair_count+=1                                                      ## increment counter
            else:
              $master_techie_none=1                                                   ## no bots to repair
## BONUS REPAIR FOR BOTS WITH HIGH AUTONOMY: function call in 'workshop_fix_random_bot'
          $mt_chance=randint(1,100)
## 0.15.n bug fix in next line, autonomy 6 was 25% chance by mistake
          if (assistant.autonomy.level==5 and mt_chance>50) or(assistant.autonomy.level==6 and mt_chance>25) or assistant.autonomy.level==7:  ## Autonomy: B 50%, A 75%, S always
            $master_techie_repair=randint(temp_min,temp_max)                          ## new random number
            $master_techie_repair_target=mgr_get_random_repairable_bot(assistant)     ## 0.10.n new function, return format: bots.append("repair",bot.id,slot,[defect]) - defect included when 1st item is "defect"
            if master_techie_repair_target:
              $master_techie_some=1                                                   ## all bot flag: 1 means any bot made at least one repair
              $master_techie_some_bot=1                                               ## this bot flag: 1 means bot made at least one repair
              if master_techie_repair_target[0]=="repair":
                call master_techie_fix_random_bot_part(master_techie_repair_target[1],master_techie_repair_target[2])
              else:
                call master_techie_fix_random_bot_part_defect(master_techie_repair_target[1],master_techie_repair_target[2],master_techie_repair_target[3])
              $mt_repair_count+=1                                                      ## increment counter
            else:
              $master_techie_none=1                                                   ## no bots to repair
## END OF BOT REPAIR SECTION

## WORKING MASTER TECH BOT GAINS MECHANICS AND ELECTRONICS XP
          if master_techie_some_bot==1:                                                        ## current bot made at least one repair
            $master_techie_actual=randint(master_techie_min,master_techie_max*5)               ## original values 0,5*5 (v0.6.0)

##            print master_techie_actual

            $assistant.give_xp("bot_mechanics",master_techie_actual*5)                         ## original values 0,5*5 (v0.6.0)
            $master_techie_actual=randint(master_techie_min,master_techie_max)

##            print master_techie_actual

            $assistant.give_xp("bot_electronics",master_techie_actual)
##  WORKING MASTER TECHIE BOT MAY LOSE STABILITY
            $master_techie_actual=randint(master_techie_min,master_techie_max)                         ## original values 0,5 (v0.6.0)
            $master_techie_actual=int(master_techie_actual*assistant.psychocore_stability_decay_mult)  ## each bot has multiplier, use it!
            if master_techie_actual<assistant.psychocore.stability:                                    ## decrease stability but not <1
              $assistant.psychocore.stability-=master_techie_actual
        elif assistant.psychocore.stability>=mt_stability_min:                                         ## stability OK: integrity must be too low
##          ""
##          "{mark}[assistant]{/} must have 100%% integrity to fix bots."
          "{info}{size=-8}{i}{mark}[assistant]{/} {bad}cannot work{/}-{mark}low integrity{/}{/}{/}{/}"
        elif assistant.chassis.integrity>=mt_integrity_min:                                    ## integrity OK: stability must be too low
##          ""
##          "{mark}[assistant]{/} must be stable to fix bots."
          "{info}{size=-8}{i}{mark}[assistant]{/} {bad}cannot work{/}-{mark}low stability{/}{/}{/}{/}"
        else:                                                                                  ## both stability and integrity too low
##          ""
##          "{mark}[assistant]{/} needs both repairs and stabilization to fix bots."
          "{info}{size=-8}{i}{mark}[assistant]{/} {bad}cannot work{/}-{mark}low integrity&stability{/}{/}{/}{/}"
        $master_techie_some_bot=0                                                              ## clear bot specific flag for next bot, leave other flags alone
        $while_counter+=1                                                                      ## increment the loop counter
## END OF WHILE LOOP

## 0.12.n gain TechBot trainer rep proportional to repairs made
      if mt_repair_count>0:                                           ## at least 1 repair made
        "Customers noticed your Master Techie bots working."
        if mt_repair_count>4:                                         ## more than 4 bot repairs
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","xl_g")        ## extra large gain
          $mc.give_xp("rep_mc_tech_trainer",temp)
        elif mt_repair_count==4:                                      ## 4 bot repairs
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","l_g")         ## large gain
          $mc.give_xp("rep_mc_tech_trainer",temp)
        elif mt_repair_count==3:                                      ## 3 bot repairs
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","m_g")         ## medium gain
          $mc.give_xp("rep_mc_tech_trainer",temp)
        elif mt_repair_count==2:                                      ## 2 bot repair
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","s_g")         ## small gain
          $mc.give_xp("rep_mc_tech_trainer",temp)
        else:                                                         ## 1 bot repair
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","xs_g")        ## extra small gain
          $mc.give_xp("rep_mc_tech_trainer",temp)
          
      if master_techie_none==1:                                                                ## all bots repaired...
        if master_techie_some==0:                                                              ## ...no repairs were made: no damaged bots at start
          ""
          "There's nothing to do though; there are no damaged bots."
        else:                                                                                  ## ...must have made some repairs...
          if master_techie_some_bot==0:                                                        ## ...last bot made no repairs
            ""
            "All damaged bots were repaired, some {mark}Master Techie bots{/} had nothing to do."
          else:                                                                                ## ...last bot did some repairs
            ""
            "All damaged bots were repaired. {mark}Master Techie bots{/} are fantastic!"
          
    else:                                                          ##  no Master Techie bots
##  set up columns and display MC thinking picture on left
##  GRAPHICS
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $mt_imagenumber=randint(10,12)                               ## MC thinking about having master techie bots
      $action_image="roles master_techie rmt_"+str(mt_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
##    TEXT
      $act.set_block("c")
## 0.10.n conditional text for bot(s) just assigned (only when no master techies)
      if mt_bot_new_assignment==0:    ## no bots just assigned
        "Maybe I should have {mark}Master Techie{/} bots and keep them at home in capsules. They can repair bots by themselves and I'd have more time to do other things."
      elif mt_bot_new_assignment==1:  ## 1 bot just assigned 
        "I just assigned a bot the {mark}Master Techie{/} role so in the future they will fix other bots by themselves and I can do other things."
      else:                           ## > 1 bot just assigned
        "I just assigned bots the {mark}Master Techie{/} role so in the future they will fix other bots by themselves and I can do other things."
##  clean up
    $assistant=None
    $assistants=None
    ""                                ## add a line before the next item is displayed
  return

label master_techie_fix_random_bot_part(bot,part):
  $bot=find_character(bot)
  $part=bot.chassis[part]
  $part.integrity+=master_techie_repair
  "{info}{size=-8}{i}{mark}[assistant]{/} repaired a damaged {mark}[part]{/} on {mark}[bot]{/}{/}{/}{/}"
  return

label master_techie_fix_random_bot_part_defect(bot,part,defect):
  $bot=find_character(bot)
  $part=bot.chassis[part]
  $defect=part.defects[int(defect)]
  $defect.fix_progress+=master_techie_repair
  if defect.fix_progress==100:
    $part.defects.remove(defect)
  "{info}{size=-8}{i}{mark}[assistant]{/} fixed a defective {mark}[part]{/} on {mark}[bot]{/}{/}{/}{/}"
  return