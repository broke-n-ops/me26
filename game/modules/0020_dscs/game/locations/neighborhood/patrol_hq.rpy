init python:

##===variables===

  phq_button=0  ## flag, set to 1 when the button should be shown

##===locations===

  class Location_patrol_hq(Location):
    name="Patrol HQ"

define label_goto_patrol_hq_action_info={
  "title": "[patrol_hq]",
  }

##===functions===

label goto_patrol_hq:
  $game.location="patrol_hq"
  return "roaming"

label roaming_patrol_hq:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"  ## TEMP - replace with new pictures
  else:
    $game_bg="corner_store cs_2"
  header "[patrol_hq]"

## insert stuff here about visit and preventive maintenance

  call random_event("roaming_patrol_hq")
  if _return=="default":
    choice("goto_patrol_hq",cost=[("energy",1)]) "Stay Longer"
    choice("goto_home",pos=16,key="home") "[home]"
    choice("goto_neighborhood",pos=17,key="cancel") "[neighborhood]"
  $process_event("roaming_finalize_patrol_hq")
  $process_event("roaming_finalize","patrol_hq")
  return