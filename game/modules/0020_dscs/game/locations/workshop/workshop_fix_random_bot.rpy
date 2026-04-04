init python:
  def workshop_get_repairable_bots():
    bots=[]
    for bot in home.sexbots:
      if bot:
        if not bot["mission"]:
          for slot,part in bot.outfit.items():
            defects=[(defect_n,defect) for defect_n,defect in enumerate(part.defects)]
            if defects:
              defects.sort(key=lambda x: (100-x[1].integrity_cap,x[1].fix_progress))
              if defects[-1][1].repairable:
                bots.append(("defect",bot.id,slot,defects[-1][0]))
                continue
                
##  fix in version 0.0.6 to prevent repairing a 'missing part' - part.rate for missing parts is "", all others are FEDCBAS
##  this routine builds a list of possible parts in bots to repair, let's not append a missing part to the list
            ##if part.integrity<part.integrity_cap:                  ##  ORIGINAL LINE
            if part.integrity<part.integrity_cap and part.rate:    ##  NEW LINE

                bots.append(("repair",bot.id,slot))
    return bots

  def workshop_get_random_repairable_bot():
    bots=workshop_get_repairable_bots()
    return randchoice(bots) if bots else None

  def label_workshop_fix_random_bot_action_info(**kwargs):
    if workshop_get_repairable_bots():
      kwargs["cost"]=[("energy",1)]
    else:
      kwargs["action"]=None
      kwargs["hint"]="{hint}no repairable bots{/}"
    return kwargs

label workshop_fix_random_bot:
  $workshop_random_tinker_target=workshop_get_random_repairable_bot()
  if workshop_random_tinker_target:
    if workshop_random_tinker_target[0]=="repair":
      return "workshop_fix_random_bot_part:"+",".join([str(v) for v in workshop_random_tinker_target[1:]]) #+",workshop_fix_random_bot"
    else:
      return "workshop_fix_random_bot_part_defect:"+",".join([str(v) for v in workshop_random_tinker_target[1:]]) #+",workshop_fix_random_bot"
  else:
    return "<<<"

label workshop_fix_random_bot_part(bot_part):
  $bot,part=bot_part.split(",")
  $bot=find_character(bot)
  $part=bot.chassis[part]
  header "[bot] - [part] - Repair"
  "You check the bots in capsules looking for damaged bots."                                     ## removed storage room, they cost extra AP so not done
  "You notice {mark}[bot.posname]{/} [part.slot!l] part - {mark}[part]{/} can use some repair."
  ""
  "You try to fix {mark}[part]{/}..."
  $assistants=active_bots_with_role_tag("techie",bot)  ## Note: 'assistants' list never includes bot being repaired

##  $print "assistants complete list"
##  $print assistants
##  $print

## 0.14.n BUG FIX, should have been added in 0.10.n: change to avoid 'double dipping' roles
  $tech_bot_new_assignment=0                           ## clear counter before starting
  $bot_count=0
  while bot_count<len(assistants):                     ## go through assistants to remove ones just assigned
    $temp_bot=assistants[bot_count]
    if temp_bot[0].tech_just_assigned==1:              ## if assigned role this turn, will be cleared next rest, sleep, or work
      $tech_bot_new_assignment+=1                      ## increment count of bots just assigned
      $assistants.pop(bot_count)                       ## remove bot from assistants - do not increment counter
    else:
      $bot_count+=1                                    ## increment bot count for while loop
## 0.14.n end of insertion

##  $print "assistants after removing just assigned and fixing self"
##  $print assistants
##  $print

  $assistants_bonus=sum(((assistant.bot_electronics.level+assistant.bot_mechanics.level)*role_efficiency for assistant,role_efficiency in assistants))/2.0
  if assistants and assistants_bonus>0:
    $assistant=randchoice(assistants)[0]
    if len(assistants)>1:
      "{mark}[assistant]{/} and other techie bots help you with minor tasks, allowing you to focus on more complicated issues."
    else:
      "{mark}[assistant]{/} help you with minor tasks, allowing you to focus on more complicated issues."
  ""
  python:
    progress=mc.calc_part_repair_progress(bot,part,assistants_bonus)
    progress=min(part.integrity_cap,part.integrity+progress)-part.integrity
    part.integrity+=progress
    base_xp_reward=int(progress*part.difficulty)
    skill_xp_reward=int(base_xp_reward*2)
  "You restore {mark}[progress]%%{/} of {mark}[part]{/} integrity."
  if part.integrity==100:
    "You {mark}fully restore{/} integrity of {mark}[part]{/}!"
  else:
    "Current integrity is {mark}[part.integrity]%%{/}."
  python hide:
    skills=[(getattr(mc,skill).level,weight) for skill,weight in part.repair_skills]
    total_weight=sum((weight for level,weight in skills))
    for skill,weight in part.repair_skills:
      mc.give_xp(skill,skill_xp_reward*weight//total_weight)
    mc.give_xp("expertise_"+bot.model_id,base_xp_reward)

##  fix in version 0.0.6 to prevent gaining expertise in a 'missing part' - part.rate for missing parts is "", all others are FEDCBAS
##  this line gives part expertise, make it conditional
##    print "part id: ",part.id
##    print "part.rate: ",part.rate
    if part.rate<>"":
      mc.give_xp("expertise_"+part.id,base_xp_reward)
    
    for assistant,role_efficiency in assistants:
      assistant.give_xp("bot_mechanics",max(0,randint(-75,25)))
      assistant.give_xp("bot_electronics",max(0,randint(-100,25)))
  $assistant=None
  $assistants=None
  $bot=None
  $part=None
  ## @@REPEAT_ACTION
  if show_repeat_action():
    choice("workshop_fix_random_bot") "Repeat"
    choice("<<<") "Back"
  else:
    choice("<<<") "Continue"
  choice("goto_workshop",pos=17,key=("home","cancel")) "Done"
  return

label workshop_fix_random_bot_part_defect(bot_part_defect):
  $bot,part,defect=bot_part_defect.split(",")
  $bot=find_character(bot)
  $part=bot.chassis[part]
  $defect=part.defects[int(defect)]
  header "[bot] - [part] - Repair"
  "You check the bots in capsules looking for damaged bots."                                     ## removed storage room, they cost extra AP so not done
  "You notice {mark}[bot.posname]{/} [part.slot!l] part - {mark}[part]{/} can use some repair."
  ""
  "You try to fix {mark}[defect]{/} defect..."
  $assistants=active_bots_with_role_tag("techie",bot)  ## Note: 'assistants' list never includes bot being repaired

##  $print "assistants complete list"
##  $print assistants
##  $print

## 0.14.n BUG FIX, should have been added in 0.10.n: change to avoid 'double dipping' roles
  $tech_bot_new_assignment=0                           ## clear counter before starting
  $bot_count=0
  while bot_count<len(assistants):                     ## go through assistants to remove ones just assigned
    $temp_bot=assistants[bot_count]
    if temp_bot[0].tech_just_assigned==1:              ## if assigned role this turn, will be cleared next rest, sleep, or work
      $tech_bot_new_assignment+=1                      ## increment count of bots just assigned
      $assistants.pop(bot_count)                       ## remove bot from assistants - do not increment counter
    else:
      $bot_count+=1                                    ## increment bot count for while loop
## 0.14.n end of insertion

##  $print "assistants after removing just assigned and fixing self"
##  $print assistants
##  $print

  $assistants_bonus=sum(((assistant.bot_electronics.level+assistant.bot_mechanics.level)*role_efficiency for assistant,role_efficiency in assistants))/2.0
  if assistants and assistants_bonus>0:
    $assistant=randchoice(assistants)[0]
    if len(assistants)>1:
      "{mark}[assistant]{/} and other techie bots help you with minor tasks, allowing you to focus on more complicated issues."
    else:
      "{mark}[assistant]{/} help you with minor tasks, allowing you to focus on more complicated issues."

## 0.14.n BUG FIX, should have been added in 0.10.n add comment if techies just assigned only when there are no assistants
  if not assistants:
    if tech_bot_new_assignment==0:
      "Maybe I should have {mark}Techie{/} bots and keep them at home in capsules so they can help be with repairs."
    elif tech_bot_new_assignment==1:
      "I just assigned a bot the {mark}Techie{/} role so they will help me when I'm working in the shop."
    elif tech_bot_new_assignment>1:
      "I just assigned bots the {mark}Techie{/} role so they will help me when I'm working in the shop." 
## 0.14.n end of insertion

  ""
  python:
    progress=mc.calc_part_defect_repair_progress(bot,part,defect,assistants_bonus)
    progress=min(100,defect.fix_progress+progress)-defect.fix_progress
    defect.fix_progress+=progress
    base_xp_reward=int(progress*part.difficulty*defect.difficulty)
    skill_xp_reward=int(base_xp_reward*2)
  "You fix {mark}[progress]%%{/} of {mark}[defect]{/}."
  if defect.fix_progress==100:
    "You {mark}fully fix{/} defect - {mark}[defect]{/}!"
    $part.defects.remove(defect)
  else:
    "Current progress is {mark}[defect.fix_progress]%%{/}."
  python hide:
    skills=[(getattr(mc,skill).level,weight) for skill,weight in part.repair_skills]
    total_weight=sum((weight for level,weight in skills))
    for skill,weight in part.repair_skills:
      mc.give_xp(skill,skill_xp_reward*weight//total_weight)
    mc.give_xp("expertise_"+bot.model_id,base_xp_reward)

##  fix in version 0.0.6 to prevent gaining expertise in a 'missing part' - part.rate for missing parts is "", all others are FEDCBAS
##  this line gives part expertise, make it conditional
##    print "part id: ",part.id
##    print "part.rate: ",part.rate
    if part.rate<>"":
      mc.give_xp("expertise_"+part.id,base_xp_reward)

    for assistant,role_efficiency in assistants:
      assistant.give_xp("bot_mechanics",max(0,randint(-75,25)))
      assistant.give_xp("bot_electronics",max(0,randint(-100,25)))
  $assistant=None
  $assistants=None
  $bot=None
  $part=None
  $defect=None
  ## @@REPEAT_ACTION
  if show_repeat_action():
    choice("workshop_fix_random_bot") "Repeat"
    choice("<<<") "Back"
  else:
    choice("<<<") "Continue"
  choice("goto_workshop",pos=17,key=("home","cancel")) "Done"
  return
