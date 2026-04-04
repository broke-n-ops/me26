init python:
  mech_min=50         ##  Radnor's default min xp is 50
  mech_max=850        ##  Radnor's default max xp is 950 - 0.12.n psychocore influence potential boost so this went down
  mech_mod=25         ##  modifier: at 75% integrity default xp, higher more xp, lower less xp
  mech_actual=0       ##  actual xp modified by integrity

define label_interact_default_train_mechanics_action_info={"cost":[("energy",1)]}

label interact_default_train_mechanics(bot):
  $skill_name=bot.bot_mechanics.name
  header "[bot] - Training: [skill_name]"
  call interact_include("train_mechanics_before")
  "You train [bot] in {mark}[skill_name]{/}."
  ""
  if mc.mechanics<bot.bot_mechanics:
    "You failed to teach [bot] anything, as [bot.heshe] knows more about mechanics than you do."
  else:
    "There is some improvement in [bot.posname] mechanics skill."
## 0.15.n completed change to actually make integrity and stability matter!!
    $mech_actual=random.randint(mech_min,mech_max)

##    $print "Mechanics random number: ",mech_actual

    $mech_actual=int(mech_actual*(bot.chassis.integrity+mech_mod)/100)       ## 0.2.2  integrity added as an influence
    $mech_actual=int(mech_actual*(bot.psychocore.stability+mech_mod)/100)    ## 0.12.n stability added as an influence

##    $print "Mechanics actual number: ",mech_actual

    $bot.give_xp("bot_mechanics",mech_actual)
  call interact_include("train_mechanics_after")
  call random_event("train_mechanics")
  if _return=="default":
    ## @@REPEAT_ACTION
    if show_repeat_action():
      if bot.chassis.is_disabled:
        interact(None,hint="{hint}bot is disabled{/}") "Repeat"
      else:
        interact("^train_mechanics") "Repeat"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
    choice("end_bot_interaction",pos=16,key="home") "Done"
    choice("<<<",pos=17,key="cancel") "Back"
  return
