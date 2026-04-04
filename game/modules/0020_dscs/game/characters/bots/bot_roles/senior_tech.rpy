##=========INIT VARIABLES=========  NOT SURE THIS IS NECESSARY
init python:
  senior_techie_count=0        ## counter to loop through bots using 'while' - DO NOT RESET, re-used for TechBot Trainer rep
  senior_techie_bonus=0        ## sum of elec and mech skill
  senior_techie_parts_fixed=0  ## counter for parts repaired
  senior_techie_min=0          ## minimum xp gain *5 OR minimum stability loss
  senior_techie_max=5          ## maximum xp gain *5 OR maximum stability loss
  senior_techie_actual=0       ## actual xp gain OR maximum stability loss
  senior_techie_repair=0       ## repair effect in % integrity gain
  senior_techie_none=0         ## set to 1 when there are no parts to repair
  senior_techie_some=0         ## set to 1 if there is at least one repair made, do not clear for each bot
  senior_techie_some_part=0    ## set to 1 if repair made, clear for each bot
  st_integrity_min=90          ## must be 100% integrity
  st_stability_min=75          ## must be "stable" which is >75%
  st_damaged_parts=0           ## set to 1 if there are any parts to repair (affects picture)
  st_bot_new_assignment=0      ## 0.10.n - counter for bots just assigned
  st_repair_count=0           ## 0.12.n count of actual repairs made for 'TechBot Trainer' rep

##============FUNCTIONS============

label role_senior_techie_repair:
  if not now("night"):
    $st_repair_count=0                                      ## reset counter
    $senior_techie_none=0                                   ## reset flag before starting
    $senior_techie_some=0                                   ## reset flag before starting
    $senior_techie_some_bot=0                               ## reset flag before starting
    $assistants=active_bots_with_role_tag("senior_techie")  ## find all active bots assigned senior_techie role

## 0.10.n change to avoid 'double dipping' roles
    $st_bot_new_assignment=0            ## clear flag before starting
    $bot_count=0
    while bot_count<len(assistants):    ## go through assistants to remove ones just assigned

##      $print "BEGIN LOOP - bot_count: ",bot_count, "len(assistants): ",len(assistants)

      $temp_bot=assistants[bot_count]

##      $print "bot_count: ",bot_count,"temp_bot[0]: ",temp_bot[0],"temp_bot[0].st_just_assigned: ",temp_bot[0].st_just_assigned

      if temp_bot[0].st_just_assigned==1:  ## if assigned role this turn
        $st_bot_new_assignment+=1          ## increment count of bots just assigned
##        $temp_bot[0].st_just_assigned=0    ## reset flag - MOVED TO REST, SLEEP, WORK
        $assistants.pop(bot_count)         ## remove bot from assistants - do not increment counter
      else:
        $bot_count+=1                      ## increment bot count for while loop

##      $print "END LOOP - bot_count: ",bot_count, "len(assistants): ",len(assistants)

## 0.10.n end of insertion

    if assistants:                                                       ## you have at least one senior techie bot
      $assistant=randchoice(assistants)[0]                               ## select 1 'Senior Techie' bot for the picture
      $senior_techie_count=len(assistants)                               ## number of senior techie bots


## find out if there are any parts to repair
      $senior_techie_repair_target=workshop_get_random_repairable_part()  ## return format: [0] is "repair" or" defect, [1] is part index #,[2] is defect info if needed
      if senior_techie_repair_target:
        $st_damaged_parts=1
      else:
        $st_damaged_parts=0


## rendom senior techie picture on left, text on the right: shows up between master techie and shopkeeper bots on time advances
## GRAPHICS
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      if st_damaged_parts==1:                                            ## there are parts to repair
        if assistant.gender=="female":
          $st_imagenumber=randint(1,4)                                   ## 1-2 Penelope, 3-4 Techie
        else:
          $st_imagenumber=randint(5,6)                                   ## 5-6 Simon
      else:
        $st_imagenumber=randint(11,12)                                   ## 11-12 empty table
      $action_image="roles senior_techie rst_"+str(st_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
## TEXT
      $act.set_block("c")
      if senior_techie_count==1:
        "It's great that my {mark}Senior Techie{/} bot can fix parts by themself!"
      else:
        "It's great that my {mark}Senior Techie{/} bots can fix parts by themselves!"

## MAIN SECTION, THIS IS WHERE PARTS GET REPAIRED!
      $while_end=len(assistants)
      $while_counter=0
##      if hide_full_description():
##        $notify.disable()
## START OF WHILE LOOP
      while while_counter<while_end:
        $assistant=find_character(assistants[while_counter][0])
        if assistant.psychocore.stability>=mt_stability_min and assistant.chassis.integrity>=mt_integrity_min:  ## work requirements met
          $senior_techie_bonus=assistant.bot_electronics.level+assistant.bot_mechanics.level                    ## S-S=14, A-S=13, A-A-12, B-A-11, B-B-10

##          $print "before senior techie bonus: ",senior_techie_bonus

## 0.10.n insert 2 lines - reduce bonus when multiple tech roles assigned
          $reduce_bonus=fn_tech_roles(assistant)
          $senior_techie_bonus-=reduce_bonus

##          $print "after senior techie bonus: ",senior_techie_bonus

          $temp_min=(senior_techie_bonus-7)*10         ## 0.10.n changed min to (bonus-8) from (bonus-10) related to mult. tech role reduction
          $temp_max=(senior_techie_bonus-4)*10
## 0.10.n insert 2 lines - minimum value cannot be < 1
          if temp_min<1:
            $temp_min=1
          $senior_techie_repair=randint(temp_min,temp_max)                                    ## B-B:10-60, B-A:20-70, A-A:30-80, A-S:40-90, to S-S:50-100

##          $print "min-max-actual: ",temp_min,temp_max,senior_techie_repair

## 1ST REPAIR HAPPENS FOR ALL SENIOR TECHIE BOTS: function call in 'workshop_fix_random_part.rpy'
          $senior_techie_repair_target=workshop_get_random_repairable_part()                  ## return format: [0] is "repair" or" defect, [1] is part index #,[2] is defect info if needed
          if senior_techie_repair_target:
            $senior_techie_some=1                                                             ## all bot flag: 1 means any bot made at least one repair
            $senior_techie_some_part=1                                                        ## this bot flag: 1 means bot made at least one repair
            if senior_techie_repair_target[0]=="repair":
              call senior_techie_fix_random_part(senior_techie_repair_target[1])
            else:
              call senior_techie_fix_random_part_defect(senior_techie_repair_target[1],senior_techie_repair_target[2])
            $st_repair_count+=1                                                        ## increment counter
          else:
            $senior_techie_none=1                                                     ## no parts to repair
## 2ND REPAIR FOR BOTS WITH AT LEAST ONE 'S' RATING: function call in 'workshop_fix_random_part.rpy'
          if assistant.bot_electronics.level==7 or assistant.bot_mechanics.level==7:  ## second repair if either elec or mech is 'S'
            $senior_techie_repair=randint(temp_min,temp_max)                          ## new random number
            $senior_techie_repair_target=workshop_get_random_repairable_part()        ## return format: [0] is "repair" or" defect, [1] is part index #,[2] is defect info if needed
            if senior_techie_repair_target:
              $senior_techie_some=1                                                   ## all bot flag: 1 means any bot made at least one repair
              $senior_techie_some_part=1                                               ## this bot flag: 1 means bot made at least one repair
              if senior_techie_repair_target[0]=="repair":
                call senior_techie_fix_random_part(senior_techie_repair_target[1])
              else:
                call senior_techie_fix_random_part_defect(senior_techie_repair_target[1],senior_techie_repair_target[2])
              $st_repair_count+=1                                                      ## increment counter
            else:
              $senior_techie_none=1                                                   ## no parts to repair
## BONUS REPAIR FOR BOTS WITH HIGH AUTONOMY: function call in 'workshop_fix_random_part.rpy'
          $st_chance=randint(1,100)
## 0.15.n bug fix in next line, autonomy 6 was 25% chance by mistake
          if (assistant.autonomy.level==5 and st_chance>50) or (assistant.autonomy.level==6 and st_chance>25) or assistant.autonomy.level==7:  ## Autonomy: B 50%, A 75%, S always
            $senior_techie_repair=randint(temp_min,temp_max)                          ## new random number
            $senior_techie_repair_target=workshop_get_random_repairable_part()        ## return format: [0] is "repair" or" defect, [1] is part index #,[2] is defect info if needed
            if senior_techie_repair_target:
              $senior_techie_some=1                                                   ## all bot flag: 1 means any bot made at least one repair
              $senior_techie_some_part=1                                               ## this bot flag: 1 means bot made at least one repair
              if senior_techie_repair_target[0]=="repair":
                call senior_techie_fix_random_part(senior_techie_repair_target[1])
              else:
                call senior_techie_fix_random_part_defect(senior_techie_repair_target[1],senior_techie_repair_target[2])
              $st_repair_count+=1                                                      ## increment counter
            else:
              $senior_techie_none=1                                                   ## no parts to repair

## END OF PART REPAIR SECTION

## WORKING SENIOR TECH BOT GAINS MECHANICS AND ELECTRONICS XP
          if senior_techie_some_part==1:                                                       ## current bot made at least one repair
            $senior_techie_actual=randint(senior_techie_min,senior_techie_max*5)               ## original values 0,5*5 (v0.9.0)

##            print senior_techie_actual

            $assistant.give_xp("bot_mechanics",senior_techie_actual*5)                         ## original values 0,5*5 (v0.9.0)
            $senior_techie_actual=randint(senior_techie_min,senior_techie_max)

##            print senior_techie_actual

            $assistant.give_xp("bot_electronics",senior_techie_actual)
##  WORKING SENIOR TECHIE BOT MAY LOSE STABILITY
            $senior_techie_actual=randint(senior_techie_min,senior_techie_max)                         ## original values 0,5 (v0.9.0)
            $senior_techie_actual=int(senior_techie_actual*assistant.psychocore_stability_decay_mult)  ## each bot has multiplier, use it!
            if senior_techie_actual<assistant.psychocore.stability:                                    ## decrease stability but not <1
              $assistant.psychocore.stability-=senior_techie_actual
        elif assistant.psychocore.stability>=st_stability_min:                                 ## stability OK: integrity must be too low
##          ""
##          "{mark}[assistant]{/} must have 100%% integrity to fix parts."
          "{info}{size=-8}{i}{mark}[assistant]{/} {bad}cannot work{/}-{mark}low integrity{/}{/}{/}{/}"
        elif assistant.chassis.integrity>=mt_integrity_min:                                    ## integrity OK: stability must be too low
##          ""
##          "{mark}[assistant]{/} must be stable to fix parts."
          "{info}{size=-8}{i}{mark}[assistant]{/} {bad}cannot work{/}-{mark}low stability{/}{/}{/}{/}"
        else:                                                                                  ## both stability and integrity too low
##          ""
##          "{mark}[assistant]{/} needs both repairs and stabilization to fix parts."
          "{info}{size=-8}{i}{mark}[assistant]{/} {bad}cannot work{/}-{mark}low integrity&stability{/}{/}{/}{/}"
        $senior_techie_some_part=0                                                             ## clear bot specific flag for next bot, leave other flags alone
        $while_counter+=1                                                                      ## increment the loop counter
## END OF WHILE LOOP

## 0.12.n gain TechBot trainer rep proportional to repairs made
      if st_repair_count>0:                                           ## at least 1 repair made
        "Customers noticed your Senior Techie bots working."
        if st_repair_count>4:                                         ## more than 4 part repairs
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","xl_g")        ## extra large gain
          $mc.give_xp("rep_mc_tech_trainer",temp)
        elif st_repair_count==4:                                      ## 4 part repairs
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","l_g")         ## large gain
          $mc.give_xp("rep_mc_tech_trainer",temp)
        elif st_repair_count==3:                                      ## 3 part repairs
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","m_g")         ## medium gain
          $mc.give_xp("rep_mc_tech_trainer",temp)
        elif st_repair_count==2:                                      ## 2 part repair
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","s_g")         ## small gain
          $mc.give_xp("rep_mc_tech_trainer",temp)
        else:                                                         ## 1 part repair
          $temp=calc_pr_rep_gain("rep_mc_tech_trainer","xs_g")        ## extra small gain
          $mc.give_xp("rep_mc_tech_trainer",temp)

      if senior_techie_none==1:                                                                ## all parts repaired...
        if senior_techie_some==0:                                                              ## ...no repairs were made: no damaged parts at start
          ""
          "There's nothing to do though; there are no damaged parts."
        else:                                                                                  ## ...must have made some repairs...
          if senior_techie_some_part==0:                                                       ## ...last bot made no repairs
            ""
            "All damaged parts were repaired, some {mark}Senior Techie bots{/} had nothing to do."
          else:                                                                                ## ...last bot did some repairs
            ""
            "All damaged parts were repaired. {mark}Senior Techie bots{/} are fantastic!"
          
    else:                                                               ##  no Senior Techie bots
##  set up columns and display MC thinking picture on left
##  GRAPHICS
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $st_imagenumber=randint(7,10)                                    ## MC thinking about having senior techie bots
      $action_image="roles senior_techie rst_"+str(st_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
##    TEXT
      $act.set_block("c")
## 0.10.n conditional text for bot(s) just assigned (only when no senior techies)
      if st_bot_new_assignment==0:    ## no bots just assigned
        "Maybe I should have {mark}Senior Techie{/} bots and keep them at home in capsules. They can repair parts by themselves and I'd have more time to do other things."
      elif st_bot_new_assignment==1:  ## 1 bot just assigned 
        "I just assigned a bot the {mark}Senior Techie{/} role so in the future they will fix parts by themselves and I can do other things."
      else:                           ## > 1 bot just assigned
        "I just assigned bots the {mark}Senior Techie{/} role so in the future they will fix parts by themselves and I can do other things."
##  clean up
    $assistant=None
    $assistants=None
    ""                                              ## add a line before the next item is displayed
  return

label senior_techie_fix_random_part(part_n):
  $part=workshop.inventory[int(part_n)]
  $part.integrity+=senior_techie_repair
  "{info}{size=-8}{i}{mark}[assistant]{/} repaired a damaged {mark}[part]{/}{/}{/}{/}"
  return

label senior_techie_fix_random_part_defect(part_n,defect):
  $part=workshop.inventory[int(part_n)]
  $defect=part.defects[int(defect)]
  $defect.fix_progress+=senior_techie_repair
  if defect.fix_progress==100:
    $part.defects.remove(defect)
  "{info}{size=-8}{i}{mark}[assistant]{/} fixed a defective {mark}[part]{/}{/}{/}{/}"
  return