##===cheat functions-called from 'home.rpy'

## init flag variable

init python:
  enable_cheats=0       ## set to 1 to enable cheats

label cheat_buttons:
  if enable_cheats:
    choice("home_workout_money_cheat",pos=8) "Money Cheats!"      ## add or subtract money
    choice("home_workout_fitness_cheat",pos=9) "Fitness Cheats!"  ## add or subtract Strength and Stamina
    choice("rays_activate_online",pos=10) "Rays Online Cheat!"     ## activate Ray's Online to make parts available
  return

label home_workout_money_cheat:
  ""
  "Money Cheats:"
  ""
  choice("hw_add_100k") "Add 100K"
  choice("hw_add_10k") "Add 10K"
  choice("hw_subtract_10k") "Subtract $10K"
  choice("hw_subtract_100k") "Subtract $100K"
  choice("hw_add_money",pos=12) "Set to $20M"
  choice("hw_subtract_money",pos=13) "Set to $1"
  choice("<<<",pos=17) "Cancel"
  return

label hw_add_money:
  ""
  "Set Money to $20,000,000"
  ""
  $mc.money=20000000
  choice("<<<") "Continue"
  return

label hw_subtract_money:
  ""
  "Set Money to $1"
  ""
  $mc.money=1
  choice("<<<") "Continue"
  return

label hw_add_100k:
  ""
  "Add $100,000"
  ""
  $mc.money=mc.money+100000
  choice("<<<") "Continue"
  return
  
label hw_add_10k:
  ""
  "Add $10,000"
  ""
  $mc.money=mc.money+10000
  choice("<<<") "Continue"
  return

label hw_subtract_10k:
  ""
  "Subtract $10,000"
  ""
  $mc.money=mc.money-10000
  choice("<<<") "Continue"
  return

label hw_subtract_100k:
  ""
  "Subtract $100,000"
  ""
  $mc.money=mc.money-100000
  choice("<<<") "Continue"
  return

label home_workout_fitness_cheat:
  ""
  "Fitness Cheats:"
  ""
  choice("hw_add_1k_strength") "+1000 Strength"
  choice("hw_add_10k_strength") "+10000 Strength"
  choice("hw_subtract_1k_strength",pos=3) "-1000 Strength"
  choice("hw_subtract_10k_strength",pos=4) "-10000 Strength"
  choice("hw_add_1k_stamina",pos=6) "+1000 Stamina"
  choice("hw_add_10k_stamina",pos=7) "+10000 Stamina"
  choice("hw_subtract_1k_stamina",pos=9) "-1000 Stamina"
  choice("hw_subtract_10k_stamina",pos=10) "-10000 Stamina"
  choice("hw_max_strength",pos=12) "Max Strength"
  choice("hw_max_stamina",pos=13) "Max Stamina"
  choice("<<<",pos=17) "Cancel"
  return

label hw_max_strength:
  ""
  "Max Strength"
  ""
  $mc.give_xp("strength",99999)
  choice("<<<") "Continue"
  return

label hw_max_stamina:
  ""
  "Max Stamina"
  ""
  $mc.give_xp("stamina",99999)
  choice("<<<") "Continue"
  return

label hw_add_1k_strength:
  ""
  "Add 1000 Strength"
  ""
  $mc.give_xp("strength",1000)
  choice("<<<") "Continue"
  return

label hw_subtract_1k_strength:
  ""
  "Subtract 1000 Strength"
  ""
  $mc.give_xp("strength",-1000)
  choice("<<<") "Continue"
  return

label hw_add_10k_strength:
  ""
  "Add 10000 Strength"
  ""
  $mc.give_xp("strength",10000)
  choice("<<<") "Continue"
  return

label hw_subtract_10k_strength:
  ""
  "Subtract 10000 Strength"
  ""
  $mc.give_xp("strength",-10000)
  choice("<<<") "Continue"
  return

label hw_add_1k_stamina:
  ""
  "Add 1000 Stamina"
  ""
  $mc.give_xp("stamina",1000)
  choice("<<<") "Continue"
  return

label hw_subtract_1k_stamina:
  ""
  "Subtract 1000 Stamina"
  ""
  $mc.give_xp("stamina",-1000)
  choice("<<<") "Continue"
  return

label hw_add_10k_stamina:
  ""
  "Add 10000 Stamina"
  ""
  $mc.give_xp("stamina",10000)
  choice("<<<") "Continue"
  return

label hw_subtract_10k_stamina:
  ""
  "Subtract 10000 Stamina"
  ""
  $mc.give_xp("stamina",-10000)
  choice("<<<") "Continue"
  return