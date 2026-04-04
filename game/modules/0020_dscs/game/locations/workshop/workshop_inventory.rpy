init python:
  combine_items_into_stacks=True

  def filter_items(items,filter,respect_dns=True):
    rv=[]
    if isinstance(filter,BotPart):
      for item in items:
        if item.id==filter.id:
          if item.integrity==filter.integrity:
            if item.defects==filter.defects:
              if not respect_dns or not item.do_not_sell:
                rv.append(item)
    elif isinstance(filter,str):
      for item in items:
        if item.id==filter:
          if not respect_dns or not item.do_not_sell:
            rv.append(item)
    elif callable(filter):
      for item in items:
        if filter(item):
          if not respect_dns or not item.do_not_sell:
            rv.append(item)
    return rv

  def combine_items(items):
    if combine_items_into_stacks:
      perfect={}
      rv=[]
      for n,item in enumerate(items):
        if not item.defects and item.integrity==100:
          if item.id in perfect:
            rv[perfect[item.id]][0]+=1
          else:
            perfect[item.id]=len(rv)
            rv.append([1,n,item])
        else:
          rv.append([1,n,item])
      return rv
    else:
      return [(1,n,item) for n,item in enumerate(workshop.inventory)]

  def prepare_workshop_inventory(shelf,items_per_page):
    inventory=combine_items(workshop.inventory)
    shelf=int(shelf or 0)
    if len(inventory)<=shelf*items_per_page:
      shelf=max(0,shelf-1)
    items=inventory[shelf*items_per_page:(shelf+1)*items_per_page]
    total=(len(inventory)+(items_per_page-1))//items_per_page
    if total>1:
      prev="workshop_inventory:"+str((shelf-1)%total)
      next="workshop_inventory:"+str((shelf+1)%total)
    else:
      prev=None
      next=None
    return shelf,items,prev,next,total

define workshop_inventory_items_per_page=6

label workshop_inventory(inventory_shelf=0):
  $inventory_shelf,shelf_items,prev_shelf,next_shelf,total_shelves=prepare_workshop_inventory(inventory_shelf,workshop_inventory_items_per_page)
  header "[workshop] - Inventory"
  if shelf_items:
    $shelf_str="Shelf {mark}#"+str(inventory_shelf+1)+"{/} of "+str(total_shelves)
    center "[shelf_str]"
    ""
    $shelf_items=shelf_items+[None]*(workshop_inventory_items_per_page-len(shelf_items))
    $act.add_screen("chassis_parts_info",shelf_items[:],True,item_caption="Shelf #"+str(inventory_shelf+1)+", part {mark}#%s{/}")
    $part_n=0
    while shelf_items:
      $part_n+=1
      $part=shelf_items.pop(0)
      if part:
        $part_count,part_inv_n,part=part
        choice(">>>workshop_inventory_part:"+str(part_inv_n)) "#[part_n] [part]"
    $part=None
  else:
    "You check inventory and see lots of empty shelves. You probably should clean these some day. Probably..."
  choice(prev_shelf,pos=12,key="z") "Prev shelf"
  choice(next_shelf,pos=13,key="x") "Next shelf"
  if workshop.inventory:
    choice(">>>workshop_sort_items",pos=14,key="s",cost=[("energy",1)]) "Sort items"
  else:
    choice(None,pos=14,key="s",hint="{hint}inventory empty{/}") "Sort items"
  if workshop.inventory:
    choice(">>>workshop_sell_items",pos=15) "Sell items"
  else:
    choice(None,pos=15,hint="{hint}inventory empty{/}") "Sell items"
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label workshop_sort_items:
  header "[workshop]"
  "You spend some time sorting items by category and state."
  
## 0.14 change sort to 'by rating' instead of 'by name' - code provided by 'nobodyzeroone' onF95Zone  
## was:  $workshop.inventory.sort(key=lambda item:(find_item_slot(item.slot).name,item.name.lower(),item.id,-item.integrity,len(item.defects)))
  $workshop.inventory.sort(key=lambda item:(find_item_slot(item.slot).name,item.rate.replace("S","\0"),item.id,-item.integrity,len(item.defects)))

  choice("<<<") "Continue"
  return

label workshop_sell_items:
  header "[workshop] - Sell items"
  $assistants=active_bots_with_role_tag("shopkeeper")
  if assistants:  ##  you have at least one shopkeeper
    "With nearly insatiable demand you can sell your whole inventory, especially if you go below average market price."
  else:           ##  you have no shopkeepers
    "With nearly insatiable demand you can sell your whole inventory, especially if you go below average market price. A shopkeeper bot might make this easier."
  $parts_to_sell=[]
  choice(">>>workshop_sell_items_rate:F") "Rate F"
  choice(">>>workshop_sell_items_rate:FE") "Rate E-"
  choice(">>>workshop_sell_items_rate:FED") "Rate D-"
  choice(">>>workshop_sell_items_rate:FEDC") "Rate C-"
  choice(">>>workshop_sell_items_rate:FEDCB") "Rate B-"
  choice(">>>workshop_sell_items_rate:FEDCBA") "Rate A-"
  choice(">>>workshop_sell_items_rate:FEDCBAS") "All items"
  choice(">>>workshop_sell_items_irrepairable") "Irrepairable items"
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label workshop_sell_items_rate(rates_to_sell):
  $parts_to_sell=filter_items(workshop.inventory,lambda part: part.rate in rates_to_sell)
  jump workshop_sell_items_confirm

label workshop_sell_items_irrepairable:
  $parts_to_sell=filter_items(workshop.inventory,lambda part: part.has_irrepairable_defects)
  jump workshop_sell_items_confirm

label workshop_sell_items_confirm:
  header "[workshop] - Sell items"
  if parts_to_sell:
    $parts_count=len(parts_to_sell)
    $part_n=0
    while part_n<len(parts_to_sell):
      $part=parts_to_sell[part_n]
      if part.rate<>"":                         ##  added conditional in 0.2.0 to bypass missing parts if they end up here via a bug!
        $part_price=bot_part_price_function(part,flat_price_below=10)
        $price_min=max(1,int(round(part_price*0.25)))
        $price_max=max(1,int(round(part_price*0.75)))
        "{info}[part.slot] - {mark}[part]{/} - price range: [money_str[price_min]]-[money_str[price_max]]{/}"
      $part_n+=1
    ""
    if parts_count>1:
      "Do you want to sell {mark}[parts_count]{/} items?"
    else:
      "Do you want to sell {mark}[part]{/}?"
    $part=None
    choice("workshop_sell_items_do") "Yes"
    choice("<<<") "No"
  else:
    "There is no such items."
    choice("<<<") "Back"
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label workshop_sell_items_do:
  header "[workshop] - Sell items"
  $price=0
  $parts_count=len(parts_to_sell)
## 0.9.n add recycling comment if there are irrepairable parts being sold
  $recycle_part=0                           ## 0.9.n add flag to be set if there is at least 1 irrepairable part being sold
  $normal_part=0                            ## 0.9.n add flag to be set if there is at least 1 repairable part being sold
  while parts_to_sell:
    $part=parts_to_sell.pop(0)
    if part.rate<>"":                         ##  added conditional in 0.2.0 to bypass missing parts if they end up here via a bug!
      if part.has_irrepairable_defects:       ## 0.9.n found an irrepairable part, set the new flag
        $recycle_part=1
      else:
        $normal_part=1
      $part_price=bot_part_price_function(part,flat_price_below=10)
      $price_min=max(1,int(round(part_price*0.25)))
      $price_max=max(1,int(round(part_price*0.75)))
      $price+=randint(price_min,price_max)
    $workshop.remove_item(part)
  if recycle_part==1:                                ## 0.9.n add comment about recycling
    if normal_part==0:                               ## 0.9.n you are selling only irrepairable parts
      "You were lucky to find a scrap recycling dealer on the grey net willing to pay you something for irrepairable parts."
    else:                                            ## 0.9.n you are selling a mix of irrepairable and normal parts
      "You were lucky to find deals on the grey net for all of the parts including scrap recycling dealers who will pay you for the irrepairable parts."
    ""
  else:                                              ## 0.9.n no irrepairable parts so no need to mention recycling
    "You found deals on the grey net for all of the parts."
    ""
  if parts_count>1:
    "You sold {mark}[parts_count]{/} items and earned [money_str[price]]."
  else:
    "You sold {mark}[part]{/} and earned [money_str[price]]."

  $mc.money+=price
  $part=None
  choice("<<<") "Continue"
  choice("goto_home",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return
