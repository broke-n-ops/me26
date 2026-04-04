## Home Reminders - function to place reminders about what's available this turn
## - Every evening Raymond's Bot Boutique is open if activated
##   - On Sunday evenings after you've delivered 'sucky bot' Simone is at Raymond's
## - On Wednesday evenings Karaoke
## - At night when dates with Ruthie are available
## - Damaged patrol bot reminder - moved from home.rpy file - this one should always be last
## NOTE: When you add the car this will need fixing for the amount of AP and money to get downtown (-1 AP, -20 subway, -25 locker, +? parking)

## variable
init python:
  rm_stubborn_player=0      ## count how many times the reminder to use the free pass is shown

## functions

label home_reminders:

## Raymond's Bot Boutique
  $global rays_activated
  $global bp_first_sex_teacher
  $global rm_stubborn_player
  $global bp_suit_for_rays
  "{size=-8} "  ## add a blank line before reminders
## reminder for Raymond's requires: evening, activated, no repeats same evening, not deactivated after bad date with Ruthie (re-activated when Simone gives you the suit)
  if now("evening") and rays_activated!=0 and rays_already_visited==0 and fwb_deactivate_rays!=1:
    if rays_first_boutique_visit==1:                                    ## You haven't gone to Raymond's yet 
      $rm_stubborn_player+=1                                               ## counter for how many times you get this reminder
      $temp_int=random.randint(1,3)                                     ## 3 possible pictures of salesman at your shop
      if temp_int==1:
        $image_text="quests mob_protection mp_177"                      ## 1st bot offered
      elif temp_int==2:
        $image_text="quests mob_protection mp_186"                      ## 2nd bot offered
      else:
        $image_text="squirrel rays ray_3"                               ## 3rd bot offered
      $temp_text="{mcsay}I have a free pass to {mark}Raymond's Bot Boutique{/} in {mark}District TX-13{/}, I should check it out.{/} {mark}(cost: 3AP, $20){/}"
    elif now("sunday") and bp_first_sex_teacher==1:                     ## Simone is at Raymond's on Sundays
      $temp_int=random.randint(1,3)                                     ## random between 3 - Simone at Raymonds
      if temp_int==1:
        $image_text="squirrel rays ray_47"
      elif temp_int==2:
        $image_text="squirrel rays ray_48"
      else:
        $image_text="squirrel rays ray_49"
      if mc_nst_date_counter>=12:                                       ## last opportunity before relationship loss
        $temp_text="{mcsay}I should go to {mark}Raymond's Bot Boutique{/} to {bad}avoid damaging my relationship{/} with {mark}[ns_teacher_name]{/}.{/} {mark}(cost: 3AP, $1,245){/}"
      else:
        $temp_text="{mcsay}On Sunday's {mark}[ns_teacher_name]{/} often goes to {mark}Raymond's Bot Boutique{/}, maybe I should go there.{/} {mark}(cost: 3AP, $1,245){/}"
    else:                                                               ## NOT first Raymond's visit and NOT Sunday (Simone)
      $temp_int=random.randint(1,2)                                     ## 2 possible pictures of Raymond's
      if temp_int==1:
        $image_text="squirrel rays ray_45"
      else:
        $image_text="squirrel rays ray_46"
      if bp_suit_for_rays==0:                                           ## haven't received suit for Raymond's; Raymond's $1200, no locker fee, subway $20: total $1220
        $temp_text="{mcsay}{mark}Raymond's Bot Boutique{/} is open, they have great luxury bots but they are expensive.{/} {mark}(cost: 3AP, $1,220){/}"
      else:                                                             ## you have the suit for Raymond's; Raymond's $1200, locker fee $25, subway $20: total $1245
        $temp_text="{mcsay}{mark}Raymond's Bot Boutique{/} is open and I have a nice suit so I can go there again.{/} {mark}(cost: 3AP, $1,245){/}"
    "{size=-8} "  ## insert blank line before reminder
    $act.start_block("l:250 c:content_width-250")
    $action_image=image_text
    center "{image=[action_image]@150x225}"
    $act.set_block("c")
    "[temp_text]"
    if rm_stubborn_player>21 and rays_first_boutique_visit==1:
##    if rm_stubborn_player>1 and rays_first_boutique_visit==1:    ## FOR TESTING
      "{size=-12}{bad}Your free pass is over 3 weeks old. Until you use the free pass you will be given only 3 AP each evening. This is EXACTLY enough to select {/}Leave Home{bad}, select {/}District TX-13 (1 AP plus a small amount of money){bad}, select {/}Raymond's{bad}, select {/}Enter Club (2 AP){bad}, and finally select {/}Begin Show{bad}. Nothing bad will happen and you will receive valuable information. I suggest you stop being stubborn and/or foolish and do this.{/}"
      $mc.energy=3
    $act.end_block()                                                    ## required for line feeds between reminders

## Dates with Ruthie - moved from 'friends_with_benefits.rpy' and modified
  $global fwb_date_available
  $global fwb_mc_new_clothes  ## 0=old clothes, 1=new clothers
  $global fwb_already_asked   ## set to the day number the time you asked, if this is today's number you cannot ask again
  if now("night") and fwb_date_available==1 and fwb_already_asked!=now.day: 
    if fwb_mc_new_clothes==0:
      $temp_int=random.randint(137,140)
    else:
      $temp_int=random.randint(142,145)
    $image_text="quests friends_with_benefits fwb_"+str(temp_int)
    "{size=-8} "  ## insert blank line before reminder
    $act.start_block("l:250 c:content_width-250")
    $action_image=image_text
    center "{image=[action_image]@150x600}"
    $act.set_block("c")
    if mc_so_date_counter>=5:        ## date Ruthie now or lose 1 relationship point when you sleep (>= is just in case, could be ==)
      "{mcsay}I should go out with {mark}[gn_store_owner_name]{/} tonight otherwise {bad}our relationship will suffer{/}.{/} {mark}(cost: $250, 3AP, Time){/}"
    else:
      "{mcsay}Maybe I should ask {mark}[gn_store_owner_name]{/} to go out tonight, we'll probably spend the night together!{/} {mark}(cost: 3AP, Time){/}"
    $act.end_block()                 ## required for line feeds between reminders

## damaged patrol bot to repair
  $global gn_repairing_bot
  $global gn_damaged_bot_waiting
  $reminder_needed=0                                     ## set to 1 if a reminder is needed and then display it
  if gn_repairing_bot==0 and gn_damaged_bot_waiting==1:  ## no damaged patrol bots in capsules or storage but one is waiting
    $reminder_needed=1
    $temp_text="{bad}You have a damaged patrol bot waiting for an available capsule or available space in storage.{/}"
  elif gn_repairing_bot==1:                              ## 1 damaged patrol bot in a capsule or storage
    $reminder_needed=1
    $temp_text="{bad}You have a damaged patrol bot that needs to be repaired.{/}"
    if gn_damaged_bot_waiting==1:                        ## there is ALSO a bot waiting for space
      $temp_text=temp_text+"{bad} You also have another damaged patrol bot waiting for an available capsule or available space in storage.{/}"
  elif gn_repairing_bot>1:                               ## 2 or more damaged patrol bots in capsules or storage
    $reminder_needed=1
    $temp_text="{bad}You have [gn_repairing_bot] damaged patrol bots that need to be repaired.{/}"
    if gn_damaged_bot_waiting==1:                        ## there is ALSO a bot waiting for space
      $temp_text=temp_text+"{bad} You also have another damaged patrol bot waiting for an available capsule or available space in storage.{/}"
  if reminder_needed==1:
    $temp_int=random.randint(1,3)                        ## random between 3 - use a bot patrol picture with each pair of bots shown in it
    if temp_int==1:
      $image_text="quests good_neighbors sgn_44"
    elif temp_int==2:
      $image_text="quests good_neighbors sgn_45"
    else:
      $image_text="quests good_neighbors sgn_46"
    "{size=-8} "  ## insert blank line before reminder
    $act.start_block("l:250 c:content_width-250")
    $action_image=image_text   
    center "{image=[action_image]@150x225}"
    $act.set_block("c")
    "[temp_text]"
    ## no 'end.block' needed, this will always be the last message
  return