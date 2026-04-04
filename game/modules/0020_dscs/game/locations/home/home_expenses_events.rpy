init python hide:
  @event_handler("time_advanced")
  def home_expenses_event():
    if now(home.payment_day,"morning"):
      queue_event("home_pay_expenses_event")

label home_pay_expenses_event:
  $game_bg="home computer"
  header "Expenses Payment Day"
  if home.expenses>mc.money:
    "You have failed your rent payment..."
    ""
    "In a few hours building owner, accompanied by some goons, evict you and throw away your belongings."
    ""
    # "After you were sitting and thinking about what to do now, you got a call from Mitsutachi Finance."
    # "{say}We were informed you are no longer able to operate a business due to a lack of office. Unfortunately, this is a breach of your contract. I've passed this on to our team. Our apologies for any inconvenience this may cause. Thank you for being our customer, Mitsutachi Finance is here for you!{/}"
    # ""
    # "In about an hour, a corporate repomen squad visits you and confiscates what they can. Including life-support implants."

    "You sit on the curb outside what used to be your shop and try to figure out what to do. You aren't paying much attention to your surroundings and don't notice that someone just walked up to you."
    ""
    "You hear a noise and look up to see the muzzle of a gun held by the guy who framed you..."

    choice("bad_ending_failed_to_pay_rent",hint="{bad}Bad Ending{/}") "Continue"
  else:
    $home["paid_expenses_today"]=True
    $mc.money-=home.rent
    "You received confirmation of your rent payment."
    $mc.money-=home.expenses-home.rent
    "You received confirmation of payment of other expenses."
    $home.update_expenses()
    ""
    $other_expenses=home.expenses-home.rent
    "Your rent for next week is: [money_str[home.rent]]."
    "Other expenses estimate: [money_str[other_expenses]]."
    choice("continue") "Continue"
  return

label bad_ending_failed_to_pay_rent:
  $set_interaction("ending")
  $act["ending_type"]="bad"
  $game_bg="black"
  $exit_main_loop=True
  return
