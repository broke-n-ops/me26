init python:
  class Location_dump_site(Location):
    name="Dump Site"

define label_goto_dump_site_action_info={
  "title": "[dump_site]",
  }

label goto_dump_site:
  $game.location="dump_site"
  $dump_site["scavenge_loot_now"]=[]
  return "roaming"

label roaming_dump_site:
  $game_bg="dump_site bg"
  $game_bgm="dump_site bgm"
  header "[dump_site]"
  
## replaced in 0.8.n
  # "A disgusting smell comes from the far west side of the district: the infamous city dump. Trash from the entire district is collected and hopefully recycled here. The recycler AI isn't very good so some nice stuff slips by occasionally."
  # ""
  # "The dump is home to scavengers, junkies, and other desperate people. Periodically, security sweeps the place and shoots those not smart enough to hide during these patrols. Not the friendliest place but, if you aren't stupid, you can avoid most problems."
  # ""
  # "Skillful and lucky scavengers can find almost anything here; mostly cheap eyes, arms, or legs but sometimes a damaged luxury sexbot. You just need to dig through all kinds of junk to find these treasures. Not a place for the faint-hearted!"
  # ""

  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "dump_site dmp_1"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "It's always strange seeing the dump surrounded by high walls and guarded but there are lots of idiots who throw away valuable stuff. After picking out the decent stuff and selling it to flea market vendors they recycle the rest. I don't want to know what they do with the smelly stuff!"
  ""
  $act.end_block()
  "Getting in isn't hard, the guards aren't paid well and are lazy. I've heard they accept bribes but I always sneak in. I don't have money to waste bribing guards at the dump! For the right price I've heard they let homeless people live in the dump. You'd have to be really desperate to live there!"
  ""
  "Once you're in you've got to watch out for patrols though. They're better paid and take their jobs seriously. It might just be rumors to scare people away but I've heard they're authorized to shoot scavengers on site. I'm always careful to avoid them just in case."

  $quests.where_to_get_bots.add_method("dump_site","you can find discarded bots at {mark}[dump_site]{/}")
  $quests.where_to_get_bot_parts.add_method("dump_site","you can find discarded bot parts at {mark}[dump_site]{/}")
  call random_event("roaming_dump_site")
  if _return=="default":
    choice(">>>dump_site_scavenge") "Scavenge"
    choice("goto_home",pos=16,key="home") "[home]"
    choice("goto_street",pos=17,key="cancel") "[street]"
  $process_event("roaming_finalize_dump_site")
  $process_event("roaming_finalize","dump_site")
  return
