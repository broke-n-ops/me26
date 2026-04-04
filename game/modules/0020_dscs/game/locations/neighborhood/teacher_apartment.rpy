init python:

##===variables===

  ## none needed yet

##===locations===

  class Location_teacher_apartment(Location):
    name="[ns_teacher_name]'s Apartment"

define label_goto_store_owner_apartment_action_info={
  "title": "[teacher_apartment]",
  }

##===functions===

label goto_teacher_apartment:
  $game.location="teacher_apartment"
  return "roaming"

label roaming_teacher_apartment:
  $image_number=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(image_number)
  header "[teacher_apartment]"

## some day there may be a reason to visit Simone's apartment and reactivate the code below
## for now dating Simone is a button from the home screen and there's nothing else to do there

##  call random_event("roaming_store_owner_apartment")
##  if _return=="default":
##    choice("goto_store_owner_apartment",cost=[("energy",1)]) "Stay Longer"
##    choice("goto_home",pos=16,key="home") "[home]"
##    choice("goto_neighborhood",pos=17,key="cancel") "[neighborhood]"
##  $process_event("roaming_finalize_store_owner_apartment")
##  $process_event("roaming_finalize","store_owner_apartment")

  return