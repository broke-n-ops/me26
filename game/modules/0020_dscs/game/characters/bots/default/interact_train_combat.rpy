init python:
  cmbt_min=50         ##  Radnor's default min xp is 50
  cmbt_max=850        ##  Radnor's default max xp is 950 - 0.12.n psychocore influence potential boost so this went down
  cmbt_mod=25         ##  modifier: at 75% integrity default xp, higher more xp, lower less xp
  cmbt_actual=0       ##  actual xp modified by integrity

define label_interact_default_train_combat_action_info={"cost":[("energy",1)]}

label interact_default_train_combat(bot):
  header "[bot] - Training: [bot.bot_combat]"
  call interact_include("train_combat_before")
  "You train [bot] in {mark}[bot.bot_combat]{/}."
  $bot.chassis.apply_damage("training_combat",(3,10))
  ""
  if mc.combat<bot.bot_combat:
    "You failed to teach [bot] anything, as [bot.heshe] is more experienced and versatile in combat than you are. But at least you learned something yourself."
    $mc.give_xp("combat",randint(100,250))
  else:
    "There is some improvement in [bot.posname] combat skill. You learned something too."
    $mc.give_xp("combat",randint(50,150))
    $cmbt_actual=randint(cmbt_min,cmbt_max)  ##  was, 50-950

##    $print "Combat random number: ",cmbt_actual

    $cmbt_actual=int(cmbt_actual*(bot.chassis.integrity+cmbt_mod)/100)       ## 0.2.2  integrity added as an influence
    $cmbt_actual=int(cmbt_actual*(bot.psychocore.stability+cmbt_mod)/100)    ## 0.12.n stability added as an influence

##    $print "Combat actual number: ",cmbt_actual

    $bot.give_xp("bot_combat",cmbt_actual)
  call interact_include("train_combat_after")
  call random_event("train_combat")
  if _return=="default":
    ## @@REPEAT_ACTION
    if show_repeat_action():
      if bot.chassis.is_disabled:
        interact(None,hint="{hint}bot is disabled{/}") "Repeat"
      else:
        interact("^train_combat") "Repeat"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
    choice("end_bot_interaction",pos=16,key="home") "Done"
    choice("<<<",pos=17,key="cancel") "Back"
  return
