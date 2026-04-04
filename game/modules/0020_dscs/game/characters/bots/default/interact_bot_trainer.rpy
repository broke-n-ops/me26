## set bot trainer skill - must be at least A

## label set_trainer_skill(bot):
label interact_default_set_trainer_skill(bot):
  header "[bot] - Set Trainer Skill Subject"
  $act.start_block("l:300 c:content_width-300")        ## smaller avatar than usual, lots of text!
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
## IMPORTANT!! role requirement is only 'social' so bot can be assigned role without a valid other skill
  if bot.trainer_subject!="":
    "Status: {mark}[bot]'s{/} current trainer skill subject is {mark}[bot.trainer_subject]{/}. A different trainer skill subject can be selected."
  else:
    "Status: {good}[bot]{/} {bad}has not been assigned a trainer subject skill yet.{/} A trainer skill subject can be selected."
  ""  
  "- A {mark}bot trainer{/} must have {mark}at least 'A' level skill{/} in a subject to teach the subject."
  "{size=-20} {/}"
  "- The {mark}bot trainer's{/} skill subject must be the same as the bot {mark}trainee's{/} skill subject."
  "{size=-20} {/}"
  "- The {mark}bot trainer{/} must have a higher skill rating than the bot {mark}trainee{/}."
  "{size=-20} {/}"
  "- A {mark}bot trainer{/} will only train other bots when they are {mark}Stable{/} and have {mark}at least 90%% Integrity{/}."
  "{size=-20} {/}"
  "- A {mark}bot trainer{/} will only train bots that are {mark}Stable{/} and have {mark}at least 75%% Integrity{/}."
  "{size=-20} {/}"

  if bot.bot_combat.level>5 and bot.trainer_subject!="Combat":            ## must be A or S and not already set
    interact("trainer_combat",key="c") "Combat"
  else:
    choice(None) "Combat"
  if bot.bot_electronics.level>5 and bot.trainer_subject!="Electronics":  ## must be A or S and not already set
    interact("trainer_electronics",key="e") "Electronics"
  else:
    choice(None) "Electronics"  
  if bot.bot_mechanics.level>5 and bot.trainer_subject!="Mechanics":      ## must be A or S and not already set
    interact("trainer_mechanics",key="m") "Mechanics"
  else:
    choice(None) "Mechanics" 
  if bot.bot_sex.level>5 and bot.trainer_subject!="Sex":                  ## must be A or S and not already set
    interact("trainer_sex",key="s") "Sex"
  else:
    choice(None) "Sex" 
  choice("end_bot_interaction",pos=16,key="home") "Done"  ## ends bot interaction
  choice("<<<",pos=17,key="cancel") "Back"                                ## goes back to bot interaction
  return

label interact_default_trainer_combat(bot):
  header "[bot] - Bot Trainer Subject"
  $act.start_block("l:300 c:content_width-300")
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "{mark}[bot]{/} will teach other bots the {mark}Combat{/} skill."
  $act.end_block()
  $bot.trainer_subject="Combat"
  choice("<<<",key="c") "Continue"
  return

label interact_default_trainer_electronics(bot):
  header "[bot] - Bot Trainer Subject"
  $act.start_block("l:300 c:content_width-300")
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "{mark}[bot]{/} will teach other bots the {mark}Electronics{/} skill."
  $act.end_block()
  $bot.trainer_subject="Electronics"
  choice("<<<",key="c") "Continue"
  return

label interact_default_trainer_mechanics(bot):
  header "[bot] - Bot Trainer Subject"
  $act.start_block("l:300 c:content_width-300")
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "{mark}[bot]{/} will teach other bots the {mark}Mechanics{/} skill."
  $act.end_block()
  $bot.trainer_subject="Mechanics"
  choice("<<<",key="c") "Continue"
  return

label interact_default_trainer_sex(bot):
  header "[bot] - Bot Trainer Subject"
  $act.start_block("l:300 c:content_width-300")
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "{mark}[bot]{/} will teach other bots the {mark}Sex{/} skill."
  ""
  "Bots assigned to train other bots in sex only train bots of the opposite gender; male {mark}Bot Trainers{/} train only female bots and female {mark}Bot Trainers{/} train only male bots."
  $act.end_block()
  $bot.trainer_subject="Sex"
  choice("<<<",key="c") "Continue"
  return