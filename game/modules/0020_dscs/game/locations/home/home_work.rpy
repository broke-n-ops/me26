##=========INIT VARIABLES=========
init python:
  clerk_bot_new_assignment=0      ## 0.10.n - counter for bots just assigned

##============FUNCTIONS============

init python:
  def label_home_work_action_info(**kwargs):
    if now("night"):
      kwargs["action"]=None
      kwargs["cost"]=["{hint}night{/}"]
    else:
      kwargs["cost"]=[("energy",3),("time",0)]
    return kwargs

define home_work_repair_task_chance=20
define home_work_buy_part_chance=30

label home_work:
  $game_bg="home workspace"
  header "[home] - Working"

## 'Mission Manager' at beginning of "Work" to ensure bots cannot execute their roles
  call role_mission_manager_schedule  ## ADDED ON 0.7.n FOR 'Mission Manager' ROLE
  $home_work_extra=min(5,mc.energy)
  $home_work_skill=mc.mechanics.level+mc.electronics.level+mc.computers.level
  $mc.energy=0
  $assistants=active_bots_with_role_tag("clerk")

## 0.10.n change to avoid 'double dipping' roles

##  $print "clerk assistants BEFORE"
##  $print assistants
##  $print ""

  $clerk_bot_new_assignment=0               ## clear flag before starting
  $bot_count=0
  while bot_count<len(assistants):          ## go through assistants to remove ones just assigned
    $temp_bot=assistants[bot_count]
    if temp_bot[0].clerk_just_assigned==1:  ## if assigned role this turn
      $clerk_bot_new_assignment+=1          ## increment count of bots just assigned
##      $temp_bot[0].clerk_just_assigned=0    ## reset flag - MOVED TO REST, SLEEP, WORK
      $assistants.pop(bot_count)            ## remove bot from assistants - do not increment counter
    else:
      $bot_count+=1                         ## increment bot count for while loop

##  $print "clerks assigned this turn: ",clerk_bot_new_assignment
##  $print ""
##  $print "clerk assistants AFTER"
##  $print assistants
##  $print ""

## 0.10.n end of insertion

  $assistants_bonus=sum((assistant.bot_social.level*role_efficiency for assistant,role_efficiency in assistants))
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""                                                                ## line feed between pictures
  $mgr_imagenumber=random.randint(8,13)                             ## Mission Manager images 8-13 - MC working in shop
  $action_image="roles mission_manager rmgr_"+str(mgr_imagenumber)
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  ""                                                                ##line feed between text
  "You open your shop and help the clients who come in. Once in a while someone brings in a damaged bot for repair or a part they want to sell."

  if home_work_extra:
    extend " {mark}You have extra energy and earn more money by serving more clients.{/}"
  ""                                           ## added a line feed before talking about clerk or lack of clerk activities

##  if assistants and assistants_bonus>0:      ## original line, will separate pictures and text, same pictures different text for bonus
  if assistants:                               ## re-use a subset of the 'Shopkeeper' images as 'Clerk' images
    $assistant=randchoice(assistants)[0]
    $act.set_block("l")
    ""                                         ## line feed between pictures
    if assistant.gender=="female":
      $mgr_imagenumber=random.randint(1,8)     ## Shopkeeper images 1-8 omit female bots selling parts
    else:
      $mgr_imagenumber=random.randint(17,20)   # Shopkeeper' images 17-20 omit male bot selling parts
    $action_image="roles shopkeeper srsk_"+str(mgr_imagenumber)
    center "{image=[action_image]@400x600}"
    $act.set_block("c")
    if assistants_bonus>0:
      if len(assistants)>1:
        "While you're handling repairs {mark}[assistant]{/} and your other clerk bots handled clients. This improved your reputation and freed time for actual work."
      else:
        "While you're handling repairs {mark}[assistant]{/} handled clients. This improved your reputation and freed time for actual work."
    else:    ##  Assistants but no bonus - NOT SURE THIS CAN HAPPEN!!
      if len(assistants)>1:
        "Unfortunately {mark}[assistant]{/} and your other clerk bots weren't good at handling clients so you couldn't get much real work done."
      else:
        "Unfortunately {mark}[assistant]{/} wasn't good at handling clients so you couldn't get much real work done."
  else:         ##  NO ASSISTANTS
    $act.set_block("l")
    ""                                                                ## line feed between pictures
    $mgr_imagenumber=random.randint(2,7)                              ## Mission Manager images 2-7 - no clerk bots, MC 'clerking'
    $action_image="roles mission_manager rmgr_"+str(mgr_imagenumber)
    center "{image=[action_image]@400x600}"
    $act.set_block("c")

## 0.10.n add comment if techies just assigned only when there are no assistants
    if not assistants:
      if clerk_bot_new_assignment==0:
        "Maybe I should have {mark}Clerk{/} bots and keep them at home in capsules so they can help be with customers."
      elif clerk_bot_new_assignment==1:
        "I just assigned a bot the {mark}Clerk{/} role so in the future they can handle customers and I can get more work done."
      elif clerk_bot_new_assignment>1:
        "I just assigned bots the {mark}Clerk{/} role so in the future they can handle customers and I can get more work done."

## 0.12.n new setting in 'Game' to allow a concise display when working
  if hide_full_description():
##    $notify.disable()
    $notify.disable("stat_xp_granted")
##    $notify.disable("stat_level_changed")
    $notify.disable("stat_learned")
    $notify.disable("stat_unlearned")
    $notify.disable("chassis_part_integrity_changed")
    $notify.disable("chassis_part_defect_added")

  python hide:
    work_money=randint(50,500+100*home_work_extra+50*assistants_bonus)+50*home_work_skill
    mc.money+=work_money                                     ## moved here so it's above rep and other info
    mc.give_xp("mood",randint(-150+3*assistants_bonus,-15))
    mc.give_xp("mechanics",max(0,randint(-250,500+50*home_work_extra+25*assistants_bonus)))
## 0.11.3 increase electronics gain when working
##    mc.give_xp("electronics",max(0,randint(-150,250+25*home_work_extra+10*assistants_bonus)))
    mc.give_xp("electronics",max(0,randint(-200,375+38*home_work_extra+18*assistants_bonus)))
    mc.give_xp("computers",max(0,randint(-150,250+25*home_work_extra+10*assistants_bonus)))

## 0.12.0 change mechanic and hacker rep gains, customers notice your techie bots working and think you're a pretty good 'TechBot Trainer' trainer
    techie_bots=active_bots_with_role_tag("techie")
    bot_count=0
    while bot_count<len(techie_bots):                  ## go through techie_bots to remove ones just assigned
      temp_bot=techie_bots[bot_count]
      if temp_bot[0].tech_just_assigned==1:            ## if assigned role this turn
##        tech_just_assigned+=1                          ## 0.12.6 removed, no flag variable for techies and reset in 'clear_role_flags.rpy'  
        techie_bots.pop(bot_count)                     ## remove bot from techie_bots, no need to increment counter since this one was removed
      else:
        bot_count+=1                                   ## increment bot count for while loop
    if len(techie_bots)>2:                             ## 3 or more techie bots
      temp=calc_pr_rep_gain("rep_mc_mechanic","m_g")   ## medium gain
      mc.give_xp("rep_mc_mechanic",temp)        
      temp=calc_pr_rep_gain("rep_mc_hacker","m_g")     ## medium gain
      mc.give_xp("rep_mc_hacker",temp)
    elif len(techie_bots)==2:                          ## 2 techie bots
      temp=calc_pr_rep_gain("rep_mc_mechanic","s_g")   ## small gain
      mc.give_xp("rep_mc_mechanic",temp)        
      temp=calc_pr_rep_gain("rep_mc_hacker","s_g")     ## small gain
      mc.give_xp("rep_mc_hacker",temp)
    elif len(techie_bots)==1:                          ## 1 techie bot
      temp=calc_pr_rep_gain("rep_mc_mechanic","xs_g")  ## extra small gain
      mc.give_xp("rep_mc_mechanic",temp)        
      temp=calc_pr_rep_gain("rep_mc_hacker","xs_g")    ## extra small gain
      mc.give_xp("rep_mc_hacker",temp)
    else:                                              ## no techie bots, they only see you working
      temp=calc_pr_rep_gain("rep_mc_mechanic","xs_g")  ## extra small gain
      temp=3+temp//2                                   ## even smaller gain
      mc.give_xp("rep_mc_mechanic",temp)
      temp=calc_pr_rep_gain("rep_mc_hacker","xs_g")    ## extra small gain
      temp=3+temp//2                                   ## even smaller gain
      mc.give_xp("rep_mc_hacker",temp)
## old code
##    mc.give_xp("rep_mc_mechanic",max(0,randint(-25,15+assistants_bonus)))   ## ORIGINAL FUNCTION
##    mc.give_xp("rep_mc_hacker",max(0,randint(-25,15+assistants_bonus//2)))  ## ORIGINAL FUNCTION

##    mc.money+=work_money  ##  moved ahead of other notifications
    for assistant,role_efficiency in assistants:
      assistant.give_xp("bot_social",max(0,randint(-75,10*assistants_bonus)))
  $assistant=None
  $assistants=None
  call role_housekeeper_clean         ## 0.2.2 housekeepers clean while you work- bug fix v0.4.1 - work used previous housekeeper bonus instead of calculating a new one
  call role_bot_trainer_train         ## 0.12.n bot trainer role trains other bots, must be before 'master techie'
  call role_senior_techie_repair      ## 0.9.n senior techie role repairs parts in inventory, must be before 'master techie'
  call role_master_techie_repair      ## 0.6.n master techie role repairs other bots
  call capsule_stability_increase     ## 0.6.n capsule upgrade increasing bot stability
## 0.10.n text about shopkeepers when working
  call role_shopkeeper_help_run_shop  ## 0.10.n show messages about shopkeepers when working (text only!)
  $act.end_block()                    ## this resets the 2 column screen to a single screen
## 0.12.n new setting in 'Game' to allow a concise display when working
  if hide_full_description():
##    $notify.enable()
    $notify.enable("stat_xp_granted")
##    $notify.enable("stat_level_changed")
    $notify.enable("stat_learned")
    $notify.enable("stat_unlearned")
    $notify.enable("chassis_part_integrity_changed")
    $notify.enable("chassis_part_defect_added")
## 0.10.n clear flags for role delay feature at end of turn
  call clear_role_delay_flags
  call random_event("home_work")
  if _return=="default":
  ## ADD IN 0.8.n
    call random_event("good_neighbor")   ## if no 'home_work' event try for a 'good_neighbor' event
    if _return=="default":               ## if no 'good_neighbor' event advance time - EVENTS MUST END WITH 'advance_time' FUNCTION CALL
      choice("advance_time") "Continue"  ## existing line with altered indentation
  return