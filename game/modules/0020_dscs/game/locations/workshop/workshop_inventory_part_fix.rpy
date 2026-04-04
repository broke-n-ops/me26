define label_workshop_fix_part_action_info={"cost":[("energy",1)]}

label workshop_fix_part(part_n_repeat):
  python:
    part_n,sep,repeat_label=part_n_repeat.partition(",")
    part=workshop.inventory[int(part_n)]
  header "[part] - Repair"
  "You try to repair {mark}[part]{/}..."
  $assistants=active_bots_with_role_tag("techie")
  $assistants_bonus=sum(((assistant.bot_electronics.level+assistant.bot_mechanics.level)*role_efficiency for assistant,role_efficiency in assistants))/2.0
  if assistants and assistants_bonus>0:
    $assistant=randchoice(assistants)[0]
    if len(assistants)>1:
      "{mark}[assistant]{/} and other techie bots help you with minor tasks, allowing you to focus on more complicated issues."
    else:
      "{mark}[assistant]{/} help you with minor tasks, allowing you to focus on more complicated issues."
  else:    ##  NO ASSISTANTS
    "I spend a lot of time making repairs, I could use a techie bot or two."
  ""
  python:
    progress=mc.calc_part_repair_progress(None,part,assistants_bonus)
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

##  fix in version 0.0.6 to prevent gaining expertise in a 'missing part' - part.rate for missing parts is "", all others are FEDCBAS
##  this line gives part expertise, make it conditional
    if part.rate<>"":
      mc.give_xp("expertise_"+part.id,base_xp_reward)

    for assistant,role_efficiency in assistants:
      assistant.give_xp("bot_mechanics",max(0,randint(-75,25)))
      assistant.give_xp("bot_electronics",max(0,randint(-100,25)))
  $assistant=None
  $assistants=None
  ## @@REPEAT_ACTION
  if show_repeat_action():
    if repeat_label:
      choice(repeat_label) "Repeat"
    elif part.integrity<part.integrity_cap:
      choice("workshop_fix_part:"+part_n) "Repeat"
    elif part.integrity==100:
      choice(None,hint="{hint}already repaired{/}") "Repeat"
    else:
      choice(None,cost=[("energy",1)]) "Repeat"
    choice("<<<") "Back"
  else:
    if repeat_label:
      choice(repeat_label) "Repeat"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  $part=None
  return

define label_workshop_fix_part_defect_action_info={"cost":[("energy",1)]}

label workshop_fix_part_defect(part_and_defect_and_repeat):
  python:
    part_n,sep,defect_n_and_repeat=part_and_defect_and_repeat.partition(",")
    part=workshop.inventory[int(part_n)]
    defect_n,sep,repeat_label=defect_n_and_repeat.partition(",")
    defect=part.defects[int(defect_n)]
  header "[part] - [defect] - Repair"
  "You try to fix {mark}[defect]{/}..."
  $assistants=active_bots_with_role_tag("techie")
  $assistants_bonus=sum(((assistant.bot_electronics.level+assistant.bot_mechanics.level)*role_efficiency for assistant,role_efficiency in assistants))/2.0
  if assistants and assistants_bonus>0:
    $assistant=randchoice(assistants)[0]
    if len(assistants)>1:
      "{mark}[assistant]{/} and other techie bots help you with minor tasks, allowing you to focus on more complicated issues."
    else:
      "{mark}[assistant]{/} help you with minor tasks, allowing you to focus on more complicated issues."
  ""
  python:
    progress=mc.calc_part_defect_repair_progress(None,part,defect,assistants_bonus)
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

##  fix in version 0.0.6 to prevent gaining expertise in a 'missing part' - part.rate for missing parts is "", all others are FEDCBAS
##  this line gives part expertise, make it conditional
    if part.rate<>"":
      mc.give_xp("expertise_"+part.id,base_xp_reward)

    for assistant,role_efficiency in assistants:
      assistant.give_xp("bot_mechanics",max(0,randint(-75,25)))
      assistant.give_xp("bot_electronics",max(0,randint(-100,25)))
  $assistant=None
  $assistants=None
  ## @@REPEAT_ACTION
  if show_repeat_action():
    if repeat_label:
      choice(repeat_label) "Repeat"
    elif defect.fix_progress<100:
      choice("workshop_fix_part_defect:"+part_n+","+defect_n) "Repeat"
    else:
      python:
        defects=[(defect_n,defect) for defect_n,defect in enumerate(part.defects)]
        defects.sort(key=lambda x: (100-x[1].integrity_cap,x[1].fix_progress))
      if defects and defects[-1][1].repairable:
        choice("workshop_fix_part_defect:"+part_n+","+str(defects[-1][0]),cost=[("energy",1)]) "Repeat"
      else:
        choice(None,cost=[("energy",1)]) "Repeat"
    choice("<<<") "Back"
  else:
    if repeat_label:
      choice(repeat_label) "Repeat"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  $part=None
  $defect=None
  $defects=None
  return
