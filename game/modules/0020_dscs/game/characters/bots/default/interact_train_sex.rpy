init python:
  sex_min=50         ##  Radnor's default min xp is 50
  sex_max=850        ##  Radnor's default max xp is 950 - 0.12.n psychocore influence potential boost so this went down
  sex_mod=25         ##  modifier: at 75% integrity default xp, higher more xp, lower less xp
  sex_actual=0       ##  actual xp modified by integrity
  asst_sex_min=50    ##  original default is 50
  asst_sex_max=350   ##  original default is 450, assistant less than bot - 0.12.n psychocore influence potential boost so this went down

define sex_training_bj_chance=50

define label_interact_default_train_sex_action_info={"cost":[("energy",1)]}

label interact_default_train_sex(bot):
  header "[bot] - Training: [bot.bot_sex]"
  call interact_include("train_sex_before")
  if bot.gender=="male":
## 0.14 Frankie bot requires that Bride of Frankie be E or better in sex (bedroom toy equivalent)
    if bot.model_id=="frankie_bot":
      $assistant=None                                            ## assume Bride not qualified
      $tmp_int=0
      while tmp_int<len(home.sexbots):                          ## Bride must be in capsule
        $tmp_bot=home.sexbots[tmp_int]
        if tmp_bot and tmp_bot.model_id=="frankie_bride_bot":   
            if tmp_bot.bot_sex.level>=2:                        ## E level is 2
              $assistant=tmp_bot                                ## assign Bride as assistant
        $tmp_int+=1
      if assistant==None:
        $act.start_block("l:440 c:content_width-440")
        $act.set_block("l")
        $action_image= "bots frankie_bride_bot avatar"  ## Bride of Frankie avatar
        center "{image=[action_image]@200x600}"
        ""
        $action_image= "bots frankie_bot avatar"        ## Frankie avatar
        center "{image=[action_image]@200x600}"
        $act.set_block("c")
        ""
        "You decide that sex training for {mark}Frankie{/} will always be with {mark}Bride of Frankie{/}. These special bots are too valuable to risk having something go wrong if they interact with your other bots."
        ""
        ""
        ""
        "You cannot train {mark}Frankie{/} in {mark}sex{/} until {mark}Bride of Frankie{/} is {mark}level E or better in sex{/}. This would qualify her as a {mark}bedroom toy{/} but for their protection I'm not assigning roles to these special bots."
        choice("end_bot_interaction",key="home") "Done"
        return
## 0.14 end of insertion, original 8 lines moved to 'else' clause for male bots other than Frankie
## note that 'assistants' are not actually used in sex training, it's only for the pictures
    else:
      $assistants=active_bots_with_role_tag("bedroom_toy")
      if assistants:                                        ## ONE OR MORE BEDROOM TOYS
        $assistant=randchoice(assistants)[0]                ##  SELECT ONE OF THE BEDROOM TOYS, NO DIFFERENCE IN OUTCOME
        "You get {mark}[assistant]{/} to help you with sex training for {mark}[bot]{/}."
      else:                                                 ##  NO ASSISTANTS AVAILABLE
##0.14 show male bot avatar
        $act.start_block("l:440 c:content_width-440")
        $act.set_block("l")
        center "{image=bots [bot.model_id] avatar@400x600}"
        ""
        $act.set_block("c")
        "Oops! I can't do sex training for {mark}[bot]{/} without a {mark}bedroom toy{/}."
        choice("end_bot_interaction",key="home") "Done"
        return

  $training_bj=randint(0,100)<sex_training_bj_chance
  if training_bj:
    $action_image=find_game_image_variant("bots [bot.model_id] :bj")
    if not action_image:
      $training_bj=False
  if training_bj:
    if bot.gender=="female":
      "Starting with oral you train [bot.posname] sexual skills by doing various penetration \"exercises\"."
    else:
      "Starting with oral you have [assistant] train [bot.posname] sexual skills by doing various penetration \"exercises\"."
  else:
    if bot.gender=="female":
      "You train [bot.posname] sexual skills by doing various penetration-based \"exercises\"."
    else:
      "You have [assistant] train [bot.posname] sexual skills by doing various penetration-based \"exercises\"."
  ""
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if training_bj:
    center "{image=[action_image]@400x600}"
    ""
  $action_image=find_game_image_variant("bots [bot.model_id] :sex")
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  if bot.gender=="female":                                                  ##  female bot training "as is"
    call break_warranty_seals(bot,("oral","vaginal","anal"),True)
    "You were a bit too {bad}rough{/} with [bot]."
    $bot.chassis.apply_damage("training_sex",(3,10))
    ""
    if bot.bot_sex<"D":
      "[bot.posname] skill is rather lacking..."
    elif bot.bot_sex>"B":
      "[bot] is great at sex, predicting your desires and providing amazing emotional feedback!"
    else:
      "[bot.posname] skill is adequate for commercial use."
  else:                                                                    ##  male bot training
##    call break_warranty_seals(bot,("oral","vaginal","anal"),False)         ##  0.12.n remove male bot warranty seals - assistant breaks bot's warranty seals
    "The training was a bit {bad}rough{/} on both [bot] and [assistant]."
##    call break_warranty_seals(assistant,("oral","vaginal","anal"),False)   ##  0.12.n bedroom toy cannot have intact seals - assistant possible warranty seal breakage-VERY UNLIKELY
    $assistant.chassis.apply_damage("training_sex",(3,10))                 ##  damage to assistant
    $bot.chassis.apply_damage("training_sex",(3,10))                       ##  damage to male bot
    ""
    if bot.bot_sex<"D":
      "[bot.posname] skill is rather lacking..."
    elif bot.bot_sex>"B":
      "[bot] is great at sex, predicting his partner's desires and providing amazing emotional feedback!"
    else:
      "[bot.posname] skill is adequate for commercial use."
  $mc.give_xp("mood",randint(10,11+25*bot.bot_sex.level))
  ""
  if mc.sex<bot.bot_sex:                            ##  bot is better at sex than MC, no benefit to bot
    if bot.gender=="male":                          ##  if male bot the assistant MIGHT benefit
      if mc.sex<assistant.bot_sex:                  ##  assistant is better at sex than MC, no benefit to assistant either
        "You failed to teach [bot] or [assistant] anything as they are both more experienced and versatile in sex than you are. At least you learned something yourself."
        $mc.give_xp("sex",randint(100,250))
      else:                                         ##  assistant gets some benefit (less than bot)
        "You failed to teach [bot] anything, as [bot.heshe] is more experienced and versatile in sex than you are. At least you and [assistant] both learned something."
        $mc.give_xp("sex",randint(100,250))
        $sex_actual=randint(asst_sex_min,asst_sex_max)  ##  was, 50-450

##        $print "Sex - Random Number: ",sex_actual
        
        $sex_actual=int(sex_actual*(assistant.chassis.integrity+sex_mod)/100)       ## 0.2.2  integrity added as an influence
        $sex_actual=int(sex_actual*(assistant.psychocore.stability+sex_mod)/100)    ## 0.12.n stability added as an influence
        
##        $print "Sex - Adjusted Final: ",sex_actual

        $assistant.give_xp("bot_sex",sex_actual)
    else:                                           ##  bot is female
        "You failed to teach [bot] anything as [bot.heshe] is more experienced and versatile in sex than you are. At least you learned something yourself."
        $mc.give_xp("sex",randint(100,250))
  else:                                             ##  bot is NOT better at sex than mc, bot benefits
    if bot.gender=="male":                          ##  bot is male so need to see about assistant
      if mc.sex<assistant.bot_sex:                  ##  assistant is better at sex than MC, no benefit to assistant
        "There is some improvement in [bot.posname] sex skill. You learned something too but the assistant is better at sex and learned nothing."
        $mc.give_xp("sex",randint(50,150))
        $sex_actual=randint(sex_min,sex_max)  ##  was, 50-950

##        $print "Sex random number: ",sex_actual

        $sex_actual=int(sex_actual*(bot.chassis.integrity+sex_mod)/100)       ## 0.2.2  integrity added as an influence
        $sex_actual=int(sex_actual*(bot.psychocore.stability+sex_mod)/100)    ## 0.12.n stability added as an influence
        
##        $print "Sex actual number: ",sex_actual

        $bot.give_xp("bot_sex",sex_actual)
      else:                                         ##  assistant is NOT better at sex than MC, assistant benefits too
        "There is some improvement in [bot.posname] sex skill. You and [assistant] both learned something too."
        $mc.give_xp("sex",randint(50,150))
        $sex_actual=randint(asst_sex_min,asst_sex_max)  ##  was, 50-450

##        $print "Sex - Random Number: ",sex_actual

        $sex_actual=int(sex_actual*(assistant.chassis.integrity+sex_mod)/100)       ## 0.2.2  integrity added as an influence
        $sex_actual=int(sex_actual*(assistant.psychocore.stability+sex_mod)/100)    ## 0.12.n stability added as an influence

##        $print "Sex - Adjusted Final: ",sex_actual

        $assistant.give_xp("bot_sex",sex_actual)
        $sex_actual=randint(sex_min,sex_max)  ##  was, 50-950

##        $print "Sex - Random Number: ",sex_actual

        $sex_actual=int(sex_actual*(bot.chassis.integrity+sex_mod)/100)       ## 0.2.2  integrity added as an influence
        $sex_actual=int(sex_actual*(bot.psychocore.stability+sex_mod)/100)    ## 0.12.n stability added as an influence

##        $print "Sex - Adjusted Final: ",sex_actual

        $bot.give_xp("bot_sex",sex_actual)
    else:                                          ##  bot is female
      "There is some improvement in [bot.posname] sex skill. You learned something too."
      $mc.give_xp("sex",randint(50,150))
      $sex_actual=randint(sex_min,sex_max)  ##  was, 50-950

##      $print "Sex - Random Number: ",sex_actual

      $sex_actual=int(sex_actual*(bot.chassis.integrity+sex_mod)/100)       ## 0.2.2  integrity added as an influence
      $sex_actual=int(sex_actual*(bot.psychocore.stability+sex_mod)/100)    ## 0.12.n stability added as an influence

##      $print "Sex - Adjusted Final: ",sex_actual
 
      $bot.give_xp("bot_sex",sex_actual)  ## 0.12.6 bug fix indentation
  $act.end_block()
  call interact_include("train_sex_after")
  call random_event("train_sex")
  if _return=="default":
    ## @@REPEAT_ACTION
    if show_repeat_action():
      if bot.chassis.is_disabled:
        interact(None,hint="{hint}bot is disabled{/}") "Repeat"
      else:
        interact("^train_sex") "Repeat"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
    choice("end_bot_interaction",pos=16,key="home") "Done"
    choice("<<<",pos=17,key="cancel") "Back"
  return
