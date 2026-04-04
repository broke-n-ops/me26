##====business partners bot verification

## All  bots except Sucky must be S level in Combat, Sex, and Social
## Sucky Bot must be S level in Sex
## part rating set at start based upon the assignment
## integrity and stability must be 100% for all bots

##===bot check===

label bp_bot_check_1():
  $game_bg="home bg"                                                      ##  home background
  header "Business Partnership Assignment Bot Check"                      ##  home background
  python:
    bot_found=0                                                           ## flag for finding at least one bot
    temp_string=""                                                        ## for displaying results
    for bots_storage in (home.sexbots,workshop.sexbots):                  ## loop through all bots
      for bot in bots_storage:
        if bot and bot.model_name=="AGTY-36":
          bot_found=1
          temp_string=temp_string+"Bot Name:  {mark}"+str(bot.name)+"{/}\n{size=-8}- Bot Model:  {mark}AGTY-36{/}\n- Bot Rate:  {mark}B{/}\n" 
          part_test=1                                                     ## assume part test pass, failed test will negate
          for slot in bot.outfit_slots: 
            part=bot.item_on_slot(slot)
            if part.rate in "FEDCB":                                      ## if not in FEDCB must be A or S - ONLY BOT THAT ALLOWS 'A' LEVEL PARTS
              part_test=0                                                 ## part fail flag
              temp_string=temp_string+"- Parts:  {bad}Fail{/}\n"
              break                                                       ## remaining parts don't matter
          if part_test==1:
            temp_string=temp_string+"- Parts:  {good}Pass{/}\n"
          if bot.chassis.integrity<100:
            temp_string=temp_string+"- Integrity:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Integrity:  {good}Pass{/}\n"
          if bot.psychocore.stability<100:  
            temp_string=temp_string+"- Stability:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Stability:  {good}Pass{/}\n"
          if bot.bot_combat.level_name=="S":
            temp_string=temp_string+"- Combat Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Combat Skill:  {bad}Fail{/}\n" 
          if bot.bot_sex.level_name=="S":
            temp_string=temp_string+"- Sex Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Sex Skill:  {bad}Fail{/}\n"  
          if bot.bot_social.level_name=="S":
            temp_string=temp_string+"- Social Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Social Skill:  {bad}Fail{/}\n"    
          if bot["mission"]:
            temp_string=temp_string+"- {bad}Bot currently on mission{/}"
          temp_string=temp_string+"\n{/}"
  if bot_found==0:
    "You do not have any {mark}AGTY-36{/} bots."
  else:
    $act.start_block("l:440 c:content_width-440")
    center "{image=bots squirrel_mylou avatar@400x600}"
    $act.set_block("c")
    "[temp_string]"
  choice("<<<") "Done"
  return
 
label bp_bot_check_2():
  $game_bg="home bg"                                                      ##  home background
  header "Business Partnership Assignment Bot Check"                      ##  home background
  python:
    bot_found=0                                                           ## flag for finding at least one bot
    temp_string=""                                                        ## for displaying results
    for bots_storage in (home.sexbots,workshop.sexbots):                  ## loop through all bots
      for bot in bots_storage:
        if bot and bot.model_name=="Tanjiro SX":
          bot_found=1
          temp_string=temp_string+"Bot Name:  {mark}"+str(bot.name)+"{/}\n{size=-8}- Bot Model:  {mark}Tanjiro SX{/}\n- Bot Rate:  {mark}A{/}\n" 
          part_test=1                                                     ## assume part test pass, failed test will negate
          for slot in bot.outfit_slots: 
            part=bot.item_on_slot(slot)
            if part.rate in "FEDCBA":                                     ## if not in FEDCBA must be S
              part_test=0                                                 ## part fail flag
              temp_string=temp_string+"- Parts:  {bad}Fail{/}\n"
              break                                                       ## remaining parts don't matter
          if part_test==1:
            temp_string=temp_string+"- Parts:  {good}Pass{/}\n"
          if bot.chassis.integrity<100:
            temp_string=temp_string+"- Integrity:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Integrity:  {good}Pass{/}\n"
          if bot.psychocore.stability<100:  
            temp_string=temp_string+"- Stability:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Stability:  {good}Pass{/}\n"
          if bot.bot_combat.level_name=="S":
            temp_string=temp_string+"- Combat Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Combat Skill:  {bad}Fail{/}\n"          
          if bot.bot_sex.level_name=="S":
            temp_string=temp_string+"- Sex Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Sex Skill:  {bad}Fail{/}\n"  
          if bot.bot_social.level_name=="S":
            temp_string=temp_string+"- Social Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Social Skill:  {bad}Fail{/}\n"    
          if bot["mission"]:
            temp_string=temp_string+"- {bad}Bot currently on mission{/}"
          temp_string=temp_string+"\n{/}"
  if bot_found==0:
    "You do not have any {mark}Tanjiro SX{/} bots."
  else:
    $act.start_block("l:440 c:content_width-440")
    center "{image=bots squirrel_tanjiro avatar@400x600}"
    $act.set_block("c")
    "[temp_string]"
  choice("<<<") "Done"
  return

## Sucky Bot Variables for reference, declared in 'business_partners.rpy'
## sucky_charger_integrity=0  ## sucky charger integrity - 0 to 100%
## sucky_head_integrity=0     ## sucky head integrity - 0 to 100%
## sucky_body_integrity=0     ## sucky body integrity - 0 to 100%
## sucky_stability=0          ## sucky stability - 0 to 100%
## sucky_sex_skill=0          ## sucky sex skill - <=999=F, 1000-2249=E,2250-4999=C, 5000-9999=C, 10000-22499=B, 22500-49999=A, 50000-100000=S

label bp_bot_check_3():
  $game_bg="home bg"                                                      ##  home background
  header "Business Partnership Assignment Bot Check"                      ##  home background
  $global sucky_charger_integrity
  $global sucky_head_integrity
  $global sucky_body_integrity
  $global sucky_stability
  $global sucky_sex_skill
  
  # $sucky_charger_integrity=8
  # $sucky_head_integrity=80
  # $sucky_body_integrity=100
  # $sucky_stability=80
  # $sucky_sex_skill=10000
  
  $act.start_block("l:390 c:360 r:content_width-750")
  $act.set_block("l")
  center "{image=bots sucky_robot avatar@400x600}"
  $act.set_block("c")
  "Model: {mark}Sucky Bot{/}"
  ""
  "- Charger Integrity:"
  "- Head Integrity:"
  "- Body Integrity:"
  "- Psychocore Stability:"
  "- Sex Skill:"
  $act.set_block("r")
  ""
  ""
  if sucky_charger_integrity!=100:
    "{bad}Fail{/}{space=45}{mark}[sucky_charger_integrity]%%{/}"
  else:
    "{good}Pass{/}{space=31}{mark}[sucky_charger_integrity]%%{/}"
  if sucky_head_integrity!=100:
    "{bad}Fail{/}{space=45}{mark}[sucky_head_integrity]%%{/}"
  else:
    "{good}Pass{/}{space=31}{mark}[sucky_head_integrity]%%{/}"
  if sucky_body_integrity!=100:
    "{bad}Fail{/}{space=45}{mark}[sucky_body_integrity]%%{/}"
  else:
    "{good}Pass{/}{space=31}{mark}[sucky_body_integrity]%%{/}"
  if sucky_stability!=100:
    "{bad}Fail{/}{space=45}{mark}[sucky_stability]%%{/}"
  else:
    "{good}Pass{/}{space=31}{mark}[sucky_stability]%%{/}"
  if sucky_sex_skill==0:
    "{bad}Fail{/}{space=45}{info}none{/}"
  elif sucky_sex_skill<1000:
    $pct=int(sucky_sex_skill/10.0)
    "{bad}Fail{/}{space=45}{info}{size=-8}([pct]%%){/}{/} {mark}F{/}"
  elif sucky_sex_skill<2250:
    $pct=int((sucky_sex_skill-1000.0)/12.5)
    "{bad}Fail{/}{space=45}{info}{size=-8}([pct]%%){/}{/} {mark}E{/}"
  elif sucky_sex_skill<5000:
    $pct=int((sucky_sex_skill-2250.0)/27.5)
    "{bad}Fail{/}{space=45}{info}{size=-8}([pct]%%){/}{/} {mark}D{/}"
  elif sucky_sex_skill<10000:
    $pct=int((sucky_sex_skill-5000.0)/50.0)
    "{bad}Fail{/}{space=45}{info}{size=-8}([pct]%%){/}{/} {mark}C{/}"
  elif sucky_sex_skill<22500:
    $pct=int((sucky_sex_skill-10000.0)/125.0)
    "{bad}Fail{/}{space=45}{info}{size=-8}([pct]%%){/}{/} {mark}B{/}"
  elif sucky_sex_skill<50000:
    $pct=int((sucky_sex_skill-22500.0)/275.0)
    "{bad}Fail{/}{space=45}{info}{size=-8}([pct]%%){/}{/} {mark}A{/}"
  else:
    $pct=int((sucky_sex_skill-50000.0)/500.0)
    "{good}Pass{/}{space=31}{info}{size=-8}([pct]%%){/}{/} {mark}S{/}"
  choice("<<<") "Done"
  return

label bp_bot_check_4():                                                   ## FEMALE BOT IN PAIR
  $game_bg="home bg"                                                      ## home background
  header "Business Partnership Assignment Bot Check"                      ## home background
  python:
    bot_found=0                                                           ## flag for finding at least one bot
    temp_string=""                                                        ## for displaying results
    for bots_storage in (home.sexbots,workshop.sexbots):                  ## loop through all bots
      for bot in bots_storage:
        if bot and bot.model_name=="ER-Sigrid m2":
          bot_found=1
          temp_string=temp_string+"Bot Name:  {mark}"+str(bot.name)+"{/}\n{size=-8}- Bot Model:  {mark}ER-Sigrid m2{/}\n- Bot Rate:  {mark}S{/}\n" 
          part_test=1                                                     ## assume part test pass, failed test will negate
          for slot in bot.outfit_slots: 
            part=bot.item_on_slot(slot)
            if part.rate in "FEDCBA":                                     ## if not in FEDCBA must be S
              part_test=0                                                 ## part fail flag
              temp_string=temp_string+"- Parts:  {bad}Fail{/}\n"
              break                                                       ## remaining parts don't matter
          if part_test==1:
            temp_string=temp_string+"- Parts:  {good}Pass{/}\n"
          if bot.chassis.integrity<100:
            temp_string=temp_string+"- Integrity:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Integrity:  {good}Pass{/}\n"
          if bot.psychocore.stability<100:  
            temp_string=temp_string+"- Stability:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Stability:  {good}Pass{/}\n"
          if bot.bot_combat.level_name=="S":
            temp_string=temp_string+"- Combat Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Combat Skill:  {bad}Fail{/}\n" 
          if bot.bot_sex.level_name=="S":
            temp_string=temp_string+"- Sex Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Sex Skill:  {bad}Fail{/}\n"  
          if bot.bot_social.level_name=="S":
            temp_string=temp_string+"- Social Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Social Skill:  {bad}Fail{/}\n"    
          if bot["mission"]:
            temp_string=temp_string+"- {bad}Bot currently on mission{/}"
          temp_string=temp_string+"\n{/}"
  if bot_found==0:
    "You do not have any {mark}ER-Sigrid m2{/} bots."
  else:
    $act.start_block("l:440 c:content_width-440")
    center "{image=bots squirrel_sigrid avatar@400x600}"
    $act.set_block("c")
    "[temp_string]"
  choice("bp_bot_check_4_b") "Continue" 
  return

label bp_bot_check_4_b():                                                 ## MALE BOT IN PAIR
  $game_bg="home bg"                                                      ## home background
  header "Business Partnership Assignment Bot Check"                      ## home background
  python:
    bot_found=0                                                           ## flag for finding at least one bot
    temp_string=""                                                        ## for displaying results
    for bots_storage in (home.sexbots,workshop.sexbots):                  ## loop through all bots
      for bot in bots_storage:
        if bot and bot.model_name=="ER-Brutus III":
          bot_found=1
          temp_string=temp_string+"Bot Name:  {mark}"+str(bot.name)+"{/}\n{size=-8}- Bot Model:  {mark}ER-Brutus III{/}\n- Bot Rate:  {mark}S{/}\n" 
          part_test=1                                                     ## assume part test pass, failed test will negate
          for slot in bot.outfit_slots: 
            part=bot.item_on_slot(slot)
            if part.rate in "FEDCBA":                                     ## if not in FEDCBA must be S
              part_test=0                                                 ## part fail flag
              temp_string=temp_string+"- Parts:  {bad}Fail{/}\n"
              break                                                       ## remaining parts don't matter
          if part_test==1:
            temp_string=temp_string+"- Parts:  {good}Pass{/}\n"
          if bot.chassis.integrity<100:
            temp_string=temp_string+"- Integrity:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Integrity:  {good}Pass{/}\n"
          if bot.psychocore.stability<100:  
            temp_string=temp_string+"- Stability:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Stability:  {good}Pass{/}\n"
          if bot.bot_combat.level_name=="S":
            temp_string=temp_string+"- Combat Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Combat Skill:  {bad}Fail{/}\n" 
          if bot.bot_sex.level_name=="S":
            temp_string=temp_string+"- Sex Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Sex Skill:  {bad}Fail{/}\n"  
          if bot.bot_social.level_name=="S":
            temp_string=temp_string+"- Social Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Social Skill:  {bad}Fail{/}\n"    
          if bot["mission"]:
            temp_string=temp_string+"- {bad}Bot currently on mission{/}"
          temp_string=temp_string+"\n{/}"
  if bot_found==0:
    "You do not have any {mark}ER-Brutus III{/} bots."
  else:
    $act.start_block("l:440 c:content_width-440")
    center "{image=bots squirrel_brute avatar@400x600}"
    $act.set_block("c")
    "[temp_string]"
  choice("<<<") "Done"
  return

label bp_bot_check_5():                                                   ## FEMALE BOT IN PAIR
  $game_bg="home bg"                                                      ## home background
  header "Business Partnership Assignment Bot Check"                      ## home background
  python:
    bot_found=0                                                           ## flag for finding at least one bot
    temp_string=""                                                        ## for displaying results
    for bots_storage in (home.sexbots,workshop.sexbots):                  ## loop through all bots
      for bot in bots_storage:
        if bot and bot.model_name=="Bride of Frankie":                    ## DNS FLAG SET, SHOULD ALWAYS FIND A BOT
          bot_found=1
          temp_string=temp_string+"Bot Name:  {mark}"+str(bot.name)+"{/}\n{size=-8}- Bot Model:  {mark}Bride of Frankie{/}\n- Bot Rate:  {mark}A{/}\n" 
          part_test=1                                                     ## assume part test pass, failed test will negate
          for slot in bot.outfit_slots: 
            part=bot.item_on_slot(slot)
            if part.rate in "FEDCBA":                                     ## if not in FEDCBA must be S
              part_test=0                                                 ## part fail flag
              temp_string=temp_string+"- Parts:  {bad}Fail{/}\n"
              break                                                       ## remaining parts don't matter
          if part_test==1:
            temp_string=temp_string+"- Parts:  {good}Pass{/}\n"
          if bot.chassis.integrity<100:
            temp_string=temp_string+"- Integrity:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Integrity:  {good}Pass{/}\n"
          if bot.psychocore.stability<100:  
            temp_string=temp_string+"- Stability:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Stability:  {good}Pass{/}\n"
          if bot.bot_combat.level_name=="S":
            temp_string=temp_string+"- Combat Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Combat Skill:  {bad}Fail{/}\n" 
          if bot.bot_sex.level_name=="S":
            temp_string=temp_string+"- Sex Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Sex Skill:  {bad}Fail{/}\n"  
          if bot.bot_social.level_name=="S":
            temp_string=temp_string+"- Social Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Social Skill:  {bad}Fail{/}\n"    
          if bot["mission"]:
            temp_string=temp_string+"- {bad}Bot currently on mission{/}"
          temp_string=temp_string+"\n{/}"
  if bot_found==0:                                                        ## SHOULD NOT BE ABLE TO HAPPEN, DNS FLAG SHOULD BE SET
    "You do not have a {mark}Bride of Frankie{/} bot."
  else:
    $act.start_block("l:440 c:content_width-440")
    center "{image=bots frankie_bride_bot avatar@400x600}"
    $act.set_block("c")
    "[temp_string]"
  choice("bp_bot_check_5_b") "Continue"
  return

label bp_bot_check_5_b():                                                 ## MALE BOT IN PAIR
  $game_bg="home bg"                                                      ## home background
  header "Business Partnership Assignment Bot Check"                      ## home background
  python:
    bot_found=0                                                           ## flag for finding at least one bot
    temp_string=""                                                        ## for displaying results
    for bots_storage in (home.sexbots,workshop.sexbots):                  ## loop through all bots
      for bot in bots_storage:
        if bot and bot.model_name=="Frankie":                             ## DNS FLAG SET, SHOULD ALWAYS FIND A BOT
          bot_found=1
          temp_string=temp_string+"Bot Name:  {mark}"+str(bot.name)+"{/}\n{size=-8}- Bot Model:  {mark}Frankie{/}\n- Bot Rate:  {mark}A{/}\n" 
          part_test=1                                                     ## assume part test pass, failed test will negate
          for slot in bot.outfit_slots: 
            part=bot.item_on_slot(slot)
            if part.rate in "FEDCBA":                                     ## if not in FEDCBA must be S
              part_test=0                                                 ## part fail flag
              temp_string=temp_string+"- Parts:  {bad}Fail{/}\n"
              break                                                       ## remaining parts don't matter
          if part_test==1:
            temp_string=temp_string+"- Parts:  {good}Pass{/}\n"
          if bot.chassis.integrity<100:
            temp_string=temp_string+"- Integrity:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Integrity:  {good}Pass{/}\n"
          if bot.psychocore.stability<100:  
            temp_string=temp_string+"- Stability:  {bad}Fail{/}\n"
          else:
            temp_string=temp_string+"- Stability:  {good}Pass{/}\n"
          if bot.bot_combat.level_name=="S":
            temp_string=temp_string+"- Combat Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Combat Skill:  {bad}Fail{/}\n" 
          if bot.bot_sex.level_name=="S":
            temp_string=temp_string+"- Sex Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Sex Skill:  {bad}Fail{/}\n"  
          if bot.bot_social.level_name=="S":
            temp_string=temp_string+"- Social Skill:  {good}Pass{/}\n"
          else:
            temp_string=temp_string+"- Social Skill:  {bad}Fail{/}\n"    
          if bot["mission"]:
            temp_string=temp_string+"- {bad}Bot currently on mission{/}"
          temp_string=temp_string+"\n{/}"
  if bot_found==0:                                                        ## SHOULD NOT BE ABLE TO HAPPEN, DNS FLAG SHOULD BE SET
    "You do not have a {mark}Frankie{/} bot."
  else:
    $act.start_block("l:440 c:content_width-440")
    center "{image=bots frankie_bot avatar@400x600}"
    $act.set_block("c")
    "[temp_string]"
  choice("<<<") "Done"
  return
