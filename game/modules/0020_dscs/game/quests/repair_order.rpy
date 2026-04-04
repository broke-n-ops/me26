init python:
  class Quest_repair_order(Quest):
    quest_type="task"

    name="Repair Order"

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
          A client asked you to repair a broken bot. Time needed and final state isn't really important, as long as the bot is functional.

          Bot model: {mark}[quest.bot.model_name]{/}.
          Bot name: {mark}[quest.bot]{/}.
          """
        if not self.bot.chassis.is_disabled:
          rv+="{mark}Ready to deliver.{/}"
        return rv
    class phase_1000_done:
      description="Order delivered."
    class phase_2000_canceled:
      description="Order canceled."

label interact_default_cancel_repair_order(bot):
  header "[workshop]"
  "You can call the client and inform them that you are unable to repair the bot. The client surely will be disappointed and your reputation may be damaged."
  interact("cancel_repair_order_do",hint="{bad}rep---{/}") "Cancel Order"
  interact("<<<") "No"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_cancel_repair_order_do(bot):
  header "[workshop]"
  "You call the client and inform them that you are unable to repair the bot; the client is disappointed. The order is returned to the client by the delivery bot."
## 0.12.n revise rep gain and make sure you have a rep to lose!!
  if mc.rep_mc_mechanic.level>1:                     ##  make sure you have a rep to lose
    $temp=calc_pr_rep_gain("rep_mc_mechanic","m_l")  ##  mechinic medium LOSS - 0.012.n REVISION
    $mc.give_xp("rep_mc_mechanic",temp)  
  $mc.give_xp("rep_mc_mechanic",-100)
  $find_quest(bot["repair_order_quest_id"]).fail()
  $move_sexbot(bot,None)
  choice("end_bot_interaction") "Continue"
  return

label interact_default_deliver_repair_order(bot):
  header "[workshop]"
  "You can call client and tell bot is ready for pickup. Or you can tinker with it bit more."
  interact("deliver_repair_order_do",hint="{good}rep+++{/}") "Deliver Order"
  interact("<<<") "Not yet"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_deliver_repair_order_do(bot):
  header "[workshop]"
  "You call client and tell bot is ready for pickup. Delivery bot return fixed bot to client. Soon after you receive confirmation message from satisfied client with attached payment."
  python:
    quest_reward_cap=3000
    quest_reward_base=1000
    quest_reward=max(1,int(round(bot_price_function(bot,base_price_mult=0,skill_mods={})/1.5)))
    quest_reward_bonus=max(0,min(quest_reward_cap,quest_reward)-quest_reward_base)
    quest_reward=quest_reward_base+quest_reward_bonus
    quest_reward_rep=quest_reward*100//quest_reward_cap
  if quest_reward_bonus>0:
    "The client added [money_str[quest_reward_bonus]] bonus to the agreed-upon [money_str[quest_reward_base]] for extra quality."
  $mc.money+=quest_reward
  if quest_reward==3000:                              ##  $3000 is the maximum value
    $temp=calc_pr_rep_gain("rep_mc_mechanic","xl_g")  ##  trainer large GAIN - 0.012.n REVISION
    $mc.give_xp("rep_mc_mechanic",temp)  
  elif quest_reward>2499:                             ##  $2500 - $2999
    $temp=calc_pr_rep_gain("rep_mc_mechanic","l_g")   ##  trainer large GAIN - 0.012.n REVISION
    $mc.give_xp("rep_mc_mechanic",temp)  
  elif quest_reward>1999:                             ##  $2000 - $2499
    $temp=calc_pr_rep_gain("rep_mc_mechanic","m_g")   ##  trainer large GAIN - 0.012.n REVISION
    $mc.give_xp("rep_mc_mechanic",temp)  
  elif quest_reward>1499:                             ##  $1500 - $1999
    $temp=calc_pr_rep_gain("rep_mc_mechanic","s_g")   ##  mechanic small GAIN - 0.012.n REVISION
    $mc.give_xp("rep_mc_mechanic",temp)  
  else:                                               ##  $1000 - $1499
    $temp=calc_pr_rep_gain("rep_mc_mechanic","xs_g")  ##  mechanic extra small GAIN - 0.012.n REVISION
    $mc.give_xp("rep_mc_mechanic",temp)     
## old code      
##  $mc.give_xp("rep_mc_mechanic",quest_reward_rep)
  $find_quest(bot["repair_order_quest_id"]).finish()
  $move_sexbot(bot,None)
  choice("end_bot_interaction") "Continue"
  return
