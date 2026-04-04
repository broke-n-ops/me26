init python hide:
  notification_categories["quests"]=("Quests","normal")

  @event_handler("quest_started")
  def quest_started(quest):
    msg=quest.quest_type.capitalize()+" {mark}"+quest.name+"{/} started."
    game_notification(msg,"quests","quest")

  @event_handler("quest_finished")
  def quest_finished(quest):
    msg=quest.quest_type.capitalize()+" {mark}"+quest.name+"{/} finished."
    game_notification(msg,"quests","quest")

  @event_handler("quest_failed")
  def quest_failed(quest):
    msg=quest.quest_type.capitalize()+" {mark}"+quest.name+"{/} {bad}failed{/}."
    game_notification(msg,"quests","quest")

  @event_handler("quest_advanced")
  def quest_advanced(quest):
    msg=quest.quest_type.capitalize()+" {mark}"+quest.name+"{/} updated."
    game_notification(msg,"quests","quest")

  @event_handler("quest_updated")
  def quest_updated(quest):
    msg=quest.quest_type.capitalize()+" {mark}"+quest.name+"{/} updated."
    game_notification(msg,"quests","quest")
