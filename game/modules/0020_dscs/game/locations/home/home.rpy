## 'start' used here for home 'init', 'max' no longer used
default start_sexbots_capsules=1
##  define max_sexbots_capsules=6  ## no longer used, 'max' is now part of 'workshop_upgrade'

init python:
  class Location_home(Location):
    name="Home"
    payment_day="Friday"
    def init(self,*args,**kwargs):
      self.sexbots=[None]*start_sexbots_capsules
      self.expenses=0
    def update_expenses(self):
      expenses={}
      process_event("expenses",expenses)
      self.expenses=sum((entry[0] for entry in expenses.values() if isinstance(entry,(list,tuple))))
    @property
    def rent(self):
      return game.difficulty*2500
    @property
    def max_sexbots(self):
      return len(self.sexbots)
    @property
    def max_sexbots_str(self):
      if self.max_sexbots>1:
        return str(self.max_sexbots)+" sexbot capsules"
      else:
        return str(self.max_sexbots)+" sexbot capsule"
    @property
    def available_capsules(self):
      return len([bot for bot in self.sexbots if bot is None])
    def add_sexbot(self,bot):
      bot=find_character(bot)
      self.sexbots[self.sexbots.index(None)]=bot
      if store.current_side_info_bot is None:
        store.current_side_info_bot=bot.id
    def remove_sexbot(self,bot,erase_bot=True):
      bot=find_character(bot)
      self.sexbots[self.sexbots.index(bot)]=None
      if erase_bot:
        bot.remove()
      if current_side_info_bot==bot.id:
        store.current_side_info_bot=([bot.id for bot in home.sexbots if bot] or [None])[0]

define label_goto_home_action_info={
  "title": "[home]",
  }

## modified in 0.8.n to include 'netconsole' as a 'home location' since you browse from home
define home_locations=("home","workshop","netconsole")
## FYI: away locations prior to 0.8.n are: ("street","robosechs","flea_market","dump_site")
## in 0.8.n "neighborhood", "corner_store", "local_diner", and "local_bar" were added as away locations

label goto_home:
  if game.location not in home_locations:
    "{mcsay}Home, sweet home...{/} You sigh, looking around."
    ""
  $game.location="home"
  return "roaming"

label roaming_home:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"

## 0.14 need to reset sucky's last training flag
  $global sucky_last_interaction
  $sucky_last_interaction=0

  "You hardly can call it \"cozy\", but it's your current home: an old warehouse! You tell yourself it's temporary, once your business gets going you'll find a better place."
  ""
  if hw_building_gym==1:         ##  GYM BEING BUILT
    "There are crude living quarters inside and there's lots of room for your shop, more than you really need in fact. There's also lots of storage space and soon what used to be a dingy basement will be a home gym."
  elif hw_equipment_level<=3:    ##  BEFORE GYM PURCHASE
    "There are crude living quarters inside and there's lots of room for your shop, more than you really need in fact. There's also lots of storage space and even a dingy basement."
  else:                          ##  GYM BUILT
    "There are crude living quarters inside and there's lots of room for your shop, more than you really need in fact. There's also lots of storage space and a great home gym in the basement."
## 0.12.8 changes to avoid bot interaction mismatch with bot side info
  $using_bot_monitor=0           ## clear bot monitor flag, add message when 2 or more capsules
  if home.max_sexbots>1 and bot_monitor_installed==0:  ## more than 1 capsules and bot monitor not installed yet
    ""
    "{good}Maybe I should get Bot Monitor installed on my capsules to make it easier to monitor my bots. I need to do that from the capsules.{/}"
## end addition

## 0.15.n created function for reminders when at home, move damaged bot there and add others AND removed previous repair bot message from 0.14.2
  call home_reminders

## added to support more than 6 capsules
  $sr24_capsule_flag=False            ## clear flag for capsule/bot panel
  $saved_scroll_positions["interaction_default_content"]=0
## added in 0.9.n - check 'rep_syndicate' in case a game is opened that didn't start with it
  if sr24_checked_syndicate_rep==0:  ## function sets flag to 1 to avoid unnecessary repeats
    call check_syndicate_reputation
  call random_event("roaming_home")
  if _return=="default":
    if now("night"):
      choice(">>>home_sleep") "Sleep"
    else:
      choice(">>>home_rest") "Rest"
    choice(">>>home_work") "Work"
    choice("goto_workshop") "[workshop]"
    choice("enter_netconsole") "[netconsole]"
    choice("leaving_home") "Leave Home"
    call home_add_buttons                      ## 0.11.n move conditional buttons to a function
    choice("hw_rename_characters",key="R",hint="Characters",pos=17) "Rename"
  $process_event("roaming_finalize_home")
  $process_event("roaming_finalize","home")
  return

label leaving_home:     ## added in 0.9 to create the 'neighborhood' location
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "[home]"
  "It's nice to get away from the shop once in a while but, since you're not rich, you don't have too many options."
  ""
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $temp_int=random.randint(1,2)
  $action_image="home_leaving hlv_"+str(temp_int)       ## images of neighborhood (store&diner)
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(3,4)
  $action_image="home_leaving hlv_"+str(temp_int)       ## images of subway station
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "The local {mark}neighborhood{/} has a few places to hang out and I don't have to go far. Some of my neighbors are interesting people and you never know what I might learn from them."
  ""
  ""
  ""
  "{mark}District TX-13{/} is the large city near by, it takes {mark}$20{/} and some time to get there {mark}on the subway{/} but there are places there that make it worth my time."
  if now("evening") and bp_suit_for_rays==1:                                ## MC in new clothing (given suit by Simone)
    extend " I'll rent a {mark}$25{/} locker at the station to hold my suit in case I decide to go to {mark}Raymond's Bot Boutique{/}."
  choice("goto_neighborhood") "Neighborhood"
  if now("evening") and bp_suit_for_rays==1 and rays_already_visited==0:       ## MC in new clothing (given suit by Simone) and you haven't gone to the show yet
    choice("goto_street",cost=[("money",45),("energy",1)]) "District TX-13"
  else:                                                                       ## MC in old clothing
     choice("goto_street",cost=[("money",20),("energy",1)]) "District TX-13" 
  choice("<<<") "Cancel"
  return

##===== 0.9.n MOVED BUTTON CREATION FROM 'home workout' EVENT HANDLER======

label home_workout_buttons:
  if hw_equipment_level<=3:                                                                     ## yoga and boxing unavailable
    if hw_workouts_today==0:                                                                    ## first workout
      choice("home_workout_action",cost=[("energy",hw_workout_ap_cost)]) "Workout"
    else:                                                                                       ## not first workout
      choice("home_workout_action",cost=[("energy",hw_workout_ap_cost)]) "Workout Again"
  else:                                                                                         ## yoga and boxing available-goes to intermediate screen
    if hw_workouts_today==0:
      choice("home_workout_action") "Workout"                                                   ## first workout
    else:
      choice("home_workout_action") "Workout Again"                                             ## not first workout
  return

label mob_quest_buttons:
  if quests.mobprotection.started and not quests.mobprotection.finished:  ## Mob Protection in process
    if quests.mobprotection!="extortion1":                                ## skip phase 1-mob hasn't appeared yet
      choice("hw_test_bot_for_mob",pos=12) "Mob Bot Check"
    if quests.mobprotection=="extortion8":                                ## extortion8 is when sabotage sex bot can be given
      choice("hw_test_special_bot_for_mob", pos=13) "Sabotage Bot Check"
  return

label good_neighbor_buttons:
  if quests.goodneighbor.started and not quests.goodneighbor.finished:                                                          ## good neighbor active
    if quests.goodneighbor=="goodneighbor1":                                                                                    ## delivering bots to store
      if mc.money>56000:                                                                                                        ## enough money to buy capsules
        choice("good_neighbor_advance",hint="To Store, {bad}$56K{/}",pos=12) "Deliver Bots"
      else:
        choice(None,hint="{bad}Requires $56K{/}",pos=12) "Deliver Bots"
    elif quests.goodneighbor=="goodneighbor3" or quests.goodneighbor=="goodneighbor4" or quests.goodneighbor=="goodneighbor5":  ## delivering bots to patrol HQ
      if mc.money>56000:                                                                                                        ## enough money to buy capsules
        choice("good_neighbor_advance",hint="To Patrol, {bad}$56K{/}",pos=12) "Deliver Bots"
      else:
        choice(None,hint="{bad}Requires $56K{/}",pos=12) "Deliver Bots"
  return

label bot_monitor_button:
  if bot_monitor_installed==1:
    choice("bot_monitor_software:0",key="m",pos=6) "Bot Monitor"   ## start on page 0
  return