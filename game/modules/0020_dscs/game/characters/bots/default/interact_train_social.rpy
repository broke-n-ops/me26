init python:
  social_min=50         ##  Radnor's default min xp is 50
  social_max=850        ##  Radnor's default max xp is 950 - 0.12.n psychocore influence potential boost so this went down
  social_mod=25         ##  modifier: at 75% integrity default xp, higher more xp, lower less xp
  social_actual=0       ##  actual xp modified by integrity

define label_interact_default_train_social_action_info={"cost":[("energy",1)]}

label interact_default_train_social(bot):
  $skill_name=bot.bot_social.name
  header "[bot] - Training: [skill_name]"
  call interact_include("train_social_before")
  "You train [bot] in {mark}[skill_name]{/}."
  ""
  if mc.social<bot.bot_social:
    "You failed to teach [bot] anything, as [bot.heshe] understands more about social interactions than you do. This is actually quite sad."
  else:
    "There is some improvement in [bot.posname] social skill."

## 0.15.n BUG FIXED - the effect of integrity and stability was not done correctly
    $social_actual=randint(social_min,social_max)  ##  was, 50-950

##    $print "Social random number: ",social_actual

    $social_actual=int(social_actual*(bot.chassis.integrity+social_mod)/100)       ## 0.2.2  integrity added as an influence
    $social_actual=int(social_actual*(bot.psychocore.stability+social_mod)/100)    ## 0.12.n stability added as an influence

##    $print "Social actual number: ",social_actual

    $bot.give_xp("bot_social",social_actual)
  call interact_include("train_social_after")
  call random_event("train_social")
  if _return=="default":
    ## @@REPEAT_ACTION
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
