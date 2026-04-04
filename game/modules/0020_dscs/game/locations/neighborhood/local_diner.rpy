init python:

##===variables===

  nh_local_diner_visit=0  ## flag, set to 1 after first visit
  nh_diner_mob_advice=0   ## flag, set to 1 after giving zen-like mob advice

##===locations===

  class Location_local_diner(Location):
    name="Street Diner"

define label_goto_local_diner_action_info={
  "title": "[local_diner]",
  }

label goto_local_diner:
  $game.location="local_diner"
  return "roaming"

##===functions===

label roaming_local_diner:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_diner ld_1"
  else:
    $game_bg="local_diner ld_2"
  header "[local_diner]"
  if nh_local_diner_visit==0:                   ## first visit to street diner
    $nh_local_diner_visit=1                     ## set flag to not repeat
    $gn_diner_owner_rename=1                    ## set flag for diner owner rename
    $temp_int=2                                 ## first visit is positive
    $temp_text="You see {mark}[gn_diner_owner_name]{/} who owns the diner. He's a {mark}retired bot engineer{/} who's always been helpful and you enjoy talking about bots with him. He's not busy so you have time to talk."
  else:
    $temp_int=random.randint(1,5)
    if temp_int==1:                             ## 20% chance-Earl busy with customers
      $temp_text="Unfortunately {mark}[gn_diner_owner_name]{/} is too busy with customers to talk to you now. He needs the business so I guess it's OK but I'm disappointed."
    elif temp_int==2:
      $temp_text="{mark}[gn_diner_owner_name]'s{/} not busy so you can ask him a few questions about {mark}electronics and computers{/}. He's a lot easier to understand than my old high school teachers!"
    elif temp_int==3:
      $temp_text="I'm lucky that {mark}[gn_diner_owner_name]{/} isn't busy so we can talk {mark}electronics and computers{/}. A lot of the things he tells me will help a lot when I'm working on bots!"
    elif temp_int==4:
      $temp_text="{mark}[gn_diner_owner_name]{/} and I sit down and discuss the {mark}electronics and computers{/} used in bots. I think he knows everything and I'm glad he's willing to help me out!"
    else:  ## must be 5
      $temp_text="{mark}[gn_diner_owner_name]'s{/} not busy so you ask him a few questions about {mark}electronics and computers{/}. I wish my high school teachers were more like {mark}[gn_diner_owner_name]{/}!"
  if temp_int==1:                                  ## 20%-Earl too busy
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $temp_int_pic=random.randint(7,8)
    $action_image="local_diner ld_"+str(temp_int_pic)
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    "[temp_text]"
    ""
    "Should I hang around and see if {mark}[gn_diner_owner_name]{/} has time to talk with me later?"
    $mc.mood.give_xp(randint(-50,-20))             ## wasted AP
  else:                                            ## positive, computers or electronics
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $temp_int_pic=random.randint(3,6)
    $action_image="local_diner ld_"+str(temp_int_pic)
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    if quests.mobprotection.started and nh_diner_mob_advice==0 and not quests.mobprotection.finished:  ## first visit to Earl during mob protection
      $nh_diner_mob_advice=1                      ## set flag to prevent repeat
      "Before your usual discussion of tech stuff you quietly tell {mark}[gn_diner_owner_name]{/} about the mob demanding you give them bots and he says {say}'Nothing is permanent, all things change. Sometimes we have to help make change happen'.{/}"
      ""
      "I thanked him for his advice and we moved on to a good discussion about tech stuff. "
    else:
      "[temp_text]"
    ""
    "I've learned a lot, should I talk to {mark}[gn_diner_owner_name]{/} longer?"
    $mc.mood.give_xp(randint(20,50))               ## identical to relax at Robosechs
    $mc.give_xp("computers",randint(25,100))       ## match Robosechs (20,80) but upscale to compensate the 20% failure rate
    $mc.give_xp("electronics",randint(25,100))     ## match Robosechs (20,80) but upscale to compensate the 20% failure rate
    $mc.give_xp("social",randint(5,25))            ## small social skill gain for conversation with a real person
  call random_event("roaming_local_diner")
  if _return=="default":
    choice("goto_local_diner",cost=[("energy",1)]) "Stay Longer"
    choice("goto_home",pos=16,key="home") "[home]"
    choice("goto_neighborhood",pos=17,key="cancel") "[neighborhood]"
  $process_event("roaming_finalize_local_diner")
  $process_event("roaming_finalize","local_diner")
  return
