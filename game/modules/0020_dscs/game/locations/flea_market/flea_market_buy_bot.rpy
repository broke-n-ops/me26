## updated in 0.8.1
define flea_market_generate_bot_mind_table=[
  ["bot_combat",(-80000,10000)],
  ["bot_electronics",(-80000,10000)],
  ["bot_mechanics",(-80000,10000)],
  ["bot_sex",(-80000,25000)],        ## was 25000
  ["bot_social",(-80000,25000)],     ## was 25000
  ]

define flea_market_generate_bot_seals_table={
  "oral": (-1000,5000),
  "vaginal": (-1000,2500),
  "anal": (-1000,1000),
  }

define flea_market_bot_with_skills_chance=10

##  ADDED BY SQUIRREL IN 'DUMP_SITE_SCAVENTE_EVENTS.RPY': PARTS CAN CHANGE RANDOMLY WHEN BOTS ARE SCAVENGED PLUS "MISSING PARTS"
##  PASTED IN HERE FOR REFERENCE ONLY, THEY ARE GLOBAL
# # define new_part_id="sr"          ##  new part id
# # define new_part_level=1          ##  new part level
# # definbe new_part_name="a"        ##  new part name
# # define old_part_id="sr"          ##  old part id
# # define old_part_level=1          ##  old part level
# # define old_part_name="a"         ##  old part name - this one wasn't needed
# # define working_slot="a"          ##  slot being worked on


init python:
  def flea_market_generate_bots_for_sale():
    notify.disable()
    rv=[]
    for n in range(randint(2,5)):
      flea_bot=generate_bot("flea_market_buy_bot","cheap","nice")

##      print "flea generated bot: ",flea_bot                       ##DEBUG LINE
##      print "flea bot model: ",flea_bot.model_id                  ##DEBUG LINE
##      print "flea bot model name: ",flea_bot.model_name           ##DEBUG LINE

##  ADDED BY SQUIRREL: PARTS CAN CHANGE RANDOMLY WHEN BOTS ARE PURCHASED AT THE FLEA MARKET PLUS "MISSING PARTS"

      for slot in flea_bot.outfit_slots:
##        print "flea START LOOP"                                   ##DEBUG LINE
        working_slot=slot
##        print "flea working slot:",working_slot                   ##DEBUG LINE
        srf_part_weight=randint(1,100)
 
##        srf_part_weight=86    ##  THIS LINE IS FOR TESTING, SET THE DESIRED OUTCOME!!!                ##TEST LINE

        if srf_part_weight>70:                                    ##  FALL THROUGH KEEPS DEFAULT PART - 70%
          old_part_id=flea_bot.item_on_slot(working_slot)
##          print "flea old part: ",old_part_id                     ##DEBUG LINE
          old_part_level=old_part_id.rate_level
##          print "flea old part level: ",old_part_level            ##DEBUG LINE
          if srf_part_weight<=76:                                 ##  UPGRADE 1 LEVEL - 6%
            if old_part_level<7:                                  ##  can increase 1
              new_part_level=old_part_level+1
##              print "flea new part level: ",new_part_level
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)
##              print "flea new_part_id",new_part_id                ##DEBUG LINE
              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                flea_bot.equip(new_part_id)
                new_part_name=flea_bot.chassis[working_slot]
                new_part_name.owner=flea_bot
                flea_bot.add_item(new_part_name)
                flea_bot.remove_item(old_part_id)
          elif srf_part_weight<=79:                               ##  UPGRADE 2 LEVELS - 3%
            if old_part_level<6:                                  ##  can increase 2
              new_part_level=old_part_level+2
##              print "flea new part level: ",new_part_level
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)
##              print "flea new_part_id",new_part_id                ##DEBUG LINE
              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                flea_bot.equip(new_part_id)
                new_part_name=flea_bot.chassis[working_slot]
                new_part_name.owner=flea_bot
                flea_bot.add_item(new_part_name)
                flea_bot.remove_item(old_part_id)
            elif old_part_level<7:                                ##  can increase 1
              new_part_level=old_part_level+1
##              print "flea new part level: ",new_part_level
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)
##              print "flea new_part_id",new_part_id                ##DEBUG LINE
              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                flea_bot.equip(new_part_id)
                new_part_name=flea_bot.chassis[working_slot]
                new_part_name.owner=flea_bot
                flea_bot.add_item(new_part_name)
                flea_bot.remove_item(old_part_id)
          elif srf_part_weight<=91:                               ##  DOWNGRADE 1 LEVEL - 12%
            if old_part_level>1:
              new_part_level=old_part_level-1
##              print "flea new part level: ",new_part_level
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)
##              print "flea new_part_id",new_part_id                                                          ##DEBUG LINE
              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                flea_bot.equip(new_part_id)
                new_part_name=flea_bot.chassis[working_slot]
                new_part_name.owner=flea_bot
                flea_bot.add_item(new_part_name)
                flea_bot.remove_item(old_part_id)
          elif srf_part_weight<=97:                               ##  DOWNGRADE 2 LEVELS - 6%
            if old_part_level>2:                                  ##  can decrease 2
              new_part_level=old_part_level-2
##              print "flea new part level: ",new_part_level
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)
##              print "flea new_part_id",new_part_id                                                          ##DEBUG LINE
              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                flea_bot.equip(new_part_id)
                new_part_name=flea_bot.chassis[working_slot]
                new_part_name.owner=flea_bot
                flea_bot.add_item(new_part_name)
                flea_bot.remove_item(old_part_id)
            elif old_part_level>1:                                ##  can decrease 1
              new_part_level=old_part_level-1
##              print "flea new part level: ",new_part_level
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)
##              print "flea new_part_id",new_part_id                                                          ##DEBUG LINE
              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                flea_bot.equip(new_part_id)
                new_part_name=flea_bot.chassis[working_slot]
                new_part_name.owner=flea_bot
                flea_bot.add_item(new_part_name)
                flea_bot.remove_item(old_part_id)
          else:                                                   ##  INSERT MISSING PART AND APPLY DAMAGE - 3%
            new_part_id=scavenge_missing_part(working_slot)
##            print "flea new part: ",new_part_id                                                             ##DEBUG LINE
            if new_part_id<>"abort_substitution":                 ##  abort when non-standard slot
              flea_bot.equip(new_part_id)
              new_part_name=flea_bot.chassis[working_slot]
              new_part_name.owner=flea_bot
              flea_bot.add_item(new_part_name)
              flea_bot.remove_item(old_part_id)
              flea_bot.chassis[working_slot].apply_damage(1000)   ##  CAUSES IRREPAIRABLE DAMAGE IN ALL CASES
##        print "flea END LOOP"                                                                               ##DEBUG LINE

      flea_bot.inventory.clear()                                ##  BUG FIX in v0.2.1 - deletes removed parts from bot's inventory

      if flea_bot:
        for slot in flea_bot.outfit_slots:
##          flea_bot.chassis[slot].apply_damage(randint(0,99),minimal_integrity=1)      ##  revised this line, see next line
          flea_bot.chassis[slot].apply_damage(randint(-25,60),minimal_integrity=1)    ##  UPDATED in 0.2.1 to have some un-damaged parts
        if randint(0,100)<flea_market_bot_with_skills_chance:
          if flea_bot.chassis.cpu.integrity>0:
            process_event("generate_bot_mind",flea_bot,"flea_market",flea_market_generate_bot_mind_table)
        generate_bot_warranty_seals(flea_bot,flea_market_generate_bot_seals_table)
        rv.append(flea_bot)
    notify.enable()
    return rv

init python:
  def label_flea_market_buy_bot_action_info(**kwargs):
## CHANGE IN SR24 v0.4.n
    if home.available_capsules>=1 or workshop.available_space>=1:
      kwargs["cost"]=[("energy",1)]
    else:
      kwargs["action"]=None
      kwargs["cost"]=["{hint}shop full{/}"]
    return kwargs

label flea_market_buy_bot:
  $flea_market.bots_for_sale=flea_market_generate_bots_for_sale()
  $flea_market["search_for_bots_now"]=True
  return "flea_market_buy_bot_list"

label flea_market_buy_bot_list:
  header "[flea_market] - Buying bot"
  if flea_market["search_for_bots_now"]:
    "You look around, searching for sexbots for sale, ignoring tons of outright junk. After quite some walking and haggling, you have a list of interesting offers. Considering quick turnover, you doubt bots will be kept for long, so if you like something, you should buy it now."
    $flea_market["search_for_bots_now"]=None
  else:
    "There are some interesting offers. Considering quick turnover, you doubt bots will be kept for long, so if you like something, you should buy it now."
  ""
  $bot_n=0
  while bot_n<len(flea_market.bots_for_sale):
    $flea_bot=flea_market.bots_for_sale[bot_n]
    $bot_n+=1
    $bot_price=max(1,int(round(bot_price_function(flea_bot,skill_mods=bot_price_skills_unimportant)*1.5)))
    $money_tag="{bad}" if bot_price>mc.money else "{mark}"
    "#[bot_n] - {mark}[flea_bot]{/}, model: {mark}[flea_bot.model_name]{/}, price: [money_tag][money_str[=bot_price]]{/}"
    choice(">>>flea_market_buy_bot_preview:{},{}".format(bot_n-1,bot_price)) "#[bot_n] - [flea_bot]"
    $flea_bot=None
  choice("flea_market_buy_bot_done",pos=17,key="cancel") "Back"
  return

label flea_market_buy_bot_preview(bot_n_and_price):
  python:
    bot_n,sep,price=bot_n_and_price.partition(",")
    bot_n=int(bot_n)
    flea_bot=flea_market.bots_for_sale[bot_n]
    price=int(price)
  header "[flea_market] - Buying bot"
  $act.add_screen("bot_preview",flea_bot.id,("info","psychocore","chassis","stats","skills","traits","parts","-parts_desc","-defects"))
  choice("flea_market_buy_bot_do:{}".format(bot_n),cost=[("money",price)]) "Buy [flea_bot.name]"
  choice ("<<<") "Back"
  choice ("<<<",pos=17,key="cancel") "Back"
  $bot=None
  return

label flea_market_buy_bot_do(flea_bot):      ## function receives 'flea_bot' parameter, internally use 'add_bot'
  header "[flea_market] - Buying bot"
  $add_bot=flea_market.bots_for_sale.pop(int(flea_bot))
## CHANGE IN SR24 v0.4.name
##  $home.add_sexbot(add_bot)
  call sr24_add_bot_do(add_bot)          ## RENPY SYNTAX: add bot to capsule if available, storage space if necessary
  "You buy {mark}[add_bot]{/}, model {mark}[add_bot.model_name]{/}."
  $add_bot=None
  choice ("<<<flea_market_buy_bot_done") "Continue"
  return

label flea_market_buy_bot_done:
  while flea_market.bots_for_sale:
    $flea_bot=flea_market.bots_for_sale.pop()
    $flea_bot.remove()
    $flea_bot=None
  $flea_market.bots_for_sale=None
  return "<<<"