init python:
  def prepare_grey_market_logo():
    rv=[
      """  e88'Y88                                 e   e                    888              d8     888 88b 888 88b  dP"b""", 
      """ d888  'Y  888,8,  ,e e,  Y8b Y888P      d8b d8b    ,88,88b 888,8, 888 ee  ,e e,   d88     888 88P 888 88P C8b Y""",
      """C8888 eeee 888 "  d88 88b  Y8b Y8P      e Y8b Y8b   "   888 888 "  888 P  d88 88b d88888   888 8K  888 8K   Y8b """,
      """ Y888 888P 888    888   ,   Y8b Y      d8b Y8b Y8b  ,ee 888 888    888 b  888   ,  888     888 88b 888 88b b Y8D""",
      """  "88 88"  888     "YeeP"    888      d888b Y8b Y8b "88 888 888    888 8b  "YeeP"  888     888 88P 888 88P YbdP """,
      """                             888                                                                                 """,
      """          WELCOME TO         888                                                                                 """,
    ]
    for n,line in enumerate(rv):
      line_color=n/float(len(rv))
      line_color=int(line_color*200)+(255-200)
      line_color="{:02X}".format(line_color)*3
      rv[n]="{color=#"+line_color+"}"+line+"{/}"
    rv="\n".join(rv)
    return rv

style grey_market_logo:
  layout "nobreak"
  font "assets/fonts/clacon2.ttf"
  kerning 0
  line_spacing 0
  outlines []

screen grey_market_logo(logo):
  if renpy.has_image("netconsole grey_market_bbs_logo",True):
    add "netconsole grey_market_bbs_logo" xalign 0.5
  else:
    add FitTextDisplayable(logo,"idle","grey_market_logo",(content_width,999)) xalign 0.5

label netconsole_grey_market_bbs:
  header "[netconsole] - [grey_market]"
  $act.add_screen("grey_market_logo",prepare_grey_market_logo())
  ""
  "The infamous \"{mark}[grey_market]{/}\" is the place to {mark}buy, sell, or trade anything{/}. When you were still at home and complained that you couldn't get parts for your {mark}sexbot hobby{/} your {mark}Dad{/} told you about this and made you promise not to tell your {mark}Mom{/}. Sometimes {mark}Dad{/} is OK!"
  ""
## replaced line in 0.9.n when simplifying grey net bbs and added space
  "Not everything here is legal but you can find links to {mark}hardware, software, services and contacts{/} you wouldn't find normally. Anything you can think of can be found here - {mark}including scams!{/}"
##  "Occasionally people sell bots here but unfortunately the prices are usually out of my reach."
  ""
  "Sometimes {mark}people ask for sexbots with special skills here{/}. When I can get my hands on a sexbot that I can fix and train this is a good source of money!"
  ""
  "Right now this is the {mark}only place that I can afford new parts{/}. I've always been careful and haven't been ripped off yet."

## removed in 0.8.n but it doesn't remove the message from saved games
##  $quests.where_to_get_bots.add_method("grey_market","you can find bots for sale at {mark}[grey_market]{/}, accessible through your {mark}[netconsole]{/}")

  $quests.where_to_sell_bots.add_method("grey_market","you can sell your bots at {mark}[grey_market]{/}, accessible through your {mark}[netconsole]{/}")
  $quests.where_to_get_bot_parts.add_method("grey_market","you can find bot parts for sale at {mark}[grey_market]{/}, accessible through your {mark}[netconsole]{/}")
  choice(">>>netconsole_grey_market_check_offers:trade") "Trade offers"
  choice(">>>netconsole_grey_market_check_offers:offtopic") "Off-topic offers"
  choice("goto_home",pos=16,key="home") "Log out"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label netconsole_grey_market_check_offers(offer_category):
  header "[netconsole] - [grey_market]"
  if offer_category=="trade":
    "You skim through long list of various offers, skipping out-of-your-league ones and outright scams."
  else:
    "Sometimes people post offers for non-commercial activities too. You check interesting ones."
  ""
  $offer_n=0
  $offer_n_id=0
  while offer_n<min(12,len(grey_market.offers)):
    $offer=grey_market.offers[offer_n]
    $offer_n+=1
    if offer.category==offer_category:
      $offer_n_id+=1
      $reward=offer.reward
      $reward_price=offer.reward_price
      "{mark}#[offer_n_id]{/} - [offer.title!i]{size=8}\n {/}"
      choice(">>>netconsole_grey_market_check_offer:"+str(offer_n-1)) "Check #[offer_n_id]"
      $reward=None
      $reward_price=None
    $offer=None
  choice("goto_home",pos=16,key="home") "Log out"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label netconsole_grey_market_check_offer(offer_n):
  $offer=grey_market.offers[int(offer_n)]

##  $print "offer id: ",offer.id

  $request=offer.request
  $reward=offer.reward
  $request_description=offer.request_description
  $reward_description=offer.reward_description
  $request_options=offer.list_request_options(12)
  header "[netconsole] - [grey_market]"
  "[offer.title!i]"
  ""
  $act.start_block("l:(content_width-100)//2 c:100 r:(content_width-100)//2")
  if request_description:
    "Request:"
    "[request_description!i]"
  $act.set_block("r")
  if reward_description:
    "Reward:"
    "[reward_description!i]"
  $act.end_block()
  if request_options:
    if isinstance(request_options,(list,tuple)):
      ""
      "You check your options fitting the request description."
      ""
      $act.add_screen("netconsole_grey_market_request_options",offer,request_options)
      $options=request_options[:]
      $option_n=0
      while options:
        $option=options.pop(0)
        if option[0] in ("part","bot"):
          $option_n+=1
          if option[0]=="part":
            $request_price=bot_part_price_function(option[2],**request.get("price_mods",{}))
          else:
            $request_price=bot_price_function(option[2],**request.get("price_mods",{}))
          $money_reward=0
          python hide:
            for money_reward in offer.reward:
              if isinstance(money_reward,dict) and money_reward["type"]=="money":
                value=money_reward["value"]
                if isinstance(value,str):

## 0.12.n add reputation to cap price value for bot mods only
                  if option[0]=="bot":
                      
##                    print "BOT OFFER START: offer_id: ",offer.id," value: ",value

                    split_values = re.split(r'[(,]',value)

##                    print "split_values[0]: ",split_values[0]
##                    print "split_values[1]: ",split_values[1]," this is the original cap"
##                    print "split_values[2]: ",split_values[2]

                    if split_values[0]=="min":
                      global price_rep_bbs_offer
                      value_increase=price_rep_bbs_offer(offer.id)

##                      print "value increase: ",value_increase

                      revised_price_cap=value_increase+int(split_values[1])

##                      print "revised_price_cap: ",revised_price_cap                        
                        
                      value=split_values[0]+"("+str(revised_price_cap)+","+split_values[2]

##                      print "BOT OFFER END: value: ",value

                  value=eval(value,{"request_price":request_price})
                store.money_reward+=int(value)
          if money_reward:
            choice("netconsole_grey_market_accept_offer:"+offer_n+","+option[0]+","+str(option[1]),cost=[("money",-money_reward)]) "#[option_n] [option[2]]"
          else:
            choice("netconsole_grey_market_accept_offer:"+offer_n+","+option[0]+","+str(option[1])) "#[option_n] [option[2]]"
      $option=None
    elif isinstance(request_options,dict):
      if "money" in request_options:
        choice("netconsole_grey_market_accept_offer:"+offer_n+",money",cost=[("money",request_options["money"])]) "Accept"
  choice("netconsole_grey_market_ignore_offer:"+offer_n,pos=12) "Ignore post"
  $request_options=None
  $request_description=None
  $reward_description=None
  $request=None
  $reward=None
  $offer=None
  choice("goto_home",pos=16,key="home") "Log out"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label netconsole_grey_market_ignore_offer(offer_n):
  header "[netconsole] - [grey_market]"
  "You mark post as {mark}ignore-post{/} and go back to offers list."
  $grey_market.remove_offer(int(offer_n))
  choice("<<<") "Continue"
  return

label netconsole_grey_market_accept_offer(offer_n_request_details):

## 0.12.n added a global variable to know which type of bot was sold for reputation gain
  $global bbs_bot_offer_type

  $offer_n,sep,request_details=offer_n_request_details.partition(",")
  
##  $print "offer_n.id: ",offer_n.id
  
  if request_details.startswith(("bot","part")):
    $request_details,sep,request_id=request_details.partition(",")

  $offer=grey_market.offers[int(offer_n)]
  $request=offer.request
  $reward=offer.reward
  $request_options=offer.list_request_options(12)
  header "[netconsole] - [grey_market]"
  if request_details=="money":
    "You send money to middleman account with link to post, accepting offer."
    ""                                ## moved up so the space isn't placed where it's not needed
  elif request_details=="part":
    $part=workshop.inventory[int(request_id)]
    "You contact middleman delivery service with a from/to address hashes."
    ""
    "Soon afterwards a delivery bot picks your {mark}[part]{/}."
    ""                                ## moved up so the space isn't placed where it's not needed
    $workshop.remove_item(part)
  elif request_details=="bot":
    $bot=find_character(request_id)
    "You contace middleman delivery service with a from/to address and just as you finish packaging {mark}[bot]{/} they arrive to pick [bot.himher] up."

##    $print "bot rate: ",bot.rate,"  bbs_bot_offer_type: ",bbs_bot_offer_type

## 0.12.n add reputations
    if bot.rate=="D":                                            ## all offers: dealer rep gain based upon bot's rate                          
      $temp=calc_pr_rep_gain("rep_mc_dealer","xs_g")             ## extra small gain
      $mc.give_xp("rep_mc_dealer",temp)
    elif bot.rate=="C":
      $temp=calc_pr_rep_gain("rep_mc_dealer","s_g")              ## small gain
      $mc.give_xp("rep_mc_dealer",temp)
    elif bot.rate=="B":
      $temp=calc_pr_rep_gain("rep_mc_dealer","m_g")              ## medium gain
      $mc.give_xp("rep_mc_dealer",temp)
    elif bot.rate=="A":
      $temp=calc_pr_rep_gain("rep_mc_dealer","l_g")              ## large gain
      $mc.give_xp("rep_mc_dealer",randint(75,300))
    elif bot.rate=="S":
      $temp=calc_pr_rep_gain("rep_mc_dealer","xl_g")             ## extra large gain
      $mc.give_xp("rep_mc_dealer",randint(100,400))
    if bbs_bot_offer_type=="combat":                             ## combat bot offers: combat bot trainer rep gain based upon bot's combat skill
      if bot.bot_combat=="D":
        $temp=calc_pr_rep_gain("rep_mc_fighter","xs_g")          ## extra small gain
        $mc.give_xp("rep_mc_fighter",randint(5,45))
      elif bot.bot_combat=="C":
        $temp=calc_pr_rep_gain("rep_mc_fighter","s_g")           ## small gain
        $mc.give_xp("rep_mc_fighter",temp)
      elif bot.bot_combat=="B":
        $temp=calc_pr_rep_gain("rep_mc_fighter","m_g")           ## medium gain
        $mc.give_xp("rep_mc_fighter",temp)
      elif bot.bot_combat=="A":
        $temp=calc_pr_rep_gain("rep_mc_fighter","l_g")           ## large gain
        $mc.give_xp("rep_mc_fighter",temp)
      elif bot.bot_combat=="S":
        $temp=calc_pr_rep_gain("rep_mc_fighter","xl_g")          ## extra large gain
        $mc.give_xp("rep_mc_fighter",temp)
    elif bbs_bot_offer_type=="sextoy":                           ## sex bot offers: sex bot trainer rep gain based upon bot's sex skill
      if bot.bot_sex=="D":
        $temp=calc_pr_rep_gain("rep_mc_sexmachine","xs_g")       ## extra small gain
        $mc.give_xp("rep_mc_sexmachine",temp)
      elif bot.bot_sex=="C":
        $temp=calc_pr_rep_gain("rep_mc_sexmachine","s_g")        ## small gain
        $mc.give_xp("rep_mc_sexmachine",temp)
      elif bot.bot_sex=="B":
        $temp=calc_pr_rep_gain("rep_mc_sexmachine","m_g")        ## medium gain
        $mc.give_xp("rep_mc_sexmachine",temp)
      elif bot.bot_sex=="A":
        $temp=calc_pr_rep_gain("rep_mc_sexmachine","l_g")        ## large gain
        $mc.give_xp("rep_mc_sexmachine",temp)
      elif bot.bot_sex=="S":
        $temp=calc_pr_rep_gain("rep_mc_sexmachine","xl_g")       ## extra large gain
        $mc.give_xp("rep_mc_sexmachine",temp)
    elif bbs_bot_offer_type=="repairbot":                        ## tech bot offers: tech trainer rep gain based upon minimum of elec and mech skills
      if bot.bot_electronics=="D" or bot.bot_mechanics=="D":
        $temp=calc_pr_rep_gain("rep_mc_tech_trainer","xs_g")     ## extra small gain
        $mc.give_xp("rep_mc_tech_trainer",temp)
      elif bot.bot_electronics=="C" or bot.bot_mechanics=="C":
        $temp=calc_pr_rep_gain("rep_mc_tech_trainer","s_g")      ## small gain
        $mc.give_xp("rep_mc_tech_trainer",temp)
      elif bot.bot_electronics=="B" or bot.bot_mechanics=="B":
        $temp=calc_pr_rep_gain("rep_mc_tech_trainer","m_g")      ## medium gain
        $mc.give_xp("rep_mc_tech_trainer",temp)
      elif bot.bot_electronics=="A" or bot.bot_mechanics=="A":
        $temp=calc_pr_rep_gain("rep_mc_tech_trainer","l_g")      ## large gain
        $mc.give_xp("rep_mc_tech_trainer",temp)
      elif bot.bot_electronics=="S" and bot.bot_mechanics=="S":
        $temp=calc_pr_rep_gain("rep_mc_tech_trainer","xl_g")     ## extra large gain
        $mc.give_xp("rep_mc_tech_trainer",temp)        
    elif bbs_bot_offer_type=="assistant":                        ## pers. asst. bot offers: trainer bot rep gain based upon bot's social skill
      if bot.bot_social=="D":                                    
        $temp=calc_pr_rep_gain("rep_mc_trainer","xs_g")          ## extra small gain
        $mc.give_xp("rep_mc_trainer",temp)
      elif bot.bot_social=="C":
        $temp=calc_pr_rep_gain("rep_mc_trainer","s_g")           ## small gain
        $mc.give_xp("rep_mc_trainer",temp)
      elif bot.bot_social=="B":
        $temp=calc_pr_rep_gain("rep_mc_trainer","m_g")           ## medium gain
        $mc.give_xp("rep_mc_trainer",temp)
      elif bot.bot_social=="A":
        $temp=calc_pr_rep_gain("rep_mc_trainer","l_g")           ## large gain
        $mc.give_xp("rep_mc_trainer",temp)
      elif bot.bot_social=="S":
        $temp=calc_pr_rep_gain("rep_mc_trainer","xl_g")          ## extra large gain
        $mc.give_xp("rep_mc_trainer",temp)
## 0.11.n added images of packaging bots
    if bot.gender=="female":
      $temp_int=random.randint(1,3)
    else:
      $temp_int=random.randint(4,6)
    "{size=-24} {/}"
    $action_image= "bbs_offers sell_bot bbs_"+str(temp_int)
    center "{image=[action_image]@760x600}"
## end of insert

    $move_sexbot(bot,None)
  else:                                ## not sure what this is for, previously - if was "money", elif was "part", and elif was "bot"
    "You accept offer."

    "THE CODE I THOUGHT WAS DEAD IN GREY NET OFFERS SAYING 'You accept offer' LIVES!"
    
##  ""                                   ## moved up to money and part offers, it's not needed for a bot offer
  $rewards=offer.reward[:]
  while rewards:
    $reward=rewards.pop(0)
    if isinstance(reward,BotPart):
      $workshop.add_item(reward)
      "{mark}[reward]{/} was delivered to your workshop."
    elif isinstance(reward,dict):
      if reward["type"]=="money":
        ## done on previous screen
        pass
  $grey_market.remove_offer(int(offer_n))
  choice("<<<") "Continue"
  $request_options=None
  $request=None
  $reward=None
  $offer=None
  return
  