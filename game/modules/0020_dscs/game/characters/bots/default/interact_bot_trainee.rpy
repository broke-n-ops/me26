## set bot trainee skill - can be turned off with value set to "never"

## label set_trainee_skill(bot):
label interact_default_set_trainee_skill(bot):
  header "[bot] - Set Trainee Skill Subject"
  $act.start_block("l:300 c:content_width-300")        ## smaller avatar than usual, lots of text!
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
## bots can only be trained in one subject at a time or can be set to not be taught
## 0.14 insert 6 lines, Frankie and Bride cannot be trained by other bots for their safety
  if bot.model_id=="frankie_bot" or bot.model_id=="frankie_bride_bot":
    ""
    "You decide that you will not allow your bots assigned the {mark}bot trainer role{/} to train {mark}[bot]{/}. These special bots are too valuable to risk having something go wrong if they interact with your other bots."
    choice("end_bot_interaction",pos=16,key="home") "Done"          ## ends bot interaction
    choice("<<<",pos=17,key="cancel") "Back"                        ## goes back to bot interaction
    return
## 0.14 end if insertion, change next clause from 'if' to 'elif'
  elif bot.trainee_subject!="never":
    "Status: {mark}[bot]'s{/} current trainee skill subject is {mark}[bot.trainee_subject]{/}. A different trainee skill subject can be chosen or training by other bots can be turned off."
  else:
    "Status: {mark}[bot]{/} has training by other bots turned {mark}off{/}. To turn training by other bots on select which skill will be the bot's trainee skill subject."
  ""
  "- A bot can only be trained by other bots when they already have {mark}at least an 'F' level skill{/} in the subject."
  "{size=-20} {/}"
  "- The {mark}bot trainee's skill subject{/} must be the same as the bot {mark}bot trainer's skill subject{/}."
  "{size=-20} {/}"
  "- The {mark}bot trainer{/} must have higher skill rating than the {mark}bot trainee{/}."
  "{size=-20} {/}"
  "- A bot can only be trained by other bots when they are {mark}Stable{/} and have {mark}at least 75%% Integrity{/}."
  "{size=-20} {/}"
  
  python:
    this_bots_skills=bot.stats_order
    if "bot_combat" in this_bots_skills:
      bot_has_combat=1
    else:
      bot_has_combat=0
    if "bot_electronics" in this_bots_skills:
      bot_has_electronics=1
    else:
      bot_has_electronics=0
    if "bot_mechanics" in this_bots_skills:
      bot_has_mechanics=1
    else:
      bot_has_mechanics=0
    if "bot_sex" in this_bots_skills:
      bot_has_sex=1
    else:
      bot_has_sex=0

  if bot_has_combat and bot.trainee_subject!="Combat":            ## must have the skill already
    interact("trainee_combat",key="c") "Combat"
  else:
    choice(None) "Combat"
  if bot_has_electronics and bot.trainee_subject!="Electronics":  ## must have the skill already
    interact("trainee_electronics",key="e") "Electronics"
  else:
    choice(None) "Electronics"  
  if bot_has_mechanics and bot.trainee_subject!="Mechanics":      ## must have the skill already
    interact("trainee_mechanics",key="m") "Mechanics"
  else:
    choice(None) "Mechanics" 
  if bot_has_sex and bot.trainee_subject!="Sex":                  ## must have the skill already
    interact("trainee_sex",key="s") "Sex"
  else:
    choice(None) "Sex"
  if bot.trainee_subject!="never":                                ## only grey if already off (actual value is 'never')
    interact("trainee_never",key="n") "Off"
  else:
    choice(None) "Off"
  choice("end_bot_interaction",pos=16,key="home") "Done"          ## ends bot interaction
  choice("<<<",pos=17,key="cancel") "Back"                        ## goes back to bot interaction
  return

label interact_default_trainee_combat(bot):
  header "[bot] - Bot Trainee Subject"
  $act.start_block("l:300 c:content_width-300")
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "{mark}[bot]{/} may be trained by other bots assigned the {mark}Bot Trainer{/} role in the {mark}Combat{/} skill."
  $act.end_block()
  $bot.trainee_subject="Combat"
  choice("<<<",key="c") "Continue"
  return

label interact_default_trainee_electronics(bot):
  header "[bot] - Bot Trainee Subject"
  $act.start_block("l:300 c:content_width-300")
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "{mark}[bot]{/} may be trained by other bots assigned the {mark}Bot Trainer{/} role in the {mark}Electronics{/} skill."
  $act.end_block()
  $bot.trainee_subject="Electronics"
  choice("<<<",key="c") "Continue"
  return

label interact_default_trainee_mechanics(bot):
  header "[bot] - Bot Trainer Subject"
  $act.start_block("l:300 c:content_width-300")
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "{mark}[bot]{/} may be trained by other bots assigned the {mark}Bot Trainer{/} role in the {mark}Mechanics{/} skill."
  $act.end_block()
  $bot.trainee_subject="Mechanics"
  choice("<<<",key="c") "Continue"
  return

label interact_default_trainee_sex(bot):
  header "[bot] - Bot Trainer Subject"
  $act.start_block("l:300 c:content_width-300")
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "{mark}[bot]{/} may be trained by other bots assigned the {mark}Bot Trainer{/} role in the {mark}Sex{/} skill."
  $act.end_block()
  $bot.trainee_subject="Sex"
  choice("<<<",key="c") "Continue"
  return

label interact_default_trainee_never(bot):
  header "[bot] - Bot Trainee Subject"
  $act.start_block("l:300 c:content_width-300")
  center "{image=bots [bot.model_id] avatar@260x600}"
  $act.set_block("c")
  "{mark}[bot]{/} will not be trained by other bots."
  $act.end_block()
  $bot.trainee_subject="never"
  choice("<<<",key="c") "Continue"
  return