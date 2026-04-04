## needs to be saved in games so it cannot be inside 'init python' block and cannot be 'define'
default capsule_upgrade_status={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0}  ## dict with upgrade level of each capsule, status is 0,1,2,3,4 for 4 levels of upgrade at various costs
## 0.12.8 add for 'Bot Monitor' software upgrade
default bot_monitor_status={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0}     ## dict with 0 or 1 for 'Bot Monitor' software license purchased
default bot_monitor_installed=0    ## set to 1 when the software is installed, influences text displayed

##==========initialize variables==========

init python:
  selected_capsule=0           ## which capsule the user selected to upgrade
  capsule_upgrade_1=8000       ## total cost 8K
  capsule_upgrade_2=12000      ## total cost 20K
  capsule_upgrade_3=30000      ## total cost 50K
  capsule_upgrade_4=75000      ## total cost 125K
  sr24_power_level=1           ## 4 levels:  1=max 6 capsules, 2=max 10, 3=max 15, 4=max 20
  sr24_max_capsules=6          ## created to replace every use of "max_sexbot_capsules" which was defined in 'home'rpy' but is no longer used
  sr24_power_upgrade_counter=0 ## countdown from payment for power upgrade until it takes place
  bot_monitor_license=2000     ## 0.12.8 cost to have a capsule added to the 'Bot Monitor' software


##===================BORDER WITH EVENT HANDLING FUNCTION===================

##=== daily notice of power upgrade status ===
init python hide:
  @event_handler("new_day")
  def power_upgrade_event():
    if sr24_power_upgrade_counter>0:         ## a power upgrade counter is in progress
      queue_event("upgrade_workshop_power")
  return

##==========functions==========

label workshop_upgrades:
  header "[workshop] - Upgrade"
  "Your workshop has plenty of room and you have all the basic tools you need but you can always use more space for bots."
  ""
  $temp=len(home.sexbots)
  "{mark}Capsules{/} are the best way to store bots that you use regularly. They are expensive and use a lot of power so each capsule increases the rent."
  extend " Capsules can be {mark}upgraded{/} with {mark}Psychocore Stabilizers{/} which use {mark}AI{/} to maintain bot psychocore stability. They are expensive but save a lot of time!"
  ""
  "The {mark}storage room{/} has plenty of beat up shelves for bots but you need {mark}Bot Support Systems{/}. Each system can support {mark}6 bots{/}. They are expensive but don't use much power. Bots in storage are offline but they are close by and safe."
  if workshop.max_sexbots==0:
    extend " You could buy {mark}Bot Support Systems{/} and keep bots you don't use regularly in the storage room."
    if mc.electronics<"D" or mc.mechanics<"D":
      extend " Unfortunately you lack the skills needed to install {mark}Bot Support Systems{/}. {info}Skills required: Mechanics: D+, Electronics: D+{/}"
  else:
    extend " There are enough {mark}Bot Support Systems{/} in the storage room to keep {mark}[workshop.max_sexbots] bots{/}"
    if workshop.available_space==1:
       extend " and right now you have space for {mark}one more bot{/}."
    elif workshop.available_space:
      extend " and right now you have space for {mark}[workshop.available_space] more bots{/}."
    else:
      extend". The storage space is full, you may want to buy another {mark}Bot Support System{/}."
  ""
  if sr24_max_capsules==len(home.sexbots):      ## you have as many capsules as the building supports
    if sr24_power_level==4:                     ## the building is at the highest power level
      "This old building has reached it's limit and can't handle another {mark}Power Upgrade{/}. It supports the 20 capsules you already own and that will have to be enough."
    else:                                       ## the building can still be upgraded
      "You own {mark}[sr24_max_capsules] capsules{/} which is all the building power capacity can support. You can ask the landlord for a {mark}Power Upgrade{/} to support more capsules if you're willing to pay for it."
  else:                                         ## the building has capacity for more capsules
    $temp1=len(home.sexbots)                    ## number of capsules you have
    $temp2=sr24_max_capsules-len(home.sexbots)  ## number of capsules you can still add at this power level
    if temp1==1:                                ## you have only 1 capsule
      "You have {mark}[temp1] capsule{/}"
    else:                                       ## you have more than 1 capsule
      "You have {mark}[temp1] capsules{/}"
    if temp2==1:                                ## the building capacity supports 1 more capsule
      extend " and the building can handle {mark}1 more capsule{/}."
    else:                                       ## the building capacity supports more than 1 capsule
      extend " and the building can handle {mark}[temp2] more capsules{/}."
    if sr24_power_level==4:                     ## the building is at the highest power level
      extend " The building cannot support another {mark}Power Upgrade{/} so 20 capsules is the most you can have."
    else:                                       ## the building can still be upgraded
      extend " Although you don't need it right now you can ask the landlord for a {mark}Power Upgrade{/} to support more capsules if you're willing to pay for it."
  if len(home.sexbots)<sr24_max_capsules:
    choice(">>>workshop_add_capsule") "Add bot capsule"
  else:
    choice(None,hint="{good}maxed{/}") "Add bot capsule"
  if workshop.max_sexbots==0:
    if mc.electronics>="D" and mc.mechanics>="D":
      choice(">>>workshop_start_storage",cost=[("energy",3),("money",5000)]) "Add storage"
    else:
      choice(None,hint="{hint}low skill{/}") "Add storage"
  else:
    if workshop.max_sexbots<workshop_sexbots_storage_max_space:
      choice(">>>workshop_add_storage",cost=[("energy",3),("money",5000)]) "Add storage"
    else:
      choice(None,hint="{good}maxed{/}") "Add storage"
  if sr24_power_level<4:                                                                  ## upgrade available
    if sr24_power_upgrade_counter!=0:                                                     ## an upgrade is in progress, cannot order another one
      choice(None,hint="(upgrade pending)") "Power Upgrade"
    elif sr24_power_level==1:
      choice(">>>workshop_increase_power_level",cost=[("money",125000)]) "Power Upgrade"  ## $125K for level 2
    elif sr24_power_level==2:
      choice(">>>workshop_increase_power_level",cost=[("money",250000)]) "Power Upgrade"  ## $250K for level 3
    elif sr24_power_level==3:
      choice(">>>workshop_increase_power_level",cost=[("money",500000)]) "Power Upgrade"  ## $500K for level 4
  else:                                                                                   ## no upgrades available
    choice(None,hint="(building at max)") "Power Upgrade"
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

init python:
  def label_workshop_add_capsule_action_info(**kwargs):
    if now("night"):
      kwargs["action"]=None
      kwargs["cost"]=["{hint}night{/}"]
    else:
      upgrade_cost=min(2000+home.max_sexbots*1000,8000)
      kwargs["cost"]=[("money",upgrade_cost),("energy",3)]
    return kwargs

label workshop_add_capsule:
  header "[workshop] - Add SexBot Capsule"
  "You connect to the local market network and order a {mark}Standard Bot Capsule{/}."
  ""
  "After installing and thoroughly testing it, you plug it into the workshop network."
  ""
  "This give me space to have another fully active bot!"
  ""
  $home.sexbots.append(None)
  "Now you have {mark}[home.max_sexbots_str]{/}."
  $home.update_expenses()
  "Expenses updated."
  choice("<<<") "Continue"
  return

label workshop_start_storage:
  header "[workshop] - Prepare SexBot Storage"
  "You connect to the local market network and buy a {mark}Bot Support System{/}."
  ""
  "You set it up between two shelving units in the storage soom and connect it to the main workshop line."
  ""
  "Unfortunately bots stored here will be offline but at least I can own more bots."
  ""
  $workshop.sexbots+=[None]*workshop_sexbots_storage_upgrade_space
  "Now you can store {mark}[workshop_sexbots_storage_upgrade_space]{/} bots here."
  choice("<<<") "Continue"
  return

label workshop_add_storage:
  header "[workshop] - Add SexBot Storage"
  "You buy another {mark}Bot Support System{/} from the local market network, set it up in the storage room, and connect it to the main line."
  ""
  $workshop.sexbots+=[None]*workshop_sexbots_storage_upgrade_space
  "Now you can store {mark}[workshop_sexbots_storage_upgrade_space]{/} extra bots here."
  choice("<<<") "Continue"
  return

label workshop_increase_power_level:
  header "[workshop] - Increase Power Level"
  ""
  "You send a request along with the required fee to your landlord to increase the power to the building you're renting."
  ""
  "The landlord is happy to accept the money but the automatic reply comes back saying it will take {mark}5 days{/} to fulfill your request."
  ""
  "It sucks that you have to pay in advance but you're looking forward to increasing the number of capsules you can use in the workshop."
  $sr24_power_upgrade_counter=5
  choice("<<<") "Continue"
  return

label upgrade_workshop_power():
##  $print "START: ",sr24_power_upgrade_counter
  $sr24_power_upgrade_counter-=1     ## decrement counter
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  ""
  if sr24_power_upgrade_counter>1:   ## if counter > 0 show countdown info
    "It's still {mark}[sr24_power_upgrade_counter] days{/} until the power upgrade you ordered will be completed. You wish you could make it go faster!"
  elif sr24_power_upgrade_counter==1:
    "The power upgrade you ordered will be completed {mark}tomorrow{/}, it seems like it took forever!"
  elif sr24_power_upgrade_counter==0:  ## when counter reaches 1 upgrade takes effect
    "You receive a message from your landlord saying the power to the building has been increased."
    if sr24_power_level==1:            ## at power level 1
      $sr24_power_level=2              ## increase to power level 2
      $sr24_max_capsules=10            ## upgrade workshop power to support 10 capsules
    elif sr24_power_level==2:          ## at power level 2
      $sr24_power_level=3              ## increase to power level 3
      $sr24_max_capsules=15            ## upgrade workshop power to support 15 capsules
    elif sr24_power_level==3:          ## at power level 2
      $sr24_power_level=4              ## increase to power level 4
      $sr24_max_capsules=20            ## upgrade workshop power to support 20 capsules
  choice("<<<") "Continue"

##  $print "END: ",sr24_power_upgrade_counter

  return
##===== end of addition=====

##=====SUPPORTING FUNCTIONS=====

label select_capsule_upgrade(capsule_n):
  $selected_capsule=int(capsule_n)               ## THIS IS A GLOBAL VARIABLE FOR CONVENIENCE
  $temp_n=selected_capsule+1                     ## display capsule number: 0-19 needs to be displayed as 1-20
  header "[workshop] - {mark}Upgrade AI{/} for SexBot Capsule"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $action_image= "squirrel upgrades cu_1"
  center "{image=[action_image]@320x480}"
  ## TEXT on right
  $act.set_block("c")
  ""
  "Capsule {mark}AI upgrades{/} include proprietary AI that increases the {mark}psychocore stability{/} of bots stored in the capsule. Upgrades come in {mark}4 levels{/} and the higher levels are much {mark}more effective{/}."
  ""
  "You can upgrade incrementally or all at once because {mark}you'll receive full credit for all previous upgrades{/}. Your final cost to reach level 4 will be the same if you increment in 4 steps or all at once."
  ""
  if capsule_upgrade_status[selected_capsule]<3:                  ## there are at least 2 levels available
    "Select the upgrade level you'd like to purchase for {mark}capsule [temp_n]{/} today:"
  elif capsule_upgrade_status[selected_capsule]==3:                ## only level 4 is available
    "Select level 4 if you'd like to upgrade {mark}capsule [temp_n]{/} today:"
  else:                                                            ## must be 4, no upgrades available
    "{mark}Capsule [temp_n]{/} is already at the highest level, no upgrades are available."
  $was_level=capsule_upgrade_status[selected_capsule]              ## level of selected capsule now
  if capsule_upgrade_status[selected_capsule]==0:                  ## active button to go to level 1
    $is_level=1
    $cost_n=calculate_upgrade_cost(was_level,is_level)
    choice("do_capsule_upgrade:"+str(is_level),cost=[("money",cost_n)]) "Level 1"
  else:
    choice(None) "Level 1"
  if capsule_upgrade_status[selected_capsule]<=1:                  ## active button to go to level 2
    $is_level=2
    $cost_n=calculate_upgrade_cost(was_level,is_level)
    choice("do_capsule_upgrade:"+str(is_level),cost=[("money",cost_n)]) "Level 2"
  else:
    choice(None) "Level 2"
  if capsule_upgrade_status[selected_capsule]<=2:                  ## active button to go to level 3
    $is_level=3
    $cost_n=calculate_upgrade_cost(was_level,is_level)
    choice("do_capsule_upgrade:"+str(is_level),cost=[("money",cost_n)]) "Level 3"
  else:
    choice(None) "Level 3"
  if capsule_upgrade_status[selected_capsule]<=3:                  ## active button to go to level 4
    $is_level=4
    $cost_n=calculate_upgrade_cost(was_level,is_level)
    choice("do_capsule_upgrade:"+str(is_level),cost=[("money",cost_n)]) "Level 4"
  else:
    choice(None) "Level 4"
  choice("workshop_capsules:1",pos=17) "Back"                      ## return to 'Capsules' screen sending "1" for alternate text
  return

label do_capsule_upgrade(capsule_level):
  $temp_n=selected_capsule+1                     ## display capsule number: 0-19 needs to be displayed as 1-20
  header "[workshop] - {mark}Upgrade AI{/} for SexBot Capsule"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $action_image= "squirrel upgrades cu_1"
  center "{image=[action_image]@320x480}"
  ## TEXT on right
  $act.set_block("c")
  ""
  "{mark}Congratulations!{/} You've just upgraded {mark}capsule [temp_n]{/} to {mark}level [capsule_level]{/}."
  ""
  "The upgrade will be loaded {mark}automatically via the net{/} and will be fully functional in just a few minutes."
  ""
  "Thank you, we're sure you'll enjoy having {mark}more free time!{/}"
  $capsule_upgrade_status[selected_capsule]=int(capsule_level)
  choice("workshop_capsules:1",pos=17) "Continue"  ## return to 'Capsules' screen sending "1" for alternate text
  return

label capsule_stability_increase:
  python:
    for bot_n,bot in enumerate(home.sexbots):   ## go through all capsules
      if bot and not bot.chassis.is_disabled:
        temp_n=0
        if capsule_upgrade_status[bot_n]==1:      ## capsule is at level 1
          temp_n=random.randint(1,2)
        elif capsule_upgrade_status[bot_n]==2:    ## capsule is at level 2
          temp_n=random.randint(2,3)
        elif capsule_upgrade_status[bot_n]==3:    ## capsule is at level 3
          temp_n=random.randint(3,5)
        elif capsule_upgrade_status[bot_n]==4:    ## capsule is at level 4
          temp_n=random.randint(5,8)

##        print bot_n,bot,temp_n
##        print bot_n,bot,bot.psychocore.stability

        bot.psychocore.stability+=temp_n          ## TRUST FUNCTION TO HANDLE TOO MUCH INCREASE

##        print bot_n,bot,bot.psychocore.stability

  return

init python:
  def calculate_upgrade_cost(was_n,is_n):
    temp=0
    if was_n==0:
      if is_n==1:
        temp=capsule_upgrade_1
      elif is_n==2:
        temp=capsule_upgrade_1+capsule_upgrade_2
      elif is_n==3:
        temp=capsule_upgrade_1+capsule_upgrade_2+capsule_upgrade_3
      else:                                                                           ## must be 4
        temp=capsule_upgrade_1+capsule_upgrade_2+capsule_upgrade_3+capsule_upgrade_4
    elif was_n==1:
      if is_n==2:
        temp=capsule_upgrade_2
      elif is_n==3:
        temp=capsule_upgrade_2+capsule_upgrade_3
      else:                                                                           ## must be 4
        temp=capsule_upgrade_2+capsule_upgrade_3+capsule_upgrade_4
    elif was_n==2:
      if is_n==3:
        temp=capsule_upgrade_3
      else:                                                                           ## must be 4
        temp=capsule_upgrade_3+capsule_upgrade_4
    else:                                                                             ## must be 3
      temp=capsule_upgrade_4                                                          ## must be 4
    return temp

##0.12.8 add bot monitor

label select_bot_monitor(capsule_n):
  $selected_capsule=int(capsule_n)               ## THIS IS A GLOBAL VARIABLE FOR CONVENIENCE
  $temp_n=selected_capsule+1                     ## display capsule number: 0-19 needs to be displayed as 1-20
  header "{size=-8}[workshop] - License {mark}Bot Monitor{/} for SexBot Capsule"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $action_image= "squirrel upgrades cu_1"
  center "{image=[action_image]@320x480}"
  ## TEXT on right
  $act.set_block("c")
  ""
  "Purchasing a {mark}Bot Monitor{/} software license for your capsule allows you to view the status of your bot remotely when they are inside the capsule."
  ""

##  $print "Bot Monitor Status: ",bot_monitor_status[selected_capsule] 

  if bot_monitor_status[selected_capsule]==0:                      ## active button, no 'Bot Monitor' license
    choice("buy_bot_monitor",cost=[("money",bot_monitor_license)]) "Bot Monitor"
  else:                                                            ## have 'Bot Monitor' license, inactive button
    choice(None,hint="{hint}(installed)") "Bot Monitor"    
  choice("workshop_capsules:1",pos=17) "Back"                      ## return to 'Capsules' screen sending "1" for alternate text
  return

label buy_bot_monitor:
  $temp_n=selected_capsule+1                     ## display capsule number: 0-19 needs to be displayed as 1-20
  header "{size=-8}[workshop] - License {mark}Bot Monitor{/} for SexBot Capsule"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $action_image= "squirrel upgrades cu_1"
  center "{image=[action_image]@320x480}"
  ## TEXT on right
  $act.set_block("c")
  ""
  "{mark}Congratulations!{/} You've just purchased a license to activate {mark}Bot Monitor{/} software for {mark}capsule [temp_n]{/}."
  ""
  $while_count=0
  $temp_sum=0
  while while_count<=19:
    $temp_sum=temp_sum+bot_monitor_status[while_count]
    $while_count+=1
  if temp_sum==0:    ## no capsules have a Bot Monitor license
    "You'll need to install the {mark}Bot Monitor client software{/} on your computer(s) to begin viewing your bot's status remotely."
    ""
  else:
    "Your {mark}Bot Monitor client software{/} will now display the status of bots placed into this capsule."
    ""
  "Thank you, for using {mark}Bot Monitor{/}!"
  if temp_sum==0:
    $bot_monitor_installed=1    ## set flag to enable button on home screen
    ""
    ""
    "{good}I decided to install the Bot Monitor client software on the computers in the workshop and in my bedroom now so I'll be able to use it whenever I want to.{/}" 
  $bot_monitor_status[selected_capsule]=1

##  $print "Bot Monitor Status: ",bot_monitor_status[selected_capsule]

  choice("workshop_capsules:1",pos=17) "Continue"  ## return to 'Capsules' screen sending "1" for alternate text
  return