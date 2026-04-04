init python:
  fr_interest_rate=[0,0.01,0.01,0.0125,0.015]        ## 0.10.n - replaced old variable sr_interest_rate
  sr_game_difficulty=""      ##  string holding difficulty level chosen by user
  fr_initial_debt=[0,250000,500000,800000,1000000]  ## 0.10.n - replaced old variable sr_initial_debt
  mc_cumulative_rep_xp=0     ##  xp given up to now, xp resets at transitions for reputations
  
init python hide:
  @event_handler("init_game")
  def intro():
    queue_event("intro")

label intro:
  $set_interaction("intro")
  scene black
  with intro_transition
  $game_bg="street bg_1"
  $game_bgm="intro"
  header "Intro"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_1" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_2" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "You were walking home after a fun night at the {mark}Robosechs club{/} through a shady part of town trying not to fall down."
  ""
  ""
  ""
  ""
  "You hear an explosion on your left and turn to look. A guy is running out of a {mark}burning building with a briefcase{/}. What the hell?"
  ""
  choice("intro_1b") "Continue"
  return

label intro_1b:
  $set_interaction("intro")
  $game_bgm="intro"
  $game_bg="street bg_2"
  header "Intro"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_3" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_4" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "While you're trying to figure out what's going on the guy runs up to you and {mark}hits you in the head with the briefcase!{/}"
  ""
  ""
  ""
  ""
  "You can't figure out what's going on but the {mark}briefcase hurts!{/} The force of the blow makes you stumble."
  ""
  choice("intro_1c") "Continue"
  return

label intro_1c:
  $set_interaction("intro")
  $game_bgm="intro"
  $game_bg="street bg_3"
  header "Intro"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_5" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_6" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "You fall down face first on the sidewalk which is really hard! The guy throws the {mark}briefcase{/} down on the ground right in front of your face and it pops open."
  ""
  ""
  ""
  "You could swear the {mark}briefcase is full of money{/} but before you get a good look the guy hits you in the back of the head and everything goes dark."
  ""
  choice("intro_2") "Continue"
  return


label intro_2:
  $set_interaction("intro")
  $game_bg="street bg_4"
  header "Intro"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_7" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_8" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "You wake up in an office with 3 men; a scruffy looking thug, the guy who ran out of the building, and an asian guy sitting at a desk."
  ""
  "You recognize the asian guy, he runs {mark}The Syndicate{/}! He looks mad as hell and asks:"
  ""
  "{say}Who the hell are you? Why did you burn my building down? Do you know how much money was in there you asshole!{/}"
  ""
  "You don't know what he's talking about but at least you know your name . . ."
  ""
  choice("intro_enter_name") "Continue"
  return

default rename_mc_to=None

init python:
  def validate_mc_name(name):
    if name.strip():
      return ""
    else:
      return "{bad}Can't be nameless{/}"

define allowed_mc_name_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -'`"

label intro_enter_name:
  $set_interaction("intro")
  $game_bg="street bg_1"
  header "Intro"
  $act.start_block("l:440 c:content_width-440")
  center "{image=mc avatar@400x600}"
  $act.set_block("c")
  ""
  "Enter your name."
  ""
  $rename_mc_to=mc.name
  $act.add_screen("ui_input","rename_mc_to","intro_rename_mc",'validate_mc_name("{}")',xalign=0.5,width=300,allowed_chars=allowed_mc_name_chars)
  choice("intro_rename_mc",key=("K_KP_ENTER","K_RETURN"),sensitive_if="$not validate_mc_name(rename_mc_to)") "Confirm name"
  return

label intro_rename_mc:
  $set_interaction("intro")
  $game_bg="street bg_2"
  header "Intro"
  $mc.name=rename_mc_to
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_9" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_10" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "You tell him your name is [mc] and that you didn't burn anything but he cuts you off:"
  ""
  "{say}Bullshit! I ought to kill you but instead you're going to {bad}pay me back every dime with interest!{/} We looked through your wallet and know you run a shop called{/} {mark}Sexbot Restoration{/}{say}. Wallet was empty, business must not be so great, eh?"
  ""
  "You don't understand what's going on, you didn't burn anything! You look at the guy that ran out of the building and it comes to you!"
  ""
  choice("intro_3") "Continue"
  return

label intro_3:
  $set_interaction("intro")
  $game_bg="street bg_3"
  header "Intro"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_11" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_12" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "{mark}That asshole is framing me!{/} He must have stolen the money in the briefcase and then burned the building to cover it up!"
  ""
  "The boss is still talking to you:"
  ""
  "{say}I'm going to send a collection agent every{/} {mark}Monday morning{/} {say}to collect payment. The minimum payment will be the interest but you better pay more than that if you know what's good for you!{/}"
  ""
  "{say}Listen up kid! If you don't make the minimum payment we will give you a pass{/} {bad}ONCE{/}{say}. The second time you miss a payment will be{/} {bad}the last time if you catch my meaning!{/}"
  choice("intro_4") "Continue"
  return

label intro_4:
  $set_interaction("intro")
  $game_bg="street bg_4"
  header "Intro"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_13" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_14" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "The guy who framed you smiles at you and says:"
  ""
  "{say}I'm happy to be the collection agent boss!{/}"
  ""
  ""
  "You protest saying that guy stole the money and is framing you! The guy starts to say something but both the boss and the thug glare at him so he keeps his mouth shut."
  ""
  "{mark}Maybe this is my chance, they don't seem to trust the guy.{/}"
  ""
  choice("intro_5") "Continue"
  return

label intro_5:
  $set_interaction("intro")
  $game_bg="street bg_1"
  header "Intro"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_15" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_16" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "The thug looks at the boss and then looks at the other guy and says menacingly:"
  ""
  "{say}Boss, I'll be happy to accompany him when he does the collections.{/}"
  ""
  "The young guy looks pissed off but he decides not to say anything."
  ""
  "The boss says:"
  ""
  "{say}Then it's settled, you two will be the collection agents. Now throw this bum out before I change my mind and just kill him!{/}"
  ""
  choice("intro_6") "Continue"
  return

label intro_6:
  $set_interaction("intro")
  $game_bg="street bg_2"
  header "Intro"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_17" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_18" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "The two guys lead me out of the building. The young guy is really pissed, thank god the thug holds the guy back or I'd be in trouble!"
  ""
  ""
  "{mark}Holy shit, I'm in trouble!{/} Business at my shop is barely enough to live on, how am I going to pay {mark}The Syndicate{/} what they are demanding? You head home thinking about what you can do to make your business more successful when you realize {bad}they didn't even tell you how much money you owe them or what the interest rate is.{/}"
  ""
  choice("intro_choose_difficulty") "Continue"
  return

label intro_choose_difficulty:
  $set_interaction("intro")
  $intro_info_pages=["difficulty_easy","difficulty_normal","difficulty_hard","difficulty_hardcore"]
  $game_bg="street bg_3"
  header "Intro"
  $act.start_block("l:440 c:content_width-440")
  center "{image=mc avatar@400x600}"
  $act.set_block("c")
  ""
  "Select difficulty level."
  ""
  "Descriptions of the levels are shown on the right, use the arrow buttons at the bottom to view each level."
  ""
  choice("intro_set_difficulty_easy",hint="easy") "Can do it!"
  choice("intro_set_difficulty_normal",hint="normal") "Manageable"
  choice("intro_set_difficulty_hard",hint="hard") "I'm in shit..."
  choice("intro_set_difficulty_hardcore",hint="hardcore") "Bring it!"
  return

label intro_set_difficulty_easy:
  $game.difficulty=1
  $sr_game_difficulty="- Easy"
  $mc.char_points=game_tunings["easy_difficulty_char_points"]
  $mc.debt=fr_initial_debt[game.difficulty]
  $mc.debt_pending=int(mc.debt*fr_interest_rate[game.difficulty])
  return "intro_setup_character"

label intro_set_difficulty_normal:
  $game.difficulty=2
  $sr_game_difficulty="- Normal"
  $mc.char_points=game_tunings["normal_difficulty_char_points"]
  $mc.debt=fr_initial_debt[game.difficulty]
  $mc.debt_pending=int(mc.debt*fr_interest_rate[game.difficulty])
  return "intro_setup_character"
    
label intro_set_difficulty_hard:
  $game.difficulty=3
  $sr_game_difficulty="- Hard"
  $mc.char_points=game_tunings["hard_difficulty_char_points"]
  $mc.debt=fr_initial_debt[game.difficulty]
  $mc.debt_pending=int(mc.debt*fr_interest_rate[game.difficulty])
  return "intro_setup_character"

label intro_set_difficulty_hardcore:
  $game.difficulty=4
  $sr_game_difficulty="- Hardcore"
  $mc.char_points=game_tunings["hardcore_difficulty_char_points"]
  $mc.debt=fr_initial_debt[game.difficulty]
  $mc.debt_pending=int(mc.debt*fr_interest_rate[game.difficulty])
  return "intro_setup_character"

screen setup_character():
  vbox:
    xalign 0.5
    text "Character points: {mark}[mc.char_points]{/}" xalign 0.5
    use vdiv
    python:
      skills=[]
      for stat in mc.stats_order:
        stat=mc.stats[stat]
        if not stat.hidden and stat.stat_type=="mc_skill":
          skills.append(stat)
      skills.sort(key=lambda skill:skill.name.lower())
      interleaved_skills=[]
      half=(len(skills)+1)//2
      for n in range(0,half):
        interleaved_skills.append(skills[n])
        if (half+n)<len(skills):
          interleaved_skills.append(skills[half+n])
      skills=interleaved_skills
    if skills:
      text "Skills" xalign 0.5
      $rows=(len(skills)+1)//2
      grid 2 rows:
        xalign 0.5
        xspacing 150
        allow_underfull True
        for skill in skills:
          vbox:
            xsize (content_width-300)//2
            use info_row(skill.name,"{mark}"+skill.level_name+"{/}")
      use vdiv

label intro_setup_character:
  $set_interaction("intro")
  $intro_info_pages=["skill_combat","skill_computers","skill_electronics","skill_mechanics","skill_sex","skill_social"]
  $game_bg="street bg_4"
  header "Intro"
  ""
  "Customize [mc]'s skill set by applying character points to the six different skills below."
  ""
  "Take your time and choose carefully!"
  ""
  $act.add_screen("setup_character")
  python:
    skills=[]
    for stat in mc.stats_order:
      stat=mc.stats[stat]
      if not stat.hidden and stat.stat_type=="mc_skill":
        skills.append(stat)
    skills.sort(key=lambda skill:skill.name.lower())
  $skill_n=0
  while skill_n<len(skills):
    python:
      skill=skills[skill_n]
      skill_n+=1
      inc_skill_cost=skill.level*skill.level
    if skill<"S":
      choice(">>>intro_setup_inc_skill:"+skill.id,cost=[("char_points",inc_skill_cost)]) "[skill]+"
    else:
      choice(None,hint="{hint}can't go over{/}") "[skill]+"
  $skill_n=0
  while skill_n<len(skills):
    python:
      skill=skills[skill_n]
      skill_n+=1
      dec_skill_cost=(skill.level-1)*(skill.level-1)
    if skill>"F":
      choice(">>>intro_setup_dec_skill:"+skill.id,cost=[("char_points",-dec_skill_cost)]) "[skill]-"
    else:
      choice(None,hint="{hint}can't go lower{/}") "[skill]-"
  choice("intro_setup_character_done",pos=17) "Done"
  return

label intro_setup_inc_skill(skill):
  $notify.disable()
  $setattr(mc,skill,getattr(mc,skill).level+1)
  $notify.enable()
  return "<<<"

label intro_setup_dec_skill(skill):
  $notify.disable()
  $setattr(mc,skill,getattr(mc,skill).level-1)
  $notify.enable()
  return "<<<"

label intro_setup_character_done:
  $set_interaction("intro")
  $intro_info_pages=None
  $game_bg="street bg_1"
  header "Intro"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "squirrel botshop sri_19" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "squirrel botshop sri_20" 
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "You finally make it home to your shop. I don't think the {mark}Syndicate Boss{/} trusts the young guy and it looked like the thug doesn't either. {mark}I better hope the thug is loyal to the boss or I'm dead!{/}"
  ""
  ""
  ""
  "Time to head to bed, tomorrow I've got to start making some serious money!"
  ""
  $notify.disable()

  ##$mc.money=3000+randint(0,4000*(5-game.difficulty))   ##  ORIGINAL CODE, CONVOLUTED!!

  $mc.money=randint(28350,33750)

  $mc_initial_debt=mc.debt     ## 0.9.n to calculate reputation increases based upon paying off debt

  $home.update_expenses()
  $quests.start_quest("where_to_get_bots")
  $quests.start_quest("where_to_get_bot_parts")
  $quests.start_quest("where_to_sell_bots")
  $quests.start_quest("show_difficulty_setting")
  $notify.enable()
  $quests.start_quest("exiled_engineer")
  $quests.exiled_engineer["paid_today"]=True
  choice("<<<") "Continue"
  
##  $print "mc.rep_syndicate.xp:",mc.rep_syndicate.xp
  return
