##====mob protection bot verification

##===bot check-standard bots===

label hw_test_bot_for_mob:
  $game_bg="home bg"         ##  home background
  header "Bot's Meeting Mob Requirements"    ##  home background

  python:
    temp_string=""       ## for displaying bot results
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot and bot.action_allowed("sell"):                                   ## must be: a bot that didn't come from a "repair order"
          temp_string=temp_string+"{mark}"+bot.name+", "+bot.model_name+":{/}"
          mbc_bot_pass=1                                                         ## assume bot passes, set to 1
          if bot.gender=="male":
            temp_string=temp_string+"-gender"
            mbc_bot_pass=0                                                       ## bot is male
          if bot.rate_level<mobprotection_bot_rating:
            temp_string=temp_string+"-bot rate"
            mbc_bot_pass=0                                                       ## bot rating too low
          mbc_skills_temp=0                                                      ## reset temp skills counter
          if bot.bot_combat.level_name in mobprotection_combat_skill:
            mbc_skills_temp+=1                                                   ## for skills increment: need to pass all 5 skills so pass value is 5
          if bot.bot_electronics.level_name in mobprotection_electronics_skill:
            mbc_skills_temp+=1
          if bot.bot_mechanics.level_name in mobprotection_mechanics_skill:
            mbc_skills_temp+=1
          if bot.bot_sex.level_name in mobprotection_sex_skill:
            mbc_skills_temp+=1
          if bot.bot_social.level_name in mobprotection_social_skill:
            mbc_skills_temp+=1
          if mbc_skills_temp<5:                                                  ## all 5 skills must pass
            temp_string=temp_string+"-skill(s)"
            mbc_bot_pass=0                                                       ## bot does not meet all skill requirements
          mobprotection_part_test_pass=1
          for slot in bot.outfit_slots:
            part=bot.item_on_slot(slot)
            if part.rate in mobprotection_part_rating:                           ## part rating uses reverse logic
              mobprotection_part_test_pass=0
              break                                                              ##  stop testing on failure, part quantity or identity irrelevant
          if mobprotection_part_test_pass==0:                                    ## 
            temp_string=temp_string+"-part(s)"
            mbc_bot_pass=0                                                       ## bot does not meet all skill requirements
          if bot.chassis.integrity<mobprotection_integrity_minimum:
            temp_string=temp_string+"-integrity"
            mbc_bot_pass=0                                                       ## bot integrity too low
          if bot.psychocore.stability<mobprotection_stability_minimum:
            temp_string=temp_string+"-stability"
            mbc_bot_pass=0                                                       ## bot stability too low
          if bot.do_not_sell:
            temp_string=temp_string+"-DNS"
            mbc_bot_pass=0                                                       ## bot is marked DNS
          if bot["mission"]:
            temp_string=temp_string+"-mission"
            mbc_bot_pass=0                                                       ## bot on mission
          if mbc_bot_pass==1:                                                    ## bot passed all tests
            bot_price=bot_price_function(bot)  ## DO NOT OMIT
            bots.append([bot,bot_price])       ## DO NOT OMIT
          temp_string=temp_string+"\n"
    bots=bots[:12]
  if bots:
    if len(bots)==1:
      ""
      "This bot will meet the mob's requirements for this week:"
      ""
    else:
      ""
      "The following bots meet the mob's requirements for this week:"
      ""
    while bots:
      $bot,bot_price=bots.pop(0)
      "{mark}[bot]{/}, model: {mark}[bot.model_name]{/}"
  else:
    ""
    "{bad}I don't have any bots that meet the mob's requirements for this week.{/}"
    ""
    "1) Check the {mark}Active Quests{/} section in the {mark}Journal{/} to see the mob's requirements."
    ""
    "2) {mark}Do NOT{/} mark bots intended for the mob {mark}'do not sell' (DNS){/}, only use that for bots you don't want to give the mob by mistake!"
    ""
    "3) {mark}Don't{/} send bots intended for the mob on {mark}missions{/}, they might get damaged and they might not be here when the mobsters come on {mark}Friday evenings{/}."
    ""
    "4) Consider putting bots intended for the mob {mark}into storage{/} to make sure they remain in perfect condition."
    ""
    "{bad}Requirements each bot does NOT meet:{/}"
    "{size=-8}[temp_string]{/}"
  $bot=None
  choice("<<<") "Continue"
  return

##===bot check-sabotage bot===

label hw_test_special_bot_for_mob:
  $game_bg="home bg"                    ##  home background
  header "Bot's For My Sabotage Plan "  ##  home background

  python:
    temp_string=""          ## for displaying bot results
    mbc_skill_any="FEDCBAS" ## used for any skill level
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot and bot.action_allowed("sell"):                                   ## must be: a bot that didn't come from a "repair order"
          temp_string=temp_string+"{mark}"+bot.name+", "+bot.model_name+":{/}"
          mbc_bot_pass=1                                                         ## assume bot passes, set to 1
          if bot.gender=="male":
            temp_string=temp_string+"-gender"
            mbc_bot_pass=0                                                       ## bot is male
          if bot.rate_level<mobprotection_special_bot_rating:
            temp_string=temp_string+"-bot rate"
            mbc_bot_pass=0                                                       ## bot rating too low
          mbc_skills_temp=0                                                      ## reset temp skills counter
          if bot.bot_combat.level_name in mbc_skill_any:                         ## combat skill not used for special bot
            mbc_skills_temp+=1                                                   ## for skills increment: need to pass all 5 skills so pass value is 5
          if bot.bot_electronics.level_name in mbc_skill_any:                    ## electronics skill not used for special bot
            mbc_skills_temp+=1
          if bot.bot_mechanics.level_name in mbc_skill_any:                      ## mechanics skill not used for special bot
            mbc_skills_temp+=1
          if bot.bot_sex.level_name in mobprotection_special_bot_sex_skill:
            mbc_skills_temp+=1
          if bot.bot_social.level_name in mobprotection_special_bot_social_skill:
            mbc_skills_temp+=1
          if mbc_skills_temp<5:                                                  ## all 5 skills must pass
            temp_string=temp_string+"-skill(s)"
            mbc_bot_pass=0                                                       ## bot does not meet all skill requirements
          mobprotection_part_test_pass=1
          for slot in bot.outfit_slots:
            part=bot.item_on_slot(slot)
            if part.rate in mobprotection_special_bot_part_rating:               ## part rating uses reverse logic
              mobprotection_part_test_pass=0
              break                                                              ##  stop testing on failure, part quantity or identity irrelevant
          if mobprotection_part_test_pass==0:                                    ## 
            temp_string=temp_string+"-part(s)"
            mbc_bot_pass=0                                                       ## bot does not meet all skill requirements
          if bot.chassis.integrity<mobprotection_special_bot_integrity_minimum:
            temp_string=temp_string+"-integrity"
            mbc_bot_pass=0                                                       ## bot integrity too low
          if bot.psychocore.stability<mobprotection_special_bot_stability_minimum:
            temp_string=temp_string+"-stability"
            mbc_bot_pass=0                                                       ## bot stability too low
          if bot.do_not_sell:
            temp_string=temp_string+"-DNS"
            mbc_bot_pass=0                                                       ## bot is marked DNS
          if bot["mission"]:
            temp_string=temp_string+"-mission"
            mbc_bot_pass=0                                                       ## bot on mission
          if mbc_bot_pass==1:                                                    ## bot passed all tests
            bot_price=bot_price_function(bot)  ## DO NOT OMIT
            bots.append([bot,bot_price])       ## DO NOT OMIT
          temp_string=temp_string+"\n"
    bots=bots[:12]
  if bots:
    if len(bots)==1:
      ""
      "This bot meet the requirements for my {mark}Sabotage Bot Plan{/}:"
      ""
    else:
      ""
      "The following bots meet the requirements for my {mark}Sabotage Bot Plan{/}:"
      ""
    while bots:
      $bot,bot_price=bots.pop(0)
      "{mark}[bot]{/}, model: {mark}[bot.model_name]{/}"
  else:
    ""
    "I {mark}do NOT{/} have any bots that can be used for my {mark}Sabotage Bot Plan{/}."
    ""
    "1) Check the requirements for my {mark}Sabotage Bot Plan{/} in the {mark}Active Quests{/} section in the {mark}Journal{/}."
    ""
    "2) {mark}Do NOT{/} mark bots intended for the mob {mark}'do not sell' (DNS){/}, only use that for bots you don't want to give the mob by mistake!"
    ""
    "3) {mark}Don't{/} send bots intended for the mob on {mark}missions{/}, they might get damaged and they might not be here when the mobsters come on {mark}Friday evenings{/}."
    ""
    "4) Consider putting bots intended for the mob {mark}into storage{/} to make sure they remain in perfect condition."
    ""
    "Requirements for my {mark}Sabotage Bot Plan{/} that each bot {mark}does NOT{/} meet:"
    "{size=-8}[temp_string]{/}"
  $bot=None
  choice("<<<") "Continue"
  return
