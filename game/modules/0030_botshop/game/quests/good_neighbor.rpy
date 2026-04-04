##==== VARIABLES===========

init python:
  gn_diner_counter=0             ## add each night you stop at store to check on it, when reaches 3 initiate diner robbery
  rpb_part_check="FEDC"          ## for 'repair bot check', if any part has one of these check fails
  gn_min_bot_rate=5              ## uses number - bots for store and patrol (both are the same) must be B+
  gn_min_part_rate="FEDC"        ## parts use reverse logic - parts must be B+
  gn_min_integrity=100           ## bots must be 100%
  gn_min_stability=100           ## bots must be 100%
  gn_min_combat_skill="AS"       ## bots must be A+ combat
  gn_min_social_skill="AS"       ## bots must be A+ social
  gn_female_bot_selected=[]      ## holding place for female bot selection while selecting male bot - NOT SURE ABOUT VARIABLE TYPE
  gn_male_bot_selected=[]        ## holding place for male bot selected - NOT SURE ABOUT VARIABLE TYPE
  gn_which_pair=-1               ## -1 - store owner, 0 - patrol 1, 1 - patrol 2, 2 - patrol 3 - done - increment each delivery - damaged bot limit = gn_which_pair
  gn_bots=[]                     ## holds bots for selection
  gn_fail_string=""              ## holds failure list for bots when none qualified
  gn_damaged_bot_waiting=0       ## flag: set to 1 when damaged patrol bot delivered but no capsule or storage space available
  gn_repairing_bot=0             ## counter: increment when bot received, decrement when bot returned
  gn_damaged_bot_gender=0        ## 0 is female bot, 1 is male bot
  gn_combat_xp=0                 ## set when bot created: female Camilla 12000, male Quinton 33000
  gn_social_xp=0                 ## set when bot created: female Camilla 22600, male Quinton 38000
  gn_damage_max=0                ## set when bot created: female Camilla 250, male Quinton 99 - Camilla is A with A parts, Quinton is B with B parts
  gn_repeat_store_robbed=0       ## count days to prevent this from happening too frequently, 5 day cycle but still random so probably

##=========2) PHASES============

  class Quest_goodneighbor(Quest):
    name="Good Neighbor(SL)"

    class phase_1_goodneighbor1:
      description="""
        {mark}I'm glad the store owner is OK.{/} I promised to help her out by giving her a pair of bots to protect her shop and help her run it too. Here's what I want to provide:
        {mark}1 female and 1 male bot{/}
        {mark}B+ rated bots{/} - they need to be good!
        {mark}B+ rated parts{/} - they need to be strong!
        {mark}A+ combat skill{/} - they need to be tough!
        {mark}A+ social skill{/} - they need to do the right thing!
        {mark}'Clerk' role{/}  - they need to run the store! ('Shopkeeper'includes 'Clerk')
        {mark}100% Integrity{/} and {mark}100% Stability{/}
        {mark}2 capsules{/} with {mark}level 2 upgrades{/} - this will cost {mark}$56,000{/}

        """

    class phase_2_goodneighbor2:
      description="""
        I'm glad I gave the store owner bots to protect her and help run the store. She's really nice, I think I'll check in on her shop when I'm coming home at night.

        """

    class phase_3_goodneighbor3:
      description="""
        The mob is no longer protecting my neighborhood so I need to step up. With a little help from my neighbors we'll set up a {mark}neighborhood patrol{/}! The patrol will always be couples so my neighborhood won't look like a combat zone. I'll make the first pair like this:
        {mark}1 female and 1 male bot{/}
        {mark}B+ rated bots{/} - they need to be good!
        {mark}B+ rated parts{/} - they need to be strong!
        {mark}A+ combat skill{/} - they need to be tough!
        {mark}A+ social skill{/} - they need to do the right thing!
        {mark}100% Integrity{/} and {mark}100% Stability{/}
        {mark}2 capsules{/} with {mark}level 2 upgrades{/} - this will cost {mark}$56,000{/}
        
        """

    class phase_4_goodneighbor4:
      description="""
        We need a {mark}second bot patrol pair{/}. One bot patrol is not enough, there's no protection when their recharging. I'll make a second pair just like the first:
        {mark}1 female and 1 male bot{/}
        {mark}B+ rated bots{/} - they need to be good!
        {mark}B+ rated parts{/} - they need to be strong!
        {mark}A+ combat skill{/} - they need to be tough!
        {mark}A+ social skill{/} - they need to do the right thing!
        {mark}100% Integrity{/} and {mark}100% Stability{/}
        {mark}2 capsules{/} with {mark}level 2 upgrades{/} - this will cost {mark}$56,000{/}

        """

    class phase_5_goodneighbor5:
      description="""
        A {mark}third bot patrol pair{/} will ensure there are two patrols on duty all the time. I'll make the third pair just like the other two pairs:
        {mark}1 female and 1 male bot{/}
        {mark}B+ rated bots{/} - they need to be good!
        {mark}B+ rated parts{/} - they need to be strong!
        {mark}A+ combat skill{/} - they need to be tough!
        {mark}A+ social skill{/} - they need to do the right thing!
        {mark}100% Integrity{/} and {mark}100% Stability{/}
        {mark}2 capsules{/} with {mark}level 2 upgrades{/} - this will cost {mark}$56,000{/}

        """

    class phase_1000_goodneighbor_done:
      description="Our neighborhood patrol is complete, it feels good to help out my friends!"
      
    class phase_2000_goodneighbor_failed:                             ## there is no possibility of failure for this quest, it will remain open indefinately until you complete it
            description="Who cares about the neighborhood anyway?"

##========= EVENT HANDLER NEEDED IN THIS QUEST - EVENT HANDLER - PYTHON HIDE=========

init python hide:
  @event_handler("time_advanced")
  def good_neighbor_event():
    if not quests.goodneighbor.started:                             ## isolate 'not started' so following 'elif' clauses work
      if not quests.goodneighbor.finished:                          ## TEST VARIABLES FOR THIS, MAY NOT BE NEEDED! if it's finished we don't want to start it again
        if now("night") and quests.mobprotection.finished:          ## store robbery happens at night after mob protection finished
          queue_event("quest_goodneighbor_event0")
    elif now("afternoon")and quests.goodneighbor=="goodneighbor1":  ## 'goodneighbor1' is while building bots for store owner
      queue_event("good_neighbor_repeat_robbery")                   ## function: 20% chance repeat robbery -3AP every 5 days, other times -1AP
    elif now("night") and quests.goodneighbor=="goodneighbor2":     ## diner robbery event during 'goodneighbor2'
      queue_event("quest_goodneighbor_event2")
    if gn_damaged_bot_waiting==1:                                   ## independent of quest state - damaged bot waiting - only 1 allowed
      if home.available_capsules>0 or workshop.available_space>0:   ## space available
        queue_event("gn_receive_damaged_patrol_bot")                ## function that receives the damaged bot
    return

##========= EVENT FUNCTIONS==========

label quest_goodneighbor_event0:          ## first store robbery
  $game.location="neighborhood"           ## set location for display, not fully implemented with 'roaming' in 0.8.n
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  $act.start_block("l:400 c:content_width-400")
  $act.set_block("l")
  $action_image= "quests good_neighbors sgn_1"
  center "{image=[action_image]@340x600}"
  "{size=-8} "
  $action_image= "quests good_neighbors sgn_2"
  center "{image=[action_image]@340x600}"
  "{size=-8} "
  $action_image= "quests good_neighbors sgn_3" 
  center "{image=[action_image]@340x600}"
  $act.set_block("c")
  "On your way to [gn_store_owner_name]'s store to pick up some food you see some thugs beating her and robbing her store! You start running towards the store and yelling hoping to scare them away."
  $mc.mood.give_xp(-50)
  "{size=-8} "
  "Your glad they decided to run away, it would have been 2 against 1 and you don't have a bot with you. You need to get to {mark}[gn_store_owner_name]{/} and find out if she's OK, she doesn't look good."
  "{size=-4} "
  "{size=-4} "
  "{mark}[gn_store_owner_name]{/} is on the ground and you kneel down to help her. Her face is bruised where they hit her, fuckin' assholes! It's a good thing I was on the way to her store right now."
  choice("good_neighbor_store_robbery2") "Continue"
  return

label quest_goodneighbor_event1:          ## deliver bots to store
  $game.location="neighborhood"           ## set location for display, not fully implemented with 'roaming' in 0.8.n
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood - Select Female Bot"
  call gn_select_bot("female")                           ## selecting a female bot 
  if gn_bots:
    $act.start_block("l:400 c:content_width-400")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_62"
    center "{image=[action_image]@340x600}"
    ""
    $act.set_block("c")
    "Select the female bot you'd like to give to the {mark}[gn_store_owner_name]{/} for her store:"
    ""
    $bot_n=0
    while gn_bots:
      $bot,bot_price=gn_bots.pop(0)
      $bot_n+=1
      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}"
      choice("good_neighbor_delivery2:{}".format(bot.id)) "Select #[bot_n]"
  else:
    "Unfortunately you don't have any female bots that meed the requirements you set for {mark}[gn_store_owner_name]'s{/} store. You need to prepare a female bot that meets these requirements."
    "Bot Rate: {mark}B+{/}"
    "All Parts: {mark}B+{/}"
    "Combat Skill: {mark}A+{/}"
    "Social Skill: {mark}A+{/}"
    "Role: {mark}Clerk{/} (Shopkeeper includes Clerk)"
    "Integrity: {mark}100\%{/}"
    "Stability: {mark}100\%{/}"
    ""
    "Requirements each bot {mark}does NOT{/} meet:"
    "{size=-8}[gn_fail_string]{/}"
    $gn_female_bot_selected=[]          ## reset for next time
    $gn_male_bot_selected=[]            ## reset for next time
  choice("goto_home", pos=17) "Cancel"  ## when leaving 'goto_home'
  return

label quest_goodneighbor_event2:        ## diner robbery
  $gn_diner_counter+=1                  ## increment counter, 3rd time initiates diner robbery
  $game.location="neighborhood"         ## set location for display, not fully implemented with 'roaming' in 0.8.n
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  if gn_diner_counter>=3:                          ## visited store twice, 3rd time is diner robbery
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_19"
    ""
    center "{image=[action_image]@400x600}"
    ""
    ""
    $action_image= "quests good_neighbors sgn_20"
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    ""
    "On your way to the diner to get something to eat you see two thugs robbing {mark}[gn_diner_owner_name]'s{/} diner and they're threatening {mark}[gn_store_owner_name]{/} too. You yell and run towards the diner trying to scare them away."
    $mc.mood.give_xp(-50)
    ""
    ""
    ""
    ""
    "Just like at {mark}[gn_store_owner_name]'s{/} store, the thugs ran away. I got lucky again! When I reached the diner I could see that {mark}[gn_store_owner_name]{/} is frightened but {mark}[gn_diner_owner_name]{/} helps me calm her down."
    choice("good_neighbor_diner_robbery2") "Continue"
    return
  elif gn_diner_counter==1:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_54"
    ""
    center "{image=[action_image]@400x600}"
    ""
    ""
    $action_image= "quests good_neighbors sgn_55"
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    ""
    "You decide to visit {mark}[gn_store_owner_name]{/} at her store to check on her and the bots you gave her and she see's you coming. I'm really glad I gave her the bots so she doesn't have to be afraid any more. She's a lot more cheerful and fun to be around now."
    ""
    ""
    "You're a little surprised when she comes right up and kisses you but it feels really nice and you enjoyed it. Afterwards you talk for a while and she says the bots are doing great. Her customers notice them and feel safer coming to the store because they're here."
  else:                                  ## must be 2
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_56"
    ""
    center "{image=[action_image]@400x600}"
    ""
    ""
    $action_image= "quests good_neighbors sgn_57"
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    ""
    "It's fun to visit with {mark}[gn_store_owner_name]{/} at her shop but you don't see when you arrive. One of the bots you gave her points to the other room and you see {mark}[gn_store_owner_name]{/} checking the shelves. Maybe I'll surprise her!"
    ""
    ""
    ""
    "{mark}[gn_store_owner_name]{/} hears me coming though. She turns around with a big smile and jumps into my arms. I was so surprised I almost dropped her but I recovered and we enjoyed a long kiss. We talked for a while, it's really fun hanging out with her!"
## 1 & 2 closing function same
  $mc.mood.give_xp(25)
  if mc_so_value<50:                                  ## 0.12.n addition: do NOT allow FWB until FWB quest end
    call mc_update_relation(gn_store_owner_name,1,0)  ## relationship gain for visiting Ruthie BEFORE diner robbery
  choice("goto_home") "Continue"
  return

label quest_goodneighbor_event3:       ## 1st bot patrol
  $game.location="neighborhood"        ## set location for display, not fully implemented with 'roaming' in 0.8.n
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood - Select Female Bot"
  call gn_select_bot("female")                           ## selecting a female bot
  if gn_bots:
    $act.start_block("l:400 c:content_width-400")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_62"
    center "{image=[action_image]@340x600}"
    ""
    $act.set_block("c")
    "Select the female bot you'd like to give to the {mark}Neighborhood Patrol{/}:"
    ""
    $bot_n=0
    while gn_bots:
      $bot,bot_price=gn_bots.pop(0)
      $bot_n+=1
      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}"
      choice("good_neighbor_delivery2:{}".format(bot.id)) "Select #[bot_n]"
  else:
    "Unfortunately you don't have any female bots that meed the requirements you set for the {mark}Neighborhood Patrol{/}. You need to prepare a female bot that meets these requirements."
    "Bot Rate: {mark}B+{/}"
    "All Parts: {mark}B+{/}"
    "Combat Skill: {mark}A+{/}"
    "Social Skill: {mark}A+{/}"
    "Integrity: {mark}100\%{/}"
    "Stability: {mark}100\%{/}"
    ""
    "Requirements each bot {mark}does NOT{/} meet:"
    "{size=-8}[gn_fail_string]{/}"
    $gn_female_bot_selected=[]      ## reset for next time
    $gn_male_bot_selected=[]        ## reset for next time
  choice("goto_home", pos=17) "Cancel"       ## when leaving 'goto_home'
  return

label quest_goodneighbor_event4:       ## 2nd bot patrol
  $game.location="neighborhood"        ## set location for display, not fully implemented with 'roaming' in 0.8.n
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood - Select Female Bot"
  call gn_select_bot("female")                           ## selecting a female bot
  if gn_bots:
    $act.start_block("l:400 c:content_width-400")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_62"
    center "{image=[action_image]@340x600}"
    ""
    $act.set_block("c")
    "Select the female bot you'd like to give to the {mark}Neighborhood Patrol{/}:"
    ""
    $bot_n=0
    while gn_bots:
      $bot,bot_price=gn_bots.pop(0)
      $bot_n+=1
      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}"
      choice("good_neighbor_delivery2:{}".format(bot.id)) "Select #[bot_n]"
  else:
    "Unfortunately you don't have any female bots that meed the requirements you set for the {mark}Neighborhood Patrol{/}. You need to prepare a female bot that meets these requirements."
    "Bot Rate: {mark}B+{/}"
    "All Parts: {mark}B+{/}"
    "Combat Skill: {mark}A+{/}"
    "Social Skill: {mark}A+{/}"
    "Integrity: {mark}100\%{/}"
    "Stability: {mark}100\%{/}"
    ""
    "Requirements each bot {mark}does NOT{/} meet:"
    "{size=-8}[gn_fail_string]{/}"
    $gn_female_bot_selected=[]      ## reset for next time
    $gn_male_bot_selected=[]        ## reset for next time
  choice("goto_home", pos=17) "Cancel"       ## when leaving 'goto_home'
  return

label quest_goodneighbor_event5:       ## 3rd bot patrol
  $game.location="neighborhood"        ## set location for display, not fully implemented with 'roaming' in 0.8.n
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood - Select Female Bot"
  call gn_select_bot("female")                           ## selecting a female bot
  if gn_bots:
    $act.start_block("l:400 c:content_width-400")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_62"
    center "{image=[action_image]@340x600}"
    ""
    $act.set_block("c")
    "Select the female bot you'd like to give to the {mark}Neighborhood Patrol{/}:"
    ""
    $bot_n=0
    while gn_bots:
      $bot,bot_price=gn_bots.pop(0)
      $bot_n+=1
      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}"
      choice("good_neighbor_delivery2:{}".format(bot.id)) "Select #[bot_n]"
  else:
    "Unfortunately you don't have any female bots that meed the requirements you set for the {mark}Neighborhood Patrol{/}. You need to prepare a female bot that meets these requirements."
    "Bot Rate: {mark}B+{/}"
    "All Parts: {mark}B+{/}"
    "Combat Skill: {mark}A+{/}"
    "Social Skill: {mark}A+{/}"
    "Integrity: {mark}100\%{/}"
    "Stability: {mark}100\%{/}"
    ""
    "Requirements each bot {mark}does NOT{/} meet:"
    "{size=-8}[gn_fail_string]{/}"
    $gn_female_bot_selected=[]      ## reset for next time
    $gn_male_bot_selected=[]        ## reset for next time
  choice("goto_home", pos=17) "Cancel"       ## when leaving 'goto_home'
  return

##========== SUPPORTING FUNCTIONS BELOW ==========

##========== 'Deliver Bot' button in 'home workout' - active: phase 1 for store, phases 3, 4, and 5 for patrol

label good_neighbor_advance:
  if quests.goodneighbor=="goodneighbor1":
    call quest_goodneighbor_event1
  elif quests.goodneighbor=="goodneighbor2":
    call quest_goodneighbor_event2
  elif quests.goodneighbor=="goodneighbor3":
    call quest_goodneighbor_event3
  elif quests.goodneighbor=="goodneighbor4":
    call quest_goodneighbor_event4
  elif quests.goodneighbor=="goodneighbor5":
    call quest_goodneighbor_event5
  return

label gn_select_bot(gn_gender):  ## parameter is desired gender
  python:
    mbc_skill_any="FEDCBAS" ## used for any skill level
    gn_bots=[]              ## list of bots meeting requirements, if any
    gn_fail_string=""       ## for displaying fail results if no bots meet requirements
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot and bot.action_allowed("sell"):                                   ## must be: a bot that didn't come from "repair order" or "repair patrol bot"
          gn_fail_string=gn_fail_string+"{mark}"+bot.name+", "+bot.model_name+":{/}"
          mbc_bot_pass=1                                                         ## assume bot passes, set to 1
          if bot.gender!=gn_gender:
            gn_fail_string=gn_fail_string+"-gender"
            mbc_bot_pass=0                                                       ## bot is wrong gender
          if bot.rate_level<gn_min_bot_rate:
            gn_fail_string=gn_fail_string+"-bot rate"
            mbc_bot_pass=0                                                       ## bot rating too low
          if gn_which_pair==-1:                                                  ## -1 is store owner, 'clerk' requirement is for store owner's bots only
            gn_role_check_pass=0                                                 ## assume fail until proven pass
            for role in bot.roles:
              if role.id=="clerk" or role.id=="shopkeeper":                      ## found 'clerk' role or 'shopkeeper' role which includes 'clerk' function
                gn_role_check_pass=1
            if gn_role_check_pass==0:
              gn_fail_string=gn_fail_string+"-not clerk"
              mbc_bot_pass=0
          mbc_skills_temp=0                                                      ## reset temp skills counter
          if bot.bot_combat.level_name in gn_min_combat_skill:                   ## combat skill must be A+
            mbc_skills_temp+=1                                                   ## for skills increment: need to pass all 5 skills so pass value is 5
          if bot.bot_electronics.level_name in mbc_skill_any:                    ## electronics skill not used 
            mbc_skills_temp+=1
          if bot.bot_mechanics.level_name in mbc_skill_any:                      ## mechanics skill not used
            mbc_skills_temp+=1
          if bot.bot_sex.level_name in mbc_skill_any:                            ## sex skill not used
            mbc_skills_temp+=1
          if bot.bot_social.level_name in gn_min_social_skill:                   ## social skill must be A+
            mbc_skills_temp+=1
          if mbc_skills_temp<5:                                                  ## all 5 skills must pass
            gn_fail_string=gn_fail_string+"-skill(s)"
            mbc_bot_pass=0                                                       ## bot does not meet all skill requirements
          mbc_part_test_pass=1
          for slot in bot.outfit_slots:
            part=bot.item_on_slot(slot)
            if part.rate in gn_min_part_rate:                                    ## part rating uses reverse logic
              mbc_part_test_pass=0
              break                                                              ## stop testing on failure, part quantity or identity irrelevant
          if mbc_part_test_pass==0:                                              ## had a part failure
            gn_fail_string=gn_fail_string+"-part(s)"
            mbc_bot_pass=0                                                       ## bot does not meet all part requirements
          if bot.chassis.integrity<gn_min_integrity:
            gn_fail_string=gn_fail_string+"-integrity"
            mbc_bot_pass=0                                                       ## bot integrity too low
          if bot.psychocore.stability<gn_min_stability:
            gn_fail_string=gn_fail_string+"-stability"
            mbc_bot_pass=0                                                       ## bot stability too low
          if bot.do_not_sell:
            gn_fail_string=gn_fail_string+"-DNS"
            mbc_bot_pass=0                                                       ## bot is marked DNS
          if bot["mission"]:
            gn_fail_string=gn_fail_string+"-mission"
            mbc_bot_pass=0                                                       ## bot on mission
          if mbc_bot_pass==1:                                                    ## bot passed all tests
            bot_price=bot_price_function(bot)  ## DO NOT OMIT
            gn_bots.append([bot,bot_price])    ## DO NOT OMIT
          gn_fail_string=gn_fail_string+"\n"
    gn_bots=gn_bots[:12]
  return

##============ quest intro, store being robbed ===========

label good_neighbor_store_robbery2:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  $act.start_block("l:400 c:content_width-400")
  $act.set_block("l")
  $action_image= "quests good_neighbors sgn_4"
  center "{image=[action_image]@340x600}"
  "{size=-8} "
  $action_image= "quests good_neighbors sgn_5"
  center "{image=[action_image]@340x600}"
  "{size=-8} "
  $action_image= "quests good_neighbors sgn_6" 
  center "{image=[action_image]@340x600}"
  $act.set_block("c")
  "Once {mark}[gn_store_owner_name]{/} is up you see she's in shock and her face is badly bruised. She can't continue running her store tonight and she needs help closing it so you ask her to come with you to your shop."
  "{size=-8} "
  "{size=-8} "
  "On the way to your shop you say she shouldn't go back to her store tonight and suggest she give one of your bots instructions for closing her store. She is pretty shook up and says that's a good idea."
  ""
  "In the shop you get one of your bots and {mark}[gn_store_owner_name]{/} gives her instructions for closing her store. This bot can do it on her own while I take care of {mark}[gn_store_owner_name]{/}. She need company getting home."
  choice("good_neighbor_store_robbery3") "Continue"
  return

label good_neighbor_store_robbery3:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  $act.start_block("l:400 c:content_width-400")
  $act.set_block("l")
  $action_image= "quests good_neighbors sgn_7"
  center "{image=[action_image]@340x600}"
  "{size=-8} "
  $action_image= "quests good_neighbors sgn_8"
  center "{image=[action_image]@340x600}"
  "{size=-8} "
  $action_image= "quests good_neighbors sgn_9" 
  center "{image=[action_image]@340x600}"
  $act.set_block("c")
  "After sending your bot to close the store you leave your shop with {mark}[gn_store_owner_name]{/} and head for the outdoor diner up the road. She's pretty rattled, I need to help her relax before she goes home."
  "{size=-10} "
  "{size=-10} "
  "When you reach {mark}[gn_diner_owner_name]'s{/} diner just up the street from your shop he's concerned so you tell him what happened. Then you say you'll hang out with {mark}[gn_store_owner_name]{/} until she feels better and this brings a smile to his face."
  "{size=-4} "
  "{mark}[gn_diner_owner_name]{/} gives you both some coffee and you sit down in front of the diner. She tells you that this has been happening ever since the mob disappeared. {mark}Even though they demanded a lot of money they kept the thugs away from her store.{/}"
  choice("good_neighbor_store_robbery4") "Continue"
  return

label good_neighbor_store_robbery4:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  $act.start_block("l:400 c:content_width-400")
  $act.set_block("l")
  $action_image= "quests good_neighbors sgn_10"
  center "{image=[action_image]@340x600}"
  "{size=-8} "
  $action_image= "quests good_neighbors sgn_11"
  center "{image=[action_image]@340x600}"
  "{size=-8} "
  $action_image= "quests good_neighbors sgn_12"
  center "{image=[action_image]@340x600}"
  $act.set_block("c")
  "After {mark}[gn_store_owner_name]{/} calms down she looks tired so you offer to walk her home. {mark}On the way you say you'll give her trained combat bots to protect her and help run her store.{/}"
  "{size=-20} "
  "Her apartment building isn't far away and when you reach it she makes a joke about her 'palace'. After she goes inside you turn around to head for home. She's really nice, I need to help her out."
  "{size=-20} "
  "On the way home you pass the diner and wave to {mark}[gn_diner_owner_name]{/} who's always smiling. {mark}I wonder if taking down the mob was such a good idea!{/}"
  "{size=-20} "
  $global mc_so_value
  $mc.mood.give_xp(25)                                     ## 0.12.n addition
  if mc_so_value<50:                                       ## do NOT allow FWB until FWB quest end
    if mc_so_value<12:                                     ## if still 'Acquaintance' force it to 'Friend' at end of store robbery
      $temp=12-mc_so_value
      call mc_update_relation(gn_store_owner_name,temp,0)  ## relationship gain for visiting
    else:
      call mc_update_relation(gn_store_owner_name,3,0)     ## relationship gain for visiting
  $mc.give_xp("rep_neighborhood",10)                       ## DINER OWNER TELLS PEOPLE HOW YOU SAVED STORE OWNER FROM THUGS
  $quests.start_quest("goodneighbor")                      ## QUEST STARTS
  $gn_repeat_store_robbed=4                                ## on 5th day a repeat robbery can occur but only 20% chance every day until it happens, when happens reset to 4 to prevent too frequent occurrances
  choice("goto_home") "Continue"                           ## ALWAYS END WITH THIS
  return

##========== diner being robbed ==========

label good_neighbor_diner_robbery2:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests good_neighbors sgn_21"
  ""
  center "{image=[action_image]@400x600}"
  ""
  ""
  $action_image= "quests good_neighbors sgn_22"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "We all sit down at one of the tables and {mark}[gn_store_owner_name]{/} asks me if I can make bots for {mark}[gn_diner_owner_name]{/} like the ones I made for her. {mark}[gn_diner_owner_name]{/} says the whole neighborhood could use them since the mob is gone and thugs have moved in."
  ""
  "I say that I'd be willing to supply bots for a {mark}Neighborhood Patrol{/} but I need help. Someone has to run the patrol and we need a place to keep the bots and their capsules."
  ""
  "{mark}[gn_store_owner_name]{/} says she can run the patrol while her bots run her store. {mark}[gn_diner_owner_name]{/} says he has an old place that has enough power for bot capsules. We decide the patrol needs {mark}3 pairs of highly trained bots that look like couples walking around the neighborhood to keep the thugs away{/}."
  ""
  choice("good_neighbor_diner_robbery3") "Continue"
  return

label good_neighbor_diner_robbery3:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests good_neighbors sgn_23"
  ""
  center "{image=[action_image]@400x600}"
  ""
  ""
  $action_image= "quests good_neighbors sgn_24"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "After discussing the details I offer to walk {mark}[gn_store_owner_name]{/} home and I hold her hand as we leave the diner with {mark}[gn_diner_owner_name]{/} smiling as he says goodbye. I enjoy {mark}[gn_store_owner_name]'s{/} company and it's nice having friends in the neighborhood."
  ""
  "When we reach {mark}[gn_store_owner_name]'s{/} apartment she gives me a hug and says thank you for helping her and {mark}[gn_diner_owner_name]{/} and the rest of the people in the neighbornood. {mark}Paying the mob for protection was hard on everyone but the thugs have been even worse{/}."
  ""
  "After a nice long hug she went inside and I walked home. The {mark}Neighborhood Patrol{/} will cost me some time and money but I think it will be worth it for the neighborhood to be safe."
  ""
  $global mc_so_value
  if mc_so_value<50:                                  ## do NOT allow FWB until FWB quest end
    call mc_update_relation(gn_store_owner_name,2,0)  ## relationship gain for visiting
  $mc.give_xp("rep_neighborhood",10)   ## DINER OWNER TELLS PEOPLE HOW YOU SAVED STORE OWNER FROM THUGS
  $quests.goodneighbor.advance()
  $game.location="street"              ## forces flavor line about getting home
  choice("goto_home") "Continue"
  return

##========== bots being delivered ==========
  
label good_neighbor_delivery2(female_bot):         ## pick male bot - bot received is female bot already selected
  $gn_female_bot_selected=female_bot               ## put the female bot in the holding variable
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "Neighborhood - Select Male Bot"
  call gn_select_bot("male")                       ## selecting a male bot this time
  if gn_bots:
    $act.start_block("l:400 c:content_width-400")
    $act.set_block("l")
    $action_image= "quests good_neighbors sgn_62"
    center "{image=[action_image]@340x600}"
    ""
    $act.set_block("c")
    if gn_which_pair==-1:                          ## -1 is store owner
      "Select the male bot you'd like to give to {mark}[gn_store_owner_name]{/} for her store:"
    else:
      "Select the male bot you'd like to give to the {mark}Neighborhood Patrol{/}:"
    ""
    $bot_n=0
    while gn_bots:
      $bot,bot_price=gn_bots.pop(0)
      $bot_n+=1
      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}"
      choice("good_neighbor_delivery3:{}".format(bot.id)) "Select #[bot_n]"
  else:
    if gn_which_pair==-1:                          ## -1 is store owner
      "Unfortunately you don't have any male bots that meed the requirements you set for {mark}[gn_store_owner_name]'s{/} store. You need to prepare a male bot that meets these requirements."
    else:
      "Unfortunately you don't have any male bots that meed the requirements you set for the {mark}Neighborhood Patrol{/}. You need to prepare a female bot that meets these requirements."
    "Bot Rate: {mark}B+{/}"
    "All Parts: {mark}B+{/}"
    "Combat Skill: {mark}A+{/}"
    "Social Skill: {mark}A+{/}"
    if gn_which_pair==-1:                          ## -1 is store owner - clerk or shopkeeper role applies to bots for store only
      "Role: {mark}Clerk{/} (Shopkeeper includes Clerk)"
    "Integrity: {mark}100\%{/}"
    "Stability: {mark}100\%{/}"
    ""
    "Requirements each bot {mark}does NOT{/} meet:"
    "{size=-8}[gn_fail_string]{/}"
    $gn_female_bot_selected=[]                     ## reset for next time
    $gn_male_bot_selected=[]                       ## reset for next time

  choice("goto_home", pos=17) "Cancel"       ## when leaving 'goto_home'
##  choice("<<<", pos=17) "Cancel"

  return

label good_neighbor_delivery3(male_bot):           ## picked both bots - bot received is male bot selected
  $gn_male_bot_selected=male_bot                   ## put the male bot in the holding variable
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
## 0.11.n add 2 lines
  if gn_which_pair>=0:                             ## store owner bots are -1, bot patrol is 0,1,2
    $phq_button=1                                  ## after delivering the first pair show patrol hq location button
  if gn_which_pair==-1:                            ## -1 is store owner
    header "Neighborhood - Deliver Bots for {mark}[gn_store_owner_name]{/}"
  else:
    header "Neighborhood - Deliver Bots for the {mark}Neighborhood Patrol{/}"
  if gn_which_pair==-1:                            ## -1 is store owner
    $first_picture=13
    $second_picture=14
  elif gn_which_pair==0:                           ## 0 is patrol 1
    $first_picture=25
    $second_picture=26
  elif gn_which_pair==1:                           ## 1 is patrol 2
    $first_picture=31
    $second_picture=32
  elif gn_which_pair==2:                           ## 2 is patrol 3
    $first_picture=37
    $second_picture=38
  $act.start_block("l:400 c:content_width-400")
  $act.set_block("l")
  $action_image= "quests good_neighbors sgn_"+str(first_picture)
  center "{image=[action_image]@340x600}"
  ""
  $action_image= "quests good_neighbors sgn_"+str(second_picture)
  center "{image=[action_image]@340x600}"
  ""
  $act.set_block("c")
  if gn_which_pair==-1:                            ## -1 is store owner
    "You instruct the bots for {mark}[gn_store_owner_name]'s{/} store that their assignment is to follow her instructions, to protect her, and to operate her shop. Afterwards you tell them to come with you."
    ""
    ""
    "You leave the shop and head towards {mark}[gn_store_owner_name]'s{/} store with the bots following you. I'm sure she'll be happy to receive these two bots. She waves when she sees you coming. "
  elif gn_which_pair==0:                           ## 0 is patrol 1
    "You head over to the back of the shop to get the bots you restored and trained for the {mark}Neighborhood Patrol{/}. You're confident they will make a big difference when they start patrolling your neighborhood."
    ""
    ""
    "After instructing the bots on their assignment you tell leave the shop and head in the direction of the {mark}Neighborhood Patrol{/} headquarters that {mark}[gn_diner_owner_name]{/} provided."
  elif gn_which_pair==1:                           ## 1 is patrol 2
    "On the way to get the bots for the {mark}Neighborhood Patrol{/} you remember the last time you delivered bots to {mark}[gn_store_owner_name]{/}. You're both excited and nervous about doing it again. I'm such a geek, maybe I need to change."
    ""
    ""
    "You give the bots their assignment and leave the shop heading off in the direction of the {mark}Neighborhood Patrol{/} HQ. You hope {mark}[gn_store_owner_name]{/} will be happy to see you like she was last time."
  elif gn_which_pair==2:                           ## 2 is patrol 3
    "While getting the last pair of bots for the {mark}Neighborhood Patrol{/} you think it will be great to see {mark}[gn_store_owner_name]{/} again. You're not as nervous as before but even more excited. Maybe I'm not such a geek afer all."
    ""
    ""
    "For the last time you give the bots their assignment and leave the shop to deliver bots for the {mark}Neighborhood Patrol{/} HQ. Delivering bots has been a good reason to see {mark}[gn_store_owner_name]{/} and you don't want it to end."
  ""
  choice("good_neighbor_delivery4") "Continue"
  return

label good_neighbor_delivery4:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  if gn_which_pair==-1:
    header "Neighborhood - Deliver Bots for {mark}[gn_store_owner_name]{/}"
  else:
    header "Neighborhood - Deliver Bots for the {mark}Neighborhood Patrol{/}"
  if gn_which_pair==-1:
    $first_picture=15
    $second_picture=16
  elif gn_which_pair==0:
    $first_picture=27
    $second_picture=28
  elif gn_which_pair==1:
    $first_picture=33
    $second_picture=34
  elif gn_which_pair==2:
    $first_picture=39
    $second_picture=40
  $act.start_block("l:400 c:content_width-400")
  $act.set_block("l")
  $action_image= "quests good_neighbors sgn_"+str(first_picture)
  center "{image=[action_image]@340x600}"
  ""
  $action_image= "quests good_neighbors sgn_"+str(second_picture)
  center "{image=[action_image]@340x600}"
  ""
  $act.set_block("c")
  if gn_which_pair==-1:
    ""
    "When you reach {mark}[gn_store_owner_name]'s{/} store your bots stay outside while you tell her that these bots are for her. She's really excited as you explain their assignment."
    ""
    ""
    "When you finish explaining things she gives you a big hug and thanks you for taking care of her and her store. She says she can't wait to show them off to her customers."
  elif gn_which_pair==0:
    ""
    "{mark}[gn_store_owner_name]{/} is waiting for you when you arrive at the HQ and is really happy to receive the first pair of bots for the patrol. She's always upbeat, I really like her."
    ""
    ""
    "The capsules are already set up and the bots get into them so you can make sure they are working. {mark}[gn_store_owner_name]{/} is excited and you enjoy talking with her."
  elif gn_which_pair==1:
    ""
    "You're surprised again when {mark}[gn_store_owner_name]{/} jumps into your arms when you arrive at HQ. Wow, this feels great and I'm glad I didn't drop her! I really enjoy kissing her."
    ""
    ""
    "The bots get into the capsules and you make sure they're working. {mark}[gn_store_owner_name]{/} tells you that having two patrols will be so much better than one. I love her enthusiasm!"
  elif gn_which_pair==2:
    ""
    "{mark}[gn_store_owner_name]{/} is busy at the computer in the small office and doesn't hear you arrive. You say hello quietly so you don't scare her. She looks up and says to give her a minute."
    ""
    ""
    "The bots get into the capsules which are working perfectly. {mark}[gn_store_owner_name]{/} apologizes for being distracted, she was working on scheduling for three patrols and has a good system planned."
  ""
  choice("good_neighbor_delivery5") "Continue"
  return

label good_neighbor_delivery5:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  if gn_which_pair==-1:
    header "Neighborhood - Deliver Bots for {mark}[gn_store_owner_name]{/}"
  else:
    header "Neighborhood - Deliver Bots for the {mark}Neighborhood Patrol{/}"
  if gn_which_pair==-1:
    $first_picture=17
    $second_picture=18
  elif gn_which_pair==0:
    $first_picture=29
    $second_picture=30
  elif gn_which_pair==1:
    $first_picture=35
    $second_picture=36
  elif gn_which_pair==2:
    $first_picture=41
    $second_picture=42
  $act.start_block("l:400 c:content_width-400")
  $act.set_block("l")
  $action_image= "quests good_neighbors sgn_"+str(first_picture)
  center "{image=[action_image]@340x600}"
  ""
  $action_image= "quests good_neighbors sgn_"+str(second_picture)
  center "{image=[action_image]@340x600}"
  ""
  $act.set_block("c")
  if gn_which_pair==-1:
    "You tell the bots to begin their assignment and then ask {mark}[gn_store_owner_name]{/} if the bot capsules arrived. She smiles and says she has them in a room in her apartment building. I told her the bots know how to use them."
    ""
    ""
    "You stay long enough to be certain that {mark}[gn_store_owner_name]{/} knows what she needs to do and then you say goodbye and head back to the shop. I really like her and it feels good to help her."
  elif gn_which_pair==0:
    "When you're getting ready to head home {mark}[gn_store_owner_name]{/} surprised you with a passionate kiss! You're a little surprised and kissing is unfamiliar to you but it feels great. You don't get this from sexbots!"
    ""
    "While you're walking home you can't stop thinking about {mark}[gn_store_owner_name]'s{/} kiss, wow! You've always been a geek and don't have a lot of experience with girls let alone women. Maybe you should change that!"
  elif gn_which_pair==1:
    "When you're ready to head home you're better prepared when {mark}[gn_store_owner_name]{/} gives you another kiss, maybe you're getting the hang of this! The kiss lasts a little longer this time and feels even better!"
    ""
    "You wave to {mark}[gn_diner_owner_name]{/} as you pass his diner on the way home. He's always so upbeat, just like {mark}[gn_store_owner_name]{/}. It feels great to make friends and be part of your neighborhood."
  elif gn_which_pair==2:
    "You sit down with her and she tells you about it. There will be three shifts and two patrols will be on duty while one is recharging in capsules. It's a great plan and the neighborhood will be well protected. She's smart too!"
    ""
    "After the conversation with {mark}[gn_store_owner_name]{/} you head home. Along the way you stop to talk with {mark}[gn_diner_owner_name]{/}. He says it's obvious that {mark}[gn_store_owner_name]{/} likes me and I better keep visiting her!"
  ""
  $mc.mood.give_xp(25)                                ## 0.12.n addition  
  if mc_so_value<50:                                  ## 0.12.n addition: do NOT allow FWB until FWB quest end
    call mc_update_relation(gn_store_owner_name,2,0)  ## relationship gain for visiting
## remove bots from game
  $move_sexbot(gn_female_bot_selected,None)
  $bot=None
  $move_sexbot(gn_male_bot_selected,None)
  $bot=None
  $gn_which_pair+=1                    ## increment the delivery count each time a delivery is executed
  "You pay the bill for the {mark}bot capsules{/} with {mark}level 2 upgrades{/}."
  $mc.money-=56000
  $mc.give_xp("rep_neighborhood",10)   ## GIVING BOTS TO STORE OWNER OR PATROL IS NOTICED
  if gn_which_pair==3:                 ## quest is completed after 3rd patrol pair delivered
    $quests.goodneighbor.finish()
## 0.11.n added call to update mc's business skill
    call mc_update_business
  else:                                ## quest advances after all other pairs
    $quests.goodneighbor.advance()
  choice("goto_home") "Continue"       ## last screen, 'goto_home'
  return