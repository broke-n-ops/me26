##  Functions start with bot avatar on left and "result_text" from mission on right 
##  Output entered will be on right below "result_text"

label whore_bot_mission_results(bot):                 ##  Successful mission
  ""

##  mc/bot skill/rep gain                             ##  streetwalker whore, customer probably doesn't know who you are
  $temp=calc_pr_rep_gain("rep_mc_trainer","xs_g")     ##  trainer extra small GAIN - 0.012.n REVISION
  $mc.give_xp("rep_mc_trainer",temp)
  $temp=calc_pr_rep_gain("rep_mc_sexmachine","xs_g")  ##  sexmachine extra small GAIN - 0.012.n REVISION
  $mc.give_xp("rep_mc_sexmachine",temp)

  $bot.give_xp("bot_sex",randint(20,200))             ##  parameters copied from training sex
##  bot damage
  $bot.chassis.apply_damage("training_sex",(3,10))    ##  parameters copied from training sex
##  warranty seals
    ##  Radnor's 'whore' mission included this but a sex trained bot probably has broken seals.
  call break_warranty_seals(bot,by_mc=False)
##  picture
  ""
  $ps_imagenumber=random.randint(1,24)

## see what happens when you set picture to left
  $act.set_block("l")
  ""

  $action_image="missions whore srwm_"+str(ps_imagenumber)  ##  whore mission success pictures are 1-24
  center "{image=[action_image]@400x600}"
  ""

## go back to center column (not sure why it isn't "right")
  $act.set_block("c")
  
##  loot - weight parameters first, cube to increase differentiation, divide to make output reasonable, randomize +/- 25%
  $temp_1=bot.rate_level                     ##  bot rate weight  50
  $temp_2=bot.bot_sex.level                  ##  sex skill weight  100
  $temp_3a=bot.item_on_slot("bot_vagina")    ##  vagina weight  50
  if temp_3a:
    $temp_3=temp_3a.rate_level
  else:
    $temp_3=0
  $temp_4a=bot.item_on_slot("bot_skin")
  if temp_4a:
    $temp_4=temp_4a.rate_level              ##  skin weight  25
  else:
    $temp_4=0
  $temp_5a=bot.item_on_slot("bot_implants")
  if temp_5a:
    $temp_5=temp_5a.rate_level              ##  implants weight  25
  else:
    $temp_5=0
  $temp_6=bot.chassis.integrity               ##  integrity weight  1
  $temp_7=bot.psychocore.stability            ##  stability weight  1

##INFO FOR TESTING-formula used in companion .json file - This info is about success vs. failure, not payout
##  $temp_99=((bot.bot_combat.level+1.2)**2.2)*2.2
##  "Success Weight: [temp_99]"

##  ADD UP THE PARAMETERS
  $temp_6=temp_1*50+temp_2*100+temp_3*50+temp_4*25+temp_5*25+temp_6*1+temp_7*1
##  cube the value to introduce a larger spread
  $temp_7=temp_6**3
##  divide by 2,000,000 to put the result at a reasonable dollar level
  $temp_8=temp_7/2000000
##  randomize between 75% and 125%
  $temp_9=randint(temp_8*0.75, temp_8*1.25)
##  give the money
  $mc.money+=temp_9
##  mood increase
  $mc.mood.give_xp(randint(5,15))
  return

label whore_bot_mission_fight(bot):                       ##  Attempted robbery on way home: damage but keeps money
  ""

##  mc/bot skill/rep gain                                 ##  streetwalker whore, customer probably doesn't know who you are
  $temp=calc_pr_rep_gain("rep_mc_trainer","xs_g")    ##  trainer extra small GAIN - 0.12.n REVISION
  $mc.give_xp("rep_mc_trainer",temp)
  $temp=calc_pr_rep_gain("rep_mc_sexmachine","xs_g")      ##  sexmachine extra small GAIN - 0.12.n REVISION
  $mc.give_xp("rep_mc_sexmachine",temp)
  $temp=calc_pr_rep_gain("rep_mc_fighter","xs_g")         ##  fighter extra small GAIN - 0.12.n REVISION
  $mc.give_xp("rep_mc_fighter",temp)

  $bot.give_xp("bot_sex",randint(20,200))                 ##  parameters copied from training sex
  $bot.give_xp("bot_combat",randint(50,400))              ##  parameters copied from training combat: won fight
##  bot damage - combat (ignore sex to avoid duplication)
  $bot.chassis.apply_damage("training_combat",(15,45))    ##  copied from night school escort damage
##  warranty seals
    ##  Radnor's 'whore' mission included this but a sex trained bot probably has broken seals.
  call break_warranty_seals(bot,by_mc=False)
##  picture
  ""
  $ps_imagenumber=random.randint(25,32)

## see what happens when you set picture to left
  $act.set_block("l")
  ""

  $action_image="missions whore srwm_"+str(ps_imagenumber)  ##  whore mission success with damage pictures are 25-32
  center "{image=[action_image]@400x600}"
  ""

## go back to center column (not sure why it isn't "right")
  $act.set_block("c")

##  loot - weight parameters first, cube to increase differentiation, divide to make output reasonable, randomize +/- 25%
  $temp_1=bot.rate_level                     ##  bot rate weight  50
  $temp_2=bot.bot_sex.level                  ##  sex skill weight  100
  $temp_3a=bot.item_on_slot("bot_vagina")    ##  vagina weight  50
  if temp_3a:
    $temp_3=temp_3a.rate_level
  else:
    $temp_3=0
  $temp_4a=bot.item_on_slot("bot_skin")
  if temp_4a:
    $temp_4=temp_4a.rate_level              ##  skin weight  25
  else:
    $temp_4=0
  $temp_5a=bot.item_on_slot("bot_implants")
  if temp_5a:
    $temp_5=temp_5a.rate_level              ##  implants weight  25
  else:
    $temp_5=0
  $temp_6=bot.chassis.integrity               ##  integrity weight  1
  $temp_7=bot.psychocore.stability            ##  stability weight  1

##INFO FOR TESTING-formula used in companion .json file
##  $temp_99=((bot.bot_combat.level+1.2)**2.2)*2.2
##  "Success Weight: [temp_99]"

##  ADD UP THE PARAMETERS
  $temp_6=temp_1*50+temp_2*100+temp_3*50+temp_4*25+temp_5*25+temp_6*1+temp_7*1
##  cube the value to introduce a larger spread
  $temp_7=temp_6**3
##  divide by 1,000,000 to put the result at a reasonable dollar level
  $temp_8=temp_7/2000000
##  randomize between 75% and 125%
  $temp_9=randint(temp_8*0.75, temp_8*1.25)
##  give the money
  $mc.money+=temp_9
##  mood - no change, money good, beat up bot bad
  return

label whore_bot_mission_failure(bot):  ##  Robbed on the way home: damaged and lost money
  ""

##  mc/bot skill/rep gain                                 ##  streetwalker whore, customer probably doesn't know who you are
##                                                        ##  no trainer change sex gain and fight loss cancel each other out
  $temp=calc_pr_rep_gain("rep_mc_sexmachine","xs_g")      ##  extra small GAIN - 0.12.n REVISION
  $mc.give_xp("rep_mc_sexmachine",temp)
  if mc.rep_mc_fighter.level>1:                           ##  make sure you have a reputation to lose! - 0.12.n REVISION
    $temp=calc_pr_rep_gain("rep_mc_fighter","xs_l")       ##  extra small LOSS - 0.12.n REVISION
    $mc.give_xp("rep_mc_fighter",temp)

  $bot.give_xp("bot_sex",randint(20,200))                 ##  parameters copied from training sex
  $bot.give_xp("bot_combat",randint(25,250))              ##  parameters halved from training combat: lost fight
##  bot damage - combat (ignore sex to avoid duplication)
  $bot.chassis.apply_damage("training_combat",(15,45))    ##  copied from night school escort damage
##  warranty seals
    ##  Radnor's 'whore' mission included this but a sex trained bot probably has broken seals.
  call break_warranty_seals(bot,by_mc=False)
##  picture
  ""
  $ps_imagenumber=random.randint(33,40)

## see what happens when you set picture to left
  $act.set_block("l")
  ""

  $action_image="missions whore srwm_"+str(ps_imagenumber)  ##  whore mission failure with damage pictures are 33-40
  center "{image=[action_image]@400x600}"

## go back to center column (not sure why it isn't "right")
  $act.set_block("c")
  
##INFO FOR TESTING-formula used in companion .json file
##  $temp_99=((bot.bot_combat.level+1.2)**2.2)*2.2
##  "Success Weight: [temp_99]"

##  mood decrease
  $mc.mood.give_xp(randint(-30,-15))
  return