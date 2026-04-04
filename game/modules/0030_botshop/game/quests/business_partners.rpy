## Business Partnership - MC and Simone the Night School teacher

##==========initialize new variables==========

init python:
  bp_dollars="$"               ## problem putting $ character in phase descriptions
  bp_who_called=0              ## 0 means MC called Simone, 1 means Simone called MC
  bp_first_call=1              ## 1 means it is the first call, 0 means it's not the first call
  bp_next_deal=0               ## day number for next deal, 1-accepting+2, others - delivering previous + random number 2-4
  bp_deal_active=0             ## set to 1 when there is an active deal, used to display buttons
  bp_date_available=0          ## set to 1 when dates with Simone are active
  bp_bonus_end=0               ## day when the bonus payment ends within the current deal, set do 0 when deal not active
  bp_penalty_start=0           ## day when penalty starts within the current deal, set do 0 when deal not active
  bp_game_over=0               ## day when the deal expires, you failed and this triggers a game over event, set do 0 when deal not active
  receive_sucky=0              ## flag: set to 1 when phase starts, set to 2 when bot received, set to 3 when committed to delivery, reset to 0 when delivered
  sucky_knowledge=0            ## how well the MC knows how sucky works, makes other interactions more effective - 0 to 10 - 1 fix charger, 2 fix body/head, 3 hack, 4 train, 5,6,7 make each one level 2, 8,9,10 make each one level 3
  sucky_low=0.25               ## multiplier when knowledge is low level
  sucky_med=0.7                ## multiplier when knowledge is mid level
  sucky_high=1.6               ## multiplier when knowledge is high level
  sucky_charger_integrity=0    ## sucky charger integrity - 0 to 100%
  sucky_head_integrity=0       ## sucky head integrity - 0 to 100%
  sucky_body_integrity=0       ## sucky body integrity - 0 to 100%
  sucky_stability=0            ## sucky stability - 0 to 100%
  sucky_sex_skill=0            ## sucky sex skill - <=999=F, 1000-2249=E,2250-4999=C, 5000-9999=C, 10000-22499=B, 22500-49999=A, 50000-99999=S
  sucky_last_interaction=0     ## for showing the interaction picture, 0=avatar, 1=fix charger, 2=fix head, 3=fix body, 4=stabilize, 5=sex training (multiple images)
  receive_frankie_bride=0      ## flag: set to 1 when you can call Simone to receive them (2 space for 2 bots), set to 2 when you can work on them, set to 3 when committed to delivery, reset to 0 when delivered
  bp_deliver_sucky=0           ## set flag to [now.day+1] when you call about delivering the bot, go to Simone's next day in the evening
  bp_deliver_frankie_bride=0   ## set flag to [now.day+1] when you call about delivering the pair, go to Raymond's the next day in the evening
  pair_female_bot=""           ## holder for female bot in pair
  pair_male_bot=""             ## holder for male bot in pair
  pair_two_payment=0           ## final payment for second pair including bonus or penalty
  bp_actual_payment=0          ## payment received for last deal including bonus or penalty for journal
  bp_night_conversation=0      ## flag to be used in next version for the conversation between MC and Ruthie about 3-way relationship with Simone, set to 1 when ready
  bp_force_store_owner_rent=0  ## flag used to force MC to pay for Ruthie's apartment - in 0.14 it just happens after delivering Tanjiro bot, will become a story in 0.15
  bp_suit_for_rays=0           ## flag used to determine which clothing the MC wears during normal visits to Raymond's Bot Boutique
  bp_first_sex_teacher=0       ## flag set to 1 after sex in event 5 so the description of 'flirting' changes

## flag variables created in 'friends with benefits' that are used here - already declared!!

##  fwb_mc_new_clothes=0        ## flag set when MC dresses up for dates with Ruthie, Simone advises when you accept 'Business Partners'
##  fwb_date_clothes=0          ## flag set after the first time you wear new clothes on a date with Ruthie, unique text first time
##  fwb_anal_ok=0               ## POSTPONED UNTIL 0.15 flag set when Ruthie will do anal, Simone helps Ruthie with sex training using her male bots
##  fwb_first_anal=0            ## POSTPONED UNTIL 0.15 flag set after first anal with Ruthie for alternate text



##==========QUEST DECLARATION==========
  
  class Quest_businesspartners(Quest):
    name="Business Partners(SL)"
    class phase_1_accept_deal:
      description="""
        I've entered into a business partnership with {mark}[ns_teacher_name]{/}:
        -       {mark}[ns_teacher_name]{/} finds rich customers
        -       I build and train the bots they want
        -       {mark}[ns_teacher_name]{/} provides non-standard bots when needed
        -       I provide standard bots and all parts
        -       The minimum sales price is {mark}$1,000,000{/}, wow!
        -       The sales price is split {mark}50:50 when she provides the bot{/}
        -       The sales price is split {mark}70:30 in my favor for standard bots{/}
        I wonder when she'll give me my first assignment?

        """

    class phase_2_bot_1:
      description="""
        I got my 1st assignment:
        -  {mark}AGTY-36 Bot{/}
        -  All {mark}A+{/} parts
        -  {mark}100% {/}Integrity and Stability
        -  {mark}S level{/} Combat, Sex, and Social skills 
        -  Price{mark} $1,000,000{/}
        -  My Share{mark} $700,000{/} (half in advance)
        -  Delivery bonus of{mark} $100,000{/} if less than {mark}1 week{/}
        -  Penalty of{mark} $100,000{/} after {mark}3 weeks{/}
        -  After {mark}5 weeks (day [bp_game_over]){/} your partnership with{mark} [ns_teacher_name]{/} will be {mark}cancelled{/}

        """

    class phase_3_wait_1:
      description="""
        I delivered my 1st assignment, my first {mark}$1,000,000{/} bot!
        Well, I only made [money_str[bp_actual_payment]] but that's still more than I've ever made for one bot.
        I wonder when {mark}[ns_teacher_name]{/} will call with another assignment?

        """

    class phase_4_bot_2:
      description="""
        I got my 2nd assignment:
        -  {mark}Tanjiro SX Bot{/}
        -  All {mark}S{/} parts
        -  {mark}100% {/}Integrity and Stability
        -  {mark}S level{/} Combat, Sex, and Social skills 
        -  Price{mark} $1,750,000{/}
        -  My Share{mark} $1,225,000{/} (half in advance)
        -  Delivery bonus of{mark} $200,000{/} if less than {mark}1 week{/}
        -  Penalty of{mark} $200,000{/} after {mark}3 weeks{/}
        -  After {mark}5 weeks (day [bp_game_over]){/} your partnership with{mark} [ns_teacher_name]{/} will be {mark}cancelled{/}

        """

    class phase_5_wait_2:
      description="""
        I delivered my 2nd assignment, a {mark}$1,750,000{/} bot!
        My share was [money_str[bp_actual_payment]], my first sale over $1M!
        I hope {mark}[ns_teacher_name]{/} calls with another assignment soon.

        """

    class phase_6_bot_special:
      description="""
        I got my 3rd assignment:
        -  Special bot provided by {mark}[ns_teacher_name]{/}
        -  {mark}100% {/}Integrity and Stability
        -  {mark}S level{/} Sex skill
        -  Price{mark} $1,500,000{/}
        -  My share{mark} $750,000{/} (half in advance)
        -  No bonus or penalty
        -  After {mark}6 weeks (day [bp_game_over]){/} your partnership with{mark} [ns_teacher_name]{/} will be {mark}cancelled{/}
          
        """

    class phase_7_bot_special_delay:
      description="""
        I deliver the 'Sucky Bot' special bot next {mark}Sunday night{/} at {mark}[ns_teacher_name]'s{/} place.
        I'm looking forward to seeing where she lives and meeting the client who wants such a strange, antique bot will be interesting.
          
        """

    class phase_8_wait_3:
      description="""
        Wow, I can't believe I had sex with {mark}[ns_teacher_name]{/}!
        I delivered my 3rd assignment, that was a really strange bot.
        I made {mark}$750,000{/} and it was fun to work on the old tech in that bot.
        The Syndicate boss's brother was the client, that's a little scary.
        I guess {mark}[ns_teacher_name]{/} will call me when she has another client.

        """
    class phase_9_bot_pair_1:
      description="""
        I got my 4th assignment:
        -  Pair of bots, {mark}ER-Sigrid m2{/} and {mark}ER-Brutus III{/}
        -  All {mark}S{/} parts (both bots)
        -  {mark}100% {/}Integrity and Stability (both bots)
        -  {mark}S level{/} Combat, Sex, and Social skills (both bots)
        -  Price{mark} $5,000,000{/}
        -  My share{mark} $3,500,000{/} (half in advance)
        -  Delivery bonus of{mark} $400,000{/} if less than {mark}2 weeks{/}
        -  Penalty of{mark} $400,000{/} after {mark}6 weeks{/}
        -  After {mark}10 weeks (day [bp_game_over]){/} your partnership with{mark} [ns_teacher_name]{/} will be {mark}cancelled{/}

        """

    class phase_10_wait_4:
      description="""
        I delivered my 4th assignment, a pair this time!
        Wow, a {mark}$5,000,000{/} deal for 2 bots and my share was [money_str[bp_actual_payment]]!
        It takes longer to build and train 2 bots but the money is great.
        I hope {mark}[ns_teacher_name]{/} give me more assignments for pairs.

        """

    class phase_11_bot_pair_2:
      description="""
        I got my 5th assignment:
        -  Pair of bots provided by {mark}[ns_teacher_name]{/}
        -  All {mark}S{/} rated parts (both bots)
        -  {mark}100% {/}Integrity and Stability (both bots)
        -  {mark}S level{/} Combat, Sex, and Social skills (both bots)
        -  Price{mark} $7,500,000{/}
        -  My share{mark} $3,750,000{/} (half in advance)
        -  Delivery bonus of{mark} $500,000{/} if less than {mark}2 weeks{/}
        -  Penalty of{mark} $500,000{/} after {mark}6 weeks{/}
        -  After {mark}10 weeks (day [bp_game_over]){/} your partnership with{mark} [ns_teacher_name]{/} will be {mark}cancelled{/}

        """

    class phase_12_bot_pair_2_delay:
      description="""
        I will deliver the pair of special bots after the show at {mark}Raymond's Bot Boutique{/}.
        It will be fun to watch the people's faces when they see me delivering these expensive bots but {mark}[ns_teacher_name]{/} is right, I need to be nice to them.
          
        """

    class phase_13_wait_5: ## this is the final phase of this quest, it will remain open until the version containing the "Revenge" quest
      description="""
        I delivered my 5th assignment, I wonder where {mark}[ns_teacher_name]{/} found those bots?
        Custom bots to match some old movie, maybe I should watch the movie on the net.
        A {mark}$7,500,000{/} sale for 2 bots and my share was [money_str[bp_actual_payment]].
        I wonder what {mark}[ns_teacher_name]'s{/} next assignments will be?
        {good}(The next assignment in the business partnership will be in a future version.){/}

        """
    class phase_1000_businesspartners_done:
      description="Our Business Partnership has been taken to a new level."
      
    class phase_2000_businesspartners_failed:           ##  placeholder, this cannot happen
      description="You are stupid!"

##==========BORDER WITH EVENT HANDLING FUNCTION===========

init python hide:
  @event_handler("time_advanced")
  def businesspartners_event():
    if not quests.businesspartners.started and fwb_can_start_bp==1:               ## quest available but hasn't started 
      if now("afternoon") and (now("Monday") or now("Thursday")):                 ## Monday or Thursday afternoon
        global bp_who_called
        bp_who_called=1                                                           ## set flag to Simone calling MC
        queue_event("business_partners_start")
    if quests.businesspartners.started and not quests.businesspartners.finished:  ## inside the business partners quest
      
##      print "Now: [now.day]  Next Deal: [bp_next_deal]"
      
      if bp_next_deal!=0 and bp_next_deal==now.day:                               ## deal active and timer for next event reached
        global bp_next_deal
        bp_next_deal=0                                                            ## clear flag
        if quests.businesspartners=="accept_deal":
          queue_event("business_partners_bot_1")
        elif quests.businesspartners=="wait_1":
          queue_event("business_partners_bot_2")
        elif quests.businesspartners=="wait_2":
          queue_event("business_partners_bot_special")
        elif quests.businesspartners=="wait_3":
          queue_event("business_partners_bot_pair_1")
        elif quests.businesspartners=="wait_4":
          queue_event("business_partners_bot_pair_2")
    global bp_deal_active
    global bp_bonus_end
    global bp_penalty_start
    global bp_game_over

    if now("morning"):                                                                ## warnings about deals come in the morning
      if now.day==bp_game_over+1:                                                     ## game over event, Ruthie and Simone leave you and you're blacklisted
        queue_event("bp_game_over")
      elif bp_deal_active==1:                                                         ## deal status info, all deals have game over
        if quests.businesspartners=="bot_1" or quests.businesspartners=="bot_2":      ## deals 1&2: bonus and penalty
          if now.day+1==bp_bonus_end:                                                 ## bonus ends tomorrow
            queue_event("bonus_warning",1)
          elif now.day==bp_bonus_end:                                                 ## bonus ends today
            queue_event("bonus_warning",0)
          elif now.day+1==bp_penalty_start:                                           ## penalty starts after tomorrow
            queue_event("penalty_warning",1)
          elif now.day==bp_penalty_start:                                             ## penalty starts after today
            queue_event("penalty_warning",0)
          elif now.day+7==bp_game_over:                                               ## 1 week until day before game over
            queue_event("game_over_warning",7)
          elif now.day+1==bp_game_over:                                               ## tomorrow is day before game over
            queue_event("game_over_warning",1)
          elif now.day==bp_game_over:                                                 ## today is day before game over
            queue_event("game_over_warning",0)
        elif quests.businesspartners=="bot_special" and not receive_sucky==3:         ## deal 3: check delivery committment flag!, no bonus or penalty
          if now.day+7==bp_game_over:                                                 ## 1 week until day before game over
            queue_event("game_over_warning",7)
          elif now.day+1==bp_game_over:                                               ## tomorrow is day before game over
            queue_event("game_over_warning",1)
          elif now.day==bp_game_over:                                                 ## today is day before game over
            queue_event("game_over_warning",0)
        elif quests.businesspartners=="bot_pair_1":                                   ## deal 4: bonus and penalty
          if now.day+1==bp_bonus_end:                                                 ## bonus ends tomorrow
            queue_event("bonus_warning",1)
          elif now.day==bp_bonus_end:                                                 ## bonus ends today
            queue_event("bonus_warning",0)
          elif now.day+1==bp_penalty_start:                                           ## penalty starts after tomorrow
            queue_event("penalty_warning",1)
          elif now.day==bp_penalty_start:                                             ## penalty starts after today
            queue_event("penalty_warning",0)
          elif now.day+14==bp_game_over:                                              ## 2 weeks until day before game over
            queue_event("game_over_warning",14)
          elif now.day+7==bp_game_over:                                               ## 1 week until day before game over
            queue_event("game_over_warning",7)
          elif now.day+1==bp_game_over:                                               ## tomorrow is day before game over
            queue_event("game_over_warning",1)
          elif now.day==bp_game_over:                                                 ## today is day before game over
            queue_event("game_over_warning",0)
        elif quests.businesspartners=="bot_special":                                  ## deal 3: no bonus or penalty
          if now.day+7==bp_game_over:                                                 ## 1 week until day before game over
            queue_event("game_over_warning",7)
          elif now.day+1==bp_game_over:                                               ## tomorrow is day before game over
            queue_event("game_over_warning",1)
          elif now.day==bp_game_over:                                                 ## today is day before game over
            queue_event("game_over_warning",0)
        elif quests.businesspartners=="bot_pair_2" and not receive_frankie_bride==3:  ## deal 5: check delivery committment flag!, bonus and penalty
          if now.day+1==bp_bonus_end:                                                 ## bonus ends tomorrow
            queue_event("bonus_warning",1)
          elif now.day==bp_bonus_end:                                                 ## bonus ends today
            queue_event("bonus_warning",0)
          elif now.day+1==bp_penalty_start:                                           ## penalty starts after tomorrow
            queue_event("penalty_warning",1)
          elif now.day==bp_penalty_start:                                             ## penalty starts after today
            queue_event("penalty_warning",0)
          elif now.day+14==bp_game_over:                                              ## 2 weeks until day before game over
            queue_event("game_over_warning",14)
          elif now.day+7==bp_game_over:                                               ## 1 week until day before game over
            queue_event("game_over_warning",7)
          elif now.day+1==bp_game_over:                                               ## tomorrow is day before game over
            queue_event("game_over_warning",1)
          elif now.day==bp_game_over:                                                 ## today is day before game over
            queue_event("game_over_warning",0)

##    print "phase: ",quests.businesspartners
##    print "receive_sucky: ",receive_sucky
##    print "bp_deliver_frankie_bride: ",bp_deliver_frankie_bride

    global receive_sucky
    global bp_deliver_sucky
    global receive_frankie_bride
    global bp_deliver_frankie_bride
    if now("afternoon") and receive_sucky==1:                                                 ## receive sucky in the afternoon after learning about the deal
      queue_event("business_partners_receive_special_bot")
    elif now("night") and now("Sunday") and receive_sucky==3 and now.day>=bp_deliver_sucky:   ## time to deliver sucky to Simone's home
      queue_event("deliver_sucky_bot")
## 0.15.n was "tomorrow night" in 0.14 but if "tomorrow night" was Sunday you could date Simone in the evening and then deliver the bots at night which is unrealistic
##        changed to "next Saturday" and made the conditional like delivering Sucky       
##    elif now("night") and bp_deliver_frankie_bride!=0 and now.day>=bp_deliver_frankie_bride:  ## time to deliver frankie and bride to Raymond's
    elif now("night") and now("Saturday") and receive_frankie_bride==3 and now.day>=bp_deliver_frankie_bride:
      queue_event("deliver_frankie_bride_bots")

## 0.16 insert call - MC and Ruthie relationship conversation 
    global bp_night_conversation
    if now("night") and bp_night_conversation==1:  ## flag variable 'bp_night_conversation' set to 1 when Frankie and Bride were delivered
      bp_night_conversation=0                      ## clear flag so the conversation is not repeated
      queue_event("relationship_conversation_1")

    return

##==========BP BUTTONS FUNCTION==========

label business_partners_buttons():
  if bp_deal_active==1:
    if quests.businesspartners=="bot_1":
      choice("bp_bot_check_1", pos=13) "Bot Check"
      choice("deliver_deal_1_test",hint="deliver bot",pos=14) "Call [ns_teacher_name]"
    elif quests.businesspartners=="bot_2":
      choice("bp_bot_check_2", pos=13) "Bot Check"
      choice("deliver_deal_2_test",hint="deliver bot",pos=14) "Call [ns_teacher_name]"
    elif quests.businesspartners=="bot_special":
      $global receive_sucky
      if receive_sucky==2:                                                                                   ## display buttons after receiving sucky
        choice("work_on_sucky",hint="(Interact)",pos=12) "Sucky Bot"
        choice("bp_bot_check_3", pos=13) "Bot Check"
        choice("deliver_deal_3_test",hint="deliver bot",pos=14) "Call [ns_teacher_name]"
    elif quests.businesspartners=="bot_pair_1":
      choice("bp_bot_check_4", pos=13) "Bot Check"
      choice("deliver_deal_4_test",hint="deliver bots",pos=14) "Call [ns_teacher_name]"
    elif quests.businesspartners=="bot_pair_2":
      $global receive_frankie_bride
      
##      $print "XXXXXXXXXXXXX receive_frankie_bride: ",receive_frankie_bride
      
      if receive_frankie_bride==1:                                                                          ## display button to call Simone to receive bots
        choice("business_partners_receive_bot_pair_2",hint="receive bots",pos=14) "Call [ns_teacher_name]"
      elif receive_frankie_bride==2:                                                                        ## display check and deliver buttons after receiving bots
        choice("bp_bot_check_5", pos=13) "Bot Check"
        choice("deliver_deal_5_test",hint="deliver bots",pos=14) "Call [ns_teacher_name]"
  if bp_date_available==1:
    choice(None,hint="$750,3AP,Time",pos=15) "Date [ns_teacher_name]"
  return

##==========START QUEST FUNCTION==========

label business_partners_start():
  $global bp_who_called
  $global bp_first_call
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Business Partnership with {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="quests business_partners bp_2"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="quests business_partners bp_1"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  if bp_first_call==1:    ## first call
    $bp_first_call=0      ## clear flag    
    if bp_who_called==0:  ## MC called Simone
      "I call {mark}[ns_teacher_name]{/} to discuss the business partnership. When she answers {mark}[ns_teacher_name]{/} says: {say}Hi {mark}[mc.name]{/}, it's good to hear from you. Let me describe the terms of a partnership, I think you'll like them.{/}"
      ""
      ""
      ""
      "I reply cautiously: {mcsay}Sure, I'd like to know what your proposal is all about.{/} {mark}[ns_teacher_name]{/} says: {say}Great, here's what I propose...{/}"
    else:                 ## Simone called MC
      "I receive a call from {mark}[ns_teacher_name]{/}, I guess she wants to discuss the partnership. I accept the call and say: {mcsay}Hi {mark}[ns_teacher_name]{/}, how are you?{/} She replies: {say}Hi {mark}[mc.name]{/}, I'm fine thanks. I haven't heard from you and I'd really like to give you the details about my proposal.{/}"
      ""
      ""
      "It might be a good idea and {mark}[gn_store_owner_name]{/} and I both like {mark}[ns_teacher_name]{/}. I've got nothing to lose by listening to her proposal: {mcsay}OK, I'd like to know what you're proposing."
    choice("business_partners_start_1") "Continue"  ## first call must review terms    
  else:                   ## NOT first call
    if bp_who_called==0:  ## MC called Simone
      "I call {mark}[ns_teacher_name]{/} to discuss the business partnership. When she answers {mark}[ns_teacher_name]{/} says: {say}Hi {mark}[mc.name]{/}, I'm glad you called. I'm anxious to get started, I hope you're ready to accept but maybe you want to review the terms?{/}"
      ""
      ""
      ""
      "I think about it for a minute. I remember her terms and they were pretty generous. Should I ask her to review them?"
    else:                 ## Simone called MC  
      "I receive a call from {mark}[ns_teacher_name]{/}, she's very persistant. I accept the call and say: {mcsay}Hi {mark}[ns_teacher_name]{/}, how are you?{/} She replies in a playful voice: {say}Hi {mark}[mc.name]{/}, I'm fine and anxious to get started, are you ready to accept? You know I won't stop calling until you do!{/}"    
      ""  
      ""
      "I'm not sure what's holding me back, {mark}[gn_store_owner_name]{/} and I both like {mark}[ns_teacher_name]{/}. Should I ask her to review the terms again?"
    choice("business_partners_start_1") "Review Terms"
    choice("business_partners_start_4") "Make Decision"
  return

label business_partners_start_1():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Business Partnership with {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_4"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_3"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} says: {say}I find rich customers who want custom bots. You build and train the bots and we split the sales. {mark}[mc.name]{/} {say}these are rich customers, we'll charge at least {mark}$1,000,000 per bot{/} and a lot more if they want A or S level bots."
  ""
  ""
  "That sounds amazing, if she finds customers and my share is decent I'll make a lot more money than I do now. I ask: {mcsay}That sounds good but how will we split the sales?"
  choice("business_partners_start_2") "Continue"
  return

label business_partners_start_2():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Business Partnership with {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_6"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_5"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} replies; {say}Great question, when they want a standard bot you provide the bot and parts and to compensate for the expense you'll get {mark}70%% of the sales price{/}. Your share is at least {mark}$700,000 per bot{/} and much more for A or S level bots.{/}"
  ""
  ""
  "I'm surprised at the split, it's more than fair and I'd make a lot of money. I say: {mcsay}That's a very nice offer, I've never sold bots for that much money.{/}"
  choice("business_partners_start_3") "Continue"
  return

label business_partners_start_3():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Business Partnership with {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_8"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_7"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} continues: {say}We'll do even better with non-standard bots. I'll provide the bots and you'll provide the parts and training. Since I'll be providing the bots the split will be {mark}50:50{/} but I guarantee you more than {mark}$700,000 for each non-standard bot{/}.{/}"
  ""
  "{size=-12} "
  "I can't believe these numbers so I ask: {mcsay}Are you sure about all of this? It sounds too good to be true.{/} She replies: {say}I'm absolutely certain of it. To prove it I'll advance you {mark}half of your share{/} every time I give you an order. That's at least {mark}$350,000{/} in advance.{/}"  
  choice("business_partners_start_4") "Continue"
  return

label business_partners_start_4():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Business Partnership with {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_9"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_10"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  ""
  "The terms of the partnership are very good. I get at least {mark}$350,000{/} each time she delivers an order and at least another {mark}$350,000{/} when she delivers the bot to the customer."
  ""
  "The advance will cover the cost of bots and parts. Even if the sale never happens I'll have that plus whatever I can get for the bot on the grey net."
  ""
  "{mark}Simone{/} is waiting for my answer. {mark}Should I do it?{/}"
  choice("accept_partnership") "Accept"
  choice("decline_partnership") "Decline"
  return

label accept_partnership():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Business Partnership with {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_11"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_12"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  ""
  "I tell {mark}[ns_teacher_name]{/}: {mcsay}You've got yourself a partner, this sounds amazing. How soon can we get started?{/}"
  ""
  ""
  ""
  "{mark}[ns_teacher_name]{/} replies: {say}That's great, I'm looking forward to making a lot of money together! I'm sending a bot over to your shop right now with a new suit for you to go to {mark}Raymond's{/}. Give me a few days to line up our first customer, I'll call you soon.{/}"
  ""
  $fwb_can_start_bp=0                       ## clear flag to remove button to call Simone that starts this quest
  $bp_next_deal=now.day+2                   ## 2 days until first deal is ready
  
##  $print "Now: [now.day]  Next Deal: [bp_next_deal]"
  
  $quests.freelancer.finish()               ## finish freelancer quest at last!!!
  $quests.start_quest("businesspartners")
  choice("bot_delivers_suit") "End Call"
  return
  
label bot_delivers_suit():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]'s{/} Bot Delivers a New Suit"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_47"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_48"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  ""
  "I can't believe how fast {mark}[ns_teacher_name]'s{/} bot got here. Without saying a word she walks up to me and hands me a bag that must contain a suit and a box that must be shoes."
  ""
  "As quickly as she arrived, the bot turns and leaves."
  ""
  "I'll probably need to use {mark}Raymond's{/} because I can't depend upon scavenging the right luxury bot when I need it. With the prices we'll be charging I can afford to buy luxury bots if I need them."
  ""
## 0.14 these two variables are created but will not do anything until 0.15
  $global bp_suit_for_rays
  $global fwb_deactivate_rays
  $bp_suit_for_rays=1          ## you have the black striped suit (store_raysbotshop.rpy)
  $fwb_deactivate_rays=0       ## visits to Raymond's Bot Boutique are active again (netconsole_net_sites.rpy)
  choice("<<<") "Continue"
  return

label decline_partnership():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Business Partnership with {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_13"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_14"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  ""
  "I tell {mark}[ns_teacher_name]{/}: {mcsay} I'm still not sure, please give me another day or two to think it over. I'm sorry but I'm a little nervous about this.{/}"
  ""
  ""
  ""
  "{size=-4} "
  "{mark}[ns_teacher_name]{/} sounds disappointed when she says: {say}OK, but please don't take too long. This is a great opportunity for both of us and since I'll handle the customers you're not taking any risks."
  choice("<<<") "End Call"
  return

##==========1ST BOT ORDER==========

label business_partners_bot_1():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Calls"
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_15"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_16"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "You're excited to receive a call from {mark}[ns_teacher_name]{/} to tell you about your 1st business partnership bot deal. I need to call {mark}[ns_teacher_name]{/} when the bot is ready and she'll pick it up."
  "{size=-16} "
  "{size=-6}-  {mark}AGTY-36{/} Bot{/}"
  "{size=-6}-  All {mark}A+{/} parts{/}"
  "{size=-6}-  {mark}100%% {/}Integrity{/}"
  "{size=-6}-  {mark}100%% {/}Stability{/}"
  "{size=-6}-  {mark}S level{/} Combat skill{/}"
  "{size=-6}-  {mark}S level{/} Sex skill{/}"
  "{size=-6}-  {mark}S level{/} Social skill{/}"
  "{size=-6}-  Price{mark} $1,000,000{/}{/}"
  "{size=-6}-  My Share{mark} $700,000{/} (half in advance){/}"
  "{size=-6}-  Bonus {mark} $100,000{/} if within {mark}1 week{/}{/}"
  "{size=-6}-  Penalty {mark} $100,000{/} if longer than {mark}3 weeks{/}{/}"
  "{size=-6}-  Partnership dissolved if longer than {mark}5 weeks{/}{/}"
  "{size=-16} "
  $mc.money+=350000                   ## half of $700,000 up front 
  $bp_deal_active=1
##  $bp_bonus_end=now.day+3             ## testing only
##  $bp_penalty_start=now.day+6         ## testing only
##  $bp_game_over=now.day+14            ## testing only
  $bp_bonus_end=now.day+7
  $bp_penalty_start=now.day+21
  $bp_game_over=now.day+35
  $quests.businesspartners.advance()
  choice("<<<") "Done"
  return

##==========2nd BOT ORDER==========

label business_partners_bot_2():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Calls"
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_17"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_18"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "You receive a call from {mark}[ns_teacher_name]{/} to tell you about your 2nd bot deal. I need to call {mark}[ns_teacher_name]{/} when the bot is ready and she'll pick it up."
  "{size=-16} "
  "{size=-6}-  {mark}Tanjiro SX{/} Bot{/}"
  "{size=-6}-  All {mark}S{/} parts{/}"
  "{size=-6}-  {mark}100%% {/}Integrity{/}"
  "{size=-6}-  {mark}100%% {/}Stability{/}"
  "{size=-6}-  {mark}S level{/} Combat skill{/}"
  "{size=-6}-  {mark}S level{/} Sex skill{/}"
  "{size=-6}-  {mark}S level{/} Social skill{/}"
  "{size=-6}-  Price{mark} $1,750,000{/}{/}"
  "{size=-6}-  My Share{mark} $1,225,000{/} (half in advance){/}"
  "{size=-6}-  Bonus {mark} $200,000{/} if within {mark}1 week{/}{/}"
  "{size=-6}-  Penalty {mark} $200,000{/} if longer than {mark}3 weeks{/}{/}"
  "{size=-6}-  Partnership dissolved if longer than {mark}5 weeks{/}{/}"
  "{size=-16} "
  $mc.money+=612500                   ## half of $1,225,000 up front
  $bp_deal_active=1
##  $bp_bonus_end=now.day+3             ## testing only
##  $bp_penalty_start=now.day+6         ## testing only
##  $bp_game_over=now.day+14            ## testing only
  $bp_bonus_end=now.day+7
  $bp_penalty_start=now.day+21
  $bp_game_over=now.day+35
  $quests.businesspartners.advance()
  choice("<<<") "Done"
  return

##==========3rd BOT ORDER==========

label business_partners_bot_special():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Calls"
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over
  $global receive_sucky
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_19"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_20"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "You receive a call from {mark}[ns_teacher_name]{/} to tell you about your 3rd bot deal, it's some kind of special bot that doesn't even need a capsule! {good}I'll get my advance when she delivers the bot this afternoon{/}."
  "{size=-16} "
  "{size=-6}-  Bot to be delivered by {mark}[ns_teacher_name]{/}{/}"
  "{size=-6}-  Parts will not be required, huh?{/}"
  "{size=-6}-  The bot does not require a {mark}Capsule{/}, what!{/}"
  "{size=-6}-  Storage will not require a {mark}Bot Support System{/}"
  "{size=-6}-  {mark}100%% {/}Integrity{/}"
  "{size=-6}-  {mark}100%% {/}Stability{/}"
  "{size=-6}-  {mark}S level{/} Sex skill{/}"
  "{size=-6}-  Price{mark} $1,500,000{/}{/}"
  "{size=-6}-  My share{mark} $750,000{/}{/}"
  "{size=-6}-  No bonus or penalty{/}"
  "{size=-6}-  Partnership dissolved if longer than {mark}6 weeks{/}{/}"
  "{size=-16} "
  $receive_sucky=1                    ## set flag to receive sucky this afternoon, receive advance then
  $bp_deal_active=1
  $bp_bonus_end=0                     ## no bonus for deal 3
  $bp_penalty_start=0                 ## no penalty for deal 3
##  $bp_game_over=now.day+3             ## testing only
  $bp_game_over=now.day+42            ## change number to 42 for release
  $quests.businesspartners.advance()
  choice("<<<") "Done"
  return

##==========4th BOT ORDER==========

label business_partners_bot_pair_1():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Calls"
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_21"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_22"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "You receive a call from {mark}[ns_teacher_name]{/} to tell you about your 4th bot deal, it's a pair this time! I need to call {mark}[ns_teacher_name]{/} when both bots are ready and she'll pick them up."
  "{size=-16} "
  "{size=-6}-  2 bots, {mark}ER-Sigrid m2{/} and {mark}ER-Brutus III{/}{/}"
  "{size=-6}-  All {mark}S{/} parts (both bots){/}"
  "{size=-6}-  {mark}100%% {/}Integrity (both bots){/}"
  "{size=-6}-  {mark}100%% {/}Stability (both bots){/}"
  "{size=-6}-  {mark}S level{/} Combat skill (both bots){/}"
  "{size=-6}-  {mark}S level{/} Sex skill (both bots){/}"
  "{size=-6}-  {mark}S level{/} Social skill (both bots){/}"
  "{size=-6}-  Price{mark} $5,000,000{/} (both bots){/}"
  "{size=-6}-  My share{mark} $3,500,000{/} (half in advance){/}"
  "{size=-6}-  Bonus {mark} $400,000{/} if within {mark}2 weeks{/}{/}"
  "{size=-6}-  Penalty {mark} $400,000{/} if longer than {mark}6 weeks{/}{/}"
  "{size=-6}-  Partnership dissolved if longer than {mark}10 weeks{/}{/}"
  "{size=-16} "
  $mc.money+=1750000                    ## half of $3,500,000 up front
  $bp_deal_active=1
##  $bp_bonus_end=now.day+3             ## testing only
##  $bp_penalty_start=now.day+6         ## testing only
##  $bp_game_over=now.day+21            ## testing only
  $bp_bonus_end=now.day+14
  $bp_penalty_start=now.day+42
  $bp_game_over=now.day+70
  $quests.businesspartners.advance()
  choice("<<<") "Done"
  return

##==========5th BOT ORDER==========

label business_partners_bot_pair_2():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Calls"
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over
  $global receive_frankie_bride
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_15"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_16"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "You receive a call from {mark}[ns_teacher_name]{/} to tell you about your 5th bot deal, it's a pair of special bots and I'll get my advance when she delivers them. {good}I need to call her when I have capsules or storage space for them{/}."
  "{size=-16} "
  "{size=-6}-  2 bots to be delivered by {mark}[ns_teacher_name]{/}{/}"
  "{size=-6}-  All {mark}S{/} parts (both bots){/}"
  "{size=-6}-  {mark}100%% {/}Integrity (both bots){/}"
  "{size=-6}-  {mark}100%% {/}Stability (both bots){/}"
  "{size=-6}-  {mark}S level{/} Combat skill (both bots}){/}"
  "{size=-6}-  {mark}S level{/} Sex skill (both bots){/}"
  "{size=-6}-  {mark}S level{/} Social skill (both bots){/}"
  "{size=-6}-  Price{mark} $7,500,000{/}{/}"
  "{size=-6}-  My share{mark} $3,750,000{/}{/}"
  "{size=-6}-  Bonus {mark} $500,000{/} if within {mark}2 weeks{/}{/}"
  "{size=-6}-  Penalty {mark} $500,000{/} if longer than {mark}6 weeks{/}{/}"
  "{size=-6}-  Partnership dissolved if longer than {mark}10 weeks{/}{/}"
  "{size=-16} "
  $bp_deal_active=1
##  $bp_bonus_end=now.day+3             ## testing only
##  $bp_penalty_start=now.day+6         ## testing only
##  $bp_game_over=now.day+21            ## testing only
  $bp_bonus_end=now.day+14
  $bp_penalty_start=now.day+42
  $bp_game_over=now.day+70
  $quests.businesspartners.advance()
  $receive_frankie_bride=1            ## set flag for call Simone button to receive bots
  choice("<<<") "Done"
  return

##====RECEIVE BOT(S) FROM SIMONE FUNCTIONS====

label business_partners_receive_special_bot():  ## always happens next turn because there is no space requirement, Sucky has a special charger
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Delivers the Special Bot"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_23"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_24"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} comes into the shop with two of her combat bots behind her carrying a strange looking bot and some sort of device with it. The bot's head is attached to the device! {mark}[ns_teacher_name]{/} says; {say}Hi {mark}[mc.name]{/}, where do you want this stuff?{/}"
  ""
  ""
  "You realize you're staring and being impolite so you say; {mcsay}Hi {mark}[ns_teacher_name]{/}, your bots can put the bot on the gurney and whatever that thing is with the head on the cart next to it.{/}"
  choice("bprsb_2") "Continue"        ## bprsb2 - Business Partner Receive Special Bot
  return

label bprsb_2():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Delivers the Special Bot"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_25"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_26"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "You're afraid she expects you to fix this thing! You say; {mcsay}I've never seen a bot like this, it must be 50 years old! Where did this antique come from and what are you expecting me to do with it?{/}"
  ""
  ""
  ""
  "{mark}[ns_teacher_name]{/} says; {say}It's an old model named '{mark}Sucky Bot{/}' which was the first to have a primitive Psychocore. An eccentric customer obtained it from who knows where and needs someone to make it work."
  choice("bprsb_3") "Continue"
  return

label bprsb_3():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Delivers the Special Bot"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_27"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_28"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "You tell {mark}[ns_teacher_name]{/}; {mcsay}I have no idea how to work on an this thing, it's nothing like any bot I've ever restored. What's this strange device the head is attached to and where do I get parts if I need them?"
  ""
  ""
  "{mark}[ns_teacher_name]{/} says; {say}That device is the charger which is a primitive capsule and you need to get it working first. You won't need parts, everything is in reasonably good condition. Research '{mark}Sucky Bot{/}' on the net and I'm certain you'll will be able to fix it. Trust me, this won't be as hard as you think."
  choice("bprsb_4") "Continue"
  return

label bprsb_4():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Delivers the Special Bot"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_29"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_30"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "I hope she's right, this could be a disaster! You're curious so you ask; {mcsay}I wonder who would want a bot like this, can I meet the client?{/} She doesn't reply while she gives you the advance payment."
  "{size=-12} "
  $mc.money+=375000     ## half of $750,000 up front
  $receive_sucky=2      ## set flag so the button to work on sucky is displayed
  ""
  "After a moment {mark}[ns_teacher_name]{/} starts to walk away but then turns and gives you a smile and a wink like she's up to something and says; {say}If you can find something better to wear you can deliver the bot in person at my place.{/} Before you can reply she turns around and leaves."
  choice("bprsb_5") "Continue"
  return

label bprsb_5():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Delivers the Special Bot"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_31"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_32"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "I guess I have no choice but to get some nicer clothes if I want to meet whoever wants this bot. I'll go online and see what I can find, what a pain in the ass."
  ""
  "Ok, I found some new clothes, I hope {mark}[ns_teacher_name]{/} will be happy. I also found an outfit to surprise {mark}[gn_store_owner_name]{/} with."
  "{size=-12} "
  $mc.money-=2500
  ""
  "It will be interesting to see where {mark}[ns_teacher_name]{/} lives, I'm sure it's no where near her school."
  ""
 
  $global fwb_mc_new_clothes            ## flag from fwb: MC wears new clothing when dating Ruthie and white suit when dating Simone
  $fwb_mc_new_clothes=1                 ## NOTE: striped suit for Raymond's uses 'bp_suit_for_rays'
  choice("<<<") "Done"
  return

label business_partners_receive_bot_pair_2():  ## you call to request the bots: if capsules/storage available she comes immediately, if not abort call (dumbass!)
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Call {mark}[ns_teacher_name]{/} to Deliver Bots"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")                                         ## set up for images but don't draw them yet
  if (home.available_capsules + workshop.available_space)<2:  ## you can't call now, not enough space for the bots, 1 image with MC thinking
    $action_image= "quests business_partners bp_33"
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    "Before making the call I realized that I don't have enough space for 2 bots. I need 2 empty capsules, 2 empty spaces in storage, or 1 of each before I can ask {mark}[ns_teacher_name]{/} to bring me the bots."
    choice("<<<") "Continue"
  else:                                                       ## you call now, 2 images: MC on phone and Simone on phone
    $action_image= "quests business_partners bp_17"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests business_partners bp_18"
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    ""
    "When she answers I say; {mcsay} Hi {mark}[ns_teacher_name]{/}, I hope this is a good time. I've got everything ready for the two special bots if you're able to deliver them now.{/}"
    ""
    ""
    ""
    "{mark}[ns_teacher_name]{/} sounds pleased; {say}Hi {mark}[mc.name]{/}, it's good to hear from you. Fortunately I have time right now to deliver them, please wait a few minutes and I'll be over as fast as possible.{/}" 
    choice("bprbp2_2") "Wait..."        ## bprbp2 - Business Partner Receive Bot Pair 2
  return

label bprbp2_2():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Delivers the Special Bots"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_35"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_36"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} arrives with one of her combat bots and the special bots. This time the special bots are functional and can walk in. They are certainly unusual! {mark}[ns_teacher_name]{/} walks up and gives me a hug; {say}Hi! I think you'll enjoy this assignment!{/}"
  ""
  "{size=-12} "
  "While you're looking at the bots; {mcsay}These are certainly not your typical bots. I guess they have some sort of theme involved?{/} As her combat bot gives you the advance payment {mark}[ns_teacher_name]{/} says; {say}They certainly do, let me tell you about them.{/}"
  "{size=-12} "
  $mc.money+=1875000             ## half of $3,750,000 up front
  choice("bprbp2_3") "Continue"
  return

label bprbp2_3():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Delivers the Special Bots"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_37"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_38"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")    
  "{mark}[ns_teacher_name]{/} says; {say}The client wants bots from an old movie made around 150 years ago called {mark}Frankenstein{/}. As they used to say, '{mark}I know a guy{/}', so I had a pair of bots altered to look like the pictures the client gave me. This is a very, very good deal for us.{/}"
  ""
  "{size=-12} "
  "You ask; {mcsay}That's a strange request for sure, what sort of person is this client?{/} {mark}[ns_teacher_name]{/} replies; {say}Actually you met them at {mark}Raymond's Bot Boutique{/}. The client is the couple that was very rude to you and {mark}[gn_store_owner_name]{/} just before you left.{/}"
  choice("bprbp2_4") "Continue"
  return

label bprbp2_4():
  $global receive_frankie_bride
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Delivers the Special Bots"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_39"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_40"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")  
  "{mark}[ns_teacher_name]{/} looks serious; {say}You're probably thinking about sabotaging the bots to get even but don't do that. This sale is really important and will get us noticed by the rich clientele at {mark}Raymond's{/}. If we do this right we will get a lot more business there.{/}"
  ""
  ""
  "She's right; {mcsay}OK, I'll play nice.{/} {mark}[ns_teacher_name]{/} smiles as she gets ready to leave; {say}Don't worry, you'll get to rub this in their faces by delivering the bots in person at a special event I'm arranging at {mark}Raymond's{/}. Trust me, this is the start of big things for us.{/}"
  $bot_cls=store.SexBot_frankie_bot                                                 ## find frankie_bot class
  $temp_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))       ## add frankie_bot to global store
  $store.global_bots_counter+=1                                                     ## increase counter for next bot addition
  $generate_bot_warranty_seals(temp_bot,default_generate_bot_warranty_seals_table)  ## set frankie_bot warranty seals
  $temp_bot.add_role("bp_special_bot")                                              ## add role limiting bot to: train, tinker, replace_part, hack
  call sr24_add_bot_do(temp_bot)                                                    ## put frankie in 1st of the at least 2 empty capsules
  $bot_cls=store.SexBot_frankie_bride_bot                                           ## find frankie_bride_bot class
  $temp_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))       ## add frankie_bride_bot to global store
  $store.global_bots_counter+=1                                                     ## increase counter for next bot addition
  $generate_bot_warranty_seals(temp_bot,default_generate_bot_warranty_seals_table)  ## set frankie_bride_bot warranty seals
  $temp_bot.add_role("bp_special_bot")                                              ## add role limiting bot to: train, tinker, replace_part, hack
  call sr24_add_bot_do(temp_bot)                                                    ## put frankie_bride_bot into 2nd of the at least 2 empty capsules
  $receive_frankie_bride=2                                                          ## set flag to display check bot and deliver buttons
  choice("<<<") "Done"
  return

##==========DELIVER BOT(S) FUNCTIONS==========

## DEAL 1

label deliver_deal_1_test():  ## looking for qualifying Mylou (model name: "AGTY-36""
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 1 - Select {mark}AGTY-36{/} Bot"
  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot and bot.action_allowed("sell"):
          if bot.model_name=="AGTY-36":
            if not bot["mission"]:
              if bot.chassis.integrity==100:
                if bot.psychocore.stability==100:
                  if bot.bot_combat.level_name=="S":
                    if bot.bot_sex.level_name=="S":
                      if bot.bot_social.level_name=="S":
                        bp_part_test_pass=1
                        for slot in bot.outfit_slots:
                          part=bot.item_on_slot(slot)
                          if part.rate in "FEDCB":           ## part testing uses NOT logic
                            bp_part_test_pass=0
                            break                            ##  stop testing if a failure is found, will only go on if no failures found
                        if bp_part_test_pass==1:
                          bot_price=bot_price_function(bot)  ## DO NOT OMIT
                          bots.append([bot,bot_price])       ## DO NOT OMIT
    bots=bots[:12]
  if bots:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "bots squirrel_mylou avatar"            ## Mylou
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    if len(bots)==1:  ## only 1 bot available
      $bot,bot_price=bots.pop(0)
      
##      $print "AGTY-36 bot picked: ",bot.id
      
      choice("bp_deliver_deal_1a:{}".format(bot.id)) "[bot]"
      "{mark}[bot]{/} is available to for {mark}[ns_teacher_name]{/} to pick up. I'll select it and then call her."
      ""
    else:             ## more than 1 bot available
      "I have to select which {mark}AGTY-36{/} bot I want to use for the business partnership deal. I'll select one and then call {mark}[ns_teacher_name]{/}."
      "" 
      $bot_n=0
      while bots:
        $bot,bot_price=bots.pop(0)
        $bot_n+=1
        "#[bot_n] - {mark}[bot]{/}"
        choice("bp_deliver_deal_1a:{}".format(bot.id)) "#[bot_n] - [bot]"
    choice("<<<",pos=17) "Cancel"
  else:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests business_partners bp_33"
    center "{image=[action_image]@400x600}"
    $act.set_block("c") 
    "I don't have a {mark}AGTY-36{/} bot ready to deliver for deal 1, I better get to work!"
    choice("<<<") "Oops!"
  return

label bp_deliver_deal_1a(bot):
  $bot=find_character(bot)                              ## required to pass to next function
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 1 - Call {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_19"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_20"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")  
  ""
  "You call Simone to tell her the {mark}AGTY-36{/} bot is ready and ask her when she wants to come over to get it."
  ""
  ""
  ""
  ""
  "{mark}[ns_teacher_name]{/} says that's great but she's busy right now so she'll send a pair of combat bots over to pick up the bot. She tells you they will be at your shop in a few minutes."
  choice("bp_deliver_deal_1b:{}".format(bot.id)) "Wait..."
  return

label bp_deliver_deal_1b(bot):
  $bot=find_character(bot)                              ## find the actual bot
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 1 - Bot Pickup"
  $global bp_next_deal
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_41"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_42"
  center "{image=[action_image]@400x600}"
  $act.set_block("c") 
  ""
  "The combat bots arrive to pick up the {mark}AGTY-36{/} bot and they pay you in cash."
  if now.day<=bp_bonus_end:               ## add bonus
    extend " They even brought the {mark}$100,000 bonus{/}, nice!"
    ""
    $bp_actual_payment=800000            ## journal share
    $mc.money+=450000
  elif now.day>bp_penalty_start:          ## subtract penalty
    extend " Too bad they had to subtract the {mark}$100,000 penalty{/} for late delivery."
    ""
    $bp_actual_payment=600000            ## journal share
    $mc.money+=250000
  else:                                   ## normal payment
    extend " As expected, they gave me the second half of my share of the deal."
    ""
    $bp_actual_payment=700000            ## journal share
    $mc.money+=350000       
  ""
  ""
  "You bring {mark}[bot]{/} out front and the three bots leave together. Wow, that was easy!"
  "{size=-16} "
  $temp=1.2*calc_pr_rep_gain("rep_mc_dealer","xl_g")       ## extra large gain * 1.2 for B level bot
  $mc.give_xp("rep_mc_dealer",temp)
  $temp=1.2*calc_pr_rep_gain("rep_mc_trainer","xl_g")      ## extra large gain * 1.2 for B level bot
  $mc.give_xp("rep_mc_trainer",temp)
  ""
  
##  $print "AGTY-36 bot delivered: ",bot.id
  
  $move_sexbot(bot,None)                     ## delete bot
  $bot=None                                  ## didn't use global so maybe unnecessary
  $quests.businesspartners.advance()
  $bp_next_deal=now.day+random.randint(2,5)  ## for testing fix it at 2
  $bp_deal_active=0
  $bp_bonus_end=0
  $bp_penalty_start=0
  $bp_game_over=0 
  choice("<<<") "Done"
  return

## DEAL 2

label deliver_deal_2_test():  ## looking for qualifying Tanjiro (model name: "Tanjiro SX")
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 2 - Select {mark}Tanjiro SX{/} Bot"
  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot and bot.action_allowed("sell"):
          if bot.model_name=="Tanjiro SX":
            if not bot["mission"]:
              if bot.chassis.integrity==100:
                if bot.psychocore.stability==100:
                  if bot.bot_combat.level_name=="S":
                    if bot.bot_sex.level_name=="S":
                      if bot.bot_social.level_name=="S":
                        bp_part_test_pass=1
                        for slot in bot.outfit_slots:
                          part=bot.item_on_slot(slot)
                          if part.rate in "FEDCBA":          ## part testing uses NOT logic
                            bp_part_test_pass=0
                            break                            ##  stop testing if a failure is found, will only go on if no failures found
                        if bp_part_test_pass==1:
                          bot_price=bot_price_function(bot)  ## DO NOT OMIT
                          bots.append([bot,bot_price])       ## DO NOT OMIT
    bots=bots[:12]
  if bots:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "bots squirrel_tanjiro avatar"            ## Tanjiro
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    if len(bots)==1:  ## only 1 bot available
      $bot,bot_price=bots.pop(0)

##      $print "Tanjiro SX bot picked: ",bot.id

      choice("bp_deliver_deal_2a:{}".format(bot.id)) "[bot]"
      "{mark}[bot]{/} is available to for {mark}[ns_teacher_name]{/} to pick up. I'll select it and then call her."
      ""
    else:             ## more than 1 bot available
      "I have to select which {mark}Tanjiro SX{/} bot I want to use for the business partnership deal and then call {mark}[ns_teacher_name]{/}."
      "" 
      $bot_n=0
      while bots:
        $bot,bot_price=bots.pop(0)
        $bot_n+=1
        "#[bot_n] - {mark}[bot]{/}"
        choice("bp_deliver_deal_2a:{}".format(bot.id)) "#[bot_n] - [bot]"
    choice("<<<",pos=17) "Cancel"
  else:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests business_partners bp_33"
    center "{image=[action_image]@400x600}"
    $act.set_block("c") 
    "I don't have a {mark}Tanjiro SX{/} bot ready to deliver for deal 2, I better get to work!"
    choice("<<<") "Oops!"
  return

label bp_deliver_deal_2a(bot):
  $bot=find_character(bot)                              ## required to pass to next function
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 2 - Call {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_21"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_22"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")  
  ""
  "You call Simone to tell her the {mark}Tanjiro SX{/} bot is ready and ask her when she wants to come over to get it."
  ""
  ""
  ""
  ""
  "{mark}[ns_teacher_name]{/} says that's great but she's busy right now so she'll send a pair of combat bots over to pick up the bot. She tells you they will be at your shop in a few minutes."
  choice("bp_deliver_deal_2b:{}".format(bot.id)) "Wait..."
  return

label bp_deliver_deal_2b(bot):
  $bot=find_character(bot)                              ## find the actual bot
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 2 - Bot Pickup"
  $global bp_force_store_owner_rent                     ## FLAG to force paying for Ruthie's apartment, will become a possible game over story in 0.15
  $global bp_next_deal
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_43"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_44"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""  
  "The combat bots arrive to pick up the {mark}Tanjiro SX{/} bot and they pay you in cash."
  if now.day<=bp_bonus_end:               ## add bonus
    extend " They even brought the {mark}$200,000 bonus{/}, nice!"
    ""
    $bp_actual_payment=1425000            ## journal share
    $mc.money+=812500
  elif now.day>bp_penalty_start:          ## subtract penalty
    extend " Too bad they had to subtract the {mark}$200,000 penalty{/} for late delivery."
    ""
    $bp_actual_payment=1025000            ## journal share
    $mc.money+=412500
  else:                                   ## normal payment
    extend " As expected, they gave me the second half of my share of the deal."
    ""
    $bp_actual_payment=1225000            ## journal share
    $mc.money+=612500
  ""
  ""
  "You bring {mark}[bot]{/} out front and the three bots leave together. Wow, that was easy!"
  "{size=-16} "
  $temp=1.4*calc_pr_rep_gain("rep_mc_dealer","xl_g")       ## extra large gain * 1.4 for A level bot private sale
  $mc.give_xp("rep_mc_dealer",temp)
  $temp=1.4*calc_pr_rep_gain("rep_mc_trainer","xl_g")      ## extra large gain * 1.4 for A level bot private sale
  $mc.give_xp("rep_mc_trainer",temp)
  ""

##  $print "Tanjiro SX bot delivered: ",bot.id  
  
  $move_sexbot(bot,None)                     ## delete bot
  $bot=None                                  ## didn't use global so maybe unnecessary
  $quests.businesspartners.advance()
  $bp_force_store_owner_rent=1               ## FLAG to force paying for Ruthie's new apartment, in 0.15 will become a story and new 'game over' situation
  $bp_next_deal=now.day+random.randint(2,5)  ## for testing fix it at 2
  $bp_deal_active=0
  $bp_bonus_end=0
  $bp_penalty_start=0
  $bp_game_over=0 
  choice("<<<") "Done"
  return

## DEAL 3

label deliver_deal_3_test():          ## testing sucky
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 3 - Call {mark}[ns_teacher_name]{/}"
  $global sucky_charger_integrity            ## sucky charger integrity - 0 to 100%
  $global sucky_head_integrity               ## sucky head integrity - 0 to 100%
  $global sucky_body_integrity               ## sucky body integrity - 0 to 100%
  $global sucky_stability                    ## sucky stability - 0 to 100%
  $global sucky_sex_skill                    ## sucky sex skill - <=999=F, 1000-2249=E,2250-4999=C, 5000-9999=C, 10000-22499=B, 22500-49999=A, 50000-99999=S
  $sucky_pass=0
  if sucky_charger_integrity==100:
    if sucky_head_integrity==100:
      if sucky_body_integrity==100:
        if sucky_stability==100:
          if sucky_sex_skill>=50000:
            $sucky_pass=1
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "bots sucky_robot avatar"       ## Sucky
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  if sucky_pass==0:                                ## sucky NOT ready to deliver
    "Before calling {mark}[ns_teacher_name]{/} I decided to check the special bot once more and I'm glad I did. I still have some work to do before I can deliver this bot."
    choice("<<<") "Done"
  else:                                            ## sucky ready to deliver
    "I checked the special bot once more and it's ready to deliver. I call {mark}[ns_teacher_name]{/} to tell her the bot is ready for delivery."
    "{size=-8} "
    "{mark}[ns_teacher_name]{/} says that's great, she'll arrange for a meeting on {mark}Sunday night{/} since she doesn't teach a class on Sunday. She also says I better not wear that ugly brown jacket!"
    "{size=-8} "
    "I assure her that I'll wear something better when I bring the bot and meet the client on {mark}Sunday night{/}. I also tell her I'm looking forward to visiting her and seeing where she lives."
    "{size=-8} "
    $receive_sucky=3                           ## flag 3 turns off buttons when committed to delivery and activates delivery on Sunday night
    $bp_deliver_sucky=now.day+1                ## set flag to go to Simone's at least one day away in case it's Sunday now
    $bp_game_over=0                            ## reset flag in case of last minute delivery, bonus and penalty not used in deal 3
    $quests.businesspartners.advance()         ## delay phase inserted to change description
    choice("<<<") "Done"
  return

## DEAL 4

label deliver_deal_4_test():  ## looking for qualifying Sigrid first
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 4 - Select {mark}ER-Sigrid m2{/} Bot"
  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot and bot.action_allowed("sell"):
          if bot.model_name=="ER-Sigrid m2":
            if not bot["mission"]:
              if bot.chassis.integrity==100:
                if bot.psychocore.stability==100:
                  if bot.bot_combat.level_name=="S":
                    if bot.bot_sex.level_name=="S":
                      if bot.bot_social.level_name=="S":
                        bp_part_test_pass=1
                        for slot in bot.outfit_slots:
                          part=bot.item_on_slot(slot)
                          if part.rate in "FEDCBA":          ## part testing uses NOT logic
                            bp_part_test_pass=0
                            break                            ##  stop testing if a failure is found, will only go on if no failures found
                        if bp_part_test_pass==1:
                          bot_price=bot_price_function(bot)  ## DO NOT OMIT
                          bots.append([bot,bot_price])       ## DO NOT OMIT
    bots=bots[:12]
  if bots:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "bots squirrel_sigrid avatar"            ## Sigrid
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    if len(bots)==1:  ## only 1 bot available
      $bot,bot_price=bots.pop(0)

##      $print "Sigrid bot picked: ",bot.id

      choice("bp_deliver_deal_4a:{}".format(bot.id)) "[bot]"
      "{mark}[bot]{/} is ready for {mark}[ns_teacher_name]{/} to pick up. I'll select it and then check the {mark}ER-Brutus III{/} bot."
      ""
    else:             ## more than 1 bot available
      "I have to select which {mark}ER-Sigrid m2{/} bot I want to use for the business partnership deal and then I'll check the {mark}ER-Brutus III{/} bot."
      "" 
      $bot_n=0
      while bots:
        $bot,bot_price=bots.pop(0)
        $bot_n+=1
        "#[bot_n] - {mark}[bot]{/}"
        choice("bp_deliver_deal_4a:{}".format(bot.id)) "#[bot_n] - [bot]"
    choice("<<<",pos=17) "Cancel"
  else:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests business_partners bp_33"
    center "{image=[action_image]@400x600}"
    $act.set_block("c") 
    "I don't have a {mark}ER-Sigrid m2{/} bot ready to deliver for deal 4, I better get to work!"
    choice("<<<") "Oops!"
  return

label bp_deliver_deal_4a(female_bot):            ## looking for Brutus bot second, parameter is selected Sigrid bot
  $global pair_female_bot
  $female_bot=find_character(female_bot)
  $pair_female_bot=female_bot

##  $print "female bot in pair: ",pair_female_bot
  
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 4 - Select {mark}ER-Brutus III{/} Bot"
  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot and bot.action_allowed("sell"):
          if bot.model_name=="ER-Brutus III":
            if not bot["mission"]:
              if bot.chassis.integrity==100:
                if bot.psychocore.stability==100:
                  if bot.bot_combat.level_name=="S":
                    if bot.bot_sex.level_name=="S":
                      if bot.bot_social.level_name=="S":
                        bp_part_test_pass=1
                        for slot in bot.outfit_slots:
                          part=bot.item_on_slot(slot)
                          if part.rate in "FEDCBA":          ## part testing uses NOT logic
                            bp_part_test_pass=0
                            break                            ##  stop testing if a failure is found, will only go on if no failures found
                        if bp_part_test_pass==1:
                          bot_price=bot_price_function(bot)  ## DO NOT OMIT
                          bots.append([bot,bot_price])       ## DO NOT OMIT
    bots=bots[:12]
  if bots:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "bots squirrel_brute avatar"              ## Brutus
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    if len(bots)==1:  ## only 1 bot available
      $bot,bot_price=bots.pop(0)

##      $print "Brutus bot picked: ",bot.id

      choice("bp_deliver_deal_4b:{}".format(bot.id)) "[bot]"
      "{mark}[bot]{/} is also available to for {mark}[ns_teacher_name]{/} to pick up. I'll select it and then call her."
      ""
    else:             ## more than 1 bot available
      "I have to select which {mark}ER-Brutus III{/} bot I want to use for the business partnership deal and then call {mark}[ns_teacher_name]{/}."
      "" 
      $bot_n=0
      while bots:
        $bot,bot_price=bots.pop(0)
        $bot_n+=1
        "#[bot_n] - {mark}[bot]{/}"
        choice("bp_deliver_deal_4b:{}".format(bot.id)) "#[bot_n] - [bot]"
    choice("<<<",pos=17) "Cancel"
  else:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests business_partners bp_33"
    center "{image=[action_image]@400x600}"
    $act.set_block("c") 
    "I don't have a {mark}ER-Brutus III{/} bot ready to deliver for deal 4, I better get to work!"
    choice("<<<") "Oops!"
  return

label bp_deliver_deal_4b(male_bot):
  $global pair_male_bot
  $male_bot=find_character(male_bot)
  $pair_male_bot=male_bot

##  $global pair_female_bot
##  $print "female bot in pair: ",pair_female_bot
##  $print "male bot in pair: ",pair_male_bot
  
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 4 - Call {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_15"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_16"
  center "{image=[action_image]@400x600}"
  $act.set_block("c") 
  ""
  "You call Simone to tell her the {mark}ER-Sigrid m2{/} bot and the {mark}ER-Brutus III{/} bot are ready and ask her when she wants to come over to get them."
  ""
  ""
  ""
  "{mark}[ns_teacher_name]{/} says that's great but she's busy right now so she'll send a pair of combat bots over to pick them up. She tells you they will be at your shop in a few minutes."
  choice("bp_deliver_deal_4c") "Wait..."
  return
  
label bp_deliver_deal_4c():
  $global pair_female_bot
  $global pair_male_bot
  $global bp_next_deal
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over
  $bot_f=find_character(pair_female_bot)                 ## find the actual female bot
  $bot_m=find_character(pair_male_bot)                   ## find the actual male bot
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 4 - Bot Pickup"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_45"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_46"
  center "{image=[action_image]@400x600}"
  $act.set_block("c") 
  "The combat bots arrive to pick up the {mark}ER-Sigrid m2{/} and {mark}ER-Brutus III{/} bots and they pay you in cash."
  if now.day<=bp_bonus_end:               ## add bonus
    extend " They even brought the {mark}$400,000 bonus{/}, nice!"
    ""
    $bp_actual_payment=3900000            ## journal share
    $mc.money+=2150000
  elif now.day>bp_penalty_start:          ## subtract penalty
    extend " Too bad they had to subtract the {mark}$400,000 penalty{/} for late delivery."
    ""
    $bp_actual_payment=3100000            ## journal share
    $mc.money+=1350000
  else:                                   ## normal payment
    extend " As expected, they gave me the second half of my share of the deal."
    ""
    $bp_actual_payment=3500000            ## journal share
    $mc.money+=1750000
  ""
  ""
  "You bring {mark}[bot_f]{/} and {mark}[bot_m]{/} out front and the four bots leave together. Wow, that was easy!"
  "{size=-16} "
  $temp=2.4*calc_pr_rep_gain("rep_mc_dealer","xl_g")       ## extra large gain * 2.4 for 2x S level bots private sale
  $mc.give_xp("rep_mc_dealer",temp)
  $temp=2.4*calc_pr_rep_gain("rep_mc_trainer","xl_g")      ## extra large gain * 2.4 for 2x S level bots private sale
  $mc.give_xp("rep_mc_trainer",temp)
  ""
  $move_sexbot(bot_f,None)                   ## delete female bot
  $move_sexbot(bot_m,None)                   ## delete male bot
  $bot=None                                  ## didn't use global so maybe unnecessary
  $quests.businesspartners.advance()
  $bp_next_deal=now.day+random.randint(2,5)  ## for testing fix it at 2
  $bp_deal_active=0
  $bp_bonus_end=0
  $bp_penalty_start=0
  $bp_game_over=0 
  choice("<<<") "Done"
  return

## DEAL 5

label deliver_deal_5_test():  ## looking for Bride of Frankie first
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 5 - Select {mark}Bride of Frankie{/} Bot"
  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot:
          if bot.model_name=="Bride of Frankie":
            if not bot["mission"]:
              if bot.chassis.integrity==100:
                if bot.psychocore.stability==100:
                  if bot.bot_combat.level_name=="S":
                    if bot.bot_sex.level_name=="S":
                      if bot.bot_social.level_name=="S":
                        bp_part_test_pass=1
                        for slot in bot.outfit_slots:
                          part=bot.item_on_slot(slot)
                          if part.rate in "FEDCBA":          ## part testing uses NOT logic
                            bp_part_test_pass=0
                            break                            ##  stop testing if a failure is found, will only go on if no failures found
                        if bp_part_test_pass==1:
                          bot_price=bot_price_function(bot)  ## DO NOT OMIT
                          bots.append([bot,bot_price])       ## DO NOT OMIT
    bots=bots[:12]
  if bots:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "bots frankie_bride_bot avatar"           ## Bride of Frankie
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    if len(bots)==1:  ## only 1 bot available
      $bot,bot_price=bots.pop(0)

##      $print "Bride of Frankie bot picked: ",bot.id

      choice("bp_deliver_deal_5a:{}".format(bot.id)) "[bot]"
      "{mark}[bot]{/} is ready for {mark}[ns_teacher_name]{/} to pick up. I'll select it and then check the {mark}Frankie{/} bot."
      ""
    else:             ## more than 1 bot available - THIS CANNOT HAPPEN UNLESS SOMEONE MODS THE GAME, FRANKIE AND BRIDE CANNOT BE SCAVENGED OR BOUGHT
      "I have to select which {mark}Bride of Frankie{/} bot I want to use for the business partnership deal and then check the {mark}Frankie{/} bot."
      "" 
      $bot_n=0
      while bots:
        $bot,bot_price=bots.pop(0)
        $bot_n+=1
        "#[bot_n] - {mark}[bot]{/}"
        choice("bp_deliver_deal_5a:{}".format(bot.id)) "#[bot_n] - [bot]"
    choice("<<<",pos=17) "Cancel"
  else:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "bots frankie_bride_bot avatar"            ## Bride of Frankie
    center "{image=[action_image]@400x600}"
    $act.set_block("c") 
    "The {mark}Bride of Frankie{/} bot is not ready to deliver for deal 5, I better get to work!"
    choice("<<<") "Oops!"
  return

label bp_deliver_deal_5a(female_bot):  ## looking for Frankie second
  $global pair_female_bot
  $female_bot=find_character(female_bot)
  $pair_female_bot=female_bot

##  $print "female bot in pair: ",pair_female_bot
  
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 5 - Select {mark}Frankie{/} Bot"
  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot:
          if bot.model_name=="Frankie":
            if not bot["mission"]:
              if bot.chassis.integrity==100:
                if bot.psychocore.stability==100:
                  if bot.bot_combat.level_name=="S":
                    if bot.bot_sex.level_name=="S":
                      if bot.bot_social.level_name=="S":
                        bp_part_test_pass=1
                        for slot in bot.outfit_slots:
                          part=bot.item_on_slot(slot)
                          if part.rate in "FEDCBA":          ## part testing uses NOT logic
                            bp_part_test_pass=0
                            break                            ##  stop testing if a failure is found, will only go on if no failures found
                        if bp_part_test_pass==1:
                          bot_price=bot_price_function(bot)  ## DO NOT OMIT
                          bots.append([bot,bot_price])       ## DO NOT OMIT
    bots=bots[:12]
  if bots:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "bots frankie_bot avatar"                 ## Frankie
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    if len(bots)==1:  ## only 1 bot available
      $bot,bot_price=bots.pop(0)

##      $print "Frankie bot picked: ",bot.id

      choice("bp_deliver_deal_5b:{}".format(bot.id)) "[bot]"
      "{mark}[bot]{/} is also ready for {mark}[ns_teacher_name]{/} to pick up. I'll select it and then call her."
      ""
    else:             ## more than 1 bot available - THIS CANNOT HAPPEN UNLESS SOMEONE MODS THE GAME, FRANKIE AND BRIDE CANNOT BE SCAVENGED OR BOUGHT
      "I have to select which {mark}Frankie{/} bot I want to use for the business partnership deal. I'll select one and then call {mark}[ns_teacher_name]{/}."
      "" 
      $bot_n=0
      while bots:
        $bot,bot_price=bots.pop(0)
        $bot_n+=1
        "#[bot_n] - {mark}[bot]{/}"
        choice("bp_deliver_deal_5b:{}".format(bot.id)) "#[bot_n] - [bot]"
    choice("<<<",pos=17) "Cancel"
  else:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "bots frankie_bot avatar"                 ## Frankie
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    "The {mark}Frankie{/} bot is not ready to deliver for deal 5, I better get to work!"
    choice("<<<") "Oops!"
  return

label bp_deliver_deal_5b(male_bot):
  $global pair_two_payment
  $global receive_frankie_bride
  $global pair_male_bot
  $male_bot=find_character(male_bot)
  $pair_male_bot=male_bot
  $global pair_female_bot
  $global bp_game_over

##  $print "female bot in pair: ",pair_female_bot
##  $print "male bot in pair: ",pair_male_bot
  
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "BP Deal 5 - Call {mark}[ns_teacher_name]{/}"
## calculate payment but not used until delivery at Raymond's
  if now.day<=bp_bonus_end:               ## add bonus
    $bp_actual_payment=4250000            ## journal entry adjusted deal value
    $pair_two_payment=2375000
  elif now.day>bp_penalty_start:          ## subtract penalty
    $bp_actual_payment=3250000            ## journal entry adjusted deal value
    $pair_two_payment=1375000
  else:                                   ## normal payment
    $bp_actual_payment=3750000            ## journal entry adjusted deal value
    $pair_two_payment=1875000
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_17"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_18"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "When I call {mark}[ns_teacher_name]{/} and tell her the bots are ready she gives me instructions;"
  ""
  if now("Saturday"):
    "{say}Bring them to {mark}Raymond's Bot Boutique{/} next {mark}Saturday night{/} after the normal show. Come well dressed and be on your best behavior. The customer will be there along with all the regulars who are anxious to see the bots they've heard about. When the customer is ready to pay I'll tell him to give the money to you. When everyone sees this they'll be shocked but just smile and enjoy it. Be professional and tell him you're sure he'll be pleased with the bots because we want everyone there to order bots from you.{/}"
  else:
    "{say}Bring them to {mark}Raymond's Bot Boutique{/} on {mark}Saturday night{/} after the normal show. Come well dressed and be on your best behavior. The customer will be there along with all the regulars who are anxious to see the bots they've heard about. When the customer is ready to pay I'll tell him to give the money to you. When everyone sees this they'll be shocked but just smile and enjoy it. Be professional and tell him you're sure he'll be pleased with the bots because we want everyone there to order bots from you.{/}"  
  ""
  $bp_deliver_frankie_bride=now.day+1     ## if you call on Saturday setting this to the next day prevents you from going the same day you call, must be at least the next day 
  $receive_frankie_bride=3                ## set flag to prevent buttons from showing up once committed to delivery NEXT SATURDAY (day check in event handler)
  $bp_game_over=0                         ## reset flag in case of last minute delivery
  $quests.businesspartners.advance()      ## delay phase inserted to change description
  choice("<<<") "Done"
  return

##==========WARNINGS========== 
  
label bonus_warning(i_flag):                        ## Note: no bonus for deal 3 - special bot
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Business Partnership {good}Bonus{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if quests.businesspartners=="bot_1":
    $action_image= "bots squirrel_mylou avatar"     ## Mylou avatar
    center "{image=[action_image]@280x600}"
  elif quests.businesspartners=="bot_2":
    $action_image= "bots squirrel_tanjiro avatar"   ## Tanjiro avatar
    center "{image=[action_image]@280x600}"
  elif quests.businesspartners=="bot_pair_1":
    $action_image= "bots squirrel_sigrid avatar"    ## Sigrid avatar
    center "{image=[action_image]@200x600}"
    ""
    $action_image= "bots squirrel_brute avatar"     ## Brutus avatar
    center "{image=[action_image]@200x600}"
  elif quests.businesspartners=="bot_pair_2":
    $action_image= "bots frankie_bride_bot avatar"  ## Bride of Frankie avatar
    center "{image=[action_image]@200x600}"
    ""
    $action_image= "bots frankie_bot avatar"        ## Frankie avatar
    center "{image=[action_image]@200x600}"
  $act.set_block("c")
  if i_flag==1:  ## tomorrow is last day
    if quests.businesspartners=="bot_1":
      "{good}Tomorrow{/} is the last day that I can receive a {good}bonus{/} for delivering an {mark}AGTY-36{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_2":
      "{good}Tomorrow{/} is the last day that I can receive a {good}bonus{/} for delivering a {mark}Tanjiro SX{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_pair_1":
      "{good}Tomorrow{/} is the last day that I can receive a {good}bonus{/} for delivering an {mark}ER-Sigrid m2{/} bot and an {mark}ER-Brutus III{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_pair_2":
      "{good}Tomorrow{/} is the last day that I can receive a {good}bonus{/} for delivering the pair of special bots to {mark}[ns_teacher_name]{/}."
  else:             ## today is last day
    if quests.businesspartners=="bot_1":
      "{good}Today{/} is the last day that I can receive a {good}bonus{/} for delivering an {mark}AGTY-36{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_2":
      "{good}Today{/} is the last day that I can receive a {good}bonus{/} for delivering a {mark}Tanjiro SX{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_pair_1":
      "{good}Today{/} is the last day that I can receive a {good}bonus{/} for delivering an {mark}ER-Sigrid m2{/} bot and an {mark}ER-Brutus III{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_pair_2":
      "{good}Today{/} is the last day that I can receive a {good}bonus{/} for delivering the pair of special bots to {mark}[ns_teacher_name]{/}."
  choice("<<<") "Done"
  return

label penalty_warning(i_flag):                      ## Note: no penalty for deal 3 - special bot
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Business Partnership {bad}Penalty{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if quests.businesspartners=="bot_1":
    $action_image= "bots squirrel_mylou avatar"     ## Mylou avatar
    center "{image=[action_image]@280x600}"
  elif quests.businesspartners=="bot_2":
    $action_image= "bots squirrel_tanjiro avatar"   ## Tanjiro avatar
    center "{image=[action_image]@280x600}"
  elif quests.businesspartners=="bot_pair_1":
    $action_image= "bots squirrel_sigrid avatar"    ## Sigrid avatar
    center "{image=[action_image]@200x600}"
    ""
    $action_image= "bots squirrel_brute avatar"     ## Brutus avatar
    center "{image=[action_image]@200x600}"
  elif quests.businesspartners=="bot_pair_2":
    $action_image= "bots frankie_bride_bot avatar"  ## Bride of Frankie avatar
    center "{image=[action_image]@200x600}"
    ""
    $action_image= "bots frankie_bot avatar"        ## Frankie avatar
    center "{image=[action_image]@200x600}"
  $act.set_block("c")
  if i_flag==1:                                     ## tomorrow is last day
    if quests.businesspartners=="bot_1":
      "{bad}Tomorrow{/} is the last day that I can avoid a {bad}penalty{/} by delivering an {mark}AGTY-36{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_2":
      "{bad}Tomorrow{/} is the last day that I can avoid a {bad}penalty{/} by delivering a {mark}Tanjiro SX{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_pair_1":
      "{bad}Tomorrow{/} is the last day that I can avoid a {bad}penalty{/} by delivering an {mark}ER-Sigrid m2{/} bot and an {mark}ER-Brutus III{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_pair_2":
      "{bad}Tomorrow{/} is the last day that I can avoid a {bad}penalty{/} by delivering the pair of special bots to {mark}[ns_teacher_name]{/}."
  else:                                             ## today is last day
    if quests.businesspartners=="bot_1":
      "{bad}Today{/} is the last day that I can avoid a {bad}penalty{/} by delivering an {mark}AGTY-36{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_2":
      "{bad}Today{/} is the last day that I can avoid a {bad}penalty{/} by delivering a {mark}Tanjiro SX{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_pair_1":
      "{bad}Today{/} is the last day that I can avoid a {bad}penalty{/} by delivering an {mark}ER-Sigrid m2{/} bot and an {mark}ER-Brutus III{/} bot to {mark}[ns_teacher_name]{/}."
    elif quests.businesspartners=="bot_pair_2":
      "{bad}Today{/} is the last day that I can avoid a {bad}penalty{/} by delivering the pair of special bots to {mark}[ns_teacher_name]{/}."
  choice("<<<") "Done"
  return

label game_over_warning(i_flag):                    ## i_flag: number of days until game over, options are 14, 7, 1, 0
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{bad}Business Partnership Threatened!{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if quests.businesspartners=="bot_1":
    $action_image= "bots squirrel_mylou avatar"     ## Mylou avatar
    center "{image=[action_image]@280x600}"
  elif quests.businesspartners=="bot_2":
    $action_image= "bots squirrel_tanjiro avatar"   ## Tanjiro avatar
    center "{image=[action_image]@280x600}"    
  elif quests.businesspartners=="bot_special":
    $action_image= "bots sucky_robot avatar"        ## Sucky avatar
    center "{image=[action_image]@280x600}"
  elif quests.businesspartners=="bot_pair_1":  
    $action_image= "bots squirrel_sigrid avatar"    ## Sigrid avatar
    center "{image=[action_image]@200x600}"
    ""
    $action_image= "bots squirrel_brute avatar"     ## Brutus avatar
    center "{image=[action_image]@200x600}"
  elif quests.businesspartners=="bot_pair_2":
    $action_image= "bots frankie_bride_bot avatar"  ## Bride of Frankie avatar
    center "{image=[action_image]@200x600}"
    ""
    $action_image= "bots frankie_bot avatar"        ## Frankie avatar
    center "{image=[action_image]@200x600}"
  $act.set_block("c")
  if i_flag==14:                                    ## two weeks until game over, only happens for "bot_pair_1" and "bot_pair_2"
    if quests.businesspartners=="bot_pair_1":
      "If I don't deliver the {mark}ER-Sigrid m2{/} and {mark}ER-Brutus III{/} bots to{mark}[ns_teacher_name]{/} within {bad}two weeks{/} I risk {bad}losing my business partnership{/}."
    elif quests.businesspartners=="bot_pair_2":
      "If I don't deliver the pair of special bots to {mark}[ns_teacher_name]{/} within {bad}two weeks{/} I risk {bad}losing my business partnership{/}."
  elif i_flag==7:                                   ## 1 week until game over, all deals
    if quests.businesspartners=="bot_1":              
      "If I don't deliver the {mark}AGTY-36{/} bot to {mark}[ns_teacher_name]{/} within {bad}one week{/} I risk {bad}losing my business partnership{/}."
    elif quests.businesspartners=="bot_2":
      "If I don't deliver the {mark}Tanjiro SX{/} bot to{mark}[ns_teacher_name]{/} within {bad}one week{/} I risk {bad}losing my business partnership{/}."
    elif quests.businesspartners=="bot_special":
      "If I don't deliver the {mark}special bot{/} bot to{mark}[ns_teacher_name]{/} within {bad}one week{/} I risk {bad}losing my business partnership{/}."
    elif quests.businesspartners=="bot_pair_1":
      "If I don't deliver the {mark}ER-Sigrid m2{/} and {mark}ER-Brutus III{/} bots to{mark}[ns_teacher_name]{/} within {bad}one week{/} I risk {bad}losing my business partnership{/}."
    elif quests.businesspartners=="bot_pair_2":
      "If I don't deliver the pair of special bots to {mark}[ns_teacher_name]{/} within {bad}one week{/} I risk {bad}losing my business partnership{/}."
  elif i_flag==1:                                   ## day after tomorrow is game over, all deals
    if quests.businesspartners=="bot_1":
      "{bad}Tomorrow{/} is the last day that I can avoid {bad}losing my business partnership{/} with {mark}[ns_teacher_name]{/} by delivering an {mark}AGTY-36{/} bot."
    elif quests.businesspartners=="bot_2":
      "{bad}Tomorrow{/} is the last day that I can avoid {bad}losing my business partnership{/} with {mark}[ns_teacher_name]{/} by delivering a {mark}Tanjiro SX{/} bot."
    elif quests.businesspartners=="bot_special":
      "{bad}Tomorrow{/} is the last day that I can avoid {bad}losing my business partnership{/} with {mark}[ns_teacher_name]{/} by delivering the special bot."
    elif quests.businesspartners=="bot_pair_1":
      "{bad}Tomorrow{/} is the last day that I can avoid {bad}losing my business partnership{/} with {mark}[ns_teacher_name]{/} by delivering an {mark}ER-Sigrid m2{/} bot and an {mark}ER-Brutus III{/} bot."
    elif quests.businesspartners=="bot_pair_2":
      "{bad}Tomorrow{/} is the last day that I can avoid {bad}losing my business partnership{/} with {mark}[ns_teacher_name]{/} by delivering the pair of special bots."
  else:                                             ## tomorrow is game over, all deals
    if quests.businesspartners=="bot_1":
      "{bad}Today{/} is the last day that I can avoid {bad}losing my business partnership{/} with {mark}[ns_teacher_name]{/} by delivering an {mark}AGTY-36{/} bot."
    elif quests.businesspartners=="bot_2":
      "{bad}Today{/} is the last day that I can avoid {bad}losing my business partnership{/} with {mark}[ns_teacher_name]{/} by delivering a {mark}Tanjiro SX{/} bot."
    elif quests.businesspartners=="bot_special":
      "{bad}Today{/} is the last day that I can avoid {bad}losing my business partnership{/} with {mark}[ns_teacher_name]{/} by delivering the special bot."
    elif quests.businesspartners=="bot_pair_1":
      "{bad}Today{/} is the last day that I can avoid {bad}losing my business partnership{/} with {mark}[ns_teacher_name]{/} by delivering an {mark}ER-Sigrid m2{/} bot and an {mark}ER-Brutus III{/} bot."
    elif quests.businesspartners=="bot_pair_2":
      "{bad}Today{/} is the last day that I can avoid a {bad}penalty{/} by delivering the pair of special bots to {mark}[ns_teacher_name]{/}."
  choice("<<<") "Done"
  return

label bp_game_over():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{bad}Business Partnership Dissolved!{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_14"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_49"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_50"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")

  "{mark}[ns_teacher_name]{/} calls to tell you that the client is pissed and threatened her. She told them who you are and you'll be blacklisted by all the rich clients in the area and your partnership is over."
  ""
  ""
  ""
  "{mark}[gn_store_owner_name]{/} calls to tell you she heard you didn't deliver Simone's assignment and the client threatened her. She's disgusted and tells you she's moving in with Simone and never wants to see you again."
  ""
  ""
  "You can't believe how badly you screwed everything up and you spend the rest of your life running the same shop in the same neighborhood wishing you could have another chance."
  choice("quest_mobprotection_game_over",hint="{bad}Bad Ending{/}") "Continue"  ## if this doesn't work create a duplicate
  return

##==========WORK ON SUCKY BOT==========

label work_on_sucky():
  $game_bg="home workspace"
  header "Work on {mark}Sucky Bot{/}"
  $global sucky_last_interaction
  if sucky_last_interaction==0 or sucky_last_interaction==6:  ## when entering the screen before taking any actions AND after research
    if sucky_knowledge==0:
      "This is a really old bot, I've never seen anything like it. I need to do some research on the net to figure out how this thing works before I can repair it."
    elif sucky_charger_integrity<75:
      "I know how {mark}Sucky's{/} charger works and I need to fix it before I can restore and train her. I could fix the charger now or I could do more research."
    elif sucky_knowledge==1:  ## charger functional but not enough knowledge to repair Sucky's head and body
      "I've repaired {mark}Sucky's{/} charger enough to use it so I need to do more research to learn how to fix her head and body."
    elif sucky_knowledge==2 and sucky_head_integrity==100 and sucky_body_integrity==100:  ## not enough knowledge to stabilize Sucky's psychocore
      "I've repaired {mark}Sucky's{/} head and body, I need to do more research to learn how to stabilize her primitive psychocore."
    elif sucky_knowledge==2:  ## head and body can be repaired
      "I know how to repair {mark}Sucky's{/} head and body. I can work on her now or I could do more research to learn about her primitive psychocore."
    elif sucky_knowledge==3 and sucky_head_integrity==100 and sucky_body_integrity==100 and sucky_stability==100:  ## not enough knowledge to train Sucky
      "I've repaired {mark}Sucky's{/} head and body and stabilized her psychocore, I need to do more research to learn how to train her." 
    elif sucky_knowledge==3:  ## head and body can be repaired and psychocore can be stabilized
      "I know how to repair {mark}Sucky's{/} hardware and stablize her psychocore. I could work on her or I could do more research to learn about training her."
    elif sucky_knowledge==4:
      "I know how to repair, stabilize, and train {mark}Sucky{/} but I bet there's more I can still learn. Should I do more research or just get to work?"
    elif sucky_knowledge==5:
      "I learned more about repairing {mark}Sucky{/} and I'll make better progress now. Maybe I should do more research into her primitive psychocore."
    elif sucky_knowledge==6:
      "I understand {mark}Sucky's{/} primitive psychocore better now, I'm sure my hacking will be more effective. Should I research training more?"
    elif sucky_knowledge==7:
      "I've got a much better understanding of everything about {mark}Sucky{/} now. I'm not sure there's more to learn, maybe I should just get to work."
    elif sucky_knowledge==8:
      "I'm glad I did more research, there was more to know about repairing {mark}Sucky{/}. I'll bet I can learn more about stabilizing her psyshocore too."
    elif sucky_knowledge==9:
      "I learned more about {mark}Sucky's{/} psychocore and I'll be able to stabilize her faster. I'm sure I could learn more about training her too."
    else:                     ## 10
      "I'm pretty sure I've learned everything I can about repairing, stabilizing, and training {mark}Sucky{/} now."
    "{size=-26} "
    if sucky_last_interaction==6:                     ## last action research AND notifications enabled
      $mc.give_xp("mechanics",random.randint(2,5))
      $mc.give_xp("electronics",random.randint(2,5))
      $mc.give_xp("computers",random.randint(2,5))
    else:                                             ## just entered interaction, no last action to show
      "{size=-8} "
      "{size=-8} "
      "{size=-8} "
    $action_image= "bots sucky_robot avatar"          ## initial entriy shows avatar
  elif sucky_last_interaction==1:                     ## fix charger
    "{mark}Sucky's{/} charger is really primitive and it's weird having to take her head off her body to use it. I'm glad we have capsules for bots now."
    "{size=-26} "
    $mc.give_xp("electronics",random.randint(5,15))
    $mc.give_xp("computers",random.randint(5,15))
    "{size=-8} "
    $tmp_int=random.randint(7,8)
    $action_image= "bots sucky_robot sb_"+str(tmp_int)
  elif sucky_last_interaction==2:  ## fix head  
    "I have to admit that taking {mark}Sucky's{/} head off to work on it makes it easier. It wouldn't make much sense for newer bots with modern skins though."
    "{size=-26} "
    $mc.give_xp("mechanics",random.randint(5,15))
    $mc.give_xp("electronics",random.randint(5,15))
    $mc.give_xp("computers",random.randint(5,15))
    $tmp_int=random.randint(5,6)
    $action_image= "bots sucky_robot sb_"+str(tmp_int)
  elif sucky_last_interaction==3:  ## fix body
    "{mark}Sucky's{/} body is really primitive. Her vagina and ass are always open just like her mouth, her joints make her really ugly, and her surfaces are too hard."
    "{size=-26} "
    $mc.give_xp("mechanics",random.randint(5,15))
    $mc.give_xp("electronics",random.randint(5,15))
    "{size=-8} "
    $tmp_int=random.randint(3,4)
    $action_image= "bots sucky_robot sb_"+str(tmp_int)
  elif sucky_last_interaction==4:  ## stabilizing
    "I'm surprised that {mark}Sucky's{/} psychocore works as well as it does, it's by far the best thing about her. I'm glad my normal tools work with it."
    "{size=-26} "
    $mc.give_xp("computers",random.randint(5,15))
    "{size=-8} "
    "{size=-8} "
    $tmp_int=random.randint(1,2)
    $action_image= "bots sucky_robot sb_"+str(tmp_int)
  else:                            ## must be 5, sex training
    $tmp_int=random.randint(1,5)
    if tmp_int<3:    ## 40% chance of bj image
      "{mark}Sucky's{/} mouth feels surprisingly good inside but it's weird that it's always wide open. I'm not too sure about the handles on the side of her head though."
      "{size=-26} "
      $mc.give_xp("sex",random.randint(5,15))
      "{size=-8} "
      "{size=-8} "
      $tmp_int=random.randint(9,12)
      $action_image= "bots sucky_robot sb_"+str(tmp_int)
    elif tmp_int<5:  ## 40% chance of vaginal sex
      "{mark}Sucky's{/} vagina feels like an E rated vagina and it's weird that it's always wide open. It's kind of hard to keep it up because she's not much to look at."
      "{size=-26} "
      $mc.give_xp("sex",random.randint(5,15))
      "{size=-8} "
      "{size=-8} "
      $tmp_int=random.randint(13,16)
      $action_image= "bots sucky_robot sb_"+str(tmp_int)
    else:            ## 20% chance of anal
      "{mark}Sucky's{/} ass is only a little tighter than her vagina and it's always wide open too. Makes it a little easier to keep it up but it's still nothing special. "
      "{size=-26} "
      $mc.give_xp("sex",random.randint(5,15))
      "{size=-8} "
      "{size=-8} "
      $tmp_int=random.randint(17,18)
      $action_image= "bots sucky_robot sb_"+str(tmp_int)
  ""
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  center "{image=[action_image]@310x600}"
  $act.set_block("c")
  "{size=-16} "
  "Model: {space=210}{mark}Sucky Bot{/}"
  ""
  $tmp_str=str(sucky_charger_integrity)
  while len(tmp_str)<4:
    $tmp_str=" "+tmp_str
  "Charger Integrity: {space=60}{mark}[tmp_str]%%{/}"
  "{size=-20} "
  $tmp_str=str(sucky_head_integrity)
  while len(tmp_str)<4:
    $tmp_str=" "+tmp_str
  "Head Integrity: {space=94}{mark}[tmp_str]%%{/}"
  "{size=-20} "
  $tmp_str=str(sucky_body_integrity)
  while len(tmp_str)<4:
    $tmp_str=" "+tmp_str
  "Body Integrity: {space=93}{mark}[tmp_str]%%{/}"
  ""
  $tmp_str=str(sucky_stability)
  while len(tmp_str)<4:
    $tmp_str=" "+tmp_str
  "Stability: {space=168}{mark}[tmp_str]%%{/}"
  ""
  if sucky_sex_skill<1000:
    $pct=int(sucky_sex_skill/10.0)
    $rating="F"
  elif sucky_sex_skill<2250:
    $pct=int((sucky_sex_skill-1000.0)/12.5)
    $rating="E"
  elif sucky_sex_skill<5000:
    $pct=int((sucky_sex_skill-2250.0)/27.5)
    $rating="D"
  elif sucky_sex_skill<10000:
    $pct=int((sucky_sex_skill-5000.0)/50.0)
    $rating="C"
  elif sucky_sex_skill<22500:
    $pct=int((sucky_sex_skill-10000.0)/125.0)
    $rating="B"
  elif sucky_sex_skill<50000:
    $pct=int((sucky_sex_skill-22500.0)/275.0)
    $rating="A"
  else:
    $pct=int((sucky_sex_skill-50000.0)/500.0)
    $rating="S"
  if sucky_sex_skill!=0:
    "Sex Skill: {space=138}{info}{size=-8}([pct]%%){/}{/} {mark}[rating]{/}"
  else:
    "Sex Skill: {space=188}{info}none{/}"
    
##  "{size=-16} "                                                                 ## TESTING ONLY!!
##  "{size=-8}{info}Last Interaction: [sucky_last_interaction]{/}{/}"             ## TESTING ONLY!!
##  "{size=-8}{info}Sucky skill level: [sucky_knowledge]{/}{/}"                   ## TESTING ONLY!!

## Research  
  if sucky_knowledge<10:                                                        ## 10 is max
    choice("research_sucky",cost=[("energy",1)]) "Research"
##    choice("research_sucky") "Research"                                         ## TESTING ONLY!!
  else:
    choice(None) "Research"
## Training
  if sucky_knowledge>=4 and sucky_head_integrity>=1 and sucky_body_integrity>=1 and sucky_stability>=1 and sucky_sex_skill<99999:  ## level 4=train - charger >=75 because Sucky is not all 0
    choice("train_sucky",cost=[("energy",1)]) "Train"
##    choice("train_sucky") "Train"                                               ## TESTING ONLY!!
  else:
    choice(None) "Train"
## Fix Charger
  if sucky_knowledge>=1 and sucky_charger_integrity<100:                        ## level 1=fix charger
    choice("fix_sucky_charger",cost=[("energy",1)]) "Fix Charger"
##    choice("fix_sucky_charger") "Repair Charger"                                   ## TESTING ONLY!!
  else:
    choice(None) "Repair Charger"
## Fix Head and Body
  if sucky_knowledge>=2 and sucky_charger_integrity>=75:                        ## level 2=fix head and body - charger must be >= 75           
    if sucky_head_integrity<100:
      choice("fix_sucky_head",cost=[("energy",1)]) "Fix Head"
##      choice("fix_sucky_head") "Repair Head"                                       ## TESTING ONLY!!
    else:
      choice(None) "Repair Head"
    if sucky_body_integrity<100:
      choice("fix_sucky_body",cost=[("energy",1)]) "Fix Body"
##      choice("fix_sucky_body") "Repair Body"                                       ## TESTING ONLY!!
    else:
      choice(None) "Repair Body"
  else:
    choice(None) "Repair Head"
    choice(None) "Repair Body"
## Stabilize
  if sucky_knowledge>=3 and sucky_head_integrity>0 and sucky_body_integrity>0 and sucky_stability<100:  ## level 3=stabilize - charger >= 75 because Sucky is not all 0
    choice("stabilize_sucky",cost=[("energy",1)]) "Stabilize"
##    choice("stabilize_sucky") "Stabilize"                                       ## TESTING ONLY!!
  else:
    choice(None) "Stabilize"
  choice("<<<",pos=17) "Done"
  return

label research_sucky():
  $global sucky_knowledge
  $sucky_knowledge+=1
  $global sucky_last_interaction
  $sucky_last_interaction=6                 ## go back to
  return "work_on_sucky"

label train_sucky():
## calculation is arbitray, absolute mazimum outcome is 5199.4, with randomizer max is 7799.1
  $global sucky_knowledge
  $global sucky_head_integrity
  $global sucky_body_integrity
  $global sucky_stability
  $global sucky_sex_skill
  if sucky_knowledge<7:                                    ## benefit: reduced value of MC learning using sq root, multiplier keeps value > 1 
    $value1=(sucky_low*5)**0.5
  elif sucky_knowledge<10:
    $value1=(sucky_med*5)**0.5
  else:
    $value1=(sucky_high*5)**0.5  
  $value2=(mc.sex.level*1.75)**3                           ## main calculation: cubed MC sex skill as most important, multiplier used for "tuning"
  $value3=(sucky_head_integrity*0.01)**2                   ## handicap: sucky's head is important so squared negative effect
  $value4=(sucky_body_integrity*0.01)                      ## handicap: sucky's body is least important, no exponent
  $value5=(sucky_stability*0.01)**3                        ## handicap: sucky's stability is most important so cubed negative effect
  $final_value=value1*value2*value3*value4*value5
  $low_value=int(final_value*0.5)
  $high_value=int(final_value*1.5)
  $randomized_value=random.randint(low_value,high_value)
  $sucky_sex_skill+=randomized_value

##  $print "final value: ",final_value," randomized value: ",randomized_value
  
  $high_value=int(randomized_value/800)
  $low_value=int(randomized_value/267)
  $head_loss=random.randint(high_value,low_value)
  $high_value=int(randomized_value/2000)
  $low_value=int(randomized_value/667)
  $body_loss=random.randint(high_value,low_value)
  $high_value=int(randomized_value/200)
  $low_value=int(randomized_value/66.7)
  $stability_loss=random.randint(high_value,low_value)  
  $sucky_head_integrity-=head_loss
  $sucky_body_integrity-=body_loss
  $sucky_stability-=stability_loss  
  
  if sucky_sex_skill>99999:                 ## don't allow > 99999
    $sucky_sex_skill=99999
  $global sucky_last_interaction
  $sucky_last_interaction=5                 ## show random sex picture
  return "work_on_sucky"

label fix_sucky_charger():
  $global sucky_charger_integrity
  $value=random.randint(21,35)
  $sucky_charger_integrity+=value
  if sucky_charger_integrity>100:           ## don't allow > 99999
    $sucky_charger_integrity=100
  $global sucky_last_interaction
  $sucky_last_interaction=1                 ## show repair charger picture
  return "work_on_sucky"

label fix_sucky_head():
  $global sucky_knowledge
  $global sucky_head_integrity
  if sucky_knowledge<5:
    $value=sucky_low*mc.electronics.level*mc.mechanics.level
  elif sucky_knowledge<8:
    $value=sucky_med*mc.electronics.level*mc.mechanics.level
  else:
    $value=sucky_high*mc.electronics.level*mc.mechanics.level
  $low_value=int(value*0.5)
  $high_value=int(value*1.5)
  $sucky_head_integrity+=random.randint(low_value,high_value)
  if sucky_head_integrity>100:
    $sucky_head_integrity=100
  $global sucky_last_interaction
  $sucky_last_interaction=2                 ## show repair head picture
  return "work_on_sucky"

label fix_sucky_body():
  $global sucky_knowledge
  $global sucky_body_integrity
  if sucky_knowledge<5:
    $value=sucky_low*mc.electronics.level*mc.mechanics.level
  elif sucky_knowledge<8:
    $value=sucky_med*mc.electronics.level*mc.mechanics.level
  else:
    $value=sucky_high*mc.electronics.level*mc.mechanics.level
  $low_value=int(value*0.5)
  $high_value=int(value*1.5)
  $sucky_body_integrity+=random.randint(low_value,high_value)
  if sucky_body_integrity>100:
    $sucky_body_integrity=100
  $global sucky_last_interaction
  $sucky_last_interaction=3                 ## show repair body picture
  return "work_on_sucky"

label stabilize_sucky():
  $global sucky_knowledge
  $global sucky_stability
  if sucky_knowledge<6:
    $value=sucky_low*mc.computers.level*mc.computers.level
  elif sucky_knowledge<9:
    $value=sucky_med*mc.computers.level*mc.computers.level
  else:
    $value=sucky_high*mc.computers.level*mc.computers.level
  $low_value=int(value*0.5)
  $high_value=int(value*1.5)
  $sucky_stability+=random.randint(low_value,high_value)
  if sucky_stability>100:
    $sucky_stability=100  
  $global sucky_last_interaction
  $sucky_last_interaction=4                 ## show Sucky on gurney
  return "work_on_sucky"

##==========DELIVER SPECIAL BOT AT SIMONE'S PLACE==========

label deliver_sucky_bot():
  $game.location="neighborhood"
  $temp_int= random.randint(1,2)
  $game_bg="neighborhood nbg_"+str(temp_int)
  header "Leaving the Shop to Deliver {mark}Sucky Bot{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_51"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_52"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "I have to ride the subway to get to {mark}[ns_teacher_name]'s{/} place so I dressed {mark}Sucky{/} up in a skirt I normally use for techie bots and a surgical mask. No one has seen a bot like this before and I'm not sure they want to!"
  ""
  ""
  ""
  "Even with the 'disguise' people are surprised to see {mark}Sucky{/} and I'm getting a lot of stares. I'm not sure if they are curious or disgusted! Oh well nothing I can do about it."
  "{size=-10} "
  $mc.money-=20
  choice("bpdsb_2") "Continue"
  return
  
label bpdsb_2():
  $game.location="teacher_apartment"
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Arriving at {mark}[ns_teacher_name]'s{/} Place"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_53"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_54"
  center "{image=[action_image]@400x600}"
  $act.set_block("c") 
  "When I get to her place {mark}[ns_teacher_name]{/} greets me at the door; {say}Hi {mark}[mc.name]{/}, glad you found my place.{/} She takes a look at {mark}Sucky{/} and almost starts laughing; {say}That's quite the disguise you have on the bot!{/} I reply; {mcsay}I did get a lot of strange looks along the way.{/}"
  ""
  ""
  "We walk into her living room and there's an Asian man sitting on her couch. I recognize him because he was at {mark}Raymond's{/} when I took {mark}[gn_store_owner_name]{/} there. His wife or mistress was a real bitch."
  choice("bpdsb_3") "Continue"
  return

label bpdsb_3():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Meeting the Client"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_55"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_56"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "{mark}[ns_teacher_name]{/} says; {mark}[mc.name]{/} {say}this is {mark}Kenji{/}, you may remember him from {mark}Raymond's{/}. {mark}Kenji{/} this is {mark}[mc.name]{/}, the best bot engineer and trainer in the area.{/}"
  ""
  ""
  "{size=-20} "
  "He looks familiar to me beyond seeing him at {mark}Raymond's{/}; {mcsay}It's nice to meet you {mark}Kenji{/}, I hope you will be happy with the bot.{/} He smiles and says; {say}Nice to meet you too, let's see what she looks like.{/} I take off her disguise and he examines {mark}Sucky{/}."
  choice("bpdsb_4") "Continue"
  return

label bpdsb_4():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Why Does {mark}Kenji{/} Look Familiar?"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_57"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_58" 
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}Kenji{/} looks at us and says; {say}My grandfather had this bot way back and I'm going to surprise him but I need a 'test drive', where can I take her?{/} {mark}[ns_teacher_name]{/} replies; {say}Please use my office at the top of the stairs.{/} While they are talking I realize why he looks familiar and I'm nervous about it."
##  ""
  "{size=-20} "
  "After he goes upstairs with {mark}Sucky{/} I ask {mark}[ns_teacher_name]{/} about him; {mcsay}This guy looks familiar to me, is he involved with the {mark}Syndidate{/}?{/} She replies; {say}Yes, he's the younger brother of the head of the {mark}Syndicate{/}. He's on great terms with his brother and this could lead to lots more business for us.{/}"
  choice("bpdsb_5") "Continue"
  return

label bpdsb_5():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Explaining My History to {mark}[ns_teacher_name]{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_59"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_60"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "I decide to tell {mark}[ns_teacher_name]{/} about my history; {mcsay}I'm not so sure about that. They already know me and I'm sure they aren't too fond of me. I had to pay them a lot of money because one of their goons framed me for bombing one of their buildings.{/}"
  ""
  "{size=-8} "
  "{mark}[ns_teacher_name]{/} is concerned; {say}That's a horrible story, are you still paying them?{/} I reply; {mcsay}No, I paid the debt off before I had my run in with the mob. Trouble seems to follow me around.{/} {mark}[ns_teacher_name]{/} looks thoughtful; {say}Maybe we can discuss this later?{/}"
  choice("bpdsb_6") "Continue"
  return

label bpdsb_6():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "The '{mark}Test Drive{/}' is Successful"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_61"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_62"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}Kenji{/} returns with a big smile; {say}Wow, I'm impressed! My grandfather will be thrilled to see this bot again. I'm really sorry about the other night at {mark}Raymond's{/}, my wife wasn't nice. We'll make it up to you if we see you there again.{/}"
  ""
  ""
  "Kenji tries to pay {mark}[ns_teacher_name]{/} but she stops him; {say}No, he's the one you need to pay. We're partners and he did all the work on this job.{/} He's surprised but hands me the money, picks up the charger, and then leaves with {mark}Sucky{/}."
  ""
  $mc.money+=1500000
  $temp=1.2*calc_pr_rep_gain("rep_mc_dealer","xl_g")       ## extra large gain * 1.2 for special bot private sale
  $mc.give_xp("rep_mc_dealer",temp)
  $temp=1.2*calc_pr_rep_gain("rep_mc_trainer","xl_g")      ## extra large gain * 1.2 for special bot private sale
  $mc.give_xp("rep_mc_trainer",temp)
  choice("bpdsb_7") "Continue"
  return

label bpdsb_7():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Splitting the Payment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_63"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_64"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "I'm not sure why {mark}[ns_teacher_name]{/} had Kenji pay me; {mcsay}That was nice of you but most of this money is yours, you already paid me the advance.{/} She replies; {say}I know but I want him to know you're just as important as I am.{/}"
  ""
  $mc.money-=1125000
  ""
  "{mark}[ns_teacher_name]{/} changes the subject giving me an unexpected look; {say}Sit down on the couch and make yourself comfortable, I'll be right back.{/}"
  choice("bpdsb_8") "Continue"
  return

label bpdsb_8():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Surprise"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_65"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_66"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "You hope this is a '{mark}let me slip into something more comfortable{/}' moment; {mcsay}Thanks, take your time and I'll just hang out while you're gone. {/}{mark}[ns_teacher_name]'s{/} hips seem to have an extra sway in them as she walks up the stairs. Am I dreaming?"
  ""
  "{size=-8} "
  "A few minutes later I see {mark}[ns_teacher_name]{/} coming down the stairs in an incredibly sexy outfit. She says; {say}I think you need to lose those clothes and sit on my piano bench, we need to find out who's mouth feels better: mine or {mark}Sucky Bot's{/}.{/}"
  choice("bpdsb_9") "Continue"
  return

label bpdsb_9():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Getting Ready for the Competition"
  $action_image= "quests business_partners bp_67"
  "At the foot of the stairs {mark}[ns_teacher_name]{/} gets down on all fours and starts crawling towards me. God she's hot!"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "My cock gets as hard as a rock watching {mark}[ns_teacher_name]{/} open her mouth and lick her lips seductively as she slowly crawls over to me."
  choice("bpdsb_10") "Continue"
  return

label bpdsb_10():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "The Competition Begins"
  $action_image= "quests business_partners bp_68"
  "When {mark}[ns_teacher_name]{/} reaches me she's staring into my eyes as she opens her mouth just inches away from my cock. She's so sexy!"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I gasp in surprise and pleasure as she takes my cock into her mouth and begins licking the head slowly. It's hard not to cum immediately!"
  choice("bpdsb_11") "Continue"
  return

label bpdsb_11():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "The Competition Heats Up"
  $action_image= "quests business_partners bp_69"
  "{mark}[ns_teacher_name]{/} reaches up and grabs the base of my cock as she takes more of it inside her mouth and uses her tongue on the head of my cock."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "It feels so good I can't resist reaching out and putting my hand on the back of her head. It's tempting but I stop myself before pushing her head down."
  choice("bpdsb_12") "Continue"
  return

label bpdsb_12():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "The Competition is Almost Finished"
  $action_image= "quests business_partners bp_70"
  "{mark}[ns_teacher_name]{/} sits down in front of me and starts moving her mouth and her hand up and down on my cock giving me an absolutely amazing blow job!"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I gasp; {mcsay}There's no doubt about it, your mouth feels way better than {mark}Sucky Bot's{/}, this feels so good I'm about to cum!"
  choice("bpdsb_13") "Continue"
  return

label bpdsb_13():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "I Think I'm the Winner!"
  $action_image= "quests business_partners bp_71"
  "I look down as {mark}[ns_teacher_name]{/} sucks even harder while flicking her tongue against the head of my cock. She's going to make me cum in her mouth!"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I cry out as I cum and she moans while taking it into her mouth. When I'm spent she looks up at me; {say}I knew my mouth would feel better than {mark}Sucky Bot's{/}."
  choice("bpdsb_14") "Continue"
  return

label bpdsb_14():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "I'd Like to Return the Favor"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_72"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_73"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "I want to return the favor; {mcsay}That was amazing, I certainly wasn't expecting that. I hope you'll let me return the favor.{/} {mark}[ns_teacher_name]{/} replies; {say}I was hoping you'd say that, let's go upstairs where we can be more comfortable."
  ""
  "{size=-8} "
  "As we're walking towards her bedroom I tell her; {mcsay}This is a little embarrassing to admit but I've fantasized about something like this ever since the day you walked into my shop to tell me about your night school. I can't believe it's happening!"
  choice("bpdsb_15") "Continue"
  return

label bpdsb_15():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_74" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_75"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "When you enter the bedroom {mark}[ns_teacher_name]{/} undresses; {say}I'm hoping you're as good with your tongue as you are with training sexbots!{/} I reply; {mcsay}With inspiration like what you did downstairs I'm certainly going to give it my best."
  ""
  ""
  "{mark}[ns_teacher_name]{/} lies down on the bed and opens her legs; {say}Come over her and put that tongue of yours to work.{/} She looks so inviting that my cock gets hard again; {mcsay}With pleasure!{/} I reply as I hurry over to her bed."
  choice("bpdsb_16") "Continue"
  return

label bpdsb_16():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Returning the Favor"
  $action_image= "quests business_partners bp_76"
  "I do my best to make {mark}[ns_teacher_name]{/} feel good by using my tongue on her clit and a finger in her pussy. Her moans let me know it's appreciated!"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "After a few minutes {mark}[ns_teacher_name]{/} pushes my head away and says; {say}That feels wonderful but my pussy is ready for your cock to fill it up.{/}"
  choice("bpdsb_17") "Continue"
  return

label bpdsb_17():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Better than My Fantasies!"
  $action_image= "quests business_partners bp_77"
  "I slowly push my cock into {mark}[ns_teacher_name]{/} but she says; {say} C'mon big boy, you can do it harder than that!{/} so I push it in all the way and begin thrusting."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "{mark}[ns_teacher_name]{/} cries out; {say}That's it, faster!{/} In a few minutes I cry out and cum inside her which makes her cry out and cum too."
  choice("bpdsb_18") "Continue"
  return

label bpdsb_18():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Relaxing Afterwards"
  $action_image= "quests business_partners bp_78"
  "As we're resting afterwards I say; {mcsay}You're beautiful and the sexiest woman I've ever known, I can't believe you wanted to do this with me.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "{mark}[ns_teacher_name]{/} says; {say}Thank you for the compliment but you need a little more confidence, you're pretty hot too and most women would envy me."
  $global bp_first_sex_teacher
  $bp_first_sex_teacher=1       ## set flag to record first sex with Simone for 'Relationship' status screen
  choice("bpdsb_19") "Continue"
  return

label bpdsb_19():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Time to Leave"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_79" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_80"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "{mark}[ns_teacher_name]{/} says; {say}I hate to say this but I have to kick you out, I have an early appointment tomorrow morning.{/} You are a little disappointed; {mcsay}I understand completely, this was a wonderful night.{/}"
  ""
  ""
  "You go downstairs to find your clothes and get dressed. {mark}[ns_teacher_name]{/} throws on a robe and follows you. You hug each other and say your goodbyes at her door before you leave to head home."
  choice("bpdsb_20") "Continue"
  return

label bpdsb_20():
  $game_bg="home bg"
  header "On My Way Home"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_81" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_82"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "As you're heading home on the subway you think about what just happened. You can't believe you just had sex with {mark}[ns_teacher_name]{/}. You've fantasized about her for a long time and never thought it would actually happen."
  "{size=-16} "
  call mc_update_relation(ns_teacher_name,3,0)             ## add 3 for first time sex with Simone
  $mc.mood.give_xp(randint(50,60))                         ## extra large mood increase
  ""
  "As you walk home from the station you wonder if it will happen again. Then you think about {mark}[gn_store_owner_name]{/}, maybe you shouldn't have done it at all. You push all these thoughts and concerns aside and go inside."
  ""
  $global bp_next_deal
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over  
  $bp_deliver_sucky=0                        ## clear flag after delivering sucky
  $receive_sucky=0                           ## set flag so work on sucky button no longer displayed
  $quests.businesspartners.advance()
  if mc.energy>2:
    $mc.energy=2
  $bp_next_deal=now.day+random.randint(2,5)  ## for testing fix it at 2
  $bp_deal_active=0
  $bp_bonus_end=0
  $bp_penalty_start=0
  $bp_game_over=0
  choice("goto_home") "Continue"  ## I believe this will fix the problem but I'm not sure
  return

##==========DELIVER FRANKIE AND BRIDE AT RAYMOND'S==========

label deliver_frankie_bride_bots():
  $game.location="neighborhood"
  $temp_int= random.randint(1,2)
  $game_bg="neighborhood nbg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_83"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_84"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{size=-14} "
  "I gather up {mark}Frankie{/} and {mark}Bride of Frankie{/} to go to {mark}Raymond's Bot Boutique{/}. As we're leaving I realize that I'm going to miss them, it was a lot of fun sex training a couple of green skin bots with scars!"
  ""
  ""
  "Just like last time, riding the subway with strange bots attracts a lot of stares. At least this time it's curiosity instead of disgust. Frankie and his Bride are doing a good acting job, I'm really happy with their social skills."
  "{size=-10} "
  $mc.money-=20
  $global pair_female_bot
  $global pair_male_bot
  $bot_f=find_character(pair_female_bot)
  $bot_m=find_character(pair_male_bot)
  $move_sexbot(bot_f,None)      ## delete female bot
  $move_sexbot(bot_m,None)        ## delete male bot
  choice("bpdbp2_2") "Continue"
  return

label bpdbp2_2():
  $game.location="rays_boutique"
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_85"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_86"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "When you arrive the door man stops you politely; {say}Good Evening Sir, please wait here for a moment. The host will be here shortly and he'd like to conceal your bots until tonight's event starts."
  ""
  ""
  "A moment later the host arrives; {say}Welcome to {mark}Raymond's{/}, I see you've brought the bots for tonight's event. Please let me take them aside so they can be a surprise, we'll take good care of them. Please go inside and enjoy yourself until the event starts.{/}"
  choice("bpdbp2_3") "Continue"
  return

label bpdbp2_3():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_87"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_88"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "As you enter {mark}Raymond's{/} you see {mark}[ns_teacher_name]{/} seated near the door and you're surprised to see {mark}[gn_store_owner_name]{/} next to her. I've never seen her dressed like this before, she looks great! When they see you entering both of them wave you over."
  ""
  ""
  "You're uneasy trying to decide how to greet the two of them together as you walk over. They both stand and no decision is necessary because {mark}[gn_store_owner_name]{/} steps forward to give you a warm hug and a kiss."
  choice("bpdbp2_4") "Continue"
  return

label bpdbp2_4():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_89"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_90"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  ""
  "{mark}[ns_teacher_name]{/} teases {mark}[gn_store_owner_name]{/}; {say}Alright you've had your turn, it's my turn now,{/} She playfully pushes {mark}[gn_store_owner_name]{/} aside to take her place and I get another warm hug."
  ""
  ""
  ""
  "{mark}[ns_teacher_name]{/} releases me and says; {say}Let's sit down for a few minutes before the night's event gets started.{/} After we sit down I say to {mark}[gn_store_owner_name]{/}; {mcsay}I didn't know you would be here, what a pleasant surprise.{/}"
  choice("bpdbp2_5") "Continue"
  return

label bpdbp2_5():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_91"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_92"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}[gn_store_owner_name]{/} says; {say}I was surprised too when {mark}[ns_teacher_name]{/} invited me. This afternoon she took me shopping and helped me get ready. It was fun but I'm not used to dressing like this, I hope you like it.{/} She looks great; {mcsay}Of course I do, you look fabulous!{/}"
  ""
  ""
  "{mark}[ns_teacher_name]{/} says; {say}I wanted {mark}[gn_store_owner_name]{/} to be here with you so she can share in the payback, they were really mean to her last time. After tonight's event {mark}we'll all go to my place{/} and celebrate our success.{/}"
  choice("bpdbp2_6") "Continue"
  return

label bpdbp2_6():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_93"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_94"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "The host comes over and interrupts us politely; {say}Now that you're all here I think it's time to start tonight's event.{/} {mark}[ns_teacher_name]{/} gets up and goes with him to the center."
  ""
  ""
  "The host speaks first; {say}Welcome to tonight's special event. As you all know, our dear friend {mark}[ns_teacher_name]{/} arranged for a custom pair of bots to be delivered here at {mark}Raymond's{/} and she will make tonight's presentation.{/} There's polite applause as {mark}[ns_teacher_name]{/} takes the microphone."
  choice("bpdbp2_7") "Continue"
  return

label bpdbp2_7():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_95"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_96"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} says: {say}Thank you, I'd like to introduce my partner {mark}[mc.name]{/} and {mark}[gn_store_owner_name]{/}. {/}She motions to us to stand and then faces {mark}Kenji's wife{/}; {say}They were here once but for some reason they left early.{/} After a pause there's polite applause."
  ""
  "{size=-16} "
  "We sit back down and {mark}[ns_teacher_name]{/} says; {say}Now, if you look towards the bar you'll see the custom bots you've all been waiting for.{/} The two bots walk in at the same time and there's a buzz around the room as everyone watches them walk in." 
  choice("bpdbp2_8") "Continue"
  return

label bpdbp2_8():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_97"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_98"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} says; {say}You can all see that these bots look good and carry themselves well but that's not really what's important is it? Should we get a demonstration before {mark}Marcus{/} and {mark}Gloria{/} pay for them? What do you say {mark}Marcus{/}?{/}"
  ""
  "{size=-6} "
  "People around the room encourage {mark}Marcus{/} to say 'Yes'. He doesn't really have a choice but he handles it well; {say}Of course, I need to know what I'm paying for don't I?{/} {mark}Frankie{/} and {mark}Bride of Frankie{/} act as if they like the idea."
  choice("bpdbp2_9") "Continue"
  return
  
label bpdbp2_9():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_99"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_100"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} turns and says; {say}{mark}Frankie{/} and {mark}Bride of Frankie{/}, you both have S level Social, Sex, and Combat skills. Please put on a demo for these people who would like to see all of your skills in action.{/}"
  ""
  ""
  "{size=-12} "
  "{mark}Frankie{/} bows to his partner; {say}My dear, perhaps we could spar briefly and then give them a demonstration of lovemaking they will never forget?{/} With a curtsy {mark}Bride of Frankie{/} says; {say}Darling, I believe that's an excellent idea.{/}"
  choice("bpdbp2_10") "Continue"
  return

label bpdbp2_10():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_101"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_102"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "They undress to {say}'Oohhs and 'Aahhs'{/}, bow formally and politely to each other, and then {mark}Bride of Frankie{/} rushes at {mark}Frankie{/}, ducks down as she reaches him, and flips him over onto his back. I notice that {mark}[gn_store_owner_name]{/} doesn't like the fighting."
  ""
  "{size=-16} "
  "{mark}Frankie{/} gets up and after a brief grapple {mark}Bride of Frankie{/} is trapped briefly in a hold. Frankie lets her up and says; {say}My lady, I believe it's time we followed {mark}[mc.name]'s{/} encouragement to 'make love, not war'.{/} With a sexy look she replies; {say}With pleasure!{/}"
  choice("bpdbp2_11a") "Continue"
  return

label bpdbp2_11a():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"

  $action_image= "quests business_partners bp_103"
  "The two bots embrace each other and what starts out as a chaste kiss rapidly turns into much more. {mark}[gn_store_owner_name]{/} is a little surprised."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "There are gasps of surprise and pleasure from all around the room. Most of the guests are aroused and can't help joining in the action."
  choice("bpdbp2_11b") "Continue"
  return

label bpdbp2_11b():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"

  $action_image= "quests business_partners bp_104"
  "From the embrace {mark}Frankie{/} picks up {mark}Bride of Frankie{/} and she cries out as he sets her down on his cock. Their performance is amazing!"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Everyone gets more aroused as the bots move faster and faster until both have very convincing orgasms. I wonder if anyone watching did too!"
  choice("bpdbp2_12") "Continue"
  return

label bpdbp2_12():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_105"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_106"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} says; {say}I trust everyone remembers that we were watching bots, right? With {mark}[mc.name]'s{/} excellent training it's easy to forget. {mark}Marcus{/} and {mark}Gloria{/}, it's time to come up take ownership of your incredibly well-trained bots.{/}"
  ""
  "{size=-6} "
  "As they both walk towards the stage {mark}[ns_teacher_name]{/} looks your way; {mark}[mc.name]{/} {say}please come up here so {mark}Marcus{/} and {mark}Gloria{/} can complete the transaction.{/} You get up and walk towards the stage thinking this is going to be fun!" 
  choice("bpdbp2_13") "Continue"
  return

label bpdbp2_13():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_107"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_108"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "When you are all at the stage {mark}Marcus{/} looks embarrassed as he hands over a small bag with the money. You smile and say; {mcsay}Thank you sir, it was a pleasure training these fine bots. I hope both of you enjoy them and that they serve you well.{/}"
  ""
  "{size=-16} "
  "The host returns to the stage and says; {say} Excuse me {mark}Marcus{/} but I believe you should ask your bots to get dressed!{/} There's laughter around the room as Marcus directs his bots to get dressed and then to join him and his wife."
  choice("bpdbp2_14") "Continue"
  return

label bpdbp2_14():
  $temp_int=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_int)
  header "Deliver Bots at {mark}Raymond's Bot Boutique{/}"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_109"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_110"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{size=-12} "
  "The host says; {say}Ladies and Gentlemen, that concludes our event however I encourage you all to stay as long as you like. Raymond's will not close until the last of you chooses to leave.{/}"
  ""
  "{size=-6} "
  "{mark}[ns_teacher_name]{/} says; {say}I hope both of you enjoyed that, I know I did. We could stay but I believe we'd enjoy ourselves more at my place.{/} I look at {mark}[gn_store_owner_name]{/} and she nods agreement. I smile at both of them; {mcsay}We agree, let's go!{/}"
  choice("bpdbp2_15") "Continue"
  return

label bpdbp2_15():
  $game.location="teacher_apartment"
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Celebrating at {mark}[ns_teacher_name]'s{/} Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_111"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_112"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "It's a short drive in {mark}[ns_teacher_name]'s{/} car to her place and soon we're entering. She says; {say}Welcome, let me get the champagne that's been chilling, please make yourselves comfortable.{/} {mark}[gn_store_owner_name]{/} and I sit together on the couch."
  ""
  "{size=-10} "
  "A few minutes later {mark}[ns_teacher_name]{/} brings over a tray with three glasses of champagne and proposes a toast; {say}To the first of many sales at {mark}Raymond's{/} that will make us very, very rich.{/} I add; {mcsay}...and to {mark}[ns_teacher_name]{/} who made it all possible.{/}"
  choice("bpdbp2_16") "Continue"
  return

label bpdbp2_16():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Celebrating at {mark}[ns_teacher_name]'s{/} Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_113"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_114"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "We're enjoying our conversation when {mark}[ns_teacher_name]{/} surprises us; {say}Let's take this party upstairs to my hot tub.{/} I'm not sure about this and look at {mark}[gn_store_owner_name]{/}, I expect her to be reluctant but she surprises me by saying enthusiastically; {say}Sounds like fun!{/}"
  ""
  "{size=-22} "
  "{mark}[ns_teacher_name]{/} gets up and says; {say}Follow me and bring your drinks with you, there’s more champagne upstairs.{/} I whisper to {mark}[gn_store_owner_name]{/}; {mcsay}You're OK with this? I'm pretty sure we won't be wearing anything.{/} Again she surprises me; {say}I know, {mark}[ns_teacher_name]{/} told me that this afternoon.{/}"
  choice("bpdbp2_17") "Continue"
  return

label bpdbp2_17():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Celebrating at {mark}[ns_teacher_name]'s{/} Apartment"
  $action_image= "quests business_partners bp_115" 
  "As soon as we enter the room {mark}[ns_teacher_name]{/} starts taking off her clothes; {say}No one needs to be shy here, come on you two.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Soon I'm in a hot tub with two beautiful women who probably don't know that I've had sex with both of them. I hope this doesn't blow up in my face."
  choice("bpdbp2_18") "Continue"
  return

label bpdbp2_18():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)

## 0.16 header change for replay
  $global bp_replay_conversation
  if bp_replay_conversation==1:   ## reached function during replay option before relationship conversation  
    header "Replay of the Hot Tub Conversation"
  else:
    header "Celebrating at {mark}[ns_teacher_name]'s{/} Apartment"
    
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_116"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_117"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "After we settle in {mark}[ns_teacher_name]{/} looks at me and says; {say}I discussed my hot tub idea with {mark}[gn_store_owner_name]{/} this afternoon and I was pretty sure you wouldn't object.{/} I smile at her; {mcsay}Two beautiful women in a hot tub, I don't think any guy would object to that.{/}"
  ""
  "{size=-12} "
  "{mark}[gn_store_owner_name]{/} says; {say}At first I was reluctant when {mark}[ns_teacher_name]{/} suggested it but then we had a long conversation and I learned a few things.{/} She doesn't seem upset but I'm afraid my fears are coming true. I wait nervously for her to continue."
  choice("bpdbp2_19") "Continue"
  return

label bpdbp2_19():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)

## 0.16 header change for replay
  $global bp_replay_conversation
  if bp_replay_conversation==1:   ## reached function during replay option before relationship conversation  
    header "Replay of the Hot Tub Conversation"
  else:
    header "Celebrating at {mark}[ns_teacher_name]'s{/} Apartment"
    
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_118"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_119"
  center "{image=[action_image]@400x600}"
  $act.set_block("c") 
  "When {mark}[gn_store_owner_name]{/} doesn't continue {mark}[ns_teacher_name]{/} steps in; {say}We discussed relationships {mark}[mc.name]{/}. Don't worry you haven't lost your girlfriend and we can all be playmates. I like both of you, you both like me. We're going to see if this works for all of us.{/}"
  ""
  "{size=-12} "
  "I'm confused; {mcsay}I'm not sure what you mean.{/} {mark}[ns_teacher_name]{/} says; {say}It means we all know what's going on, no secrets. I told {mark}[gn_store_owner_name]{/} that I seduced you when you came to my place to deliver a bot but I'm not trying to take you away from her.{/}"
  choice("bpdbp2_20") "Continue"
  return

label bpdbp2_20():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)

## 0.16 header change for replay
  $global bp_replay_conversation
  if bp_replay_conversation==1:   ## reached function during replay option before relationship conversation  
    header "Replay of the Hot Tub Conversation"
  else:
    header "Celebrating at {mark}[ns_teacher_name]'s{/} Apartment"

  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_120"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_121"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "I look over at {mark}[gn_store_owner_name]{/} and I'm not sure what she's thinking. I don't want to hurt her; {mcsay}I'm sorry {mark}[gn_store_owner_name]{/} I shouldn't have done that, you have a right to be mad.{/} She looks at me and smiles; {say}At first I was mad {mark}[mc.name]{/} but I'm not mad now.{/}"
  ""
  "{size=-18} "
  "Now I'm really confused. {mark}[ns_teacher_name]{/} says; {say}This afternoon {mark}[gn_store_owner_name]{/} and I talked about this. I said that there's no need for jealousy, we can all enjoy each other's company in pairs or all three together. We'll be honest with each other and see where things go.{/}"
  choice("bpdbp2_21") "Continue"
  return

label bpdbp2_21():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)

## 0.16 header change for replay
  $global bp_replay_conversation
  if bp_replay_conversation==1:   ## reached function during replay option before relationship conversation  
    header "Replay of the Hot Tub Conversation"
  else:
    header "Celebrating at {mark}[ns_teacher_name]'s{/} Apartment"
    
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_122"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_123"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "I want to make sure that {mark}[gn_store_owner_name]'s{/} really comfortable with this; {mcsay}Wow, this is quite a surprise. {mark}[gn_store_owner_name]{/}, are you really OK with all of this or are you just going along?{/} She raises her glass and smiles at me; {say}I'm really OK and I want to give this a try.{/}" 
  ""
  "{size=-22} "
  "{mark}[ns_teacher_name]{/} says; {say}As much as I'd like to seduce both of you right here in this hot tub perhaps it's best if we don't go there tonight. I think the two of you need a chance to talk about this privately. We also have the business partnership to think about and I want it to continue.{/}"

## 0.16 last function in reply needs the correct button
  if bp_replay_conversation==1:   ## last function in replay, need alternate button
    $bp_replay_conversation=0     ## reset flag just in case (should not matter)
    choice("relationship_conversation_2") "End Replay"
  else:
    choice("bpdbp2_22") "Continue"
  return

label bpdbp2_22():
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "Celebrating at {mark}[ns_teacher_name]'s{/} Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_124"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_125"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} says; {say}Come on you two, we need a group hug. I like both of you a lot and I hope you decide to give this crazy idea a try.{/} We wrap our arms around each for a long, silent moment before getting out of the hot tub and getting dressed."
  ""
  "{size=-24} "
  if pair_two_payment==1875000:   ## full payment amount
    "When we get downstairs {mark}[ns_teacher_name]{/} says; {say}Before you leave take your share of the money from the bag. I'll have one of my combat bots drive you back to {mark}[gn_store_owner_name]'s{/} apartment. The subway is a bad place to be when it's this late.{/} {mark}[gn_store_owner_name]{/} and I thank her and we're both pretty quiet on the ride to her apartment."
  elif pair_two_payment>1875000:  ## bonus of 500000 added 
    "When we get downstairs {mark}[ns_teacher_name]{/} says; {say}Before you leave take your share of the money {good}plus your $500,000 bonus{/} from the bag. I'll have one of my combat bots drive you back to {mark}[gn_store_owner_name]'s{/} apartment. The subway is a bad place to be when it's this late.{/} {mark}[gn_store_owner_name]{/} and I thank her and we're both pretty quiet on the ride to her apartment."
  else:                           ## penalty of 500000 subtracted
    "When we get downstairs {mark}[ns_teacher_name]{/} says; {say}Before you leave take your share of the money {bad}minus your $500,000 penalty{/} from the bag. I'll have one of my combat bots drive you back to {mark}[gn_store_owner_name]'s{/} apartment. The subway is a bad place to be when it's this late.{/} {mark}[gn_store_owner_name]{/} and I thank her and we're both pretty quiet on the ride to her apartment."
  "{size=-16} "
  
  $mc.money+=pair_two_payment
  $temp=4.0*calc_pr_rep_gain("rep_mc_dealer","xl_g")       ## extra large gain * 4.0 for 2x special A bots public sale
  $mc.give_xp("rep_mc_dealer",temp)
  $temp=4.0*calc_pr_rep_gain("rep_mc_trainer","xl_g")      ## extra large gain * 4.0 for 2x special A bots public sale
  $mc.give_xp("rep_mc_trainer",temp)
  $temp=4.0*calc_pr_rep_gain("rep_mc_fighter","xl_g")      ## extra large gain * 4.0 for 2x special A bots public sale
  $mc.give_xp("rep_mc_fighter",temp)
  $temp=4.0*calc_pr_rep_gain("rep_mc_sexmachine","xl_g")   ## extra large gain * 4.0 for 2x special A bots public sale
  $mc.give_xp("rep_mc_sexmachine",temp)
  choice("bpdbp2_23") "Continue"
  return

label bpdbp2_23():
  $game.location="store_owner_apartment"
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests business_partners bp_126"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_127"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "It's late when we arrive at {mark}[gn_store_owner_name]'s{/}; {mcsay}I think we should get some sleep and discuss this tomorrow, is that alright?{/} {mark}[gn_store_owner_name]{/} agrees; {say}That's a good idea, why don't you come over tomorrow night.{/} I reply; {mcsay}Good idea, we both have businesses to run.{/}"
  ""
  "{size=-18} "
  "When we're in bed before going to sleep I say; {mcsay}Tomorrow night we'll figure out what we want to do. You're important to me and I don't want to do anything to mess that up.{/} {mark}[gn_store_owner_name]{/} smiles; {say}That's nice to hear and I feel the same way.{/}"
  "{size=-10} "
  $global bp_night_conversation                  ## flag for conversation to happen next night - SET HERE BUT USED IN NEXT VERSION
  $global bp_next_deal
  $global bp_deal_active
  $global bp_bonus_end
  $global bp_penalty_start
  $global bp_game_over
  $global pair_two_payment
  $global bp_deliver_frankie_bride
  $global receive_frankie_bride
  $quests.businesspartners.advance()             ## the wait phase after the 5th delivery is the end of 0.14, there are no more deals until a future version
##  $bp_next_deal=now.day+2                      ## 0.14 NO NEXT DEAL, THIS MAY BE USED IN 0.16
##  next 2 lines are for 0.15.1 only:
  "{size=-10} "
  "{good}(The next assignment in the business partnership will be in a future version.){/}"
  $bp_night_conversation=1                       ## flag for conversation to happen next night - SET HERE BUT USED IN FUTURE VERSION
  $bp_next_deal=0                                ## setting to 0 makes this quest idle
  $bp_deal_active=0
  $bp_bonus_end=0
  $bp_penalty_start=0
  $bp_game_over=0
  $bp_deliver_frankie_bride=0
  $receive_frankie_bride=0                       ## reset after delivering bots
  choice("back_at_the_shop_bp_version") "Sleep"
  return

label back_at_the_shop_bp_version():
  $game_bg="workshop bg_on_date"
  header "{info}At the Shop Last Night{/}"
  "{mark} Last night while you were at {mark}Raymond's Bot Boutique{/} and {mark}[ns_teacher_name]'s{/} place."
  ""
  call role_mission_manager_schedule
  choice("sleep_after_date_bp_version") "Continue"
  return

label sleep_after_date_bp_version():
  $global mc_so_value
## THIS IS A DIFFERENt FROM THE NORMAL SLEEP WHERE THE TIME ADVANCE IS AFTER FITNESS, HOUSEKEEPER, CAPSULES, AND ROLL FLAGS
  $now.advance()             ## advance time so you get up in the morning
  $game.location="store_owner_apartment"
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests business_partners bp_128"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests business_partners bp_129"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "When I wake up {mark}[gn_store_owner_name]{/} is already awake; {say}Good morning, sleepy head!{/} I'm still sleepy; {mcsay}Good morning, you're up early.{/} She gets out of bed; {say}It's not that early dummy, you need to get going. Like you said, we have businesses to run!{/}"
  "{size=-8} "
  "I get dressed thinking I'll look strange dressed like this walking home. {mark}[gn_store_owner_name]{/} throws on a robe and at the door I give her a kiss; {mcsay}Last night was a little strange but I enjoyed it.{/} She smiles; {say}Me too.{/}"
  "{size=-8}"
  "While walking home I think about last night's discussion in the hot tub. Can this work? I'll think about it during the day and we'll talk about it tonight at {mark}[gn_store_owner_name]'s{/}."
  choice("sleep_after_date2_bp_version") "Continue"
  return

label sleep_after_date2_bp_version():
  $game.location="home"            ## follow up activities shown from home
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Home"
## DO THE EXACT SAME THINGS THAT HAPPEN WHEN THE FINAL 'Sleep' BUTTON IS PRESSED NORMALLY AT HOME EXCEPT ADVANCE TIME WHICH WAS ALREADY DONE
  call fwb_fitness_update          ## modified version from home workout (in FWB file)
  $housekeeper_call_from=0         ##  INDICATES CALLED FROM "SLEEP" - a kluge!!
  call role_housekeeper_clean
  call capsule_stability_increase
  call clear_role_delay_flags
  choice("goto_home") "Continue"
  return