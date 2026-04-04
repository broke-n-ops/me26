label workshop_inventory_part(part_n):
  python:
    part_n=int(part_n)
    part=workshop.inventory[part_n]
    if combine_items_into_stacks and not part.defects and part.integrity==100:
      same_parts=[(part_n,invp) for part_n,invp in enumerate(workshop.inventory) if invp==part and not invp.defects and invp.integrity==100]
      invp=None
    else:
      same_parts=[(part_n,part)]
    same_type_part_count=len([1 for invp in workshop.inventory if invp.id==part.id])
    part_count=len(same_parts)
    part_n,part=same_parts[-1]
  $slot=find_item_slot(part.slot)
  header "[workshop] - Part info"
  if part_count>1:
    "Part: {mark}[part]{/}{size=-8}x{/}{mark}[part_count]{/}."
  else:
    "Part: {mark}[part]{/}."
  if same_type_part_count>1:
    extend " You have {mark}[same_type_part_count]{/} of these"
    if same_type_part_count>part_count:
      extend " in various conditions."
    else:
      extend "."
  "Category: {mark}[slot]{/}. Rate: {mark}[part.rate]{/}."
  $slot=None
  ""
  "[part.description]"
  ""
  if part.integrity==part.integrity_cap and part.integrity_cap!=100:
    "Integrity: {mark}[part.integrity]%%{/} {size=-8}{info}({bad}[part.integrity_cap]{/}/100){/}{/} -  defects do not allow full repair"
  else:
    "Integrity: {mark}[part.integrity]%%{/} {size=-8}{info}([part.integrity_cap]/100){/}{/}"
  if part.integrity==100 and not part.defects:
    "Part in {mark}perfect condition{/}, no repair required."
  if part.integrity<part.integrity_cap and part.rate<>"":           ##  added conditional for part.rate in 0.2.0
    choice(">>>workshop_fix_part:"+str(part_n)) "Fix part"
  else:
    choice(None) "Fix part"
  $defects=[(defect_n,defect) for defect_n,defect in enumerate(part.defects)]
  ""
  "Defects:"
  if defects:
    $defects.sort(key=lambda x: (100-x[1].integrity_cap,x[1].fix_progress))
    if defects[-1][1].repairable:
      choice(">>>workshop_fix_part_defect:"+str(part_n)+","+str(defects[-1][0])) "Fix defect"
    else:
      choice(None) "Fix defect"
    while defects:
      $defect_n,defect=defects.pop(0)
      $cap_color="mark" if defect.integrity_cap==100 else "bad"

      if defect.repairable:
        "{bad}[defect]{/}, integrity cap: {[cap_color]}[defect.integrity_cap]%%{/}, fix progress: {mark}[defect.fix_progress]%%{/}"
      else:
        "{bad}[defect]{/}, integrity cap: {[cap_color]}[defect.integrity_cap]%%{/}, {bad}irrepairable{/}"
      "{size=-8}{info}[defect.description]{/}{/}"
  else:
    "{info}There is no defects in this part.{/}"
    choice(None) "Fix defect"
  if part.is_destroyed:  ## 0.9.n changed text for recycling, not sure when if ever this code is executed
    ""
    "Part is too damaged to be of any use so you decide to look for a scrap recycling dealer who can make use of it."
    choice("workshop_part_throw_away:"+str(part_n)) "Throw away"
  elif part.damage_on_remove=="missing":                          ##  added in 0.2.0 to automatically discard missing parts that end up in inventory
    ""
    "That's funny, I have an empty spot on the shelf. Oh well, doesn't matter."
    $workshop.remove_item(part)
    $part=None
    choice("<<<") "Continue"
  else:
    $part_price=bot_part_price_function(part,flat_price_below=10)
    $price_min=max(1,int(round(part_price*0.25)))
    $price_max=max(1,int(round(part_price*0.75)))
    ""
## 0.9.n added 3 lines below and indented the text that used to be used all the time
    if part.has_irrepairable_defects:
      "You're pretty sure you can find a scrap recycling dealer on the grey net who might give you something for this irrepairable part."
    else:
      "You think you can receive something in the [money_str[price_min]] - [money_str[price_max]] range for it if you check grey net. Maybe some shops can offer more."
    if part.do_not_sell:
      "This item is marked {mark}do-not-sell{/}."
      choice(None,hint="{hint}not allowed{/}") "Sell"
      if combine_items_into_stacks:
        choice(None,hint="{hint}not allowed{/}") "Sell stack"
      choice(None,hint="{hint}not allowed{/}") "Sell all"
      choice(">>>workshop_part_toggle_dns:"+str(part_n),hint="toggle do-not-sell",pos=12) "DNS: on"
    else:
      choice("workshop_part_sell:"+str(part_n)) "Sell"
      if combine_items_into_stacks:
        if part_count>1:
          choice("workshop_part_sell_stack:"+str(part_n)) "Sell stack"
        else:
          choice(None) "Sell stack"
      if len(filter_items(workshop.inventory,part.id))>0:
        choice("workshop_part_sell_all:"+str(part_n)) "Sell all"
      else:
        choice(None) "Sell all"
      choice(">>>workshop_part_toggle_dns:"+str(part_n),hint="toggle do-not-sell",pos=12) "DNS: off"
  $defect=None
  $part=None
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label workshop_part_toggle_dns(part_n):
  $part=workshop.inventory[int(part_n)]
  $part.do_not_sell=not part.do_not_sell
  $part=None
  return "<<<"

label workshop_part_throw_away(part_n):
  $part=workshop.inventory[int(part_n)]
  header "[part] - Throwing away"  ## 0.9.n changed text for recycling, not sure when if ever this code is executed
  "You find a scrap recycling dealer on the grey net who can use the part and a delivery bot takes the useless [part] away."
  $workshop.remove_item(part)
  $part=None
  choice("<<<") "Continue"
  return

label workshop_part_sell(part_n):
  $part_n=int(part_n)
  $part=workshop.inventory[part_n]
  $part_price=bot_part_price_function(part,flat_price_below=10)
  $price_min=max(1,int(round(part_price*0.25)))
  $price_max=max(1,int(round(part_price*0.75)))
  $price=randint(price_min,price_max)
  header "[part] - Selling"
## 0.9.n add 3 lines and indent the line that was used all the time, adjusted text for grammer too
  if part.has_irrepairable_defects:
    "You found a scrap recycling dealer willing to give you something for the irrepairable part. After a delivery bot takes the {mark}[part]{/} you receive the money you were promised."
  else:
    "You search the grey net for any offers for {mark}[part]{/}. Soon enough, you find an offer for [money_str[price]] and take it. After a delivery bot takes the {mark}[part]{/} you receive the money you were promised."
  $mc.money+=price
  $workshop.remove_item(part)
  $part=None
  choice("<<<") "Continue"
  return

label workshop_part_sell_stack(part_n):
  $part_n=int(part_n)
  $parts_to_sell=filter_items(workshop.inventory,workshop.inventory[part_n])
  jump workshop_part_sell_bulk

label workshop_part_sell_all(part_n):
  $part_n=int(part_n)
  $parts_to_sell=filter_items(workshop.inventory,workshop.inventory[part_n].id)
  jump workshop_part_sell_bulk

label workshop_part_sell_bulk:
  $part=parts_to_sell[0]
  header "[part] - Selling"
  "You search the grey net for offers to buy all of the {mark}[part]{/} you have. Soon enough, you find reasonable offers and make arrangements to sell everything."  ## 0.9.n edited
  $price=0
  while parts_to_sell:
    $part=parts_to_sell.pop(0)
    $part_price=bot_part_price_function(part,flat_price_below=10)
    $price_min=max(1,int(round(part_price*0.25)))
    $price_max=max(1,int(round(part_price*0.75)))
    $part_price=randint(price_min,price_max)
    $workshop.remove_item(part)
    $price+=part_price
    "{info}Sold {mark}[part]{/} for [money_str[part_price]].{/}"
  "After a number of delivery bots take the goods you receive the money you were promised"  ##0.9.n grammer
  $mc.money+=price
  $part=None
  choice("<<<") "Continue"
  return
