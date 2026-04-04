## 0.13 BOT MONITOR INTRODUCED
## 0.14 MAJOR UPGRADE TO BOT MONITOR: tinker and stabilize buttons for each bot within bot monitor

## bot monitor licenses purchased using 'Monitor' button on 'Capsules' screen, client software automatically installed
## background image is computer screen
## flag for bot monitor installed is in the 'workshop_upgrade.rpy' file

## flag variable to allow bot interactions
init python:
  using_bot_monitor=0          ## set to 1 when inside bot monitor, reset to 1 after call statement
  last_capsule=0               ## set to 1 when displaying last capsule to avoid extra space after
  bm_bot_integrity=""          ## colorized string with value of bot's integrity
  bm_bot_stability=""          ## colorized string with value of bot's stability
  bm_integrity_minimum=1       ## integrity minimum based upon assignments (tasks), OBSOLETE - keep in to avoid potential save integrity problem
  bm_stability_minimum=1       ## stability minimum based upon assignments (tasks), OBSOLETE - keep in to avoid potential save integrity problem

## 0.15.1 variable used in screen companion file
  bm_defective_bot=-1

##=====MAIN FUNCTION=====

label bot_monitor_software(page_number_str):
  $page_number=int(page_number_str)
  $global last_capsule
  $global using_bot_monitor
  $using_bot_monitor=1
  $game_bg="home bot_monitor"
  header "{size=-4}Bot Monitor{/}"
  
## display 5 bots at a time on up to 4 screens
## exception: withe 6 capsules display all, no pages

  $bot=[]
  if home.max_sexbots<=6:                             ## if 6 or less capsules display them all
    $while_counter=0
    $while_end=home.max_sexbots                         
  else:                                               ## if more than 6 capsules display 5 at a time
    $while_counter=page_number*5                      ## first bot to display: 0, 5, 10, 15
    $while_end=while_counter+5
  if while_end>home.max_sexbots:                      ## cannot display capsules you don't have
    $while_end=home.max_sexbots  
  call find_minimums()                                ## get the integrity and stability minimums for ALL BOTS
  $act.add_screen("draw_divider")                     ## divider line above first bot
  while while_counter<while_end:
    if while_counter+1!=while_end:
      $last_capsule=0
    else:
      $last_capsule=1
    $act.start_block("l:220 c:content_width-220")                                        ## needs to be reset each time because divider needs to clear it    
    $bot=find_character(home.sexbots[while_counter])                          
    if bot:                                                                              ## bot may be None if capsule empty

##0.15.1 insert:  determine if the bot is defective and if bot monitor notices
      $global db_psychocore_decay
      $global bm_defective_bot
      $bm_defective_bot=0                                                                ## assume normal bot OR defective bot not noticed
      $temp_int=random.randint(1,10)                                                     ## for random chance of displaying 'Read Error' on defective bot

##      $print "bot: ",bot,"  psychocore_stability_decay: ",bot.psychocore_stability_decay_mult,"  temp_int: ",temp_int

      if bot.psychocore_stability_decay_mult==db_psychocore_decay and temp_int<=2:       ## identifies defective bot and displays error 20% of the time
##      if bot.psychocore_stability_decay_mult==db_psychocore_decay:                       ## FOR TESTING ONLY! identifies defective bot and displays error all the time

        $bm_defective_bot=1                                                                  ## defective bot noticed, flag used to set stability reading to 'Read Error'
## end of insert          

      $bm_repairable_bot=bot_monitor_repairable_bot(bot)                                 ## if bot has irrepairable, destroyed, or missing parts don't allow Tinker and Stabilize button because parts must be replaced
      if bot_monitor_status[while_counter]==0:                                           ## bot monitor not active (licensed)
        $act.set_block("l")
        $act.add_screen("avatar_inactive_buttons",bot)
        $act.set_block("c")
        $act.add_screen("bot_monitor_inactive",bot,while_counter+1)                      ## to display text saying bot monitor is not active on this capsule, while_counter+1 is capsule number
        $button_title="C"+str(while_counter+1)+"-"+bot.name
        choice(None,hint=bot.model_name) "[button_title]"
      elif bot["mission"]:                                                               ## bot on mission, cannot monitor
        $act.set_block("l")
        $act.add_screen("avatar_inactive_buttons",bot) 
        $act.set_block("c")
        $act.add_screen("bot_on_mission",bot,while_counter+1)                            ## to display text saying bot is on a mission and cannot be monitored, while_counter+1 is capsule number
        choice(None,hint="(bot on mission)") "[button_title]"  
      elif bm_repairable_bot==0:                                                         ## bot has irrepairable, destroyed, or missing parts and cannot be tinkered within bot monitor
        $act.set_block("l")
        $act.add_screen("avatar_inactive_buttons",bot) 
        $act.set_block("c")
        $act.add_screen("replace_parts",bot,while_counter+1)                             ## to display text saying bot is on a mission and cannot be monitored, while_counter+1 is capsule number
        $button_title="C"+str(while_counter+1)+"-"+bot.name
        choice(">>>begin_bot_interaction:"+bot.id,hint="(replace parts)") "[button_title]" 
      else:                                                                              ## monitor active on capsule and bot not on mission
        $act.set_block("l")
        $act.add_screen("avatar_repair_buttons",bot,page_number_str,bm_defective_bot)
        $act.set_block("c")
        $act.add_screen("bot_information_text",bot,while_counter+1,page_number_str,bm_defective_bot)
        $button_title="C"+str(while_counter+1)+"-"+bot.name
        choice(">>>begin_bot_interaction:"+bot.id,hint=bot.model_name) "[button_title]" 
    else:                                                                                ## no bot in the capsule
      if bot_monitor_status[while_counter]==1:                                           ## capsule is licensed
        $act.set_block("c")
        $act.add_screen("empty_capsule",while_counter+1,)                               ## while_counter+1 is capsule number, 1 parameter means capsule IS licensed
      else:                                                                              ## capsule NOT licensed
        $act.set_block("c")
        $act.add_screen("empty_capsule",while_counter+1)                               ## while_counter+1 is capsule number, 0 parameter means capsule IS NOT licensed
      $button_title="C"+str(while_counter+1)+"-"+"Empty"
      choice(None) "[button_title]"
    $act.end_block()
    $act.add_screen("draw_divider")                                                      ## divider line below bot
    $while_counter+=1
## create page buttons only if more than 6 capsules
  if home.max_sexbots>6:
    if page_number==0:
      choice(None, pos=12) "Capsules 1-5"
      choice("bot_monitor_software:1",key="b",pos=13) "Capsules 6-10"
      if home.max_sexbots>10:
        choice("bot_monitor_software:2",key="c",pos=14) "Capsules 11-15"
      if home.max_sexbots>15:
        choice("bot_monitor_software:3",key="d",pos=15) "Capsules 16-20"
    elif page_number==1:
      choice("bot_monitor_software:0",key="a", pos=12) "Capsules 1-5"
      choice(None,pos=13) "Capsules 6-10"
      if home.max_sexbots>10:
        choice("bot_monitor_software:2",key="c",pos=14) "Capsules 11-15"
      if home.max_sexbots>15:
        choice("bot_monitor_software:3",key="d",pos=15) "Capsules 16-20"
    elif page_number==2:
      choice("bot_monitor_software:0",key="a", pos=12) "Capsules 1-5"
      choice("bot_monitor_software:1",key="b",pos=13) "Capsules 6-10"
      if home.max_sexbots>10:
        choice(None,pos=14) "Capsules 11-15"
      if home.max_sexbots>15:
        choice("bot_monitor_software:3",key="d",pos=15) "Capsules 16-20"
    elif page_number==3:
      choice("bot_monitor_software:0",key="a", pos=12) "Capsules 1-5"
      choice("bot_monitor_software:1",key="b",pos=13) "Capsules 6-10"
      if home.max_sexbots>10:
        choice("bot_monitor_software:2",key="c",pos=14) "Capsules 11-15"
      if home.max_sexbots>15:
        choice(None,pos=15) "Capsules 16-20"
  choice("bot_monitor_help:"+page_number_str,key="h",pos=16) "Help"
  choice("<<<",key="cancel",pos=17) "Done"
  return

##=====SUPPORTING FUNCTIONS=====

label find_minimums():                                       ## find minimums based upon assignment: trainee, managed, roles for all bots in capsules
  python:
    for bot in home.sexbots:
      if bot:
        tmp_int=1
        tmp_stab=1
        if bot.trainee_subject!="never" or bot.allow_manage:
          tmp_int=75
          tmp_stab=75
        for role in bot.roles:
          if role.id=="master_techie" or role.id=="senior_techie" or role.id=="bot_trainer" or role.id=="mission_manager":
            tmp_int=90
            tmp_stab=75
          elif role.id=="housekeeper":
            tmp_stab=75
        bot.task_req_integrity=tmp_int
        bot.task_req_stability=tmp_stab
  return

init python:

## used to determine if a bot can be tinkered within bot monitor: must have no irrepairable, destroyed, or missing parts
  def bot_monitor_repairable_bot(bot):
    temp_value=1                                   ## assume bot is repairable
    for slot,part in sorted(bot.outfit.items()):
      if part.has_irrepairable_defects or part.is_destroyed or part.damage_on_remove=="missing":
        temp_value=0
    return temp_value

## used to colorize the actual integrity and stability
  def colorize_percent_string(t_string,t_value):
    r=(100-t_value)/100.0
    g=t_value/100.0
    b=0
    return "{color="+Color(rgb=(r,g,b)).hexcode+"}"+t_string+"{/}"

## used to colorize the required integrity and stability 
  def colorize_required_percent_string(act_value,req_value):
    if act_value>req_value+6:    ## > 6 above requirement - green
      r=0.0
      g=1.0
      b=0.0
    elif act_value>req_value+3:  ## 4-6 above requirement - yellow
      r=0.9
      g=0.9
      b=0.2
## 0.14 changed > to >= because equal should not be red
    elif act_value>=req_value:   ## 0-3 above requirement - orange
      r=0.9
      g=0.45
      b=0.0
    else:                       ## below requirement - red
      r=1.0
      g=0.0
      b=0.0
    temp_str=str(req_value)+"%"
    while len(temp_str)<4:
      temp_str=" "+temp_str
    temp_str="{color="+Color(rgb=(r,g,b)).hexcode+"}"+temp_str+"{/}"  
    return temp_str

##=====TINKER FUNCTIONS=====

label bm_repair_bot(pass_string):                            ## contains bot_id, space, page_number_str
  $repair_part=""
  $defect_part=""
  $bots=[]
  $bot_id,page_number_str=pass_string.split(" ")
  $bot=find_character(bot_id)
  $integrity=100                                             ## will be replaced with integrity of lowest part
  if bot:
    python:
      for slot,part in sorted(bot.outfit.items()):           ## first find a defect just in case, then find repairable bot
        ## next 4 lines copied verbatim from 'workshop_fix_random_bot.rpy
        defects=[(defect_n,defect) for defect_n,defect in enumerate(part.defects)]
        if defects:
          defects.sort(key=lambda x: (100-x[1].integrity_cap,x[1].fix_progress))
          if defects[-1][1].repairable:
            defect_part=part
            fix_defect=defects[-1][0]
        if part.integrity<part.integrity_cap and part.rate:  ## integrity_cap is max integrity for a part with defect(s), part.rate is false for 'missing parts'
          if integrity>part.integrity:                       ## new candidate for lowest integrity part
            integrity=part.integrity                         ## new threshold for comparison of remaining parts                    
            repair_part=part
  if integrity<100:                                          ## repairable part found, otherwise defects prevent repair                   
    call fix_bot_part_silent(bot,repair_part.slot.id)
  elif bot:                                                  ## no repairable part, fix a defect instead
    call fix_bot_part_defect_silent(bot,defect_part.slot.id,fix_defect)
  return ("bot_monitor_software:"+page_number_str)

label fix_bot_part_silent(bot,part_id):                ## copy from interact_tinker.rpy removing text and buttons
  $notify.disable()                                    ## turn notifications off for silence
  $part=bot.chassis[part_id]
  $assistants=active_bots_with_role_tag("techie",bot)  ## Note: 'assistants' list never includes bot being repaired

##  $print "assistants complete list"
##  $print assistants
##  $print

## next 9 lines remove bots just assigned from 'assistants'
  $tech_bot_new_assignment=0                           ## reset counter added in 0.10.n
  $bot_count=0
  while bot_count<len(assistants):                     ## go through assistants to remove ones just assigned
    $temp_bot=assistants[bot_count]
    if temp_bot[0].tech_just_assigned==1:              ## if assigned role this turn
      $tech_bot_new_assignment+=1                      ## increment count of bots just assigned
      $assistants.pop(bot_count)                       ## remove bot from assistants - do not increment counter
    else:
      $bot_count+=1                                    ## increment bot count for while loop
## end removing bots just assigned

##  $print "assistants after removing just assigned and fixing self"
##  $print assistants
##  $print

  $assistants_bonus=sum(((assistant.bot_electronics.level+assistant.bot_mechanics.level)*role_efficiency for assistant,role_efficiency in assistants))/2.0
  python:
    progress=mc.calc_part_repair_progress(bot,part,assistants_bonus)
    progress=min(part.integrity_cap,part.integrity+progress)-part.integrity
    part.integrity+=progress
    base_xp_reward=int(progress*part.difficulty)
    skill_xp_reward=int(base_xp_reward*2)
  python hide:
    skills=[(getattr(mc,skill).level,weight) for skill,weight in part.repair_skills]
    total_weight=sum((weight for level,weight in skills))
    for skill,weight in part.repair_skills:
      mc.give_xp(skill,skill_xp_reward*weight//total_weight)
    mc.give_xp("expertise_"+bot.model_id,base_xp_reward)
##  fix in version 0.0.6 to prevent gaining expertise in a 'missing part' - part.rate for missing parts is "", all others are FEDCBAS
##  this line gives part expertise, make it conditional
    if part.rate<>"":
      mc.give_xp("expertise_"+part.id,base_xp_reward)
    for assistant,role_efficiency in assistants:
      assistant.give_xp("bot_mechanics",max(0,randint(-75,25)))
      assistant.give_xp("bot_electronics",max(0,randint(-100,25)))
  $assistant=None
  $assistants=None
  $part=None
  $mc.energy-=1                                       ## cost is 1 AP
  $notify.enable()                                    ## turn notifications back on when done
  return

label fix_bot_part_defect_silent(bot,part_id,defect):     ## copy from interact_tinker.rpy removing text and buttons
  $notify.disable()                                       ## turn notifications off for silence
  $part=bot.chassis[part_id]
  $defect=part.defects[defect]
  $assistants=active_bots_with_role_tag("techie",bot)     ## Note: 'assistants' list never includes bot being repaired

##  $print "assistants complete list"
##  $print assistants
##  $print

## next 9 lines remove bots just assigned from 'assistants'
  $tech_bot_new_assignment=0                              ## clear flag before starting
  $bot_count=0
  while bot_count<len(assistants):                        ## go through assistants to remove ones just assigned
    $temp_bot=assistants[bot_count]
    if temp_bot[0].tech_just_assigned==1:                 ## if assigned role this turn
      $tech_bot_new_assignment+=1                         ## increment count of bots just assigned
      $assistants.pop(bot_count)                          ## remove bot from assistants - do not increment counter
    else:
      $bot_count+=1                                       ## increment bot count for while loop
## end removing bots just assigned

##  $print "assistants after removing just assigned and fixing self"
##  $print assistants
##  $print

  $assistants_bonus=sum(((assistant.bot_electronics.level+assistant.bot_mechanics.level)*role_efficiency for assistant,role_efficiency in assistants))/2.0
  python:
    progress=mc.calc_part_defect_repair_progress(bot,part,defect,assistants_bonus)
    progress=min(100,defect.fix_progress+progress)-defect.fix_progress
    defect.fix_progress+=progress
    base_xp_reward=int(progress*part.difficulty*defect.difficulty)
    skill_xp_reward=int(base_xp_reward*2)
  if defect.fix_progress==100:
    $part.defects.remove(defect)
  python hide:
    skills=[(getattr(mc,skill).level,weight) for skill,weight in part.repair_skills]
    total_weight=sum((weight for level,weight in skills))
    for skill,weight in part.repair_skills:
      mc.give_xp(skill,skill_xp_reward*weight//total_weight)
    mc.give_xp("expertise_"+bot.model_id,base_xp_reward)
##  fix in version 0.0.6 to prevent gaining expertise in a 'missing part' - part.rate for missing parts is "", all others are FEDCBAS
##  this line gives part expertise, make it conditional
    if part.rate<>"":
      mc.give_xp("expertise_"+part.id,base_xp_reward)

    for assistant,role_efficiency in assistants:
      assistant.give_xp("bot_mechanics",max(0,randint(-75,25)))
      assistant.give_xp("bot_electronics",max(0,randint(-100,25)))
  $assistant=None
  $assistants=None
  $part=None
  $defect=None
  $defects=None
  $mc.energy-=1                                           ## cost is 1 AP
  $notify.enable()                                        ## turn notifications back on when done
  return

##=====STABILIZE FUNCTION=====

label bm_stabilize_bot(pass_string):
  $notify.disable()                                    ## turn notifications off for silence
  $bot_id,page_number_str=pass_string.split(" ")
  $bot=find_character(bot_id)
  if bot:
    python:
      progress=mc.calc_stability_progress(bot)
      
##      print "progress: ",progress

      progress=min(100,bot.psychocore.stability+progress)-bot.psychocore.stability
      
##      print "adjusted progress: ",progress

      base_xp_reward=progress
      skill_xp_reward=int(base_xp_reward*2)
    $bot.psychocore.stability+=progress
    python:
      mc.give_xp("computers",skill_xp_reward)
      mc.give_xp("expertise_"+bot.model_id,base_xp_reward)  ## only change in 0.14.1 is a bug fix changing "bot_target.model_id" to "bot.model_id" (was a copy paste error)
  $mc.energy-=1                                             ## cost is 1 AP
  $notify.enable()                                          ## turn notifications back on when done
  return ("bot_monitor_software:"+page_number_str)

##====HELP FUNCTIONS=====

label bot_monitor_help(page_number_str):
  $game_bg="home bot_monitor"
  header "{size=-4}Bot Monitor - Help{/}"
  $act.add_screen("draw_divider")
  "{size=-16} {/}"
  "{size=-2}{mark}Tinker (1AP): {/}{mcsay}At a cost of 1 AP each time the button is pressed the lowest integrity part on the bot will be tinkered with: either repaired (integrity) or fixed (defects).{/}{/}"
  "{size=-16} {/}"
  "{size=-4}{mark}Tinker Details: {/}{mcsay}The lowest integrity part will be repaired each time until it reaches 100%% integrity unless the part has one or more defects. If the part has defects it will be repaired until it reaches the integrity cap for the defect (typically 75%%). When the cap is reached the part will be fixed to remove the defect(s). {mark}Important! Unfortunately 'Bot Monitor' is unable to report the status of defects. To monitor progress when fixing defects you must interact with the bot using the buttons below the screen.{/} After the part's defect(s) are fixed the part will be repaired until it reaches 100%% integrity.{/}{/}" 
  "{size=-2} {/}"
  "{size=-2}{mark}Stabilize (1AP): {/}{mcsay}At a cost of 1 AP each time the button is pressed the bot will be hacked to increase the stability until it is 100%% stable.{/}{/}"
  "{size=-2} {/}"
  "{size=-2}{mark}Duties Require: {/}{mcsay}This is the level of integrity/stability required for the bot to perform all of it's rolls and assignments (being managed and/or trained by other bots).{/}{/}"
  "{size=-16} {/}"
  $act.add_screen("draw_divider")

##  $print "inside help for bot monitor"

  choice("bm_close_help:"+page_number_str) "Close"
  return

label bm_close_help(page_number_str):
  return ("bot_monitor_software:"+page_number_str)