init python:
  def flea_market_generate_bot_parts_for_sale():
    notify.disable()
    rv=[]
    for n in range(randint(2,5)):
      part=generate_bot_part("flea_market_buy_part","cheap")
      if part:
        part.apply_damage(randint(5,99),minimal_integrity=1)
        rv.append(part)
    notify.enable()
    return rv

define label_flea_market_buy_bot_parts_action_info={"cost":[("energy",1)]}

label flea_market_buy_bot_parts:
  header "[flea_market] - Buying bot parts"
  "You look around, searching for bot parts for sale, ignoring tons of outright junk. After quite some walking and haggling, you have a list of interesting offers. Considering quick turnover, you doubt parts will be kept for long, so if you like something, you should buy it now."
  ""
  $flea_market.parts_for_sale=flea_market_generate_bot_parts_for_sale()
  $part_n=0
  while part_n<len(flea_market.parts_for_sale):
    $part=flea_market.parts_for_sale[part_n]
    $part_n+=1
    $slot=find_item_slot(part.slot)
    $part_price=max(1,int(round(bot_part_price_function(part,flat_price_below=25)*1.5)))
    $part_with_defects="*" if part.defects else ""
    $money_tag="{bad}" if part_price>mc.money else "{mark}"
    python:
      part_rate=""
      if not game.hardcore:
        if mc.has_stat("expertise_"+part.id) or game.difficulty==1:
          part_rate=", rate: {mark}"+part.rate+"{/}"
        else:
          part_rate=", rate: {info}?{/}"
    "#[part_n] - [slot] - {mark}[part]{/}[part_rate], integrity: {bad}[part_with_defects]{/}{mark}[part.integrity]%%{/}, price: [money_tag][money_str[=part_price]]{/}."
    choice("flea_market_buy_bot_part:{}".format(part_n-1),cost=[("money",part_price)]) "Buy #[part_n]"
    $slot=None
    $part=None
  choice("flea_market_buy_bot_part_done",pos=17,key="cancel") "Back"
  return

label flea_market_buy_bot_part(part):
  header "[flea_market] - Buying bot part"
  $part=flea_market.parts_for_sale.pop(eval(part))
  $workshop.add_item(part)
  "You buy {mark}[part]{/}."
  $part=None
  choice ("flea_market_buy_bot_part_done") "Continue"
  return

label flea_market_buy_bot_part_done:
  $flea_market.parts_for_sale=None
  return "<<<"
