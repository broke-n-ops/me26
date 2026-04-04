init python:
  class Location_robosechs(Location):
    name="Robo/6 Club"

define label_goto_flea_market_action_info={
  "title": "[robosechs]",
  }

label goto_robosechs:
  $game.location="robosechs"
  "A bouncer scans you and says, {say}Welcome to RoboSechs, enjoy your time{/}. Wow, that combat bot has military-grade parts."
  $action_image="squirrel botshop sq_7"
  center "{image=[action_image]@800x600}"
  
  return "roaming"

label roaming_robosechs:
  $game_bg="robosechs bg"
  $game_bgm="robosechs bgm"
  header "[robosechs]"
  "You hear loud music, see dancing sexbots, and smell drugs. Bots serve customers drinks and will do more if you have the money."
  ""
  call random_event("roaming_robosechs")
  if _return=="default":
    choice(">>>robosechs_relax") "Relax"
    choice(">>>robosechs_private_room") "Private Room"
    choice(">>>robosechs_sell_bot") "Offer Bot"
    choice("goto_home",pos=16,key="home") "[home]"
    choice("goto_street",pos=17,key="cancel") "[street]"
  $process_event("roaming_finalize_robosechs")
  $process_event("roaming_finalize","robosechs")
  return
