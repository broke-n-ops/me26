init python hide:
  @event_handler("expenses")
  def home_rent(expenses):
    if home.rent is not None:
      expenses["home_0_rent"]=(home.rent,"Chop Shop weekly rent")

  @event_handler("expenses")
  def home_capsules_maintainance(expenses):
    expenses["home_capsules"]=(home.max_sexbots*500*game.difficulty,home.max_sexbots_str+": power, cartridges and maintenance")
