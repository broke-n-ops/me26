##=========INIT VARIABLES=========  NOT SURE THIS IS NECESSARY
init python:

## FOLLOWING LINE NOT NEEDED AFTER TESTING - VARIABLE 'housekeeper_staff' CAN BE COMMENTED OUT
##  housekeeper_staff=0         ##  number of available housekeepers
  housekeeper_count=0         ##  counter to loop through bots using 'while'
  housekeeper_bonus=0         ##  counter for AP gain or loss
  next_turn_string=""         ##  string for "this morning", "this afternoon", "this evening", "tonight"
  housekeeper_call_from=0     ##  to know where the call came from since I can't figure out parameters: 0-sleep, 1-rest
  hskpr_min=0                 ##  minimum psychocore stability loss when working
  hskpr_max=5                 ##  maximum psychocore stability loss when working
  hskpr_actual=0              ##  actual psychocore stability loss

##============FUNCTION============

label role_housekeeper_clean:
  $housekeeper_count=0                                   ##  reset counter for 'while' loop
  $housekeeper_bonus=0                                   ##  reset counter for AP gain or loss
  $assistants=active_bots_with_role_tag("housekeeper")   ##  find all active housekeeper bots
  if now.tod_name=="Morning":
    if housekeeper_call_from==0:                         ##  value when set from sleep
      $next_turn_string="this morning"
    elif housekeeper_call_from==1:                       ##  value when set from rest
      $next_turn_string="this afternoon"
  elif now.tod_name=="Afternoon":
    $next_turn_string="this evening"
  elif now.tod_name=="Evening":
    $next_turn_string="tonight"
  else:               ##  must be night!
    $next_turn_string="this morning"

## FOLLOWING 3 LINES NOT NEEDED AFTER TESTING - VARIABLE 'housekeeper_staff' CAN BE COMMENTED OUT
##  $housekeeper_staff=len(assistants)                     ##  number of housekeeper bots
##  ""
##  "Staff: [housekeeper_staff]"

##  $print "assistants 1:"
##  $print assistants

  if assistants:
    python:
      for assistant,role_efficiency in assistants:
        housekeeper_count+=1                       ##  add 1 to count
        if assistant.psychocore.stability>=75:     ##  cutoff for 'stable'
          housekeeper_bonus+=1                     ##  add 1 AP next turn
        elif assistant.psychocore.stability<25:    ##  cutoff for 'unstable'
          housekeeper_bonus-=1                     ##  subtract 1 AP next turn

##    "housekeeper_count: [housekeeper_count]"       ##  these 2 lines are for testing only
##    "housekeeper_bonus: [housekeeper_bonus]"

##  apply limit based upon game difficulty setting: easy(1)=5, normal(2)=4, hard(3)=3, hardcore(4)=2
  $housekeeper_bonus=min(6-game.difficulty,housekeeper_bonus)

##  bonus is applied in 'mc.rpy' whenever time advances, flavor text follows

##  $print "assistants 2:"
##  $print assistants

  if assistants:
    $assistant=randchoice(assistants)[0]    ##  select 1 to use by name

##    "Chosen Housekeeper: [assistant]"       ##  this line is for testing

##  set up columns and display a rendom housekeeper picture on the left
##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    if assistant.gender=="female":
      $hk_imagenumber=random.randint(1,8)
    else:
      $hk_imagenumber=random.randint(9,16)
    if not now("night"):
      ""
##      ""
    $action_image="roles housekeeper srhk_"+str(hk_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
##  TEXT
    $act.set_block("c")
    if not now("night"):     ## line feeded except at night
      ""
##      ""
    if housekeeper_bonus>0:                                     ##  AP increase from housekeepers
      if housekeeper_count==1:                                  ##  one housekeeper
        "My housekeeper bot {mark}[assistant]{/} is great!"
        "{good}1 extra AP [next_turn_string]!{/}"
      else:
        "{mark}[assistant]{/} and my other housekeeper bots are great!"
        "{good}[housekeeper_bonus] extra AP [next_turn_string]!{/}"
    elif housekeeper_bonus<0:                                   ##  AP decrease from housekeepers
      if housekeeper_count==1:                                  ##  one housekeeper
        "My housekeeper bot {mark}[assistant]{/} is unstable, I need to fix that!"
        "{bad}1 less AP [next_turn_string].{/}"
      else:
        "Some of my housekeeper bots are unstable, I need to fix that!"
        "{bad}[housekeeper_bonus] less AP [next_turn_string].{/}"
    else:                                                       ##  no change to AP from housekeepers
      if housekeeper_count==1:                                  ##  one housekeeper
        "My housekeeper bot {mark}[assistant]{/} is not stable, I should fix that!"
      else:
        "Some of my housekeeper bots are unstable, I should fix that!"
  else:                                                        ##  no housekeepers
##  set up columns and display a rendom housekeeper picture on the left
##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $hk_imagenumber=random.randint(17,24)
    if not now("night"):                  ## at night no line feed needed
      ""
    $action_image="roles housekeeper srhk_"+str(hk_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
##  TEXT
    $act.set_block("c")
    if not now("night"):                  ## at night no line feed needed
      ""
    "Maybe I should have {mark}Housekeeper{/} bots and keep them at home in capsules. That would give me more time to get things done."

##  give all housekeepers a social skill boost proportional to their stability and reduce their stability

##  $print "assistants 3:"
##  $print assistants

  if assistants:
    python:
        
##      print now.dow_name,now.tod_name
##      print "housekeeper assistants"
##      print assistants
##      print "Chosen Housekeeper: ",assistant

      for assistant,role_efficiency in assistants:
        upper_limit=int(assistant.psychocore.stability/8)
        assistant.give_xp("bot_social",randint(1,upper_limit))

##        print "upper limit: [upper_limit]"

        hskpr_actual=randint(hskpr_min,hskpr_max)    ## values 0,5 (v0.6.0)

##        print "housekeeper stability loss: ",assistant,hskpr_actual

        hskpr_actual=int(hskpr_actual*assistant.psychocore_stability_decay_mult)

##        print hskpr_actual

        if hskpr_actual<assistant.psychocore.stability:  ##  decrease stability but not <1
          assistant.psychocore.stability-=hskpr_actual

##      print ""

##  clean up
  $assistant=None
  $assistants=None
  ""                  ## add space before next item is displayed: housekeeper, master_techie, shopkeeper
  return