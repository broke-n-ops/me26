init python:
  def workshop_get_unstable_bots():
    bots=[]
    for bot in home.sexbots:
      if bot:
        if not bot["mission"]:
          if bot.psychocore.stability<100:
            bots.append(bot.id)
    return bots

  def workshop_get_random_unstable_bot():
    bots=workshop_get_unstable_bots()
    return randchoice(bots) if bots else None

  def label_workshop_stabilize_random_bot_action_info(**kwargs):
    if workshop_get_unstable_bots():
      kwargs["cost"]=[("energy",1)]
    else:
      kwargs["action"]=None
      kwargs["hint"]="{hint}all bots 100% stable{/}"
    return kwargs

label workshop_stabilize_random_bot:

##  $print "Called 'workshop_stabilize_random_bot'"

  $bot_target=workshop_get_random_unstable_bot()

##  $print "workshop_stabilize_random_bot - bot_target: ",bot_target
##  $print "workshop_stabilize_random_bot - bot_target.id: ",bot_target.id

  $bot_target=find_character(bot_target)

##  $print "workshop_stabilize_random_bot - bot_target (char): ",bot_target

  if bot_target:
    header "[bot_target] - Stabilizing PsychoCore"
    python:
      progress=mc.calc_stability_progress(bot_target)
      progress=min(100,bot_target.psychocore.stability+progress)-bot_target.psychocore.stability
      base_xp_reward=progress
      skill_xp_reward=int(base_xp_reward*2)
    "You run defragmentation tools, manually remove neural dead loops, and run diagnostics over and over. Eventually, you managed to improve [bot_target.posname] PsychoCore stability by {mark}[progress]%%{/}."
    $bot_target.psychocore.stability+=progress
    "Current stability is {mark}[bot_target.psychocore.stability]%%{/}."
    python:
      mc.give_xp("computers",skill_xp_reward)
      mc.give_xp("expertise_"+bot_target.model_id,base_xp_reward)
    ## @@REPEAT_ACTION
    if show_repeat_action():
      choice("workshop_stabilize_random_bot") "Repeat"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
    choice("goto_workshop",pos=17,key=("home","cancel")) "Done"
    return
  else:                              ## this only happens if there is a major bug, i.e. button active but no bots to stabilize which shouldn't happen
    return "<<<"