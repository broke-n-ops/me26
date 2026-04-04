##  Initialize variables - IN MALE FIGHT .rpy FILE ONLY: OMIT FROM FEMALE FIGHT .rpy FILE
init python:
  ufc_fight_level=3         ##  set in entry function based (D,C,B,A,S = 3,4,5,6,7 - use in consolidated functions
  ufc_bot=[]                ##  set in entry function - use in consolidated functions
  ufc_mission_title=""      ##  set in entry function - use in consolidated functions
  ufc_rate_eval=0           ##  portion of bot evaluation dependent upon bot rating, depends upon fight class level
  ufc_rate_weight=7         ##  weight applied to bot eval
  ufc_parts_eval=0          ##  portion of bot evaluation dependent upon parts in bot, depends upon fight class level
  ufc_bot_part=""           ##  part name on a slot, used to get part's rate_level
  ufc_part_level=0          ##  level of part found on a slot
  ufc_parts_weight=1.4     ##  weight applied to parts evaluation for cheating calculation
  ufc_bot_eval=0            ##  final evaluation of bot, depends upon fight level, weighted sum of bot and parts
  ufc_win_loss_weight=0.33  ##  bot evaluation affects cheating more than win/loss
  ufc_combat_weight=7       ##  weight to apply to bot's combat skill difference vs fight level
  ufc_won_fight=0           ##  0 =lost, 1=won
  ufc_buy_bot_mult=2500     ##  multiply bot rate by this to buy back your bot after cheating
  ufc_bot_price=0           ##  value to pay for bot's return: bot.rate * ufc_buy_bot_mult
  ufc_opponent=1            ##  which opponent is involved in the current fight, values are 1 or 2
  ufc_imagenumber=0         ##  image number for display and for referencing next image
  ufc_d_prize_money=2500    ##  prize money for a D class bot fight
  ufc_c_prize_money=5000    ##  prize money for a C class bot fight
  ufc_b_prize_money=10000    #  prize money for a B class bot fight
  ufc_a_prize_money=20000   ##  prize moned for a A class bot fight
  ufc_o_prize_money=50000   ##  prize money for a Open bot fight
  ufc_win_weight=3          ##  multiplier for number of bot's wins
  ufc_loss_weight=2         ##  multiplier for number of bot's losses
  ufc_d_bot_offer=10000     ##  offer price for D bot
  ufc_c_bot_offer=20000     ##  offer price for C bot
  ufc_b_bot_offer=50000     ##  offer price for B bot
  ufc_a_bot_offer=100000    ##  offer price for A bot
  ufc_s_bot_offer=500000    ##  offer price for S bot
  ufc_bonus_offer=2         ##  multiplier for high offer
  ufc_buy_offer=0           ##  final price for owner to buy bot
  ufc_low_offer=3           ##  wins required for low buy offer
  ufc_high_offer=5          ##  wins required for high buy offer
  ufc_final_offer=6         ##  wins required for final offer hint
  ufc_loss_limit=5          ##  maximum lost fights for by offer
  ufc_called_owner=0        ##  flag for calling owner, set to 1 when you do it
  ufc_integrity_zero=95     ##  above is benefit, below is handicap
  ufc_integrity_weight=0.8  ##  integrity weight
##  ufc_stability_zero=75     ##  above is benefit, below is handicap  - no longer used
##  ufc_stability_weight=0.2  ##  stability weight  - no longer used
  ufc_stability_loss=0      ##  stability loss from fight
  ufc_stb_lost_max=15       ##  lost fight: max stability loss
  ufc_stb_lost_min=5        ##  lost fight: min stability loss
  ufc_stb_won_max=6         ##  won fight: max stability loss
  ufc_stb_won_min=2         ##  won fight: min stability loss

##  3 LINES BELOW ARE FOR TESTING, OVERWRITES THRESHOLDS
##  ufc_low_offer=1           ##  wins required for low buy offer
##  ufc_high_offer=2          ##  wins required for high buy offer
##  ufc_final_offer=3         ##  wins required for final offer hint

##=======ENTRY FUNCTIONS - 1 FOR EACH FIGHT CLASS=========

label ufc_male_outcome_d(bot):    ##  entry function for a D class fight
  $ufc_fight_level=3
  $ufc_bot=bot
  $ufc_mission_title="UFC Male D"
  $ufc_opponent=random.randint(1,2)
  call ufc_male_fight_scene
  return

label ufc_male_outcome_c(bot):    ##  entry function for a C class fight
  $ufc_fight_level=4
  $ufc_bot=bot
  $ufc_mission_title="UFC Male C"
  call ufc_male_fight_scene
  return

label ufc_male_outcome_b(bot):    ##  entry function for a B class fight
  $ufc_fight_level=5
  $ufc_bot=bot
  $ufc_mission_title="UFC Male B"
  call ufc_male_fight_scene
  return

label ufc_male_outcome_a(bot):    ##  entry function for an A class fight
  $ufc_fight_level=6
  $ufc_bot=bot
  $ufc_mission_title="UFC Male A"
  call ufc_male_fight_scene
  return

label ufc_male_outcome_s(bot):    ##  entry function for an S class fight
  $ufc_fight_level=7
  $ufc_bot=bot
  $ufc_mission_title="UFC Male Open"
  call ufc_male_fight_scene
  return

##=================DISPLAY FUNCTIONS=====================

label ufc_male_fight_scene:          ##  1st screen - bot fighting in arena
##  header already displayed by the 'mission_finished' function before calling bypass
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [ufc_bot.model_id] avatar@240x360}"
  $act.set_block("c")
  "{good}UFC fight on!{/} During the fight sometimes {mark}[ufc_bot.name]{/} does well..."
  if ufc_opponent==1:                                      ## fighting opponent 1
    $ufc_imagenumber=random.randint(1,8)                   ## hitting pictures
  else:                                                    ## fighting opponent 2
    $ufc_imagenumber=random.randint(31,38)                 ## hitting pictures
  $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  "... and sometimes {mark}[ufc_bot.name]{/} doesn't do so well. Tough fight!"
  if ufc_opponent==1:                                      ## fighting opponent 1
    $ufc_imagenumber=random.randint(9,16)                  ## hitting pictures
  else:                                                    ## fighting opponent 2
    $ufc_imagenumber=random.randint(39,46)                 ## hitting pictures
  $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"

##  "inside ufc_male_fight_scene, display an image and text showing the bot fighting"

  choice("ufc_male_determine_outcome") "Win or Lose?"
  return

label ufc_male_caught_cheating:                                ##  2nd screen if cheating, no room for avatar on this screen
  header "[ufc_bot.name] - {mark}[ufc_mission_title]{/} mission"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if ufc_opponent==1:                                      ## fighting opponent 1
    $ufc_imagenumber=random.randint(25,26)                 ## caught cheating
    $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
    center "{image=[action_image]@400x600}"
  else:                                                    ## fighting opponent 2
    $ufc_imagenumber=random.randint(55,56)                 ## caught cheating
    $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
    center "{image=[action_image]@400x600}"
  ""
  $ufc_imagenumber=random.randint(61,62)                   ## owner calls
  $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")

  $ufc_bot_price=ufc_buy_bot_mult*ufc_bot.rate_level
  "I received a call from the owner of the {mark}'Fuck Em Up'{/} club:"
  ""
  "{say}Hey Asshole, we caught your little trick! I'm sure you know that your bot didn't belong in the class you entered [ufc_bot.himher] in. If you read the 'fine print' you know we've confiscated your bot. If you come in right now we'll sell it back to you for{/} {bad}$[ufc_bot_price]{/}{say}. You've got 1 hour or we're keeping the bot.{/}"
  ""
  "Before I could say anything he hung up on me."
  ""
  if mc.money>ufc_bot_price:                            ##  you have enough money to buy the bot back
    "Damn, I thought I'd get away with it. Should I go to the {mark}'Fuck Em Up'{/} club and buy my bot back?"
    if mc.rep_mc_trainer.level>=2:
      $temp=calc_pr_rep_gain("rep_mc_trainer","s_l")    ## small LOSS - 0.12.n REVISION
      $mc.give_xp("rep_mc_trainer",temp)
##      $mc.give_xp("rep_mc_trainer",randint(-25,-10))    ## OLD CODE
    if mc.rep_mc_fighter.level>=2:
      $temp=calc_pr_rep_gain("rep_mc_fighter","s_l")    ## small LOSS - 0.12.n REVISION
      $mc.give_xp("rep_mc_fighter",temp)
##      $mc.give_xp("rep_mc_fighter",randint(-25,-10))    ## OLD CODE
    choice("ufc_male_buy_back") "Buy Bot Back"
    choice("ufc_male_do_not_buy_back") "Give Up Bot"
  else:
    "Damn, I thought I'd get away with it and I don't have enough money to buy the bot back. Shit."
    if mc.rep_mc_trainer.level>=2:
      $temp=calc_pr_rep_gain("rep_mc_trainer","s_l")    ## small LOSS - 0.12.n REVISION
      $mc.give_xp("rep_mc_trainer",temp)
##      $mc.give_xp("rep_mc_trainer",randint(-25,-10))    ## OLD CODE
    if mc.rep_mc_fighter.level>=2:
      $temp=calc_pr_rep_gain("rep_mc_fighter","s_l")    ## small LOSS - 0.12.n REVISION
      $mc.give_xp("rep_mc_fighter",temp)
##      $mc.give_xp("rep_mc_fighter",randint(-25,-10))    ## OLD CODE
    choice("ufc_male_do_not_buy_back") "Continue"
  return

label ufc_male_buy_back:                                       ##  3rd screen if cheating and buying back bot
  header "[ufc_bot.name] - {mark}[ufc_mission_title]{/} mission"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [ufc_bot.model_id] avatar@240x360}"
  $act.set_block("c")
  "When you arrive they send you to the bar upstairs to pay the owner for {mark}[ufc_bot.name]{/}."
  $ufc_imagenumber=random.randint(63,64)                    ## paying owner
  $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"
  "After lecturing you about cheating, the owner tells you to go downstairs to the locker room and pick up your bot."
  $ufc_imagenumber=random.randint(65,66)                    ## picking up bot
  $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"
  $mc.money-=ufc_bot_price
  $bot=None
  choice("<<<") "Continue"
  return
  
label ufc_male_do_not_buy_back:                                ##  3rd screen if cheating and NOT buying back bot
  header "[ufc_bot.name] - {mark}[ufc_mission_title]{/} mission"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [ufc_bot.model_id] avatar@240x360}"
  $act.set_block("c")

  "You find yourself holding a silent phone. Shit, I hate losing bots."
  $ufc_imagenumber=random.randint(1,2)                    ## talking on phone
  $action_image="missions ufc UFC_B_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"
  "You set the phone down and think about what happened. Maybe I shouldn't cheat again." 
  $ufc_imagenumber=random.randint(3,4)                    ## after hanging up with owner
  $action_image="missions ufc UFC_B_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"
  $move_sexbot(ufc_bot,None)     ##  remove bot
  $bot=None
  choice("<<<") "Continue"
  return

label ufc_male_win_or_lose:                                    ##  2nd screen if not caught cheating, no room for avatar on this screen
  header "[ufc_bot.name] - {mark}[ufc_mission_title]{/} mission"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if ufc_won_fight==1:                                                       ## your bot won
    $ufc_bot.ufc_wins+=1                                                     ## add win
    $ufc_bot.ufc_record=str(ufc_bot.ufc_wins)+" - "+str(ufc_bot.ufc_losses)  ## update bot record characteristic for status screen
    if ufc_opponent==1:                                                      ## fighting opponent 1
      $ufc_imagenumber=random.randint(17,20)                                 ## pinning opponent
      $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
      $ufc_imagenumber=random.randint(27,28)                  ## referee raises arm
      $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
      center "{image=[action_image]@400x600}"
    else:                                                     ## fighting opponent 2
      $ufc_imagenumber=random.randint(47,50)                  ## pinning opponent
      $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
      $ufc_imagenumber=random.randint(57,58)                  ## referee raises arm
      $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
      center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    "Yes! {mark}[ufc_bot.name]{/} wins the fight! His record is now [ufc_bot.ufc_record]. {good}Hell yes! Prize money coming my way!{/}"
##    ""
##    "Hell yes! Prize money coming my way!"
    ""
    $ufc_bot.chassis.apply_damage("training_combat",(5,25))  ##  lighter damage from a winning fight
    ""
    $ufc_stability_loss=random.randint(ufc_stb_won_min,ufc_stb_won_max)
    if ufc_bot.psychocore.stability>ufc_stability_loss:
      $ufc_bot.psychocore.stability-=ufc_stability_loss
    else:
      $ufc_bot.psychocore.stability=0

## 0.12.n WON FIGHT - changed rep gains
    if ufc_fight_level==3:                             ## D level fight
      $temp=calc_pr_rep_gain("rep_mc_trainer","xs_g")  ## extra small gain
      $mc.give_xp("rep_mc_trainer",temp)
      $temp=calc_pr_rep_gain("rep_mc_fighter","xs_g")  ## extra small gain
      $mc.give_xp("rep_mc_fighter",temp)
    elif ufc_fight_level==4:                           ## C level fight
      $temp=calc_pr_rep_gain("rep_mc_trainer","s_g")   ## small gain
      $mc.give_xp("rep_mc_trainer",temp)
      $temp=calc_pr_rep_gain("rep_mc_fighter","s_g")   ## small gain
      $mc.give_xp("rep_mc_fighter",temp)
    elif ufc_fight_level==5:                           ## B level fight
      $temp=calc_pr_rep_gain("rep_mc_trainer","m_g")   ## medium gain
      $mc.give_xp("rep_mc_trainer",temp)
      $temp=calc_pr_rep_gain("rep_mc_fighter","m_g")   ## medium gain
      $mc.give_xp("rep_mc_fighter",temp)
    elif ufc_fight_level==6:                           ## A level fight
      $temp=calc_pr_rep_gain("rep_mc_trainer","l_g")   ## large gain
      $mc.give_xp("rep_mc_trainer",temp)
      $temp=calc_pr_rep_gain("rep_mc_fighter","l_g")   ## large gain
      $mc.give_xp("rep_mc_fighter",temp)
    elif ufc_fight_level==7:                           ## Open fight
      $temp=calc_pr_rep_gain("rep_mc_trainer","xl_g")  ## extra large gain
      $mc.give_xp("rep_mc_trainer",temp)
      $temp=calc_pr_rep_gain("rep_mc_fighter","xl_g")  ## extra large gain
      $mc.give_xp("rep_mc_fighter",temp)
## old code
##    $mc.give_xp("rep_mc_trainer",randint(20,60))       ##  bot trainer reputation - 1st REVISION
##    $mc.give_xp("rep_mc_fighter",randint(50,125))      ##  sexbot fighter reputation - 1st REVISION

    ""
    if ufc_fight_level==3:      ## D level fight
      $mc.money+=ufc_d_prize_money
    elif ufc_fight_level==4:    ## C level fight
      $mc.money+=ufc_c_prize_money
    elif ufc_fight_level==5:    ## B level fight
      $mc.money+=ufc_b_prize_money
    elif ufc_fight_level==6:    ## A level fight
      $mc.money+=ufc_a_prize_money
    elif ufc_fight_level==7:    ## Open fight
      $mc.money+=ufc_o_prize_money
  else:                                                                      ## your bot lost
    $ufc_bot.ufc_losses+=1                                                   ## add loss
    $ufc_bot.ufc_record=str(ufc_bot.ufc_wins)+" - "+str(ufc_bot.ufc_losses)  ## update bot record characteristic for status screen
    if ufc_opponent==1:                                                      ## fighting opponent 1
      $ufc_imagenumber=random.randint(21,24)                                 ## being pinned
      $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
      $ufc_imagenumber=random.randint(29,30)                  ## referee raises opponent's arm
      $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
      center "{image=[action_image]@400x600}"
    else:                                                     ## fighting opponent 2
      $ufc_imagenumber=random.randint(51,54)                  ## being pinned
      $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
      $ufc_imagenumber=random.randint(59,60)                  ## referee raises opponent's arm
      $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
      center "{image=[action_image]@400x600}"
    ##  TEXT
    $act.set_block("c")
    "Damn, {mark}[ufc_bot.name]{/} lost the fight. His record is now [ufc_bot.ufc_record]. {bad}Shit, I could have used the money.{/}"
    ""
##    "Shit, I could have used the money."
##    ""
    if ufc_bot.bot_combat.level<7:  ## 0.9.n bot is not S level in combat, make conditional text
      "I guess {mark}[ufc_bot.name]{/} could use more {mark}combat{/} training and I better make sure [ufc_bot.hisher] {mark}integrity{/} and {mark}stability{/} are both high."
    else:
      "{mark}[ufc_bot.name]{/} is highly skilled in combat so there's no training that will help but I must make sure [ufc_bot.hisher] {mark}integrity{/} and {mark}stability{/} are both high."
    ""
    $ufc_bot.chassis.apply_damage("training_combat",(10,50))  ## heavy damage from a losing fight
    ""
    $ufc_stability_loss=random.randint(ufc_stb_lost_min,ufc_stb_lost_max)
    if ufc_bot.psychocore.stability>ufc_stability_loss:
      $ufc_bot.psychocore.stability-=ufc_stability_loss
    else:
      $ufc_bot.psychocore.stability=0

## 0.12.n LOST FIGHT - changed rep gains
    if ufc_fight_level==3:                               ## D level fight
      if mc.rep_mc_trainer.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_trainer","xs_l")  ## extra small loss
        $mc.give_xp("rep_mc_trainer",temp//4)            ## loss 4-fold less effect           
      if mc.rep_mc_fighter.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_fighter","xs_l")  ## extra small loss
        $mc.give_xp("rep_mc_fighter",temp//4)
    elif ufc_fight_level==4:                             ## C level fight
      if mc.rep_mc_trainer.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_trainer","s_l")   ## small loss
        $mc.give_xp("rep_mc_trainer",temp//4)
      if mc.rep_mc_fighter.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_fighter","s_l")   ## small loss
        $mc.give_xp("rep_mc_fighter",temp//4)
    elif ufc_fight_level==5:                             ## B level fight
      if mc.rep_mc_trainer.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_trainer","m_l")   ## medium loss
        $mc.give_xp("rep_mc_trainer",temp//4)
      if mc.rep_mc_fighter.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_fighter","m_l")   ## medium loss
        $mc.give_xp("rep_mc_fighter",temp//4)
    elif ufc_fight_level==6:                             ## A level fight
      if mc.rep_mc_trainer.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_trainer","l_l")   ## large loss
        $mc.give_xp("rep_mc_trainer",temp//4)
      if mc.rep_mc_fighter.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_fighter","l_l")   ## large loss
        $mc.give_xp("rep_mc_fighter",temp//4)
    elif ufc_fight_level==7:                             ## Open fight
      if mc.rep_mc_trainer.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_trainer","xl_l")  ## extra large loss
        $mc.give_xp("rep_mc_trainer",temp//4)
      if mc.rep_mc_fighter.level>=2:                     ## must have rep to lose
        $temp=calc_pr_rep_gain("rep_mc_fighter","xl_l")  ## extra large loss
        $mc.give_xp("rep_mc_fighter",temp//4)
## old code
##    if mc.rep_mc_trainer.level>=2:
##      $mc.give_xp("rep_mc_trainer",randint(-25,-10))            ## bot trainer reputation - 1st REVISION
##    if mc.rep_mc_fighter.level>=2:
##      $mc.give_xp("rep_mc_fighter",randint(-25,-10))           ## sexbot fighter reputation - 1st REVISION

## 0.9.n if bot is marked DNS bypass the possibilities of selling the bot
  if ufc_won_fight==1 and ufc_bot.do_not_sell:
    ""
    "When I signed {mark}[ufc_bot.name]{/} up for this fight I told them I wouldn't sell [ufc_bot.himher] so I won't get an offer I don't want. {size=-8}{info}(bot marked DNS){/}{/}"
    choice("<<<") "Continue"
## LINE BELOW: bot won - enough wins - not too many losses
  elif ufc_won_fight==1 and ufc_bot.ufc_wins>=ufc_low_offer and ufc_bot.ufc_losses<=ufc_loss_limit:  ## 0.9.n was if, now elif
    choice("ufc_male_buy_offer") "Continue"
## LINE BELOW: bot qualified for offer but exceeds loss limit - AND you haven't called owner yet
  elif ufc_won_fight==1 and ufc_bot.ufc_wins>=ufc_low_offer and ufc_called_owner==0:
    $ufc_called_owner=1                              ##  set flag so you don't call owner more than once
    choice("ufc_male_call_owner") "Continue"
  else:                                              ## your bot lost
    choice("<<<") "Continue"
  return

##===========SELLING A WINNING BOT FUNCTIONS)=============

label ufc_male_buy_offer:
  header "[ufc_bot.name] - {mark}[ufc_mission_title]{/} mission"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [ufc_bot.model_id] avatar@240x360}"
  if ufc_bot.rate_level==3:              ## D bot
    $ufc_buy_offer=ufc_d_bot_offer
  elif ufc_bot.rate_level==4:            ## C bot
    $ufc_buy_offer=ufc_c_bot_offer
  elif ufc_bot.rate_level==5:            ## B bot
    $ufc_buy_offer=ufc_b_bot_offer
  elif ufc_bot.rate_level==6:            ## A bot
    $ufc_buy_offer=ufc_a_bot_offer
  elif ufc_bot.rate_level==7:            ## S bot
    $ufc_buy_offer=ufc_s_bot_offer
  if ufc_bot.ufc_wins>=ufc_high_offer:   ## bot has enough wins for high offer
    $ufc_buy_offer=ufc_buy_offer*ufc_bonus_offer

## multiply offer by winning percentage and truncate to nearest 100
  $ufc_buy_offer=ufc_buy_offer*ufc_bot.ufc_wins/(ufc_bot.ufc_wins+ufc_bot.ufc_losses)
  $ufc_buy_offer=100*int(ufc_buy_offer/100)
  
## 0.12.n add a variable amount to the price based upon the MC's reputation  
  $ufc_buy_offer=ufc_buy_offer+price_rep_ufc_fight() 

  $act.set_block("c")
  "You receive a call from the owner of the {mark}'Fuck Em Up'{/} club."
  ""
  $ufc_imagenumber=random.randint(61,62) ## owner calls
  $action_image="missions ufc UFC_M_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  if ufc_bot.ufc_wins<ufc_high_offer:           ## INITIAL OFFER
    if ufc_bot.ufc_losses==0:                   ## bot is undefeated
      "He says that he's noticed my bot hasn't lost a fight at his club yet and offers to buy [ufc_bot.himher] for {mark}$[ufc_buy_offer]{/}."
    elif ufc_bot.ufc_losses<ufc_bot.ufc_wins:   ## bot has winning record
      "He says my bot has a few wins at his club and has a good record. He offers to buy [ufc_bot.himher] for {mark}$[ufc_buy_offer]{/}."
    else:                                       ##  bot has even or less record
      "He says my bot has a few wins at his club but doesn't have a great record. He offers to buy [ufc_bot.himher] for {mark}$[ufc_buy_offer]{/}."
    ""
    "That a nice offer, should I sell {mark}[ufc_bot.name]{/}? If [ufc_bot.heshe] keeps winning will it get better?"
  elif ufc_bot.ufc_wins<ufc_final_offer: ##  DOUBLED OFFER
    if ufc_bot.ufc_losses==0:                   ## bot is undefeated
      "He's excited and says my bot is great and hasn't lost a fight at his club yet! He offers to buy [ufc_bot.himher] for {mark}$[ufc_buy_offer]{/}."
    elif ufc_bot.ufc_losses<ufc_bot.ufc_wins:   ## bot has winning record
      "He's excited and says my bot has a lot of wins at his club and has a good record. He offers to buy [ufc_bot.himher] for {mark}$[ufc_buy_offer]{/}."
    else:                                       ##  bot has even or less record
      "He's excited and says my bot has a lot of wins at his club but doesn't have a great record. He offers to buy [ufc_bot.himher] for {mark}$[ufc_buy_offer]{/}."
    ""
    "That's a {mark}really good{/} offer, should I sell {mark}[ufc_bot.name]{/}? If [ufc_bot.heshe] keeps winning will it get better?"
  else:                                  ##  HINT: TOP OFFER
    if ufc_bot.ufc_losses==0:                   ## bot is undefeated
      "He says my bot is fantastic and still hasn't lost a fight at his club but his absolutely top offer to buy [ufc_bot.himher] is {mark}$[ufc_buy_offer]{/}."
      ""
      "Is that really his top offer? Should I sell {mark}[ufc_bot.name]{/}? If [ufc_bot.heshe] loses a fight the offer will probably go down."
    elif ufc_bot.ufc_losses<ufc_bot.ufc_wins:   ## bot has winning record
      "He's excited and says my bot has a lot of wins at his club and has a good record. He offers to buy [ufc_bot.himher] for {mark}$[ufc_buy_offer]{/}."
      ""
      "That's a {mark}really good{/} offer, should I sell {mark}[ufc_bot.name]{/}? If [ufc_bot.heshe] keeps winning will it get better?"
    else:                                       ##  bot has even or less record
      "He's excited and says my bot has a lot of wins at his club but doesn't have a great record. He offers to buy [ufc_bot.himher] for {mark}$[ufc_buy_offer]{/}."
      ""
      "That's a {mark}really good{/} offer, should I sell {mark}[ufc_bot.name]{/}? If [ufc_bot.heshe] keeps winning will it get better?"
  choice("ufc_male_sell_bot") "Sell Bot"
  choice("ufc_male_keep_bot") "Keep Bot"
  return

label ufc_male_sell_bot:
  header "[ufc_bot.name] - {mark}[ufc_mission_title]{/} mission"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [ufc_bot.model_id] avatar@240x360}"
  $act.set_block("c")
  "You decide it's a good offer and tell the club owner you'll sell {mark}[ufc_bot.name]{/}."
  $ufc_imagenumber=random.randint(1,2)                    ## talking on phone
  $action_image="missions ufc UFC_B_"+str(ufc_imagenumber)
  center "{image=[action_image]@340x510}"
  ""
  "Good money! You can't wait to build and train another bot!"
  $ufc_imagenumber=random.randint(3,4)                    ## after hanging up with owner
  $action_image="missions ufc UFC_B_"+str(ufc_imagenumber)
  center "{image=[action_image]@340x510}"
  ""
  $mc.money+=ufc_buy_offer
## 0.12.n add  reputations
  if ufc_bot.rate=="D":                              ## dealer rep based upon bot's rate
    $temp=calc_pr_rep_gain("rep_mc_dealer","xs_g")   ## extra small gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif ufc_bot.rate=="C":
    $temp=calc_pr_rep_gain("rep_mc_dealer","s_g")    ## small gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif ufc_bot.rate=="B":
    $temp=calc_pr_rep_gain("rep_mc_dealer","m_g")    ## medium gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif ufc_bot.rate=="A":
    $temp=calc_pr_rep_gain("rep_mc_dealer","l_g")    ## large gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif ufc_bot.rate=="S":
    $temp=calc_pr_rep_gain("rep_mc_dealer","xl_g")   ## extra large gain
    $mc.give_xp("rep_mc_dealer",temp)
  if ufc_bot.bot_combat=="D":                            ## combat bot trainer rep based upon bot's combat skill
    $temp=calc_pr_rep_gain("rep_mc_fighter","xs_g")  ## extra small gain
    $mc.give_xp("rep_mc_fighter",temp)
  elif ufc_bot.bot_combat=="C":   
    $temp=calc_pr_rep_gain("rep_mc_fighter","s_g")   ## small gain
    $mc.give_xp("rep_mc_fighter",temp)
  elif ufc_bot.bot_combat=="B": 
    $temp=calc_pr_rep_gain("rep_mc_fighter","m_g")   ## medium gain
    $mc.give_xp("rep_mc_fighter",temp)
  elif ufc_bot.bot_combat=="A": 
    $temp=calc_pr_rep_gain("rep_mc_fighter","l_g")   ## large gain
    $mc.give_xp("rep_mc_fighter",temp)
  elif ufc_bot.bot_combat=="S":
    $temp=calc_pr_rep_gain("rep_mc_fighter","xl_g")  ## extra large gain
    $mc.give_xp("rep_mc_fighter",temp)
  $move_sexbot(ufc_bot,None)     ##  remove bot
  $bot=None
  choice("<<<") "Continue"
  return

label ufc_male_keep_bot:
  header "[ufc_bot.name] - {mark}[ufc_mission_title]{/} mission"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [ufc_bot.model_id] avatar@240x360}"
  $act.set_block("c")
  "You tell the club owner you're not willing to sell {mark}[ufc_bot.name]{/} at that price."
  $ufc_imagenumber=random.randint(1,2)                    ## talking on phone
  $action_image="missions ufc UFC_B_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  "You hope the owner will increase his offer if your bot keeps winning."
  $ufc_imagenumber=random.randint(3,4)                    ## after hanging up with owner
  $action_image="missions ufc UFC_B_"+str(ufc_imagenumber)
  center "{image=[action_image]@400x600}"
  $bot=None
  choice("<<<") "Continue"
  return

label ufc_male_call_owner:
  header "[ufc_bot.name] - {mark}[ufc_mission_title]{/} mission"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [ufc_bot.model_id] avatar@240x360}"
  $act.set_block("c")
  "You decide to call the {mark}'FuckEmUp'{/} club owner because {mark}[ufc_bot.name]{/} won yet he didn't call with an offer to buy [ufc_bot.himher]."
  $ufc_imagenumber=random.randint(1,2)                    ## talking on phone
  $action_image="missions ufc UFC_B_"+str(ufc_imagenumber)
  center "{image=[action_image]@320x480}"    ## reduce size to fit
  ""
  "He said {mark}he never buys bots with more than 5 losses{/} and hung up. Damn, I'll write this in my journal notes so I remember."
  $ufc_imagenumber=random.randint(3,4)                    ## thinking at desk
  $action_image="missions ufc UFC_B_"+str(ufc_imagenumber)
  center "{image=[action_image]@320x480}"    ## reduce size to fit
  if not quests.ufc_too_many_losses.started:       ## 0.10.n to avoid starting more than once and reset to phase 1 for saved games
    $quests.start_quest("ufc_too_many_losses")     ## start quest which displays info in Journal Notes
  elif quests.ufc_too_many_losses!="showsetting":  ## phase is beyond 1 because of bug before 0.10.n
    $quests.mobprotection.advance(1)               ## reset to phase 1 - "showsetting"
  $bot=None
  choice("<<<") "Continue"
  return

##===========CALCULATION FUNCTIONS (NO DISPLAY)===========

label ufc_male_determine_outcome:    ##  determine if cheating, if not determine win or lose
  call ufc_male_evaluate_bot
  $temp_1=randint(1,100)
  if temp_1<ufc_bot_eval:            ##  random number less than bot evaluation, caught cheating
    call ufc_male_caught_cheating
  else:                              ##  not caught cheating, evaluate win/loss
    python:
##      print "UFC Fight:"
      temp_1=50                                                                          ##  base is 50% chance of winning
##      print "Base:",temp_1
      temp_1=temp_1+ufc_combat_weight*(ufc_bot.bot_combat.level-ufc_fight_level)         ##  combat skill adjustment
##      print "+ Combat Skill:",temp_1
      temp_1=temp_1+ufc_bot_eval*ufc_win_loss_weight                                     ##  bot eval adjustment
##      print "+ Weighted Bot Evaluation:",temp_1
      temp_2=ufc_bot.ufc_wins*ufc_win_weight-ufc_bot.ufc_losses*ufc_loss_weight          ##  win/loss record adjustment
      if temp_2>10*ufc_win_weight:                                                       ##  record equivalent to 10-0 is max
        temp_2=10*ufc_win_weight
      elif temp_2<-10*ufc_loss_weight:                                                   ##  record equivalent to 0-10 is min
        temp_2=-10*ufc_loss_weight
      temp_1=temp_1+temp_2                                                               ##  apply limited record adjustment
##      print "+ Weighted Bot Fight Record:",temp_1
      temp_1=temp_1+(ufc_bot.chassis.integrity-ufc_integrity_zero)*ufc_integrity_weight  ##  integrity adjustment
##      print "+ Weighted Integrity:",temp_1
      if ufc_bot.psychocore.stability<25:                                                ##  unstable value -70
        temp_1=temp_1-70
      elif ufc_bot.psychocore.stability<50:                                              ##  glitchy value -30
        temp_1=temp_1-30
      elif ufc_bot.psychocore.stability<75:                                              ##  quirky value -10 - stable falls through value 0
        temp_1=temp_1-10
##      print "+ Weighted Stability:",temp_1
      if temp_1>98:
        temp_1=98
      elif temp_1<2:
        temp_1=2
##      print "+ min/max:", temp_1
      temp_2=randint(1,100)
      if temp_2<=temp_1:
        ufc_won_fight=1
      else:
        ufc_won_fight=0
##    $ufc_won_fight=0  ## force loss for testing, comment out otherwise
##    $ufc_won_fight=1  ## force win for testing, comment out otherwise
    call ufc_male_win_or_lose
  return

label ufc_male_evaluate_bot:   ## unweighted value for cheating - weighted value for  win/lose
  python:
    ufc_rate_eval=ufc_bot.rate_level-ufc_fight_level              ##  bot rate - fight level
##    print "Bot Rate Difference:",ufc_rate_eval
    ufc_parts_eval=0                                              ##  initialize part level
    for slot in ufc_bot.outfit_slots:                             ##  applies to all bot parts
      ufc_bot_part=ufc_bot.item_on_slot(slot)
      if ufc_bot_part:                                            ##  should not be a problem, parts should exist!!
        ufc_part_level=ufc_bot_part.rate_level-ufc_fight_level    ##  part rate - fight level
      else:
        ufc_part_level=0
      ufc_parts_eval=ufc_parts_eval+ufc_part_level                              ##  add current part to total
##    print "Bot Parts Difference:",ufc_parts_eval
    ufc_bot_eval=ufc_rate_eval*ufc_rate_weight+ufc_parts_eval*ufc_parts_weight  ##  calculate weighted value using both bot and parts
##    print "Fully Weighted Bot Evaluation:",ufc_bot_eval
  return