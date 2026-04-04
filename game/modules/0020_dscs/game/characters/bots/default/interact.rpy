##  Variables for Scrolling Slots  -  section added by squirrel
init python:
  tinker_current_row=0    ##  Used in file 'interact_tinker.rpy'

label interact_default_include_greet(bot):
  "{say}Yes, Master?{/} [bot] looks at you attentively, ready to follow your orders."
  "{size=-14} {/}"
  return

label interact_default(bot):
  $game_bg="home workspace"
  $home["workshop_bot"]=None
  header "[bot]"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [bot.model_id] avatar@400x600}"
  $act.set_block("c")
  if bot.chassis.is_disabled:
    "[bot] has heavily damaged or missing chassis parts and is currently offline."
  else:
    call interact_include("greet")
    if bot.psychocore_stability_decay_mult!=db_psychocore_decay:  ## NOT - this isn't a defective bot
      extend " A scan shows no signs of significant chassis damage or PsychoCore glitches."
    else:                                                         ## defective bot
      extend " A scan shows no signs of significant chassis damage but there are {mark}occasional PsychoCore glitches{/}."
    extend " Energy consumption, CPU load, and network traffic are all normal."
  call interact_default_choices
  $act.end_block()
  return

label interact_default_choices:
  if bot.chassis.is_disabled or not bot.action_allowed("train"):
    if bot.chassis.is_disabled:
      choice(None) "Train"
    else:
      choice(None,hint="{hint}not allowed{/}") "Train"
  else:
    interact("train") "Train"
  if not bot.action_allowed("tinker"):
    choice(None,hint="{hint}not allowed{/}") "Tinker"
  else:
    $tinker_current_row=1                                          ##  Added by squirrel:  This makes sure tinkering always starts with row 1 if there are multiple rows
    interact("tinker") "Tinker"
  if bot.chassis.is_disabled or not bot.action_allowed("hack"):
    if bot.chassis.is_disabled:
      choice(None) "Hack"
    else:
      choice(None,hint="{hint}not allowed{/}") "Hack"
  else:
    interact("hack") "Hack"

  if bot.chassis.is_disabled or not bot.action_allowed("mission"):
    if bot.chassis.is_disabled:
      choice(None,pos=5) "Missions"
    else:
      choice(None,pos=5,hint="{hint}not allowed{/}") "Missions"
  else:
    interact("missions",pos=5,key="m") "Missions"  ## 0.9.n added 'm' key
  python:
    for pos,(role_action,role_action_info) in enumerate(bot.roles_actions()):
      if role_action:
        interact(role_action,pos=pos+6,**role_action_info)(None)
      else:
        choice(role_action,pos=pos+6,**role_action_info)(None)

## 0.12.n moved from button position 4 to button position 9 (4th button on second row)
  if bot.allow_manage:
    interact("set_mission_priority",pos=9,hint="(when managed)",key="p") "Set Priority"
  else:
    choice(None,pos=9,hint="(when managed)") "Set Priority"

## 0.10.2 put in message for bot managers
  if bot.has_role("mission_manager"):
    "{size=-14} {/}"
    "{mark}[bot]{/} will send other bots on other missions as a {mark}Bot Manager{/}." 

## 0.7.n FOR THE 'mission_manager' BOT ROLE
  "{size=-14} {/}"
  if not bot.allow_manage:
    "{mark}[bot] will NOT be managed by other bots.{/}"
## 0.14 insert if...else to prevent 'Business Partner Special Bots' (Frankie and Bride of Frankie) from being managed
    if not bot.has_role("bp_special_bot"):
      interact("bot_toggle_mgr_allow",hint="toggle allow manage",pos=12, key="a") "Manage: No"  ## 0.9.n added 'a' key
    else:
      choice(None,pos=12,hint="(not allowed)") "Manage: No"
  else:
    "{mark}[bot]{/} will be managed by other bots."
## 0.10.2 support selecting mission priority 
    if bot.mgr_priority=="default":
      if bot.gender=="female":
        extend " Mission priority: {mark}Highest Skill Level{/}"
      else:
        extend " Mission priority: {mark}Highest Skill Level{/}"
    elif bot.mgr_priority=="sex":
      if bot.gender=="female":
        extend " Mission priority: {mark}Whore{/}"
      else:
        extend " Mission priority: {mark}Gigolo{/}"
    elif bot.mgr_priority=="tech":
        extend " Mission priority: {mark}Scavenge{/}"
    elif bot.mgr_priority=="combat":
        extend " Mission priority: {mark}UFC Fight{/}"
## 0.10.n end of insertion
## 0.14 insert if...else to prevent 'Business Partner Special Bots' (Frankie and Bride of Frankie) from being managed
    if not bot.has_role("bp_special_bot"):
      interact("bot_toggle_mgr_allow",hint="toggle allow-manage",pos=12, key="a") "Manage: Yes"  ## 0.9.n added 'a' key
    else:
      choice(None,pos=12,hint="(not allowed)") "Manage: No"
## 0.12.n insert buttons to set bot trainer skill subject and bot trainee skill subject
  if bot.has_role("bot_trainer"):
    "{size=-14} {/}"
    if bot.trainer_subject!="":  ## a subject has already been set for this bot
      "{mark}[bot]{/} will train other bots in {mark}[bot.trainer_subject]{/} as a {mark}Bot Trainer{/}." 
    else:                        ## no subject has been selected yet for this bot
      "{good}[bot]{/} {bad}has not been assigned a trainer subject skill yet.{/}"
    interact("set_trainer_skill",pos=10,hint="(trainer role)",key="t") "Set Subject"
  else:
    choice(None, pos=10,hint="(trainer role)") "Set Subject"
  "{size=-14} {/}"
  if bot.trainee_subject=="never":                           ## bot will not be trained
    "{mark}[bot]{/} will not be trained by other bots."
  else:
    "{mark}[bot]{/} may be trained in {mark}[bot.trainee_subject]{/} by other bots."
  interact("set_trainee_skill",pos=11,hint="(when student)",key="t") "Set Subject"
## 0.14 insert if...else to prevent 'Business Partner Special Bots' (Frankie and Bride of Frankie) from being managed
  if not bot.has_role("bp_special_bot"):
    if bot.do_not_sell:
      "{size=-14} {/}"
      "{mark}[bot]{/} is marked {mark}do-not-sell{/}."
      interact("bot_toggle_dns",hint="toggle do-not-sell",pos=13, key="d") "DNS: on"  ## 0.9.n added 'd' key
    else:
      interact("bot_toggle_dns",hint="toggle do-not-sell",pos=13,key="d") "DNS: off"  ## 0.9.n added 'd' key
  else:
    interact(None,pos=13) "DNS"
## end 0.14 change
  if bot.chassis.is_disabled or not bot.action_allowed("rename"):
    if bot.chassis.is_disabled:
      choice(None,pos=14) "Rename"
    else:
      choice(None,pos=14,hint="{hint}not allowed{/}") "Rename"
  else:
    interact("rename",pos=14, key="n") "Rename"  ## 0.9.n added 'n' key
  if bot.chassis.is_disabled:
    choice(None,pos=15,key="r") "Roles"
  else:
    interact("roles",pos=15,key="r") "Roles"
  choice(">>>enter_mode:mode_status:"+bot.id,title="Status",pos=16,key="s") "Status"
  choice("<<<",pos=17,key=("home","cancel")) "Done"
  return

label interact_default_bot_toggle_dns(bot):
  $bot.do_not_sell=not bot.do_not_sell
  return "<<<"

## INSERTED IN 0.7.n FOR THE 'mission_manager' BOT ROLE
label interact_default_bot_toggle_mgr_allow(bot):
  $bot.allow_manage=not bot.allow_manage
  return "<<<"
## END INSERTED