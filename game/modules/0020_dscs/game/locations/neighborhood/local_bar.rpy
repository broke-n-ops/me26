init python:

##===variables===

  nh_local_bar_visit=0       ## flag, set to 1 after first visit
  ns_training_advice=0       ## flag for special visit with Louis so he tells you 'practice makes perfect' for night school escort training
  ns_celebrate_completion=0  ## set if mob protection finished before night school to change reason for recommendation to go to local bar

##===locations===

  class Location_local_bar(Location):
    name="Neighborhood Bar"

define label_goto_local_bar_action_info={
  "title": "[local_bar]",
  }

label goto_local_bar:
  $game.location="local_bar"
  return "roaming"

##===functions===

label roaming_local_bar:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="local_bar lb_1"
  else:
    $game_bg="local_bar lb_2"
  header "[local_bar]"
  if nh_local_bar_visit==0:                        ## first visit to local bar
    $nh_local_bar_visit=1                          ## set flag to not repeat
    $gn_retired_fighter_rename=1                   ## set flag for retired fighter rename
    $temp_int=2                                    ## first visit is positive
    $temp_text="An old guy at the bar is talking about {mark}bot UFC fights{/}. You learn his name is {mark}[gn_retired_fighter_name]{/} and he's a {mark}retired boxer and UFC bot trainer{/}."
  else:
    $temp_int=random.randint(1,3)
    if temp_int==1 and ns_training_advice==0:      ## 33%-old fighter not at bar-check flag for ns escort training advice not set
      $temp_text="Unfortunately {mark}[gn_retired_fighter_name]{/} is not at the bar right now so you get a drink and do some people watching."
    elif temp_int==2:                              ## 33%-talk old fighter 1
      $temp_text="You see that {mark}[gn_retired_fighter_name]{/} is at the bar so you buy a drink and join him, you're sure he'll give you pointers on {mark}bot combat skill{/}."
    else:                                          ## 33%-talk old fighter 2-fall through for night school special advice
      $temp_text="Great, {mark}[gn_retired_fighter_name]{/} is at the bar, I'll buy a beer and sit with him. He loves to talk and he'll teach me something about {mark}training bots in combat{/}."
  if temp_int==1 and ns_training_advice==0:        ## 33%-old fighter not at bar and flag for ns escort training advice not set
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $temp_int_pic=random.randint(7,8)
    $action_image="local_bar lb_"+str(temp_int_pic)
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    "[temp_text]"
    ""
    "Should I buy another drink and hang around to see if {mark}[gn_retired_fighter_name]{/} comes in later?"
    $mc.mood.give_xp(randint(10,40))               ## bar is still fun, just not as much
    $mc.give_xp("social",randint(5,15))            ## small social skill gain for being out in public
  else:                                            ## talking to Louis-fall through for escort training advice
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $temp_int_pic=random.randint(3,6)
    $action_image="local_bar lb_"+str(temp_int_pic)
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    "[temp_text]"
    ""
    if ns_training_advice==1:                      ## special advice for night school escort training
      $ns_training_advice=0                        ## reset flag, one time event
      "I told {mark}[gn_retired_fighter_name]{/} I need a good escort and he said, {say}Look kid, just train bots in{/} {mark}combat{/} {say}again and again. Every time you train them you'll learn more and will do better next time. Remember the old saying{/} {mark}'practice makes perfect'{/}{say}!"
      ""
    "I've learned a lot, should I talk to {mark}[gn_retired_fighter_name]{/} longer?"  ## 0.9.1 - was diner owner name: fixed
    $mc.mood.give_xp(randint(20,50))
    $mc.give_xp("combat",randint(30,120))          ## match Robosechs (20,80) but upscale to compensate the 33% failure rate
    $mc.give_xp("social",randint(10,25))           ## small social skill gain for conversation with a real person
  call random_event("roaming_local_bar")
  if _return=="default":
    choice("goto_local_bar",cost=[("money",15),("energy",1)]) "Stay Longer"
    choice("goto_home",pos=16,key="home") "[home]"
    choice("goto_neighborhood",pos=17,key="cancel") "[neighborhood]"
  $process_event("roaming_finalize_local_bar")
  $process_event("roaming_finalize","local_bar")
  return