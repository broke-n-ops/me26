init python hide:
  notification_categories["bot_traits"]=("Bot Traits&Quirks","normal")

  @event_handler("trait_gained")
  def bot_trait_gained(char,trait):
    if char.notify_trait_gained:
      if trait.notify_trait_gained:
        msg=char.name+" gained trait {"+trait.trait_color+"}"+trait.name+"{/}"
        game_notification(msg,"bot_traits","bot_traits")

  @event_handler("trait_lost")
  def bot_trait_lost(char,trait):
    if char.notify_trait_lost:
      if trait.notify_trait_lost:
        msg=char.name+" lost trait {"+trait.trait_color+"}"+trait.name+"{/}"
        game_notification(msg,"bot_traits","bot_traits")
