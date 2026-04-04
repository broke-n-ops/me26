##=========INIT VARIABLES=========
init python:
  shpkpr_bot_new_assignment=0      ## 0.10.n - counter for bots just assigned

##============FUNCTIONS============

label role_shopkeeper_sell_items:
  if not now("night"):
    $assistants=active_bots_with_role_tag("shopkeeper")

## 0.10.n change to avoid 'double dipping' roles
    $shpkpr_bot_new_assignment=0             ## clear flag before starting
    $bot_count=0
    while bot_count<len(assistants):    ## go through assistants to remove ones just assigned

##      $print "BEGIN LOOP - bot_count: ",bot_count, "len(assistants): ",len(assistants)

      $temp_bot=assistants[bot_count]

##      $print "bot_count: ",bot_count,"temp_bot[0]: ",temp_bot[0],"temp_bot[0].mt_just_assigned: ",temp_bot[0].mt_just_assigned

      if temp_bot[0].shpkpr_just_assigned==1:  ## if assigned role this turn
        $shpkpr_bot_new_assignment+=1          ## increment count of bots just assigned
##        $temp_bot[0].shpkpr_just_assigned=0    ## reset flag - MOVED TO REST, SLEEP, WORK
        $assistants.pop(bot_count)             ## remove bot from assistants - do not increment counter
      else:
        $bot_count+=1                          ## increment bot count for while loop

##      $print "END LOOP - bot_count: ",bot_count, "len(assistants): ",len(assistants)

## 0.10.n end of insertion

    $assistants_bonus=sum(((assistant.bot_electronics.level+assistant.bot_mechanics.level+assistant.bot_social.level)*role_efficiency for assistant,role_efficiency in assistants))/3.0
    if assistants and assistants_bonus>0:
##      ""
      $assistant=randchoice(assistants)[0]
##  GRAPHICS
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      if workshop["do_not_sell"]:                  ##  this is when the workshop is marked 'do not sell'
        if assistant.gender=="female":
          $sk_imagenumber=random.randint(9,16)     ##  first 8 images omit female bots selling parts
        else:
          $sk_imagenumber=random.randint(21,24)    ##  images 17-20 omit male bot selling parts
      else:                                        ##  selling parts is active
        if assistant.gender=="female":
          $sk_imagenumber=random.randint(1,16)
        else:
          $sk_imagenumber=random.randint(17,24)
      $action_image="roles shopkeeper srsk_"+str(sk_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
##  TEXT
      $act.set_block("c")

## 0.12.n modified rep gains and added text explaining it
      if workshop["do_not_sell"]:                                      ## shopkeepers DON'T sell parts
        if len(assistants)>1:
          "{mark}[assistant]{/} and other shopkeeper bots operated your shop and helped clients with minor problems. Customers are impressed that your bots can run the shop."
          $mc.money+=randint(25*assistants_bonus,75*assistants_bonus)  ## moved here so it's above the rep gain (has to be put in 3 times though)
          if len(assistants)>2:                                        ## 3 or more shopkeepers 
            $temp=calc_pr_rep_gain("rep_mc_trainer","m_g")             ## large gain
          else:                                                        ## must be 2 shopkeepers
            $temp=calc_pr_rep_gain("rep_mc_trainer","s_g")             ## medium gain
          $mc.give_xp("rep_mc_trainer",temp)
        else:                                                          ## 1 shopkeeper
          "{mark}[assistant]{/} operated your shop and helped clients with minor problems. Customers are impressed that your bot can run the shop."
          $mc.money+=randint(25*assistants_bonus,75*assistants_bonus)  ## moved here so it's above the rep gain
          $temp=calc_pr_rep_gain("rep_mc_trainer","xs_g")              ## small gain
          $mc.give_xp("rep_mc_trainer",temp)
      else:                                                            ## shopkeepers sell parts
        if len(assistants)>1:
          "{mark}[assistant]{/} and other shopkeeper bots operated your shop, helped clients with minor problems, and sold items from inventory. Customers are impressed that your bots can run the shop."
          $mc.money+=randint(25*assistants_bonus,75*assistants_bonus)  ## moved here so it's above the rep gain
          if len(assistants)>2:                                        ## 3 or more 
            $temp=calc_pr_rep_gain("rep_mc_trainer","m_g")             ## large gain
          else:                                                        ## must be 2
            $temp=calc_pr_rep_gain("rep_mc_trainer","s_g")             ## medium gain
          $mc.give_xp("rep_mc_trainer",temp)
        else:                                                          ## must be 1
          "{mark}[assistant]{/} operated your shop, helped clients with minor problems, and sold items from inventory. Customers are impressed that your bot can run the shop."
          $temp=calc_pr_rep_gain("rep_mc_trainer","xs_g")              ## small gain
          $mc.give_xp("rep_mc_trainer",temp)
        "{size=-22} {/}"                                               ## small line feed to separate working from selling parts
      if not workshop["do_not_sell"]:
        python:
          parts_to_sell=filter_items(workshop.inventory,lambda part: part.rate in "FEDC")
          parts_to_sell_count=int(round(assistants_bonus/(randint(30,50)*0.1)))
          parts_sold_money=0
        while parts_to_sell_count>0 and parts_to_sell:
          python:
            parts_to_sell_count-=1
            part=randchoice(parts_to_sell)
            parts_to_sell.remove(part)
            part_price=bot_part_price_function(part,flat_price_below=25)
            price_min=max(1,int(round(part_price*0.75)))
            price_max=max(1,int(round(part_price*1.25)))
            price=randint(price_min,price_max)
            parts_sold_money+=price
            workshop.remove_item(part)
          "{info}{i}{size=-8}Sold {mark}[part]{/} for [money_str[price]].{/}{/}{/}"
        if parts_sold_money>0:
          $mc.money+=parts_sold_money
      python:
        for assistant,role_efficiency in assistants:
          assistant.give_xp("bot_mechanics",max(0,randint(-100,50)))
          assistant.give_xp("bot_electronics",max(0,randint(-100,50)))
          assistant.give_xp("bot_social",max(0,randint(-100,50)))
    
## 0.10.n add comment if shopkeepers just assigned only when there are no assistants
    if not assistants:                               ## no shopkeepers, show MC
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $sk_imagenumber=random.randint(25,32)
      $action_image="roles shopkeeper srsk_"+str(sk_imagenumber)
      center "{image=[action_image]@400x600}"
##  TEXT
      $act.set_block("c")
      if shpkpr_bot_new_assignment==0:
        "Maybe I should have {mark}Shopkeeper{/} bots and keep them at home in capsules so they can help run the shop."
      elif shpkpr_bot_new_assignment==1:
        "I just assigned a bot the {mark}Shopkeeper{/} role so in the future they will help me run the shop."
      elif shpkpr_bot_new_assignment>1:
        "I just assigned bots the {mark}Shopkeeper{/} role so in the future they will help me run the shop."
    $act.end_block()  ## this resets the 2 column screen to a single screen
    $part=None
    $assistant=None
    $assistants=None
    ""                ## add a line before the next item is displayed
  return

label role_shopkeeper_help_run_shop:                   ## only text messages when you work
  $assistants=active_bots_with_role_tag("shopkeeper")  ## need to know how many shopkeepers and how many just assigned

##  $print "assistants BEFORE just assigned test"
##  $print assistants

  $shpkpr_bot_new_assignment=0                         ## clear flag before starting
  $bot_count=0
  while bot_count<len(assistants):                     ## go through assistants to remove ones just assigned
    $temp_bot=assistants[bot_count]
    if temp_bot[0].shpkpr_just_assigned==1:            ## if assigned role this turn
      $shpkpr_bot_new_assignment+=1                    ## increment count of bots just assigned
      $assistants.pop(bot_count)                       ## remove bot from assistants - do not increment counter
    else:
      $bot_count+=1                                    ## increment bot count for while loop

##  $print "assistants AFTER just assigned test"
##  $print assistants
##  $print "just assigned: ",shpkpr_bot_new_assignment

  if assistants:                                   ## there is one or more shopkeepers, show them
    $assistant=randchoice(assistants)[0]           ## pick a random assistant for images
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    if workshop["do_not_sell"]:                    ## this is when the workshop is marked 'do not sell'
      if assistant.gender=="female":
        $sk_imagenumber=random.randint(9,16)       ## first 8 images - female bots selling parts
      else:
        $sk_imagenumber=random.randint(21,24)      ## images 17-20 - male bot selling parts
    else:                                          ## selling parts is active
      if assistant.gender=="female":
        $sk_imagenumber=random.randint(1,16)
      else:
        $sk_imagenumber=random.randint(17,24)
    $action_image="roles shopkeeper srsk_"+str(sk_imagenumber)
    center "{image=[action_image]@400x600}"
  else:                                            ## no shopkeepers, show MC
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $sk_imagenumber=random.randint(25,32)
    $action_image="roles shopkeeper srsk_"+str(sk_imagenumber)
    center "{image=[action_image]@400x600}"
##  TEXT
  $act.set_block("c")
  if not assistants:                                   ## no shopkeepers
    if shpkpr_bot_new_assignment==0:                   ## none just assigned
      "Maybe I should have {mark}Shopkeeper{/} bots and keep them at home in capsules, they would be a great help running the shop."
    elif shpkpr_bot_new_assignment==1:                 ## none just assigned
      "I just assigned a bot the {mark}Shopkeeper{/} role so in the future they can help me run the shop."
    elif shpkpr_bot_new_assignment>1:                  ## more than one just assigned
      "I just assigned bots the {mark}Shopkeeper{/} role so in the future they can can help me run the shop."
  elif len(assistants)==1:                             ## one shopkeeper
    "Even when I run the shop myself my {mark}Shopkeeper{/} bot is still a great help as both a Clerk and a Techie"
  elif len(assistants)>1:                              ## multiple shopkeepers
    "Even when I run the shop myself my {mark}Shopkeeper{/} bots are still a great help as both Clerks and Techies"

  $act.end_block()  ## this resets the 2 column screen to a single screen
  $assistant=None
  $assistants=None
  ""                ## add a line before the next item is displayed
  return