init python hide:
  @random_event("home_work")
  def home_work_none():
    return None,30

  @random_event("home_work")
  def home_work_repair_order():
    if home.available_capsules>0:
      return "home_work_event_repair_order",10

  @random_event("home_work")
  def home_work_buy_part():
    return "home_work_event_buy_part",25

label home_work_event_repair_order:
  ""
  "A client approached and asked you to repair the broken bot. There is no rush; final state is also not really important, as long as the bot is functional. A client offers you [money_str[1000]] for work."
  choice("home_work_preview_repair_task") "Look at bot"
  choice("advance_time") "Decline"
  return

label home_work_event_buy_part:
  ""
  "Some dirty junkie approached and offered you some bot part. {say}Not red, boss! Found at a dump site.{/} Well, it's not completely broken and you surely will have it much cheaper than on the streets."
  $part=generate_bot_part("junkie_part","all")
  $part_price=randint(50,250)
  python:
    part_rate=""
    if not game.hardcore:
      if mc.has_stat("expertise_"+part.id) or game.difficulty==1:
        part_rate=", rate: {mark}"+part.rate+"{/}"
      else:
        part_rate=", rate: {info}?{/}"
  ""
  "It's [part.slot] - {mark}[part]{/}[part_rate], he wants [money_str[part_price]] for it."
  if mc.money<part_price:
    ""
    "You tell you don't need it right now. Would be a shame to admit you don't have such pocket change. Crap, it's annoying to be poor."
  $quests.where_to_get_bot_parts.add_method("home_work","sometimes people offer you parts when you {mark}work at [home]{/}")
  choice("home_work_buy_bot_part:"+part.id,cost=[("money",part_price)]) "Accept"
  choice("advance_time") "Decline"
  $part=None
  return

label home_work_buy_bot_part(part):
  $notify.disable()
  $part=find_item_cls(part)()
  $part.apply_damage(randint(5,95),minimal_integrity=1)
  $notify.enable()
  header "[home] - Working"
  "You buy {mark}[part]{/} and place it to inventory to check later. It's sure not new, but actual state is hard to tell just by looking at it."
  $workshop.add_item(part)
  $part=None
  choice("advance_time") "Continue"
  return

label home_work_preview_repair_task:
  python:
    notify.disable()
    bot=generate_bot("repair_task","cheap")
    while not bot.chassis.is_disabled:
      for slot in bot.outfit_slots:
        bot.chassis[slot].apply_damage(randint(5,50))
    notify.enable()
  header "[home] - Working"
  "You ask client to show scans before you decide, in few minutes you have basic information about bot in question."
  ""
  $act.add_screen("bot_preview",bot.id,("info","-psychocore","chassis","-stats","-skills","-traits","parts","-parts_desc","-defects"))
  choice("home_work_accept_repair_task:{}".format(bot.id)) "Accept"
  choice("home_work_decline_repair_task:{}".format(bot.id)) "Decline"
  $bot=None
  return

label home_work_decline_repair_task(bot):
  $find_character(bot).remove()
  return "advance_time"

label home_work_accept_repair_task(bot):
  header "[home] - Working"
  python:
    notify.disable()
    bot=find_character(bot)
    home.add_sexbot(bot)
    bot.add_role("repair_order")
    notify.enable()
  "You accept an offer and soon the bot is delivered to your workshop. There is no rush, but it will occupy a bot capsule, so you shouldn't delay repair for too long."
  $bot["repair_order_quest_id"]=quests.start_quest("repair_order",bot.id).id
  choice("advance_time") "Continue"
  $bot=None
  return
