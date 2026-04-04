init python:

##===variables===

  ## none needed yet

##===locations===

  class Location_store_owner_apartment(Location):
    name="[gn_store_owner_name]'s Apartment"

define label_goto_store_owner_apartment_action_info={
  "title": "[store_owner_apartment]",
  }

##===functions===

label goto_store_owner_apartment:
  $game.location="store_owner_apartment"
  return "roaming"

label roaming_store_owner_apartment:
  $game_bg="apartment bg_apartment"
  header "[store_owner_apartment]"

## some day there may be a reason to visit Ruthie's apartment and reactivate the code below
## for now dating Ruthie is a button from the home screen and there's nothing else to do there

##  call random_event("roaming_store_owner_apartment")
##  if _return=="default":
##    choice("goto_store_owner_apartment",cost=[("energy",1)]) "Stay Longer"
##    choice("goto_home",pos=16,key="home") "[home]"
##    choice("goto_neighborhood",pos=17,key="cancel") "[neighborhood]"
##  $process_event("roaming_finalize_store_owner_apartment")
##  $process_event("roaming_finalize","store_owner_apartment")
  return