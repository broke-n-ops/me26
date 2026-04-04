init python hide:
  @event_handler("time_advanced",-10)
  def process_game():
    game.process_event("time_advanced")

  @event_handler("time_advanced",-9)
  def process_locations():
    for loc_id,loc in sorted(all_locations.items()):
      loc.process_event("time_advanced")

  @event_handler("time_advanced",-7)
  def process_characters():
    for char_id,char in sorted(all_characters.items()):
      char.process_event("time_advanced")

  @event_handler("time_advanced",-5)
  def process_quests():
    for quest_id,quest in sorted(all_quests.items()):
      quest.process_event("time_advanced")
