##========Random Events========

init python:
  train_social_bot=[]              ##  need to store bot to enable multiple functions to use it

init python hide:
  @random_event("train_social")
  def train_social_none():         ##  this is the chance of 'no event'
    return None,75

  @random_event("train_social")
  def train_social_psychocore():
    return "train_social_stability_check",25
##    return "train_social_stability_check",9999  ##  replace the line above with this line during testing

##========Supporting Functions========

label train_social_stability_check():
  $train_social_bot=bot
  $trigger_event=randint(1,74)          ##  trigger value always below minimum stable bot value

##  $trigger_event=99                               ##  these 4 lines are for testing only
##  ""
##  "trigger_event: [trigger_event]"
##  "bot.psychocore.stability: [bot.psychocore.stability]"

  if bot.psychocore.stability<=trigger_event:
    choice("train_social_stability_event") "Continue"
  else:

##  Below is an exact copy of what normally happens at the end of 'train_social'
    if show_repeat_action():
      if bot.chassis.is_disabled:
        interact(None,hint="{hint}bot is disabled{/}") "Repeat"
      else:
        interact("^train_social") "Repeat"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
    choice("end_bot_interaction",pos=16,key="home") "Done"
    choice("<<<",pos=17,key="cancel") "Back"
  return

label train_social_stability_event():
  header "[train_social_bot] - Training: Social"
  if mc.energy>0:
    "Unfortunately {mark}[train_social_bot]{/} wasn't stable and went a little crazy during training. You wasted time getting [train_social_bot.himher] back under control and [train_social_bot.heshe] lost a little of [train_social_bot.hisher] social skill."
    ""
    "You should probably stabilize [train_social_bot.himher] before giving [train_social_bot.himher] any more training."
    ""
    $mc.energy-=1
    "{bad} Lost 1 AP!{/}"
    $train_social_bot.give_xp("bot_social",randint(-25,-2))
    $mc.mood.give_xp(randint(-100,-50))
  else:
    "Unfortunately {mark}[train_social_bot]{/} wasn't stable and went a little crazy during training. Since you were a little tired when training started it was difficult to get [train_social_bot.himher] back under control. As a result [train_social_bot.heshe] lost a significant part of [train_social_bot.hisher] social skill."
    ""
    "You should probably stabilize [train_social_bot.himher] before giving [train_social_bot.himher] any more training."
    ""
    $train_social_bot.give_xp("bot_social",randint(-49,-26))
    $mc.mood.give_xp(randint(-200,-100))
##  Below is an exact copy of what normally happens at the end of 'train_social'
  $bot=train_social_bot
  if show_repeat_action():
    if bot.chassis.is_disabled:
      interact(None,hint="{hint}bot is disabled{/}") "Repeat"
    else:
      interact("^train_social") "Repeat"
    choice("<<<") "Back"
  else:
    choice("<<<") "Continue"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return