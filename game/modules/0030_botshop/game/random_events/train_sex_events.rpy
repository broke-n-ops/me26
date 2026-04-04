##========Random Events========

init python:
  train_sex_bot=[]              ##  need to store bot to enable multiple functions to use it

init python hide:
  @random_event("train_sex")
  def train_sex_none():         ##  this is the chance of 'no event'
    return None,75

  @random_event("train_sex")
  def train_sex_psychocore():
    return "train_sex_stability_check",25
##    return "train_sex_stability_check",9999  ##  replace the line above with this line during testing

##========Supporting Functions========

label train_sex_stability_check():
  $train_sex_bot=bot
  $trigger_event=randint(1,74)          ##  trigger value always below minimum stable bot value

##  $trigger_event=99                               ##  these 4 lines are for testing only
##  ""
##  "trigger_event: [trigger_event]"
##  "bot.psychocore.stability: [bot.psychocore.stability]"

  if bot.psychocore.stability<=trigger_event:
    choice("train_sex_stability_event") "Continue"
  else:

##  Below is an exact copy of what normally happens at the end of 'train_sex'
    if show_repeat_action():
      if bot.chassis.is_disabled:
        interact(None,hint="{hint}bot is disabled{/}") "Repeat"
      else:
        interact("^train_sex") "Repeat"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
    choice("end_bot_interaction",pos=16,key="home") "Done"
    choice("<<<",pos=17,key="cancel") "Back"
  return
  
label train_sex_stability_event():
  header "[train_sex_bot] - Training: Sex"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image=find_game_image_variant("bots [train_sex_bot.model_id] :sex")
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  if mc.energy>0:
    "Unfortunately {mark}[train_sex_bot]{/} wasn't stable and went a little crazy during training. You wasted time and suffered minor injuries getting [train_sex_bot.himher] back under control. In addition, [train_sex_bot.heshe] lost a little of [train_sex_bot.hisher] sex skill."
    ""
    "You should probably stabilize [train_sex_bot.himher] before giving [train_sex_bot.himher] any more training."
    ""
    $mc.energy-=1
    "{bad} Lost 1 AP!{/}"
    $mc.give_xp("strength",randint(-300,-200))
    $mc.give_xp("stamina",randint(-300,-200))
    $train_sex_bot.give_xp("bot_sex",randint(-25,-2))
    $mc.mood.give_xp(randint(-100,-50))
  else:
    "Unfortunately {mark}[train_sex_bot]{/} wasn't stable and went a little crazy during training. You were a little tired when training started so you suffered significant injuries getting [train_sex_bot.himher] back under control and [train_sex_bot.heshe] lost a significant portion of [train_sex_bot.hisher] sex skill."
    ""
    "You should probably stabilize [train_sex_bot.himher] before giving [train_sex_bot.himher] any more training."
    ""
    $mc.give_xp("strength",randint(-1000,-500))
    $mc.give_xp("stamina",randint(-1000,-500))
    $train_sex_bot.give_xp("bot_sex",randint(-49,-26))
    $mc.mood.give_xp(randint(-200,-100))
##  Below is an exact copy of what normally happens at the end of 'train_sex'
  $bot=train_sex_bot
  if show_repeat_action():
    if bot.chassis.is_disabled:
      interact(None,hint="{hint}bot is disabled{/}") "Repeat"
    else:
      interact("^train_sex") "Repeat"
    choice("<<<") "Back"
  else:
    choice("<<<") "Continue"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return