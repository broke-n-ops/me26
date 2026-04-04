## 0.11.N MOVED LOCATION CODE FROM 'store_raysbotshop.rpy'

init python:

##===variables===

  ## declared in 'store_raysbotshop.rpy' in 0020-locations

##===locations===

  class Location_rays_boutique(Location):
    name="Raymond's Bot Boutique"

define label_goto_rays_boutique_action_info={
  "title": "[rays_boutique]",
  }

##===functions===

label goto_rays_boutique:
  $game.location="rays_boutique"
  return "roaming"

## 0.15.n new roaming function created to enable payment before entering the club
label roaming_rays_boutique:                    
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)          ## random between 2 backgrounds
  header "[rays_boutique]"
  if bp_suit_for_rays==0:                               ## MC in original clothing (not given suit by Simone)
    "When you exit the elevator there are two intimidating bouncers looking you over. They make you nervous staring at you like that but it's their job."
    "{size=-22} "
    $temp_image=random.randint(41,42)
    $action_image="squirrel rays ray_"+str(temp_image)
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    if rays_first_boutique_visit==1:                     ## first visit you give them a free pass
      "You hand one of them your free pass and he looks it over carefully. Eventually they both step aside to let you in. I wonder what it's like inside."
    else:
      "The {mark}$1,200{/} admission fee is a lot of money but if you want to buy a luxury bot you have to pay the fee and go in."
  else:                                                 ## MC in suit for Raymond's
    "Exiting the elevator you see the usual two bouncers. Even though they've seen you before they take their job seriously and look you over carefully."
    "{size=-22} "
    $temp_image=random.randint(41,42)
    $action_image="squirrel rays ray_"+str(temp_image)+"a"
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    "Your shop is doing well so the {mark}$1,200{/} admission fee doesn't seem so big now, it's worth it if you want to buy luxury bots."

## moved to main file, after testing delete the next line
##  call rays_initialize_visit

## NEXT LINE ONLY USED IN SAVED GAMES THAT COMPLETED THE BOT SALESMAN'S VISITS - kept this line here
  $quests.where_to_get_bots.add_method("sr24_raymonds","you can find luxury bots for sale at {mark}Raymond's Bot Boutique{/}")

  if rays_first_boutique_visit==1:                     ## first visit is free courtesy of salesman and you can't back out
    choice ("rays_enter_club",cost=[("energy",rays_boutique_energy_cost)]) "Enter Club"  ## takes time to view show, 2 AP
  else:
    choice ("rays_enter_club",cost=[("energy",rays_boutique_energy_cost),("money",rays_boutique_money_cost)]) "Enter Club"
    choice("goto_street") "Leave"                      ## if you leave there is no cost and you go back to the street
## added 2 lines in 0.9.n when creating location
  $process_event("roaming_finalize_rays_boutique")
  $process_event("roaming_finalize","rays_boutique")
  return

##===functions start on line 475 of file 'store_raysbotshop.rpy' in '0030-game-content' as of version 0.15.n
## END OF INSERT