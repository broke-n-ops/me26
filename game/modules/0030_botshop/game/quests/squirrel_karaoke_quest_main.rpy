init python:

##=========INIT VARIABLES=========
  sr_attended_today=0               ##  0.15.n set to day value when attending, 'karaoke' button greyed out if value matches day value
  sr_bot_minimum=4                  ##  need a C level bot for karaoke
  sr_cpu_minimum="CBAS"             ##  need a C level CPU - lots of processing: sing, entertain, adjust to audience reaction
  sr_vocoder_minimum="CBAS"         ##  need a C level vocoder - sing
  sr_powercore_minimum="CBAS"       ##  need a C level powercore - support processing and strong singing voice
  sr_social_skill_minimum="CBAS"    ##  need a C level social skill - understanding how to act human
  sr_karaoke_teacher_visit=0        ##  set to 1 when teacher visits to prevent reoccurrance
##  ns_teacher_relation_value=0     ##  0.11.n - replaced in 'mc_relationships.rpy': mc_nst_value
  sr_teacher_threshold=31           ##  0.11.n - set to 31 which is minimum for flirting as defined in 'mc_relationships.rpy'
  sr_first_karaoke=0                ##  set to 1 when when you complete your first competition, you can't win the first one
  sr_karaoke_wins=0                 ##  increment each time you win
  sr_karaoke_congrats=0             ##  flag for teacher congratulations on completing quest
  sr_karaoke_chance=0               ##  for random number generation; selecting pictures and determining win or lose
  sr_karaoke_win=0                  ##  set to 1 when you determine a win, set to 0 when you determine a loss
  sr_karaoke_bot=0                  ##  Bot class number
  sr_karaoke_bot_weight=2           ##  Bot weight is 1, could be adjusted
  sr_karaoke_cpu=0                  ##  weighted CPU class number
  sr_karaoke_cpu_weight=1           ##  CPU weight is 1, could be adjusted
  sr_karaoke_vocoder=0              ##  weighted Vocoder class number
  sr_karaoke_vocoder_weight=6       ##  Vocoder weight is 6, could be adjusted
  sr_karaoke_powercore=0            ##  weighted Powercore class number
  sr_karaoke_powercore_weight=1     ##  Powercore weight is 6, could be adjusted
  sr_karaoke_socialskill=0          ##  weighted Social Skill number
  sr_karaoke_socialskill_weight=6   ##  Social Skill weight is 6, could be adjusted
  sr_karaoke_integrity=0            ##  weighted Integrity number
  sr_karaoke_integrity_weight=0.25  ##  Integrity weight is 6, could be adjusted
  sr_karaoke_stability=0            ##  weighted Stability number
  sr_karaoke_stability_weight=0.50  ##  Stability weight is 6, could be adjusted
  sr_karaoke_base_parameters=4      ##  all bot parameters are 'C'
  sr_karaoke_base_value=0           ##  weighted value of bot with all base level parameters (ignoring integrity and stability) - by definition cannot win, must exceed minimum!!
  sr_karaoke_win_chance=0           ##  final value to compare random number to for win or lose
                                    ##  Formula:  Bot*BotWeight+CPU*CPUWeight+Vocoder*VocoderWeight+Powercore*PowercoreWeight+SocialSkill*SocialSkillWeight-Base-(100-Integrity)*IntegrityWeight-(100-Stabilility)*StabilityWeight
  sr_karaoke_teacher_win=0          ##  if you lose teacher has a 50% chance of winning, otherwise she comes in second and still beats you
  sr_karaoke_treat_cost=400         ##  2 $100 entry fees plus drinks & tips for 2
  sr_karaoke_dutch_cost=200         ##  $100 entry fee plus drinks & tips

##=====CREATE CLASS FOR QUEST=====

  class Quest_karaoke(Quest):
    name="Karaoke Competition"

    class phase_1_introduction:
      description="""
        Competitions are on {mark}Wednesday Evenings{/}
        Minimum bot requirement:
        {mark}C level bot
        C level CPU, Vocoder, and Powercore parts
        C level Social skill{/}
        I suspect {mark}Integrity{/} and {mark}Psychocore Stability{/} matter

        """

    class phase_2_attended:
      description="""
        Competitions are on {mark}Wednesday Evenings{/}
        Minimum bot requirement:
        {mark}C level bot
        C level CPU, Vocoder, and Powercore parts
        C level Social skill{/}
        I suspect {mark}Integrity{/} and {mark}Psychocore Stability{/} matter
        Wins: {mark}0 of 3{/}

        """

    class phase_3_win1:
      description="""
        Competitions are on {mark}Wednesday Evenings{/}
        Minimum bot requirement:
        {mark}C level bot
        C level CPU, Vocoder, and Powercore parts
        C level Social skill{/}
        I suspect {mark}Integrity{/} and {mark}Psychocore Stability{/} matter
        Wins: {mark}1 of 3{/}

        """

    class phase_4_win2:
      description="""
        Competitions are on {mark}Wednesday Evenings{/}
        Minimum bot requirement:
        {mark}C level bot
        C level CPU, Vocoder, and Powercore parts
        C level Social skill{/}
        I suspect {mark}Integrity{/} and {mark}Psychocore Stability{/} matter
        Wins: {mark}2 of 3{/}

        """

    class phase_1000_karaoke_done:
      description="""
        I won the bet with the teacher but I can still participate for fun
        Competitions are on {mark}Wednesday Evenings{/}
        Minimum bot requirement:
        {mark}C level bot
        C level CPU, Vocoder, and Powercore parts
        C level Social skill{/}
        I suspect {mark}Integrity{/} and {mark}Psychocore Stability{/} matter

        """

    # # class phase_1000_karaoke_done:
      # # description="""
        # # The sponsors decided to stop running the karaoke competition.
        # # Too bad, but maybe they will start another type of competition.
        
        # # """
    class phase_2000_karaoke_failed:           ##  placeholder, this cannot happen
      description="You are stupid!"

##======================================================
##=========BORDER WITH EVENT HANDLING FUNCTION==========
##======================================================

init python hide:
  @event_handler("time_advanced")
  def karaoke_event():
    if now("sunday","morning"):                ##  time for teacher visit if...
      if sr_karaoke_teacher_visit==0:          ##  if visit hasn't happened yet...
        if quests.nightschool.finished:        ##  ...night school finished
          queue_event("quest_karaoke_event0")  ##  teacher comes to make karaoke challenge and starts event

##  MAKE KARAOKE HAPPEN OFTEN FOR TESTING PURPOSES
##    if now("evening"):                           ##  EVERY EVENING FOR TESTING
    if now("wednesday","evening"):             ##  competitions are on Wednesday evenings
      if quests.karaoke=="introduction":
        queue_event("quest_karaoke_event1")    ##  you have not attended a competion yet
      if quests.karaoke=="attended":
        queue_event("quest_karaoke_event2")    ##  you attended at least one competion
      if quests.karaoke=="win1":
        queue_event("quest_karaoke_event3")    ##  you have won 1 competition
      if quests.karaoke=="win2":
        queue_event("quest_karaoke_event4")    ##  you have won 2 competitions
      if quests.karaoke=="karaoke_done":
        queue_event("quest_karaoke_event5")    ##  you completed the quest but can still attend if you want
  return

##======================================================
##===========BORDER WITH QUEST FUNCTIONS================
##======================================================

## THIS BUTTON WAS NOT ADDED BECAUSE IT IS A BAD IDEA!!!
## LEFT THE FUNCTION HERE SHOULD SOMETHING CHANGE MAKING IT A GOOD IDEA
##  0.15.n add function to make karaoke visits a button instead of an event
##  when doing this the event handler must not call functions event1 through event5

# # label karaoke_button:
  # # $global sr_attended_today
  # # if quests.karaoke.started and now("wednesday","evening"):  ## 'started' remains TRUE even after the quest is finished

# # ##  if quest.karake.started and now("evening"):              ## ALTERNATE LINE FOR TESTING ONLY - EVERY DAY
  
    # # if sr_attended_today==now.day:                           ## last attendance was today, grey out button
      # # choice(None,pos=16, hint="(show over)") "Karaoke"
    # # else:                                                    ## haven't attended today, button active
      # # if mc.energy<3 or mc.money<200:                        ## not enough energy or money
        # # choice(None,hint="$200,3AP",pos=16) "Karaoke"
      # # else:
        # # choice("karaoke_select_bot",hint="$200,3AP",pos=16) "Karaoke"  ## not using quest event handler so separate functions obsolete
  # # return

## UNDONE!!!!  0.15.n end of inserted function
## END OF ABANDONED FUNCTION

label quest_karaoke_event0:           ## teacher comes to the shop to issue a karaoke challenge
  $game_bg="home workspace"
  header "Night School Teacher Visits the Shop"
  ##  GRAPHICS 4 fixed pictures - only shown once per game
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests karaoke_club srk_1" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests karaoke_club srk_2"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests karaoke_club srk_3"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests karaoke_club srk_4"
  center "{image=[action_image]@400x600}"
  ##  TEXT next lines sets text on the right - 4 pictures: she arrives, talk over coffee, she leaves, think afterwards
  $act.set_block("c")
  ""
  "I heard the door open and was surprised to see {mark}[ns_teacher_name]{/}, the night school teacher, walking in. I've been trying to come up with an excuse to see her again. I'm glad she came!"
  ""
  ""
  "I offered her some coffee and we sat down to talk.  She told me about about a {mark}bot karaoke competition{/} on {mark}Wednesday evenings{/}. She enters a bot every week and said if I did too my {mark}social skill{/} training would improve."
  ""
  "As she was leaving she said;"
  ""
  "{say}I bet you can't win 3 times! If you want to try you'll need at least a{/} {mark}C level bot{/} {say}with{/} {mark}C level CPU, Vocoder, and Powercore{/}{say}, and{/} {mark}C level social skill{/}{say}.{/}"
  ""
  ""
  "I sure enjoyed seeing her again, it might be worth it just to hang out with her! I don't know about training a bot to do karaoke though, what a crazy idea. I bet {mark}Integrity and Stability{/} also matter!"
  ""
  $sr_karaoke_teacher_visit=1          ##  set flag to prevent reoccurance
  $quests.start_quest("karaoke")
  choice("advance_time") "Continue"
  return

label quest_karaoke_event1:    ##  you have NOT attended a karaoke competition yet
  $game_bg="home workspace"
  header "Time for the Karaoke Competition"
  
  ##  GRAPHICS 2 fixed pictures
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests karaoke_club srk_41" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image="quests karaoke_club srk_3"
  center "{image=[action_image]@400x600}"

  ##  TEXT next lines sets text on the right - 2 pictures: thinking at computer, remembering teacher
  $act.set_block("c")
  ""
  "The {mark}karaoke competition{/} that {mark}[ns_teacher_name]{/} told me about is happening this evening. It will cost me at least {mark}$200{/} and will take {mark}most of the evening{/}."
  ""
  ""
  ""
  "I remember that {mark}[ns_teacher_name]{/} sure looked good when she came to my shop."
  if mc.energy>=3 and mc.money>=200:
    extend " I'm not sure about this but I might have fun and learn something. Should I go to the competition?"
    choice("karaoke_select_bot",hint="3AP, $200") "Yes"
    choice("<<<") "No"
  else:
    if mc.energy<<3 and mc.money<<200:
     "Nah, it's too late. I can't get there in time and I don't have enough money anyway."
    elif mc.energy<<3:
      "Nah, it's too late for me to get there in time."
    else:    ##  not enough money
      "What am I thinking? I don't have enough money to do this!"
    choice("<<<") "Continue"
  return

label quest_karaoke_event2:     ##  you have attended a competition but have not won yet
  $game_bg="home workspace"
  header "Time for the Karaoke Competition"
  $global fwb_mc_new_clothes    ## 0=old, 1=new
  $global bp_first_sex_teacher
  $global mc_nst_date_counter
  
  $temp_int=random.randint(29,34)
  $action_image= "quests karaoke_club srk_"+str(temp_int)

  ##  GRAPHICS 2 fixed pictures
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests karaoke_club srk_41" 
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(29,34)
  $temp_text="quests karaoke_club srk_"+str(temp_int)
  if fwb_mc_new_clothes==1:  ## new clothes
    $temp_text=temp_text+"a"
  $action_image=temp_text
  center "{image=[action_image]@400x600}"

  ##  TEXT next lines sets text on the right - 2 pictures: thinking at computer, remembering teacher
  $act.set_block("c")
  ""
  "The {mark}karaoke competition{/} is happening again this evening. It was sort of fun last time but it will cost me at least {mark}$200{/} and will take {mark}most of the evening{/}."
  ""
  ""
  ""
  if mc.energy>=3 and mc.money>=200:    ## with 0 wins
    if bp_first_sex_teacher==0:         ## before sex with Simone
      "Last time I had a great time with {mark}[ns_teacher_name]{/} after the competition and I'm sure I'll learn something. Maybe my bot will get my {mark}first win in our bet{/} too! Should I go?"
    else:                               ## had sex with Simone
      "I always have a great time with {mark}[ns_teacher_name]{/} and I always learn something. It would be great if I {mark}get my first win{/} but it would be even better if we {mark}go to her place afterwards{/}. {mcsay}(Requires 3 additional AP){/}"
      ""
      if mc_nst_date_counter>=12:       ## add warning about relationship loss
        "I haven't seen {mark}[ns_teacher_name]{/} for a long time, {bad}our relationship might suffer{/} if I don't go this time. Should I go?"
      else:
        "Should I go?"
    choice("karaoke_select_bot",hint="3AP, $200") "Yes"
    choice("<<<") "No"
  else:
    if mc.energy<<3 and mc.money<<200:
      "Nah, it's too late. I can't get there in time and I don't have enough money anyway."
    elif mc.energy<<3:
      "Nah, it's too late for me to get there in time."
    else:    ##  not enough money
      "What am I thinking? I don't have enough money to do this!"
    choice("<<<") "Continue"
  return

label quest_karaoke_event3:     ##  you have attended a competition and have 1 win
  $game_bg="home workspace"
  header "Time for the Karaoke Competition"
  $global fwb_mc_new_clothes    ## 0=old, 1=new
  $global bp_first_sex_teacher
  $global mc_nst_date_counter
  
  ##  GRAPHICS 2 fixed pictures
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests karaoke_club srk_41" 
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(29,34)
  $temp_text="quests karaoke_club srk_"+str(temp_int)
  if fwb_mc_new_clothes==1:  ## new clothes
    $temp_text=temp_text+"a"
  $action_image=temp_text
  center "{image=[action_image]@400x600}"

  ##  TEXT next lines sets text on the right - 2 pictures: thinking at computer, remembering teacher
  $act.set_block("c")
  ""
  "The {mark}karaoke competition{/} is happening again this evening. I've won once, maybe I can do it again! It will cost me at least {mark}$200{/} and will take {mark}most of the evening{/}."
  ""
  ""
  ""
  if mc.energy>=3 and mc.money>=200:    ## with 1 win
    if bp_first_sex_teacher==0:         ## before sex with Simone
      "I always have a great time with {mark}[ns_teacher_name]{/} after the competition and I'm sure I'll learn something. Maybe my bot will get me {mark}another win in our bet{/} too. Should I go?"
    else:                               ## had sex with Simone
      "I always have a great time with {mark}[ns_teacher_name]{/} and I always learn something. It would be great if I {mark}get another win{/} but it would be even better if we {mark}go to her place afterwards{/}. {mcsay}(Requires 3 additional AP){/}"
      ""
      if mc_nst_date_counter>=12:       ## add warning about relationship loss
        "I haven't seen {mark}[ns_teacher_name]{/} for a long time, {bad}our relationship might suffer{/} if I don't go this time. Should I go?"
      else:
        "Should I go?"
    choice("karaoke_select_bot",hint="3AP, $200") "Yes"
    choice("<<<") "No"
  else:
    if mc.energy<<3 and mc.money<<200:
     "Nah, it's too late. I can't get there in time and I don't have enough money anyway."
    elif mc.energy<<3:
      "Nah, it's too late for me to get there in time."
    else:    ##  not enough money
      "What am I thinking? I don't have enough money to do this!"
    choice("<<<") "Continue"
  return

label quest_karaoke_event4:    ##  you have attended a competition and have 2 wins
  $game_bg="home workspace"
  header "Time for the Karaoke Competition"
  $global fwb_mc_new_clothes   ## 0=old, 1=new
  $global bp_first_sex_teacher
  $global mc_nst_date_counter
  
  ##  GRAPHICS 2 fixed pictures
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests karaoke_club srk_41" 
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(29,34)
  $temp_text="quests karaoke_club srk_"+str(temp_int)
  if fwb_mc_new_clothes==1:  ## new clothes
    $temp_text=temp_text+"a"
  $action_image=temp_text
  center "{image=[action_image]@400x600}"

  ##  TEXT next lines sets text on the right - 2 pictures: thinking at computer, remembering teacher
  $act.set_block("c")
  ""
  "The {mark}karaoke competition{/} is happening again this evening. I've won twice now, all I need is one more win! It will cost me at least {mark}$200{/} and will take {mark}most of the evening{/}."
  ""
  ""
  if mc.energy>=3 and mc.money>=200:    ## with 2 wins
    if bp_first_sex_teacher==0:         ## before sex with Simone
      "I always have a great time with {mark}[ns_teacher_name]{/} after the competition and I'm sure I'll learn something. Maybe I'll {mark}finally win the bet{/} this time too! Should I go?"
    else:                               ## had sex with Simone
      "I always have a great time with {mark}[ns_teacher_name]{/} and I always learn something. It would be great if I {mark}win the bet{/} but it would be even better if we {mark}go to her place afterwards{/}. {mcsay}(Requires 3 additional AP){/}"
      ""
      if mc_nst_date_counter>=12:       ## add warning about relationship loss
        "I haven't seen {mark}[ns_teacher_name]{/} for a long time, {bad}our relationship might suffer{/} if I don't go this time. Should I go?"
      else:
        "Should I go?"
    choice("karaoke_select_bot",hint="3AP, $200") "Yes"
    choice("<<<") "No"
  else:
    if mc.energy<<3 and mc.money<<200:
     "Nah, it's too late. I can't get there in time and I don't have enough money anyway."
    elif mc.energy<<3:
      "Nah, it's too late for me to get there in time."
    else:    ##  not enough money
      "What am I thinking? I don't have enough money to do this!"
    choice("<<<") "Continue"
  return

label quest_karaoke_event5:    ##  you won 3 times, the competition is over but you can still go just for fun
  $game_bg="home workspace"
  header "Time for the Karaoke Competition"
  $global fwb_mc_new_clothes   ## 0=old, 1=new
  $global bp_first_sex_teacher
  $global mc_nst_date_counter
  
  ##  GRAPHICS 2 fixed pictures
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests karaoke_club srk_41" 
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(29,34)
  $temp_text="quests karaoke_club srk_"+str(temp_int)
  if fwb_mc_new_clothes==1:  ## new clothes
    $temp_text=temp_text+"a"
  $action_image=temp_text
  center "{image=[action_image]@400x600}"

  ##  TEXT next lines sets text on the right - 2 pictures: thinking at computer, remembering teacher
  $act.set_block("c")
  ""
  "The {mark}karaoke competition{/} is happening again this evening. I've won three times so I won't get any benefit but I could go to hang out with {mark}[ns_teacher_name]{/}. It will cost me at least {mark}$200{/} and will take {mark}most of the evening{/}."
  ""
  ""
  if mc.energy>=3 and mc.money>=200:    ## with 3 wins, quest finished
    if bp_first_sex_teacher==0:         ## before sex with Simone
      "I always have a great time with {mark}[ns_teacher_name]{/} after the competition. She seems to like me, {mark}I wonder if I have a chance with her?{/} Should I go?"
    else:                               ## had sex with Simone
      "I always have a great time with {mark}[ns_teacher_name]{/} after the competition and it would be even better if we {mark}go to her place afterwards{/}. {mcsay}(Requires 3 additional AP){/}"
      ""
      if mc_nst_date_counter>=12:       ## add warning about relationship loss
        "I haven't seen {mark}[ns_teacher_name]{/} for a long time, {bad}our relationship might suffer{/} if I don't go this time. Should I go?"
      else:
        "Should I go?"  
    choice("karaoke_select_bot",hint="3AP, $200") "Yes"
    choice("<<<") "No"
  else:
    if mc.energy<<3 and mc.money<<200:
     "Nah, it's too late. I can't get there in time and I don't have enough money anyway."
    elif mc.energy<<3:
      "Nah, it's too late for me to get there in time."
    else:    ##  not enough money
      "What am I thinking? I don't have enough money to do this!"
    choice("<<<") "Continue"
  return

##=======================================================================
##=========BORDER WITH KARAOKE COMPETITION SUPPORTING FUNCTIONS==========
##=======================================================================

label karaoke_select_bot:
  $game_bg="home workspace"
  header "Time for the Karaoke Competition"
  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot: ## and bot.action_allowed("sell"):                          ##  NOT SURE ABOUT NEED FOR 'action_allowed': Works this way so leave it out
          if not bot["mission"]:                                            ##  bot isn't busy
            if bot.gender=="female":                                        ## female bots only
              if bot.chassis.integrity>0:                                   ##  integrity = 0 means disabled and unavailable!!!
                if bot.rate_level>=sr_bot_minimum:                          ##  bot rating
                  if bot.bot_social.level_name in sr_social_skill_minimum:  ##  social skill
                    part=bot.item_on_slot("bot_cpu")
                    if part.rate in sr_cpu_minimum:                         ##  CPU
                      part=bot.item_on_slot("bot_vocoder")
                      if part.rate in sr_vocoder_minimum:                   ##  vocoder
                        part=bot.item_on_slot("bot_powercore")
                        if part.rate in sr_powercore_minimum:               ##  powercore
                          bot_price=bot_price_function(bot)                 ##  Success! DO NOT OMIT, FOR SOME REASON THIS IS NEEDED!!
                          bots.append([bot,bot_price])                      ##  Success!
    bots=bots[:12]
  if bots:
    ""
    "{mark}There's no way I'm going to a club with a male sexbot!{/} These bots are qualified to be in the karaoke competition:"
    ""

##    "Starting Teacher Relationship: [mc_nst_value]"       ##  COMMENT OUT LATER!!

    ""
    $bot_n=0
    while bots:
      $bot,bot_price=bots.pop(0)
      $bot_n+=1
      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}, social skill: {mark}[bot.bot_social.level_name]{/}."
      choice("karaoke_outcome:{}".format(bot.id)) "Select #[bot_n]"
    $bot=None
  else:
    $bot=None
    ""
    "Unfortunately I have no bots qualified for the karaoke competition."
    ""
  $bots=None
  choice("<<<",pos=17,key="cancel") "Changed my mind"
  return

label karaoke_outcome(bot):                   ##  one outcome function works, use flags for special cases
  $bot=find_character(bot)
  $temp_int=random.randint(1,2)
  $game_bg="karaoke_club bg_karaoke_"+str(temp_int)
  header "Karaoke Competition"

## 0.15.n mark attendance to prevent attending more than once a day
  $global sr_attended_today
  $sr_attended_today=now.day

##  GRAPHICS next 2 lines set up the pictures on the left side
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $sr_karaoke_chance=random.randint(5, 7)     ##  arriving at the indie club
  $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
  if bp_first_sex_teacher==1:
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
  ""
  $sr_karaoke_chance=random.randint(8, 13)     ##  teacher's bot is singing
  $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
  if bp_first_sex_teacher==1:
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
  ""
  $sr_karaoke_chance=random.randint(14, 19)     ##  your bot is singing
  $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
  if bp_first_sex_teacher==1:
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
  ""

  ##  TEXT next lines sets text on the right
  $act.set_block("c")
  ##  4 pictures; arrive, teacher bot sing, MC bot sing, award on stage (all 3 possibilities)
  ""
  "When we arrived at {mark}El Mocando's{/} club {mark}[ns_teacher_name]{/} and her bot were already there. We joined them at their table and ordered drinks while waiting for the competition."
  ""
  ""
  ""
  "{mark}[ns_teacher_name]'s{/} bot went up on stage and I have to say she's good. You can tell it's a bot performing but sometimes you think the emotion is real. Pretty cool!"
  ""
  ""
  ""
  ""
  if sr_first_karaoke==0:  ## first time use special text
    "My bot went up on stage and I know she's not well prepared. I didn't know what these competitions are like but we'll be ready next time."
  else:
    "My bot went up on stage and I think she was pretty good. Not sure if she measures up to the others but we'll wait for the judges to decide."
  ""
  choice("karaoke_result:{}".format(bot.id)) "Who wins?"
  return

label karaoke_result(bot):
  $bot=find_character(bot)
  $temp_int=random.randint(1,2)
  $game_bg="karaoke_club bg_karaoke_"+str(temp_int)
  header "Karaoke Competition"
  $global mc_nst_value
  
  if sr_first_karaoke==0:                     ##  this is the MC's first competition, FLAG RESET AT END!!!
    $sr_karaoke_win=0                         ##  can't win first time regardless of bot
    $sr_karaoke_chance=random.randint(1, 2)   ##  find out if teacher wins
    if sr_karaoke_chance==1:
      $sr_karaoke_teacher_win=1               ##  teacher wins, she treats you
    else:
      $sr_karaoke_teacher_win=0               ##  teacher does NOT win, MC treat decision required
  else:                                       ##  this is NOT the MC's first competition...
    call karaoke_win_or_lose(bot)             ##  ...function to determine if you win or lose the competition this time
##  GRAPHICS next 2 lines set up the pictures on the left side
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if sr_karaoke_win==1:                          ##  you won
    $sr_karaoke_chance=random.randint(23, 25)    ##  MC and MCs bot on stage
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
  elif sr_karaoke_teacher_win==1:                ##  teacher wins
    $sr_karaoke_chance=random.randint(20, 22)    ##  MC and MCs bot on stage
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
  else:                                          ##  neither wins
    $sr_karaoke_chance=random.randint(26, 28)    ##  MC and MCs bot on stage
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"

  ##  TEXT next lines sets text on the right
  $act.set_block("c")
  ""
  if sr_karaoke_win==1:                             ##  you won - you pay for both of you (no option)
    "I was surprised when they announced that my bot won and we were invited up on stage to receive the prize. My bot did a pretty good acting job looking very excited!"
    ""
    if quests.karaoke<>"karaoke_done":              ##  haven't won 3 times yet
      $mc.give_xp("social",randint(2600,2800))      ##  mc gain social skill of advanced night school class
    $temp=calc_pr_rep_gain("rep_mc_trainer","l_g")  ##  trainer large GAIN - 0.012.n REVISION
    $mc.give_xp("rep_mc_trainer",temp)
    $bot.give_xp("bot_social",randint(175,250))     ##  bot gain social skill of advanced night school class
    $mc.mood.give_xp(randint(30,50))                ##  win, large mood increase
    $mc.money+=1000                                 ##  collect prize
    choice("karaoke_finish") "Your Treat!"
  elif sr_karaoke_teacher_win==1:                   ##  teacher wins - she pays for both of you (no option)
    "I guess it's no surprise, {mark}[ns_teacher_name]'s{/} bot won and they went up on stage. I think they've been up there before and her bot acts very natural, I like her approach!"
    ""
    if quests.karaoke<>"karaoke_done":           ##  haven't won 3 times yet
      $mc.give_xp("social",randint(900,1200))    ##  mc gain social skill of beginner night school class
    $bot.give_xp("bot_social",randint(25,100))   ##  bot gain social skill of beginner night school class
    $mc.mood.give_xp(randint(6,12))              ##  teacher pays, small mood increase
    choice("karaoke_finish") "Her Treat!"
  else:                                          ##  neither wins - you decide to treat teacher or go 'dutch'
    "Too bad, neither of our bots won. I'm disappointed, I thought {mark}[ns_teacher_name]'s{/} bot was the best. It doesn't seem to bother her though, she's always so easy going."
    ""
    if quests.karaoke<>"karaoke_done":           ##  haven't won 3 times yet
      $mc.give_xp("social",randint(900,1200))    ##  mc gain social skill of beginner night school class
    $bot.give_xp("bot_social",randint(25,100))   ##  bot gain social skill of beginner night school class
    $mc.mood.give_xp(randint(-12,-6))            ##  neither win, small mood decrease
    choice("karaoke_finish_treat",hint="$400") "Treat Teacher"
    choice("karaoke_finish_dutch",hint="$200") "Pay for Yourself"
  return

label karaoke_finish:                                    ## function called when eithe MC or Teacher wins
  $temp_int=random.randint(1,2)
  $game_bg="karaoke_club bg_karaoke_"+str(temp_int)
  header "Karaoke Competition"
  $global mc_nst_value
  
##  GRAPHICS next 2 lines set up the pictures on the left side
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if mc_nst_value<sr_teacher_threshold:                  ## below flirting level
    $sr_karaoke_chance=random.randint(29, 31)            ##  relax low relationship pose 1
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
    ""
    $sr_karaoke_chance+=2                                ##  relax low relationship pose 2
    if sr_karaoke_chance==31:                            ##  NO: 29>32; 30>33; 31>34
      $sr_karaoke_chance=34                              ##  29>31>34; 30>32; 31>33
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
    ""
    if sr_karaoke_wins==3 and sr_karaoke_congrats==0:    ##  on third win display extra picture completing quest, do NOT set flag until text!
      $sr_karaoke_chance+=1                              ##  increment last picture
      if sr_karaoke_chance==35:                          ##  loop back if necessary
        $sr_karaoke_chance=32
      $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
      if bp_first_sex_teacher==1:
        $action_image=action_image+"a"
      center "{image=[action_image]@400x600}"
  else:                                                  ## high relationship
    $sr_karaoke_chance=random.randint(35, 37)            ##  relax high relationship pose 1
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
    ""
    $sr_karaoke_chance+=2                                ##  relax high relationship pose 2
    if sr_karaoke_chance==37:                            ##  NO: 35>38; 36>39; 37>40
      $sr_karaoke_chance=40                              ##  35>37>40; 36>38; 37>39
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
    ""
    if sr_karaoke_wins==3 and sr_karaoke_congrats==0:    ##  on third win display extra picture completing quest, do NOT set flag until text!
      $sr_karaoke_chance+=1                              ##  increment last picture
      if sr_karaoke_chance==41:                          ##  loop back if necessary
        $sr_karaoke_chance=38
      $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
      if bp_first_sex_teacher==1:
        $action_image=action_image+"a"
      center "{image=[action_image]@400x600}"

  ##  TEXT next lines sets text on the right
  $act.set_block("c")
  ##  To reach this function either MC or teacher won - 2 pictures - 4 options: winner/relationship
  
## 0.15.n add new if... clause used after having sex with Simone (change previous if... to elif)
  if bp_first_sex_teacher==1:                            ## you've had sex with Simone and she will ask you to come home

## MC or Simone won - separate text
    if sr_karaoke_win==1:                                ##  you won - you are treating the teacher
      ""
      "As usual, we sit together on the couch at the other end of the room with our drinks and talk about the competition . Since I won it's my treat tonight. "
      ""
      ""
      ""
      if sr_karaoke_wins==3 and sr_karaoke_congrats==0:  ##  on third win display extra text completing quest
        $sr_karaoke_congrats=1                           ##  set flag to avoid repetition
        "{mark}[ns_teacher_name] congratulated me for 3 wins{/}. She said that I wouldn't benefit from the competitions any more but my bot would and she hopes I will continue attending."
        ""
        ""
        ""
      "After a few minutes {mark}[ns_teacher_name]{/} changes the subject; {say}Why don't we leave early and go to my place? I have plenty of time before teaching class tonight.{/}"
      ""
      "I'm pretty sure I know what she has in mind, should I go to her place?"
    elif sr_karaoke_teacher_win==1:                      ##  teacher wins - she pays for both of you (no option)
      ""
      "As usual, we sit together on the couch at the other end of the room with our drinks and talk about the competition . Since {mark}[ns_teacher_name]{/} won it's her treat tonight. "
      ""
      "After a few minutes {mark}[ns_teacher_name]{/} changes the subject; {say}Why don't we leave early and go to my place? I have plenty of time before the class tonight.{/}"
      ""
      "I'm pretty sure I know what she has in mind, should I go to her place?"
## end of 0.15.n insert, clause below changed to elif...
   
  elif mc_nst_value<sr_teacher_threshold:                ##  below flirting level
    if sr_karaoke_win==1:                                ##  you won - you are treating the teacher
      ""
      "After the competition we went to the other end of the club and sat down on the couches to discuss the competition. I really enjoy talking with {mark}[ns_teacher_name]{/}."
      ""
      ""
      ""
      "We talked for a long time and had a good time hanging out together. Since I won the competition I told her it was {mark}my treat tonight{/}. I can afford it since I'm still up $600 for the night."
      ""
      if sr_karaoke_wins==3 and sr_karaoke_congrats==0:  ##  on third win display extra text completing quest
        $sr_karaoke_congrats=1                           ##  set flag to avoid repetition
        ""
        "As we were getting ready to leave {mark}[ns_teacher_name] congratulated me for 3 wins{/}. She said that I wouldn't benefit from the competitions any more but my bot would and she hopes I will continue attending."
        ""
    elif sr_karaoke_teacher_win==1:                      ##  teacher wins - she pays for both of you (no option)
      ""
      "After the competition {mark}[ns_teacher_name]{/} told me it was {mark}her treat tonight{/} since she won. We went over to the couches on the other end of the club for another drink."
      ""
      ""
      ""
      "We talked about the competition for a while and then she asked how my shop was doing. I said it's doing well lately thanks to her because I have a big edge with social skill bot training."
      ""
  else:                                                  ##  high relationship
    if sr_karaoke_win==1:                                ##  you won - you are treating the teacher
      ""
      "After the competition we went to the other end of the club and sat down on the couches together. This feels like a date, {mark}[ns_teacher_name]{/} started flirting with me!"
      ""
      ""
      ""
      "We didn't talk much about the competition, instead we talked about ourselves. I enjoyed learning about her and she seemed interested in me too. Of course it was {mark}my treat tonight{/} since I won."
      ""
      if sr_karaoke_wins==3 and sr_karaoke_congrats==0:  ##  on third win display extra text completing quest
        $sr_karaoke_congrats=1                           ##  set flag to avoid repetition
        ""
        "As we were getting ready to leave {mark}[ns_teacher_name] congratulated me for 3 wins{/}. She said that I wouldn't benefit from the competitions any more but my bot would and she hopes I will continue attending."
        ""
    elif sr_karaoke_teacher_win==1:                      ##  teacher wins - she pays for both of you (no option)
      ""
      "After the competition {mark}[ns_teacher_name]{/} told me it was {mark}her treat{/} after winning. We went over to the couches and ordered another drink. I really like hanging out with her!"
      ""
      ""
      "We talked briefly about the competition and then started talking about ourselves. She has an interesting life and she's really hot. I enjoy flirting with her and she seems to enjoy it too!"
      ""
  $mc.energy-=3                                          ##  Energy used: 1 AP to get there, 2 AP for the show (similar to Raymond's)
  $mc.mood.give_xp(randint(6,12))                        ##  good conversation - small mood increase
  if sr_karaoke_win==1:                                  ##  MC won
    if mc_nst_value<45:                                  ##  Karaoke limit is mid-point of 'Flirting' (31-60)
      call mc_update_relation(ns_teacher_name,3,0)       ##  add 3 for MC win
    $mc.money-=sr_karaoke_treat_cost                     ##  treat teacher, pay for 2 - otherwise teacher won and treats you
    if sr_karaoke_wins==3:                               ##  Finish when 3 wins
      $quests.karaoke.finish()
    elif quests.karaoke<>"karaoke_done":                 ##  If not 'done' then 'advance
      $quests.karaoke.advance()
  else:                                                  ##  Teacher won
    if mc_nst_value<45:                                  ##  Karaoke limit is mid-point of 'Flirting' (31-60)
      call mc_update_relation(ns_teacher_name,2,0)       ##  add 2 for Teacher win and she treats
  $bot=None                                              ##  always clear bot from memory when finished

##  if first class increment counter and advance quest
  if sr_first_karaoke==0:                                ##  if this is first time... (cannot be a 'win' because cannot win first time no matter what)
    $sr_first_karaoke=1                                  ##  ...increment flag
    $quests.karaoke.advance()                            ##  ...advance quest
  $sr_karaoke_win=0                                      ##  reset MC win - not sure who won so reset them both
  $sr_karaoke_teacher_win=0                              ##  reset teacher win - not sure who won so reset them both

## 0.15.n create yes/no buttons for going home with Simone when needed
  if bp_first_sex_teacher==1:                            ## need yes/no buttons 
    choice("sd_arriving",cost=[("energy",3)]) "Yes"      ## Yes go home with Simone
    choice("karaoke_no_answer") "No"                     ## No leeds to new function
  else:
    choice("<<<") "Continue"
  return

label karaoke_finish_treat:                          ##  function called when neither MC nor Teacher win
  $temp_int=random.randint(1,2)
  $game_bg="karaoke_club bg_karaoke_"+str(temp_int)
  header "Karaoke Competition"
  $global mc_nst_value
##  GRAPHICS next 2 lines set up the pictures on the left side
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if mc_nst_value<sr_teacher_threshold:              ## below flirting level
    $sr_karaoke_chance=random.randint(29, 31)        ##  relax low relationship pose 1
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
    ""
    $sr_karaoke_chance+=2                            ##  relax low relationship pose 2
    if sr_karaoke_chance==31:                        ##  NO: 29>32; 30>33; 31>34
      $sr_karaoke_chance=34                          ##  29>31>34; 30>32; 31>33
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
  else:
    $sr_karaoke_chance=random.randint(35, 37)        ##  relax high relationship pose 1
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
    ""
    $sr_karaoke_chance+=2                            ##  relax high relationship pose 2
    if sr_karaoke_chance==37:                        ##  NO: 35>38; 36>39; 37>40
      $sr_karaoke_chance=40                          ##  35>37>40; 36>38; 37>39
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
  ##  TEXT next lines sets text on the right
  $act.set_block("c")
  ##  To reach this function neither of you won and you're treating - 2 pictures - 2 options - relationship
  
## 0.15.n add new if... clause used after having sex with Simone (change previous if... to elif)
  if bp_first_sex_teacher==1:                        ## you've had sex with Simone and she will ask you to come home
## neither won - treating Simone
    ""
    "As usual, we sit together on the couch at the other end of the room with our drinks and talk about the competition . Even though neither of us won it's my treat tonight."
    ""
    "After a few minutes {mark}[ns_teacher_name]{/} changes the subject; {say}Why don't we leave early and go to my place? I have plenty of time before teaching class tonight.{/}"
    ""
    "I'm pretty sure I know what she has in mind, should I go to her place?"
## end of 0.15.n insert, clause below changed to elif...

  elif mc_nst_value<sr_teacher_threshold:            ##  below flirting level
    ""
    "After the competition we went to the other end of the club and sat down on the couches to discuss the competition. I really enjoy talking with {mark}[ns_teacher_name]{/}."
    ""
    ""
    ""
    "We talked for a long time and had a good time hanging out together. Even though I didn't win the competition I told her it was {mark}my treat tonight{/}. Spending time with her is worth the extra expense!"
    ""
  else:                                              ##  high relationship
    ""
    "After the competition we went to the other end of the club and sat down on the couches together. This feels like a date, {mark}[ns_teacher_name]{/} started flirting with me!"
    ""
    ""
    ""
    "We didn't talk much about the competition, instead we talked about ourselves. I enjoyed learning about her and she seemed interested in me too. I didn't win tonight but I deciced to {mark}treat her anyway{/}, she's worth it!"
    ""
  $mc.energy-=3                                      ##  Energy used
  $mc.mood.give_xp(randint(6,12))                    ##  good conversation - small mood increase
  if mc_nst_value<45:                                ##  Karaoke limit is mid-point of 'Flirting' (31-60)
    call mc_update_relation(ns_teacher_name,2,0)     ##  neither MC nor Teacher won but you treated, add 2
  $mc.money-=sr_karaoke_treat_cost                   ##  treat teacher, pay for 2
  $bot=None                                          ##  always clear bot from memory when finished

##  if first class increment counter and advance quest
  if sr_first_karaoke==0:                            ##  if this is first time...
    $sr_first_karaoke=1                              ##  ...increment flag
    $quests.karaoke.advance()                        ##  ...advance quest

## 0.15.n create yes/no buttons for going home with Simone when needed
  if bp_first_sex_teacher==1:                        ## need yes/no buttons 
    choice("sd_arriving",cost=[("energy",3)]) "Yes"  ## Yes go home with Simone
    choice("karaoke_no_answer") "No"                 ## No leeds to new function
  else:
    choice("<<<") "Continue"
  return

label karaoke_finish_dutch:                          ## function called with neither teacher or MC win - dutch selected
  $temp_int=random.randint(1,2)
  $game_bg="karaoke_club bg_karaoke_"+str(temp_int)
  header "Karaoke Competition"
  $global mc_nst_value
##  GRAPHICS next 2 lines set up the pictures on the left side
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if mc_nst_value<sr_teacher_threshold:              ##  below flirting level
    $sr_karaoke_chance=random.randint(29, 31)        ##  relax low relationship pose 1
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
    ""
    $sr_karaoke_chance+=2                            ##  relax low relationship pose 2
    if sr_karaoke_chance==31:                        ##  NO: 29>32; 30>33; 31>34
      $sr_karaoke_chance=34                          ##  29>31>34; 30>32; 31>33
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
  else:
    $sr_karaoke_chance=random.randint(35, 37)        ##  relax high relationship pose 1
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"
    ""
    $sr_karaoke_chance+=2                            ##  relax high relationship pose 2
    if sr_karaoke_chance==37:                        ##  NO: 35>38; 36>39; 37>40
      $sr_karaoke_chance=40                          ##  35>37>40; 36>38; 37>39
    $action_image="quests karaoke_club srk_"+str(sr_karaoke_chance)
    if bp_first_sex_teacher==1:
      $action_image=action_image+"a"
    center "{image=[action_image]@400x600}"

  ##  TEXT next lines sets text on the right
  $act.set_block("c")
  ##  To reach this function neither of you won and you are NOT treating - 2 pictures 2 options - relationship

## 0.15.n add new if... clause used after having sex with Simone (change previous if... to elif)
  if bp_first_sex_teacher==1:                        ## you've had sex with Simone and she will ask you to come home
## neither won - dutch treat
    ""
    "As usual, we sit together on the couch at the other end of the room with our drinks and talk about the competition . Neither of us won and it's dutch treat tonight."
    ""
    "After a few minutes {mark}[ns_teacher_name]{/} changes the subject; {say}Why don't we leave early and go to my place? I have plenty of time before teaching class tonight.{/}"
    ""
    "I'm pretty sure I know what she has in mind, should I go to her place?"
## end of 0.15.n insert, clause below changed to elif...

  elif mc_nst_value<sr_teacher_threshold:            ##  below flirting level
    ""
    "After the competition we went to the other end of the club and sat down on the couches to discuss the competition. I really enjoy talking with {mark}[ns_teacher_name]{/}."
    ""
    ""
    ""
    "We talked for a long time and had a good time hanging out together. Money is a little tight right now so I didn't offer to treat her this time. {mark}She looks disappointed{/}, maybe that was a mistake."
    ""
  else:                                              ##  high relationship
    ""
    "After the competition we went to the other end of the club and sat down on the couches together. This feels like a date, {mark}[ns_teacher_name]{/} started flirting with me!"
    ""
    ""
    ""
    "We didn't talk much about the competition, instead we talked about ourselves. I enjoyed learning about her and she seemed interested in me too. Maybe I should have treated her, {mark}she looks disappointed{/}."
    ""
  $mc.energy-=3                                      ##  Energy used
  $mc.mood.give_xp(randint(-12,-6))                  ##  ended on bad note - small mood decrease
  call mc_update_relation(ns_teacher_name,-1,0)      ##  neither MC nor Teacher won AND you did NOT treat her, subtract 1
  $mc.money-=sr_karaoke_dutch_cost                   ##  going dutch, pay for 1
  $bot=None                                          ##  always clear bot from memory when finished

##  if first class increment counter and advance quest
  if sr_first_karaoke==0:                            ##  if this is first time...
    $sr_first_karaoke=1                              ##  ...increment flag
    $quests.karaoke.advance()                        ##  ...advance quest

## 0.15.n create yes/no buttons for going home with Simone when needed
  if bp_first_sex_teacher==1:                        ## need yes/no buttons 
    choice("sd_arriving",cost=[("energy",3)]) "Yes"  ## Yes go home with Simone
    choice("karaoke_no_answer") "No"                 ## No leeds to new function
  else:
    choice("<<<") "Continue"
  return

## 0.15.n function added for no answer required to lose relationship and mood
label karaoke_no_answer:
  $temp_int=random.randint(1,2)
  $game_bg="karaoke_club bg_karaoke_"+str(temp_int)
  header "Karaoke Competition"
  ##  GRAPHICS next 2 lines set up the pictures on the left side
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $temp_image=random.randint(42,43)
  $action_image= "quests karaoke_club srk_"+str(temp_image)+"a"
  center "{image=[action_image]@400x600}"
  ""
  $temp_image=random.randint(44,45)
  $action_image= "quests karaoke_club srk_"+str(temp_image)+"a"
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT next lines sets text on the right
  $act.set_block("c")
  ""
  "You tell {mark}[ns_teacher_name]{/} that you'd like to but you really can't do it tonight. She's surprised and I think she's even a little angry which makes me feel bad."
  ""
  ""
  ""
  "As you're leaving you think {mark}[ns_teacher_name]{/} looked very upset when you said goodbye. If I'm not prepared to go to her place maybe I shouldn't go to {mark}Karaoke{/} on Wednesdays."
  call mc_update_relation(ns_teacher_name,-2,0)  ## lose 2 relationship point
  $mc.mood.give_xp(randint(-50,-30))             ##  large mood decrease
  choice("<<<") "Continue"                        ## end karaoke takes you home I HOPE!!!
  return

##============================================
##=====WIN / LOSS DETERMINATION FUNCTION======
##============================================

##  COPY OF VARIABLES USED FOR CONVENIENCE

  # # # sr_karaoke_bot=0                  ##  Bot class number
  # # # sr_karaoke_bot_weight=2           ##  Bot weight is 1, could be adjusted
  # # # sr_karaoke_cpu=0                  ##  weighted CPU class number
  # # # sr_karaoke_cpu_weight=1           ##  CPU weight is 1, could be adjusted
  # # # sr_karaoke_vocoder=0              ##  weighted Vocoder class number
  # # # sr_karaoke_vocoder_weight=6       ##  Vocoder weight is 6, could be adjusted
  # # # sr_karaoke_powercore=0            ##  weighted Powercore class number
  # # # sr_karaoke_powercore_weight=1     ##  Powercore weight is 6, could be adjusted
  # # # sr_karaoke_socialskill=0          ##  weighted Social Skill number
  # # # sr_karaoke_socialskill_weight=6   ##  Social Skill weight is 6, could be adjusted
  # # # sr_karaoke_integrity=0            ##  weighted Integrity number
  # # # sr_karaoke_integrity_weight=0.25  ##  Integrity weight is 6, could be adjusted
  # # # sr_karaoke_stability=0            ##  weighted Stability number
  # # # sr_karaoke_stability_weight=0.50  ##  Stability weight is 6, could be adjusted
  # # # sr_karaoke_base_parameters=4      ##  all bot parameters are 'C'
  # # # sr_karaoke_base_value=0           ##  weighted value of all 'C' level bot (ignoring integrity and stability) - by definition cannot win, must exceed minimum!!
  # # # sr_karaoke_win_chance=0           ##  final value to compare random number to for win or lose
                                    # # # ##  Formula:  Bot*BotWeight+CPU*CPUWeight+Vocoder*VocoderWeight+Powercore*PowercoreWeight+SocialSkill*SocialSkillWeight-Base-(100-Integrity)*IntegrityWeight-(100-Stabilility)*StabilityWeight

label karaoke_win_or_lose(bot):
  $global mc_nst_value
  $bot=find_character(bot)
  $sr_karaoke_chance=random.randint(1, 100)  ##  generate a random integer from 1 to 100 for win/loss determination

##  TEST - DELETE LATER
  ## "random chance value"
  ## "  sr_karaoke_chance: [sr_karaoke_chance]"

##  get weighted parameters

  $sr_karaoke_bot=bot.rate_level*sr_karaoke_bot_weight                                            ##  bot parameter
  $sr_karaoke_cpu=bot.item_on_slot("bot_cpu").rate_level*sr_karaoke_cpu_weight                    ##  cpu parameter
  $sr_karaoke_vocoder=bot.item_on_slot("bot_vocoder").rate_level*sr_karaoke_vocoder_weight        ##  vocoder parameter
  $sr_karaoke_powercore=bot.item_on_slot("bot_powercore").rate_level*sr_karaoke_powercore_weight  ##  powercore parameter
  $sr_karaoke_socialskill=bot.bot_social.level*sr_karaoke_socialskill_weight                         ##  social skill parameter
  $sr_karaoke_integrity=bot.chassis.integrity                                                     ##  unweighted integrity parameter
  $sr_karaoke_stability=bot.psychocore.stability                                                  ##  unweighted stability parameter
  
##  calculate base - C level parameters
  $sr_karaoke_base_value=sr_karaoke_base_parameters*(sr_karaoke_bot_weight+sr_karaoke_cpu_weight+sr_karaoke_vocoder_weight+sr_karaoke_powercore_weight+sr_karaoke_socialskill_weight)

##  sum of weighted parameters (except integrity and stability) minus base 
  $sr_karaoke_win_chance=sr_karaoke_bot+sr_karaoke_cpu+sr_karaoke_vocoder+sr_karaoke_powercore+sr_karaoke_socialskill-sr_karaoke_base_value


  # # # "weighted parameters:"
  # # # "  bot: [sr_karaoke_bot]"
  # # # "  cpu: [sr_karaoke_cpu]"
  # # # "  vocoder: [sr_karaoke_vocoder]"
  # # # "  powercore: [sr_karaoke_powercore]"
  # # # "  social skill: [sr_karaoke_socialskill]"
  # # # $karaoke_temp=sr_karaoke_bot+sr_karaoke_cpu+sr_karaoke_vocoder+sr_karaoke_powercore+sr_karaoke_socialskill
  # # # "  sum: [karaoke_temp]"
  # # # "  base: [sr_karaoke_base_value]"
  # # # "  integrity: [sr_karaoke_integrity]"
  # # # "  stability: [sr_karaoke_stability]"
  # # # "chance before integrity and stability:"
  # # # "  sr_karaoke_win_chance: [sr_karaoke_win_chance]"


##  calculate win chance - apply integrity and stability
  $sr_karaoke_win_chance=sr_karaoke_win_chance-(100-sr_karaoke_integrity)*sr_karaoke_integrity_weight-(100-sr_karaoke_stability)*sr_karaoke_stability_weight

  # # # "apply integrity and stability"
  # # # "  final win chance: [sr_karaoke_win_chance]"

  if sr_karaoke_chance<=sr_karaoke_win_chance:
    $sr_karaoke_win=1                           ##  MC won, you will treat teacher
    $sr_karaoke_wins+=1                         ##  increment win count
  else:
    $sr_karaoke_win=0                           ##  MC did NOT win
    $sr_karaoke_chance=random.randint(1, 2)
    if sr_karaoke_chance==1:
      $sr_karaoke_teacher_win=1                 ##  Teacher won, she will treat you
    else:
      $sr_karaoke_teacher_win=0                 ##  Neither MC nor Teacher won, dutch decision needed later
  return