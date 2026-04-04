init python:
  class Location_flea_market(Location):
    name="Flea Market"
    def init(self):
      self.bots_for_sale=None
      self.bot_parts_for_sale=None

define label_goto_flea_market_action_info={
  "title": "[flea_market]",
  }

label goto_flea_market:
  $game.location="flea_market"
  return "roaming"

label roaming_flea_market:
  $game_bg="flea_market bg"
  $game_bgm="flea_market bgm"
  header "[flea_market]"

  # "You see lots of stalls, some tents, even a couple of shop vehicles, buying, selling, and trading all kinds of stuff. Weird mix of hard to distinguish smells, constant noise, and lots of people chaotically walking from stall to stall."
  # ""
  # "Just the right place to find something nice and cheap. Or sell something, cheap too, sadly."

  "This is no ordinary flea market, it's a black market alley lined with small shops selling and trading all kinds of goods both legal and illegal. It's not very crowded, too many dangerous people around. Many shops have human or bot guards for protection."
  ""
  "If you have the courage it's the right place to find something nice and cheap. It's also a place you can sell things, sadly also cheap."
  ""


  $quests.where_to_get_bots.add_method("flea_market","you can buy working bots at {mark}[flea_market]{/}")
  $quests.where_to_get_bot_parts.add_method("flea_market","you can buy bot parts at {mark}[flea_market]{/}")
  $quests.where_to_sell_bots.add_method("flea_market","you can sell your bots at {mark}[flea_market]{/}, though prices are really bad, and buyers only care about parts integrity")
  call random_event("roaming_flea_market")
  if _return=="default":
    choice(">>>flea_market_buy_bot") "Buy Bot"
    choice(">>>flea_market_sell_bot") "Sell Bot"
    choice(">>>flea_market_buy_bot_parts") "Buy Bot Parts"
    choice("goto_home",pos=16,key="home") "[home]"
    choice("goto_street",pos=17,key="cancel") "[street]"
  $process_event("roaming_finalize_flea_market")
  $process_event("roaming_finalize","flea_market")
  return
