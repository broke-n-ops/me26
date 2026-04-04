init python:
  elec_min=50         ##  Radnor's default min xp is 50
  elec_max=850        ##  Radnor's default max xp is 950 - 0.12.n psychocore influence potential boost so this went down
  elec_mod=25         ##  modifier: at 75% integrity default xp, higher more xp, lower less xp
  elec_actual=0       ##  actual xp modified by integrity

define label_interact_default_train_electronics_action_info={"cost":[("energy",1)]}

label interact_default_train_electronics(bot):
  $skill_name=bot.bot_electronics.name
  header "[bot] - Training: [skill_name]"
  call interact_include("train_electronics_before")
  "You train [bot] in {mark}[skill_name]{/}."
  ""
  if mc.electronics<bot.bot_electronics:
    "You failed to teach [bot] anything, as [bot.heshe] knows more about electronics than you do."
  else:
    "There is some improvement in [bot.posname] electronics skill."
## 0.15.n completed change to actually make integrity and stability matter!!
    $elec_actual=random.randint(elec_min,elec_max)

##    $print "Electronics random number: ",elec_actual

    $elec_actual=int(elec_actual*(bot.chassis.integrity+elec_mod)/100)       ## 0.2.2  integrity added as an influence
    $elec_actual=int(elec_actual*(bot.psychocore.stability+elec_mod)/100)    ## 0.12.n stability added as an influence

##    $print "Electronics actual number: ",elec_actual

    $bot.give_xp("bot_electronics",elec_actual)
  call interact_include("train_electronics_after")
  call random_event("train_electronics")
  if _return=="default":
    ## @@REPEAT_ACTION
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
