init python:

##===variables===

  nh_corner_store_visit=0  ## flag, set to 1 after first visit

##===locations===

  class Location_corner_store(Location):
    name="Corner Store"

define label_goto_corner_store_action_info={
  "title": "[corner_store]",
  }

label goto_corner_store:
  $game.location="corner_store"
  return "roaming"

##===functions===

label roaming_corner_store:
  $temp_int= random.randint(1,2)
  if temp_int==1:
    $game_bg="corner_store cs_1"
  else:
    $game_bg="corner_store cs_2"
  header "[corner_store]"
  if nh_corner_store_visit==0:               ## first visit to corner store
    $nh_corner_store_visit=1                 ## set flag to not repeat
    $gn_store_owner_rename=1                 ## set flag for store owner rename
    $temp_int=2                              ## first visit is positive
    $temp_text="You see {mark}[gn_store_owner_name]{/} who owns the store. {mark}She's pretty cute and very friendly too{/}. I'm usually awkward with women but not with her for some reason. Nice, she's not busy and we can talk!"
  else:
    $temp_int=random.randint(1,5)
    if temp_int==1 and gn_which_pair==-1:    ## 20% chance-Ruthie busy with customers-ONLY BEFORE SHE HAS BOTS  NEED TO TEST THIS!!!
      $temp_text="Unfortunately {mark}[gn_store_owner_name]{/} is busy with customers. I know she needs the business but I was looking forward to talking with her."
    elif temp_int==1:
      $temp_text="{mark}[gn_store_owner_name]'s{/} not busy so you spend a while talking with her. She doesn't know much about bots but she always seems interested!"
    elif temp_int==2:
      $temp_text="I'm glad {mark}[gn_store_owner_name]{/} isn't busy, I really enjoy talking with her. She's always cheerful even when business is slow, how does she do it!"
    elif temp_int==3:
      $temp_text="{mark}[gn_store_owner_name]{/} smiles when she sees me coming into her store. Talking with her always puts me in a good mood. She's kind of hot too!"
    elif temp_int==4:
      $temp_text="Business is slow but {mark}[gn_store_owner_name]{/} seems to cheer up when she sees me. I wonder if it's me or if she's this way with all customers?"
    else:  ## must be 5
      $temp_text="{mark}[gn_store_owner_name]'s{/} always fun to talk with and our conversations put me in a good mood. I'm glad she isn't busy but I know she needs paying customers too."
  if temp_int==1 and gn_which_pair==-1:      ## 20% chance-Ruthie busy with customers-ONLY BEFORE SHE HAS BOTS  NEED TO TEST THIS!!!!
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $temp_int=random.randint(7,8)
    $action_image="corner_store cs_"+str(temp_int)
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    "[temp_text]"
    ""
    "Maybe I should wait around for a while, {mark}[gn_store_owner_name]{/} might have time to talk soon."
    $mc.mood.give_xp(randint(-50,-20))       ## wasted AP
  else:
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $temp_int=random.randint(3,6)
    $action_image="corner_store cs_"+str(temp_int)
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    "[temp_text]"
    ""
    "{mark}[gn_store_owner_name]{/} is great and I'm really enjoying myself, should I stay a little longer?"
    $global mc_so_value
    if mc_so_value<50:                                  ## do NOT allow FWB until FWB quest end
      call mc_update_relation(gn_store_owner_name,1,0)  ## relationship gain for visiting
    $mc.mood.give_xp(randint(20,50))         ## identical to relax at Robosechs
    $mc.give_xp("social",randint(25,100))    ## match Robosechs (20,80) but upscale to compensate the 20% failure rate
  call random_event("roaming_corner_store")
  if _return=="default":
    choice("goto_corner_store",cost=[("energy",1)]) "Stay Longer"
    choice("goto_home",pos=16,key="home") "[home]"
    choice("goto_neighborhood",pos=17,key="cancel") "[neighborhood]"
  $process_event("roaming_finalize_corner_store")
  $process_event("roaming_finalize","corner_store")
  return