## set priority of missions when bot management is active
## copied line from 'bot.rpy'
##     mgr_priority="default"  ## default is highest skill, ties broken by sex>tech>combat, otherwise set priority to "sex", "tech", "combat"

## NOTE: in 0.12.n the messages saying 'greater than 75% stability' were changed to 'Stable' - these are equivalent statements


## label set_mission_priority(bot):
label interact_default_set_mission_priority(bot):
  header "[bot] - Mission Priority When Managed"
  $act.start_block("l:300 c:content_width-300")        ## smaller avatar than usual, lots of text!
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  if bot.gender=="female":
    $sex_role="Whore"
  else:
    $sex_role="Gigolo"
  if bot.mgr_priority=="sex":
    "When {mark}[bot]{/} is managed [bot.hisher] priority mission is {mark}[sex_role]{/} which only occurs at night."
    ""
    "In the morning {mark}[bot]{/} will be sent on a {mark}Scavenge{/} mission if [bot.hisher] {mark}Electronics{/} and {mark}Mechanics{/} skills are both {mark}level C or higher{/}."
    ""
##    "The bot manager {bad}WILL NOT{/} send {mark}[bot]{/} on missions if [bot.hisher] {mark}integrity is less than [sendbot_integrity_min]%%{/} or if [bot.hisher] {mark}stability is less than [sendbot_stability_min]%%{/}."
    "The bot manager {bad}WILL NOT{/} send {mark}[bot]{/} on missions if [bot.hisher] {mark}integrity is less than [sendbot_integrity_min]%%{/} or if [bot.heshe] is {mark}not Stable{/}."    
  elif bot.mgr_priority=="tech":
    "When {mark}[bot]{/} is managed [bot.hisher] priority mission is {mark}Scavenge{/} and [bot.heshe] will be sent as frequently as possible {mark}except at night{/} when [bot.heshe] is being recharged."
    ""
    "When {mark}Scavenge{/} is their priority mission bots are not sent on any other missions."
    ""
##    "The bot manager {bad}WILL NOT{/} send {mark}[bot]{/} on missions if [bot.hisher] {mark}integrity is less than [sendbot_integrity_min]%%{/} or if [bot.hisher] {mark}stability is less than [sendbot_stability_min]%%{/}."
    "The bot manager {bad}WILL NOT{/} send {mark}[bot]{/} on missions if [bot.hisher] {mark}integrity is less than [sendbot_integrity_min]%%{/} or if [bot.heshe] is {mark}not Stable{/}."    
  elif bot.mgr_priority=="combat":
    "When {mark}[bot]{/} is managed [bot.hisher] priority mission is {mark}UFC Fight{/}. Bot Managers always send bots to the correct fight class fights two times a week on the appropriate evenings."
    ""
    "On days when {mark}[bot]'s{/} class is not fighting [bot.heshe] will be sent on other missions if [bot.heshe] is qualified."

    extend " In the morning [bot.heshe] will be sent on a {mark}Scavenge{/} mission if [bot.hisher] {mark}Electronics{/} and {mark}Mechanics{/} skills are both {mark}level C or higher{/}."
    extend " At night if [bot.heshe] will be sent on a {mark}[sex_role]{/} mission if [bot.hisher] {mark}Sex{/} skill is {mark}level C or higher{/}."
    ""
##    "The bot manager {bad}WILL NOT{/} send {mark}[bot]{/} on missions if [bot.hisher] {mark}integrity is less than [sendbot_integrity_min]%%{/} or if [bot.hisher] {mark}stability is less than [sendbot_stability_min]%%{/}."
    "The bot manager {bad}WILL NOT{/} send {mark}[bot]{/} on missions if [bot.hisher] {mark}integrity is less than [sendbot_integrity_min]%%{/} or if [bot.heshe] is {mark}not Stable{/}."    
  else:                            ## must be default
    "When {mark}[bot]{/} is managed missions are based upon [bot.hisher] highest skill level. When skills are equal: {mark}Sex > Tech > Combat{/}. (Tech = lower of Electronics and Mechanics) {good}All missions require level C skill or higher{/}."
    ""
    "{good}Sex:{/} {mark}[sex_role]{/} missions at night, {mark}Scavenge{/} missions in the morning."
    ""
    "{good}Tech:{/} {mark}Scavenge{/} missions {mark}except at night{/} when [bot.heshe] is being recharged. No other missions."
    ""
    "{good}Combat:{/} {mark}UFC Fight{/} missions on the correct evenings {mark}if you can pay the fee{/}. Other days: mornings {mark}Scavenge{/} missions and night {mark}[sex_role]{/} missions."
    ""
##    "The bot manager {bad}WILL NOT{/} send {mark}[bot]{/} on missions if [bot.hisher] {mark}integrity is less than [sendbot_integrity_min]%%{/} or if [bot.hisher] {mark}stability is less than [sendbot_stability_min]%%{/}."
    "The bot manager {bad}WILL NOT{/} send {mark}[bot]{/} on missions if [bot.hisher] {mark}integrity is less than [sendbot_integrity_min]%%{/} or if [bot.heshe] is {mark}not Stable{/}."    
  $act.end_block()
  if bot.mgr_priority=="default":
    choice(None) "Highest Skill"
  else:
    interact("priority_default",key="d") "Highest Skill"
  if bot.mgr_priority=="sex" or bot.bot_sex.level<4:                      ## inactive if set to sex or sex skill < C
    if bot.gender=="female":
      choice(None) "Whore"
    else:
      choice(None) "Gigolo"
  else:
    if bot.gender=="female":
      interact("priority_sex",key="s") "Whore"
    else:
      interact("priority_sex",key="s") "Gigolo"
  $bot_tech_level=min(bot.bot_mechanics.level,bot.bot_electronics.level)  ## TECH level is minimum of electronics and mechanics levels
  if bot.mgr_priority=="tech" or bot_tech_level<4:                        ## inactive if set to tech or tech skill < C
    choice(None) "Scavenge"
  else:
    interact("priority_tech",key="s") "Scavenge"
  if bot.mgr_priority=="combat" or bot.bot_combat.level<4:                ## inactive if set to combat or combat skill < C
    choice(None) "UFC Fight"
  else:
    interact("priority_combat",key="s") "UFC Fight"
  choice("end_bot_interaction",pos=16,key="home") "Done"  ## ends bot interaction
  choice("<<<",pos=17,key="cancel") "Back"                ## goes back to bot interaction
  return

label interact_default_priority_default(bot):
  header "[bot] - Mission Priority When Managed"
  $act.start_block("l:300 c:content_width-300")        ## smaller avatar than usual, lots of text!
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "The priority mission when {mark}[bot]{/} is managed will be based upon [bot.hisher] {mark}Highest Skill{/}."
  $act.end_block()
  $bot.mgr_priority="default"
  choice("<<<",key="c") "Continue"
  return

label interact_default_priority_sex(bot):
  header "[bot] - Mission Priority When Managed"
  $act.start_block("l:300 c:content_width-300")        ## smaller avatar than usual, lots of text!
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  if bot.gender=="female":
    $sex_role="Whore"
  else:
    $sex_role="Gigolo"
  "The priority mission priority when {mark}[bot]{/} is managed will be {mark}[sex_role]{/}."
  $act.end_block()
  $bot.mgr_priority="sex"
  choice("<<<",key="c") "Continue"
  return

label interact_default_priority_tech(bot):
  header "[bot] - Mission Priority When Managed"
  $act.start_block("l:300 c:content_width-300")        ## smaller avatar than usual, lots of text!
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "The priority mission priority when {mark}[bot]{/} is managed will be {mark}Scavenge{/}."
  $act.end_block()
  $bot.mgr_priority="tech"
  choice("<<<",key="c") "Continue"
  return

label interact_default_priority_combat(bot):
  header "[bot] - Mission Priority When Managed"
  $act.start_block("l:300 c:content_width-300")        ## smaller avatar than usual, lots of text!
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "The priority mission priority when {mark}[bot]{/} is managed will be {mark}UFC Fight{/}."
  $act.end_block()
  $bot.mgr_priority="combat"
  choice("<<<",key="c") "Continue"
  return