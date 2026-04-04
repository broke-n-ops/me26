## 0.10.n variable for defective bot hints/disclosures
init python:
  db_disclosure_chance=-25          ## compare to random number for displaying disclosure, starts negative so you won't get the disclosure too quickly
  db_disclosure_cap=70              ## cap on disclosure chance
  db_disclosure_shown=0             ## flag for 1st disclosure

label interact_default_include_hack_attach_bot(bot):
  if home["workshop_bot"]==bot.id:  ## This is shown after completing an action within 'Hack'
    "{mark}[bot]{/} lies on the gurney with the scanner under the robotic arm. The scanner shows the status of [bot.hisher] {mark}PsychoCore and processor activity{/}."
  else:
    if bot.chassis.is_disabled:     ## NOTE: When a bot is disabled the 'Hack' button is inactive, this cannot happen
      "You place disabled {mark}[bot]{/} on the gurney with the scanner underneath the robotic arm. You set the scanner to show the status of [bot.hisher] {mark}PsychoCore and processor activity{/}."
    else:                           ## This is shown when you click on 'Hack' with a normal bot
      "You tell {mark}[bot]{/} to to lie on the gurney with the scanner underneath the robotoc arm. You set the scanner to show the status of [bot.hisher] {mark}PsychoCore and processor activity{/}."
  $home["workshop_bot"]=bot.id
  ""
  return

label interact_default_hack(bot):
  header "[workshop] - [bot]"
  call interact_include("hack_attach_bot")
  "You scan [bot.posname] neural networks for dead loops and irregularities. Combined with activity logs and energy consumption spikes, it gives you a more or less clear picture."
  ""
  "PsychoCore stability: {mark}[bot.psychocore.stability]%%{/}, [bot.psychocore.status_str]."
  if bot.psychocore.stability!=100:
    interact("hack_stabilize",cost=[("energy",1)]) "Stabilize"
  else:
    choice(None,hint="{hint}already stable{/}") "Stabilize"
  $traits=[trait for trait in bot.psychocore.traits if not trait.hidden]
  if traits:
    extend " You found some irregularities."
  else:
    extend " You found no PsychoCore quirks."
  ""
  if traits:
    $act.add_screen("workshop_quirks_info",bot.id)
    if bot.action_allowed("remove_quirk"):
      interact("remove_quirks,0") "Remove Quirks"
    else:
      choice(None,hint="{hint}not allowed{/}") "Remove Quirks"
  else:
    choice(None) "Remove Quirks"
  if not bot.action_allowed("wipe_psychocore"):
    choice(None,pos=12,hint="{hint}not allowed{/}") "Wipe PsychoCore"
  else:
    interact("wipe_psychocore",pos=12) "Wipe PsychoCore"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_hack_stabilize(bot):
  header "[bot] - Stabilizing PsychoCore"
  python:
    progress=mc.calc_stability_progress(bot)
    progress=min(100,bot.psychocore.stability+progress)-bot.psychocore.stability
    base_xp_reward=progress
    skill_xp_reward=int(base_xp_reward*2)
  "You run defragmentation tools, manually remove neural dead loops, and run diagnostics over and over. Eventually, you managed to improve [bot.posname] PsychoCore stability by {mark}[progress]%%{/}."
  $bot.psychocore.stability+=progress
  "Current stability is {mark}[bot.psychocore.stability]%%{/}."
  python:
    mc.give_xp("computers",skill_xp_reward)
    mc.give_xp("expertise_"+bot.model_id,base_xp_reward)

## 0.15.1 moved and modifed hints/disclosures to stabilize function for defective bot feature

## some day consider tweaking this based upon game difficulty level
      
  $global db_psychocore_decay
  $global db_disclosure_chance
  $global db_disclosure_cap
  $global db_disclosure_shown
  if bot.psychocore_stability_decay_mult==db_psychocore_decay:  ## this identifies the bot as defective
##    $print "IDENTIFIED DEFECTIVE BOT"
    if db_disclosure_shown:                                     ## if you have already seen the defective bot disclosure it shows up every time
      ""
      "{bad}You notice that the bot's Psychocore readings are glitching.{/}"
      ""
      "{mcsay}I've seen this before, a bot with a damaged Psychocore. What should I do with it?{/}"
    else:                                                       ## you have not seen the defective bot disclosure yet
      $temp_chance=random.randint(1,100)
      if temp_chance<db_disclosure_chance:                      ## you see the defective bot disclosure for the first time
        $db_disclosure_shown=1                                  ## set flag to show the disclosure every time from now on
        ""
        "You notice that the {mark}Psychocore{/} readings are {bad}glitching{/} and you decide to spend some time investigating the glitches."
        ""
        "{mcsay}Wow, this bot's Psychocore is badly damaged and unfortunately there is no way to fix a Psychocore. I'm not sure I should use this bot myself and if I sell the bot it could hurt my reputation and my business. What should I do with it?{/}"
        $quests.start_quest("defective_bots")
      elif temp_chance<=50:                                     ## show a hint about defective bot 50% of the time
        ""
        "When you check the scanner you notice strange {mark}Psychocore{/} readings, it seems to be glitching occasionally."
      $db_disclosure_chance+=mc.computers.level                ## always increase chance of getting disclosure
      if db_disclosure_chance>db_disclosure_cap:
        $db_disclosure_chance=db_disclosure_cap

## 0.15.1 end of insertion

  ## @@REPEAT_ACTION
  if show_repeat_action:
    if bot.psychocore.stability!=100:
      interact("^hack_stabilize",cost=[("energy",1)]) "Repeat"
    else:
      choice(None,hint="{hint}already stable{/}") "Repeat"
    choice("<<<") "Back"
  else:
    choice("<<<") "Continue"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

define workshop_bot_quirks_per_page=6

init python:
  def prepare_bot_quirks(bot,page=None,per_page=None):
    bot=find_character(bot)
    page=int(page or 0)
    traits=[trait for trait in bot.psychocore.traits if not trait.hidden]
    if per_page is None:
      per_page=len(traits)
    if len(traits)<=page*per_page:
      page=max(0,page-1)
    page_traits=traits[page*per_page:(page+1)*per_page]
    total_pages=max(1,(len(traits)+(per_page-1))//per_page)
    if total_pages>1:
      prev=(page-1)%total_pages
      next=(page+1)%total_pages
    else:
      prev=None
      next=None
    return page,page_traits,total_pages,prev,next

label interact_default_remove_quirks(bot,page):
  header "[bot] - Removing Quirks"
  python:
    page,page_traits,total_pages,prev_page,next_page=prepare_bot_quirks(bot,page,workshop_bot_quirks_per_page)
    page_str="Page {mark}#"+str(page+1)+"{/} of "+str(total_pages)
  center "[page_str]"
  ""
  "While it is common knowledge that you can't directly edit PsychoCore paths, you can lessen or even completely remove PsychoCore quirks by using certain neuroprogramming tricks and obscure tools."
  ""
  if not page_traits:
    "There are no PsychoCore quirks."
  $act.add_screen("workshop_quirks_info",bot,page,True)
  $trait_n=0
  while page_traits:
    $trait=page_traits.pop(0)
    $trait_n+=1
    if trait.inherent:
      choice(None,hint="{hint}inherent{/}") "[trait]"
    elif trait.automatic:
      choice(None,hint="{hint}automatic{/}") "[trait]"
    else:
      interact("remove_quirk,"+str(bot.psychocore.traits.index(trait)),cost=[("energy",1)]) "[trait]"
    $trait=None
  if prev_page is None:
    choice(None,pos=12,key="z") "Prev Page"
  else:
    interact("^remove_quirks,"+str(prev_page),pos=12,key="z") "Prev Page"
  if next_page is None:
    choice(None,pos=13,key="x") "Next Page"
  else:
    interact("^remove_quirks,"+str(next_page),pos=13,key="x") "Next Page"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_remove_quirk(bot,trait_n):
  header "[bot] - Removing Quirk"
  $trait=bot.psychocore.traits[int(trait_n)]
  python:
    progress=mc.calc_pscychocore_quirk_progress(bot,trait)
    progress=abs(max(-100,trait.progress-progress)-trait.progress)
    trait_progress=trait.progress-progress
    base_xp_reward=int(progress*trait.difficulty)
    skill_xp_reward=int(base_xp_reward*2)
  "After quick probing, you managed to locate the most active neural blocks associated with {[trait.trait_color]}[trait]{/}."
  "You manually re-route related neural loops, add temporary conditions and watchdogs, and start \"touching\" the same associative elements over and over until the feedback gets weaker."
  ""
  "Eventually, you managed to lower {[trait.trait_color]}[trait]{/} level by {mark}[progress]{/}."
  "Current level is {mark}[trait_progress]{/}."
  $trait.evolve(-progress)
  $trait_changed=not bot.psychocore.has_trait(trait)
  python hide:
    skills=[(getattr(mc,skill).level,weight) for skill,weight in trait.repair_skills]
    total_weight=sum((weight for level,weight in skills))
    for skill,weight in trait.repair_skills:
      mc.give_xp(skill,skill_xp_reward*weight//total_weight)
    mc.give_xp("expertise_"+bot.model_id,base_xp_reward)
  ## @@REPEAT_ACTION
  if show_repeat_action():
    if trait_changed:
      choice(None,cost=[("energy",1)]) "Repeat"
    else:
      interact("^remove_quirk,"+trait_n,cost=[("energy",1)]) "Repeat"
    choice("<<<") "Back"
  else:
    choice("<<<") "Continue"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_wipe_psychocore(bot):
  header "[bot] - Wipe PsychoCore"
  "You prepare to {bad}completely wipe{/} {mark}[bot.posname]{/} PsychoCore."
  ""
  "This will return {mark}[bot]{/} to factory settings, removing any acquired skills, traits, and quirks. This is an {bad}irreversible{/} process."
  interact("wipe_psychocore_do",cost=[("energy",1)]) "Yes, continue"
  choice("<<<") "No, cancel"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_wipe_psychocore_do(bot):
  header "[bot] - Wipe PsychoCore"
  "You completely wipe {mark}[bot.posname]{/} PsychoCore."
  python hide:
    for role in bot.roles[:]:
      bot.remove_role(role)
    for trait in bot.psychocore.traits[:]:
      trait.reset()
    for stat in bot.stats_order[:]:
      if stat!="autonomy":
        bot.unlearn_stat(stat)
    bot.autonomy=0
    bot.psychocore.stability=100
## 0.10.n reset management priority to default
    bot.mgr_priority="default"
  choice("end_bot_interaction_part:,hack") "Continue"
  return
