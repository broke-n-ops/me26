# # ====================INIT VARIABLES

init python:
  ps_imagenumber=0    ##  create a new variable for this mod, not sure if I could use the other one

label ps_wrong_shop(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(1,4)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  pornshop entrance pic
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "{mark}[bot]{/} went to a {bad}pornshop{/} instead of a {bad}pawnshop{/}! I think {mark}[bot]{/} needs better {mark}social skills{/}!"
  ""
  return

label ps_frigid_bot(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(5,6)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  missionary with clumsyness and bored owner
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "After a short time he stopped, {bad}stole her money{/}, and said; {say}'Get out of here you frigid bot, I'd rather jerk off!'{/} Maybe {mark}[bot]{/} needs better {mark}sex skills{/}."
  ""
  return

label ps_no_sex(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(7,8)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  pawnshop owner doesn't want sex, no damage
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "This was a surprise, maybe he's gay. {mark}[bot]{/} came home with some parts:"
  ""
  return

label ps_doggy_sex(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(9,10)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  doggy style, skin & genitals damage
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "{mark}[bot]{/} let the guy have a good time and, after a little wear and tear, came home with some parts:"
  ""
  return

label ps_cowgirl_sex(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(11,12)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  cowgirl, skin & genitals damage
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "{mark}[bot]{/} showed the guy a good time and, after a little wear and tear, came home with some parts:"
  ""
  return

label ps_blowjob_sex(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(13,14)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  blowjob, no damage
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "{mark}[bot]{/} got a mouthful from the guy and came home with some parts:"
  ""
  return

label ps_titfuck_sex(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(15,16)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  titfuck, skin only damage
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "After getting a little skin wear on her tits {mark}[bot]{/} came home with some parts:"
  ""
  return

label ps_handjob_sex(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(17,18)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  handjob, no damage
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "Nice, no damage to repair this time and {mark}[bot]{/} came home with some parts:"
  ""
  return

label ps_anal_sex(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(19,20)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  anal, heavier skin & genitals damage
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "Pervert didn't last long! {mark}[bot]{/} will need a little repair but she came home with some parts:"
  ""
  return

label ps_spank_bot_sex(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(21,22)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  spank bot, very heavy skin damage
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "The asshole really beat her ass hard! {mark}[bot]{/} will need repair but she came home with some parts:"
  ""
  return

label ps_spank_owner_sex(bot):
##  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $ps_imagenumber=random.randint(23,24)
  $action_image="missions pawnshop ps_"+str(ps_imagenumber)  ##  spank owner, no damage
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""
  "I'm glad {mark}[bot]{/} was smart enough not to hurt the pervert and she came home with some parts:"
  ""
  return