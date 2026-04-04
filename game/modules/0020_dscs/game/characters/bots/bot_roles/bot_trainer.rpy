## train random bot - model files:
##    workshop_stabilize_random_bot.rpy     modules 0020 game locations workshop
##    interact_train_nnnnnnn.rpy            modules 0020 game characters bots default
## Bot Trainer bots must be 'A' or 'S' level in the subject and in social skill, they are experts
## Trainee bots must have the skill to be trained, they need some familiarity with the subject given by a human trainer
## The Trainee bot receives about 2/3 the skill they would get from a human trainer
## The Bot Trainer does NOT gain skill from the training and they lose stability
## role happens on 'rest' but not on 'sleep' so 'home_rest.rpy' file has call but 'friends_with_benefits.rpy' does not
## role also happens on 'work' so 'home_work.rpy' file has call

##=========INIT VARIABLES=========

init python:
  trainer_integrity_min=90    ## minimum integrity for a bot to train another bot
  trainer_stability_min=75    ## minimum stability for a bot to train another bot
  trainee_integrity_min=75    ## minimum integrity for a bot to be trained
  trainee_stability_min=75    ## minimum stability for bot to be trained
  trainer_xp_min=40           ## minimum training is 80% of what MC minimum which is 50
  trainer_subt=9              ## for training calculations - 'subt'
  trainer_max_mult=140        ## for training maximum calculation: formula is ('social skill' + 'subject skill - 'subt') * 'max mult'
  trainer_stab_min=1          ## minimum stability loss by trainer
  trainer_stab_max=3          ## maximum stability loss by trainer
  training_mod=25             ## copy normal MC adjustment, >75% integrity benefits, <75% integrity suffers
    
##========PYTHON FUNCTIONS======== (still under 'init python:')

  def trainer_get_trainable_bots(trainer_bot):
    bots=[]
    for bot in home.sexbots:
      if bot:
        if not bot["mission"]:                                                                                    ## test 1 - trainee not on mission

##          print "Inside called function: Testing pair - trainer: ",trainer_bot," skill: ",trainer_bot.trainer_subject," candidate bot: ",bot," skill: ",bot.trainee_subject

          if trainer_bot.trainer_subject==bot.trainee_subject:                                                  ## test 2 - trainer/trainee subject match
            if bot.chassis.integrity>trainee_integrity_min and bot.psychocore.stability>trainee_stability_min:  ## test 3 - trainee stability and integrity sufficient
              if trainer_bot.trainer_subject=="Combat":
                if trainer_bot.bot_combat.level>bot.bot_combat.level+1:                                         ## test 4a - trainer 2 steps above trainee, also weeds out training yourself
                  
##                  print "Inside called function: Viable Combat Pair - trainer: ",trainer_bot," trainee: ",bot
                  
                  bots.append(bot)
              elif trainer_bot.trainer_subject=="Electronics":
                if trainer_bot.bot_electronics.level>bot.bot_electronics.level+1:                               ## test 4b - trainer 2 steps above trainee, also weeds out training yourself

##                  print "Inside called function: Viable Electronics Pair - trainer: ",trainer_bot," trainee: ",bot

                  bots.append(bot)                
              elif trainer_bot.trainer_subject=="Mechanics":
                if trainer_bot.bot_mechanics.level>bot.bot_mechanics.level+1:                                   ## test 4c - trainer 2 steps above trainee, also weeds out training yourself

##                  print "Inside called function: Viable Mechanics Pair - trainer: ",trainer_bot," trainee: ",bot

                  bots.append(bot)                
              else:    ## must be sex
                if trainer_bot.bot_sex.level>bot.bot_sex.level+1:                                               ## test 4d - trainer 2 steps above trainee, also weeds out training yourself

##                  print "Inside called function: Viable Sex Pair - trainer: ",trainer_bot," trainee: ",bot,

                  bots.append(bot)                
    return bots

  def trainer_get_random_trainable_bot(trainer_bot):
    bots=trainer_get_trainable_bots(trainer_bot)
    return randchoice(bots) if bots else None

##============RENPY FUNCTIONS============

label role_bot_trainer_train:
  if not now("night"):                                                          ## no training at night, recharging
    $assistants=active_bots_with_role_tag("bot_trainer")                        ## find all active 'bot_trainer' bots
    $bt_bot_new_assignment=0                                                    ## clear flag before starting
    $bot_count=0
    while bot_count<len(assistants):                                            ## go through assistants to remove ones just assigned
      $temp_bot=assistants[bot_count]
      if temp_bot[0].bt_just_assigned==1:                                       ## if assigned role this turn
        $bt_bot_new_assignment+=1                                               ## increment count of bots just assigned
        $assistants.pop(bot_count)                                              ## remove bot from assistants - do not increment counter since 1 removed
      else:
        $bot_count+=1                                                           ## increment bot count for while loop
    if assistants:                                                              ## at least one 'bot_trainer' is available after removing 'just assigned' bots
      $bot_count=0
      $trainers_for_image=[]                                                    ## list of trainers that have viable trainees for image

##      $print "Starting loop looking for trainers to use in picture"

      while bot_count<len(assistants):                                          ## loop to create list of viable trainers for image if not 'None' at least 1 training will occur
        $trainer_bot=find_character(assistants[bot_count][0])                   ## get a trainer

##        $print "Beginning search for a trainee bot for training bot: ",trainer_bot

        $trainee_bot=trainer_get_random_trainable_bot(trainer_bot)              ## find out if there is an available trainee for this trainer

##        $print "One of the viable trainee bots found or 'None': ",trainee_bot

        ## next line, determine if trainer will work: stable, sufficient integrity, available trainee
        if trainer_bot.psychocore.stability>=trainer_stability_min and trainer_bot.chassis.integrity>=trainer_integrity_min and trainee_bot:
          $trainers_for_image.append(trainer_bot)                               ## add to candidate bots for image - this is actual bot NOT an object at ...

##          $print "Adding viable trainer to candidate list, trainer: ",trainer_bot," (trainee found is irrelevant at this time)"

        $bot_count+=1

##      $print "Completed search for viable trainers, candidates for picture:"
##      $print trainers_for_image
##      $print "Starting search to select which candidate which will be in the picture and their trainee" 

      if len(trainers_for_image)>0:                                             ## >=1 viable trainer/trainee pair - >= 1 training will occur, 
        $assistant_trainer=randchoice(trainers_for_image)                       ## list is actual bots, no conversion required
        $assistant_trainee=trainer_get_random_trainable_bot(assistant_trainer)  ## select trainee - object at ...
      else:                                                                     ## no viable trainer/trainee pairs - no training will happen
        $assistant_trainer=randchoice(assistants)[0]                            ## select any trainer, doesn't matter
        $assistant_trainee=None                                                 ## no trainee, use as flag for picture selection

##      $print "Selected final pair for picture - trainer: ",assistant_trainer,"  trainee: ",assistant_trainee," (trainee could be 'None')"

## GRAPHICS
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      if assistant_trainer.trainer_subject=="Combat":
        if assistant_trainer.gender=="female" and assistant_trainee==None:               ## female trainer/no trainee
          $mt_imagenumber=randint(42,44)
        elif assistant_trainer.gender=="male" and assistant_trainee==None:               ## male trainer/no trainee  
          $mt_imagenumber=randint(45,46)
        elif assistant_trainer.gender=="female" and assistant_trainee.gender=="female":  ## female trainer / female trainee
          $mt_imagenumber=randint(1,8)
        elif assistant_trainer.gender=="female" and assistant_trainee.gender=="male":    ## female trainer / male trainee
          $mt_imagenumber=randint(9,10)
        elif assistant_trainer.gender=="male" and assistant_trainee.gender=="female":    ## male trainer / female trainee
          $mt_imagenumber=randint(11,14)
        else:                                                                            ## male trainer / male trainee
          $mt_imagenumber=randint(15,16)
      elif assistant_trainer.trainer_subject=="Sex":
        if assistant_trainer.gender=="female" and assistant_trainee==None:               ## female trainer/no trainee
          $mt_imagenumber=randint(47,49)
        elif assistant_trainer.gender=="male" and assistant_trainee==None:               ## male trainer/no trainee
          $mt_imagenumber=randint(50,51)
        elif assistant_trainer.gender=="female":                                         ## female trainer / male trainee
          $mt_imagenumber=randint(27,35)
        else:                                                                            ## male trainer / male trainee
          $mt_imagenumber=randint(36,41)
      else:  ## must be Electronics or Mechanics
        if assistant_trainer.gender=="female" and assistant_trainee==None:               ## female trainer/no trainee
          $mt_imagenumber=randint(52,53)
        elif assistant_trainer.gender=="male" and assistant_trainee==None:               ## male trainer/no trainee  
          $mt_imagenumber=54
        elif assistant_trainer.gender=="female" and assistant_trainee.gender=="female":  ## female trainer / female trainee
          $mt_imagenumber=randint(17,20)
        elif assistant_trainer.gender=="female" and assistant_trainee.gender=="male":    ## female trainer / male trainee
          $mt_imagenumber=randint(21,22)
        elif assistant_trainer.gender=="male" and assistant_trainee.gender=="female":    ## male trainer / female trainee
          $mt_imagenumber=randint(23,24)
        else:                                                                            ## male trainer / male trainee
          $mt_imagenumber=randint(25,26)

      $action_image="roles bot_trainer bt_"+str(mt_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
## TEXT
      $act.set_block("c")
      if len(trainers_for_image)>0:                                 ## >=1 viable trainer/trainee pair - >= 1 training will occur
        if len(assistants)==1:                                      ## singular bot trainer
          "It's great that my {mark}Bot Trainer{/} bot can train other bots by themself!"
        else:                                                       ## multiple bot trainers
          "It's great that my {mark}Bot Trainer{/} bots can train bots by themselves!"
      else:                                                         ## assistants but no trainable bots
        if len(assistants)==1:                                      ## singular bot trainer'
          "Unfortunately my {mark}Bot Trainer{/} bot had no available bots to train."
        else:                                                       ## multiple bot trainers
          "Unfortunately my {mark}Bot Trainer{/} bots had no available bots to train."

## MAIN SECTION, THIS IS WHERE BOTS GET TRAINED!
      if len(trainers_for_image)>0:                                 ## >=1 viable trainer/trainee pair - >= 1 training will occur
        $while_end=len(assistants)
        $while_counter=0
## START OF WHILE LOOP

##        $print "Beginning actual training loop"

        while while_counter<while_end:
          $assistant=find_character(assistants[while_counter][0])
          if assistant.psychocore.stability>=trainer_stability_min and assistant.chassis.integrity>=trainer_integrity_min:  ## trainer requirements met
            if assistant!=assistant_trainer:                         ## NOT the trainer in image
              $temp_bot=trainer_get_random_trainable_bot(assistant)
            
##              $print "Training Loop - trainer: ",assistant," trainee: ",temp_bot," skill: ",assistant.trainer_subject
            
            else:                                                    ## trainer in image        
              $temp_bot=assistant_trainee                            ## call up the previously selected trainee
              
##              $print "Training Loop - Pictured assistant - trainer: ",assistant," trainee: ",temp_bot," skill: ",assistant.trainer_subject

            if temp_bot:                                             ## a candidate bot to train was found
              if assistant.trainer_subject=="Combat":
                $bot_trainer_value=assistant.bot_social.level+assistant.bot_combat.level
                $actual_skill="bot_combat"
              elif assistant.trainer_subject=="Electronics":
                $bot_trainer_value=assistant.bot_social.level+assistant.bot_electronics.level
                $actual_skill="bot_electronics"
              elif assistant.trainer_subject=="Mechanics":
                $bot_trainer_value=assistant.bot_social.level+assistant.bot_mechanics.level
                $actual_skill="bot_mechanics"
              elif assistant.trainer_subject=="Sex":
                $bot_trainer_value=assistant.bot_social.level+assistant.bot_sex.level
                $actual_skill="bot_sex"
              else:            ## SHOULD NOT BE ABLE TO HAPPEN BUT JUST IN CASE
                $bot_trainer_value=assistant.bot_social.level   
          
##              $print "bot_trainer_value: ",bot_trainer_value; " should be 12, 13, or 14"
          
              $temp_max=(bot_trainer_value-trainer_subt)*trainer_max_mult  ## parameters declared at top of function, empirically determined to make desired range
          
##              $print "Maximum XP for trainee: ",temp_max," (min is declared =40)"
          
              $trainee_xp_value=randint(trainer_xp_min,temp_max)           ## min parameter declared at top of function, final range 40 to 700 (comparison: MC range is 50 to 850)

##              $print "Random result XP for trainee: ",temp_bot," skill: ",actual_skill," xp gain: ",trainee_xp_value

              if actual_skill=="bot_combat":
                $t_text="Combat"
              elif actual_skill=="bot_electronics":
                $t_text="Electronics"
              elif actual_skill=="bot_mechanics":
                $t_text="Mechanics"
              else:
                $t_text="Sex"
              "{info}{size=-8}{i}{mark}[assistant]{/} trained {mark}[temp_bot]{/} in {mark}[t_text]{/}{/}{/}{/}"
              if actual_skill=="bot_combat":
                $assistant.chassis.apply_damage("training_combat",(1,5))          ## trainer small combat damage
                $temp_bot.chassis.apply_damage("training_combat",(3,10))          ## trainee normal combat training damage
              elif actual_skill=="bot_sex":
                $assistant.chassis.apply_damage("training_sex",(3,10))            ## trainer normal sex damage
                $temp_bot.chassis.apply_damage("training_sex",(3,10))             ## trainee normal sex damage
              else:                                                               ## elec or mech, trainer stability reduced manually
                $trainer_value=random.randint(trainer_stab_min,trainer_stab_max)  ## trainer lose between 1 and 3
                $assistant.psychocore.stability-=trainer_value
              $trainee_xp_value=int(trainee_xp_value*(temp_bot.chassis.integrity+training_mod)/100)     ## modify training based upon trainee integrity
              $trainee_xp_value=int(trainee_xp_value*(temp_bot.psychocore.stability+training_mod)/100)

##              $print "Adjusted Training XP: ",trainee_xp_value

              $temp_bot.give_xp(actual_skill,trainee_xp_value)                    ## only trainee benefits from training
            else:                                                                 ## this assistant had no bots to train
              "{info}{size=-8}{i}{mark}[assistant]{/} had no bots to train{/}{/}{/}"
          else:                                                                   ## bot trainer stability or integrity too low, cannot train
            if assistant.psychocore.stability>=trainer_stability_min:             ## stability OK: integrity must be too low
              "{info}{size=-8}{i}{mark}[assistant]{/} {bad}cannot work{/}-{mark}low integrity{/}{/}{/}{/}"
            elif assistant.chassis.integrity>=trainer_integrity_min:                 ## integrity OK: stability must be too low
              "{info}{size=-8}{i}{mark}[assistant]{/} {bad}cannot work{/}-{mark}low stability{/}{/}{/}{/}"
            else:                                                               ## both stability and integrity too low
              "{info}{size=-8}{i}{mark}[assistant]{/} {bad}cannot work{/}-{mark}low integrity&stability{/}{/}{/}{/}"
          $while_counter+=1

##      $print "Finished all training loops"

## end of actions, picture, and text when there was at least 1 trainer including picture and text
## includes if there were no trainees and no actual training occurred

    else:                                                                       ##  no Bot Trainer bots
##  set up columns and display MC thinking picture on left
##  GRAPHICS
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $mt_imagenumber=randint(10,12)                                            ## MC thinking about having bot trainer bots - re-used from mt
      $action_image="roles master_techie rmt_"+str(mt_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
##    TEXT
      $act.set_block("c")
      if bt_bot_new_assignment==0:    ## no bots just assigned
        "Maybe I should have {mark}Bot Trainer{/} bots and keep them at home in capsules. They can train other by themselves and I'd have more time to do other things."
      elif bt_bot_new_assignment==1:  ## 1 bot just assigned 
        "I just assigned a bot the {mark}Bot Trainer{/} role so in the future they will train other bots by themselves and I can do other things."
      else:                           ## > 1 bot just assigned
        "I just assigned bots the {mark}Bot Trainer{/} role so in the future they will train other bots by themselves and I can do other things."
##  clean up
    $assistant=None
    $assistants=None
    ""                 ## add a line before the next item is displayed
  return