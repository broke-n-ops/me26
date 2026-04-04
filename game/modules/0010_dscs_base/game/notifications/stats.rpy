init python:
  def stat_notification_category(stat):
    if stat.stat_type=="bot_stat":
      return "bot_stats"
    elif stat.stat_type=="bot_skill":
      return "bot_skills"
    elif stat.stat_type=="mc_stat":
      return "player_stats"
    elif stat.stat_type=="mc_skill":
      return "player_skills"
    elif stat.stat_type.startswith("expertise"):
      return "player_expertise"
    elif stat.stat_type.endswith("rep"):
      return "player_reputation"
    else:
      return "player_stats"

init python hide:
  notification_categories["player_stats"]=("Player Stats","normal")
  notification_categories["player_skills"]=("Player Skills","small")
  notification_categories["player_reputation"]=("Player Reputation","small")
  notification_categories["player_expertise"]=("Player Expertise","small")
  notification_categories["bot_stats"]=("Bot Stats","small")
  notification_categories["bot_skills"]=("Bot Skills","small")

  @event_handler("stat_xp_granted")
  def stats_xp_granted(char,stat,xp):
    if char.notify_xp_granted:
      if stat.notify_xp_granted:
        if hasattr(stat,"xp_gain_msg"):
          msg=stat.xp_gain_msg(char,stat,xp)
        else:
          if xp>0:
            msg="%s gained %s xp in %s"%(char,xp,stat)
          elif xp<0:
            msg="%s lost %s xp in %s"%(char,-xp,stat)
        game_notification(msg,stat_notification_category(stat),"stat_xp_granted")

  @event_handler("stat_level_changed")
  def stats_level_change(char,stat,old_level,level):
    if char.notify_level_changed:
      if stat.notify_level_changed:
        if hasattr(stat,"level_changed_msg"):
          msg=stat.level_changed_msg(char,stat,old_level,level)
        else:
          msg="%s is now level {mark}%s{/} in {mark}%s{/}"%(char,stat.level_name,stat)
        game_notification(msg,stat_notification_category(stat),"stat_level_changed")

  @event_handler("stat_learned")
  def stat_learned(char,stat):
    if char.notify_stat_learned:
      if stat.notify_stat_learned:
        if hasattr(stat,"learned_msg"):
          msg=stat.learned_msg(char,stat)
        else:
          msg="{} learned new skill - {{mark}}{}{{/}}".format(char,stat)
        game_notification(msg,stat_notification_category(stat),"stat_learned")

  @event_handler("stat_unlearned")
  def stat_unlearned(char,stat):
    if char.notify_stat_unlearned:
      if stat.notify_stat_unlearned:
        if hasattr(stat,"unlearned_msg"):
          msg=stat.unlearned_msg(char,stat)
        else:
          msg="{} completely forgot known skill - {}".format(char,stat)
        game_notification(msg,stat_notification_category(stat),"stat_unlearned")
