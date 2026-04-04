##==== VARIABLES===========

init python:
  fwb_day="Monday"            ## payment day for Ruthie's rent
  fwb_amount=7500             ## full payment for Ruthie's rent
  fwb_delay_days=0            ## countdown used to space out events
  fwb_date_available=0        ## flag set to 1 when event 5 ends night has button for "Date Ruthie", at MC's until Ruthie new apartnemt
                              ## also: reset to 0 when paying for her new apartment (end event 6), no dates allowed temporarily
                              ## also" reset to 1 when you spend the night at her new apartment (end event 8), dates allowed again
  fwb_show_upgrade_message=0  ## flag for seeing the long version when you first think about upgrading Ruthie's apartment
  fwb_pay_rent=0              ## flag set when you start paying Ruthie's rent in event 7
  fwb_paid_today=False        ## flag set to 'True' when you pay the rent to update the left side status screen
  fwb_skip_first_week=0       ## flag set after skipping the first weeks rent paid in advance
  fwb_upgrade_done=0          ## flag set to 1 after you go to Ruthie's new apartment in event 8, dates now 75% at her place
  fwb_next_date=1             ## flag based upon rent payments: 1(full)=85:15 yes, 0(half)=65:35 yes, -1(none)=100% no
  fwb_already_asked=0         ## flag set to day number when you ask Ruthie for a date
  fwb_can_start_bp=0          ## flag set after date with Ruthie at bar when you decide to enter partnership with Simone
  fwb_first_new_clothes=1     ## clear flag after use, first time in new clothes has unique text on date
  fwb_postponed=0             ## flag incremented each time a "postpone" or "not now" button is available
                              ## each situation has a threshold either 1 or 3 depending upon how many times a person can delay an action_image
                              ## each time an event starts the flag is reset to 0
                              ## purpose: allow delays for critical situations but eventually force progress
  fwb_buy_lunch=0             ## flag set when you choose not to buy lunch to force you to buy next time
  fwb_rays_date=0             ## flag set when postponing date at rays to change text second time through
  fwb_bar_after_rays=0        ## flag set when postponing meeting Ruthie at the bar after Simone's visit
  fwb_upgrade_decision=0      ## count down so you think about upgrading Ruthie's apartment every 3 days
  fwb_first_sex=0             ## flag set to 1 after sex in event 5 so the description of 'flirting' changes
  
## 0.15.n re-wrote relationship deterioration, next 2 variables no longer used
##  fwb_mc_so_decrement=0       ## flag set to 1 when you haven't dated Ruthie for 3 days, next morning call function to do it and clear flag 
##  fwb_last_date=0             ## counter of days with no date with Ruthie, if 4 or more decrease relationship by 1

##  THE FOLLOWING VARIABLES ARE FLAGS THAT WILL BE SET DURING THE 'Business Partners' QUEST ONCE IT'S IN THE GAME
  fwb_mc_new_clothes=0        ## flag set when MC dresses up for dates with Ruthie, Simone advises when you accept 'Business Partners'
  fwb_anal_ok=0               ## flag set when Ruthie will do anal, some time mention that Simone told her you like it but not immediately
  fwb_first_anal=0            ## flag set after first anal with Ruthie for alternate text
  fwb_deactivate_rays=0       ## flag to be used in 0.15 that will deactivate Raymond's Bot Boutique visits after the bad date with Ruthie, reset in Business Partners when MC gets a suit
  fwb_mc_old_clothes=0        ## single use flag: for first night in Ruthie's new apartment you always wear your old clothes and must put them on in the morning
## 0.15.n add counter to limit sex on dates
  fwb_sex_count=0            ## limit is 3: increment in each function you have sex, when the value reaches 3 grey out the buttons        

##=========Define Quest and Phases============

  class Quest_fwbenefits(Quest):
    name="Friends With Benefits(SL)"

    class phase_1_fwbenefits1:
      description="""
        I really like {mark}[gn_store_owner_name]{/}, I should ask her on a date. I'll impress her by taking her to {mark}Raymond's Bot Boutique{/}.

        """

    class phase_2_fwbenefits2:
      description="""
        I'm glad {mark}[gn_store_owner_name]{/} will go to {mark}Raymond's Bot Boutique{/} with me. I'm sure we'll have a good time.

        """

    class phase_3_fwbenefits3:
      description="""
        The date with {mark}[gn_store_owner_name]{/} at {mark}Ray's Bot Boutique{/} was terrible, we don't fit in with the rich people who go there.
        It was nice to see {mark}[ns_teacher_name]{/} though!

        """

    class phase_4_fwbenefits4:
      description="""
        I'm not sure about {mark}[ns_teacher_name]'s{/} partnership offer, since {mark}[gn_store_owner_name]{/} met her maybe she can help me decide.
        I should ask {mark}[gn_store_owner_name]{/} for a date at the neighborhood bar, I think we'll have more fun there than going downtown again.

        """

    class phase_5_fwbenefits5:
      description="""
        I'm glad {mark}[gn_store_owner_name]{/} agreed to meet me at the neighborhood bar, I'm sure we'll have a better time there than we did at {mark}Raymond's Bot Boutique{/}.
        I wonder what she thinks about {mark}[ns_teacher_name]{/}.

        """

    class phase_6_fwbenefits6:
      description="""
        Finally, after all the sex I've had with bots I'm no longer a virgin with real people!
        I had a great time with {mark}[gn_store_owner_name]{/} but her place is horrible. She needs a better place, can I afford to help her out?

        """

    class phase_7_fwbenefits7:
      description="""
        I'm glad that {mark}[gn_store_owner_name]{/} is excited about her new apartment. I'll give her a few days to move in and get settled.

        """

    class phase_8_fwbenefits8:
      description="""
        I'm looking forward to seeing {mark}[gn_store_owner_name]'s{/} new apartment and breaking in her new bed!

        """

    class phase_1000_fwbenefits_done:
      description="It's great that {mark}[gn_store_owner_name]{/} and I became {mark}Friends with Benefits{/}, I wonder how far this relationship will go?"
      
    class phase_2000_fwbenefits_failed:                             ## there is no possibility of failure for this quest, it will remain open indefinately until you complete it
            description="Who likes her anyway!"

##========= EVENT HANDLER NEEDED IN THIS QUEST - EVENT HANDLER - PYTHON HIDE=========

init python hide:
  @event_handler("time_advanced")
  def fw_benefits_event():
    global fwb_delay_days                                        ## counter used to skip days when needed
    global fwb_upgrade_done                                      ## flag set when Ruthie moves into new apartment
    global fwb_pay_rent                                          ## flag set after skipping the first week's rent
    global fwb_upgrade_decision                                  ## counter to consider upgrading Ruthie's apartment every 4 days
    global fwb_date_available                                    ## flag set when you can date Ruthie 

## 0.15.n re-wrote relationship deterioration, next 2 variables no longer used
##    global fwb_last_date                                         ## counter of days since last date
##    global fwb_mc_so_decrement                                   ## flag to 'queue' a relationship status decrement for 3 days no date

    if not quests.fwbenefits.started:                            ## isolate 'not started' so 'elif' clauses work
      if not quests.fwbenefits.finished:                         ## if finished don't start again
        if now("afternoon") and quests.goodneighbor.finished:    ## friends with benefits starts after good neighbor is finished
          queue_event("quest_fwbenefits_event0")                 ## visit Ruthie at Patrol HQ, take her to Earl's Diner, walk her home
    elif now("evening") and quests.fwbenefits=="fwbenefits1":
      
      if fwb_delay_days<=0:                                      ## delay days set to 1 in event0
        queue_event("quest_fwbenefits_event1")                   ## Option: Visit Ruthie in store and invite to date at Ray's Boutique tomorrow
      else:
        fwb_delay_days=fwb_delay_days-1
    elif now("evening") and quests.fwbenefits=="fwbenefits2":    ## Option: Date at Ray's Boutique or postpone
      queue_event("quest_fwbenefits_event2")
    elif now("morning") and quests.fwbenefits=="fwbenefits3":    ## No Option: Simone visits shop to propose partnership, you say you'll think about it
      queue_event("quest_fwbenefits_event3")
    elif now("afternoon") and quests.fwbenefits=="fwbenefits4":  ## Option: Visit Ruthie at store and ask to meet at local bar tonight
      queue_event("quest_fwbenefits_event4")
    elif now("night") and quests.fwbenefits=="fwbenefits5":      ## Option: Meet at bar or postpone
      queue_event("quest_fwbenefits_event5")
    elif now("afternoon") and quests.fwbenefits=="fwbenefits6":  ## Option: Upgrade Ruthie's apartment
      if fwb_upgrade_decision==0:                                ## count down expired
        fwb_upgrade_decision=3                                   ## reset counter
        queue_event("quest_fwbenefits_event6")
      else:
        fwb_upgrade_decision-=1                                  ## decrement counter

## 0.15 story added 5 lines to escalate paying for Ruthie's apartment, delayed 2 days from last "No" decision
    elif now("evening") and quests.fwbenefits=="fwbenefits6":    ## escalation for upgrading apartment
      global bp_force_store_owner_rent
      if bp_force_store_owner_rent>0 and fwb_upgrade_decision==1:  ## escalation started and 2 days before next decision
        queue_event("fwb_escalate_apartment_rent")
## end of 0.15 addition

    elif now("afternoon") and quests.fwbenefits=="fwbenefits7":  ## After moving in Ruthie invites you to her new apartment
      if fwb_delay_days<=0:
        queue_event("quest_fwbenefits_event7")
      else:
        fwb_delay_days=fwb_delay_days-1
    elif now("night") and quests.fwbenefits=="fwbenefits8":      ## You go to Ruthie's new apartment and sleep over, quest ends
      queue_event("quest_fwbenefits_event8")
    if now("monday","morning") and fwb_upgrade_done:             ## weekly rent starts in event 7 and never ends
      queue_event("fwb_rent_ruthie")                             ## first week paid in advance handled in called function

## 0.15.n no longer needed - re-wrote relationship loss and removed code from 0.11.3
##        counter variables changed, incrementing them and actual relationship loss in a
##        nightly call to 'update_relationshp_counters' function in file 'mc_relationships.rpy' in '0030-game-functions'

    return

##========= EVENT FUNCTIONS==========

##===== Button for Booty Call Date with Ruthie =====

label friends_with_benefits_button:
  $global fwb_date_available
  $global fwb_already_asked
  $global fwb_can_start_bp
  
## 0.15.n obsolete variable
##  $global fwb_last_date

  if now("night") and fwb_date_available==1:
    if fwb_already_asked!=now.day and mc.money>=250 and mc.energy>=3:  ## 'already asked' flag set to today when you press the button (in called function)
      choice("fwb_ask_ruthie_date",hint="$250,3AP,Time",pos=16) "Date [gn_store_owner_name]"
    elif fwb_already_asked==now.day:
      choice(None,hint="{color=#666666}already asked{/}",pos=16) "Date [gn_store_owner_name]"
    elif mc.money<250 or mc.energy<3:
      choice(None,hint="{color=#666666}$250,3AP,Time{/}",pos=16) "Date [gn_store_owner_name]"
  elif now("morning") and fwb_can_start_bp==1:                                                 ## call Simone about partnership
    $global bp_who_called
    $bp_who_called=0                                                                           ## set flag to MC calling Simone
    choice("business_partners_start",hint="(partnership)",pos=15) "Call [ns_teacher_name]"     ## 0.14.n business partners quest created
  return

##===== Finish night after Booty Call Dates with Ruthie =====

## 0.16 deleted function 'back_at_the_shop' - in 0.15.0 it was incorporated into 'sleep_after_date' and is no longer used
label sleep_after_date(date_location):
  $global mc_so_value
  $global fwb_mc_new_clothes   ## need to read flag for MC's clothes when leaving
  $global fwb_mc_old_clothes   ## need to know if this is the morning after "first night in Ruthie's apartment
  if date_location=="home":  ## Ruthie stayed at your place, Ruthie needs to leave
    $game.location="home"
    $game_bg="home bg"
    $game_bgm="home bgm"
    header "Home"
  else:
    $game.location="store_owner_apartment"
    $game_bg="apartment bg_apartment"
    header "[gn_store_owner_name]'s Apartment"    
  
## THIS IS A DIFFERENCE FROM THE NORMAL SLEEP WHERE THE TIME ADVANCE IS AFTER FITNESS, HOUSEKEEPER, CAPSULES, AND ROLL FLAGS
  "Last night while you were enjoying your date:"
  "{size=-22} "
  call role_mission_manager_schedule
  "{size=-16} "
  $now.advance()             ## advance time so you get up in the morning
  "This morning:"
  "{size=-22} "
  if date_location=="home":  ## Ruthie stayed at your place, Ruthie needs to leave
## 0.15.n 4 lines no longer needed, merged 2 functions so already done
##    $game.location="home"  ## 
##    $game_bg="home bg"
##    $game_bgm="home bgm"
##    header "Home"
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $action_image= "quests friends_with_benefits fwb_122"
    center "{image=[action_image]@345x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_123"
    center "{image=[action_image]@345x600}"
    ##  TEXT
    $act.set_block("c")
    "When we wake up {mark}[gn_store_owner_name]{/} is the first one out of bed and says; {say}Sorry, I have to get going to run the store.{/} While she gets dressed I get up and say; {mcsay}Let me find some pants so I can walk you to the door "
    ""
    "{size=-16} "
    "At the door {mark}[gn_store_owner_name]{/} and I kiss passionately before she leaves. Afterwards I enjoy thinking about last night for a few minutes."
    "{size=-22} "
    if quests.fwbenefits.finished or mc_so_value<45:   ## if quest done OR below midpoint of 'Flirting'
      call mc_update_relation(gn_store_owner_name,3,0)
    $mc.mood.give_xp(randint(6,12))                 ## small mood increase
  else:                            ## MC stayed at Ruthie's place, need to walk home
## 0.15.n 5 lines no longer needed, merged 2 functions so already done 
##    $global fwb_mc_new_clothes   ## need to read flag for MC's clothes when leaving
##    $global fwb_mc_old_clothes   ## need to know if this is the morning after "first night in Ruthie's apartment
##    $game.location="store_owner_apartment"
##    $game_bg="apartment bg_apartment"
##    header "[gn_store_owner_name]'s Apartment"
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $action_image= "quests friends_with_benefits fwb_124"
    center "{image=[action_image]@345x600}"
    ""
    if fwb_mc_new_clothes==0:                                  ## still using MC's old clothes
      $action_image= "quests friends_with_benefits fwb_125"    ## old clothing picture
    else:                                                      ## using MC's new clothes
      if fwb_mc_old_clothes==1:                                ## flag set for "first night at Ruthies new apartment" 
        $fwb_mc_old_clothes=0                                  ## clear flag for "first night at Ruthies new apartment"
        $action_image= "quests friends_with_benefits fwb_125"  ## old clothing picture
      else:                                                    ## flag NOT set for "first night at Ruthies new apartment"
        $action_image= "quests friends_with_benefits fwb_211"  ## new clothing picture
    center "{image=[action_image]@345x600}"
    ##  TEXT - THE SAME IN BOTH OLD AND NEW CLOTHES
    $act.set_block("c")
    "In the morning we wake up together and I get out of bed first saying; {mcsay}I hate to leave but I have to get back to the shop.{/} As she throws on her robe {mark}[gn_store_owner_name]{/} replies; {say}I need to get to my store as well.{/}"
    ""
    "{size=-16} "
    "At the door we share a passionate kiss before I leave for the shop. While I'm walking home I enjoy thinking about last night."
    "{size=-22} "
    if quests.fwbenefits.finished or mc_so_value<45:   ## if quest done OR below midpoint of 'Flirting'
      call mc_update_relation(gn_store_owner_name,3,0)
    $mc.mood.give_xp(randint(6,12))                  ## small mood increase
  choice("sleep_after_date2") "Continue"
  return

## This screen is similar to the second 'Sleep' screen (home_sleep_finish) where the rest of the functions are called
label sleep_after_date2:
  $game.location="home"            ## follow up activities shown from home
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Home"
## DO THE EXACT SAME THINGS THAT HAPPEN WHEN THE FINAL 'Sleep' BUTTON IS PRESSED NORMALLY AT HOME EXCEPT ADVANCE TIME WHICH WAS ALREADY DONE
  call fwb_fitness_update          ## modified version from home workout
  $housekeeper_call_from=0         ##  INDICATES CALLED FROM "SLEEP" - a kluge!!
  call role_housekeeper_clean
  call capsule_stability_increase

## 0.15.n relationship decrease included in following function in 'mc_relationships.rpy' in '0030-game-functions'
  call update_relationship_counters  
  call clear_role_delay_flags

## 0.15.n moved resetting raymond's bot boutique flag here
  $rays_already_visited=0                              ## reset visit flag for the next day
  $rays_online_bot_list=0                              ## reset flag so new bot list is generated when online store opened
  
  choice("goto_home") "Continue"
  return

##===== Fitness Update Substitute - replace pictures and text

label fwb_fitness_update:                              ## Daily loss of strength and stamina, calculate fitness level
## 0.15.n moved next 2 lines to 'sleep_after_date2 in this file
##  $rays_already_visited=0                              ## reset visit flag so you can only go once an evening
##  $rays_online_bot_list=0                              ## reset flag so new bot list is generated when online store opened
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if hw_workouts_today>=1:                             ## one or more workouts yesterday
    $action_image="quests friends_with_benefits fwb_1"
  else:                                                ## no workouts yesterday
    $action_image="quests friends_with_benefits fwb_2"
  ""
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  if hw_workouts_today>=1:         ##  you did at least one workout today
    $hw_last_workout=0             ##  reset the last workout counter
    "I feel great this morning since I worked out yesterday!"
  elif hw_first_workout!=0:      ##  you did not work out today (and have worked out at least once)
    $hw_last_workout+=1          ##  increment the 'days since last workout' counter
    "I feel sluggish this morning, maybe it's because I didn't work out yesterday."
    if mc.strength.level_name=="F":
      $hw_skill_impact=hw_level_f_base_loss
    elif mc.strength.level_name=="E":
      $hw_skill_impact=hw_level_e_base_loss
    elif mc.strength.level_name=="D":
      $hw_skill_impact=hw_level_d_base_loss
    elif mc.strength.level_name=="C":
      $hw_skill_impact=hw_level_c_base_loss
    elif mc.strength.level_name=="B":
      $hw_skill_impact=hw_level_b_base_loss
    elif mc.strength.level_name=="A":
      $hw_skill_impact=hw_level_a_base_loss
    elif mc.strength.level_name=="S":
      $hw_skill_impact=hw_level_s_base_loss
    $hw_skill_value=round(hw_skill_impact*hw_last_workout**hw_fudgefactor_loss,2)
    $hw_min_value=hw_skill_value*0.85
    $hw_max_value=hw_skill_value*1.15
    $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
    if mc.strength.level_name!="F" or mc.strength.xp!=0:
      $mc.give_xp("strength",hw_entry_value)         ##  real version after testing
    if mc.stamina.level_name=="F":
      $hw_skill_impact=hw_level_f_base_loss
    elif mc.stamina.level_name=="E":
      $hw_skill_impact=hw_level_e_base_loss
    elif mc.stamina.level_name=="D":
      $hw_skill_impact=hw_level_d_base_loss
    elif mc.stamina.level_name=="C":
      $hw_skill_impact=hw_level_c_base_loss
    elif mc.stamina.level_name=="B":
      $hw_skill_impact=hw_level_b_base_loss
    elif mc.stamina.level_name=="A":
      $hw_skill_impact=hw_level_a_base_loss
    elif mc.stamina.level_name=="S":
      $hw_skill_impact=hw_level_s_base_loss
    $hw_skill_value=round(hw_skill_impact*hw_last_workout**hw_fudgefactor_loss,2)
    $hw_min_value=hw_skill_value*0.85
    $hw_max_value=hw_skill_value*1.15
    $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
    if mc.stamina.level_name!="F" or mc.stamina.xp!=0:
      $mc.give_xp("stamina",hw_entry_value)            ##  real version after testing
  $hw_previous_max_energy_base=mc.max_energy_base
  call hw_update_fitness
  if hw_previous_max_energy_base>mc.max_energy_base:   ##  level went down from nightly loss
    "You know what they say: Use it or lose it!"
    "{bad}Lost 1 AP per turn{/}"
    ""
  elif hw_previous_max_energy_base<mc.max_energy_base:
    "These workouts are really making a difference!"
    "{good}Gained 1 AP per turn{/}"
    ""
  $hw_workouts_today=0            ##  reset the workouts today counter for the new day
  return

##===== Event 0 =====

label quest_fwbenefits_event0:  ## AFTERNOON: visit Ruthie at Patrol HQ, take her to Earl's Diner, walk her home
  $global fwb_postponed
  $fwb_postponed+=1     ## increment flag to force event
  $game_bg="home bg"    ## decision to go to HQ is made at home
  $game_bgm="home bgm"
  header "Visit Patrol HQ?"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_3"  ## first use of image 3
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "I wonder how {mark}[gn_store_owner_name]{/} is doing? I'm always nervous with women, it's just easier with bots. Somehow it's not so bad with {mark}[gn_store_owner_name]{/} though."
  ""
  if fwb_postponed<=3:      ## can still postpone
    "Maybe I should go visit her at the {mark}Bot Patrol HQ{/}. I can use the excuse that I wanted to check on the bots. After I check the bots I'll ask her to have lunch with me at {mark}[gn_diner_owner_name]'s Diner{/}."
    ""
    choice("fwb_event0_hq1") "Go To HQ"
    choice("<<<") "Not Now"
  else:                     ## cannot postpone again
    "{good}I've put this off too long, I need to do this now. I'll tell her I'm checking on the bots and then I will ask her to go to lunch with me at [gn_diner_owner_name]'s diner.{/}"
    ""
    choice("fwb_event0_hq1") "Go To HQ"
  return

label fwb_event0_hq1:
  $game.location="patrol_hq"        ## use neigborhood, no need for patrol hq location
  $game_bg="patrol_hq bg_patrolhq"
  header "Patrol HQ"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_4"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_5"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{mark}[gn_store_owner_name]{/} greets me with a hug that almost knocks me over when I get to {mark}Bot Patrol HQ{/}. I think she likes me but maybe it's just because I gave her the bots."
  ""
  "I don't have the nerve to tell her I came to see her so I say; {mcsay}I came to make sure everything is OK and to check on the bots{/}."
  ""
  "{mark}[gn_store_owner_name]{/} replies; {say}Of course, let's take a look.{/}"
  ""
  "She watches me as I check on the bots and capsules. They're all good, I didn't really expect anything to be wrong."
  ""
  $global mc_so_value
## 0.11.3 deleted relationship gain for just showing up at HQ, you have to ask for the date
##  if mc_so_value<45:                                  ## do NOT allow FWB until quest end
##    call mc_update_relation(gn_store_owner_name,1,0)  ## relationship gain for visiting
  if mc.money>40:           ## you have enough money for lunch
    $global fwb_buy_lunch
    if fwb_buy_lunch==0:    ## havn't chosen not to buy lunch yet
      "{mark}Now's the time, should I ask her to have lunch with me or not?{/}"
      choice("fwb_event0_hq2",hint="$40") "Buy Lunch"
      choice("fwb_event0_nolunch") "Don't Buy Lunch"
    else:                   ## chose not to buy lunch before
      "{good}I can't keep putting this off, I'm going to ask her to lunch.{/}"
      choice("fwb_event0_hq2",hint="$40") "Buy Lunch"
  else:                     ## VERY UNLIKELY
    "{mark}Damn, I wanted to invite her to lunch but I just realized I can't afford it.{/}"
    choice(None,hint="$40") "Buy Lunch"
    choice("fwb_event0_nolunch") "Don't Buy Lunch"
  return

label fwb_event0_nolunch:           ## you did NOT to invite Ruthie to lunch at the diner
  $global fwb_postponed
  $fwb_postponed=0                  ## clear flag/counter to start postpone count over
  $global fwb_buy_lunch
  $fwb_buy_lunch=1                  ## set flag so you cannot choose to not buy lunch a second time
  $game.location="patrol_hq"
  $game_bg="patrol_hq bg_patrolhq"
  header "Patrol HQ"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_6"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_7"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  if mc.money>40:    ## you had enough money for lunch but chose not to
    "When I finish checking on the bots and capsules it's the right time but I'm too afraid to ask her out."
    "{size=-6} "
    "I'm nervous and say; {mcsay} Everything is great and I need to get back to my shop now{/}."
    "{size=-6} "
    "{mark}[gn_store_owner_name]{/} looks disappointed as she says: {say}Thanks for coming, you can come over any time to check on the patrol{/}."
    "{size=-6} "
    "{mark}Her hug is less enthusiastic than when I arrived, I probably should have invited her to lunch.{/}"
  else:              ## VERY UNLIKELY - couldn't ask because you didn't have enough money
    "When I finish checking everything I say; {mcsay} You're doing a great job maintaining the bots and running the patrol.{/}"
    "{size=-6} "
    "{mark}[gn_store_owner_name]{/} looks pleased as she says: {say}I'm trying to do my best.{/}"
    "{size=-6} "
    "Since I can't afford lunch I say; {mcsay}I think it's time I get back to my shop, I'll see you again soon.{/}"
    "{size=-6} "
    "{mark}[gn_store_owner_name]{/} gives me a hug and says; {say}Thanks for coming, come back any time to check on the patrol{/}."
    "{size=-6} "
    "Her hug is less enthusiastic than when I arrived, {mark}I need to make some money so I can invite her to lunch{/}."
## 0.11.3 delete loss of relationship for not asking about lunch but add mood decrease
##  call mc_update_relation(gn_store_owner_name,-1,0)  ##  no invite, relationship loss
  "{size=-6} "
  $mc.mood.give_xp(randint(-12,-6))                  ##  small mood decrease
  choice("goto_home") "Go Home"
  return

label fwb_event0_hq2:               ## you invited Ruthie to diner
  $global fwb_postponed
  $fwb_postponed=0                  ## clear flag/counter to use next time
  $game.location="patrol_hq"
  $game_bg="patrol_hq bg_patrolhq"
  header "Patrol HQ"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_8"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_9"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "When I finish checking on the bots and capsules we stand up and I gather up my courage."
  ""
  "I try to look confident and say; {mcsay}Can I buy you lunch at{/} {mark}[gn_diner_owner_name]'s Diner{/}?"
  ""
  "{mark}[gn_store_owner_name]{/} looks happy and replies; {say}I'd love to, thanks for asking.{/}"
  ""
  "I'm both happy and relieved and say; {mcsay}Great, is there anything you need to do or can we go now?{/}"
  ""
  "Without hesitating {mark}[gn_store_owner_name]{/} says; {say}Now is great, let's go.{/}"
  choice("fwb_event0_diner1") "Continue"
  return

label fwb_event0_diner1:
  $game.location="local_diner"   ## meal with Ruthie at diner
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_diner ld_1"
  else:
    $game_bg="local_diner ld_2"
  header "[local_diner]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_10"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_11"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{mark}[gn_diner_owner_name]{/} smiles when he hands us the Ramen noodles we ordered and {mark}[gn_store_owner_name]{/} says; {say}Looks great{/} {mark}{mark}[gn_diner_owner_name]{/}{/}{say}, you make the best Ramen!{/}"
  ""
  "During lunch {mark}[gn_store_owner_name]{/} says; {say}I'm so glad you asked me to lunch and thanks for checking up on the patrol. I think it's really helping our neighborhood.{/}"
  ""
  "I wouldn't have thought of it myself so I say; {mcsay}I'm glad you asked me to help out and you're doing a great job running the patrol.{/}"
  ""
  "As we're finishing lunch {mark}[gn_store_owner_name]{/} says; {say}It's good to see you outside your shop. Customers always tell me how great your bots are but you need to have fun too.{/}"
  choice("fwb_event0_diner2") "Continue"
  return

label fwb_event0_diner2:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_diner ld_1"
  else:
    $game_bg="local_diner ld_2"
  header "[local_diner]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_12"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_13"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "We finish lunch and get up to leave. {mark}[gn_store_owner_name]{/} says; {say}Thanks again, I need to make sure my store is OK but your bots probably run it better than I do!{/}"
  "{size=-6} "
  "I reply: {mcsay}I'm sure customers would rather see you than a couple of bots. I'm going back to my shop, let's walk together.{/}"
  "{size=-6} "
  "When we get to my shop {mark}[gn_store_owner_name]{/} surprises me with more than a hug. She really makes me happy. When she lets go of me she says; {say}This was fun, see you again soon I hope.{/}"
  "{size=-6} "
  $mc.mood.give_xp(randint(6,12))    ##  small mood increase
  $mc.money-=40                      ## pay for lunch
  $global fwb_delay_days
  $fwb_delay_days=1                  ## prevent asking for date from happening same day
  $global mc_so_value
  if mc_so_value<45:                                  ## do NOT allow FWB until quest end
    call mc_update_relation(gn_store_owner_name,1,0)  ## lunch was fun, relationship gain
  $quests.start_quest("fwbenefits")
  choice("goto_home") "Go Home"
  return

##===== Event 1 =====

label quest_fwbenefits_event1:  ## EVENING: visit Ruthie in store, ask for date at Ray's Bot Boutique tomorrow
  $global fwb_postponed
  $fwb_postponed+=1     ## increment flag to force event
  $game_bg="home bg"    ## decision to go to store is made at home
  $game_bgm="home bgm"
  header "Ask {mark}[gn_store_owner_name]{/} for a date?"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_14"  ## first use of image 14
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  if fwb_rays_date==0:   ## you haven't asked Ruthie for this date before
    "I really enjoyed having lunch with {mark}[gn_store_owner_name]{/} the other day, I'd like to do something special with her."
    ""
    "I don't know of many places to go downtown but I could take her to {mark}Ray's Bot Boutique{/}. It's a fancy place and I want to make her feel special but it is pretty expensive even if I don't buy any bots."
    ""
    if fwb_postponed<=3:        ## can still postpone
      "{mark}Should I walk over to [gn_store_owner_name]'s store and ask her to go downtown with me tomorrow evening?{/}"
      choice("fwb_event1_store1") "Go To Store"
      choice("<<<") "Not Now"
    else:                      ## cannot postpone again
      "{good}I've put this off for too long, I'll walk over to [gn_store_owner_name]'s store right now and ask her to go downtown with me tomorrow evening.{/}"
      choice("fwb_event1_store1") "Go To Store"
  else:                  ## you cancelled the date once already
    "I feel bad about postponing my date with {mark}[gn_store_owner_name]{/}. I really like her, I need to grow a pair and do this."
    ""
    "Even though it's expensive I'll take her to {mark}Ray's Bot Boutique{/}. It's a fancy place and I want to make her feel special."
    ""
    "{good}I'll walk over to [gn_store_owner_name]'s store right now and ask her to go downtown with me tomorrow evening.{/}"
    choice("fwb_event1_store1") "Go To Store"
  return

label fwb_event1_store1:
  $global fwb_postponed
  $fwb_postponed=0                ## clear flag/counter for next use
  $game.location="corner_store"   ## invite Ruthie on date at store
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_15"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_16"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  if fwb_rays_date==0:        ## first time asking for date at Ray's
    "{mark}[gn_store_owner_name]{/} and her bots were working in the store when I arrived and she embraced me saying; {say}I'm glad you came, the store is empty and I was bored.{/}"
    ""
    "She feels good and actually I'm glad the store is empty. When we break the embrace I ask; {mcsay}Is the store empty a lot? How are the bots working out?{/}"
    ""
    "She says; {say}You just came at a slow time, the store is usually busy and the bots are working out great. They treat customers well and make them feel safe so I think they've actually increased sales. They also give me plenty of time to run the bot patrol.{/}"
  else:                       ## you've cancelled at least one date at Ray's
    "As usual, {mark}[gn_store_owner_name]{/} and her bots were working in the store when I arrived. {mark}[gn_store_owner_name]{/} embraced me saying; {say}You always seem to know when the store will be empty.{/}"
    ""
    "She feels good and I'm glad the store is empty. We break the embrace and I say playfully; {mcsay}I don't think you ever have any customers.{/}"
    ""
    "She replies; {say}Hey, that's mean. Of course I have customers. Everyone in the neighborhood comes to my store. People can get along without bots but they have to eat you know.{/}"
  choice("fwb_event1_store2") "Continue"
  return

label fwb_event1_store2:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_17"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_18"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  if fwb_rays_date==0:        ## first time asking for date at Ray's
    "You say to {mark}[gn_store_owner_name]{/}; {mcsay}The reason I came over is to ask if you'd like to go downtown with me tomorrow evening. There's a fancy place called {/} {mark}Raymond's Bot Boutique{/} {mcsay}that I've been to. I can't afford the bots they sell but it's a nice place.{/}"
    ""
    "She gets excited and jumps into my arms saying; {say}I'd love to go out with you! I never go downtown, I can't remember the last time."
  else:                       ## you've cancelled at least one date at Ray's
    "You say to {mark}[gn_store_owner_name]{/}; {mcsay}The reason I came over is to ask you for a date again, I'm sorry I postponed it last time. Would you like to go downtown to{/} {mark}Raymond's Bot Boutique{/} {mcsay}tomorrow evening.{/}"
    ""
    "She gets excited just like last time and jumps into my arms saying; {say}I'd love to go out with you! Like I told you before, I can't remember the last time I went downtown.{/}"
  choice("fwb_event1_store3") "Continue"
  return

label fwb_event1_store3:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_19"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_20"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "You set {mark}[gn_store_owner_name]{/} down but don't let her go as you say; {mcsay}Great, I'm sure we'll have fun. I'll pick you up at your apartment tomorrow evening and we'll ride the subway downtown."
  "{size=-6} "
  "She replies; {say}This will be fun, I'm looking forward to it already.{/}"
  "{size=-6} "
  "You say your goodbyes and you're feeling pretty good as you walk back to your shop. {mark}[gn_store_owner_name]{/} watches you leave thoughtfully."
  "{size=-6} "
  $mc.mood.give_xp(randint(6,12))                    ##  small mood increase
  $global fwb_delay_days
  $fwb_delay_days=0                                  ## date is next day, no delay needed
  $global mc_so_value
  if mc_so_value<45:                                 ## do NOT allow FWB until quest end
   call mc_update_relation(gn_store_owner_name,1,0)  ##  asked and accepted, relationship gain
  $quests.fwbenefits.advance()
  choice("goto_home") "Go Home"
  return

##===== Event 2 =====

label quest_fwbenefits_event2:  ## EVENING: Pick Ruthie up, go to Ray's, stuff happens there, take Ruthie home
  $game_bg="home bg"    ## decision to go on date is made at home
  $game_bgm="home bgm"
  header "Date with {mark}[gn_store_owner_name]{/}"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_3"     ## 2nd use of image 3
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "It's time to go pick up {mark}[gn_store_owner_name]{/} at her apartment for our date. I really like her and I want to do this but it is expensive. {mark}Raymond's Bot Boutique{/} will cost {mark}$1,200 each{/} and the subway another {mark}$20 each{/}. At least drinks are included in the admission."
  ""
  "Even if I dont' buy any bots the night will cost me {mark}$2,440{/}."
  ""
  if mc.money>2440:           ## you have enough money
    if fwb_rays_date==0:      ## first time through
      "{mark}Should I do this or should I call it off?"
      choice("fwb_event2_date1",hint="$2440, 3 AP") "Go on Date"
      choice("fwb_event2_postpone") "Postpone Date"
    else:                     ## you've postponed the date before
      "{good}I can't postpone this again, let's do it.{/}"
      choice("fwb_event2_date1",hint="$2440") "Go on Date"
  else:                       ## you don't have enough money
    "{bad}Damn, I didn't plan this well, I don't have enough money for this date, I'll have to postpone it.{/}"
    choice("fwb_event2_postpone") "Postpone Date"
  return

label fwb_event2_postpone:
  $game_bg="home bg"    ## decision to postpone is made at home
  $game_bgm="home bgm"
  header "Date with {mark}[gn_store_owner_name]{/}"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_21"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_22"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "You call {mark}[gn_store_owner_name]{/} and say; {mcsay}I'm sorry but something came up and I have to postpone our date tonight. I hope you understand."
  "{size=-6} "
  "You can hear the disappointment in her voice when she says; {say}I hope everything is OK, maybe we can do it another night?"
  "{size=-6} "
  "Sensing her disappointment you say; {mcsay}I'm really sorry, of course we can do it another night. I'll let you know when.{/}"
  "{size=-6} "
  "After you hang up you feel terrible and decide you'll have to pick another day and go through with the date."
  "{size=-6} "
  $mc.mood.give_xp(randint(-50,-30))                  ##  large mood decrease
  $global fwb_delay_days
  $fwb_delay_days=0              ## no delay needed, repeat event every day
  call mc_update_relation(gn_store_owner_name,-2,0)    ##  postponed, relationship loss, loss always allowed
  $quests.fwbenefits.advance(1)  ## go back to previous phase so you can ask for date again
  $global fwb_rays_date
  $fwb_rays_date=1               ## set flag so text changes second time throughevent 1 and cannot postpone date again if you have enough money
  choice("<<<") "Continue"       ## abort event 2, never left home, <<< ok
  return

label fwb_event2_date1:
  $game.location="neighborhood"      ## start of date is in neighborhood
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "[neighborhood]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_23"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_24"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "You're surprised that {mark}[gn_store_owner_name]{/} was waiting in front of her apartment building. You great with a hug and a kiss and then ask; {mcsay}Have you been waiting long?"
  ""
  "She says; {say}No, I'm just anxious and excited, let's go."
  ""
  "You walk to the subway station together and along the way {mark}[gn_store_owner_name]{/} says; {say}I'm a little nervous, is this a really fancy place?{/}"
  ""
  "You reply; {mcsay}It is fancy and mostly rich people go there. Don't worry, we're just going there to have a good time and do some people watching."
  ""
  $mc.money-=40                          ## pay for subway
  choice("fwb_event2_date2a") "Continue"
  return

## 0.15.n add a scene in the hallway with bouncers to match normal entrance to Raymond's
label fwb_event2_date2a:
  $game.location="rays_boutique"
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel rays ray_44"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel rays ray_43"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "When you get out of the elevator the two scary looking bouncers are there as usual. {mark}[ns_teacher_name]{/} looks a little scared so you try to look confident to reassure her."
  ""
  "One of the bouncers looks at you with stern expression and the other looks at {mark}[ns_teacher_name]{/} with a look that makes her even more nervous. The guy needs some manners."
  ""
  "You get out the admission fee for both of you and hand it to one of the bouncers. He counts it twice while the other one keeps staring at {mark}[ns_teacher_name]{/}. Eventually they let you in."
  ""
  $mc.money-=2400                        ## pay for Raymond's
  choice("fwb_event2_date2b") "Continue"
  return


label fwb_event2_date2b:
  $game.location="rays_boutique"
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_25"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_26"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "When you walk inside you're surprised to hear a familiar voice call out; {mark}[mc.name]{/}{say}, what a pleasant surprise to see you!{/}"
  ""
  "I can't believe it, I know someone here? Although she's dressed differently I realize it's {mark}[ns_teacher_name]{/} the {mark}Night School{/} teacher. She continues; {say}Please join me here, I'd love to meet your girlfriend.{/}"
  ""
  "You accept her invitation and both of you sit down across from {mark}[ns_teacher_name]{/} as you make introductions; {mcsay}This is{/} {mark}[gn_store_owner_name]{/} {mcsay}who owns a market near my workshop and this is{/} {mark}[ns_teacher_name]{/} {mcsay}who operates a{/} {mark}Night School{/}{mcsay}.{/}"
  ""
##  $mc.money-=2400                        ## pay for Raymond's - moved payment to scene by elevators
  choice("fwb_event2_date3") "Continue"
  return

label fwb_event2_date3:
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_27"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_28"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
## 0.14 changed text to stop assuming you've won more than one Karaoke competition, it was confusing if you hadn't  
  $global sr_first_karaoke
  $global sr_karaoke_wins
  if sr_karaoke_wins>1:      ## won at karaoke more than once
    "{mark}[ns_teacher_name]{/} notices that {mark}[gn_store_owner_name]{/} is very nervous and tries to help her out by saying; {say}It's a pleasure to meet you{/} {mark}[gn_store_owner_name]{/}{say}. I met {mark}[mc.name]{/} {say}when he took my class in bot social training and now his bots win Karaoke competitions.{/}"
  elif sr_karaoke_wins==1:   ## won one time at karaoke
    "{mark}[ns_teacher_name]{/} notices that {mark}[gn_store_owner_name]{/} is very nervous and tries to help her out by saying; {say}It's a pleasure to meet you{/} {mark}[gn_store_owner_name]{/}{say}. I met {mark}[mc.name]{/} {say}when he took my class in bot social training and now his bot won a Karaoke competition.{/}"
  elif sr_first_karaoke!=0:  ## competed in karaoke but no wins
    "{mark}[ns_teacher_name]{/} notices that {mark}[gn_store_owner_name]{/} is very nervous and tries to help her out by saying; {say}It's a pleasure to meet you{/} {mark}[gn_store_owner_name]{/}{say}. I met {mark}[mc.name]{/} {say}when he took my class in bot social training and we both attend bot Karaoke competitions.{/}"
  else:                      ## never competed in karaoke
    "{mark}[ns_teacher_name]{/} notices that {mark}[gn_store_owner_name]{/} is very nervous and tries to help her out by saying; {say}It's a pleasure to meet you{/} {mark}[gn_store_owner_name]{/}{say}. I met {mark}[mc.name]{/} {say}when he took my class in bot social training and he was one of my favorite students.{/}"
## 0.14 end of change
  ""
  "{mark}[gn_store_owner_name]{/} is grateful that {mark}[ns_teacher_name]{/} is being nice to her and replies; {say}I know he's good. He gave me two fantastic trained bots that help me run my store and then he made six more trained bots that patrol our neighborhood to keep all of us safe.{/}"
  ""
  "While listening {mark}[ns_teacher_name]{/} quietly motions to the host standing nearby who nods and winks to let her know he's ready."
  choice("fwb_event2_date4") "Continue"
  return

label fwb_event2_date4:
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_29"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_30"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "The host comes over and taps me on the shoulder saying politely; {say}Sir, would you be kind enough to join me at the bar so we can speak privately?{/}"
  ""
  "I'm surprised and a little nervous but he's not threatening so I say; {mcsay}Of course.{/}"
  ""
  "When I turn to {mark}[gn_store_owner_name]{/} I see she's very nervous so I say; {mcsay}Excuse me, I'm not sure what this is about but I'll be back in no time.{/}"
  ""
  "{mark}[ns_teacher_name]{/} helps by smiling and saying in a very friendly voice; {say}No need to hurry, I'll enjoy talking with{/} {mark}[gn_store_owner_name]{/} {say}while you two are busy.{/}"
  choice("fwb_event2_date5") "Continue"
  return

label fwb_event2_date5:
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_31"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_32"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "At the bar the host asks; {say}First things first, what can I get for you and your guest?{/}"
  ""
  "I realize it might be out of place here but I reply; {mcsay}Two beers please.{/}"
  ""
  "While the bartender pours the beers the host says; {say}Please don't take this badly but I wanted to ask you to please dress more formally when you come to {mark}Raymond's{/}. I hate to ask but we have a reputation to maintain, I hope you understand.{/}"
  ""
  "I'm not really happy about it but I guess I understand so I say; {mcsay}I'm sorry, I understand and will dress better if I come back.{/}"
  choice("fwb_event2_date6") "Continue"
  return

label fwb_event2_date6:
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_33"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_34"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{bad}(Conversation I missed){/}"
  ""
  "{mark}[ns_teacher_name]{/} friendly; {say}So how long have you and{/} {mark}[mc.name]{/} {say}been seeing each other?{/} {mark}[gn_store_owner_name]{/} shyly; {say}This is our first date.{/}"
  ""
  "{mark}[ns_teacher_name]{/} knowingly: {say}I'm guessing you'd like more dates and maybe more than dates?{/} {mark}[gn_store_owner_name]{/} shyly; {say}Yes.{/}"
  ""
  "{mark}[ns_teacher_name]{/} says: {say}I plan to offer him a business partnership that will make us both rich: his bots and my contacts. If you help me convince him I'll coach you on building the relationship you want.{/} {mark}[gn_store_owner_name]{/} giving her phone number; {say}I won't promise anything and I won't lie to him.{/}"
  choice("fwb_event2_date7") "Continue"
  return

label fwb_event2_date7:
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_35"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_36"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "When I return with the beers {mark}[gn_store_owner_name]{/} looks relieved and asks: {say}Thanks, what did he want?"
  ""
  "To avoid embarrassment I reply; {mcsay}He just asked me what sort of bots I'm interested in, I'm not sure why it needed to be private.{/}"
  ""
  "{mark}[ns_teacher_name]{/} has a funny look, I think she knows I'm lying. I continue; {mcsay}Did you two enjoy getting to know each other?{/}"
  ""
  "{mark}[ns_teacher_name]{/} replies quickly before {mark}[gn_store_owner_name]{/} can say anything; {say}We enjoyed a little girl talk.{/} Looking at {mark}[gn_store_owner_name]{/} she adds: {say}Just getting to know each other, no obligation but maybe we can be friends.{/}"
  choice("fwb_event2_date8") "Continue"
  return

label fwb_event2_date8:
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_37"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_38"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "We're interrupted by a couple coming to our table to say hello to {mark}[ns_teacher_name]{/}. The man speaks nicely to her while the woman glares at {mark}[gn_store_owner_name]{/} and I menacingly."
  ""
  "I can see that {mark}[gn_store_owner_name]{/} is really upset about how the woman looked at her so I try to comfort her as the couple walks away."
  ""
  "I notice that {mark}[ns_teacher_name]{/} and the woman exchange evil looks as they leave while the man tries to calm his partner down. {mark}The man looks familiar, he resembles the syndicate leader that I had to pay when that guy framed me.{/}"
  choice("fwb_event2_date9") "Continue"
  return

label fwb_event2_date9:
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_39"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_40"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "A little while later another couple stops by to say hi to {mark}[ns_teacher_name]{/}. Both of them are angry and ask what she's doing with people like us."
  ""
  "Looking around I see that a few other people are staring at us. Both {mark}[gn_store_owner_name]{/} and I are really hurt by these people's behavior."
  ""
  "The host comes over and {mark}[ns_teacher_name]{/} stands up to confront them. The couple is surprised that people are defending the two of you instead of agreeing with them. The host insists that they behave politely and asks them to return to their seats."
  choice("fwb_event2_date10") "Continue"
  return

label fwb_event2_date10:
  $temp_image=random.randint(1,2)      ## date2 is in Ray's Boutique
  $game_bg="rays_boutique bg_"+str(temp_image)
  header "[rays_boutique]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_41"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_42"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{mark}[gn_store_owner_name]{/} is really upset and I am too. I comfort her saying; {mcsay}The people here are a bunch of rich assholes, I'm sorry I brought you here and I think it's time we leave.{/}"
  "{size=-6} "
  $mc.mood.give_xp(randint(-50,-30))                  ##  large mood decrease
  "{size=-6} "
  "{mark}[ns_teacher_name]{/} says; {say}I'm really sorry about some of the people here. It was really nice to meet you {mark}[gn_store_owner_name]{/} and I hope to see you again somewhere else.{/}"
  "{size=-6} "
  "As we leave I can hear the host talking with {mark}[ns_teacher_name]{/}. She's angry that he let things get out of hand and he apologizes saying he intervened as quickly as he could."
  choice("fwb_event2_date11") "Continue"
  return

label fwb_event2_date11:
  $game.location="neighborhood"           ## going home to the neighborhood
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_43"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_44"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "You take {mark}[gn_store_owner_name]{/} back to the subway station and get on the train back home. She says; {say}I'm sorry I got so upset and ruined the evening.{/}"
  ""
  "I tell her; {mcsay}Dont' say that, you didn't ruin anything. Those rich assholes caused it all. I'm sorry I took you there, it was stupid of me.{/}"
  ""
  "You walk {mark}[gn_store_owner_name]{/} from the subway station back to her apartment building and say goodnight to her before walking home yourself."
  ""

##0.14 will be used in 0.15 when I create pictures of MC at Raymond's with the suit - button deactivated in 'street.rpy' (0020-game-locations-street)
  $global fwb_deactivate_rays
  $fwb_deactivate_rays=1

  $mc.energy-=3                                       ## used hint in original button, must put this in manually
  $global fwb_delay_days
  $fwb_delay_days=0                                   ## no delay, Simone visits next morning
  $global mc_so_value
  if mc_so_value<45:                                  ## do NOT allow FWB until quest end
    call mc_update_relation(gn_store_owner_name,1,0)  ## date was bad but not your fault, relationship gain
  $quests.fwbenefits.advance()
  choice("goto_home") "Go Home"                       ## end of event 2, left home, return required
  return

##===== Event 3 =====

label quest_fwbenefits_event3:  ## MORNING: Simone visits shop to propose partnership, you say you'll think about it
  $game_bg="home bg"            ## Simone visits shop
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Visits My Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_45"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_46"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "While I'm working in the shop checking one of my bot's psychocore readings I'm surprised to see {mark}[ns_teacher_name]{/} walking into the shop. She's dressed down today, I almost didn't recognize her. {mark}Her top is unbuttoned pretty far, she's really hot and it's distracting{/}."
  ""
  "She says; {say}Can you take a break? I'd like to talk with you if that's OK.{/} I say; {mcsay}Sure, have a seat and I'll get us some coffee.{/}"
  ""
  "She starts saying; {say}It was nice to meet {mark}[gn_store_owner_name]{/} last night and I'm sorry it ended badly. I wasn't surprised when she told me about the bots you made for her and to help out your neighbors.{/}"
  choice("fwb_event3_simone1") "Continue"
  return

label fwb_event3_simone1:
  $game_bg="home bg"       ## Simone visits shop
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Visits My Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_47"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_48"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "I wasn't sure what to say so {mark}[ns_teacher_name]{/} continued; {say}I also know about the bots you made that took down the mob.{/} I'm shocked and ask; {mcsay}How do you know about that?{/}"
  ""
  "She smiles and says; {say}Relax, I'm not telling anyone. I planted the entertainment bots in their hideout so I knew everything about both the mob and your bots.{/}"
  ""
  "Changing the subject she says; {say}I have a proposal for you, a business partnership. You're doing OK here but I have contacts who will pay large amounts of money for the type of bots you can build and train. What do you think?{/}"
  choice("fwb_event3_simone2") "Continue"
  return

label fwb_event3_simone2:
  $game_bg="home bg"    ## Simone visits shop
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Visits My Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_49"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_50"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "Wow, I wasn't expecting this so I say; {mcsay}I'm not sure. You can train bots yourself, why do you want to work with me?{/}"
  ""
## 0.14 changed text to stop assuming you've won more than one Karaoke competition, it was confusing if you hadn't  
  $global sr_first_karaoke
  $global sr_karaoke_wins
  if sr_karaoke_wins>1:      ## won at karaoke more than once
    "{mark}[ns_teacher_name]{/} replies; {say}You have an amazing knack for training bots. Your bots won Karaoke contests faster than anyone else, your bots took down an entire mob, your bots run {mark}[gn_store_owner_name]'s{/} store, and your bots keep your neighborhood safe. Beside all of that I like you and I want to help you out.{/}"
  elif sr_karaoke_wins==1:   ## won one time at karaoke
    "{mark}[ns_teacher_name]{/} replies; {say}You have an amazing knack for training bots. Your bot won a Karaoke contest faster than anyone else, your bots took down an entire mob, your bots run {mark}[gn_store_owner_name]'s{/} store, and your bots keep your neighborhood safe. Beside all of that I like you and I want to help you out.{/}"
  elif sr_first_karaoke!=0:  ## competed in karaoke but no wins
    "{mark}[ns_teacher_name]{/} replies; {say}You have an amazing knack for training bots. Your bots took down an entire mob, your bots run {mark}[gn_store_owner_name]'s{/} store, your bots keep your neighborhood safe, and I'm sure your bots will win Karaoke contests if you keep trying. Beside all that I like you and I want to help you out.{/}"
  else:                      ## never competed in karaoke
    "{mark}[ns_teacher_name]{/} replies; {say}You have an amazing knack for training bots. Your bots took down an entire mob, your bots run {mark}[gn_store_owner_name]'s{/} store, and your bots keep your neighborhood safe. I'm sure your bots would win Karaoke contests if you tried. Beside all of that I like you and I want to help you out.{/}"
## 0.14 end of change
  ""
  "I'm still uncertain so I say; {mcsay}I'll have to think about it.{/} She replies; {say}OK, just let me know when you decide you want to make real money. If you want I'll keep your name out of it so there's no risk.{/}"
  choice("fwb_event3_simone3") "Continue"
  return

label fwb_event3_simone3:
  $game_bg="home bg"    ## Simone visits shop
  $game_bgm="home bgm"
  header "{mark}[ns_teacher_name]{/} Visits My Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_51"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_52"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "As {mark}[ns_teacher_name]{/} is leaving she turns and says; {say}Here's some free advice, if you want to hang around and sell bots to high rollers you need to dress better. Keep in touch.{/}"
  ""
  "After she leaves I think about what she said. Her proposal seems like a good idea but I'm not certain and the free advice is the same thing the host told me last night. {mark}Coincidence or are they working together?{/} Oh well, back to work now."
  ""
  $global fwb_delay_days
  $fwb_delay_days=0             ## no delay needed, go to Ruthie's store same day
  $global mc_nst_value
  if mc_nst_value<35:                             ## limit for teacher in 0.11.n
    call mc_update_relation(ns_teacher_name,1,0)  ## she visited, you got offer, relationship gain
  $quests.fwbenefits.advance()
  choice("<<<") "Continue"      ## end event 3, never left home, <<< ok
  return

##===== Event 4 =====

label quest_fwbenefits_event4:  ## AFTERNOON: visit Ruthie at store, ask to meet at local bar tonight
  $global fwb_postponed
  $fwb_postponed+=1     ## increment flag to force event
  $game_bg="home bg"            ## decision to visit Ruthie at store made at home
  $game_bgm="home bgm"
  header "HOME - - Coffee Break Over"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
##  $action_image= "quests friends_with_benefits fwb_14"     ## 2nd use of image 14
  $action_image= "quests friends_with_benefits sq_4b"    ## use coffee break image
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  if fwb_postponed<=1:    ## first time through
    "Before getting back to work I think about {mark}[gn_store_owner_name]{/}. I don't like the way our first date ended and I need to do something to make it up to her."
    ""
    "Another thing, she's been running a store on her own so she knows something about running a business. She also met {mark}[ns_teacher_name]{/}, maybe she can help me decide if I should become her partner or not."
    ""
    "{mark}Maybe I should go to her shop and ask her to meet me at the local bar tonight. No rich assholes there! Should I do it?{/}"
    choice("fwb_event4_store1") "Go to Store"
    choice("<<<") "Not Now"
  else:                   ## you postponed doing this once and cannot do it again
    "It's time to go back to work but you can't stop thinking about how badly your first date with {mark}[gn_store_owner_name]{/} went."
    ""
    "You also want to talk to her about {mark}[ns_teacher_name]'s{/} partnership proposal, she met her and might have some good advice."
    ""
    "{good}You decide you must go to [gn_store_owner_name]'s store and ask her to meet you at the local bar tonight.{/}"
    choice("fwb_event4_store1") "Go to Store"
  return

label fwb_event4_store1:
  $global fwb_postponed
  $fwb_postponed=0                ## clear flag/counter for next use
  $game.location="corner_store"   ## MC goes to Ruthie's store
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_53"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_54"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{mark}[gn_store_owner_name]{/} greets me with a warm hug saying; {say}You always visit when there aren't any customers.{/} I smile and reply; {mcsay}I told the bots to chase all the customers away.{/} She replies; {say}You're so mean, are you trying to sabotage my store?{/}"
  ""
  "You laugh and change the subject; {mcsay}I want to apologize for how our date ended, going there was a bad idea.{/} She replies; {say}Hey, it's not your fault that rich people are jerks.{/}"
  ""
  "I decide it's time to get to the reason I came; {mcsay}I'd like to make it up to you. If you meet me at our local bar tonight I'm sure there are no rich assholes there and we'll have a good time. What do you say?{/}"
  choice("fwb_event4_store2") "Continue"
  return

label fwb_event4_store2:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_55"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_56"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{mark}[gn_store_owner_name]{/} gives me another hug and smiles back saying; {say}I'd love to meet you at the bar tonight and if any rich assholes show up we'll all gang up on them and throw them out.{/}"
  "{size=-6} "
  "As I turn around to leave I say; {mcsay}Great, I'll see you tonight. I need to get back to work and your shop is {good}\"full of customers\"{/} to take care of.{/}"
  "{size=-6} "
  "She calls out after me; {say}You better stop telling my bots to chase customers away, I need them or I'll be out on the street!{/}"
  "{size=-6} "
  $mc.mood.give_xp(randint(6,12))                     ## small mood increase
  $global fwb_delay_days
  $fwb_delay_days=0                                   ## no delay needed, go to bar same day
  $global mc_so_value
  if mc_so_value<45:                                  ## do NOT allow FWB until quest end
    call mc_update_relation(gn_store_owner_name,1,0)  ## date asked and accepted, relationship gain
  $quests.fwbenefits.advance()
  choice("goto_home") "Go Home"     ## end event 4
  return

##===== Event 5 =====

label quest_fwbenefits_event5:  ## NIGHT: meet at bar, discuss Simone, have fun, walk Ruthie home, have sex, walk home
  $global fwb_bar_after_rays
  $game_bg="home bg"    ## decision to meet Ruthie at bar happens at home
  $game_bgm="home bgm"
  header "Time to Meet {mark}[gn_store_owner_name]{/} at the Bar"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_3"     ## 3rd use of image 3
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")

  if fwb_bar_after_rays==0:     ## first time through, postpone is available
    "It's time to meet {mark}[gn_store_owner_name]{/} at the bar, I really owe her a good time. I really like her and I think she likes me too."
    ""
    "It's sort of funny, I have lots of sex with bots but technically I'm still a virgin. Who knows, maybe one day I'll get lucky."
    ""
    "{mark}Should I go or should I call her and postpone it until tomorrow?{/}"
    choice("fwb_event5_bar1",cost=[("money",250),("energy",3)]) "Go to Bar"
    choice("fwb_event5_postpone") "Postpone Date"
  else:                         ## postponed once, can't do it again
    if mc.money>250:
      "It's time to meet {mark}[gn_store_owner_name]{/} at the bar and I can't disappoint her like I did last night."
      ""
      "I'm sure we'll have a good time at the bar and if I'm lucky an even better time afterwards."
      ""
      "{good}I better get going, I don't want her to sit there waiting for me.{/}"
      choice("fwb_event5_bar1",cost=[("money",250),("energy",3)]) "Go to Bar"
    else:
      "It's time to meet {mark}[gn_store_owner_name]{/} at the bar {bad}but I don't have enough money{/}."
      ""
      "I can't disappoint her like I did last night. I know, I'll ask {mark}[gn_diner_owner_name]{/} to lend me the money so I don't disappoint {mark}[gn_store_owner_name]{/}. He likes her and I think he likes me so I'm sure he'll do it."
      ""
      "{good}I'll stop at the diner to get some money and then go to the bar.{/}"
      ""
      choice("fwb_event5_borrow_money") "Go to Diner"
  return

label fwb_event5_postpone:
  $global fwb_bar_after_rays
  $fwb_bar_after_rays=1  ## set flag indicating you postponed the bar meeting with Ruthie
  $game_bg="home bg"     ## decision to postpone is made at home
  $game_bgm="home bgm"
  header "[home]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_57"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_58"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "You're not ready for this so you make up an excuse and call {mark}[gn_store_owner_name]{/} to postpone the date."
  "{size=-6} "
  "You call her and say; {mcsay}Hey, I'm really sorry but I got a big order and I need to postpone our date at the bar until tomorrow.{/}"
  "{size=-6} "
  "{mark}[gn_store_owner_name]{/} sounds disappointed; {say}Are you sure, I was really looking forward to seeing you tonight.{/}"
  "{size=-6} "
  "You reply; {mcsay}Yes, I'm sure. The job has to be delivered tomorrow, I promise to make it up to you tomorrow night.{/}"
  "{size=-6} "
  "She sounds a little angry; {say}OK, if that's the way it has to be I guess it's OK. You better not back out again tomorrow."
  "{size=-6} "
  "You reply; {mcsay}I promise, tomorrow night for sure.{/}"
  "{size=-6} "
  $mc.mood.give_xp(randint(-50,-30))                 ## large mood decrease
  call mc_update_relation(gn_store_owner_name,-2,0)  ## postponed, relationship lost - loss always allowed
  choice("<<<") "Continue"                           ## abort event 5, never left home, <<< ok
  return

label fwb_event5_borrow_money:
  $game.location="local_diner"
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_diner ld_1"
  else:
    $game_bg="local_diner ld_2"
  header "[local_diner]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_208"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_209"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "When I arrive at the diner I say; {mcsay}I'm in a jam {mark}[gn_diner_owner_name]{/} and I could really use your help. I asked{/} {mark}[gn_store_owner_name]{/}{mcsay} to meet me at the local bar tonight and I'm short on cash. Can I borrow{/} {mark}$250{/}{mcsay}? I'll pay you back as soon as I can.{/}"
  ""
  "{mark}[gn_diner_owner_name]{/} smiles and replies; {say}You can have the money as a gift. You do so much for our neighborhood I am happy to be able to give back. It makes me happy to see the two of you enjoy yourselves.{/}"
  ""
  "You're surprised and reply; {mcsay}Thanks, you're the best{/} {mark}[gn_diner_owner_name]{/} {mcsay}and I really appreciate it. Sorry I have to hurry off.{/}"
  ""
  "You run off to the local bar hoping you arrive ahead of {mark}[gn_store_owner_name]{/}."
  choice("fwb_event5_bar1",cost=[("energy",3)]) "Go to Bar" 
  return

label fwb_event5_bar1:
  $game.location="local_bar"       ## date at local bar
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_59"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_60"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "I arrive before {mark}[gn_store_owner_name]{/} and I see that {mark}[gn_retired_fighter_name]{/} is sitting in his favorite seat at the bar. I order a beer and sit down to talk with him until she gets here."
  ""
  "After a little while {mark}[gn_store_owner_name]{/} walks in and draws everyone's attention including mine. She's wearing a new outfit instead of her usual clothes and she looks fantastic. I've always known she has a great figure but it really shows in her new outfit."
  choice("fwb_event5_bar2") "Continue"
  return

label fwb_event5_bar2:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_61"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_62"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{mark}[gn_store_owner_name]{/} comes over to say hi to {mark}[gn_retired_fighter_name]{/} and I and then gives me a hug. {mark}[gn_retired_fighter_name]{/} gives a wolf whistle, punches me in the shoulder and asks; {say}What is this hot babe doing with an ugly mug like you?{/}"
  ""
  "I decide to play his game and say to {mark}[gn_store_owner_name]{/}; {mcsay}Let's get away from this old man and sit down in the back.{/} She smiles at both of us and says; {say}Good idea, let's go.{/} She turns and leads the way to a table."
  ""
  "Neither {mark}[gn_retired_fighter_name]{/} nor I can resist checking {mark}[gn_store_owner_name]{/} out as she walks away. It's amazing what a difference her new outfit makes. I think it's giving her more confidence too."

  choice("fwb_event5_bar3") "Continue"
  return

label fwb_event5_bar3:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_63"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_64"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "We sit down at a table towards the back and I tell {mark}[gn_store_owner_name]{/}; {mcsay}You look fantastic! Maybe {mark}[gn_retired_fighter_name]{/} has a point, what are you doing with me?"
  ""
  "She looks a little embarrassed and says; {say}Actually{/} {mark}[ns_teacher_name]{/} {say}suggested I dress up a little more the other night and bought me the outfit this afternoon. Do you like it?{/} I reply; {mcsay}Of course I do and I think you saw everyone elses reaction too.{/}"
  ""
  "Is {mark}[ns_teacher_name]{/} up to something? I continue; {mcsay}That was really nice of her and it looks great on you. Actually I wanted to talk with you about {mark}[ns_teacher_name]{/}."
  choice("fwb_event5_bar4") "Continue"
  return

label fwb_event5_bar4:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_65"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_66"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "I start by saying; {mcsay}This morning{/} {mark}[ns_teacher_name]{/} {mcsay}came into my shop and offered me a business partnership. She said she has contacts who would pay a lot of money for the type of bots I've been building and training.{/}"
  ""
  "I'm surprised when {mark}[gn_store_owner_name]{/} looks even more embarrassed and says; {say}She told me she was going to do that and she wants me to help her convince you to accept.{/}"
  choice("fwb_event5_bar5") "Continue"
  return

label fwb_event5_bar5:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_67"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_68"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "This is getting strange so I ask; {mcsay}So is that why she bought you the outfit?{/}"
  ""
  "{mark}[gn_store_owner_name]{/} responds emphatically; {say}It probably was but I'm not going to try to convince you of anything. I told her I wouldn't promise anything, I wouldn't lie to you, and that it's your decision. She said OK and bought me the outfit anyway.{/}"
  ""
  "I believe her and she looks relieved when I say; {mcsay}Thanks, I'm glad you told her that. To be honest, since you met her at{/} {mark}Raymond's{/} {mcsay}I  planned to ask you what you think of{/} {mark}[ns_teacher_name]{/} {mcsay}and her proposal.{/}"
  choice("fwb_event5_bar6") "Continue"
  return

label fwb_event5_bar6:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_69"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_70"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "Your conversation is interrupted when the barmaid comes by; {say}What can I get for you two?{/} {mark}[gn_store_owner_name]{/} says; {say}White wine please.{/} and I say; {mcsay}I'll have a draft beer.{/}"
  ""
  "I tease {mark}[gn_store_owner_name]{/} a little by asking; {mcsay}So is ordering wine another one of{/} {mark}[ns_teacher_name]'s{/} {mcsay}suggestions?{/} Again she's a little embarrassed; {say}Yes it is, she said wine is a little more classy than beer and that beer bellies aren't attractive.{/}"
  ""
  "I'm surprised; {mcsay}Hey, that was mean of her. You look great and you don't have even the slightest hint of a beer belly.{/} She quickly replies' {say}No, it's not like that. It was just girl talk and we laughed about it.{/}"
  choice("fwb_event5_bar7") "Continue"
  return


label fwb_event5_bar7:
  $global fwb_can_start_bp
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_71"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_72"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "Returning to our conversation before the interruption, {mark}[gn_store_owner_name]{/} says; {say}I know the outfit and advice make it look like I'm on her side but since you ask I'll tell you that I honestly think she's smart, she's kind, she wasn't pushy, and I really enjoyed spending time with her.{/}"
  ""
  "I tell her; {mcsay}I've also spent some time with her at{/} {mark}Bot Karaoke Contests{/} {mcsay} and I think the same thing. I'm seriously considering accepting the partnership. It might be just the thing I need to make my business successful.{/} {mark}[gn_store_owner_name]{/} agrees; {say}I'm a little reluctant to say anything but I agree with you.{/}"
  $fwb_can_start_bp=1    ## flag set so you can call Simone to start business partner quest, greyed out button until quest exists!
  choice("fwb_event5_bar8") "Continue"
  return

label fwb_event5_bar8:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_73"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_74"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "The barmaid interupts us again by bringing our drinks. After she sets them down and leaves I say to {mark}[gn_store_owner_name]{/} playfully; {mcsay}Maybe I should switch to wine too.{/} She replies playfully; {say}Why, do you think you're growing a beer belly?{/}"
  ""
  "A little more seriously I say; {mcsay}Actually{/} {mark}[ns_teacher_name]{/} {mcsay}suggested that I start dressing better too. In fact the guy at{/} {mark}Raymond's{/} {mcsay}told me the same thing when he pulled me aside the other night.{/} She says; {say}I thought you were leaving something out the other night.{/} Then she adds playfully; {say}Maybe it's a good idea, I'd like to hang out with a classy guy!{/}"
  choice("fwb_event5_bar9") "Continue"
  return

label fwb_event5_bar9:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_75"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_76"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "I decide that's enough business; {mcsay}Let's toast to a better night in our neighborhood than the one downtown.{/} {mark}[gn_store_owner_name]{/} agrees; {say}I'll definitely drink to that!{/}"
  ""
  "To get to know her better I ask; {mcsay}Hey, I've always wondered how you got started running your store.{/} She answers sadly; {say}It was my parents store and I started running it when they died.{/} I reply; {mcsay}I'm sorry, that must have been difficult.{/} {mark}[gn_store_owner_name]{/} says; {say}Yes it was but it turned out OK. So how did you get your shop started?{/} I tell her; {mcsay}I flunked out of school so my parents gave me a little money and threw me out of the house so I used the money to open my shop.{/} She says; {say}That was pretty smart of you.{/}"
  choice("fwb_event5_bar10") "Continue"
  return

label fwb_event5_bar10:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_77"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_78"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "We spend time getting to know each other and having a couple more drinks. I'm having a great time and it seems like she is too, at least I hope she is. The local bar is a much better place for us than downtown, no one is going to come over and give us a hard time about anything. It's loud in here but we barely notice."
  ""
  "After some time I notice that {mark}[gn_store_owner_name]{/} is getting a tired so I say; {mcsay}Hey, it been great but I can see you're getting a little tired, let me walk you home.{/} She replies; {say}I guess you're right, I hate to end the evening but I am tired.{/} We get up and walk arm in arm out of the bar."
  choice("fwb_event5_apartment1") "Continue"
  return

label fwb_event5_apartment1:              ## date moves to Ruthie's apartment
  $game.location="store_owner_apartment"
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_79"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_80"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "When we reach {mark}[gn_store_owner_name]'s{/} apartment building she looks down shyly and says; {say}Would you like to come inside?{/} I think she's sending me a message that I'm happy to hear; {mcsay}I'd love to, thanks for inviting me.{/}"
  ""
  "We go inside and make our way through the building to her apartment. She goes inside and turns around looking really embarrassed. It's not a great apartment and it's incredibly small. She says; {say}This is it, I know it's not much but it's home.{/} Trying to hide my surprise I go inside and she shuts the door behind me. I tell her; {mcsay}Hey, I'm living in my shop. We're both struggling a bit now but someday it will get better for both of us.{/}"
  choice("fwb_event5_apartment2") "Continue"
  return

label fwb_event5_apartment2:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_81"
  "I wasn't wrong about the message. {mark}[gn_store_owner_name]{/} moves closer and at first our kisses are gentle but soon we're both topless."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Our kisses get more and more passionate and before long {mark}[gn_store_owner_name]{/} breaks the embrace to fold down her small bed."
  choice("fwb_event5_apartment3") "Continue"
  return

label fwb_event5_apartment3:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_82"
  "I kneel in front of {mark}[gn_store_owner_name]{/} so I can play with her tits and suck on her nipples. This is so much more exciting than sex with bots!"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She begins moaning in pleasure which makes me happy because it's genuine. When bots moan it's just their training and doesn't mean anything."
  choice("fwb_event5_apartment4") "Continue"
  return

label fwb_event5_apartment4:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_83"
  "I'm encouraged by {mark}[gn_store_owner_name]'s{/} response to my lips and tongue on her tits so I move down and start licking her pussy."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She gets louder as my tongue plays with her clit. Her juices tastes different from the fluids used in bots and are much more exciting."
  choice("fwb_event5_apartment5") "Continue"
  return

label fwb_event5_apartment5:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_84"
  "After a few minutes {mark}[gn_store_owner_name]{/} stops me and says; {say}Stand up, it's my turn.{/} She sits up and begins kissing and licking my cock."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Soon she takes my cock into her mouth. It feels fantastic as she moves her mouth up and down on my cock and uses her tongue on the underside."
  choice("fwb_event5_apartment6") "Continue"
  return

label fwb_event5_apartment6:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_210"
  "After a few minutes we both realize it's time for the real thing. We're both a little nervous but we're too excited to let that stop us."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I enter {mark}[gn_store_owner_name]{/} slowly and carefully, I don't want to hurt her. In a few minutes she's encouraging me to ge faster and harder."
  choice("fwb_event5_apartment6b") "Continue"
  return

label fwb_event5_apartment6b:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_85"
  "This is so different from sex with bots, it feels great and it's exciting to know that {mark}[gn_store_owner_name]'s{/} response is real."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "We're both too excited to last long and soon we both cum at the same time. When our orgasms subside we're both sweaty, exhausted and happy."
  choice("fwb_event5_apartment7") "Continue"
  return

label fwb_event5_apartment7:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_86"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_87"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "Afterwards we cuddle together on {mark}[gn_store_owner_name]'s{/} tiny bed for awhile and it feels wonderful."
  "{size=-6} "
  "I have to tell her; {mcsay}That was amazing, this night has been wonderful.{/} She replies; {say} I've been looking forward to this and it was even better than I imagined.{/}"
  "{size=-6} "
  $mc.mood.give_xp(randint(50,60))                  ## extra large mood increase
  "{size=-6} "
  "Her bed is too small for both of us so I say; {mcsay}I'm sorry, I have to head home now.{/} and she replies; {say}I understand, my place is too small for me to ask you to stay over.{/} I get dressed and she throws on a robe and we share one more kiss before I leave."
  choice("fwb_event5_walkinghome1") "Continue"
  return

label fwb_event5_walkinghome1:
  $game.location="neighborhood"      ## walking home is in neighborhood
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "[neighborhood]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_88"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_89"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{mark}[gn_store_owner_name]{/} watches me walk down the hall to leave her apartment building. I'm thinking that her apartment is really small and it's not fair that she has to live like that. My place is nothing great but it's more comfortable than hers."
  ""
  "Maybe I'll have to invite her to stay over at my place, at least my bed is big enough for both of us."
  ""
  "I wonder what it would cost to get her a better apartment. She deserves better than this. My shop is doing OK, if it's not too expensive maybe I can help her out."
  $global fwb_first_sex
  $fwb_first_sex=1             ## set flag to change text in 'flirting' relationship
  $global mc_so_value
## 0.11.3 increased the minimum value after losing virginity to 'Flirting' mid point (was 35)
  if mc_so_value<45:                                          ## must be at least 45 (mid level 'Flirting') after 1st sex
     $temp_int=45-mc_so_value                                 ## increase it to 45
     call mc_update_relation(gn_store_owner_name,temp_int,0)  ## great date, relationship gain to at least 35
  elif mc_so_value<55:                                        ## do NOT allow FWB until quest end
    call mc_update_relation(gn_store_owner_name,5,0)          ## great date, relationship gain if between 45 and 54
  choice("fwb_event5_arrivedhome") "Continue"
  return

label fwb_event5_arrivedhome:  ## don't change game_location until after this function but use home background
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_90"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_91"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "As I reach the shop I realize I'm pretty tired. Our date took longer than I expected but I'm certainly not complaining. I know I've had lots of sex with bots but I'm finally no longer a virgin! I can't believe my first time was with a beautiful woman like {mark}[gn_store_owner_name]{/}."
  ""
  "Inside the shop I have a little energy left to do some work but before I get started I realize I have two things I have to think about: deciding if I want to accept {mark}[ns_teacher_name]'s{/} partnership offer and finding out if I can afford to help {mark}[gn_store_owner_name]{/} move into a better place."
  ""
  if mc.energy>=2:
    $mc.energy=2
  $quests.fwbenefits.advance()
  choice("goto_home") "Continue"
  return

##===== Event 6 =====

label quest_fwbenefits_event6:      ## AFTERNOON: think about upgrading Ruthie's apt., go to store to tell her
  $global fwb_show_upgrade_message
  if fwb_show_upgrade_message==0:   ## first time requires 2 extra screens with full analysis
    $fwb_show_upgrade_message=1     ## increment flag to avoid repeat
    $global fwb_date_available
    $fwb_date_available=1           ## when event 6 starts you can date Ruthie every night if you want to
    call fwb_event6_cost1
  else:
    call fwb_event6_upgrade1
  return

label fwb_event6_cost1:
  $game_bg="home bg"    ## decision to upgrade Ruthie's apartment is made at home
  $game_bgm="home bgm"
  header "Upgrading {mark}[gn_store_owner_name]'s{/} Apartment"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_92"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_93"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "Before I get started in the shop I decide to look for apartments for {mark}[gn_store_owner_name]{/}. She needs to be near her store and I want her to be near me too. Her current building is in a good location, I wonder if it has any nicer apartments in it."
  ""
  "It turns out that the top floor in her building has nicer places. They have 2 rooms so she wouldn't need to rent a second room for the bot capsules and they have a separate entrance with a doorman."
  ""
  "The rent is {mark}$10,000 per week{/}, that's a lot of money but maybe it can work. The living room looks decent and has large windows. Since it's on the top floor the view is pretty good."
  choice("fwb_event6_cost2") "Continue"
  return

label fwb_event6_cost2:
  $game_bg="home bg"    ## decision to upgrade Ruthie's apartment is made at home
  $game_bgm="home bgm"
  header "Upgrading {mark}[gn_store_owner_name]'s{/} Apartment"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_94"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_95"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "The bedroom looks OK too, let's hope I spend some time there with her! I'm sure she'd like a real bathroom instead of that combination sink-shower-toilet that takes up almost half of her room."
  ""
  "Right now her two rooms are $1,250 per week each so she's paying {mark}$2,500 per week{/}. Maybe I could pay the difference which is {mark}$7,500 per week{/}. To rent the place they want 1 week's rent in advance plus prorated rent if you move in before Monday, a security deposit, and she'd need some money for furnishings too."
  ""
  "I'm going to think about this for a few days. If I decide to help her out this would be a good way to do it."
  choice("<<<") "Continue"
  return

label fwb_event6_upgrade1:  ## decide to pay for Ruthie's upgraded apartment
  $game_bg="home bg"        ## decision to upgrade Ruthie's apartment is made at home
  $game_bgm="home bgm"
  header "Upgrading {mark}[gn_store_owner_name]'s{/} Apartment"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_96"
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  "I've researched the top floor apartments in {mark}[gn_store_owner_name]'s{/} building, now I need to decide if I can afford to do this for her."
  "{size=-22} "
  "{good}The most important thing is that I'll have to pay $7,500 rent for her every Monday.{/}"
  "{size=-22} "
  "She's already paid this week's rent so upgrading her apartment today at the full {mark}$10,000 rent{/} would cost:"
  "{size=-22} "
  ## Calculate cost
  if now("sunday"):
    $initial_rent=31429  ## 10000 per week: 8 days rent, deposit-5000, and furnishings-15000
    "8 days rent $11,439"
    "Deposit $5,000"
    "Furnishings $15,000"
    "{good}Total $31,429{/}"
  elif now("monday"):
    $initial_rent=40000  ## 14 days
    "14 days rent $20,000"
    "Deposit $5,000"
    "Furnishings $15,000"
    "{good}Total $40,000{/}"
  elif now("tuesday"):
    $initial_rent=38574  ## 13 days
    "13 days rent $18,574"
    "Deposit $5,000"
    "Furnishings $15,000"
    "{good}Total $38,574{/}"
  elif now("wednesday"):
    $initial_rent=37145  ## 12 days
    "12 days rent $17,145"
    "Deposit $5,000"
    "Furnishings $15,000"
    "{good}Total $37,145{/}"
  elif now("thursday"):
    $initial_rent=35716  ## 11 days
    "11 days rent $15,716"
    "Deposit $5,000"
    "Furnishings $15,000"
    "{good}Total $35,716{/}"
  elif now("friday"):
    $initial_rent=34287  ## 10 days
    "10 days rent $14,287"
    "Deposit $5,000"
    "Furnishings $15,000"
    "{good}Total $34,287{/}"
  elif now("saturday"):
    $initial_rent=32858  ## 9 days
    "9 days rent $12,858"
    "Deposit $5,000"
    "Furnishings $15,000"
    "{good}Total $32,858{/}"
  "{size=-22} "
  "{mark}This is a big committment, should I do it?{/}"
  choice("fwb_event6_upgrade2",cost=[("money",initial_rent)]) "Yes"
  choice("<<<") "No"

## 0.14 temporary situation: after selling 2 luxury bots in 'Business Partners' force MC to pay for Ruthie's apartment upgrade (you've received $1,925,000 already)
## 0.15 will revert to allowing you to refuse but you won't like the consequences!
##  if bp_force_store_owner_rent==0 or mc.money<50000:                 
##    choice("<<<") "No" 
##  else:
##    "{size=-16} "
##    "{good}(Version 0.14 - You partnership earnings have been at least $1,925,000 so 'No' is no longer available.){/}"
##    choice(None) "No"
  return

label fwb_event6_upgrade2:       ## upgrade Ruthie's apartment
  $game.location="corner_store"  ## go to store to tell Ruthie about it
  $temp_int=random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"

  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  ""
  $action_image= "quests friends_with_benefits fwb_97"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_98"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "After paying the money to upgrade {mark}[gn_store_owner_name]'s{/} apartment I decide to walk over to her store to tell her about it. It's always nice to see her and I'm sure the new apartment will be a pleasant surprise."
  ""
  ""
  ""
  "When I get there I can't believe her store is empty again! How do I get so lucky? She's happy to see me and we great each other with a warm hug and a passionate kiss."
  choice("fwb_event6_upgrade3") "Continue"
  return

label fwb_event6_upgrade3:
  $temp_int=random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_99"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_100"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "We sit down at the counter in her store and I say; {mcsay}I've got some big news for you.{/} {mark}[gn_store_owner_name]{/} reacts playfully; {say}What, did you win the lottery?{/}"
  ""
  "I reply; {mcsay}No but in a way you did...{/} and I tell her all about her new apartment and how I'll pay the difference so her rent won't change."
  ""
  "At first she's excited but then I see her mood change; {say} I can't accept this, you don't need to do it and I can take care of myself.{/}"
  ""
  "I need to be careful so I say; {mcsay}I know you can take care of yourself and you run your own store so you have every right to be proud of what you've accomplished.{/}"
  choice("fwb_event6_upgrade4") "Continue"
  return

label fwb_event6_upgrade4:  ## upgrade Ruthie's apartment
  $temp_int=random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_101"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_102"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "I decide to try a different approach so I say playfully; {mcsay}Hey, this is really for me. I don't want to visit you in that tiny place. You need a better place to entertain me!{/}"
  ""
  "Her mood starts to change and she responds; {say}You're such an idiot, that's crazy. You've already given me bots, isn't this too much?{/} I reply more seriously; {mcsay}No it's not too much. I want you to be happy and my shop is doing well enough to afford it so please accept this.{/}"
  ""
  "{mark}[gn_store_owner_name]{/} considers it and then as she gets up to give me a kiss she says; {say}OK, thank you for helping me out but from now on drinks at the bar will be on me.{/}"
  choice("fwb_event6_upgrade5") "Continue"
  return

label fwb_event6_upgrade5:
  $temp_int=random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_103"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_104"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "I'm glad she accepts it and say; {mcsay}OK, drinks on you. You know, it's a good thing you accepted it because I've already paid for it.{/} She gives me a look that makes me get up and start to run."
  "{size=-10} "
  "She pretends to be mad and comes after me saying; {say}You better run, if I get my hands on you you'll be black and blue all over for weeks!{/}"
  "{size=-10} "
  "As I run away I call out to her; {mcsay}I have to get back to work but since you already live in the building the penthouse entrance and your apartment are already programmed to recognize you.{/}"
  "{size=-10} "
  $mc.mood.give_xp(randint(6,12))                  ## small mood increase
  $global fwb_delay_days
  $fwb_delay_days=1                 ## Ruthie needs time to move and set up her new apartment
  $global fwb_pay_rent
  $fwb_pay_rent=1                   ## set flag to start putting Ruthie's rent on the left side info screen
  $global fwb_date_available
  $fwb_date_available=0             ## temporarily clear flag, no dates while Ruthie is moving
  $global mc_so_value
  if mc_so_value<45:                                  ## do NOT allow FWB until quest end
    call mc_update_relation(gn_store_owner_name,1,0)  ## she accepted new apartment, relationship gain
  $quests.fwbenefits.advance()      ## advance quest
  choice("goto_home") "Continue"
  return

##===== Event 7 =====

label quest_fwbenefits_event7:  ## AFTERNOON: Ruthie drops by in morning to invite you over tonight to new apartment
  $game_bg="home bg"            ## at home
  $game_bgm="home bgm"
  header "[home]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_105"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_106"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "While I'm working in the shop I hear the door and see {mark}[gn_store_owner_name]{/} coming in. I stop working and walk over to greet her with a hug."
  ""
  "She's excited as she tells me; {say}I've been busy moving into my new apartment. The bots helped me move my things and the last tenant left some furniture behind which I'll use. They also left other stuff behind that I have to go through but it's beginning to feel like home.{/}"
  ""
  "I say; {mcsay}That's great, I can't wait to see it.{/} She smiles; {say}That's why I'm here, please come over tonight and I'll give you a tour...{/} Then she adds in a sultry voice; {say}...and maybe we can break in my new bed.{/}"
  choice("fwb_event7_invite1") "Continue"
  return

label fwb_event7_invite1:  ## Full Event: Ruthie drops by in morning to invite you over tonight to new apartment
  $game_bg="home bg"       ## at home
  $game_bgm="home bgm"
  header "[home]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_107"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_108"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "I say; {mcsay}I'm glad you like it and are getting comfortable.{/} Then I add playfully; {mcsay}With an invitation like that how could I possibly refuse? I'm already looking forward to it.{/}"
  "{size=-6} "
  "{mark}[gn_store_owner_name]{/} smiles and says; {say}Me too!{/} Then she says; {say}Sorry, I have to get back to the store now, I'll see you tonight.{/}"
  "{size=-6} "
  "I follow her to the door and before she walks out she turns and gives me a passionate kiss and says; {say}That was only a teaser!{/} and then she turns and leaves."
  "{size=-6} "
  $mc.mood.give_xp(randint(6,12))                     ## small mood increase
  $global mc_so_value
  if mc_so_value<45:                                  ## do NOT allow FWB until quest end
    call mc_update_relation(gn_store_owner_name,1,0)  ## she invited, you accepted, relationship gain
  $quests.fwbenefits.advance()      ## advance quest
  choice("goto_home") "Continue"
  return

##===== Event 8 =====

label quest_fwbenefits_event8:  ## NIGHT: First booty call at Ruthie's new apartment
  $game.location="store_owner_apartment"
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_109"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_110"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "I walk to {mark}[gn_store_owner_name]'s{/} building and go in the entrance to the penthouse apartments. There's a doorman who looks me over and nods. I guess {mark}[gn_store_owner_name]{/} let him know I'm coming."
  ""
  "I go up the elevator to the top floor and she's waiting for me, I guess the doorman let her know I was coming. As soon as I'm inside her apartment {mark}[gn_store_owner_name]{/} jumps into my arms for a greeting hug and kiss. I could get used to greetings like this."
  ""
  "When I set her down she asks excitedly; {say}Are you ready for the tour?{/} I smile at her excitement and say; {mcsay}Lead on!{/}"
  choice("fwb_event8_date1") "Continue"
  return

label fwb_event8_date1:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_111"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_112"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "First {mark}[gn_store_owner_name]{/} shows me the bedroom so I can see where she's keeping the bot capsules. She says; {say}It was a little creepy staring at them all night so I got this room divider to hide them.{/} I reply; {mcsay}Good idea, that would be a little creepy.{/}"
  ""
  ""
  "Next she's really excited to show me the bathroom; {say}I'm so happy to have a real bathroom instead of that combo unit in the old place.{/} It's good to see her so happy; {mcsay}That thing was sort of weird wasn't it.{/}"
  choice("fwb_event8_date2") "Continue"
  return

label fwb_event8_date2:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_113"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_114"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "When we return to the living room she's got a bottle of wine on the table and a couple of glasses. I propose a toast; {mcsay}To{/} {mark}[gn_store_owner_name]{/} {mcsay}and her new apartment, may you be together for a long time.{/}"
  ""
  "After we take a couple of sips she climbs into my lap and says; {say}Thank you for making this possible.{/} I reply; {mcsay}You've made it look like home with the plants all around and I recognized a few pictures from your old apartment.{/}"
  ""
  "She leans into me and we share a long kiss and lose track of everything except each other."
  choice("fwb_event8_date3") "Continue"
  return

label fwb_event8_date3:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_115"
  "Our passion grows and we start undressing each other right there on the couch. When I see her tits I can't resist and start caressing them."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I lean forward and use my lips and tongue on her nipples while continuing to caress her tits. She grabs my head and moans in pleasure."
  choice("fwb_event8_date4") "Continue"
  return

label fwb_event8_date4:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_116"
  "Her strong response entices me to move down and use my tongue on her pussy and clit. She pulls my hair and cries out; {say}Yes! Don't stop!{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Her loud cries and gasps encourage me to continue. With the way she tastes and how her body responds I could keep this up all night."
  choice("fwb_event8_date5") "Continue"
  return

label fwb_event8_date5:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_117"
  "She says; {say}My turn, stand up.{/} At first I'm reluctant but then I realize what she's going to do and how it will feel so I stand up."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She takes my cock into her warm, wet mouth while caressing my balls and I put my hand on {mark}[gn_store_owner_name]'s{/} head but there's no need for force."
  choice("fwb_event8_date6") "Continue"
  return

label fwb_event8_date6:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_118"
  "After a while we decide to move into her bedroom. {mark}[gn_store_owner_name]{/} lies on the bed and I get on top, she's so wet that my cock slides in easily."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "We enjoy each other in missionary position like we did the first time in her old apartment. It feels just as good but I think we'll last longer this time."
  choice("fwb_event8_date7") "Continue"
  return

label fwb_event8_date7:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_119"
  "{mark}[gn_store_owner_name]{/} says; {say}Let me get on top for a while.{/} I lie on the bed and say; {mcsay}Your ride awaits my lady.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She smiles and lowers herself onto my cock. She's wet and it slides in easily. We hold hands as she starts riding me enthusiastically."
  choice("fwb_event8_date8") "Continue"
  return

label fwb_event8_date8:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_120"
  "She starts to tire so I say; {mcsay}I'm going to cum soon, let's switch to doggy.{/} {mark}[gn_store_owner_name]{/} looks surprised but eagerly gets on her hands and knees."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I push my cock deep into her and begin thrusting rapidly. Soon she cries out; {say}I'm cumming!{/} and I make one last deep, hard thrust and cum too."
  choice("fwb_event8_date9") "Continue"
  return

label fwb_event8_date9:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $action_image= "quests friends_with_benefits fwb_121"
  "Afterwards we're content but exhausted. I tell her; {mcsay}That was wonderful, you make me feel so good.{/} She replies; {say}It was amazing, thank you."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "After a while {mark}[gn_store_owner_name]{/} says; {say}We're both tired, you should sleep here tonight.{/}"
  "{size=-22} "
  $mc.mood.give_xp(randint(30,50))                           ## large mood increase
  $global fwb_mc_old_clothes
  $fwb_mc_old_clothes=1                                      ## set flag so you put on old clothes when you get up
  $global fwb_upgrade_done
  $fwb_upgrade_done=1                                        ## nightly dates can now happen at Ruthie's place
  $global fwb_date_available
  $fwb_date_available=1                                      ## set flag to allow dates again
  $global mc_so_value
  $local_diff=77-mc_so_value                                 ## 0.11.3 force to FWB midpoint of 80, increased to 77 now and waking up together is always +3
  call mc_update_relation(gn_store_owner_name,local_diff,0)  ## you are friends with benefits by definition
  $quests.fwbenefits.finish()                                ## finish quest
##  choice("back_at_the_shop:away") "Sleep"
  choice("sleep_after_date:away") "Sleep"
  return

##===== Nightly Date with Ruthie =====

label fwb_ask_ruthie_date:
  $game_bg="home bg"      ## ask for date done at home
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(1,100)
  $ruthie_answer=0
  $global fwb_already_asked
  $fwb_already_asked=now.day  ## you pressed the button to ask, don't allow it to be pressed again on same day
  $global fwb_next_date
  if fwb_next_date==1:        ## fall through when fwb_next_date=-1: 'ruthie_answer' = 0
    if temp_int<=85:
      $ruthie_answer=1
  elif fwb_next_date==0:
    if temp_int<=65:
      $ruthie_answer=1
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_133"
  center "{image=[action_image]@400x600}"
  ""
  if ruthie_answer==1:
    $action_image= "quests friends_with_benefits fwb_134"
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    "I'd like to see {mark}[gn_store_owner_name]{/} tonight so I give her a call; {mcsay}Hi {mark}[gn_store_owner_name]{/}, hope you had a good day. I'd love to see you, are you up for a night out at our favorite place?{/}"
    ""
    if random.randint(1,4)==1:    ## she had a bad day
      "{mark}[gn_store_owner_name]{/} sounds frustrated when she replies; {say}Hi{/} {mark}[mc.name]{/}{say}. It was a tough day at the store and I really need a break.{/} {good}Give me a half hour and I'll meet you there.{/}"
      ""
      "I'm sure we can turn her day around; {mcsay}Sorry about your day, I promise to make it better. See you there in a little while.{/} She replies; {say}I'll try to hurry.{/}"
    else:
      "{mark}[gn_store_owner_name]{/} sounds happy when she replies; {say}Hi{/} {mark}[mc.name]{/}{say}. Thanks, that would be a great ending for a good day!{/} {good}Give me a half hour and I'll meet you there.{/}"
      ""
      "I'm glad {mark}[gn_store_owner_name]'s{/} in a good mood; {mcsay}That's great, I'll see you there in a little while and we'll have some fun.{/} She replies; {say}I'll try to hurry.{/}"
    ""
    "After we hang up I get ready to go and then head out to our favorite place."
    choice("fwb_ruthie_date1",cost=[("money",250),("energy",3),("time",0)]) "Continue"
  else:
    $action_image= "quests friends_with_benefits fwb_135"
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    "I'd like to see {mark}[gn_store_owner_name]{/} tonight so I give her a call; {mcsay}Hi {mark}[gn_store_owner_name]{/}, I hope you had a good day. I'd love to see you tonight, are you up for a night out at our favorite place?{/}"
    ""
    if fwb_next_date==1:    ## Ruthie is happy with you - you paid full rent
      "{mark}[gn_store_owner_name]{/} sounds tired when she replies; {say}Hi{/} {mark}[mc.name]{/}{bad}. Thanks for the invite but I'm really tired.{/} {say}I need to go to bed early tonight but I promise to make it up to you.{/}"
      ""
      "Too bad, I was looking forward to seeing her; {mcsay}I'm sorry to hear that but it's OK. Get a good night's sleep and I'll give you a call another night.{/} She replies; {say}Thanks for understanding.{/}"
      ""
      "I hope she was just tired and isn't angry with me for some reason."
    elif fwb_next_date==0:  ## Ruthie is a frustrated with you - you paid half rent
      "{mark}[gn_store_owner_name]{/} sounds upset when she replies; {say}Hi{/} {mark}[mc.name]{/}{bad}. Sorry, I'm not in the mood tonight and I wouldn't be any fun.{/} {say}I think I'll just go to bed early tonight.{/}"
      ""
      "Something is bothering her; {mcsay}I'm sorry to hear that but it's OK. Get a good night's sleep and I'll give you a call another night.{/} She replies; {say}Thanks for understanding.{/}"
      ""
      "This isn't like her, maybe she's upset with me because I paid only half the rent I promised."
    else:                   ## Ruthie is angry with you - you did not pay any rent
      "{mark}[gn_store_owner_name]{/} sounds angry when she replies; {bad}Hi{/} {mark}[mc.name]{/}{bad}. Not tonight, I've been working extra hard trying to make the rent payment. Maybe some other time.{/}"
      ""
      "She's angry with me; {mcsay}I'm sorry, I really messed up. I promise to get back on track next week.{/} She replies; {bad}I hope you keep your promise, I can't afford this place by myself.{/}"
      ""
      "I feel bad about breaking my promise to {mark}[gn_store_owner_name]{/}. I better fix this next week."
    choice("<<<") "Continue"
  return

## Date Revision Start

label fwb_ruthie_date1:           ## meet Ruthie at bar - 0.15 ADD SKIP SCENE BUTTON
  $global fwb_mc_new_clothes      ## need to read flag
  $global fwb_first_new_clothes   ## need to read flag

## 0.15.n obsolete variable and add reset counter for Ruthie dates
##  $global fwb_last_date

## 0.15.n reset counter for Ruthie dates
  $global mc_so_date_counter
  $mc_so_date_counter=0                              ## reset counter

## 0.15.n obsolete variable
##  $fwb_last_date=0                ## reset counter for last date to 0 since we're on a date
  
##  $print "Day: ",now.day," On a date and reset date counter: ",fwb_last_date
  
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  ""  ## space after money deducted
  if fwb_mc_new_clothes==0:
    $action_image= "quests friends_with_benefits fwb_136"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_137"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests friends_with_benefits fwb_141"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_142"
    center "{image=[action_image]@400x600}"
  ""
  ##  TEXT - CHANGES DEPENDING UPON CLOTHES SITUATION
  $act.set_block("c")
  ""  ## space after money deducted
  if fwb_mc_new_clothes==0 or fwb_first_new_clothes==0:       ## text same in old and new clothes except first time wearing new clothes
    ""
    "When I get to the local bar {mark}[gn_store_owner_name]{/} isn't there yet so I decide to sit down at the bar and order a beer. I enjoy talking with the bartender while I'm waiting."
    ""
    ""
    "After a few minutes {mark}[gn_store_owner_name]{/} arrives and I stand up to greet her with a kiss; {mcsay}Hi! You look great, ready for a good time?"
    ""
    "{mark}[gn_store_owner_name]{/} replies happily; {say}I sure am, let's head over to our usual table.{/}"
  else:                                                       ## must be fwb_mc_new_clothes==1 and fwb_first_new_clothes==1
    $fwb_first_new_clothes=0                                  ## clear flag for future dates with new clothes
    "Everyone is surprised when I walk in wearing different clothes. When I sit down at the bar to wait for {mark}[gn_store_owner_name]{/} the bartender teases me about the new clothes."
    ""
    ""
    "After a few minutes {mark}[gn_store_owner_name]{/} arrives and I stand up to greet her with a kiss; {mcsay}Hi! You look great, ready for a good time?"
    ""
    "{mark}[gn_store_owner_name]{/} replies happily; {say}I like your new look, what a nice surprise!{/}"
  choice("fwb_ruthie_date2") "Continue"
## 0.15 ADD SKIP SCENE BUTTON, 
  choice("fwb_ruthie_date_skip", pos=17) "Skip Scene"
  return

## 0.15 insert function to handle skip scene outcomes
## NEED TO ADD RELATIONSHIP POINT GAIN OR LOSS

label fwb_ruthie_date_skip:       ## - Skip scene requires a function to determine which outcome actually happened:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "Skipped Date Scene with {mark}[gn_store_owner_name]{/}: Outcome ..."
  $temp_int=random.randint(1,10)
  $global fwb_upgrade_done
  if fwb_upgrade_done==0:  ## BEFORE updrading Ruthie's apartment
    "You had a great time with {mark}[gn_store_owner_name]{/} at the local bar."
    ""
    if temp_int<=5:        ## 50% of the time she sleeps over at your shop
      "At the end of the night you invited {mark}[gn_store_owner_name]{/} to sleep over at your shop and {good}you had a great night together{/}."
      "{size=-16} "
      $mc.mood.give_xp(randint(36,62))                  ## large mood increase for date plus small mood increase for waking up together
      ""
      "{mark} Back at your workshop while you were enjoying your date:"
      ""
      call role_mission_manager_schedule
      $global mc_so_value  
      if quests.fwbenefits.finished or mc_so_value<45:   ## if quest done OR below midpoint of 'Flirting'
        call mc_update_relation(gn_store_owner_name,3,0)
      $now.advance()             ## advance time so you get up in the morning  
      choice("sleep_after_date2") "Continue"
    else:
      if temp_int<=8:        ## 30% of the time you ask and she says "NO"
        "At the end of the night you invited {mark}[gn_store_owner_name]{/} to sleep over at your shop {bad}but she said no{/}. You walked her home and seeing her apartment building reminded you about her tiny apartment."
      else:                  ## 20% of the time you're too scared to ask
        "At the end of the night {bad}you were too afraid to ask{/} {mark}[gn_store_owner_name]{/} to sleep over so you just walked her home. Seeing her apartment building reminded you about her tiny apartment."  
      ""
      "Since the night was shorter than you hoped it would be you have some time to work."
      "{size=-16} "
      "{size=-8}{info}Received 1 AP{/}{/}"
      $mc.energy+=1    ## get 1 of the 3 AP back
      choice("goto_home") "Continue"
  else:                    ## AFTER upgrading Ruthie's apartment
    if temp_int<=7:        ## 70% chance you sleep over at her apartment
      "{mark}[gn_store_owner_name]{/} invited you for a sleep over at her apartment and you had a great night together."
      $mc.mood.give_xp(randint(36,62))                  ## large mood increase for date plus small mood increase for waking up together
      "{mark} Back at your workshop while you were enjoying your date:"
      ""
      call role_mission_manager_schedule
      $global mc_so_value  
      if quests.fwbenefits.finished or mc_so_value<45:   ## if quest done OR below midpoint of 'Flirting'
        call mc_update_relation(gn_store_owner_name,3,0)
      $now.advance()             ## advance time so you get up in the morning  
      choice("sleep_after_date2") "Continue"
    else:                  ## 30% chance she sleeps over at your shop
      "You invited {mark}[gn_store_owner_name]{/} for a sleep over at your shop and you had a great night together."
      "{size=-16} "
      $mc.mood.give_xp(randint(36,62))                  ## large mood increase for date plus small mood increase for waking up together
      ""
      "{mark} Back at your workshop while you were enjoying your date:"
      ""
      call role_mission_manager_schedule
      $global mc_so_value  
      if quests.fwbenefits.finished or mc_so_value<45:   ## if quest done OR below midpoint of 'Flirting'
        call mc_update_relation(gn_store_owner_name,3,0)
      $now.advance()             ## advance time so you get up in the morning  
      choice("sleep_after_date2") "Continue"
  return

## end of inserted function for skipping scene

label fwb_ruthie_date2:           ## meet Ruthie at bar
  $global fwb_mc_new_clothes      ## need to read flag
  $global fwb_upgrade_done
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  if fwb_mc_new_clothes==0:
    $action_image= "quests friends_with_benefits fwb_138"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_139"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests friends_with_benefits fwb_143"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_144"
    center "{image=[action_image]@400x600}"
  $temp_int=random.randint(1,10)
  if fwb_upgrade_done==0:                                  ## path before upgrading her apartment
    ##  TEXT - SAME IN BOTH OLD AND NEW CLOTHES
    $act.set_block("c")
    "We sit down at your usual table and talk about what each of us has been doing. Since we both run our own businesses there's always something interesting to talk about."
    ""
    "While we're enjoying our conversation I order a couple of rounds of drinks and time passes quickly. {mark}[gn_store_owner_name]{/} is easy to talk with and we're both having a good time."
    ""
    if temp_int<=8:    ## 80% chance you ask Ruthie to come home with you
      $temp_int=random.randint(1,4)
      if temp_int<=5:  ## 50% chance you ask and she says yes
        "When the second round of drinks is finished I ask {mark}[gn_store_owner_name]{/}; {mcsay}I'd love to continue our evening a little more privately,{/} {good}would you like to come to my place tonight?{/} She replies; {say}Sounds nice,{/} {good}lead the way.{/}"
        choice("fwb_ruthie_home_sleep1") "Continue"
      else:            ## 30% chance you ask and she says no
        "When the second round of drinks is finished I ask {mark}[gn_store_owner_name]{/}; {mcsay}I'd love to continue our evening a little more privately,{/} {good}would you like to come to my place tonight?{/} She replies; {say}I'm sorry{/} {mark}[mc.name]{/}{bad}, not tonight.{/}"
        choice("fwb_ruthie_date2b") "Continue"
    else:              ## 20% chance you don't ask Ruthie to come home with you
      "After the drinks {bad}I'm too nervous to ask her to come over tonight{/} so I say; {mcsay}I had a wonderful time tonight{/} {mark}[gn_store_owner_name]{/}, {mcsay}I'm glad we did this but I think it's time I walk you home.{/} She replies; {say}I had a great time too, let's do it again soon.{/}"
      choice("fwb_ruthie_date2b") "Continue"
  elif temp_int<=3:                       ## after upgrdading apartment: 30% chance go to MC's place
    if fwb_mc_new_clothes==0:
      $action_image= "quests friends_with_benefits fwb_139"
    else:
      $action_image= "quests friends_with_benefits fwb_144"
    center "{image=[action_image]@400x600}"
    ##  TEXT - SAME IN BOTH OLD AND NEW CLOTHES
    $act.set_block("c")
    "We sit down at your usual table and talk about what each of us has been doing. Since we both run our own businesses there's always something interesting to talk about."
    ""
    "While we're enjoying our conversation {mark}[gn_store_owner_name]{/} orders a couple of rounds of drinks and time passes quickly. {mark}[gn_store_owner_name]{/} is easy to talk with and we're both having a good time."
    ""
    "When the second round of drinks is finished I ask {mark}[gn_store_owner_name]{/}; {mcsay}I'd love to continue our evening a little more privately, would you like to come to my place tonight?{/} She replies; {say}Of course, lead the way.{/}"
    choice("fwb_ruthie_home_sleep1") "Continue"
  else:                                  ## after upgrading apartment: 70% chance go to Ruthie's place
    if fwb_mc_new_clothes==0:
      $action_image= "quests friends_with_benefits fwb_140"
    else:
      $action_image= "quests friends_with_benefits fwb_145"
    center "{image=[action_image]@400x600}"
    ##  TEXT - SAME IN BOTH OLD AND NEW CLOTHES
    $act.set_block("c")
    "We sit down at our usual table and talk about what each of us has been doing. Since we both run our own businesses there's always something interesting to talk about."
    ""
    "While we're enjoying our conversation {mark}[gn_store_owner_name]{/} orders a couple of rounds of drinks and time passes quickly. I really enjoy her company."
    ""
    "After the second round of drinks I learn that {mark}[gn_store_owner_name]{/} is enjoying herself too; {say}I think it's time we take this party to my place, what do you think?{/} I reply; {mcsay}Great idea, let's go.{/}"
    choice("fwb_ruthie_away_sleep1") "Continue"
  return

label fwb_ruthie_date2b:            ## only used when asking for dates when the quest isn't finished yet
  $game.location="neighborhood"     ## walking Ruthie home
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  if fwb_mc_new_clothes==0:
    $action_image= "quests friends_with_benefits fwb_212"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_90"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests friends_with_benefits fwb_214"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_215"
    center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "We leave the bar and walk to {mark}[gn_store_owner_name]'s{/} apartment building. As we near the building she says: {say}Thanks for walking me home.{/} I reply: {mcsay}Of course, my pleasure.{/}"
  ""
  ""
  "While I'm walking home I can't help thinking about that ugly, tiny apartment she lives in. {mark}Should I do something about it?{/}"
  ""
  "It turned out {mark}the night was shorter than I hoped it would be{/}, maybe I can work a little before going to bed."
  "{size=-16} "
  "{size=-8}{info}Received 1 AP{/}{/}"
  $mc.energy+=1    ## get 1 of the 3 AP back
  choice("goto_home") "Continue"
  return

##===== Sleep with Ruthie at MCs place =====

label fwb_ruthie_home_sleep1:  ## Ruthie spends the night at your place
  $global fwb_mc_new_clothes   ## need to read flag
  $game.location="home"
  $game_bg="home bg"    ## home (bedroom would have unlikely exercise equipment issue)
  $game_bgm="home bgm"
  header "[home]"
## 0.15.n Ruthie anal flag not set yet, first day it's possible was set when you had anal with Simone, and you've reached that day
  $global sd_ruthie_anal_day
  $global fwb_anal_ok
  if fwb_anal_ok==0 and sd_ruthie_anal_day>0 and now.day>=sd_ruthie_anal_day:
    $fwb_anal_ok=1
## 0.15.n reset counter for number of times you have sex this date, 3 is the limit
  $global fwb_sex_count
  $fwb_sex_count=0
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  if fwb_mc_new_clothes==0:
    $action_image= "quests friends_with_benefits fwb_146"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_148"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests friends_with_benefits fwb_147"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_149"
    center "{image=[action_image]@400x600}"
  ##  TEXT - SAME IN BOTH OLD AND NEW CLOTHES
  $act.set_block("c")
  "We walk arm in arm to the front of my workshop. {mark}[gn_store_owner_name]{/} says; {say}I'm glad we're almost there, I can't wait to get inside.{/} I'm anxious too; {mcsay}I've been looking forward to this all night.{/}"
  ""
  ""
  ""
  "Once we're inside we're so hot for each other that we don't even make it to the bedroom before we start undressing each other and kissing passionately. The way we feel we might not make it to the bedroom."
## insert buttons for selecting foreplay on couch or skip
  choice("fwb_couch_hj") "Hand Job"
  choice("fwb_couch_finger") "Finger"
  choice("fwb_couch_sucktits") "Suck Tits"
  choice("fwb_couch_titjob") "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_bedroom_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_bedroom_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_bedroom_69", pos=17) "Go to Bedroom"
  return

label fwb_couch_hj:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(152,153)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I sit down on the couch and {mark}[gn_store_owner_name]{/} kneels next to me and starts playing with my cock."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She leans in and kisses me while stroking my cock which really turns me on and I can't resist holding her head and kissing her back."
  choice(None) "Hand Job"
  choice("fwb_couch_finger") "Finger"
  choice("fwb_couch_sucktits") "Suck Tits"
  choice("fwb_couch_titjob") "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_bedroom_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_bedroom_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_bedroom_69", pos=17) "Go to Bedroom"
  return

label fwb_couch_finger:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(150,151)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "{mark}[gn_store_owner_name]{/} starts to head for the bedroom door but I can't resist grabbing her from behind."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Using both hands I squeeze her breast and finger her pussy. She gasps in surprise but recovers and reaches back to play with my cock."
  choice("fwb_couch_hj") "Hand Job"
  choice(None) "Finger"
  choice("fwb_couch_sucktits") "Suck Tits"
  choice("fwb_couch_titjob") "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_bedroom_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_bedroom_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_bedroom_69", pos=17) "Go to Bedroom"
  return

label fwb_couch_sucktits:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(154,155)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "We sit down together on the couch and I lean over to grab {mark}[gn_store_owner_name]'s{/} breast and suck on her nipple."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She moans in pleasure and to keep up with her I stroke my cock. She watches me for a moment and then says; {say}Hey, that's my toy!{/}"
  choice("fwb_couch_hj") "Hand Job"
  choice("fwb_couch_finger") "Finger"
  choice(None) "Suck Tits"
  choice("fwb_couch_titjob") "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_bedroom_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_bedroom_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_bedroom_69", pos=17) "Go to Bedroom"
  return

label fwb_couch_titjob:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(156,157)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "{mark}[gn_store_owner_name]{/} sits on the couch saying; {say}Come over here, I want to feel your cock between my tits.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I stand in front of her and she wraps her tits around my cock. {mark}[gn_store_owner_name]{/} looks up at me and licks her lips which really turns me on."
  choice("fwb_couch_hj") "Hand Job"
  choice("fwb_couch_finger") "Finger"
  choice("fwb_couch_sucktits") "Suck Tits"
  choice(None) "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_bedroom_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_bedroom_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_bedroom_69", pos=17) "Go to Bedroom"
  return

label fwb_bedroom_bj:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(158,159)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "{mark}[gn_store_owner_name]{/} says; {say}Sit down, I want to suck your cock.{/} I sit on the edge of the bed; {mcsay}Sounds great!{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She kneels in front of me and puts her hands behind her back. I enjoy watching her use only her lips and tongue to work on my cock."
  choice(None) "Blowjob"
  choice("fwb_bedroom_lick") "Eat Pussy"
  choice("fwb_bedroom_69") "69"
  $global fwb_anal_ok
  $global fwb_first_anal
  if fwb_anal_ok==1 and fwb_first_anal==0:                         ## anal was just activated but has NOT happened yet
    choice("fwb_bedroom_anal", pos=17) "Enough Foreplay"
  else:
    if fwb_anal_ok==0:  ## anal not allowed yet
      $temp_int=random.randint(1,4)
    else:               ## anal allowed now
      $temp_int=random.randint(1,5)
    if temp_int==1:
      choice("fwb_bedroom_missionary", pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("fwb_bedroom_cowgirl", pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("fwb_bedroom_doggy", pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("fwb_bedroom_standing", pos=17) "Enough Foreplay"
    else:
      choice("fwb_bedroom_anal", pos=17) "Enough Foreplay"
  return

label fwb_bedroom_lick:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(160,161)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I say playfully; {mcsay}Lie down, I'm hungry and in the mood for a nice juicy pussy.{/} She grins and lies on the bed."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "When I start licking her pussy and clit she grabs my head and says; {say}You really are hungry. Keep going, that feels great.{/}"
  choice("fwb_bedroom_bj") "Blowjob"
  choice(None) "Eat Pussy"
  choice("fwb_bedroom_69") "69"
  $global fwb_anal_ok
  $global fwb_first_anal
  if fwb_anal_ok==1 and fwb_first_anal==0:                         ## anal was just activated but has NOT happened yet
    choice("fwb_bedroom_anal", pos=17) "Enough Foreplay"
  else:
    if fwb_anal_ok==0:  ## anal not allowed yet
      $temp_int=random.randint(1,4)
    else:               ## anal allowed now
      $temp_int=random.randint(1,5)
    if temp_int==1:
      choice("fwb_bedroom_missionary", pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("fwb_bedroom_cowgirl", pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("fwb_bedroom_doggy", pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("fwb_bedroom_standing", pos=17) "Enough Foreplay"
    else:
      choice("fwb_bedroom_anal", pos=17) "Enough Foreplay"
  return

label fwb_bedroom_69:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(162,163)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I say; {mcsay}Let's 69{/} and {mark}[gn_store_owner_name]{/} replies; {say}Great idea! Lie down, I want to be on top.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "We lie down and I grab her ass and use my tongue on her pussy and clit while she takes my cock into her mouth and sucks enthusiastically."
  choice("fwb_bedroom_bj") "Blowjob"
  choice("fwb_bedroom_lick") "Eat Pussy"
  choice(None) "69"
  $global fwb_anal_ok
  $global fwb_first_anal
  if fwb_anal_ok==1 and fwb_first_anal==0:                         ## anal was just activated but has NOT happened yet
    choice("fwb_bedroom_anal", pos=17) "Enough Foreplay"
  else:
    if fwb_anal_ok==0:  ## anal not allowed yet
      $temp_int=random.randint(1,4)
    else:               ## anal allowed now
      $temp_int=random.randint(1,5)
    if temp_int==1:
      choice("fwb_bedroom_missionary", pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("fwb_bedroom_cowgirl", pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("fwb_bedroom_doggy", pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("fwb_bedroom_standing", pos=17) "Enough Foreplay"
    else:
      choice("fwb_bedroom_anal", pos=17) "Enough Foreplay"
  return

label fwb_bedroom_missionary:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(164,165)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "When we're both ready {mark}[gn_store_owner_name]{/} lies on the bed and says; {say}Hurry, I'm ready for you.{/} I'm ready for her too so I get on top."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I enter gently but she wraps her legs around me and squeezes her breast saying; {say}Faster!{/} I speed up and soon we both cum at the same time."
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice(None) "Missionary"
    choice("fwb_bedroom_doggy") "Doggy"
    choice("fwb_bedroom_cowgirl") "Cowgirl"
    choice("fwb_bedroom_standing") "Standing"
    if fwb_anal_ok==1:
      choice("fwb_bedroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_home_sleep5",pos=17) "Exhausted"

  return

label fwb_bedroom_cowgirl:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(166,167)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "When she's ready {mark}[gn_store_owner_name]{/} says playfully; {say}This cowgirl wants to go for a ride tonight!{/} I lie down and she sits on my cock for a ride."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "One of her hands grabs mine and the other squeezes her breast while she rides up and down. She cums first but I'm close behind."
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice("fwb_bedroom_missionary") "Missionary"
    choice("fwb_bedroom_doggy") "Doggy"
    choice(None) "Cowgirl"
    choice("fwb_bedroom_standing") "Standing"
    if fwb_anal_ok==1:
      choice("fwb_bedroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_home_sleep5",pos=17) "Exhausted" 
  
  return

label fwb_bedroom_doggy:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(168,169)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "When I'm ready I say to {mark}[gn_store_owner_name]{/}; {mcsay}Get on your hands and knees, I want you from behind.{/} She smiles at me and gets into position."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I enter her hard but she's wet and my cock goes in easily. I thrust faster and faster before cumming inside her which makes her cum too."
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice("fwb_bedroom_missionary") "Missionary"
    choice(None) "Doggy"
    choice("fwb_bedroom_cowgirl") "Cowgirl"
    choice("fwb_bedroom_standing") "Standing"
    if fwb_anal_ok==1:
      choice("fwb_bedroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_home_sleep5",pos=17) "Exhausted" 

  return

label fwb_bedroom_standing:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(170,171)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I'm surprised when {mark}[gn_store_owner_name]{/} stands up, bends over, and grabs her ass saying; {say}Come here, I want you from behind standing up.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She looks so hot bent over and I can't resist pounding her hard from behind. She cries out when she cums and then I cum too."
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice("fwb_bedroom_missionary") "Missionary"
    choice("fwb_bedroom_doggy") "Doggy"
    choice("fwb_bedroom_cowgirl") "Cowgirl"
    choice(None) "Standing"
    if fwb_anal_ok==1:
      choice("fwb_bedroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_home_sleep5",pos=17) "Exhausted" 

  return

label fwb_bedroom_anal:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(172,173)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  $global fwb_first_anal  ## first time anal with Ruthie flag
  if fwb_first_anal==0:   ## first time with Ruthie
    $fwb_first_anal=1     ## set flag to prevent repeat
    "{mark}[gn_store_owner_name]{/} says shyly; {say}I want to do something special for you, I've heard that guys really like anal so I want to try it.{/}"
    "{size=-22} "
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    "I try to be gentle and slowly push into her tight ass. I know it hurts but she says; {say}It's OK, keep going.{/} After a few more strokes I cum in her ass."
  else:
    "Soon I can't resist asking; {mcsay}Can we do anal tonight?{/} As she gets on the bed on her hands and knees {mark}[gn_store_owner_name]{/} replies: {say}OK but please be gentle.{/}"
    "{size=-22} "
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    "Her ass is tight and it feels great. She plays with herself and since I'm gentle she's enjoying it and when I cum in her ass she cums too."
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice("fwb_bedroom_missionary") "Missionary"
    choice("fwb_bedroom_doggy") "Doggy"
    choice("fwb_bedroom_cowgirl") "Cowgirl"
    choice("fwb_bedroom_standing") "Standing"
    choice(None) "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_home_sleep5",pos=17) "Exhausted" 

  return
    
label fwb_ruthie_home_sleep5:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $temp_int=random.randint(174,176)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "Afterwards {mark}[gn_store_owner_name]{/} lies on top of me and says; {say}That was great, I'm so glad you called me tonight.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I'm exhausted but happy and say; {mcsay}You're wonderful and it was a great night.{/} We're both tired and soon we're asleep."
  $mc.mood.give_xp(randint(30,50))                  ## large mood increase
  choice("sleep_after_date:home") "Sleep"
  return

##===== Sleep with Ruthie at her new apartment =====

label fwb_ruthie_away_sleep1:  ## spend the night at Ruthie's new apartment
  $global fwb_mc_new_clothes   ## need to read flag
  $game.location="store_owner_apartment"
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
## 0.15.n Ruthie anal flag not set yet, first day it's possible was set when you had anal with Simone, and you've reached that day
  $global sd_ruthie_anal_day
  $global fwb_anal_ok
  if fwb_anal_ok==0 and sd_ruthie_anal_day>0 and now.day>=sd_ruthie_anal_day:
    $fwb_anal_ok=1
## 0.15.n reset counter for number of times you have sex this date, 3 is the limit
  $global fwb_sex_count
  $fwb_sex_count=0
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  if fwb_mc_new_clothes==0:
    $action_image= "quests friends_with_benefits fwb_177"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_179"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests friends_with_benefits fwb_178"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_180"
    center "{image=[action_image]@400x600}"
  ##  TEXT - SAME IN BOTH OLD AND NEW CLOTHES
  $act.set_block("c")
  "We walk to {mark}[gn_store_owner_name]'s{/} apartment building and use the penthouse entrance. We walk past the doorman who checks {mark}[gn_store_owner_name]{/} out and glares at me but says nothing."
  ""
  ""
  ""
  "In her apartment we're in a hurry and start undressing each other. When we're both topless {mark}[gn_store_owner_name]{/} jumps into my arms. After a few minutes she says; {say}Let's continue this on the couch.{/}"
## insert buttons for selecting foreplay on couch or skip
  choice("fwb_apartment_hj") "Hand Job"
  choice("fwb_apartment_finger") "Finger"
  choice("fwb_apartment_sucktits") "Suck Tits"
  choice("fwb_apartment_titjob") "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_apartment_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_apartment_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_apartment_69", pos=17) "Go to Bedroom"
  return

label fwb_apartment_finger:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(181,182)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I sit on her couch and {mark}[gn_store_owner_name]{/} climbs onto my lap. While sharing a passionate kiss I reach down and begin playing with her pussy."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "We both get excited and our kisses grow more and more intense as her pussy gets more and more wet."
  choice("fwb_apartment_hj") "Hand Job"
  choice(None) "Finger"
  choice("fwb_apartment_sucktits") "Suck Tits"
  choice("fwb_apartment_titjob") "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_apartment_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_apartment_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_apartment_69", pos=17) "Go to Bedroom"
  return

label fwb_apartment_hj:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(183,184)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I sit down on the couch but {mark}[gn_store_owner_name]{/} kneels on the couch instead and starts playing with my cock."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "My cock gets harder and harder as she strokes it and I pull her in for a long, wet French kiss."
  choice(None) "Hand Job"
  choice("fwb_apartment_finger") "Finger"
  choice("fwb_apartment_sucktits") "Suck Tits"
  choice("fwb_apartment_titjob") "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_apartment_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_apartment_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_apartment_69", pos=17) "Go to Bedroom"
  return

label fwb_apartment_sucktits:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(185,186)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I surprise {mark}[gn_store_owner_name]{/} by pulling her onto my lap and sucking on her nipples. She responds by grabbing my hair."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She cries out in pleasure while I enjoy sucking on her nipples and squeezing her ass. Her body feels great and makes my cock hard!"
  choice("fwb_apartment_hj") "Hand Job"
  choice("fwb_apartment_finger") "Finger"
  choice(None) "Suck Tits"
  choice("fwb_apartment_titjob") "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_apartment_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_apartment_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_apartment_69", pos=17) "Go to Bedroom"
  return

label fwb_apartment_titjob:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(187,188)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "{mark}[gn_store_owner_name]{/} tells me to sit down on her couch and smiles as she kneels in front of me and squeezes my cock between her tits."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "{mark}[gn_store_owner_name]{/} moves her breasts up and down on my cock and says; {say}You're getting harder, I guess you like it.{/} I reply; {mcsay}I love it, your tits feel great.{/}"
  choice("fwb_apartment_hj") "Hand Job"
  choice("fwb_apartment_finger") "Finger"
  choice("fwb_apartment_sucktits") "Suck Tits"
  choice(None) "Tit Job"
  $temp_int=random.randint(1,3)
  if temp_int==1:
    choice("fwb_apartment_bj", pos=17) "Go to Bedroom"
  elif temp_int==2:
    choice("fwb_apartment_lick", pos=17) "Go to Bedroom"
  else:
    choice("fwb_apartment_69", pos=17) "Go to Bedroom"
  return

label fwb_apartment_bj:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(189,190)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I gently push {mark}[gn_store_owner_name]{/} down onto the bed and kneel above her. She's surprised but doesn't resist as I push my cock into her mouth."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Her mouth feels great! I try not to force my cock in too deep but occasionally I go too far and {mark}[gn_store_owner_name]{/} gags a little but doesn't try to stop me."
  choice(None) "Blowjob"
  choice("fwb_apartment_lick") "Eat Pussy"
  choice("fwb_apartment_69") "69"
  $global fwb_anal_ok
  $global fwb_first_anal
  if fwb_anal_ok==1 and fwb_first_anal==0:                         ## anal was just activated but has NOT happened yet
    choice("fwb_apartment_anal", pos=17) "Enough Foreplay"
  else:
    if fwb_anal_ok==0:  ## anal not allowed yet
      $temp_int=random.randint(1,4)
    else:               ## anal allowed now
      $temp_int=random.randint(1,5)
    if temp_int==1:
      choice("fwb_apartment_missionary", pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("fwb_apartment_doggy", pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("fwb_apartment_cowgirl", pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("fwb_apartment_standing", pos=17) "Enough Foreplay"
    else:
      choice("fwb_apartment_anal", pos=17) "Enough Foreplay"
  return

label fwb_apartment_lick:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(191,192)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "{mark}[gn_store_owner_name]{/} lies down and says; {say}I'm ready for some of that tongue of yours.{/} I move my head down to her pussy; {mcsay}Sounds tasty.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I enjoy using my tongue to excite her clit. She wraps her leg around my head to hold me in place and cries out; {say}Yes! Just like that! Don't stop!"
  choice("fwb_apartment_bj") "Blowjob"
  choice(None) "Eat Pussy"
  choice("fwb_apartment_69") "69"
  $global fwb_anal_ok
  $global fwb_first_anal
  if fwb_anal_ok==1 and fwb_first_anal==0:                         ## anal was just activated but has NOT happened yet
    choice("fwb_apartment_anal", pos=17) "Enough Foreplay"
  else:
    if fwb_anal_ok==0:  ## anal not allowed yet
      $temp_int=random.randint(1,4)
    else:               ## anal allowed now
      $temp_int=random.randint(1,5)
    if temp_int==1:
      choice("fwb_apartment_missionary", pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("fwb_apartment_doggy", pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("fwb_apartment_cowgirl", pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("fwb_apartment_standing", pos=17) "Enough Foreplay"
    else:
      choice("fwb_apartment_anal", pos=17) "Enough Foreplay"
  return

label fwb_apartment_69:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(193,194)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I ask; {mcsay}Ready for some 69?{/} {mark}[gn_store_owner_name]{/} replies; {say}As long as I'm on top, you're too heavy.{/} As I lie down I say; {mcsay}Sounds good to me.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She lies on top and grabs my cock while licking the shaft. I grab her ass with both hands and start licking her pussy which is driping wet."
  choice("fwb_apartment_bj") "Blowjob"
  choice("fwb_apartment_lick") "Eat Pussy"
  choice(None) "69"
  $global fwb_anal_ok
  $global fwb_first_anal
  if fwb_anal_ok==1 and fwb_first_anal==0:                         ## anal was just activated but has NOT happened yet
    choice("fwb_apartment_anal", pos=17) "Enough Foreplay"
  else:
    if fwb_anal_ok==0:  ## anal not allowed yet
      $temp_int=random.randint(1,4)
    else:               ## anal allowed now
      $temp_int=random.randint(1,5)
    if temp_int==1:
      choice("fwb_apartment_missionary", pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("fwb_apartment_doggy", pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("fwb_apartment_cowgirl", pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("fwb_apartment_standing", pos=17) "Enough Foreplay"
    else:
      choice("fwb_apartment_anal", pos=17) "Enough Foreplay"
  return

label fwb_apartment_missionary:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(195,196)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "When we're ready {mark}[gn_store_owner_name]{/} lies on the bed with her legs in the air and says; {say}I want you on top this time.{/} She's wet and my cock slides in easily."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I thrust in and out slowly for a long time before I say; {mcsay}I'm about to cum.{/} She replies; {say}Me too!{/} One last thrust and we cum together."
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice(None) "Missionary"
    choice("fwb_apartment_doggy") "Doggy"
    choice("fwb_apartment_cowgirl") "Cowgirl"
    choice("fwb_apartment_standing") "Standing"
    if fwb_anal_ok==1:
      choice("fwb_apartment_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_away_sleep5",pos=17) "Exhausted"

  return

label fwb_apartment_cowgirl:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(197,198)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "When I'm ready I lie down and ask; {mcsay}Is my cowgirl ready for a ride?{/} {mark}[gn_store_owner_name]{/} smiles and replies; {say}She's ready for a long, hard ride!{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "My cowgirl climbs on top of me and goes for a long, hard ride while we look into each other's eyes. She comes first but I'm not far behind."
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice("fwb_apartment_missionary") "Missionary"
    choice("fwb_apartment_doggy") "Doggy"
    choice(None) "Cowgirl"
    choice("fwb_apartment_standing") "Standing"
    if fwb_anal_ok==1:
      choice("fwb_apartment_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_away_sleep5",pos=17) "Exhausted"

  return

label fwb_apartment_doggy:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(199,200)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "When she's ready {mark}[gn_store_owner_name]{/} kneels on the bed and says; {say}Take me from behind.{/} I kneel behind her she reaches back so we can lock arms."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She's wet and ready so I slide my cock into her and start thrusting forcefully. She gasps each time it goes deep and I say; {mcsay}Your pussy is so tight!{/}"
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice("fwb_apartment_missionary") "Missionary"
    choice(None) "Doggy"
    choice("fwb_apartment_cowgirl") "Cowgirl"
    choice("fwb_apartment_standing") "Standing"
    if fwb_anal_ok==1:
      choice("fwb_apartment_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_away_sleep5",pos=17) "Exhausted"

  return

label fwb_apartment_standing:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(201,202)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "I'm surprised when {mark}[gn_store_owner_name]{/} says; {say}Stand up.{/} We stand and she jumps into my arms. I grab her ass and say; {mcsay}So you want it this way?{/} She smiles; {say}Yes!{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She gasps as I set her down on my cock and then use my arms to lift her up and down. In a short time I cum inside her causing her to cum too."
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice("fwb_apartment_missionary") "Missionary"
    choice("fwb_apartment_doggy") "Doggy"
    choice("fwb_apartment_cowgirl") "Cowgirl"
    choice(None) "Standing"
    if fwb_anal_ok==1:
      choice("fwb_apartment_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_away_sleep5",pos=17) "Exhausted"

  return

label fwb_apartment_anal:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(203,204)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  $global fwb_first_anal
  if fwb_first_anal==0:  ## first time with Ruthie
    $fwb_first_anal=1    ## set flag to prevent repeat, same text is OK since it only happens once in the game
    "{mark}[gn_store_owner_name]{/} says shyly; {say}I want to do something special for you, I've heard that guys really like anal so I want to try it.{/}"
    "{size=-22} "
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    "I try to be gentle and slowly push into her tight ass. I know it hurts but she says; {say}It's OK, keep going.{/} After a few more strokes I cum in her ass."
  else:
    "She surprises me when {mark}[gn_store_owner_name]{/} asks; {say}Would you like anal tonight?{/} I reply: {mcsay}Of course, I'd love to and I promise to be gentle.{/} She lies down on her side."
    "{size=-22} "
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    "I get behind her and she gasps when I put my cock in her ass. I'm gentle so soon she's enjoying it and it doesn't take long before I cum in her ass."
  $global fwb_sex_count
  $global fwb_anal_ok
  $fwb_sex_count+=1
  if fwb_sex_count<3:
    choice("fwb_apartment_missionary") "Missionary"
    choice("fwb_apartment_doggy") "Doggy"
    choice("fwb_apartment_cowgirl") "Cowgirl"
    choice("fwb_apartment_standing") "Standing"
    choice(None) "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("fwb_ruthie_away_sleep5",pos=17) "Exhausted"

  return

label fwb_ruthie_away_sleep5:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(205,207)
  $action_image= "quests friends_with_benefits fwb_"+str(temp_int)
  "Afterwards we lie together and I say; {mcsay}That was wonderful, thanks for inviting me to your place.{/} She replies; {say}It sure was great, I'm glad you're here.{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Afer a few minutes {mark}[gn_store_owner_name]{/} says; {say}This feels good but I really need to sleep.{/} We enjoy a brief kiss and say goodnight. Soon we're both asleep."
  $mc.mood.give_xp(randint(30,50))                  ## large mood increase
  choice("sleep_after_date:away") "Sleep"
  return

##===== Weekly Rent for Ruthie =====

label fwb_rent_ruthie:  ## weekly on Monday morning
  $global fwb_skip_first_week  ## need to read and reset flag
  $game_bg="home bg"    ## pay Ruthie's rent at home
  $game_bgm="home bgm"
  header "{mark}[gn_store_owner_name]'s{/} Rent is Due"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_126"
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  if fwb_skip_first_week==0:    ## first week you've already paid in advance
    $fwb_skip_first_week=1      ## set flag so you pay from now on
    "I was about to pay {mark}[gn_store_owner_name]'s{/} rent today but then I remembered that I paid the first week in advance when I got her the apartment."
    $global fwb_paid_today
    $fwb_paid_today=True        ## resets payment day on left side status screen even though you didn't pay
    choice("<<<") "Continue"
  else:
    "{mark}[gn_store_owner_name]'s{/} rent is due today. I check my finances to see if I can afford to pay the {mark}$7,500{/} I promised this time."
    ""
    if mc.money>7500:           ## Ruthie will be happy with me, 85% chance of getting a date this week
      "I can afford to pay the full amount I promised but I perhaps I should pay only half or not pay at all this week."
    elif mc.money>3750:         ## Ruthie will be hurt, only 65% chance of getting a date this week
      "I can't afford to pay the full amount, I could pay half or perhaps I shouldn't pay at all this week."
    else:                       ## Ruthie will be pissed at me, no chance of getting a date this week
      "I'm so broke I can't afford to pay even half of her rent, I guess I'll have to tell her I can't pay this week."
    choice("fwb_rent_ruthie_full",cost=[("money",7500)]) "Full Payment"
    choice("fwb_rent_ruthie_half",cost=[("money",3750)]) "Half Payment"
    choice("fwb_rent_ruthie_none") "Don't Pay"
  return

label fwb_rent_ruthie_full:
  $game_bg="home bg"         ## pay Ruthie's rent at home
  $game_bgm="home bgm"
  header "{mark}[gn_store_owner_name]'s{/} Rent is Due"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  ""
  $action_image= "quests friends_with_benefits fwb_127"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_128"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "I make the full payment I promised and give {mark}[gn_store_owner_name]{/} a call; {mcsay}Hi {mark}[gn_store_owner_name]{/}{mcsay}, I wanted to let you know that I paid {mark}$7,500{/} rent for you as promised.{/}"
  ""
  ""
  "Ruthie replies cheerfully; {say}Hi {mark}[mc.name]{/}, thanks for letting me know. I really appreciate your help, this place is so much better than the tiny place I used to live in.{/}"
  ""
  "We say our goodbyes and end the call. She sounded cheerful this morning which always puts me in a good mood."
  $global fwb_next_date
  $fwb_next_date=1          ## will be 85:15 yes this week
  $global fwb_paid_today
  $fwb_paid_today=True      ## resets payment day on left side status screen
  choice("<<<") "Continue"
  return

label fwb_rent_ruthie_half:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[gn_store_owner_name]'s{/} Rent is Due"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  ""
  $action_image= "quests friends_with_benefits fwb_129"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_130"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "I pay half of the amount I promised and give {mark}[gn_store_owner_name]{/} a call to give her the news; {mcsay}Hi {mark}[gn_store_owner_name]{/}{mcsay}, I wanted to let you know that I could only pay {mark}$3,750{/} of the rent for you this week, I'm sorry.{/}"
  ""
  ""
  "Ruthie sounds disappointed; {say}Hi {mark}[mc.name]{/}, thanks for letting me know. I'll figure out how to pay an extra {mark}$3,750{/} this week. I hope both your shop and my store do better this week.{/}"
  ""
  "We say our goodbyes and end the call. I hated to disappoint her but at least she didn't sound angry about it."
  $global fwb_next_date
  $fwb_next_date=0          ## will be 65:35 yes this week
  $global fwb_paid_today
  $fwb_paid_today=True      ## resets payment day on left side status screen
  choice("<<<") "Continue"
  return

label fwb_rent_ruthie_none:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[gn_store_owner_name]'s{/} Rent is Due"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  ""
  $action_image= "quests friends_with_benefits fwb_131"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_132"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "I give {mark}[gn_store_owner_name]{/} a call to tell her I can't pay any of her rent this week; {mcsay}Hi {mark}[gn_store_owner_name]{/}{mcsay}, I'm really sorry but business has been really bad and I can't help pay your rent this week.{/}"
  ""
  ""
  "{mark}[gn_store_owner_name]{/} sounds sarcastic and angry; {say}Well that's just great. I shouldn't have agreed to this, the old apartment was bad but at least I could afford it.{/}"
  ""
  "She didn't say hello and she hung up on me without saying goodbye. She was really angry and I guess I can't blame her."
  $global fwb_next_date
  $fwb_next_date=-1          ## will always be no this week
  $global fwb_paid_today
  $fwb_paid_today=True       ## resets payment day on left side status screen even though you didn't pay
  choice("<<<") "Continue"
  return