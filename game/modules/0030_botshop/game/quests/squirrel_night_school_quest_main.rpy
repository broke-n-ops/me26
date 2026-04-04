init python:

##  there are 3 courses with 'n' sessions where 'n' depends upon difficulty level, they get more expensive and more effective as you progress

  nightschool_course=0              ##  0=not started, 1=1st course, 2=2nd course, 3=3rd course
  nightschool_session=0             ##  n sessions per course, counter for attendance
  nightschool_sessionspercourse=3   ##  game difficulty dependent: 3-easy, 5-normal, 7-hard, 9-hardcore
  nightschool_current_course="x"    ##  will be 'beginning', 'intermediate', or 'advanced'
  nightschool_chance=0              ##  random number from 1 through 100 used to select outcomes
  nightschool_result="G"            ##  code for outcome, values are A through G
    ##  A did not make it to class, thugs destroyed bot
    ##  B did not make it to class, thugs damaged bot
    ##  C did not make it to class, home safe (ran away from thugs)
    ##  D made it to class (no thugs encountered), bot destroyed on way home
    ##  E made it to class (no thugs encountered), bot damaged on way home
    ##  F made it to class (no thugs encountered), home safe (thug missed shooting at bot)
    ##  G made it to class (no thugs encountered), home safe (no thugs encountered)
  nightschool_combat_skill="DCBAS"  ##  must be D+, affects possible bot_damage
  nightschool_integrity_minimum=60  ##  must be >=60, affects possible bot_damage
  ns_picturenumber=0                ##  stores number of a specific picture for display (obtained from random number generator)
  ns_backgroundnumber=0             ##  stores number of background screen to display, random 1 through 4
  ns_teacher_name="Simone"          ##  teacher needs a name - last name "Hall" but only used when reading her business card
  ns_teacher_rename=0               ##  set to 1 when when the teacher hands you her card and you read her name

##  SPECIAL LINES FOR TEST PURPOSES:
##  COMMENT OUT LINE IN 'nightschool_start_event' GIVING LOTS OF MONEY
##  CHANGE ACTIVE LINE FOR HEADER IN 'nightschool_gotoclass', 'nightschool_attendclass', AND 'nightschool_goinghome'

  class Quest_nightschool(Quest):
    name="Night School"
    class phase_1_idea:
      description="""
        Now that I've got my own shop maybe there are some things I should learn.
        Maybe there is a night school that I could go to?

        """

    class phase_2_introduction:
      description="""
        There is a {mark}night school{/} for training bots {mark}social skills{/}.
        An introduction to the course is on {mark}Sunday nights{/} and is {mark}free{/}.
        I need a {mark}combat trained{/} bot as an escort.

        """
    class phase_3_course1:
      description="""
        The {mark}Beginner course{/} on social skill training is on {mark}Wednesdays and Saturdays{/}.
        Each session will cost {mark}$1,500{/}.
        I need a {mark}bot to train{/} that is also {mark}combat trained{/} as an escort.
        I have attended {mark}[nightschool_session] of [nightschool_sessionspercourse]{/} classes in the Beginner course.

        """
    class phase_4_course2:
      description="""
        The {mark}Intermediate course{/} on social skill training is on {mark}Tuesdays and Fridays{/}
        Each session will cost {mark}$3,000{/}.
        I need a {mark}bot to train{/} that is also {mark}combat trained{/} as an escort.
        I have attended {mark}[nightschool_session] of [nightschool_sessionspercourse]{/} classes in the Intermediate course.

        """
    class phase_5_course3:
      description="""
        The {mark}Advanced course{/} on social skill training is on {mark}Mondays and Thursdays{/}.
        Each session will cost {mark}$4,500{/}.
        I need a {mark}bot to train{/} that is also {mark}combat trained{/} as an escort.
        I have attended {mark}[nightschool_session] of [nightschool_sessionspercourse]{/} classes in the Advanced course.

        """

    class phase_1000_nightschool_done:             ##  placeholder, will never be seen
      description="You completed all 3 courses."
      
    class phase_2000_nightschool_failed:           ##  placeholder, this cannot happen
      description="You are stupid!"

##===================BORDER WITH EVENT HANDLING FUNCTION===================

##  Note: Renaming teacher added after version 0.0.4
##        Must be hidden until teacher visits shop and MC meets her
##        Must be backward compatible: saves could be before, during, or after Night School quest
##        added in 0.8.n:
##          set teacher flag when she visits shop to tell you about her classes
##          put it in every night school event from 'introduction' on for old saves where quest is in progress
##          put it in the 'home workout' time advance handler for old saves after night school is over

init python hide:
  @event_handler("time_advanced")
  def nightschool_event():
    if not quests.nightschool.started:                         ## isolate 'not started' so following 'elif' clauses work
      if not quests.nightschool.finished:                      ## if it's finished we don't want to start it again
        if now("morning") and now.day>=13 :                    ## 0.11.3 moved to Saturday morning after first 'Framed!' payment to reduce gap
          queue_event("nightschool_start_event")
    elif quests.nightschool=="idea":
      if now("sunday","morning"):
        queue_event("quest_nightschool_event1")                ## teacher visit, course information
    elif quests.nightschool=="introduction":
      if now("sunday","night"):                                ## normal line
##      if now("night"):                                         ## line for testing
        queue_event("quest_nightschool_event2")                ## attend introduction
    elif quests.nightschool=="course1":
      if now("wednesday","night") or now("saturday","night"):  ## normal line
##      if now("night"):                                         ## line for testing
        queue_event("quest_nightschool_event3")                ## attend session course 1
    elif quests.nightschool=="course2":
      if now("tuesday","night") or now("friday","night"):      ## normal line
##      if now("night"):                                         ## line for testing
        queue_event("quest_nightschool_event4")                ## attend session course 2
    elif quests.nightschool=="course3":
      if now("monday","night") or now("thursday","night"):     ## normal line
##      if now("night"):                                         ## line for testing
        queue_event("quest_nightschool_event5")                ## attend session course 3
  return

##===================BORDER WITH EVENT FUNCTIONS===================

label nightschool_start_event:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests night_school ns_74" 
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "I had trouble sleeping last night, I kept thinking about the {mark}money the Syndicate demanded{/}. This shop has to be successful, {mark}I can't afford to fail!{/}"
  ""
  "Maybe there's a {mark}night school{/} nearby that can help me figure out how to run a business! Who am I kidding, I probably can't afford it anyway. I'll just have to figure it out on my own."
  ""
  if game.difficulty==1:              ##  Easy
    $nightschool_sessionspercourse=3
  elif game.difficulty==2:            ##  Normal
    $nightschool_sessionspercourse=6
  elif game.difficulty==3:            ##  Hard
    $nightschool_sessionspercourse=9
  elif game.difficulty==4:            ##  Hardcore
    $nightschool_sessionspercourse=12
  $quests.start_quest("nightschool")
  choice("<<<") "Continue"
  return
  
label quest_nightschool_event1:    ##  woman comes to shop, tells you intro is Sunday night
  $ns_teacher_rename=1             ##  activate teacher rename - FIRST TIME FOR NEW GAMES
  $game_bg="home workspace"
  header "Night School"
  ##  GRAPHICS 5 fixed pictures because it's only shown once per game
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests night_school ns_1" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests night_school ns_2"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests night_school ns_3"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests night_school ns_4"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests night_school ns_5"
  center "{image=[action_image]@400x600}"
  ##  TEXT next lines sets text on the right - not perfectly synced with pictures but length works
##  CHECK THIS!!!!!
  $act.set_block("c")
  "A hot babe came into the shop. I couldn't help but stare as she walked up to me and said:"
  ""
  "{say}Nice shop! I see you know what you're doing with bots. You've obviously got mechanics, electronics, and computers down. Like most men, you probably have fun doing the sex training too!{/}"
  ""
  "I was a little embarrassed, she's pretty bold! She noticed my embarrassment but went on:"
  ""
  "{say}With a shop in this neighborhood I'll bet you're good at combat training too but you probably have trouble with social skill training. Sorry but most bot jockeys are geeks and have trouble with social training. I can help with this and give you an edge with your competitors.{/}"
  ""
  "I had to admit she had a point and I could use an advantage with my bot business. I asked what she meant and she said:"
  ""
  "{say}I teach{/} {mark}bot social training classes{/}{say}, here's my card if you want to check it out. I give a{/} {mark}free introduction on Sunday nights{/}{say}. Unfortunately the neighborhood is sketchy so you'll need a bot escort with at least{/} {mark}'C' level combat training.{/}"
  ""
  if gn_retired_fighter_rename==0:  ## you haven't met Louis yet
    "I said I'd think about it and she smiled as she left the shop. Her card reads '{mark}[ns_teacher_name] Hall, Cognitive Robotics Institute{/}'. Sounds good but I'm worried about the need for an escort. I've heard about a {mark}retired fighter{/} who hangs out at the {mark}neighborhood bar{/}, maybe he can help me."
  else:                             ## you've met Louis
    "I said I'd think about it and she smiled as she left the shop. Her card reads '{mark}[ns_teacher_name] Hall, Cognitive Robotics Institute{/}'. Sounds good but I'm worried about the need for an escort. I should go to the {mark}neighborhood bar{/} and talk to {mark}[gn_retired_fighter_name]{/}, he'll help me out."
  ""
  call mc_update_relation(ns_teacher_name,1,0)
  $ns_training_advice=1             ## set flag to get special advice next time you go to the neighborhood bar
  $quests.nightschool.advance()     ##  next course
  choice("continue") "Continue"
  return

label quest_nightschool_event2:     ##  course introduction
  $ns_teacher_rename=1              ##  activate teacher rename - FOR OLD SAVES
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  
  header "Night School"
  "The introduction to the {mark}bot social skill training class{/} is going on tonight. {mark}[ns_teacher_name]{/},the teacher, said it's free but it will take time. As they say, 'time is money'."
  ""
  if mc.energy>=3:
    "Should I go to the introduction?"
    choice("quest_nightschool_introduction",hint="3AP") "Yes"
    choice("continue") "No"
  else:
    "You look at the time and see it's pretty late. You'd never make it in time, maybe next week."
    choice("continue") "Continue"
  return

label quest_nightschool_event3:    ##  course 1 available
  $ns_teacher_rename=1             ##  activate teacher rename - FOR OLD SAVES
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"
  "The {mark}Beginner course in bot social skill training{/} is going on tonight. It will take most of the night and costs $1,500."
  ""
  if mc.energy>=3 and mc.money>=1500:
    "Should I go to the class?"
    choice("quest_nightschool_course1",hint="3AP, $1,500") "Yes"
    choice("continue") "No"
  else:
    if mc.energy<<3 and mc.money <<1500:
     "It's too late, you can't get there in time and can't afford the course anyway."
    elif mc.energy<<3:
      "It's too late, you can't get there in time."
    else:    ##  not enough money
      "You don't have enough money to pay for the course."
    choice("continue") "Continue"
  return

label quest_nightschool_event4:    ##  course 2 available
  $ns_teacher_rename=1             ##  activate teacher rename - FOR OLD SAVES
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"
  "The {mark}Intermediate course in bot social skill training{/} is going on tonight. It will take most of the night and costs $3,000."
  ""
  if mc.energy>=3 and mc.money>=3000:
    "Should I go to the class?"
    choice("quest_nightschool_course1",hint="3AP, $3,000") "Yes"
    choice("continue") "No"
  else:
    if mc.energy<<3 and mc.money <<3000:
     "It's too late, you can't get there in time and can't afford the course anyway."
    elif mc.energy<<3:
      "It's too late, you can't get there in time."
    else:    ##  not enough money
      "You don't have enough money to pay for the course."
    choice("continue") "Continue"
  return

label quest_nightschool_event5:    ##  course 3 available
  $ns_teacher_rename=1             ##  activate teacher rename - FOR OLD SAVES
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"
  "The {mark}Advanced course in bot social skill training{/} is going on tonight. It will take most of the night and costs $4,500."
  ""
  if mc.energy>=3 and mc.money>=4500:
    "Should I go to the class?"
    choice("quest_nightschool_course1",hint="3AP, $4,500") "Yes"
    choice("continue") "No"
  else:
    if mc.energy<<3 and mc.money <<4500:
     "It's too late, you can't get there in time and you can't afford the course anyway."
    elif mc.energy<<3:
      "It's too late, you can't get there in time."
    else:    ##  not enough money
      "You don't have enough money to pay for the course."
    choice("continue") "Continue"
  return

##=====================BORDER WITH ATTENDING CLASS FUNCTIONS=====================

label quest_nightschool_introduction:
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"
  "{mark}[ns_teacher_name]{/}, the hot looking teacher, said I need a combat trained bot escort to go the the introduction. I'm looking forward to seeing her again!"
  ""
  call nightschool_select_escort_bot
  return

label quest_nightschool_course1:
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"
  "Theses classes are in a bad neighborhood so I need a combat trained bot escort. The bot will also get some social skill training."
  ""
  call nightschool_select_escort_bot
  return

label quest_nightschool_course2:
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"
  "Theses classes are in a bad neighborhood so I need a combat trained bot escort. The bot will also get some social skill training."
  ""
  call nightschool_select_escort_bot
  return

label quest_nightschool_course3:
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"
  "Theses classes are in a bad neighborhood so I need a combat trained bot escort. The bot will also get some social skill training."
  ""
  call nightschool_select_escort_bot
  return

##====================BORDER WITH SUPPORTING FUNCTIONS=========================

label nightschool_select_escort_bot:   ##  select escort bot

  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot:
          if bot.gender=="female":
            if not bot["mission"]:
              if bot.chassis.integrity>=nightschool_integrity_minimum:
                if bot.bot_combat.level_name in nightschool_combat_skill:
                  bot_price=bot_price_function(bot)                        ##  DO NOT OMIT
                  bots.append([bot,bot_price])                             ##  DO NOT OMIT
    bots=bots[:12]
  if bots:
    "{mark}There is no way I'm walking around town with a male sexbot!{/} Fortunately these {mark}female bots{/} are qualified escorts for attending night school:"
    ""
    $bot_n=0
    while bots:
      $bot,bot_price=bots.pop(0)
      $bot_n+=1
      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}, combat skill: {mark}[bot.bot_combat.level_name]{/}."
      choice("nightschool_outcome:{}".format(bot.id)) "Select #[bot_n]"
    $bot=None
  else:
    $bot=None
    "Unfortunately I have no {mark}female bots{/} qualified to escort me to night school and {mark}there is no way I'm walking around town with a male sexbot even if it is combat trained!{/}"
    ""
##    choice("<<<") "Continue"
  $bots=None
  choice("<<<",pos=17,key="cancel") "Changed my mind"
  return

label nightschool_outcome(bot):                 ##  attended (0,1) - bot_damage (0=none, 1=damage before, 2=death before, 3=damage after, 4=death after)
  $bot=find_character(bot)
  if quests.nightschool=="introduction":        ## introduction only
    $nightschool_chance=random.randint(51, 100) ## guaranteed to attend class, slight chance for bot damage/destroy
  else:                                         ## actual classes
    $nightschool_chance=random.randint(1, 100)  ## all classes except introduction
  if bot.bot_combat.level_name=="D":  
    if bot.chassis.integrity<80:       ##  D rating - low integrity
      if nightschool_chance<=10:       ##  10% miss class, bot destroyed
        $nightschool_result="A"
      elif nightschool_chance<=30:     ##  20% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=50:     ##  30% miss class, safe home (ran away)
        $nightschool_result="C"
      elif nightschool_chance<=60:     ##  10% attend class, bot destroyed
        $nightschool_result="D"
      elif nightschool_chance<=80:    ##  20% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=95:     ##  15% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  5% attend class, safe home (no thugs)
        $nightschool_result="G"
    else:                              ##  D rating - high integrity
      if nightschool_chance<=6:        ##  6% miss class, bot destroyed
        $nightschool_result="A"
      elif nightschool_chance<=18:     ##  12% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=50:     ##  32% miss class, safe home (ran away)
        $nightschool_result="C"
      elif nightschool_chance<=56:     ##  6% attend class, bot destroyed
        $nightschool_result="D"
      elif nightschool_chance<=68:    ##  12% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=86:     ##  18% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  14% attend class, safe home (no thugs)
        $nightschool_result="G"
  elif bot.bot_combat.level_name=="C":
    if bot.chassis.integrity<80:       ##  C rating - low integrity
      if nightschool_chance<=6:        ##  6% miss class, bot destroyed
        $nightschool_result="A"
      elif nightschool_chance<=18:     ##  12% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=40:     ##  22% miss class, safe home (ran away)
        $nightschool_result="C"
      elif nightschool_chance<=46:     ##  6% attend class, bot destroyed
        $nightschool_result="D"
      elif nightschool_chance<=58:    ##  12% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=76:     ##  18% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  24% attend class, safe home (no thugs)
        $nightschool_result="G"
    else:                              ##  C rating - high integrity
      if nightschool_chance<=4:        ##  4% miss class, bot destroyed
        $nightschool_result="A"
      elif nightschool_chance<=14:     ##  10% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=40:     ##  26% miss class, safe home (ran away)
        $nightschool_result="C"
      elif nightschool_chance<=44:     ##  4% attend class, bot destroyed
        $nightschool_result="D"
      elif nightschool_chance<=54:    ##  10% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=69:     ##  15% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  31% attend class, safe home (no thugs)
        $nightschool_result="G"
  elif bot.bot_combat.level_name=="B":
    if bot.chassis.integrity<80:       ##  B rating - low integrity
      if nightschool_chance<=4:        ##  4% miss class, bot destroyed
        $nightschool_result="A"
      elif nightschool_chance<=14:     ##  10% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=30:     ##  16% miss class, safe home (ran away)
        $nightschool_result="C"
      elif nightschool_chance<=34:     ##  4% attend class, bot destroyed
        $nightschool_result="D"
      elif nightschool_chance<=44:    ##  10% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=59:     ##  15% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  41% attend class, safe home (no thugs)
        $nightschool_result="G"
    else:                              ##  B rating - high integrity
      if nightschool_chance<=2:        ##  2% miss class, bot destroyed
        $nightschool_result="A"
      elif nightschool_chance<=10:     ##  8% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=30:     ##  20% miss class, safe home (ran away)
        $nightschool_result="C"
      elif nightschool_chance<=32:     ##  2% attend class, bot destroyed
        $nightschool_result="D"
      elif nightschool_chance<=40:    ##  8% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=52:     ##  12% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  48% attend class, safe home (no thugs)
        $nightschool_result="G"
  elif bot.bot_combat.level_name=="A":
    if bot.chassis.integrity<80:       ##  A rating - low integrity
      if nightschool_chance<=2:        ##  2% miss class, bot destroyed
        $nightschool_result="A"
      elif nightschool_chance<=10:     ##  8% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=20:     ##  10% miss class, safe home (ran away)
        $nightschool_result="C"
      elif nightschool_chance<=22:     ##  2% attend class, bot destroyed
        $nightschool_result="D"
      elif nightschool_chance<=30:    ##  8% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=42:     ##  12% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  58% attend class, safe home (no thugs)
        $nightschool_result="G"
    else:                              ##  A rating - high integrity
##  no chance of miss class, bot destroyed ("A" outcome)
      if nightschool_chance<=6:        ##  6% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=20:     ##  14% miss class, safe home (ran away)
        $nightschool_result="C"
##  no chance of attend class, bot destroyed ("D" outcome)
      elif nightschool_chance<=26:    ##  6% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=35:     ##  9% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  65% attend class, safe home (no thugs)
        $nightschool_result="G"
  elif bot.bot_combat.level_name=="S":
    if bot.chassis.integrity<80:       ##  S rating - low integrity
##  no chance of miss class, bot destroyed ("A" outcome)
      if nightschool_chance<=3:        ##  3% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=10:     ##  7% miss class, safe home (ran away)
        $nightschool_result="C"
##  no chance of attend class, bot destroyed ("D" outcome)
      elif nightschool_chance<=13:    ##  3% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=20:     ##  7% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  80% attend class, safe home (no thugs)
        $nightschool_result="G"
    else:                              ##  S rating - high integrity
##  no chance of miss class, bot destroyed ("A" outcome)
      if nightschool_chance<=2:        ##  2% miss class, bot damaged
        $nightschool_result="B"
      elif nightschool_chance<=5:      ##  3% miss class, safe home (ran away)
        $nightschool_result="C"
##  no chance of attend class, bot destroyed ("D" outcome)
      elif nightschool_chance<=7:     ##  2% attend class, bot damaged
        $nightschool_result="E"
      elif nightschool_chance<=10:     ##  3% attend class, safe home (thug missed shot)
        $nightschool_result="F"
      else:                            ##  90% attend class, safe home (no thugs)
        $nightschool_result="G"
  call nightschool_gotoclass(bot)
  return

##==============BORDER WITH GO TO CLASS FUNCTION======================

label nightschool_gotoclass(bot):
  $bot=find_character(bot)
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"            ##  this line is for the real release
##  header "Night School - Random Result: [nightschool_result]"    ##  this line is for test releases
  $mc.energy-=3                          ##  Energy used even if you don't make it to class
##  BEGIN INTRODUCTION
  if quests.nightschool=="introduction":
    if nightschool_result=="A":         ##  did not attend, bot destroyed
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_a_pictures
      ##  TEXT next lines sets text on the right, 5 picture 5 lines
      $act.set_block("c")
      "Walking to class we saw a group of thugs in front of us. They were armed and looked dangerous. {mark}[ns_teacher_name]{/} wasn't kidding when she told me this was a {bad}bad neighborhood.{/}"
      ""
      ""
      ""
      "We stopped when the thug in the middle told us we should turn around and leave their territory. The other thugs looked at my escort bot, I'm sure they were thinking of what they'd like to do with her."
      ""
      ""
      "Before I could do anything, my escort bot surprised all of us by {mark}punching one of the thugs in the face{/}, he went down hard. She's a combat trained bot but this was a bad idea so I turned and ran."
      ""
      ""
      ""
      "She quickly turned around and kicked another thug in the nuts but while she did this the last thug {bad}pulled his shotgun and shot her{/}. It sure was a good thing that I decided to run!"
      ""
      ""
      "I risked looking back as I ran and saw {bad}the thug shoot her again{/}. God I hate losing bots like this! At least I made it home in one piece but if I want to go to these classes I need a new escort."
      if bot.bot_combat.level_name=="A":      ## NOTE: S bots cannot have outcome A
        extend " I guess even an {mark}A level combat bot{/} isn't always enough!" 
      elif bot.bot_combat.level_name=="B":
        extend " I thought a {mark}B level combat bot{/} would be good enough."
      elif bot.bot_combat.level_name=="C":
        extend " Maybe I need even better than a {mark}C level combat bot{/}."
      else:  ## must be D
        extend " The teacher was right, a {mark}D level combat bot{/} isn't enough."
      $move_sexbot(bot,None)
    elif nightschool_result=="B":       ##  did not attend, bot damaged
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_b_pictures
      ##  TEXT next lines sets text on the right, 5 pictures 5 lines
      $act.set_block("c")
      "Walking to class we saw a group of thugs in front of us. They were armed and looked dangerous. {mark}[ns_teacher_name]{/} wasn't kidding when she told me this was a {bad}bad neighborhood{/}."
      ""
      ""
      ""
      "We stopped when the thug in the middle told us we should turn around and leave their territory. The other thugs looked at my escort bot, I'm sure they were thinking of what they'd like to do with her."
      ""
      ""
      "Before I could do anything, my escort bot surprised all of us by {mark}punching one of the thugs in the face{/}, he went down hard. She's a combat trained bot but this was a bad idea so I turned and ran."
      ""
      ""
      ""
      "She turned to her left and kicked another thug in the nuts but while she did this the last thug {bad}sliced her shoulder with his huge knife{/}. It sure was a good thing that I decided to run!"
      ""
      ""
      "I risked looking back as I ran and saw {mark}my escort bot turn and run{/}. Her arm was hanging limp as she ran but no one chased her and we made it home."
      ""
      "I have work to do because {bad}[bot.heshe] was damaged{/} giving us time to escape."
      if bot.bot_combat.level_name=="S":
        extend " I'll repair {mark}[bot]{/} and all I can do is hope for better luck next time."
      elif bot.bot_combat.level_name=="A":
        extend " I'll repair {mark}[bot]{/} for next time. Maybe {mark}S level combat skill{/} would help." 
      elif bot.bot_combat.level_name=="B":
        extend " I'll repair {mark}[bot]{/} for next time. I'm sure {mark}A level combat skill{/} would help."
      elif bot.bot_combat.level_name=="C":
        extend " I'll repair {mark}[bot]{/} for next time. I guess {mark}C level combat skill{/} isn't enough."
      else:  ## must be D
        extend " I'll repair {mark}[bot]{/} for next time. The teacher recommended at least {mark}C level combat skill{/}."
      $bot.chassis.apply_damage("training_combat",(15,45))
    elif nightschool_result=="C":       ##  did not attend, home safe
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_c_pictures
      ##  TEXT next lines sets text on the right, 3 pictures 3 lines
      $act.set_block("c")
      "Walking to class we saw a group of thugs in front of us. They were armed and looked dangerous. {mark}[ns_teacher_name]{/} wasn't kidding when she told me this was a {bad}bad neighborhood{/}."
      ""
      ""
      ""
      "We stopped when the thug in the middle told us we should turn around and leave their territory. The other thugs looked at my escort bot, I'm sure they were thinking of what they'd like to do with her."
      ""
      ""
      "My escort bot decided to run so she grabbed my hand and we started running away. The thugs started chasing us but we were faster than they were. Thank God the guy with the shotgun didn't use it!"
      ""
      "We made it home safely."
    else:                                ##  results D, E, F, and G all go to "nightschool_attendclass" so only enter code once
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_defg_pictures
      ##  TEXT next lines sets text on the right, 2 pictures 2 lines
      $act.set_block("c")
      "{mark}[ns_teacher_name]{/} wasn't kidding, the school sure is in a sketchy area. If I decide to take these classes I better be careful and {mark}always bring a good combat bot!{/}"
      ""
      ""
      ""
      ""
      "On the way there I wondered how she survives in this neighborhood but after seeing her army of combat bots I think she's pretty safe."
##  BEGIN COURSE 1
  elif quests.nightschool=="course1":
    if nightschool_result=="A":         ##  did not attend, bot destroyed
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_a_pictures
      ##  TEXT next lines sets text on the right, 5 pictures 5 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "Walking to class we ran into a group of thugs. They were armed, a spiked bat, a large knife, and a shotgun. It's just like {mark}[ns_teacher_name]{/} said, the classes are in a {bad}bad neighborhood.{/}"
      ""
      ""
      ""
      "They didn't move so we had to stop. The one in the middle told us to leave their territory. The others looked at my escort bot imagining what they would do with her after they chased me away."
      ""
      ""
      "Suddenly my escort bot surprised everyone by {mark}punching the thug on the right in the face{/}, he went down hard. I didn't like the direction this was going so I quickly turned and ran."
      ""
      ""
      ""
      "My bot turned around and kicked the thug on the right in the nuts. Bad choice, she hadn't touched the one with the shotgun.  He {bad}pulled his shotgun and shot her{/}. If I hadn't decided to run I'd be next!"
      ""
      ""
      "I risked looking back as I ran and saw {bad}the thug shoot her again{/}. God I hate losing bots like this! At least I made it home in one piece but if I want to go to these classes I need a new escort."
      if bot.bot_combat.level_name=="A":      ## NOTE: S bots cannot have outcome A
        extend " I guess even an {mark}A level combat bot{/} isn't always enough!" 
      elif bot.bot_combat.level_name=="B":
        extend " I thought a {mark}B level combat bot{/} would be good enough."
      elif bot.bot_combat.level_name=="C":
        extend " Maybe I need even better than a {mark}C level combat bot{/}."
      else:  ## must be D
        extend " The teacher was right, a {mark}D level combat bot{/} isn't enough."
      $move_sexbot(bot,None)
    elif nightschool_result=="B":       ##  did not attend, bot damaged
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_b_pictures
      ##  TEXT next lines sets text on the right, 5 pictures 5 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "Walking to class we ran into a group of thugs. They were armed, a spiked bat, a large knife, and a shotgun. It's just like {mark}[ns_teacher_name]{/} said, the classes are in a {bad}bad neighborhood.{/}"
      ""
      ""
      ""
      "They didn't move so we had to stop. The one in the middle told us to leave their territory. The others looked at my escort bot imagining what they would do with her after they chased me away."
      ""
      ""
      "Suddenly my escort bot surprised everyone by {mark}punching the thug on the right in the face{/}, he went down hard. I didn't like the direction this was going so I quickly turned and ran."
      ""
      ""
      ""
      "She turned to her kicked the thug with the shotgun in the nuts but while she did this the last thug {bad}sliced her shoulder with his huge knife{/}. Her arm doesn't look good, I'm glad that I decided to run!"
      ""
      ""
      "I risked looking back once more and I saw {mark}my escort bot turn and run{/}. Her arm looked useless but no one chased her and I expect her to make it home."
      ""
      "I have work to do because {bad}[bot.heshe] was damaged{/} giving us time to escape."
      if bot.bot_combat.level_name=="S":
        extend " I'll repair {mark}[bot]{/} and all I can do is hope for better luck next time."
      elif bot.bot_combat.level_name=="A":
        extend " I'll repair {mark}[bot]{/} for next time. Maybe {mark}S level combat skill{/} would help." 
      elif bot.bot_combat.level_name=="B":
        extend " I'll repair {mark}[bot]{/} for next time. I'm sure {mark}A level combat skill{/} would help."
      elif bot.bot_combat.level_name=="C":
        extend " I'll repair {mark}[bot]{/} for next time. I guess {mark}C level combat skill{/} isn't enough."
      else:  ## must be D
        extend " I'll repair {mark}[bot]{/} for next time. The teacher recommended at least {mark}C level combat skill{/}."
      $bot.chassis.apply_damage("training_combat",(15,45))
    elif nightschool_result=="C":       ##  did not attend, home safe
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_c_pictures
      ##  TEXT next lines sets text on the right, 3 pictures 3 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "While we were walking to class we ran into a group of armed and dangerous thugs. I really want to take these classes but why do the have to be in such a {bad}bad neighborhood{/}."
      ""
      ""
      ""
      "We had to stop when they didn't get out of our way.  One told us to turn around and leave their territory. The others looked at my bot, I'm sure they were thinking of what they would do with her."
      ""
      ""
      "My escort bot decided we were outnumbered so she grabbed my hand and we started running away. The thugs started to chase us but we were way faster than them. Good thing the guy with the shotgun didn't use it!"
      ""
      "We made it home safely."
    else:                                ##  results D, E, F, and G all go to "nightschool_attendclass" so only enter code once
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_defg_pictures
      ##  TEXT next lines sets text on the right, 2 pictures 2 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "Just like {mark}[ns_teacher_name]{/} said, the school sure is in a {bad}sketchy area{/}. If I continue taking these classes I have to be careful and always bring a good combat bot!"
      ""
      ""
      ""
      ""
      "It was great to arrive at the school and see her combat bot guards outside. There will be more inside, I don't even know how many she has!  At least we're safe in the classroom."
##  BEGIN COURSE 2
  elif quests.nightschool=="course2":
    if nightschool_result=="A":         ##  did not attend, bot destroyed
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_a_pictures
      ##  TEXT next lines sets text on the right, 5 pictures 5 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "Damn, this time there's a group of armed thugs waiting for us in the middle of the street. These are great classes but it sure sucks trying to get to them, this is a really {bad}bad neighborhood.{/}"
      ""
      ""
      ""
      "They didn't move so we had to stop. The thug in the middle told us to turn around and leave their territory. The other thugs looked at my bot. It wasn't hard to figure out what they were thinking!"
      ""
      ""
      "All of a sudden my bot {mark}punched one of the thugs in the face{/} and he went down hard. We are outnumbered and one of them has a shotgun so I didn't like our chances. I decided to turn tail and run!"
      ""
      ""
      ""
      "Next she turned around and kicked another thug in the nuts but this gave the last thug time to {bad}pull his shotgun and shoot her{/}. She went down immediately, I don't like her chances! Good thing I ran!"
      ""
      ""
      "I risked looking back as I ran and saw {bad}the thug shoot her again{/}. God I hate losing bots like this! At least I made it home in one piece but if I want to go to these classes I need a new escort."
      if bot.bot_combat.level_name=="A":      ## NOTE: S bots cannot have outcome A
        extend " I guess even an {mark}A level combat bot{/} isn't always enough!" 
      elif bot.bot_combat.level_name=="B":
        extend " I thought a {mark}B level combat bot{/} would be good enough."
      elif bot.bot_combat.level_name=="C":
        extend " Maybe I need even better than a {mark}C level combat bot{/}."
      else:  ## must be D
        extend " The teacher was right, a {mark}D level combat bot{/} isn't enough."
      $move_sexbot(bot,None)
    elif nightschool_result=="B":       ##  did not attend, bot damaged
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_b_pictures
      ##  TEXT next lines sets text on the right, 5 pictures 5 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "On our way to class we encountered a group of thugs in the road. They were armed and looked dangerous. These classes sure are in a {bad}bad neighborhood{/}. We hoped they would let us by."
      ""
      ""
      ""
      "Unfortunately they didn't move and we had to stop. One of them told us to turn around and leave their territory. The other thugs leered at my bot. They probably expected to have a good time with her!"
      ""
      ""
      "My bot surprised all of us by {mark}punching one of the thugs in the face{/}, he went down hard. She's a combat trained bot and has the element of surprise on her side but this was a bad idea. I turned and ran!"
      ""
      ""
      ""
      "She quickly turned to her left and kicked the thug with the shotgun in the nuts but while she did this the last thug {bad}sliced her shoulder with his huge knife{/} and her arm is limp. Good thing I decided to run!"
      ""
      ""
      "I risked another look back and I was happy to see {mark}my escort bot turn and run{/}. Her arm was hanging limp as she ran but no one chased her so I expect her to make it home."
      ""
      "I have work to do because {bad}[bot.heshe] was damaged{/} giving us time to escape."
      if bot.bot_combat.level_name=="S":
        extend " I'll repair {mark}[bot]{/} and all I can do is hope for better luck next time."
      elif bot.bot_combat.level_name=="A":
        extend " I'll repair {mark}[bot]{/} for next time. Maybe {mark}S level combat skill{/} would help." 
      elif bot.bot_combat.level_name=="B":
        extend " I'll repair {mark}[bot]{/} for next time. I'm sure {mark}A level combat skill{/} would help."
      elif bot.bot_combat.level_name=="C":
        extend " I'll repair {mark}[bot]{/} for next time. I guess {mark}C level combat skill{/} isn't enough."
      else:  ## must be D
        extend " I'll repair {mark}[bot]{/} for next time. The teacher recommended at least {mark}C level combat skill{/}."
      $bot.chassis.apply_damage("training_combat",(15,45))
    elif nightschool_result=="C":       ##  did not attend, home safe
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_c_pictures
      ##  TEXT next lines sets text on the right, 3 pictures 3 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "Damn, this time there's a group of armed thugs waiting for us in the middle of the street. These are great classes but it sucks trying to get to them, this sure is a {bad}bad neighborhood.{/}"
      ""
      ""
      ""
      "Unfortunately they didn't move so we stopped. One of them told us to turn around and leave their territory. The other thugs leered at my bot expecting to have a good time with her!"
      ""
      ""
      "My bot decided we should run so she grabbed my hand and we started running away. Even though the thugs started chasing us we ran faster. Thank God the guy with the shotgun didn't use it!"
      ""
      "We made it home safely."
    else:                                ##  results D, E, F, and G all go to "nightschool_attendclass" so only enter code once
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_defg_pictures
      ##  TEXT next lines sets text on the right, 2 pictures 2 lines
      $act.set_block("c")
## EDIT FOR FLAVOR, THIS IS FROM INTRODUCTION
      "Another trip to class through this {bad} incredibly bad neighborhood{/}. I always keep my eyes open on the way to class and bring a strong bot with me."
      ""
      ""
      ""
      ""
      "It always feels great when we see {mark}[ns_teacher_name]'s combat bots{/} guarding the entrance. She has so many of these things that I'm sure the local thugs are afraid of her."
##  BEGIN COURSE 3
  elif quests.nightschool=="course3":
    if nightschool_result=="A":         ##  did not attend, bot destroyed
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_a_pictures
      ##  TEXT next lines sets text on the right, 5 pictures 5 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "Walking to class we ran into a group of thugs. They were armed, a spiked bat, a large knife, and a shotgun. It's just like {mark}[ns_teacher_name]{/} said, the classes are in a {bad}bad neighborhood.{/}"
      ""
      ""
      ""
      "They didn't move so we had to stop. The one in the middle told us to leave their territory. The others looked at my escort bot imagining what they would do with her after they chased me away."
      ""
      ""
      "All of a sudden my bot {mark}punched one of the thugs in the face{/} and he went down hard. We are outnumbered and one of them has a shotgun so I didn't like ouf chances. I decided to turn tail and run!"
      ""
      ""
      ""
      "Next she turned around and kicked another thug in the nuts but this gave the last thug time to {bad}pull his shotgun and shoot her{/}. She went down immediately, I don't like her chances! Good thing I ran!"
      ""
      ""
      "I risked looking back as I ran and saw {bad}the thug shoot her again{/}. God I hate losing bots like this! At least I made it home in one piece but if I want to go to these classes I need a new escort."
      if bot.bot_combat.level_name=="A":      ## NOTE: S bots cannot have outcome A
        extend " I guess even an {mark}A level combat bot{/} isn't always enough!" 
      elif bot.bot_combat.level_name=="B":
        extend " I thought a {mark}B level combat bot{/} would be good enough."
      elif bot.bot_combat.level_name=="C":
        extend " Maybe I need even better than a {mark}C level combat bot{/}."
      else:  ## must be D
        extend " The teacher was right, a {mark}D level combat bot{/} isn't enough."
      $move_sexbot(bot,None)
    elif nightschool_result=="B":       ##  did not attend, bot damaged
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_b_pictures
      ##  TEXT next lines sets text on the right, 5 pictures 5 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "Walking to class we ran into a group of thugs. They were armed, a spiked bat, a large knife, and a shotgun. It's just like {mark}[ns_teacher_name]{/} said, the classes are in a {bad}bad neighborhood.{/}"
      ""
      ""
      ""
      "They didn't move so we had to stop. The one in the middle told us to leave their territory. The others looked at my escort bot imagining what they would do with her after they chased me away."
      ""
      ""
      "My escort bot surprised us by {mark}punching one of the thugs in the face{/}, he went down hard. She's a combat trained bot with the element of surprise on her side but this was a bad idea. I turned and ran!"
      ""
      ""
      ""
      "She quickly turned to her left and kicked the thug with the shotgun in the nuts but at the same time the last thug {bad}sliced her shoulder with his huge knife{/}. Her arm is limp, good thing I decided to run!"
      ""
      ""
      "I risked looking back once more and I saw {mark}my escort bot turn and run{/}. Her arm looked useless but no one chased her so I'm pretty sure she'll make it home."
      ""
      "I have work to do because {bad}[bot.heshe] was damaged{/} giving us time to escape."
      if bot.bot_combat.level_name=="S":
        extend " I'll repair {mark}[bot]{/} and all I can do is hope for better luck next time."
      elif bot.bot_combat.level_name=="A":
        extend " I'll repair {mark}[bot]{/} for next time. Maybe {mark}S level combat skill{/} would help." 
      elif bot.bot_combat.level_name=="B":
        extend " I'll repair {mark}[bot]{/} for next time. I'm sure {mark}A level combat skill{/} would help."
      elif bot.bot_combat.level_name=="C":
        extend " I'll repair {mark}[bot]{/} for next time. I guess {mark}C level combat skill{/} isn't enough."
      else:  ## must be D
        extend " I'll repair {mark}[bot]{/} for next time. The teacher recommended at least {mark}C level combat skill{/}."
      $bot.chassis.apply_damage("training_combat",(15,45))
    elif nightschool_result=="C":       ##  did not attend, home safe
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_c_pictures
      ##  TEXT next lines sets text on the right, 3 pictures 3 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "While we were walking to class we ran into a group of armed and dangerous thugs. I really want to take these classes but why do the have to be in such a {bad}bad neighborhood{/}."
      ""
      ""
      ""
      "We had to stop when they didn't get out of our way.  One told us to turn around and leave their territory. The others looked at my bot, I'm sure they were thinking of what they would do with her."
      ""
      ""
      "My escort bot decided we should run so she grabbed my hand and we started running away. The thugs started chasing us but we ran so fast we got away easily. Thank God the guy didn't use the shotgun!"
      ""
      "We got home safely."
    else:                                ##  results D, E, F, and G all go to "nightschool_attendclass" so only enter code once
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_defg_pictures
      ##  TEXT next lines sets text on the right, 2 pictures 2 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "I'll never get used to the {bad} dangerous neighborhood{/} where these classes are held. I don't know how anyone lives here. When I go to class I'll always bring a good combat bot!"
      ""
      ""
      ""
      ""
      "I always relax when we get close to the school and see the combat bots guarding the entrance. The first few times they made me nervous but now I welcome the sight of them!."
  if nightschool_result=="A" or nightschool_result=="B" or nightschool_result=="C":  ## results A, B, and C finished
    choice("<<<") "Continue"
  else:                                                                              ## results D, E, F, or G go on
    choice("nightschool_attendclass:{}".format(bot.id)) "Continue"
  return

##==============BORDER WITH ATTEND CLASS FUNCTIONS (2)==============

label nightschool_attendclass(bot):
  $bot=find_character(bot)
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"            ##  this line is for the real release
##  header "Night School - Random Result: [nightschool_result]"    ##  this line is for test releases
## BEGIN INTRODUCTION
  if quests.nightschool=="introduction":
    ##  GRAPHICS next 2 lines set up the pictures on the left side
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    call nightschool_displayattendclasspictures
    $act.set_block("c")
    "{mark}[ns_teacher_name]{/} told us there are {mark}3 courses{/} available: {mark}beginning, intermediate, and advanced.{/} Each course includes {mark}[nightschool_sessionspercourse] sessions{/} and you have to take them in order."
    ""
    "{mark}Beginning{/} is on {mark}Wednesdays and Saturdays{/} and costs {mark}$1,500{/} per session."
    "{mark}Intermediate{/} is on {mark}Tuesdays and Fridays{/} and costs {mark}$3,000{/} per session."
    "{mark}Advanced{/} is on {mark}Mondays and Thursdays{/} and costs {mark}$4,500{/} per session."
    ""
    "These courses sure aren't cheap but since you pay as you go I should try it once. If it's a waste of time I'll never go again."
    ""
    "{mark}[ns_teacher_name]{/} said the classes are self paced so you don't have to attend every time. Once a week or once a month might be affordable. She also said your {mark}escort bot{/} will gain {mark}social skill{/} because you'll use [bot.himher] to practice on."

##BEGIN COURSE 1
  elif quests.nightschool=="course1":
    $nightschool_current_course="Beginning"
    $nightschool_session+=1            ##  increment session counter
    "I attended the {mark}[nightschool_current_course]{/} class, {mark}session [nightschool_session]{/}."
    ""
    ##  GRAPHICS next 2 lines set up the pictures on the left side
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    call nightschool_displayattendclasspictures
    ##  TEXT next lines sets text on the right, 5 pictures 5 lines
    $act.set_block("c")
## EDIT - DRAFTED
    if nightschool_session==1:           ## first class-first session has custom text, 5 pictures 5 lines (WAS 5 EACH)
      "The classroom sure doesn't match the neighborhood, it's really clean and well equipped! The class is about half full, I guess that's a good sign.  {mark}[ns_teacher_name] sure is hot too!{/}"
      ""
      ""
      ""
      "Everyone in the class brought combat bots with them just like I did, some of the bots look pretty good! They're all checking out the teacher just like I am, we sure are a bunch of geeks!"
      ""
      ""
      ""
      "I may be imagining it but I thought {mark}[ns_teacher_name]{/} was looking at me a lot. Probable wishful thinking! I enjoyed the class and was surprised when it was over and she kicked us out."
    else:
      "I wonder how much easier the beginning course is than the other courses. The price increases a lot each time so I hope they get more effective. I guess I need to finish beginner to find out."
      ""
      ""
      ""
      call nightschool_attendancetext    ## randomize last 2 of 3 generic lines for all sessions except 1 (WAS 4 OF 5)
##  BEGIN COURSE 2
  elif quests.nightschool=="course2":
    $nightschool_current_course="Intermediate"
    $nightschool_session+=1            ##  increment session counter
    "I attended the {mark}[nightschool_current_course]{/} class, {mark}session [nightschool_session]{/}."
    ""
    ##  GRAPHICS next 2 lines set up the pictures on the left side
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    call nightschool_displayattendclasspictures
    ##  TEXT next lines sets text on the right, 5 pictures 5 lines
    $act.set_block("c")
## EDIT - DRAFTED
    "The intermediate classes are a quite a bit harder than the beginner classes but I guess they should be for the extra money I'm paying. I need stronger improvement to make this worth my time."
    ""
    ""
    ""
    call nightschool_attendancetext    ## randomize last 2 of 3 lines when attending class (WAS 4 OF 5)
##  BEGIN COURSE 3
  elif quests.nightschool=="course3":
    $nightschool_current_course="Advanced"
    $nightschool_session+=1            ##  increment session counter
    "I attended the {mark}[nightschool_current_course]{/} class, {mark}session [nightschool_session]{/}."
    ""
    ##  GRAPHICS next 2 lines set up the pictures on the left side
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    call nightschool_displayattendclasspictures
    ##  TEXT next lines sets text on the right, 5 pictures 5 lines
    $act.set_block("c")
## EDIT - DRAFTED
    "The advanced classes are really intense! I hope the results are worth the expense. So far the courses have been pretty good so I expect the advanced class will improve my skills even more."
    ""
    ""
    ""
    call nightschool_attendancetext    ## randomize last 3 of 5 lines when attending class
  choice("nightschool_goinghome:{}".format(bot.id)) "Continue"
  return  

label nightschool_attendancetext:           ## randomize 2 lines when attending class (WAS 4 LINES)
  $r=random.randint(1,6)
  if r==1:
    "Tonight the classroom is about half full as always. It sure is a collection of geeks, I guess that's why I fit right though. {mark}At least all these geeks have some interesting bots!{/}"
  elif r==2:
    "As always, the classroom is about half full with the usual collection of geeks and bots. I see the same faces here most of the time. Who cares though, I'm not here to make friends."
  elif r==3:
    "The usual collection of geeks and bots are here! There's seems to be a little bit more social interaction tonight, maybe we are all learning something. The bots are better trainied too!"
  elif r==4:
    "{mark}[ns_teacher_name]{/} is more intense than usual tonight, when she comes over to watch me I need to be on my toes. I like it when she comes over though though, it keeps me motivated!"
  elif r==5:
    "{mark}[ns_teacher_name]{/} seems a little more friendly and less intense tonight. Every time she comes over to me she's got a big smile on her face. Maybe this class is changing me in a good way!"
  else:
    "{mark}[ns_teacher_name]{/} seemed a little bit distracted tonight. She gave us more time to work independently than she usually does. I guess we all have our own problems to deal with sometimes."
  ""
  ""
  $r=random.randint(1,6)
  if r==1:
    "I have to say that {mark}[ns_teacher_name]{/} really knows her stuff! I think she's paying more attention to me than anyone else tonight but I'm pretty sure that's just wishful thinking on my part!"
  elif r==2:
    "Sometimes I realize I'm not listening to what {mark}[ns_teacher_name]{/} is saying, instead I'm daydreaming about what I'd like to do with her. God what I geek I am! I have to stop this daydreaming."
  elif r==3:
    "I was really in the zone tonight, one time {mark}[ns_teacher_name]{/} was watching me and when she started talking she really startled me! I embarrassed myself by having to ask her what she had said."
  elif r==4:
    "Sometimes it's hard to avoid staring at {mark}[ns_teacher_name]{/} because {mark}she's pretty hot!{/} She said I'm making good progress, as long as I can afford to pay for these classes I'll keep coming back."
  elif r==5:
    "I didn't waste any time tonight, there's too much to do. Of course {mark}[ns_teacher_name]{/} is still hot but I stayed focused. I can't spend all class daydreaming about her if I want to get better."
  else:
    "Time really flew by tonight, before I knew it {mark}[ns_teacher_name]{/} was kicking us out so she could go home herself! It's funny, sometimes I daydream about her and sometimes I don't. I wonder why?"
  return

##==============BORDER WITH GOING HOME FUNCTION======================

label nightschool_goinghome(bot):
  $bot=find_character(bot)
  $ns_backgroundnumber=random.randint(1,4)
  $game_bg="street bg_"+str(ns_backgroundnumber)
  header "Night School"            ##  this line is for the real release
##  header "Night School - Random Result: [nightschool_result]"    ##  this line is for test releases
##  BEGIN INTRODUCTION
  if quests.nightschool=="introduction":
    if nightschool_result=="D":         ##  attended class, bot destroyed
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E, and F numbers 50 to 64
      call nightschool_displayresult_d_pictures
      ## TEXT next line sets text on right, 7 pictures - 8 lines
      $act.set_block("c")
##  EDIT - DRAFTED
      "As we were walking home from class we saw a group of well armed thugs. To get home we have to get past them. I need to count on my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we stopped in front of them.  One of them said we can't go through their territory. The other two just stared at my bot hoping they were going to have some fun."
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "All three thugs were on the ground as I ran past them but I didn't think they'd stay down forever so I ran as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "After I ran by, my bot started running behind me. I'm sure she is faster than I am but she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "The thugs were down but not out and they started to get up. As he was getting up, the one with the shotgun decided to use it! Unfortunately {bad}my bot was hit in the back and went down{/}."
      ""
      ""
      "I risked looking back as I ran and saw {bad}the thug shoot her again{/}. God I hate losing bots like this! At least I made it home in one piece but if I want to go to these classes I need a new escort."
      if bot.bot_combat.level_name=="A":      ## NOTE: S bots cannot have outcome A
        extend " I guess even an {mark}A level combat bot{/} isn't always enough!" 
      elif bot.bot_combat.level_name=="B":
        extend " I thought a {mark}B level combat bot{/} would be good enough."
      elif bot.bot_combat.level_name=="C":
        extend " Maybe I need even better than a {mark}C level combat bot{/}."
      else:  ## must be D
        extend " The teacher was right, a {mark}D level combat bot{/} isn't enough."
      $move_sexbot(bot,None)
    elif nightschool_result=="E":       ##  attended class, bot damaged
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E, and F numbers 50 to 64
      call nightschool_displayresult_e_pictures
      ##  TEXT next lines sets text on the right, 6 pictures 7 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "As we were walking home from class we saw a group of well armed thugs. To get home we have to get past them. I need to count on my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we stopped in front of them.  One of them said we can't go through their territory. The other two just stared at my bot hoping they were going to have some fun."
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "All three thugs were on the ground as I ran past them but I didn't think they'd stay down forever so I ran as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "After I ran by, my bot started running behind me. I'm sure she is faster than I am but she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "The thugs were down but not out and they started to get up. As he was getting up, the one with the shotgun decided to use it! {bad}My bot was hit{/} but kept running with me."
      ""
      "I have work to do because {bad}[bot.heshe] was damaged{/} giving us time to escape."
      if bot.bot_combat.level_name=="S":
        extend " I'll repair {mark}[bot]{/} and all I can do is hope for better luck next time."
      elif bot.bot_combat.level_name=="A":
        extend " I'll repair {mark}[bot]{/} for next time. Maybe {mark}S level combat skill{/} would help." 
      elif bot.bot_combat.level_name=="B":
        extend " I'll repair {mark}[bot]{/} for next time. I'm sure {mark}A level combat skill{/} would help."
      elif bot.bot_combat.level_name=="C":
        extend " I'll repair {mark}[bot]{/} for next time. I guess {mark}C level combat skill{/} isn't enough."
      else:  ## must be D
        extend " I'll repair {mark}[bot]{/} for next time. The teacher recommended at least {mark}C level combat skill{/}."
      $bot.chassis.apply_damage("training_combat",(15,45))
    elif nightschool_result=="F":       ##  attended class, home safe (shot missed)
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E,and F numbers 50 to 64
      call nightschool_displayresult_f_pictures
      ##  TEXT next lines sets text on the right, 6 pictures - 7 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "As we were walking home from class we saw a group of well armed thugs. To get home we have to get past them. I need to count on my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we stopped in front of them.  One of them said we can't go through their territory. The other two just stared at my bot hoping they were going to have some fun."
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "All three thugs were on the ground as I ran past them but I didn't think they'd stay down forever so I ran as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "After I ran by, my bot started running behind me. I'm sure she is faster than I am but she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "The thugs were down but not out and they started to get up. As he was getting up, the one with the shotgun decided to use it! {mark}Thank God he missed!{/} We ran even faster in case he tried again!"
      ""
      "We both made it home safely. My bot saved my life back there!"
    elif nightschool_result=="G":        ##  "G": attended class, home safe (no thugs)
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_g_pictures
      ##  TEXT next lines sets text on the right, 1 picture 2 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "I sure hate walking home through this {mark}sketchy neighborhood{/}. I don't know if we just got lucky or if the locals are scared of my escort bot and are leaving us alone. I don't care either way!"
      ""
      "We made it home safely."
## BEGIN COURSE 1
  elif quests.nightschool=="course1":
    if nightschool_result=="D":         ##  attended class, bot destroyed
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E, and F numbers 50 to 64
      call nightschool_displayresult_d_pictures
      ##  TEXT next lines sets text on the right, 7 pictures 8 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "While we were walking home from class we noticed a group of well armed thugs up ahead. We have to get past them to get home. I need my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we had to stop.  One of them asked me what we were doing in their territory. The other two just stared at my bot hoping they were going to have some fun. Not good!"
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "Wow, she really took care of them! I ran past the three thugs who were all down on the ground as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "Once she saw me running, my bot started running behind me. Even though she is faster than I am she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "I didn't think the thugs were going to stay down for long. They started getting up and the one with the shotgun took a shot at us! Unfortunately {bad}my bot was hit in the back and went down{/}."
      ""
      ""
      "I risked looking back as I ran and saw {bad}the thug shoot her again{/}. God I hate losing bots like this! At least I made it home in one piece but if I want to go to these classes I need a new escort."
      if bot.bot_combat.level_name=="A":      ## NOTE: S bots cannot have outcome A
        extend " I guess even an {mark}A level combat bot{/} isn't always enough!" 
      elif bot.bot_combat.level_name=="B":
        extend " I thought a {mark}B level combat bot{/} would be good enough."
      elif bot.bot_combat.level_name=="C":
        extend " Maybe I need even better than a {mark}C level combat bot{/}."
      else:  ## must be D
        extend " The teacher was right, a {mark}D level combat bot{/} isn't enough."
      $move_sexbot(bot,None)
    elif nightschool_result=="E":       ##  attended class, bot damaged
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E, and F numbers 50 to 64
      call nightschool_displayresult_e_pictures
      ##  TEXT next lines sets text on the right, 6 pictures 7 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "While we were walking home from class we noticed a group of well armed thugs up ahead. We have to get past them to get home. I need my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we had to stop.  One of them asked me what we were doing in their territory. The other two just stared at my bot hoping they were going to have some fun. Not good!"
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "Wow, she really took care of them! I ran past the three thugs who were all down on the ground as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "Once she saw me running, my bot started running behind me. Even though she is faster than I am she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "I didn't think the thugs were going to stay down for too long. They started getting up and the one with the shotgun decided to take a shot at us! {bad}My bot was hit{/} but kept running with me."
      ""
      "I have work to do because {bad}[bot.heshe] was damaged{/} giving us time to escape."
      if bot.bot_combat.level_name=="S":
        extend " I'll repair {mark}[bot]{/} and all I can do is hope for better luck next time."
      elif bot.bot_combat.level_name=="A":
        extend " I'll repair {mark}[bot]{/} for next time. Maybe {mark}S level combat skill{/} would help." 
      elif bot.bot_combat.level_name=="B":
        extend " I'll repair {mark}[bot]{/} for next time. I'm sure {mark}A level combat skill{/} would help."
      elif bot.bot_combat.level_name=="C":
        extend " I'll repair {mark}[bot]{/} for next time. I guess {mark}C level combat skill{/} isn't enough."
      else:  ## must be D
        extend " I'll repair {mark}[bot]{/} for next time. The teacher recommended at least {mark}C level combat skill{/}."
      $bot.chassis.apply_damage("training_combat",(15,45))
    elif nightschool_result=="F":       ##  attended class, home safe (shot missed)
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E,and F numbers 50 to 64
      call nightschool_displayresult_f_pictures
      ##  TEXT next lines sets text on the right, 6 pictures 7 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "While we were walking home from class we noticed a group of well armed thugs up ahead. We have to get past them to get home. I need my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we had to stop.  One of them asked me what we were doing in their territory. The other two just stared at my bot hoping they were going to have some fun. Not good!"
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "Wow, she really took care of them! I ran past the three thugs who were all down on the ground as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "Once she saw me running, my bot started running behind me. Even though she is faster than I am she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "I didn't think the thugs were going to stay down for too long. They started getting up and the one with the shotgun decided to take a shot at us! {mark}Thank God he missed!{/} We ran even faster!"
      ""
      "We both made it home safely. My bot saved my life back there!"
    elif nightschool_result=="G":        ##  "G": attended class, home safe (no thugs)
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_g_pictures
      ##  TEXT next lines sets text on the right, 1 picture 2 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "I hate walking home through this {mark}sketchy neighborhood{/}. I don't know if we just got lucky or if the locals are scared of my escort bot and are leaving us alone. I don't care either way!"
      ""
      "We made it home safely."
##  BEGIN COURSE 2
  elif quests.nightschool=="course2":
    if nightschool_result=="D":         ##  attended class, bot destroyed
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E, and F numbers 50 to 64
      call nightschool_displayresult_d_pictures
      ##  TEXT next lines sets text on the right, 7 pictures 8 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "As we were walking home from class we saw a group of well armed thugs. To get home we have to get past them. I need to count on my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we stopped in front of them.  One of them said we can't go through their territory. The other two just stared at my bot hoping they were going to have some fun."
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "All three thugs were on the ground as I ran past them but I didn't think they'd stay down forever so I ran as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "After I ran by, my bot started running behind me. I'm sure she is faster than I am but she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "The thugs were down but not out and they started to get up. As he was getting up, the one with the shotgun decided to use it! Unfortunately {bad}my bot was hit in the back and went down{/}."
      ""
      ""
      "I risked looking back as I ran and saw {bad}the thug shoot her again{/}. God I hate losing bots like this! At least I made it home in one piece but if I want to go to these classes I need a new escort."
      if bot.bot_combat.level_name=="A":      ## NOTE: S bots cannot have outcome A
        extend " I guess even an {mark}A level combat bot{/} isn't always enough!" 
      elif bot.bot_combat.level_name=="B":
        extend " I thought a {mark}B level combat bot{/} would be good enough."
      elif bot.bot_combat.level_name=="C":
        extend " Maybe I need even better than a {mark}C level combat bot{/}."
      else:  ## must be D
        extend " The teacher was right, a {mark}D level combat bot{/} isn't enough."
      $move_sexbot(bot,None)
    elif nightschool_result=="E":       ##  attended class, bot damaged
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E, and F numbers 50 to 64
      call nightschool_displayresult_e_pictures
      ##  TEXT next lines sets text on the right, 6 pictures 7 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "As we were walking home from class we saw a group of well armed thugs. To get home we have to get past them. I need to count on my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we stopped in front of them.  One of them said we can't go through their territory. The other two just stared at my bot hoping they were going to have some fun."
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "All three thugs were on the ground as I ran past them but I didn't think they'd stay down forever so I ran as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "After I ran by, my bot started running behind me. I'm sure she is faster than I am but she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "The thugs were down but not out and they started to get up. As he was getting up, the one with the shotgun decided to use it! {bad}My bot was hit{/} but kept running with me."
      ""
      "I have work to do because {bad}[bot.heshe] was damaged{/} giving us time to escape."
      if bot.bot_combat.level_name=="S":
        extend " I'll repair {mark}[bot]{/} and all I can do is hope for better luck next time."
      elif bot.bot_combat.level_name=="A":
        extend " I'll repair {mark}[bot]{/} for next time. Maybe {mark}S level combat skill{/} would help." 
      elif bot.bot_combat.level_name=="B":
        extend " I'll repair {mark}[bot]{/} for next time. I'm sure {mark}A level combat skill{/} would help."
      elif bot.bot_combat.level_name=="C":
        extend " I'll repair {mark}[bot]{/} for next time. I guess {mark}C level combat skill{/} isn't enough."
      else:  ## must be D
        extend " I'll repair {mark}[bot]{/} for next time. The teacher recommended at least {mark}C level combat skill{/}."
      $bot.chassis.apply_damage("training_combat",(15,45))
    elif nightschool_result=="F":       ##  attended class, home safe (shot missed)
      ## NEW OUTCOME FOR GRAPHICS TBD (in this situation there was no mention of trip home)
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E,and F numbers 50 to 64
      call nightschool_displayresult_f_pictures
      ##  TEXT next lines sets text on the right, 6 pictures 7 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "As we were walking home from class we saw a group of well armed thugs. To get home we have to get past them. I need to count on my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we stopped in front of them.  One of them said we can't go through their territory. The other two just stared at my bot hoping they were going to have some fun."
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "All three thugs were on the ground as I ran past them but I didn't think they'd stay down forever so I ran as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "After I ran by, my bot started running behind me. I'm sure she is faster than I am but she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "The thugs were down but not out and they started to get up. As he was getting up, the one with the shotgun decided to use it! {mark}Thank God he missed!{/} We ran even faster in case he tried again!"
      ""
      "We both made it home safely. My bot saved my life back there!"
    elif nightschool_result=="G":        ##  "G": attended class, home safe (no thugs)
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_g_pictures
      ##  TEXT next lines sets text on the right, 1 picture 2 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "I really hate walking home through this {mark}sketchy neighborhood{/}. I don't know if we just got lucky or if the locals are scared of my escort bot and are leaving us alone. I don't care either way!"
      ""
      "We made it home safely."
## BEGIN COURSE 3
  elif quests.nightschool=="course3":
    if nightschool_result=="D":         ##  attended class, bot destroyed
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E, and F numbers 50 to 64
      call nightschool_displayresult_d_pictures
      ##  TEXT next lines sets text on the right, 7 pictures 8 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "While we were walking home from class we noticed a group of well armed thugs up ahead. We have to get past them to get home. I need my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we had to stop.  One of them asked me what we were doing in their territory. The other two just stared at my bot hoping they were going to have some fun. Not good!"
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "Wow, she really took care of them! I ran past the three thugs who were all down on the ground as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "Once she saw me running, my bot started running behind me. Even though she is faster than I am she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "I didn't think the thugs were going to stay down for long. They started getting up and the one with the shotgun took a shot at us! Unfortunately {bad}my bot was hit in the back and went down{/}."
      ""
      ""
      "I risked looking back as I ran and saw {bad}the thug shoot her again{/}. God I hate losing bots like this! At least I made it home in one piece but if I want to go to these classes I need a new escort."
      if bot.bot_combat.level_name=="A":      ## NOTE: S bots cannot have outcome A
        extend " I guess even an {mark}A level combat bot{/} isn't always enough!" 
      elif bot.bot_combat.level_name=="B":
        extend " I thought a {mark}B level combat bot{/} would be good enough."
      elif bot.bot_combat.level_name=="C":
        extend " Maybe I need even better than a {mark}C level combat bot{/}."
      else:  ## must be D
        extend " The teacher was right, a {mark}D level combat bot{/} isn't enough."
      $move_sexbot(bot,None)
    elif nightschool_result=="E":       ##  attended class, bot damaged
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E, and F numbers 50 to 64
      call nightschool_displayresult_e_pictures
      ##  TEXT next lines sets text on the right, 6 pictures 7 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "While walking home from class we noticed a group of well armed thugs up ahead. We have to get past them somehow to get home. I need my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we had to stop.  One of them asked me what we were doing in their territory. The other two just stared at my bot hoping they were going to have some fun. Not good!"
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "Wow, she really took care of them! I ran past the three thugs who were all down on the ground as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "Once she saw me running, my bot started running behind me. Even though she is faster than I am she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "I didn't think the thugs were going to stay down for too long. They started getting up and the one with the shotgun decided to take a shot at us! {bad}My bot was hit{/} but kept running with me."
      ""
      "I have work to do because {bad}[bot.heshe] was damaged{/} giving us time to escape."
      if bot.bot_combat.level_name=="S":
        extend " I'll repair {mark}[bot]{/} and all I can do is hope for better luck next time."
      elif bot.bot_combat.level_name=="A":
        extend " I'll repair {mark}[bot]{/} for next time. Maybe {mark}S level combat skill{/} would help." 
      elif bot.bot_combat.level_name=="B":
        extend " I'll repair {mark}[bot]{/} for next time. I'm sure {mark}A level combat skill{/} would help."
      elif bot.bot_combat.level_name=="C":
        extend " I'll repair {mark}[bot]{/} for next time. I guess {mark}C level combat skill{/} isn't enough."
      else:  ## must be D
        extend " I'll repair {mark}[bot]{/} for next time. The teacher recommended at least {mark}C level combat skill{/}."
      $bot.chassis.apply_damage("training_combat",(15,45))
    elif nightschool_result=="F":       ##  attended class, home safe (shot missed)
      ## NEW OUTCOME FOR GRAPHICS TBD (in this situation there was no mention of trip home)
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displaygoinghomepictures      ##  displays pictures used in D, E,and F numbers 50 to 64
      call nightschool_displayresult_f_pictures
      ##  TEXT next lines sets text on the right, 6 pictures 7 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "While we were walking home from class we noticed a group of well armed thugs up ahead. We have to get past them to get home. I need my escort bot to get me through, not much I can do myself."
      ""
      ""
      ""
      "The thugs didn't move so we had to stop.  One of them asked me what we were doing in their territory. The other two just stared at my bot hoping they were going to have some fun. Not good!"
      ""
      ""
      "My bot said 'Run!' and sprang into action! {mark}She kicked the guy in the middle into the guy on the right while her elbow hit the guy on the left in the head.{/} I was suprised but started running."
      ""
      ""
      ""
      "Wow, she really took care of them! I ran past the three thugs who were all down on the ground as fast as I could. My bot looked back at me to make sure I was running."
      ""
      ""
      "Once she saw me running, my bot started running behind me. Even though she is faster than I am she stayed behind me so that anything the thugs did would hit her instead of me. Good thinking!"
      ""
      ""
      ""
      "I didn't think the thugs were going to stay down for too long. They started getting up and the one with the shotgun decided to take a shot at us! {mark}Thank God he missed!{/} We ran even faster!"
      ""
      "We both made it home safely. My bot saved my life back there!"
    elif nightschool_result=="G":        ##  "G": attended class, home safe (no thugs)
      ## NEW OUTCOME FOR GRAPHICS TBD (in this situation there was no mention of trip home)
      ##  GRAPHICS next 2 lines set up the pictures on the left side
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      call nightschool_displayresult_g_pictures
      ##  TEXT next lines sets text on the right, 1 picture 2 lines
      $act.set_block("c")
## EDIT - DRAFTED
      "I hate walking home through this {mark}sketchy neighborhood{/}. I don't know if we just got lucky or if the locals are scared of my escort bot and are leaving us alone. I don't care either way!"
      ""
      "We made it home safely."
##  MUST PUT ALL QUEST ADVANCE AND FINISH FUNCTIONS HERE TO AVOID LOGIC ERRORS BY CHANGING QUEST STATUS WHILE EXECUTING THE QUEST

  if quests.nightschool=="introduction":    ##  attended, go to class 1
    ""
    call mc_update_relation(ns_teacher_name,1,0)
    $quests.nightschool.advance()
  elif quests.nightschool=="course1":       ##  if last session go to class 2
    ""
    $mc.money-=1500
    $mc.give_xp("social",randint(900,1200))
    if nightschool_result!="D":             ##  result D is dead bot, can't gain experience!
      $bot.give_xp("bot_social",randint(25,100))
    if nightschool_session>=nightschool_sessionspercourse:    ##  counter=#sessions course ends
      ""
      "I completed the Beginner course. I wonder what the intermediate class will be like?"
      ""
      call mc_update_relation(ns_teacher_name,1,0)
      $quests.nightschool.advance()         ##  next course
      $nightschool_session=0                ##  reset session counter
  elif quests.nightschool=="course2":       ##  if last session go to class 3
    ""
    $mc.money-=3000
    $mc.give_xp("social",randint(1700,2000))
    if nightschool_result!="D":             ##  result D is dead bot, can't gain experience!
      $bot.give_xp("bot_social",randint(100,175))
    if nightschool_session>=nightschool_sessionspercourse:    ##  counter=#sessions course ends
      "I completed the Intermediate course, I guess the Advanced course will be even harder."
      ""
      call mc_update_relation(ns_teacher_name,2,0)
      $quests.nightschool.advance()         ##  next course
      $nightschool_session=0                ##  reset session counter
  elif quests.nightschool=="course3":
    ""
    $mc.money-=4500
    $mc.give_xp("social",randint(2600,2800))
    if nightschool_result!="D":             ##  result D is dead bot, can't gain experience!
      $bot.give_xp("bot_social",randint(175,250))
    if nightschool_session>=nightschool_sessionspercourse:    ##  counter=#sessions course ends
      "I completed the Advanced course so I'm finished with this school. I'm going to miss {mark}[ns_teacher_name]{/}!"
      ""
      call mc_update_relation(ns_teacher_name,3,0)
      $quests.nightschool.finish()          ##  DONE!!!
      $nightschool_session=0                ##  reset session counter (habit!!)
  $bot=None                                 ##  always clear bot from memory when finished
  choice("<<<") "Continue"
  return

##======================BORDER WITH DISPLAY PICTURE FUNCTIONS========================

#+++++++++GOING TO CLASS SECTION++++++++++++++

label nightschool_displayresult_a_pictures:
  $nightschool_chance=random.randint(1, 3)       ##  walking up to thugs
  if nightschool_chance==1:
    $action_image= "quests night_school ns_26"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_27"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_28"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  standing in front of thugs
  if nightschool_chance==1:
    $action_image= "quests night_school ns_29"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_30"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_31"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  hitting thug 2
  if nightschool_chance==1:
    $action_image= "quests night_school ns_32"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_33"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_34"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  kicking thug 1
  if nightschool_chance==1:
    $action_image= "quests night_school ns_35"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_36"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_37"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  shot on ground
  if nightschool_chance==1:
    $action_image= "quests night_school ns_38"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_39"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_40"
    center "{image=[action_image]@400x600}"
  ""
  return

label nightschool_displayresult_b_pictures:
  $nightschool_chance=random.randint(1, 3)       ##  walking up to thugs
  if nightschool_chance==1:
    $action_image= "quests night_school ns_26"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_27"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_28"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  standing in front of thugs
  if nightschool_chance==1:
    $action_image= "quests night_school ns_29"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_30"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_31"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  hitting thug 2
  if nightschool_chance==1:
    $action_image= "quests night_school ns_32"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_33"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_34"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  kicking thug 3
  if nightschool_chance==1:
    $action_image= "quests night_school ns_41"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_42"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_43"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  running away
  if nightschool_chance==1:
    $action_image= "quests night_school ns_44"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_45"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_46"
    center "{image=[action_image]@400x600}"
  ""
  return

label nightschool_displayresult_c_pictures:
  $nightschool_chance=random.randint(1, 3)       ##  walking up to thugs
  if nightschool_chance==1:
    $action_image= "quests night_school ns_26"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_27"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_28"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  standing in front of thugs
  if nightschool_chance==1:
    $action_image= "quests night_school ns_29"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_30"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_31"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  running away
  if nightschool_chance==1:
    $action_image= "quests night_school ns_47"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_48"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_49"
    center "{image=[action_image]@400x600}"
  ""
  return

label nightschool_displayresult_defg_pictures:   ##  DEFG all go to attend class so walking to school is the same
  $nightschool_chance=random.randint(1, 3)       ##  walking to class
  if nightschool_chance==1:
    $action_image= "quests night_school ns_6"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_7"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_8"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  entering class
  if nightschool_chance==1:
    $action_image= "quests night_school ns_9"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_10"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_11"
    center "{image=[action_image]@400x600}"
  ""
  return

##++++++++ATTEND CLASS FUNCTIONS+++++++++++++++

label nightschool_displayattendclasspictures:
  $ns_randomlist=[]
  while len(ns_randomlist)<3:                ## get 3 unique picture numbers to display (WAS 5)
    $r=random.randint(12,25)
    if r not in ns_randomlist:
      $ns_randomlist.append(r)
  $ns_picturenumber=ns_randomlist[0]
  call nightschool_displayclassroompicture
  ""
  $ns_picturenumber=ns_randomlist[1]
  call nightschool_displayclassroompicture
  ""
  $ns_picturenumber=ns_randomlist[2]
  call nightschool_displayclassroompicture
  $ns_randomlist.clear()                     ##clear the list for next time
  return

label nightschool_displayclassroompicture:
  if ns_picturenumber==12:
    $action_image="quests night_school ns_12"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==13:
    $action_image="quests night_school ns_13"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==14:
    $action_image="quests night_school ns_14"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==15:
    $action_image="quests night_school ns_15"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==16:
    $action_image="quests night_school ns_16"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==17:
    $action_image="quests night_school ns_17"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==18:
    $action_image="quests night_school ns_18"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==19:
    $action_image="quests night_school ns_19"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==20:
    $action_image="quests night_school ns_20"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==21:
    $action_image="quests night_school ns_21"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==22:
    $action_image="quests night_school ns_22"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==23:
    $action_image="quests night_school ns_23"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==24:
    $action_image="quests night_school ns_24"
    center "{image=[action_image]@400x600}"
  elif ns_picturenumber==25:
    $action_image="quests night_school ns_25"
    center "{image=[action_image]@400x600}"
  return

##++++++++GOING HOME FUNCTIONS++++++++++++++++

label nightschool_displaygoinghomepictures:
  $nightschool_chance=random.randint(1, 3)       ##  walking up to thugs
  if nightschool_chance==1:
    $action_image= "quests night_school ns_50"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_51"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_52"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  standing in front of thugs
  if nightschool_chance==1:
    $action_image= "quests night_school ns_53"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_54"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_55"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  knocking down all 3 thugs
  if nightschool_chance==1:
    $action_image= "quests night_school ns_56"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_57"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_58"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  starting to run away
  if nightschool_chance==1:
    $action_image= "quests night_school ns_59"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_60"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_61"
    center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 3)       ##  running away
  if nightschool_chance==1:
    $action_image= "quests night_school ns_62"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_63"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_64"
    center "{image=[action_image]@400x600}"
  ""
  return

label nightschool_displayresult_d_pictures:
  $action_image= "quests night_school ns_65"     ##  shot in back (only 1 pic)
  center "{image=[action_image]@400x600}"
  ""
  $nightschool_chance=random.randint(1, 2)       ##  shot again on ground (2 pics
  if nightschool_chance==1:
    $action_image= "quests night_school ns_66"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_67"
    center "{image=[action_image]@400x600}"
  ""
  return

label nightschool_displayresult_e_pictures:
  $action_image= "quests night_school ns_68"     ##  shot in shoulder (only 1 pic)
  center "{image=[action_image]@400x600}"
  ""
  return

label nightschool_displayresult_f_pictures:
  $nightschool_chance=random.randint(1, 2)       ##  shooter missed (2 pics)
  if nightschool_chance==1:
    $action_image= "quests night_school ns_69"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_70"
    center "{image=[action_image]@400x600}"
  ""
  return

label nightschool_displayresult_g_pictures:
  $nightschool_chance=random.randint(1, 3)       ##  walking home safely
  if nightschool_chance==1:
    $action_image= "quests night_school ns_71"
    center "{image=[action_image]@400x600}"
  elif nightschool_chance==2:
    $action_image= "quests night_school ns_72"
    center "{image=[action_image]@400x600}"
  else:
    $action_image= "quests night_school ns_73"
    center "{image=[action_image]@400x600}"
  ""
  return
