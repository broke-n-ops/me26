##  Functions start with bot avatar on left and "result_text" from mission on right 
##  Output entered will be on right below "result_text"


label scavenge_bot_mission_entry_fail(bot):  ## Bot didn't enter dump, hack and chase pictures
  if bot.gender=="female":
    $ps_imagenumber=random.randint(31,39)    ## number picks outfit
  else:
    $ps_imagenumber=random.randint(64,66)    ## male bot
  "{mark}[bot]{/mark} hacked the door to get inside the dump."
  $action_image="missions scavenge scb_"+str(ps_imagenumber)
  center "{image=[action_image]@340x510}"
  if ps_imagenumber<=33:                     ## outfit 1
    $ps_imagenumber=49
  elif ps_imagenumber<=36:                   ## outfit 2
    $ps_imagenumber=50
  elif ps_imagenumber<=39:                   ## outfit 3
    $ps_imagenumber=51
  else:                                      ## male bot
    $ps_imagenumber=random.randint(70,72)
  "Unfortunately [bot.heshe] was seen trying to get in and had to make a run for it. At least [bot.heshe] didn't get caught."
  $action_image="missions scavenge scb_"+str(ps_imagenumber)
  center "{image=[action_image]@340x510}"
  return

label scavenge_bot_mission_search_fail(bot):        ## Bot found nothing
  if bot.bot_sex.level>=4 and bot.bot_electronics.level<bot.bot_sex.level:  ## oral sex entry (C or better and > electronics)
    if bot.gender=="female":
      $ps_imagenumber=random.randint(40,48)         ## number picks outfit
    else:
      $ps_imagenumber=random.randint(67,69)         ## male bot
    "{mark}[bot]{/mark} found a creative way to get inside the dump!"
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if ps_imagenumber<=42:                          ## outfit 1
      $ps_imagenumber=random.randint(1,3)
    elif ps_imagenumber<=45:                        ## outfit 2
      $ps_imagenumber=random.randint(4,6)
    elif ps_imagenumber<=48:                        ## outfit 3
      $ps_imagenumber=random.randint(7,9)
    else:                                           ## male bot
      $ps_imagenumber=random.randint(52,54)
    if bot.bot_social.level<=3:                     ##  F,E,D strong hint - C,B weak hint - A,S no hint
      "Shit, [bot.heshe] didn't find anything. Maybe better {mark}social skill{/mark} would help [bot.himher] avoid patrols."
    elif bot.bot_social.level<=5:
      "Shit, [bot.heshe] didn't find anything. It might be bad luck but better {mark}social skill{/mark} couldn't hurt."
    else:
      "Shit, [bot.heshe] didn't find anything. {mark}[bot]{/mark} has strong {mark}social skill{/mark}, it's just bad luck."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if bot.scavenge_success==0:                     ## no successful searches yet
      "{mark}[bot]{/mark} hasn't found anything at the dump yet, maybe [bot.heshe] needs practice."
    elif bot.scavenge_success==1:
      "{mark}[bot]{/mark} found something once before, maybe [bot.heshe] will get better."
    elif bot.scavenge_success<=5:
      "{mark}[bot]{/mark} found things before, maybe [bot.heshe] will get better."
    elif bot.scavenge_success<=10:
      "Although {mark}[bot]{/mark} failed this time I think [bot.heshe] is getting better."
    elif bot.scavenge_success<=25:
      "{mark}[bot]{/mark} has been finding things more often, too bad [bot.heshe] failed this time."
    elif bot.scavenge_success<=50:
      "Although [bot.heshe] failed this time, {mark}[bot]{/mark} often finds things at the dump."
    else:  ## 51 or more
      "I'm surprised {mark}[bot]{/mark} found nothing this time, [bot.heshe] usually finds things."
  else:                                             ## hack door entry
    if bot.gender=="female":
      $ps_imagenumber=random.randint(31,39)         ## number picks outfit
    else:
      $ps_imagenumber=random.randint(64,66)         ## male bot
    "{mark}[bot]{/mark} hacked the door to get inside the dump."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if ps_imagenumber<=33:                          ## outfit 1
      $ps_imagenumber=random.randint(1,3)
    elif ps_imagenumber<=36:                        ## outfit 2
      $ps_imagenumber=random.randint(4,6)
    elif ps_imagenumber<=39:                        ## outfit 3
      $ps_imagenumber=random.randint(7,9)
    else:                                           ## male bot
      $ps_imagenumber=random.randint(52,54)
    if bot.bot_social.level<=3:                     ##  F,E,D strong hint - C,B weak hint - A,S no hint
      "Shit, [bot.heshe] didn't find anything. Maybe better {mark}social skill{/mark} would help [bot.himher] avoid patrols."
    elif bot.bot_social.level<=5:
      "Shit, [bot.heshe] didn't find anything. It might be bad luck but better {mark}social skill{/mark} couldn't hurt."
    else:
      "Shit, [bot.heshe] didn't find anything. {mark}[bot]{/mark} has strong {mark}social skill{/mark}, it's just bad luck."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if bot.scavenge_success==0:                     ## no successful searches yet
      "{mark}[bot]{/mark} hasn't found anything at the dump yet, maybe [bot.heshe] needs practice."
    elif bot.scavenge_success==1:
      "{mark}[bot]{/mark} found something once before, maybe [bot.heshe] will get better."
    elif bot.scavenge_success<=5:
      "{mark}[bot]{/mark} found things before, maybe [bot.heshe] will get better."
    elif bot.scavenge_success<=10:
      "Although {mark}[bot]{/mark} failed this time I think [bot.heshe] is getting better."
    elif bot.scavenge_success<=25:
      "{mark}[bot]{/mark} has been finding things more often, too bad [bot.heshe] failed this time."
    elif bot.scavenge_success<=50:
      "Although [bot.heshe] failed this time, {mark}[bot]{/mark} often finds things at the dump."
    else:  ## 51 or more
      "I'm surprised {mark}[bot]{/mark} found nothing this time, [bot.heshe] usually finds things."
  return

label scavenge_bot_mission_success_small(bot):      ## Bot found 'cheap' or 'nice' part(s)
  if bot.scavenge_success<100:                  ## increment scavenge success counter if under limit
    $bot.scavenge_success+=1

##    $print "Bot's success count:",bot.scavenge_success
##    $print "Mission Success Weight:",50+bot.bot_social.level*5+bot.scavenge_success

  if bot.bot_sex.level>=4 and bot.bot_electronics.level<bot.bot_sex.level:  ## oral sex entry (C or better and > electronics)
    if bot.gender=="female":
      $ps_imagenumber=random.randint(40,48)         ## number picks outfit
    else:
      $ps_imagenumber=random.randint(67,69)         ## male bot
    "{mark}[bot]{/mark} found a creative way to get inside the dump!"
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if ps_imagenumber<=42:                          ## outfit 1
      $ps_imagenumber=random.randint(10,15)
    elif ps_imagenumber<=45:                        ## outfit 2
      $ps_imagenumber=random.randint(16,21)
    elif ps_imagenumber<=48:                        ## outfit 3
      $ps_imagenumber=random.randint(22,27)
    else:                                           ## male bot
      $ps_imagenumber=random.randint(55,60)
    "Nice, [bot.heshe] found something useful! Not much, but it's free money."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
  else:                                             ## hack door entry
    if bot.gender=="female":
      $ps_imagenumber=random.randint(31,39)         ## number picks outfit
    else:
      $ps_imagenumber=random.randint(64,66)         ## male bot
    "{mark}[bot]{/mark} hacked the door to get inside the dump."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if ps_imagenumber<=33:                          ## outfit 1
      $ps_imagenumber=random.randint(10,15)
    elif ps_imagenumber<=36:                        ## outfit 2
      $ps_imagenumber=random.randint(16,21)
    elif ps_imagenumber<=39:                        ## outfit 3
      $ps_imagenumber=random.randint(22,27)
    else:                                           ## male bot
      $ps_imagenumber=random.randint(55,60)
    "Nice, [bot.heshe] found something useful! Not much, but it's free money."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
  return

label scavenge_bot_mission_success_large(bot):      ## Bot found 'good' or 'luxury' part(s)
  if bot.scavenge_success<100:                  ## increment scavenge success counter if under limit
    $bot.scavenge_success+=1

##    $print "Bot success count:",bot.scavenge_success
##    $print "Mission Success Weight:",50+bot.bot_social.level*5+bot.scavenge_success

  if bot.bot_sex.level>=4 and bot.bot_electronics.level<bot.bot_sex.level:  ## oral sex entry (C or better and > electronics)
    if bot.gender=="female":
      $ps_imagenumber=random.randint(40,48)         ## number picks outfit
    else:
      $ps_imagenumber=random.randint(67,69)         ## male bot
    "{mark}[bot]{/mark} found a creative way to get inside the dump!"
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if ps_imagenumber<=42:                          ## outfit 1
      $ps_imagenumber=random.randint(10,15)
    elif ps_imagenumber<=45:                        ## outfit 2
      $ps_imagenumber=random.randint(16,21)
    elif ps_imagenumber<=48:                        ## outfit 3
      $ps_imagenumber=random.randint(22,27)
    else:                                           ## male bot
      $ps_imagenumber=random.randint(55,60)
    "Wow, [bot.heshe] found something really nice! Lucky day!"
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
  else:                                             ## hack door entry
    if bot.gender=="female":
      $ps_imagenumber=random.randint(31,39)         ## number picks outfit
    else:
      $ps_imagenumber=random.randint(64,66)         ## male bot
    "{mark}[bot]{/mark} hacked the door to get inside the dump."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if ps_imagenumber<=33:                          ## outfit 1
      $ps_imagenumber=random.randint(10,15)
    elif ps_imagenumber<=36:                        ## outfit 2
      $ps_imagenumber=random.randint(16,21)
    elif ps_imagenumber<=39:                        ## outfit 3
      $ps_imagenumber=random.randint(22,27)
    else:                                           ## male bot
      $ps_imagenumber=random.randint(55,60)
    "Wow, [bot.heshe] found something really nice! Lucky day!"
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
  return

label scavenge_bot_mission_dead(bot):               ## Bot destroyed by thugs, only entry picture
  if bot.bot_sex.level>=4 and bot.bot_electronics.level<bot.bot_sex.level:  ## oral sex entry (C or better and > electronics)
    if bot.gender=="female":
      $ps_imagenumber=random.randint(40,48)         ## number picks which outfit
    else:
      $ps_imagenumber=random.randint(67,69)         ## male bot
    "{mark}[bot]{/mark} should have returned by now. You check hacked cams around the dump and see [bot.heshe] found a creative way to get inside the dump!"
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@400x600}"
  else:                                             ##  hack door entry
    if bot.gender=="female":
      $ps_imagenumber=random.randint(31,39)         ## number picks which outfit
    else:
      $ps_imagenumber=random.randint(64,66)         ## male bot
    "{mark}[bot]{/mark} should have returned by now. You check hacked cams around the dump and see [bot.heshe] hacked the door to get inside the dump!"
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@400x600}"
  "None of the cams show [bot.himher] leaving. I guess the fucking scavs took [bot.himher] or maybe some big pile of junk moved at the wrong time... Fuck!\n\n{mark}[bot]{/mark} is {bad}lost{/mark}."
  return

label scavenge_bot_mission_damaged(bot):            ##  Bot damaged by thugs
  if bot.bot_sex.level>=4 and bot.bot_electronics.level<bot.bot_sex.level:  ## oral sex entry (C or better and > electronics)
    if bot.gender=="female":
      $ps_imagenumber=random.randint(40,48)         ## number picks outfit
    else:
      $ps_imagenumber=random.randint(67,69)         ## male bot
    "{mark}[bot]{/mark} found a creative way to get inside the dump!"
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if ps_imagenumber<=42:                          ## outfit 1
      $ps_imagenumber=28
    elif ps_imagenumber<=45:                        ## outfit 2
      $ps_imagenumber=29
    elif ps_imagenumber<=48:                        ## outfit 3
      $ps_imagenumber=30
    else:                                           ## male bot
      $ps_imagenumber=random.randint(61,63)
    "Shit, [bot.heshe] was ambushed by two scavs but managed to fend them off. Fucking pests! At least [bot.heshe] is safe home now."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
  else:                                             ## hack door entry
    if bot.gender=="female":
      $ps_imagenumber=random.randint(31,39)         ## number picks outfit
    else:
      $ps_imagenumber=random.randint(64,66)         ## male bot
    "{mark}[bot]{/mark} hacked the door to get inside the dump."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
    if ps_imagenumber<=33:                          ## outfit 1
      $ps_imagenumber=28
    elif ps_imagenumber<=36:                        ## outfit 2
      $ps_imagenumber=29
    elif ps_imagenumber<=39:                        ## outfit 3
      $ps_imagenumber=30
    else:                                           ## male bot
      $ps_imagenumber=random.randint(61,63)
    "Shit, [bot.heshe] was ambushed by two scavs but managed to fend them off. Fucking pests! At least [bot.heshe] is safe home now."
    $action_image="missions scavenge scb_"+str(ps_imagenumber)
    center "{image=[action_image]@340x510}"
  return