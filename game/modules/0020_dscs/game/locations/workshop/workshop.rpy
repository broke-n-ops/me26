define workshop_sexbots_storage_start_space=0
define workshop_sexbots_storage_upgrade_space=6
define workshop_sexbots_storage_max_space=6*15

init python:
  class Location_workshop(Location):
    name="Workshop"
    def init(self,*args,**kwargs):
      self.sexbots=[None]*workshop_sexbots_storage_start_space
    @property
    def max_sexbots(self):
      return len(self.sexbots)
    @property
    def available_space(self):
      return len([bot for bot in self.sexbots if bot is None])
    def add_sexbot(self,bot):
      bot=find_character(bot)
      self.sexbots[self.sexbots.index(None)]=bot
    def remove_sexbot(self,bot,erase_bot=True):
      bot=find_character(bot)
      self.sexbots[self.sexbots.index(bot)]=None
      if erase_bot:
        bot.remove()

define label_goto_workshop_action_info={
  "title": "[workshop]",
  }

label goto_workshop:
  $game.location="workshop"
  return "roaming"

label roaming_workshop:
  $game_bg="workshop bg"
  $game_bgm="home bgm"
  header "[workshop]"
  "The back half of your space is the workshop which is larger than you need. It's messy but you have a really nice repair robot, a few tool carts, and your bot capsules in the back."
  ""
  "The door to the right is the storage room and the one on the left leads to the basement."
  ""
  if workshop["do_not_sell"]:
    "You have set your shop on {mark}do-not-sell{/} mode. Your shopkeeper bots will not sell any parts."
    ""
  "The building is at {mark}Power Level [sr24_power_level]{/} which allows you to have up to {mark}[sr24_max_capsules] capsules{/}."
  if sr24_max_capsules==len(home.sexbots):
    if sr24_power_level==4:
      extend " You own 20 capsules and the building cannot support any more {mark}Power Upgrades{/} so this will have to be enough."
    else:
      extend " You own as many capsules as the building can support, if you want to add more capsules the building needs a {mark}Power Upgrade{/}."
  else:
    $temp=sr24_max_capsules-len(home.sexbots)
    if temp==1:
      extend " The building has enough power to support {mark}1{/} more capsule"
    else:
      extend " The building has enough power to support {mark}[temp]{/} more capsules"
    if sr24_power_level==4:
      extend " and it can not handle any more {mark}Power Upgrades{/}."
    else:
      extend ", there's no need for a {mark}Power Upgrade{/} right now."
## addition for increasing capsules
  $workshop_storage_page=0
  $sr24_capsule_flag=False                                  ## clear flag for capsule/bot panel

## TRY SYNCHRONIZING PAGES, DON'T SET TO 0 AUTOMATICALLY
##  $sr24_capsules_screen_page=0                              ## set capsule page to 0 (bots 1-5)

##  $print "START saved_scroll_positions"
##  $print saved_scroll_positions
##  $print "END saved_scroll_positions"

  $saved_scroll_positions["interaction_default_content"]=0
## end of addition

  call random_event("roaming_workshop")
  if _return=="default":
    choice(">>>workshop_inventory:0") "Inventory"
    choice(">>>workshop_upgrades") "Upgrades"
    choice(">>>workshop_capsules:0") "Capsules"
    if workshop.max_sexbots>0:
      choice(">>>workshop_storage") "Storage"
    if workshop["do_not_sell"]:
      choice(">>>workshop_toggle_global_parts_dns",hint="toggle do-not-sell",pos=12) "DNS: on"
    else:
      choice(">>>workshop_toggle_global_parts_dns",hint="toggle do-not-sell",pos=12) "DNS: off"
    choice(">>>workshop_fix_random_part",pos=13,key="t") "Tinker"
    choice(">>>workshop_fix_random_bot",pos=14) "Tinker bots"
    choice(">>>workshop_stabilize_random_bot",pos=15) "Stabilize bots"  ## added for v0.5.n
    choice("goto_home",pos=17,key=("home","cancel")) "Done"
  $process_event("roaming_finalize_workshop")
  $process_event("roaming_finalize","workshop")
  return

label workshop_toggle_global_parts_dns:
  $workshop["do_not_sell"]=not workshop["do_not_sell"]
  return "<<<"
