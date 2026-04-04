define flea_market_bot_price_cap=30000

label flea_market_sell_bot:
  header "[flea_market] - Selling bot"
  "You ask around if anyone is buying bots. Developed skills or rare models aren't valued here, buyers only check the state of the chassis. There are no high bidders here but you {mark}might{/} get better offers if you have a good reputation as a {mark}bot dealer{/} and {mark}mechanic{/}."
  ""
  $bots=[bot for bot in home.sexbots if bot and not bot.do_not_sell and bot.action_allowed("sell") and not bot["mission"]]
  $bots+=[bot for bot in workshop.sexbots if bot and not bot.do_not_sell and bot.action_allowed("sell") and not bot["mission"]]
  $bots=bots[:12]
  if bots:
    "After walking from shop to shop showing the shopkeepers scans of your bots, and some fierce haggling, you finally have a list of interesting offers."
    ""
    $bot_n=0
    while bot_n<len(bots):
      $bot=bots[bot_n]
      $bot_n+=1
      $bot_price=max(1,int(round(bot_price_function(bot,skill_mods=bot_price_skills_unimportant,base_price_mult=0.1)*0.75)))

## 0.12.n add reputation to cap price value
      $price_cap_increase=price_rep_flea_market()
      $revised_price_cap=flea_market_bot_price_cap+price_cap_increase
      $bot_price=min(revised_price_cap,bot_price)

      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}, price: [money_str[bot_price]]"
      choice("flea_market_sell_bot_do:{}".format(bot.id),cost=[("money",-bot_price)]) "Sell #[bot_n]"
    $bot=None
  else:
    "You don't have bots for sale."
  $bots=None
  choice("<<<",pos=17,key="cancel") "Back"
  return

label flea_market_sell_bot_do(bot):
  header "[flea_market] - Selling bot"
  $bot=find_character(bot)
  "You sell {mark}[bot]{/}."
## 0.12.n add reputations
  if bot.rate=="D":                                     ## dealer rep based upon bot's rate
    $temp=calc_pr_rep_gain("rep_mc_dealer","xs_g")      ## extra small gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif bot.rate=="C":
    $temp=calc_pr_rep_gain("rep_mc_dealer","s_g")       ## small gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif bot.rate=="B":
    $temp=calc_pr_rep_gain("rep_mc_dealer","m_g")       ## medium gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif bot.rate=="A":
    $temp=calc_pr_rep_gain("rep_mc_dealer","l_g")       ## large gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif bot.rate=="S":
    $temp=calc_pr_rep_gain("rep_mc_dealer","xl_g")      ## extra large gain
    $mc.give_xp("rep_mc_dealer",temp)
  if not bot.chassis.is_disabled:                       ## mechanic gain does not happen with a disabled chassis
    if bot.chassis.integrity<25:                        ## mechanic rep based upon bot's integrity
      $temp=calc_pr_rep_gain("rep_mc_mechanic","xs_g")  ## extra small gain
      $mc.give_xp("rep_mc_mechanic",temp)
    elif bot.chassis.integrity<50:   
      $temp=calc_pr_rep_gain("rep_mc_mechanic","s_g")   ## small gain
      $mc.give_xp("rep_mc_mechanic",temp)
    elif bot.chassis.integrity<75: 
      $temp=calc_pr_rep_gain("rep_mc_mechanic","m_g")   ## medium gain
      $mc.give_xp("rep_mc_mechanic",temp)
    elif bot.chassis.integrity<100: 
      $temp=calc_pr_rep_gain("rep_mc_mechanic","l_g")   ## large gain
      $mc.give_xp("rep_mc_mechanic",temp)
    else:                                               ## integrity must be 100
      $temp=calc_pr_rep_gain("rep_mc_mechanic","xl_g")  ## extra large gain
      $mc.give_xp("rep_mc_mechanic",temp)
  $move_sexbot(bot,None)
  $bot=None
  choice("<<<") "Continue"
  return
