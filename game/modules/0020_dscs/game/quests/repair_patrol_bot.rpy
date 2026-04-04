init python:
  class Quest_repair_patrol_bot(Quest):
    quest_type="task"

    name="Repair Patrol Bot"

    repeatable=True
    keep_closed=False

    def init(self,bot_id):
      self["bot_id"]=bot_id
    @property
    def bot(self):
      return find_character(self["bot_id"])

    class phase_1_repair:
      def description(self):
        rv="""
          One of the {mark}Neighborhood Patrol{/} bots was damaged protecting the neighborhood from thugs. You need to repair the damage. {mark}Integrity must be 100% and any replacement parts must be B+{/}.

          Bot model: {mark}[quest.bot.model_name]{/}.
          Bot name: {mark}[quest.bot]{/}.
          """
        if self.bot.chassis.integrity==100:
          rv+="{mark}Ready to return.{/}"
        return rv
    class phase_1000_done:
      description="Patrol Bot Repaired."
    class phase_2000_canceled:
      description="Cannot get here."

label interact_default_return_patrol_bot(bot):

##  $print
##  $print "1) interact_default_return_patrol_bot(bot): ",bot

  header "[workshop]"
  "You place {mark}[bot]{/} on the gurney and perform a last minute check."
  ""
  if bot.gender=="female":                                  ## female bot being returned
    $action_image= "quests good_neighbors sgn_58"
  else:                                            ## male bot damaged
    $action_image= "quests good_neighbors sgn_59"
  center "{image=[action_image]@680x600}"
## check part ratings
  python:
    rpb_part_test_pass=1
    for slot in bot.outfit_slots:      ## assume pass before starting check
      part=bot.item_on_slot(slot)
      if part.rate in rpb_part_check:  ## part rating uses reverse logic
        rpb_part_test_pass=0
        break                          ##  stop testing on failure, part quantity or identity irrelevant
  if bot.psychocore.stability<100:     ## cannot return unstable bots
    $rpb_part_test_pass=0
  if rpb_part_test_pass==0:
    ""
    "{bad}What was I thinking?{/} All {mark}Neighborhood Patrol{/} bots need {mark}B+ level parts{/} and need to be {mark}100\% Stable{/}. I can't return this bot yet."
    interact(None,hint="{bad}bot not ready{/}") "Return Patrol Bot"
  else:
    ""
    "The patrol bot has {mark}100\% Integrity{/}, has {mark}all B+ level parts{/}, and is {mark}100\% Stable{/}. That means [bot.heshe]'s is good as new and ready to protect the neighbornood!"
    interact("return_patrol_bot_do") "Return Patrol Bot"
  interact("<<<") "Cancel"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_return_patrol_bot_do(bot):

##  $print "2) interact_default_return_patrol_bot_do(bot): ",bot

  header "[workshop]"
  "You instruct {mark}[bot]{/} to return to the {mark}Neighborhood Patrol{/} headquarters and report for duty."
  ""
  if bot.gender=="female":                                  ## female bot being returned
    $action_image= "quests good_neighbors sgn_60"
  else:                                            ## male bot damaged
    $action_image= "quests good_neighbors sgn_61"
  center "{image=[action_image]@660x600}"
  ""
  "{mark}[bot]{/} reports for duty and {mark}[gn_store_owner_name]{/} is very happy to see [bot.himher]. The neighborhood is safer when the patrol is at full strength."
  $mc.give_xp("rep_neighborhood",10)
  $find_quest(bot["repair_patrol_bot_quest_id"]).finish()
  $move_sexbot(bot,None)                                   ## bot removed from game, patrol is not a holding area
  $gn_repairing_bot-=1                                     ## counter: decrement when bot returned

##  $print
##  $print "returned a bot after repair"
##  $print "gn_repairing_bot: ",gn_repairing_bot
##  $print "gn_damaged_bot_waiting: ",gn_damaged_bot_waiting

  choice("end_bot_interaction") "Continue"
  return