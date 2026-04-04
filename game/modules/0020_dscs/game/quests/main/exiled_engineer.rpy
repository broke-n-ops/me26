init python:
  sr_custom_amount=0        ##  custom payment amount
  sr_debt_after_payment=0   ##  working value; debt after proposed custom payment
  sr_money_after_payment=0  ##  working value; MC money after proposed custom payment

##===============================================
##  ABOVE IS NEW VARIABLES, BELOW IS QUEST PHASES
##===============================================

  class Quest_exiled_engineer(Quest):
    payment_day="Monday"
    name="Framed!(SL)"
    class phase_1_debt1:
      description="""
        You receive a message from the boss with the status of your debt:

        Debt: [money_str[mc.debt]]
        Interest: [money_str[mc.debt_pending]]
        Payment day: {mark}[quest.payment_day]{/}


        """

    class phase_2_debt2:
      description="""
        You receive a message from the boss with the status of your debt:

        Debt: [money_str[mc.debt]]
        Interest: [money_str[mc.debt_pending]]
        Payment day: {mark}[quest.payment_day]{/}

        You will NOT receive another pass, make your payments


        """

    class phase_1000_done:
      description="The boss sent a message: Congratulations, you paid the debt. Don't do it again!"

    class phase_2000_failed:
      description="You failed your debt payments!"

##===================================================
##  EVENT HANDLER FOR EXILED_ENGINEER (FRAMED!) QUEST
##===================================================

init python hide:
  @event_handler("time_advanced")
  def debt_payment_event():
    if quests.exiled_engineer=="debt1" or quests.exiled_engineer=="debt2":
      if now("monday","morning"):
##      if now("morning"):                    ## for testing pay every day, need money cheat!!
        queue_event("quest_exiled_engineer_debt_event")

##==================================
##  FUNCTION CALLED BY EVENT HANDLER
##==================================

label quest_exiled_engineer_debt_event:
  $game_bg="home computer"
  header "Debt Payment Day"
  $hw_imagenumber=random.randint(1,2)
  if hw_imagenumber==1:                ##  ALTERNATIVE ARRIVAL 1
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $hw_imagenumber=random.randint(1,3)
    $action_image="squirrel botshop fr_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(4,6)
    $action_image="squirrel botshop fr_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(7,9)
    $action_image="squirrel botshop fr_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    "It's monday morning and the debt collectors show up bright and early. I'm sure glad the thug volunteered to come along, the young guy scares me."
    ""
    "The young guy starts walking faster and looks threatening, thank goodness the thug grabs him and pulls him back."
    ""
    "The young guy stands in back looking pissed while the thug does the talking:"
    ""
    "{say}You know why we're here kid, you better have money for us.{/}"
    ""
    "{mcsay}The money is in the other room, I'll be right back.{/}"
    ""
  else:                                ##  ALTERNATIVE ARRIVAL 2
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $hw_imagenumber=random.randint(1,3)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel botshop fr_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(10,12)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel botshop fr_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(13,15)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel botshop fr_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    "It's monday morning and the debt collectors show up bright and early. I'm sure glad the thug volunteered to come along, the young guy scares me."
    ""
    "The young guy gets in my face waving his fists and yelling:"
    ""
    "{say}HEY ASSHOLE, YOU BETTER HAVE A LOT OF MONEY FOR US! MAYBE I'LL KICK YOUR ASS ANYWAY! COME ON, WE AIN'T GOT ALL DAY!"
    ""
    "Just when I thought he was going to hit me the thug pulled him back and said:"
    ""
    "{say}Shut up asshole! Kid go get the money while I calm this guy down.{/}"
    ""
    "That guy is scary! {mcsay}OK, I'll be right back.{/}"
    ""
  choice("quest_exiled_engineer_debt_event2") "Continue"
  return
  
label quest_exiled_engineer_debt_event2:                      ## 0.12.6 add a new screen which tells stupid players why they should build their business up before paying their debt
  $game_bg="home computer"
  header "Debt Payment Day"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $hw_imagenumber=random.randint(32,33)                         ## need image(s) for thinking in bedroom getting money, 2 poses, 2 cameras for at least some variety
  $action_image="squirrel botshop fr_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(34,35)
  $action_image="squirrel botshop fr_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"  
  ""
  ##  TEXT
  $act.set_block("c")
  "I have to be careful. I need to {mark}keep enough money for emergencies{/} and I should also {mark}reinvest in my business{/}."
  "If I always do everything by myself the business will never grow. If I had {mark}more capsules{/} I'm sure I could {mark}train bots to help me run the shop{/}."
  "It also would be great to have an {mark}inventory of parts{/} so I can restore bots faster."
  ""
  "They are only demanding that I pay the interest each week but if I do that I'll be paying them forever. If I give them too much of my money I can't reinvest in my business and I'll live like this forever. This is complicated, what should I do?" 
  ""
  $sr_custom_amount=mc.debt_pending    ##  set initial custom amount ASAP; must be before calling 'sr_select_payment_type'
  if mc.money>=mc.debt_pending:                   ##  you have enough money to pay the interest
    choice ("sr_minimum_payment",pos=0) "Pay Minimum"
  if mc.money>=mc.debt_pending+101:              ##  you have enough money to make at least the minimal addition of $100
    choice ("sr_custom_payment", pos=1) "Custom Amount"
  if mc.money>=mc.debt+mc.debt_pending:           ##  you have enough money to pay off the debt including the current interest
    choice ("sr_full_payment",pos=2) "Pay Full Debt"
  if quests.exiled_engineer=="debt1":             ##  you don't have enough money or decided not to pay for some reason - FIRST TIME
    choice ("sr_do_not_pay",pos=3) "Refuse to pay"
  elif quests.exiled_engineer=="debt2":           ##  you don't have enough money or decided not to pay for some reason - SECOND TIME - GAME OVER
    choice ("sr_no_second_pass",pos=3) "Refuse to pay"
  return

##===========================================
##  PAYMENT FUNCTIONS - MINIMUM, FULL, CUSTOM
##===========================================

label sr_minimum_payment:
  $quests.exiled_engineer["paid_today"]=True    ##  this resets the payment day
  $game_bg="home computer"
  header "Debt Payment Day"
  call sr_show_payment_pics    ##  SAME PICS FOR ALL PAYMENT TYPES
  ##  TEXT
  $act.set_block("c")
  ""
  "I tell them I'll get their money and I come back with the minimum payment. The young guy starts coming to meet me to get the money but the thug holds him back."
  ""
  "It's pretty bad when a guy like that is being my friend, good thing the young guy doesn't challenge him. The thug takes the money and says:"
  ""
  "{say}Kid, this is just the minimum payment. That's OK but you'll be paying forever if this is all you give us. You need to do better.{/}"
  ""
  "They both glare at me for a minute and then they turn around and leave the shop. The young guy turns back and says:"
  ""
  "{say}You better have more money for us next time asshole!{/}"
  ""
  ##  interest only payment, no reduction in principle
  $mc.money-=mc.debt_pending
## reputation with The Syndicate does not increase for paying interest only
## 0.10.n replacement variable, see intro - 1 new line
  $mc.debt_pending=int(mc.debt*fr_interest_rate[game.difficulty])
  choice("<<<") "Continue"
  return

label sr_full_payment:
  $quests.exiled_engineer["paid_today"]=True    ##  this resets the payment day
  $game_bg="home computer"
  header "Debt Payment Day"
  call sr_show_payment_pics                 ##  SAME PICS FOR ALL PAYMENT TYPES
  $action_image="squirrel botshop fr_31"    ##  ADD CELEBRATION PICTURE FOR FULL PAYMENT
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "I tell them I'll get their money and I come back with the full payment including interest. As usual, the thug makes sure he gets the money. When he see's the stack of money he says:"
  ""
  "{say}Wow kid, is this the whole thing?{/}"
  ""
  "I nod while he counts the money. When he's done counting he says:"
  ""
  "{say}Great kid! We're done here. Good luck with your shop.{/}"
  ""
  "They turn around and start to leave but the young guy has to say something on their way out:"
  ""
  "{say}You're lucky you decided to pay us, I sort of wish you hadn't so I could take you down!{/}"
  ""
  "Once they're gone you celebrate with a fist pump, I sure hope I never see those two again!"
  ""
  ##  full payment includes debt plus interest
  $mc.debt+=mc.debt_pending
  $mc.money-=mc.debt
  $mc.debt=0
  $mc.debt_pending=0
## reputation should reach neutral, actual formula is complicated so I just set it directly
##  $print "BEFORE - Rep level: ",mc.rep_syndicate.level,"Rep xp:",mc.rep_syndicate.xp
  $mc.rep_syndicate.level=0
  $mc.rep_syndicate.xp=0
  $mc.give_xp("rep_syndicate",1)     ## to cause notification
##  $print "AFTER - Rep level: ",mc.rep_syndicate.level,"Rep xp:",mc.rep_syndicate.xp
  $quests.exiled_engineer.finish()
## 0.11.n added call to update mc's business skill
  call mc_update_business
  $quests.start_quest("freelancer")
  choice("<<<") "Continue"
  return

label sr_custom_payment:
  $game_bg="home computer"
  header "Set Custom Payment Amount"
  $sr_debt_after_payment=mc.debt+mc.debt_pending-sr_custom_amount
  $sr_money_after_payment=mc.money-sr_custom_amount
  ""
  ""
  "Custom Payment Amount:    {mark}$[sr_custom_amount]{/}"
  ""
  "Minimum payment (weekly interest):    $[mc.debt_pending]"
  ""
  ""
  "Increasing your payment will reduce the debt:"
  "Current Debt:    $[mc.debt]"
  "Debt After Payment:    $[sr_debt_after_payment]"
  ""
  ""
  if sr_money_after_payment >=50000:   ##  you have plenty of money remaining
    "Money Remaining After Payment:    {mark}$[sr_money_after_payment]{/}"
    ""
    "{mark}You could increase the payment to lower the debt without much risk.{/}"
  elif sr_money_after_payment >=25000:  ##  remaining money not a problem
    "Money Remaining After Payment:    {say}$[sr_money_after_payment]{/}"
    ""
    "{say}You can probably increase the payment but it's getting a little risky!{/}"
  else:
    "Money Remaining After Payment:    {bad}$[sr_money_after_payment]{/}"
    ""
    "{bad}Are you sure you want to make this payment? Not much money left over!{/}"
  ""
  if mc.money>sr_custom_amount+100 and sr_debt_after_payment>100:
    choice("sr_add_100",pos=0) "Add $100"
  if mc.money>sr_custom_amount+1000 and sr_debt_after_payment>1000:
    choice("sr_add_1k",pos=1) "Add $1,000"
  if mc.money>sr_custom_amount+10000 and sr_debt_after_payment>10000:
    choice("sr_add_10k",pos=2) "Add $10,000"
  if mc.money>sr_custom_amount+100000 and sr_debt_after_payment>100000:
    choice("sr_add_100k",pos=3) "Add $100,000"
  choice("sr_start_over",pos=4) "Reset to Minimum"
  choice("sr_make_custom_payment",pos=5) "Make Payment"
  choice("quest_exiled_engineer_debt_event",pos=17) "Back"
  return

label sr_add_100:
  $sr_custom_amount+=100
  return "sr_custom_payment"

label sr_add_1k:
  $sr_custom_amount+=1000
  return "sr_custom_payment"

label sr_add_10k:
  $sr_custom_amount+=10000
  return "sr_custom_payment"

label sr_add_100k:
  $sr_custom_amount+=100000
  return "sr_custom_payment"

label sr_start_over:
  $sr_custom_amount=mc.debt_pending
  return "sr_custom_payment"

label sr_make_custom_payment:
  $quests.exiled_engineer["paid_today"]=True    ##  this resets the Payment day
  $game_bg="home computer"
  header "Debt Payment Day"
  call sr_show_payment_pics    ##  SAME PICS FOR ALL PAYMENT TYPES
  ##  TEXT
  $act.set_block("c")
  ""
  "I tell them I'll get their money and I come back with a payment I can afford. The young guy tries to get the money but the thug holds him back."
  ""
  "I'm glad the thug doesn't trust the guy, I'm sure he'd steal most of my payment if he could. The thug takes the money and says:"
  ""
  "{say}Great kid, keep putting a little extra in the payments like this and eventually you'll be all paid up.{/}"
  ""
  "They turn around and start to leave but the young guy has to say something to me on their way out:"
  ""
  "{say}We'll be back next week asshole, you better have a lot of money for us.{/}"
  ""
  $mc.debt+=mc.debt_pending
  $mc.money-=sr_custom_amount
  $mc.debt-=sr_custom_amount
  $principle_payment=sr_custom_amount-mc.debt_pending  ## need to know how much principle is being paid this time
## 0.10.n replacement variable, see intro - 1 new line
  $mc.debt_pending=int(mc.debt*fr_interest_rate[game.difficulty])
## 0.9.n REPUTATION GAIN
## 0.10.n replacement variable, see intro - 1 new line
  $temp=((principle_payment+0.0)/(fr_initial_debt[game.difficulty]+0.0))*5998.65  ## amount of xp the principle payment corresponds to
  $mc_cumulative_rep_xp=mc_cumulative_rep_xp+temp
  $mc.give_xp("rep_syndicate",temp)  ## reputation gain with The Syndicate
  choice("<<<") "Continue"
  return
  
label sr_show_payment_pics:
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(16,18)    ##  SEMI-HARD CODE - SIMPLE
  $action_image="squirrel botshop fr_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(19,21)    ##  SEMI-HARD CODE - SIMPLE
  $action_image="squirrel botshop fr_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(22,24)    ##  SEMI-HARD CODE - SIMPLE
  $action_image="squirrel botshop fr_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  return

##======================================================
##  NON- PAYMENT FUNCTIONS - FIRST OK - SECOND GAME OVER
##======================================================

label sr_do_not_pay:
  $quests.exiled_engineer["paid_today"]=True    ##  this resets the payment day
  $game_bg="home computer"
  header "Debt Payment Day"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel botshop fr_25"      ##  CAN ONLY DO THIS ONCE SO NO PICTURE OPTIONS
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel botshop fr_26"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel botshop fr_27"
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "You tell the guys business has been bad and you don't have anything for them this time."
  ""
  "At first they are surprised but then the young guy get's mad and tries to punch me in the face but the thug grabs his arm and says:"
  ""
  "{say}The boss said he'd give the kid a pass ONCE, remember?"
  ""
  "Then he says to me:"
  ""
  "{say}You're living dangerously kid.{/} {bad}This is your ONE pass. Don't do this again.{/}"
  ""
  "They turn around and start arguing while they leave the shop. I better not do this again, I remember what the boss said and I don't think he was kidding."
  ""
  $quests.exiled_engineer.advance()    ##  advance quest to debt2 - used pass
  choice ("<<<") "Continue"
  return

label sr_no_second_pass:
  $game_bg="home computer"
  header "Debt Payment Day"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel botshop fr_28"      ##  CAN ONLY DO THIS ONCE SO NO PICTURE OPTIONS
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel botshop fr_29"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel botshop fr_30"
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "I tell the two guys that I don't have the money for them. The thug can't believe it and looks up at the ceiling in exasperation.  The young guy looks happy though."
  ""
  "The young guy looks at the thug and says:"
  ""
  "{say}Well, can I do it?"
  ""
  "I get real scared when the thug nods his head and says:"
  ""
  "{say}Go ahead.{/}"
  ""
  "The young guy pulls out a gun! Before I can do anything I feel a sharp pain in my chest..."
  ""
  choice("bad_ending_failed_to_pay_debt",hint="{bad}Bad Ending{/}") "Continue"
  return

label bad_ending_failed_to_pay_debt:
  $set_interaction("ending")
  $act["ending_type"]="bad"
  $game_bg="black"
  $exit_main_loop=True
  return
