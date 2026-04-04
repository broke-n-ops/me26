init python:
  class Location_street(Location):
    name="District TX-13"

define label_goto_street_action_info={
  "title": "[street]",
  }

label goto_street:
  $game.location="street"
  return "roaming"

label roaming_street:
  $sr_which_street=random.randint(1,4)
  if sr_which_street==1:
    $game_bg="street bg_1"
  elif sr_which_street==2:
    $game_bg="street bg_2"
  elif sr_which_street==3:
    $game_bg="street bg_3"
  else:
    $game_bg="street bg_4"
  $game_bgm="street bgm"
  header "[street]"
  "This part of town is much better than the lower level slums but even so there's nothing to get too excited about."
  ""
  " Huge buildings with tiny apartments, brothels, night clubs, chop shops, flea markets, and even a few legitimate businesses."
  ""
  "Not much traffic and few people are on the sidewalks because crime levels are high."
  ""
  "Unlike the slums, you can expect to make it home alive."
  if now("evening") and rays_activated==1 and rays_already_visited==0:  ## display note about Rays being open unless already visited today
    if fwb_deactivate_rays==1:                                          ## Raymond's is off limits until you get the suit from Simone
      $temp_text="{bad}{mark}Raymond's Bot Boutique{/} is open but after the bad experience with {mark}[gn_store_owner_name]{/} I'm not going there again.{/}"
    else:
      $temp_text="{mark}Raymond's Bot Boutique{/} is open if I want to go there."
    $temp_int=random.randint(1,2)                                       ## 2 possible pictures of Raymond's
    if temp_int==1:
      $image_text="squirrel rays ray_45"
    else:
      $image_text="squirrel rays ray_46"
    ""                                                                  ## insert 2 full size blank line before note
    ""
    $act.start_block("l:250 c:content_width-250")
    $action_image=image_text
    center "{image=[action_image]@150x225}"
    $act.set_block("c")
    "[temp_text]"
    $act.end_block() 
  call random_event("roaming_street")
  if _return=="default":
    choice("goto_robosechs") "[robosechs]"
    choice("goto_flea_market") "[flea_market]"
    choice("goto_dump_site") "[dump_site]"

##  ADDED IN SR24 0.4.n to create the location for the luxury bot store when active
    if rays_activated==1:
      if now("evening"):                                            ## boutique only open in evening
## 0.15.n now using the 'fwb_deactivate_rays' flag created in 0.14
        if fwb_deactivate_rays==1:                                  ## Ray's deactivated after bad date with Ruthie
          choice(None, hint="{hint}(no way!){/}") "Raymond's"
        elif rays_already_visited==1:                               ## you already visited this evening
          choice(None, hint="{hint}(show over){/}") "Raymond's"
        else:                                                       ## haven't visited and not deactivated
## 0.9.n changed rays boutique to location
          choice("goto_rays_boutique") "Raymond's"                  ## active button - old version: choice("rays_luxury_bots") "Raymond's" - location name is too long for button
      else:
        choice(None,hint="{hint}(evenings only){/}") "Raymond's"
    choice("goto_home",pos=17,key=["home","cancel"]) "[home]"
  $process_event("roaming_finalize_street")
  $process_event("roaming_finalize","street")
  return
