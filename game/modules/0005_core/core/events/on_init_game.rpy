init python hide:
  @event_handler("init_game",-10)
  def init_game():
    store.game=Game()
    store.now=CurrentDateTime(game.start_day,game.start_time)

  @event_handler("init_game",-5)
  def init_locations():
    for loc_id,loc_cls in sorted(locations_cls_by_id.items()):
      if loc_id and not loc_id.startswith("_"):
        setattr(store,loc_id,loc_cls())

  @event_handler("init_game",-4)
  def init_characters():
    for char_id,char_cls in sorted(characters_cls_by_id.items()):
      if char_id and not char_id.startswith("_"):
        setattr(store,char_id,char_cls())

  @event_handler("init_game",-3)
  def init_quests():
    store.quests=store.quests_manager=QuestsManager()
    for quest_id,quest_cls in sorted(quests_cls_by_id.items()):
      if quest_id and not quest_id.startswith("_"):
        if not quest_cls.repeatable:
          quest_cls()

  @event_handler("init_game",-1)
  def start_game():
    game.pc=game.default_pc
    process_event("game_started")
    process_event("update_state")
