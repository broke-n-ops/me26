##=========INIT VARIABLES=========
init python:
  tinker_last_row=0          ##  number of rows needed to display all slots: 6 slots per row; vanilla game has 11 already, Daedalron adds 5, could create dummies for testing
  tech_bot_new_assignment=0  ## 0.10.n - counter for bots just assigned

##============FUNCTIONS============

label interact_default_include_tinker_attach_bot(bot):
  if home["workshop_bot"]==bot.id:  ## This is shown after completing an action within 'Tinker'
    "{mark}[bot]{/} lies on the gurney with the scanner under the robotic arm. The scanner shows the status of [bot.hisher] {mark}parts{/}."
  else:
    if bot.chassis.is_disabled:     ## This is shown when you click on 'Tinker' with a disabled bot
      "You place disabled {mark}[bot]{/} on the gurney with the scanner under the robotic arm. You set the scanner to show the status of [bot.hisher] {mark}parts{/}."
    else:                           ## This is shown when you click on 'Tinker' with a normal bot
      "You tell {mark}[bot]{/} to lie on the gurney with the scanner under the robotic arm. You set the scanner to show the status of [bot.hisher] {mark}parts{/}."
  $home["workshop_bot"]=bot.id
  ""
  return

label interact_default_tinker(bot):
  header "[workshop] - [bot]"
  call interact_include("tinker_attach_bot")
  $act.add_screen("status_sexbot_page_chassis_status",bot.id,False)
  $tinker_part_slots=[find_item_slot(slot) for slot in bot.outfit_slots]
  $tinker_first_slot=(tinker_current_row-1)*6          ##  row 1=0, row 2=6, row 3=12, etc.
  $tinker_last_slot=len(tinker_part_slots)             ##  tentatively set last slot to end of list
## change made in v0.4.n
  $temp_float=float(tinker_last_slot-0.1)              ## deleting a fraction to avoid extra button with 12 slots
  $tinker_last_row=int(temp_float/6)+1                 ##  should be 2 for vanilla game, 3 if you add Daedalron Bots, etc.
  if tinker_last_slot>tinker_first_slot+12:            ##  if NOT true display all, if true cannot display all
    $tinker_last_slot=tinker_first_slot+12             ##  last displayed slot will be 12 more than first displayed slot - 2 full rows
  $count=0
  $max_count=tinker_last_slot-tinker_first_slot
  while count < max_count:                             ##  count is number of slots to display - -1 because we start with 0
    $pop_number=tinker_first_slot+count
    $tinker_part_slot=tinker_part_slots[pop_number]    ##  changed from 'pop' function to make the scroll work, see line above
    $count+=1
    $tinker_part=bot.item_on_slot(tinker_part_slot)
    if tinker_part:
      interact("tinker_bot_part,"+tinker_part_slot.id) "[tinker_part_slot]"
    else:
      choice(None) "[tinker_part_slot]"
  $tinker_part_slots=[]                                ## after using the array clear it like the previous 'pop' function did
  $tinker_part=None
  $tinker_part_slot=None
  if not bot.action_allowed("disassemble"):
    choice(None,pos=12,hint="{hint}not allowed{/}") "Disassemble"
  else:
    interact("disassemble",pos=12) "Disassemble"
  if tinker_last_row<3:                                     ##  only 2 rows; Down=NO, UP=NO
    choice(None,pos=14) "Scroll Up"
    choice(None,pos=15) "Scroll Down"
  elif tinker_last_row>tinker_current_row+1:                ##  CANNOT display last row; Down=Yes
    if tinker_current_row>1:                                ##  Top row NOT 1; Up=Yes
      interact("tinker_scroll_up",pos=14) "Scroll Up"
    else:                                                   ##  Top row 1; Up=NO
      interact(None,pos=14) "Scroll Up"
    interact("tinker_scroll_down",pos=15) "Scroll Down"
  else:                                                     ##  CAN display last row; Down=No
    if tinker_current_row>1:                                ##  Top row NOT 1; Up=Yes
      interact("tinker_scroll_up",pos=14) "Scroll Up"
    else:                                                   ##  Top row 1; Up=NO
      choice(None,pos=14) "Scroll Up"
    choice(None,pos=15) "Scroll Down"
##  TRIED REMOVING 'DONE' BUT IT IS PRESENT IN SUB-SCREENS SO IT'S INCONSISTENT
##  TO REMOVE IT I HAVE TO REMOVE IT FROM SUB-SCREENS TOO SO I'LL LEAVE IT
##  MAY CHANGE MY MIND LATER
  choice("end_bot_interaction",pos=16,key="home") "Done"    ##  tentative; remove done, forces 'back' but I think it will be more clear
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_tinker_scroll_up(bot):               ##  new scroll function
  $tinker_current_row-=2
  return "<<<"

label interact_default_tinker_scroll_down(bot):             ##  new scroll function
  $tinker_current_row+=2
  return "<<<"

label interact_default_tinker_bot_part(bot,part):
  $part=bot.chassis[part]
  $slot=find_item_slot(part.slot)
  header "[slot] - [part]"
  "Part name: {mark}[part]{/}."
  "Category: {mark}[slot]{/}. Rate: {mark}[part.rate]{/}."
  ""
  "[part.description]"
  ""
  if part.integrity==part.integrity_cap and part.integrity_cap!=100:
    "Integrity: {mark}[part.integrity]%%{/} {size=-8}{info}({bad}[part.integrity_cap]{/}/100){/}{/} -  defects do not allow full repair"
  else:
    "Integrity: {mark}[part.integrity]%%{/} {size=-8}{info}([part.integrity_cap]/100){/}{/}"
  if part.integrity==100 and not part.defects:
    "Part in {mark}perfect condition{/}, no repair required."

##  EDITED BY SQUIRREL IN VERSION 0.0.4 TO ACCOMMODATE "MISSING" PARTS

  if part.integrity<part.integrity_cap and part.damage_on_remove!="missing":    ##  you cannot "repair" a "missing" part

    interact("fix_bot_part,"+part.slot.id) "Fix part"
  else:
    choice(None) "Fix part"
  $defects=[(defect_n,defect) for defect_n,defect in enumerate(part.defects)]
  ""
  "Defects:"
  if defects:
    $defects.sort(key=lambda x: (100-x[1].integrity_cap,x[1].fix_progress))
    if defects[-1][1].repairable:
      interact("fix_bot_part_defect,"+part.slot.id+","+str(defects[-1][0])) "Fix defect"
    else:
      choice(None) "Fix defect"
    while defects:
      $defect_n,defect=defects.pop(0)
      if defect.repairable:
        "{bad}[defect]{/}, integrity cap: [defect.integrity_cap], fix progress: [defect.fix_progress]%%"
      else:
        "{bad}[defect]{/}, integrity cap: [defect.integrity_cap], {bad}irrepairable{/}"
      "{size=-8}{info}[defect.description]{/}{/}"
  else:
    "{info}There is no defects in this part.{/}"
    choice(None) "Fix defect"
  if not bot.action_allowed("replace_part"):
    choice(None,hint="{hint}not allowed{/}") "Replace"
  else:
    interact("replace_bot_part,"+part.slot.id+",0") "Replace"
  if part.do_not_sell:
    ""
    "This item is marked {mark}do-not-sell{/}."
    interact("bot_part_toggle_dns,"+part.slot.id,hint="toggle do-not-sell",pos=12) "DNS: on"
  else:
    interact("bot_part_toggle_dns,"+part.slot.id,hint="toggle do-not-sell",pos=12) "DNS: off"
  $defect=None
  $defects=None
  $part=None
  $slot=None
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_bot_part_toggle_dns(bot,slot):
  $part=bot.chassis[slot]
  $part.do_not_sell=not part.do_not_sell
  $part=None
  return "<<<"

define label_interact_default_fix_bot_part_action_info={"cost":[("energy",1)]}

label interact_default_fix_bot_part(bot,part_id):
  $part=bot.chassis[part_id]
  header "[part] - Repair"
  "You try to repair {mark}[part]{/}..."
  $assistants=active_bots_with_role_tag("techie",bot)  ## Note: 'assistants' list never includes bot being repaired

##  $print "assistants complete list"
##  $print assistants
##  $print

## 0.10.n change to avoid 'double dipping' roles
  $tech_bot_new_assignment=0               ## reset counter before starting
## 0.14.n delete 7 lines, function 'active_bots_with_role_tag' automatically ignores bot being repaired
##  $bot_in_repair=0                              ## assume bot in repair is NOT a techie
##  $efficiency=bot.role_tag_efficiency("techie")
##  if efficiency>0:                              ## bot is assigned techie role
##    if bot.tech_just_assigned==1:               ## check to see if just assigned (not active yet)
##      $tech_bot_new_assignment+=1               ## increment count of bots just assigned
##    else:
##      $bot_in_repair=1                          ## bot is active techie, cannot repair itself
  $bot_count=0
  while bot_count<len(assistants):         ## go through assistants to remove ones just assigned and self
    $temp_bot=assistants[bot_count]
    if temp_bot[0].tech_just_assigned==1:  ## if assigned role this turn, will be cleared next rest, sleep, or work
      $tech_bot_new_assignment+=1          ## increment count of bots just assigned
      $assistants.pop(bot_count)           ## remove bot from assistants - do not increment counter
    else:
      $bot_count+=1                        ## increment bot count for while loop
## 0.10.n end of insertion

##  $print "assistants after removing just assigned and fixing self"
##  $print assistants
##  $print

  $assistants_bonus=sum(((assistant.bot_electronics.level+assistant.bot_mechanics.level)*role_efficiency for assistant,role_efficiency in assistants))/2.0
  if assistants and assistants_bonus>0:
    ""  ## line feed to make next line more noticeable
    $assistant=randchoice(assistants)[0]
    if len(assistants)>1:
      "{mark}[assistant]{/} and other techie bots help you with minor tasks, allowing you to focus on more complicated issues."
    else:
      "{mark}[assistant]{/} help you with minor tasks, allowing you to focus on more complicated issues."

## 0.10.n add comments when no assistants: 1) if techie trying to repair itself, 2) if techies just assigned
  if not assistants:
    ""
    if tech_bot_new_assignment==0:   ## no techies just assigned
        
## 0.14.n delete 3 lines and fix indent on 4the line, assistant list cannot include bot being repaired
##      if bot_in_repair==1:           ## techie trying to repair itself with no other active techies
##        "[bot] is your only {mark}Techie{/} and cannot help you repair [bot.himher]self."
##      else:
      "Maybe I should have {mark}Techie{/} bots and keep them at home in capsules so they can help me with repairs."

    elif tech_bot_new_assignment==1: 
      "I just assigned a bot the {mark}Techie{/} role so in the future they will help me when I'm repairing bots."
    elif tech_bot_new_assignment>1:
      "I just assigned bots the {mark}Techie{/} role so in the future they will help me when I'm repairing bots."
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
    if part.rate<>"":
      mc.give_xp("expertise_"+part.id,base_xp_reward)

    for assistant,role_efficiency in assistants:
      assistant.give_xp("bot_mechanics",max(0,randint(-75,25)))
      assistant.give_xp("bot_electronics",max(0,randint(-100,25)))
  $assistant=None
  $assistants=None
  ## @@REPEAT_ACTION
  if show_repeat_action():
    if part.integrity<part.integrity_cap:
      interact("^fix_bot_part,"+part_id) "Repeat"
    elif part.integrity==100:
      choice(None,hint="{hint}already repaired{/}") "Repeat"
    else:
      choice(None,cost=[("energy",1)]) "Repeat"
    choice("<<<") "Back"
  else:
    choice("<<<") "Continue"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  $part=None
  return

define label_interact_default_fix_bot_part_defect_action_info={"cost":[("energy",1)]}

label interact_default_fix_bot_part_defect(bot,part_and_defect):
  $part,sep,defect=part_and_defect.partition(",")
  $part=bot.chassis[part]
  $defect=part.defects[int(defect)]
  header "[part] - [defect] - Repair"
  "You try to fix {mark}[defect]{/}..."
  $assistants=active_bots_with_role_tag("techie",bot)  ## Note: 'assistants' list never includes bot being repaired

##  $print "assistants complete list"
##  $print assistants
##  $print

## 0.10.n change to avoid 'double dipping' roles
  $tech_bot_new_assignment=0             ## reset counter before starting
  $bot_count=0
  while bot_count<len(assistants):    ## go through assistants to remove ones just assigned and self
    $temp_bot=assistants[bot_count]
    if temp_bot[0].tech_just_assigned==1:  ## if assigned role this turn, will be cleared next rest, sleep, or work
      $tech_bot_new_assignment+=1          ## increment count of bots just assigned
      $assistants.pop(bot_count)           ## remove bot from assistants - do not increment counter
    else:
      $bot_count+=1                      ## increment bot count for while loop
## 0.10.n end of insertion

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

## 0.10.n add comment if techies just assigned only when there are no assistants
  if not assistants:
    if tech_bot_new_assignment==0:
      "Maybe I should have {mark}Techie{/} bots and keep them at home in capsules so they can help me with repairs."
    elif tech_bot_new_assignment==1:
      "I just assigned a bot the {mark}Techie{/} role so they will help me when I'm working in the shop."
    elif tech_bot_new_assignment>1:
      "I just assigned bots the {mark}Techie{/} role so they will help me when I'm working in the shop."

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
    if part.rate<>"":
      mc.give_xp("expertise_"+part.id,base_xp_reward)

    for assistant,role_efficiency in assistants:
      assistant.give_xp("bot_mechanics",max(0,randint(-75,25)))
      assistant.give_xp("bot_electronics",max(0,randint(-100,25)))
  $assistant=None
  $assistants=None
  ## @@REPEAT_ACTION
  if show_repeat_action():
    if defect.fix_progress<100:
      interact("^fix_bot_part_defect,"+part_and_defect) "Repeat"
    else:
      python:
        defects=[(defect_n,defect) for defect_n,defect in enumerate(part.defects)]
        defects.sort(key=lambda x: (100-x[1].integrity_cap,x[1].fix_progress))
      if defects and defects[-1][1].repairable:
        interact("^fix_bot_part_defect,"+part.slot.id+","+str(defects[-1][0]),cost=[("energy",1)]) "Repeat"
      else:
        choice(None,hint="{hint}already fixed{/}") "Repeat"
    choice("<<<") "Back"
  else:
    choice("<<<") "Continue"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  $part=None
  $defect=None
  $defects=None
  return

init python:
  def make_part_replacements_list(slot,page):
    per_page=6
    rv=[]
    for n,item in enumerate(workshop.inventory):
      if item.slot==slot:
        rv.append((n,item))
    rv.sort(key=lambda x:(x[1].id,-x[1].integrity,len(x[1].defects)))
    n=len(rv)-1
    while n>0:
      if rv[n][1].id==rv[n-1][1].id:
        if rv[n][1].integrity==rv[n-1][1].integrity:
          if rv[n][1].defects==rv[n-1][1].defects:
            rv.pop(n)
      n-=1
    rv.sort(key=lambda x:(-x[1].rate_level,x[1].name.lower(),x[1].id,-x[1].integrity,len(x[1].defects)))
    total=(len(rv)+(per_page-1))//per_page
    if total>1:
      prev="^replace_bot_part,"+slot+","+str((page-1)%total)
      next="^replace_bot_part,"+slot+","+str((page+1)%total)
    else:
      prev=None
      next=None
    rv=rv[page*per_page:(page+1)*per_page]
    return rv,prev,next

label interact_default_replace_bot_part(bot,part_slot_page):
  $part_slot,sep,page=part_slot_page.partition(",")
  $part_slot=find_item_slot(part_slot)
  $page=int(page)
  $part=bot.chassis[part_slot.id]
  header "[part_slot] - Replace"
  $part_options,prev_page,next_page=make_part_replacements_list(part.slot.id,page)


##  ADDED BY SQUIRREL IN VERSION 0.0.4 - if you have a "missing" part and damage to the socket you cannot replace

  if part.damage_on_remove=="missing" and part.defects:              ##  You must repair the damage before inserting a new part
    "You must repair the damage before you can insert a new part."

  elif part_options:    ##  CHANGED TO elif BY SQUIRREL

    "You search for options you can use to replace {mark}[part]{/}. After some rummaging through the workshop inventory shelves, you found something."
    ""
    $act.add_screen("workshop_replace_part_info",part,[part_option[1] for part_option in part_options],show_descriptions=False)
    $part_n=0
    while part_options:
      $part_option=part_options.pop(0)
      $part_n+=1
      interact("replace_bot_part_do,"+part.slot.id+","+str(part_option[0])) "#[part_n] [part_option[1]]"
  else:
    "You rummage through the inventory shelves but find nothing fitting to replace {mark}[part]{/} with."
  $part_option=None
  $part=None
  $part_slot=None
  interact(prev_page,pos=12,key="z") "Prev"
  interact(next_page,pos=13,key="x") "Next"
  choice("<<<",pos=17,key="cancel") "Back"
  return

define label_interact_default_replace_bot_part_do_action_info={"cost":[("energy",1)]}

label interact_default_replace_bot_part_do(bot,part_slot_and_part_n):
  $part_slot,sep,part_n=part_slot_and_part_n.partition(",")
  $part_slot=find_item_slot(part_slot)
  $part=bot.chassis[part_slot.id]
  $new_part=workshop.inventory[int(part_n)]
  header "[part_slot] - Replace"

  python:
##    print "old part from 'interact_tinker.rpy' replace part: ",part
##    print "new part from 'interact_tinker.rpy' replace part: ",new_part
    workshop.remove_item(new_part)
    new_part.owner=bot
    bot.add_item(new_part)
    bot.equip(new_part)
    bot.remove_item(part)
    damage_on_remove=part.damage_on_remove

##  LINE EDITED BY SQUIRREL IN VERSION 0.0.4 - new flag for "damage_on_remove" of "missing" added

    if damage_on_remove!="missing" and isinstance(damage_on_remove,(list,tuple)):    ##  bypass if this is a "missing" part

      damage_on_remove=randint(100*damage_on_remove[0],100*damage_on_remove[1])
    elif damage_on_remove in ("max","destroy"):
      damage_on_remove="destroy"
    elif isinstance(damage_on_remove,float):
      damage_on_remove*=100

##  THIS WAS MOVED FROM BEFORE THE python: SECTION TO AFTERWARDS AND EDITED FOR MISSING PART FUNCTION

  if damage_on_remove!="missing":                            ##  "missing" part cannot be "replaced"

    "You replace {mark}[part]{/} with {mark}[new_part]{/}."  ##  INDENTED BY SQUIRREL
    ""                                                       ##  INDENTED BY SQUIRREL

  if damage_on_remove=="destroy":
    "You can't remove {mark}[part]{/} without destroying it."
    $part.apply_damage(damage_on_remove,silent=True)

##  LINE EDITED BY SQUIRREL IN VERSION 0.0.4 - new flag for "damage_on_remove" of "missing" added

  elif damage_on_remove and damage_on_remove!="missing":    ##  bypass this if part is "missing"

    "You damaged {mark}[part]{/} during removal."
    $part.apply_damage(damage_on_remove)

##  ADDED BY SQUIRREL IN VERSION 0.0.4 - new flag for "damage_on_remove" of "missing" added

  if damage_on_remove=="missing":                          ##  message for "missing" parts
    "You insert a new part to replace the missing part."

  elif part.is_destroyed:    ##  CHANGED TO elif BY SQUIRREL

    "Original {mark}[part]{/} was damaged beyond repair, so you just {bad}throw it away{/}."
  else:
    "You {good}store{/} original {mark}[part]{/} at workshop inventory."
    $workshop.add_item(part)
    $part.owner=None
  $part_slot=None
  $part=None
  $new_part=None
  choice("end_bot_interaction_part:,tinker") "Continue"
  return

label interact_default_disassemble(bot):
  header "[bot] - Disassemble"
  "You prepare to {bad}disassemble{/} {mark}[bot]{/}."
  ""
  "You will strip {mark}[bot]{/} of any usable parts and sell everything else to a {mark}scrap recycling{/} dealer."
  ""
  "There are valuable materials in the {mark}bot chassis{/}, particularly in higher rated bots."
  ""
  "{bad}Once done, [bot.heshe] can't be reassembled.{/}"
  interact("disassemble_do",cost=[("energy",1)]) "Yes, continue"
  choice("<<<") "No, cancel"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_disassemble_do(bot):
  header "[bot] - Disassemble"
  ## 0.9.n recycle scrap
  "You disassemble {mark}[bot]{/} part by part setting aside the useless parts to be recycled."
  "{size=-16} {/}"
  $recycle_chassis=50*bot.rate_level       ## low value, intentionally not a money maker
  $recycle_parts=0                         ## clear to tally up part value
  python:
    bot.inventory.clear()                  ##  v0.2.1 - 1 line bug fix/workaround for bug in creating bots in scavenge and flea market
    for slot in bot.outfit_slots:
      bot.unequip(slot)
  while bot.inventory:
    $part=bot.inventory.pop(0)
## 0.9.n added filter for irrepairable parts to stop wasting time putting them into inventory
    if not part.has_irrepairable_defects and not part.is_destroyed and part.damage_on_remove!="missing":  ##  added AND clause in 0.2.1 to replace change in 0.0.5
      $workshop.add_item(part)
      $part.owner=None
      "{size=-8}You move {mark}[part]{/} to inventory.{/}"
## 0.9.n recycle scrap
    elif part.damage_on_remove!="missing":              ## get paid for irrepairable or destroyed parts, not missing parts
      $recycle_parts=recycle_parts+2                    ## $2 per part recycled
      "{size=-8}You set aside {mark}[part]{/} for recycling.{/}"
  "{size=-16} {/}"
  "When you're done you find a scrap recycling dealer on the grey net and accept his offer of {mark}$[recycle_chassis]{/} for the chassis and {mark}$[recycle_parts]{/} for the parts. It's not much but it's better than nothing."
  "{size=-16} {/}"
  "A little later a delivery drone arrives and takes everything away and you received the money agreed upon."
  $mc.money=mc.money+recycle_chassis+recycle_parts
  $move_sexbot(bot,None)
  $part=None
  choice("end_bot_interaction") "Continue"
  return