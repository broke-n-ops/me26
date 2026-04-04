##========Random Events========

init python:
  train_electronics_bot=[]              ##  need to store bot to enable multiple functions to use it

init python hide:
  @random_event("train_electronics")
  def train_electronics_none():         ##  this is the chance of 'no event'
    return None,75

  @random_event("train_electronics")
  def train_electronics_psychocore():
    return "train_electronics_stability_check",25
##    return "train_electronics_stability_check",9999  ##  replace the line above with this line during testing

##========Supporting Functions========

label train_electronics_stability_check():
  $train_electronics_bot=bot
  $trigger_event=randint(1,74)          ##  trigger value always below minimum stable bot value

##  $trigger_event=99                               ##  these 4 lines are for testing only
##  ""
##  "trigger_event: [trigger_event]"
##  "bot.psychocore.stability: [bot.psychocore.stability]"

  if bot.psychocore.stability<=trigger_event:
    choice("train_electronics_stability_event") "Continue"
  else:

##  Below is an exact copy of what normally happens at the end of 'train_electronics'
    if show_repeat_action():
      if bot.chassis.is_disabled:
        interact(None,hint="{hint}bot is disabled{/}") "Repeat"
      else:
        interact("^train_electronics") "Repeat"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
    choice("end_bot_interaction",pos=16,key="home") "Done"
    choice("<<<",pos=17,key="cancel") "Back"
  return

label train_electronics_stability_event():
  header "[train_electronics_bot] - Training: Electronics"
  if mc.energy>0:
    "Unfortunately {mark}[train_electronics_bot]{/} wasn't stable and went a little crazy during training. You wasted time getting [train_electronics_bot.himher] back under control and [train_electronics_bot.heshe] lost a little of [train_electronics_bot.hisher] electronics skill."
    ""
    "You should probably stabilize [train_electronics_bot.himher] before giving [train_electronics_bot.himher] any more training."
    ""
    $mc.energy-=1
    "{bad} Lost 1 AP!{/}"
    $train_electronics_bot.give_xp("bot_electronics",randint(-25,-2))
    $mc.mood.give_xp(randint(-100,-50))
  else:
    "Unfortunately {mark}[train_electronics_bot]{/} wasn't stable and went a little crazy during training. Since you were a little tired when training started it was difficult to get [train_electronics_bot.himher] back under control. As a result [train_electronics_bot.heshe] lost a significant portion of [train_electronics_bot.hisher] electronics skill."
    ""
    "You should probably stabilize [train_electronics_bot.himher] before giving [train_electronics_bot.himher] any more training."
    ""
    $train_electronics_bot.give_xp("bot_electronics",randint(-49,-26))
    $mc.mood.give_xp(randint(-200,-100))
##  Below is an exact copy of what normally happens at the end of 'train_electronics'
  $bot=train_electronics_bot
  if show_repeat_action():
    if bot.chassis.is_disabled:
      interact(None,hint="{hint}bot is disabled{/}") "Repeat"
    else:
      interact("^train_electronics") "Repeat"
    choice("<<<") "Back"
  else:
    choice("<<<") "Continue"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return