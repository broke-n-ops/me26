init python:

  class Location_neighborhood(Location):
    name="Neighborhood"

define label_goto_neighborhood_action_info={
  "title": "[neighborhood]",
  }

label goto_neighborhood:
  $game.location="neighborhood"
  return "roaming"

label roaming_neighborhood:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="neighborhood nbg_1"
  else:
    $game_bg="neighborhood nbg_2"
  header "[neighborhood]"
  
  "You leave the shop and step into your {mark}local neighborhood{/}. It's not the {mark}nicest place{/} or the {mark}safest place{/} but I can afford the rent."
  ""
  "There are a few businesses nearby that provide all your needs: a {mark}corner store{/} to buy food, a {mark}street diner{/} when I'm too lazy to prepare food, and a {mark}neighborhood bar{/} when I want to relax."
  ""
  "I always {mark}spend a little money{/} wherever I go, everyone in this neighborhood {mark}struggles to make ends meet{/}."

  call random_event("roaming_neighborhood")
  if _return=="default":
    choice("goto_corner_store",cost=[("money",20),("energy",1)]) "[corner_store]"
    choice("goto_local_diner",cost=[("money",10),("energy",1)]) "[local_diner]"
    choice("goto_local_bar",cost=[("money",15),("energy",1)]) "Local Bar"          ## didn't use location name, too long
## 4 lines - Delay for Future Version, no purpose yet for 2 new locations
##    if phq_button or quests.goodneighbor.finished:                ## if flag set or quest ended for saved games
##      choice("goto_patrol_hq",cost=[("energy",1)]) "[patrol_hq]"
##    if quests.fwbenefits.finished:                                ## button only applies after quest
##      choice("goto_store_owner_apartment",cost=[("energy",1)]) "[store_owner_apartment]"
    choice("goto_home",pos=17) "Home"
  $process_event("roaming_finalize_neighborhood")
  $process_event("roaming_finalize","neighborhood")
  return


