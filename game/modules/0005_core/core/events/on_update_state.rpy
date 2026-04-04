init python hide:
  @event_handler("update_state",-9)
  def update_game_state():
    for char_id,char in all_characters.items():
      if char!=game.pc:
        char.ai()
      else:
        char.activity=None
