##  Functions start with bot avatar on left and "result_text" from mission on right 
##  Output entered will be on right below "result_text"

label gigolo_bot_mission_client_a(bot):               ##  Successful mission with dominating older woman in bedroom
  ""
##  mc/bot skill/rep gain                             ##  woman client made appointment, they know who you are and tell friends
  $temp=calc_pr_rep_gain("rep_mc_trainer","l_g")      ##  trainer large GAIN - 0.012.n REVISION
  $mc.give_xp("rep_mc_trainer",temp)
  $temp=calc_pr_rep_gain("rep_mc_sexmachine","l_g")   ##  sexmachine large GAIN - 0.012.n REVISION
  $mc.give_xp("rep_mc_sexmachine",temp)
  $bot.give_xp("bot_sex",randint(20,200))             ##  parameters copied from training sex
##  bot damage
  $bot.chassis.apply_damage("training_sex",(20,55))   ##  training sex with increased intensity because of dominatrix - normal (3,10) - combat normal (15,45)
##  warranty seals
    ##  Radnor's 'whore' mission included this but a sex trained bot probably has broken seals.
  call break_warranty_seals(bot,by_mc=False)
##  picture
  ""
  $ps_imagenumber=random.randint(1,3)
  $act.set_block("l")
  ""
  $action_image="missions gigolo srgm_"+str(ps_imagenumber)  ##  gigolo mission Simon success pictures are 1-3
  center "{image=[action_image]@400x600}"
  ""
## go back to center column (not sure why it isn't "right")
  $act.set_block("c")
##  loot - weight parameters and add them up
  $temp_1=bot.rate_level                     ##  bot rate weight   2
  $temp_2=bot.bot_sex.level                  ##  sex skill weight  5
  $temp_3=bot.bot_social.level               ##  sex skill weight  3
  $temp_4a=bot.item_on_slot("bot_penis")     ##  penis weight      2
  if temp_4a:
    $temp_4=temp_4a.rate_level
  else:
    $temp_4=0
##  SUM WEIGHTED PARAMETERS
  $temp_5=temp_1*2+temp_2*5+temp_3*3+temp_4*2
##  APPLY CONDITIONAL and GIVE MONEY - Client a dominatrix pays the most
  if temp_5<=40:          ##  All D Bot except C Sex Skill is 41
    $mc.money+=500
  elif temp_5<=52:        ##  All C Bot except B Sex Skill is 53
    $mc.money+=1000
  elif temp_5<=64:        ##  All B Bot except A Sex Skill is 65
    $mc.money+=2000
  elif temp_5<=76:        ##  All B Bot except A Sex Skill is 65
    $mc.money+=5000
  else:                   ##  At least all A Bot with S Sex Skill
    $mc.money+=10000
##  mood increase
  $mc.mood.give_xp(randint(5,15))
  return

label gigolo_bot_mission_client_b(bot):              ##  Successful mission with submisive business woman in office
  ""
##  mc/bot skill/rep gain                            ##  woman client made appointment, they know who you are and tell friends
  $temp=calc_pr_rep_gain("rep_mc_trainer","m_g")     ##  trainer medium GAIN - 0.012.n REVISION
  $mc.give_xp("rep_mc_trainer",temp)
  $temp=calc_pr_rep_gain("rep_mc_sexmachine","m_g")  ##  sexmachine medium GAIN - 0.012.n REVISION
  $mc.give_xp("rep_mc_sexmachine",temp)
  $bot.give_xp("bot_sex",randint(20,200))            ##  parameters copied from training sex
##  bot damage
  $bot.chassis.apply_damage("training_sex",(3,10))   ##  training sex with normal parameters
##  warranty seals
    ##  Radnor's 'whore' mission included this but a sex trained bot probably has broken seals.
  call break_warranty_seals(bot,by_mc=False)
##  picture
  ""
  $ps_imagenumber=random.randint(4,6)
  $act.set_block("l")
  ""
  $action_image="missions gigolo srgm_"+str(ps_imagenumber)  ##  gigolo mission Quinton success pictures are 4-6
  center "{image=[action_image]@400x600}"
  ""
## go back to center column (not sure why it isn't "right")
  $act.set_block("c")
##  loot - weight parameters and add them up
  $temp_1=bot.rate_level                     ##  bot rate weight   2
  $temp_2=bot.bot_sex.level                  ##  sex skill weight  5
  $temp_3=bot.bot_social.level               ##  sex skill weight  3
  $temp_4a=bot.item_on_slot("bot_penis")     ##  penis weight      2
  if temp_4a:
    $temp_4=temp_4a.rate_level
  else:
    $temp_4=0
##  SUM WEIGHTED PARAMETERS
  $temp_5=temp_1*2+temp_2*5+temp_3*3+temp_4*2
##  APPLY CONDITIONAL and GIVE MONEY - Client b submissive pays middle amount
  if temp_5<=40:          ##  All D Bot except C Sex Skill is 41
    $mc.money+=400
  elif temp_5<=52:        ##  All C Bot except B Sex Skill is 53
    $mc.money+=800
  elif temp_5<=64:        ##  All B Bot except A Sex Skill is 65
    $mc.money+=1500
  elif temp_5<=76:        ##  All B Bot except A Sex Skill is 65
    $mc.money+=3500
  else:                   ##  At least all A Bot with S Sex Skill
    $mc.money+=7500
##  mood increase
  $mc.mood.give_xp(randint(5,15))
  return

label gigolo_bot_mission_client_c(bot):              ##  Successful mission with crazy/kinky cyberpunk woman in apartment
  ""
##  mc/bot skill/rep gain
  $temp=calc_pr_rep_gain("rep_mc_trainer","s_g")     ##  trainer small GAIN - kinky woman - 0.012.n REVISION
  $mc.give_xp("rep_mc_trainer",temp)
  $temp=calc_pr_rep_gain("rep_mc_sexmachine","s_g")  ##  sexmachine small GAIN - 0.012.n REVISION
  $mc.give_xp("rep_mc_sexmachine",temp)
  $bot.give_xp("bot_sex",randint(20,200))            ##  parameters copied from training sex
##  bot damage
  $bot.chassis.apply_damage("training_sex",(6,20))   ##  training sex with 2x normal parameters
##  warranty seals
    ##  Radnor's 'whore' mission included this but a sex trained bot probably has broken seals.
  call break_warranty_seals(bot,by_mc=False)
##  picture
  ""
  $ps_imagenumber=random.randint(7,9)
  $act.set_block("l")
  ""
  $action_image="missions gigolo srgm_"+str(ps_imagenumber)  ##  gigolo mission Raze success pictures are 7-9
  center "{image=[action_image]@400x600}"
  ""
## go back to center column (not sure why it isn't "right")
  $act.set_block("c")
##  loot - weight parameters and add them up
  $temp_1=bot.rate_level                     ##  bot rate weight   2
  $temp_2=bot.bot_sex.level                  ##  sex skill weight  5
  $temp_3=bot.bot_social.level               ##  sex skill weight  3
  $temp_4a=bot.item_on_slot("bot_penis")     ##  penis weight      2
  if temp_4a:
    $temp_4=temp_4a.rate_level
  else:
    $temp_4=0
##  SUM WEIGHTED PARAMETERS
  $temp_5=temp_1*2+temp_2*5+temp_3*3+temp_4*2
##  APPLY CONDITIONAL and GIVE MONEY - Client c crazy/kinky pays the least
  if temp_5<=40:          ##  All D Bot except C Sex Skill is 41
    $mc.money+=300
  elif temp_5<=52:        ##  All C Bot except B Sex Skill is 53
    $mc.money+=600
  elif temp_5<=64:        ##  All B Bot except A Sex Skill is 65
    $mc.money+=1000
  elif temp_5<=76:        ##  All B Bot except A Sex Skill is 65
    $mc.money+=2500
  else:                   ##  At least all A Bot with S Sex Skill
    $mc.money+=5000
##  mood increase
  $mc.mood.give_xp(randint(5,15))
  return

label gigolo_bot_mission_robbed(bot):                     ##  Robbery on way home: damage and lost money
  ""
##  mc/bot skill/rep gain - no trainer change sex gain and fight loss cancel each other out
  $temp=randint(1,3)                                      ##  need to select which client bot went to: dominatrix, business woman, kinky woman
  if temp==1:
    $temp=calc_pr_rep_gain("rep_mc_sexmachine","l_g")     ##  trainer large GAIN - dominatrix - 0.012.n REVISION
  elif temp==2:
    $temp=calc_pr_rep_gain("rep_mc_sexmachine","m_g")     ##  trainer medium GAIN - business woman - 0.012.n REVISION
  else:
    $temp=calc_pr_rep_gain("rep_mc_sexmachine","s_g")     ##  trainer medium GAIN - kinky woman - 0.012.n REVISION
  $mc.give_xp("rep_mc_sexmachine",temp)
  if mc.rep_mc_fighter.level>1:                           ##  make sure you have a reputation to lose! - 0.12.n REVISION
    $temp=calc_pr_rep_gain("rep_mc_fighter","m_l")        ##  medium LOSS - 0.12.n REVISION
    $mc.give_xp("rep_mc_fighter",temp)
  $bot.give_xp("bot_sex",randint(20,200))                 ##  parameters copied from training sex
  $bot.give_xp("bot_combat",randint(25,250))              ##  parameters from training combat halved: lost fight
##  bot damage - combat (ignore sex to avoid duplication)
  $bot.chassis.apply_damage("training_combat",(15,45))    ##  copied from night school escort damage
##  warranty seals
    ##  Radnor's 'whore' mission included this but a sex trained bot probably has broken seals.
  call break_warranty_seals(bot,by_mc=False)
##  picture
  ""
  $ps_imagenumber=random.randint(13,15)
  $act.set_block("l")
  ""
  $action_image="missions gigolo srgm_"+str(ps_imagenumber)  ##  gigolo mission robbed on way home pictures are 13-15
  center "{image=[action_image]@400x600}"
  ""
## go back to center column (not sure why it isn't "right")
  $act.set_block("c")
##  mood - beat up bot and no money
  $mc.mood.give_xp(randint(-15,-5))
  return

label gigolo_bot_mission_mugged(bot):                     ##  Mugged on the way (never made appointment): damaged and no money
  ""
##  mc/bot skill/rep gain
  if mc.rep_mc_fighter.level>1:                           ##  make sure you have a reputation to lose!
    $temp=calc_pr_rep_gain("rep_mc_fighter","xs_l")       ##  extra small LOSS, thugs probably don't know who you are - 0.12.n REVISION
    $mc.give_xp("rep_mc_fighter",temp)
  $bot.give_xp("bot_combat",randint(25,250))              ##  parameters halved from training combat: lost fight
##  bot damage - combat (ignore sex to avoid duplication)
  $bot.chassis.apply_damage("training_combat",(15,45))    ##  copied from night school escort damage
##  warranty seals
    ##  Radnor's 'whore' mission included this but a sex trained bot probably has broken seals.
##  call break_warranty_seals(bot,by_mc=False)
##  picture
  ""
  $ps_imagenumber=random.randint(10,12)
  $act.set_block("l")
  ""
  $action_image="missions gigolo srgm_"+str(ps_imagenumber)  ##  gigolo mission robbed on way home pictures are 10-12
  center "{image=[action_image]@400x600}"
## go back to center column (not sure why it isn't "right")
  $act.set_block("c")

##INFO FOR TESTING-formula used in companion .json file
##  $temp_99=((bot.bot_combat.level+1.2)**2.2)*2.2
##  "Success Weight: [temp_99]"

##  large mood decrease, beat up bot, no money AND client pissed (missed appt.)
  $mc.mood.give_xp(randint(-40,-20))
  return