define sr_last_time=0    ##  flag for alternating relax from couch to bar

define label_robosechs_relax_action_info={"cost": [("energy",1)]}

label robosechs_relax:
  header "[robosechs] - Relax"
  if sr_last_time==0:    ##  either first time or last time was "1"
    $sr_last_time=1
    $action_image="squirrel botshop sq_8"
    center "{image=[action_image]@800x600}"
    "You ask one of the bot waitresses to get you a drink and then find a seat near the dancing bots. After a few minutes you strike up a conversation with a guy already sitting there. Surprisingly you enjoy the conversation just as much as the dancing sexbots, maybe life isn't so bad!"
    $mc.mood.give_xp(randint(35,75))
    $mc.give_xp("social",randint(40,160))
  else:                  ##  must be "1", last time was "0"
    $sr_last_time=0
    $action_image="squirrel botshop sq_9"
    center "{image=[action_image]@800x600}"
    "You take a seat at the bar and order a drink. The guy sitting at the bar ignores you but at least the one human bartender pretends to enjoy your company. The mix of loud music, flashy visuals, and dancing sexbots melts your brain enough to purge troubling thoughts. At least for now."
    $mc.mood.give_xp(randint(20,50))
    $mc.give_xp("social",randint(20,80))
  call random_event("robosechs_relax")
  if _return=="default":
    ## @@REPEAT_ACTION
    if show_repeat_action():
      choice("robosechs_relax") "Relax longer"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
    choice("<<<",pos=17,key="cancel") "Back"
  return
