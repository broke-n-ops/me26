##  Initialize new variables
init python:
  rays_activated=0               ## USED IN 'street.rpy': set to 1 to activate 'Raymond's' location
##  try again: NEXT FLAG DIDN'T WORK IN 'street.rpy' SO MOVED TO 'squirrelhome_workout_man variables
  rays_already_visited=0         ## flag set to 1 when you begin show and used to avoid repeat visits same evening
  rays_online_bot_list=0       ## flag set to 1 when online bot list is generated, will be cleared each morning
  rays_first_boutique_visit=1    ## first visit is free, afterwards it costs to view the bots
  rays_boutique_money_cost=1200  ## ADJUST LATER price to visit boutique
  rays_boutique_energy_cost=2    ## ADJUST LATER energy used to visit boutique (time spent)
  rays_bought_bot=0              ## set to 1 if you buy a bot this visit, if not activate store (one time only!)
  rays_online_activated=0        ## set to 1 when the online store is activated, set to 2 after leaving text displayed
  rays_bot_count=0               ## which bot from original list of 6 is being viewed currently
  rays_available_capsule=0       ## will be > 0 when you have at least one capsule available
  rays_available_space=0         ## will be > 0 when you have at least one space available (storage)
  rays_which_bot=""              ## holder for bot ID needed for diaplaying avatar
  rays_bot_index=0               ## which bot in the array of 6 is being viewed
  rays_trait_price=5000          ## premium price addition per trait (F,E,D,C bots) (no E or F bots!)
  rays_trait_price_luxury=10000  ## premium price addition per trait (B,A,S bots)
  rays_bot_markup_dict={         ## dict with markup on bots by rating
    u'S':1.6,
    u'A':2.0,
    u'B':2.1,
    u'C':2.8,
    u'D':2.1,
    u'E':2.3,
    u'F':2.5,
    }
  rays_all_slots_list=[]         ## holds slots 'list of lists'
  rays_all_parts_list=[]         ## holds parts 'list of lists'
  rays_part_slot=""              ## user selected slot when buying parts
  rays_part_slot_name=""         ## name of user selected slot when buying parts
##  rays_current_row=1           ## DECLARED AND USED IN 'netconsole_net_site.rpy'
  rays_last_row=0                ## holds number of rows required to display slot buttons
  rays_part_top_row=0            ## index of parts on top row in part's page
  rays_part_type_total=0         ## number of parts of a specific type being viewed in online store

  rays_markup_slope=0.185        ## slope for empiracle calculation of markup for mod slots
  rays_markup_intercept=1.215    ## intercept for above: markup=slope*category_price_mult+intercept
  rays_part_rate_mult=0          ## part price multiplier based upon the part's rating (ups the price of low rated parts)
  rays_part_rate_markup_dict={   ## dict with markup multiplier for parts by rating
    u'S':2.1,
    u'A':2.3,
    u'B':2.5,
    u'C':2.7,
    u'D':2.9,
    u'E':3.1,
    u'F':3.3,
    }

  rays_part_markup={}            ## initialize an empty dict to hold the final part markup values

## ORIGINAL VALUES IN 'rays_markup"list' dict:
  # # rays_part_markup={             ## dict to lookup markup per slot (part type) - about 2.2x over BBS offer prices
    # # u'bot_cpu':7.3,              ## DEF 3.4  BC 3.2  SA 3.3
    # # u'bot_eyes':4.2,             ## DEF 2.0  BC 1.8  SA 1.9
    # # u'bot_ears':3.3,             ## DEF 1.6  BC 1.4  SA 1.5
    # # u'bot_vocoder':3.1,          ## DEF 1.5  BC 1.3  SA 1.4
    # # u'bot_powercore':5.7,        ## DEF 2.7  BC 2.5  SA 2.6
    # # u'bot_arms':4.8,             ## DEF 2.3  BC 2.1  SA 2.2
    # # u'bot_legs':3.7,             ## DEF 1.9  BC 1.7  SA 1.8
    # # u'bot_skin':4.6,             ## DEF 2.2  BC 2.0  SA 2.1
    # # u'bot_implants':4.0,         ## DEF 1.9  BC 1.7  SA 1.8
    # # u'bot_vagina':4.7,           ## DEF 2.2  BC 2.0  SA 2.1
    # # u'bot_penis':4.5,            ## DEF 2.1  BC 1.9  SA 2.0
    # # }

## Part base prices are set in 'part.rpy' (in 0010 modules folder), copied here as comments for reference
##  base_bot_part_prices={
##    "F": 25,
##    "E": 100,
##    "D": 250,
##    "C": 500,
##    "B": 1000,
##    "A": 2500,
##    "S": 5000,
##    }

## Bot base prices are set in 'bot.rpy' (in 11010 modules folder), copied here as comments for reference
##  base_bot_model_prices={
##    "F": 1000,
##    "E": 2500,
##    "D": 5000,
##    "C": 10000,
#3    "B": 25000,
##    "A": 50000,
##    "S": 180000,  - this was 250000 in DSCS which I believe was too high
##    }

##  variables for bot salesman from mob quest
  rays_salesman_b_price=167600   ## 'B' bot, 1 trait (sex) - 15% off - actual=197200
  rays_salesman_a_price=395100   ## 'A' bot, 2traits (sex,social) - 15% off - actual =464800
  rays_salesman_s_price=671900   ## 'S' bot, 2 traits (sex,social) - 15% off - actual=790500
  rays_salesman_bot_price=0      ## price of bot sold in current visit

## REAL LINE
  rays_salesman_day=50           ## TENTATIVE VALUE - fallback if home gym not purchased
## SUBSTITUTE LINE FOR TESTING PURPOSES
##  rays_salesman_day=1            ## FOR TESTING - START VISITS QUICKLY

  rays_salesman_visit_count=0    ## increment after each visit, if >=3 no more visits
  rays_salesman_bought_bot=0     ## set to 1 if you buy a bot, influences reveal text
  rays_salesman_bought_sigrid=0  ## set to 1 if you buy Sigrid, influences reveal images and text

## ADDED IN V0.6.0beta BUG FIX
  rays_boutique_bots_for_sale=[]  ## holds array of luxury bots for the boutique
  rays_online_bots_for_sale=[]    ## holds array of non-luxury bots for the online store

##======EVENT HANDLER FOR BOT SALESMAN=======

init python hide:
  @event_handler("time_advanced")
  def rays_event():

## REAL LINE
    if now("tuesday","afternoon"):                             ## visits are on tuesdays afternoons
## SUBSTITUTE LINE FOR TEST PURPOSES
##    if now("afternoon"):                                       ## FOR TESTING VISITS EVERY AFTERNOON
      if now.day>=rays_salesman_day or hw_equipment_level>=4:  ## passed fallback day OR gym paid for
        if rays_salesman_visit_count<3:                        ## salesman visits stop after 3
          ##rays_salesman_visits_shop()
          queue_event("rays_salesman_visits_shop")

##======BOT SALESMAN MOVED FROM MOB QUEST=======

label rays_salesman_visits_shop:                     ##  Dealer offers luxury bots at high prices
  $game_bg="home workspace"
  header "Raymond's Dealer Visits Shop"
  if rays_salesman_visit_count==0:                   ## 1st visit, 'B' level bot
    $rays_salesman_visit_count+=1                    ## increase to 1
    $rays_salesman_bot_price=rays_salesman_b_price   ## set price to 85% of Mylou's price
    ## GRAPHICS on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_170"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_171"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_172"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_173"
    center "{image=[action_image]@400x600}"
    ## TEXT on right
    $act.set_block("c")
    ""
    "A slick looking character comes into the shop along with a nice looking luxury bot. He gestures to the bot who strikes a nice pose. He turns to me and says:"
    ""
    ""
    ""
    "{say}We're representing{/} {mark}Raymond's Bot Boutique{/} {say}and I'd like to sell you this amazing{/} {mark}B-rated luxury bot{/} {say}for only{/} {mark}$[rays_salesman_bot_price]{/}{say}. That's a 15%% discount, why don't you take a look?{/}"
    ""
    ""
    ""
    "You are a little annoyed at the interruption but it's a nice looking bot! You examine her pretty closely and you're impressed."
    ""
    ""
    ""
  elif rays_salesman_visit_count==1:                 ## 2nd visit, 'A' level bot
    $rays_salesman_visit_count+=1                    ## increase to 2
    $rays_salesman_bot_price=rays_salesman_a_price   ## set price to 85% of Natalie's price
    ## GRAPHICS on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_179"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_180"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_181"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_182"
    center "{image=[action_image]@400x600}"
    ## TEXT on right
    $act.set_block("c")
    ""
    "The same slick looking character from {mark}Raymond's Bot Boutique{/} comes into the shop again. This time an even nicer bot struts around the shop like she's flirting with me. The guy says:"
    ""
    ""
    "{say}Hey kid, I've got a fantastic{/} {mark}A-rated luxury bot{/} {say}with me this time. She's an amazing luxury bot for only{/} {mark}$[rays_salesman_bot_price]{/}{say}. That's a 15%% discount. Go ahead, take a look!{/}"
    ""
    ""
    ""
    ""
    "You are a little annoyed at the interruption but it's a great looking bot! You examine her closely, she's really something."
    ""
    ""
    ""
    ""
  else:                                              ## 3rd visit, 'S' level bot
    $rays_salesman_visit_count+=1                    ## increase to 3rd (no more visits)
    $rays_salesman_bot_price=rays_salesman_s_price   ## set price to 85% of Sigrid's price
    ## GRAPHICS on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_188"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_189"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_190"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_191"
    center "{image=[action_image]@400x600}"
    ## TEXT on right
    $act.set_block("c")
    ""
    "The slick looking character from {mark}Raymond's Bot Boutique{/} is back again. The best bot I've ever seen is with him, I think she's S rated! While I'm staring at her the guy says:"
    ""
    ""
    "{say}I see you've noticed our top of the line{/} {mark}S-rated luxury bot{/} {say}. Everything about her is high end, you won't find a better bot anywhere.  You can have this top of the line luxury bot for{/} {mark}$[rays_salesman_bot_price]{/}{say}. That's a 15%% discount. Fantastic, isn't she?{/}"
    ""
    ""
    ""
    "You completely forget what you were doing and enjoy checking out this bot. Everything about her is top of the line and she looks great too!"
    ""
    ""
    ""
  call sr24_add_bot_ok                               ## sets 'sr24_rooom_for_bot=1 if there is room
  if mc.money<rays_salesman_bot_price:               ## not enough money to buy bot
    "{mark}I need to stop dreaming because I don't have $[rays_salesman_bot_price].{/}"
    ""
    choice("rays_refuse__bot") "Can't Afford Bot"
  elif sr24_room_for_bot!=1:                         ## no space available, button active
    "{mark}Unfortunately the shop is full and I have no where to put another bot.{/}"
    ""
    choice("rays_refuse__bot") "Shop Full"
  else:                                              ## enough money and space available
    "That's a lot of money but I can see this luxury bot is well made with the all appropriately rated parts. Should I buy this bot?"
    ""
    choice("rays_salesman_buy_bot_do") "Buy the Bot"
    choice("rays_refuse__bot") "Refuse"
  return

label rays_salesman_buy_bot_do:
  header "Raymond's Dealer Visits Shop"
  call sr24_add_bot_ok                               ## sets 'sr24_rooom_for_bot=1 if there is room
  if sr24_room_for_bot==1:                           ## space check successful, add bot - if unsuccessful don't add bot
    if rays_salesman_visit_count==1:                 ## 1st visit; Mylou (B)
      ## GRAPHICS on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_174"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_175"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_176"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right
      $act.set_block("c")
      "You tell the dealer you'll buy the bot and say you'll be right back with the money.  The dealer smiles and says:"
      ""
      "{say}Great decision! I'll load the sex skill trait included with this model while you're gone."
      ""
      "You come back and see that the bot made herself comfortable! You hand the dealer the money and he says:"
      ""
      "{say}Congratulations kid, I'm sure you'll love this bot. See you next time.{/}"
      ""
      "You take the bot to the back of the shop to put her in a capsule. I'm going to love working on this one!"
      ""
      $mc.money=mc.money-rays_salesman_bot_price     ## subtract current bot price to pay for the bot
      $bot_cls=store.SexBot_squirrel_mylou           ##  Add Mylou bot in perfect condition
      $rays_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))
      $store.global_bots_counter+=1
      $generate_bot_warranty_seals(rays_bot,default_generate_bot_warranty_seals_table)
## CHANGE IN SR24 v0.4.n
##      $home.add_sexbot(bot)
      call sr24_add_bot_do(rays_bot)
      $rays_bot=None
      $rays_salesman_bought_bot=1                    ##  set flag to bot purchased from salesman
      choice("<<<") "Continue"                       ##  1st visit; continue
    elif rays_salesman_visit_count==2:               ##  2nd visit; Natalie (A)
      ## GRAPHICS on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_183"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_184"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_185"
      center "{image=[action_image]@400x600}"
      ## TEXT on right
      $act.set_block("c")
      "You tell the dealer you'll buy the bot and say you'll be right back with the money.  The dealer smiles and says:"
      ""
      "{say}Fantastic! I'll load the sex and social skill traits included with this model while you're gone."
      ""
      "You come back and see that the bot made herself comfortable! You hand the dealer the money and he says:"
      ""
      "{say}Congratulations kid, I'm sure you'll love this bot. See you next time.{/}"
      ""
      "You take the bot to the back of the shop to put her in a capsule. I'm going to love working on this one!"
      ""
      $mc.money=mc.money-rays_salesman_bot_price     ## subtract current bot price to pay for the bot
      $bot_cls=store.SexBot_squirrel_natalie         ##  Add Natalie in perfect condition
      $rays_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))
      $store.global_bots_counter+=1
      $generate_bot_warranty_seals(rays_bot,default_generate_bot_warranty_seals_table)
## CHANGE IN SR24 v0.4.n
##      $home.add_sexbot(bot)
      call sr24_add_bot_do(rays_bot)
      $rays_bot=None
      $rays_salesman_bought_bot=1                    ##  set flag to bot purchased from salesman
      choice("<<<") "Continue"                       ## 2nd visit; continue
    else:                                            ## 3rd visit; Sigrid (S)
      ## GRAPHICS on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_192"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_193"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "squirrel rays ray_1"           ## TEST Excel line 22 - salesman in background shouldn't be leaving
      center "{image=[action_image]@400x600}"
      ## TEXT on right
      $act.set_block("c")
      "You tell the dealer you'll buy the bot and say you'll be right back with the money.  The dealer smiles and says:"
      ""
      "{say}Great! I'll load the sex and social skill traits included with this model while you're gone."
      ""
      "You come back and see that the bot made herself comfortable! You hand the dealer the money and he says:"
      ""
      "{say}Congratulations kid, I'm sure you'll love this bot.{/}"
      ""
      "The dealer hangs around while you take the bot to the back of the shop to put her in a capsule."
      ""
      $mc.money=mc.money-rays_salesman_bot_price     ## subtract current bot price to pay for the bot
      $bot_cls=store.SexBot_squirrel_sigrid          ##  Add Sigrid bot in perfect condition
      $rays_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))
      $store.global_bots_counter+=1
      $generate_bot_warranty_seals(rays_bot,default_generate_bot_warranty_seals_table)
## CHANGE IN SR24 v0.4.n
##      $home.add_sexbot(bot)
      call sr24_add_bot_do(rays_bot)
      $rays_bot=None
      $rays_salesman_bought_bot=1                    ## set flag to bot purchased from salesman
      $rays_salesman_bought_sigrid=1                 ## set flag to Sigrid purchased
      choice("rays_salesman_reveal") "Continue"      ## 3rd visit; reveal Raymond's Bot Boutique
  return

label rays_refuse__bot:                              ## Used when can't afford, no space, and player choice
  header "Raymond's Dealer Visits Shop"
  if rays_salesman_visit_count==1:                   ## 1st visit; refuse or can't afford Mylou (B)
    ## GRAPHICS on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_177"    ##  Mylou pictures
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_178"
    center "{image=[action_image]@400x600}"
    choice("<<<") "Continue"                         ## 1st visit; continue
  elif rays_salesman_visit_count==2:                 ## 2nd visit; refuse or can't afford Natalie (A)
    ## GRAPHICS on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_186"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_187"
    center "{image=[action_image]@400x600}"
    choice("<<<") "Continue"                         ## 2nd visit; continue
  else:                                              ## 3rd visit; refuse or can't afford Sigrid (S)
    ## GRAPHICS on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_195"    ## this one is OK
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "squirrel rays ray_2"             ## TEST Excel line 23 - salesman looking at MC with Sigrid disappointed
    center "{image=[action_image]@400x600}"
    choice("rays_salesman_reveal") "Continue"        ## 3rd visit; reveal Raymond's Bot Boutique
  ## TEXT on right
  $act.set_block("c")
  call sr24_add_bot_ok                               ## sets 'sr24_rooom_for_bot=1 if there is room
  if mc.money<rays_salesman_bot_price:               ## can't afford
    ""
    "Instead of admitting that you can't afford the bot you decide to tell the dealer that the bot looks great but you're not interested."
    ""
    ""
    ""
    if rays_salesman_visit_count<3:
      "The dealer tries to change your mind but you hold firm and eventually he leaves the shop with the luxury bot. She looks back at you as she leaves, she's well trained!"
    else:  ## 3rd visit
      "The dealer tries to change your mind but you hold firm. You wish he would just give up and leave."
    ""
  elif sr24_room_for_bot!=1:                         ## no space
    ""
    "You don't want to admit that your shop has no room for another bot so you decide to tell the dealer you're not interested this time."
    ""
    ""
    ""
    if rays_salesman_visit_count<3:
      "The dealer tries to change your mind but you hold firm and eventually he leaves the shop with the luxury bot. She looks back at you as she leaves, she's well trained!"
    else:  ## 3rd visit
      "The dealer tries to change your mind but you hold firm. You wish he would just give up and leave."
    ""
  else:                                              ## player choice
    ""
    "You decide that you can't justify spending that kind of money right now and decide to tell the dealer you're not interested this time."
    ""
    ""
    ""
    if rays_salesman_visit_count<3:
      "The dealer tries to change your mind but you hold firm and eventually he leaves the shop with the luxury bot. She looks back at you as she leaves, she's well trained!"
    else:  ## 3rd visit
      "The dealer tries to change your mind but you hold firm. You wish he would just give up and leave."
    ""
  return

label rays_salesman_reveal:
  header "Raymond's Dealer Visits Shop"
  ## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if rays_salesman_bought_sigrid==1:
    $action_image= "squirrel rays ray_6"   ## TEST Excel line 24 - salesman talking to MC without Sigrid version 1
  else:
    $action_image= "squirrel rays ray_3"   ## TEST Excel line 25 - salesman talking to MC with Sigrid version 1
  center "{image=[action_image]@400x600}"
  ""
  if rays_salesman_bought_sigrid==1:
    $action_image= "squirrel rays ray_7"   ## TEST Excel line 24 - salesman talking to MC without Sigrid version 2
  else:
    $action_image= "squirrel rays ray_4"   ## TEST Excel line 25 - salesman talking to MC with Sigrid version 1
  center "{image=[action_image]@400x600}"
  ""
  if rays_salesman_bought_sigrid==1:
    $action_image= "squirrel rays ray_8"   ## TEST salesman leaving without Sigrid
  else:
    $action_image= "squirrel rays ray_5"   ## TEST salesman leaving with Sigrid
  center "{image=[action_image]@400x600}"
  ## TEXT on right
  $act.set_block("c")
  if rays_salesman_bought_bot==0:          ## did NOT buy bot from salesman
    ""
    "Before leaving the salesman says:"
    ""
    "{say}Hey kid, since you never buy anything I have to stop wasting my time coming here. Let me leave you with this free pass to our boutique in the city. It's a high class place, the pass is worth{/} {mark}$1,200.{/} {say}Your first visit will be free and I'm sure you'll have a good time. Check it out!{/}"
    ""
    "You look at the card he gave you. It says {mark}Raymond's Bot Boutique{/} and it's open {mark}every evening{/}. Since it's free I'll give it a try."
    ""
    ""
    "The salesman and his bot leave the shop. Probably a good thing he won't come in and distract me any more."
  else:                                    ## bought at least one bot from salesman
    if rays_salesman_bought_sigrid==1:
      "When you return the salesman says:"
    else:
      "Before leaving the salesman says:"
    ""
    "{say}Hey kid, I know you're busy so I'll stop coming by your shop and wasting your time. Let me give you this free pass to get you into our boutique in the city. It's a high class place, the pass is worth{/} {mark}$1,200.{/} {say}First time will be free and I'm sure you'll have a good time. Check it out!{/}"
    ""
    "You look at the card he gave you. It says {mark}Raymond's Bot Boutique{/} and it's open {mark}every evening{/}. Great, I'll have to check this place out!"
    ""
    ""
    "The salesman and his bot leave the shop. Probably a good thing he won't come in and distract me any more."
  $rays_activated=1                        ## USED IN 'street.rpy': activate 'Raymond's' location
  ""
  $quests.where_to_get_bots.add_method("sr24_raymonds","you can find luxury bots for sale at {mark}Raymond's Bot Boutique{/}")
  choice("<<<") "Continue"
  return

##====== END OF SALESMAN VISIT FUNCTIONS ======
##====== START OF RAYMOND'S BOT BOUTIQUE FUNCTIONS ======

## initializing variables

## 0.11.n moved location code including 'roaming' function to 0020 locations, calls initialize function here

label rays_initialize_visit:
  call rays_create_slots_list                          ## create slots list and part markup list each time you enter the boutique
  call rays_create_parts_list                          ## create parts list each time you enter the boutique
  $rays_bought_bot=0                                   ## reset flag for this visit
  $rays_boutique_bots_for_sale=rays_generate_bots()    ## generate array containing 6 luxury bots
  $rays_bot_count=0                                    ## reset bot count for this visit
  $rays_bot_index=0                                    ## reset bot index for this visit
  return

##============DISPLAY BOT FUNCTIONS==========

## 0.15.n created new roaming function in 'rays_bot_boutique.rpy' and moved previous roaming function here with a new name and some editing
label rays_enter_club:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)          ## random between 2 backgrounds
  header "[rays_boutique]"
  $rays_already_visited=1                               ## set flag to 1 so you cannot come back the same evening
  if rays_first_boutique_visit==1:                      ## first visit different text - MC in original clothing unless player refused to go!!!!
    "You enter the bot boutique and take a look around. This is a nice place and everyone is well dressed!"
    "{size=-22} "
    $temp_image=random.randint(9,10)
    $action_image="squirrel rays ray_"+str(temp_image)
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    "Considering the place and clientele you're out of your league here! A guy in tie and tails with a microphone is introducing tonight's program."
  elif bp_suit_for_rays==0:                           ## MC in original clothing (not given suit by Simone)
    "As usual the clientele all stare at you making you feel out of place."
    "{size=-22} "
    $temp_image=random.randint(9,10)
    $action_image="squirrel rays ray_"+str(temp_image)
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    "You're right on time and the host is introducing tonight's program."
  elif now("sunday") and bp_first_sex_teacher==1:       ## MC Simone is there on Sunday after clothing change
    "{mark}[ns_teacher_name]{/} is sitting at her usual table. As always she looks great!"
    "{size=-22} "
    $temp_image=random.randint(9,10)
    $action_image="squirrel rays ray_"+str(temp_image)+"b"
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    "You sit down next to her and greet her quietly because the host is introducing tonight's program that's about to start."
  else:                                                 ## MC in suit from Simone any day except Sunday
    "You feel comfortable here wearing the suit that {mark}[ns_teacher_name]{/} gave you."
    "{size=-22} "
    $temp_image=random.randint(9,10)
    $action_image="squirrel rays ray_"+str(temp_image)+"a"
    center "{image=[action_image]@800x600}"
    "{size=-22} "
    "The host is introducing tonight's program which is about to start. You hope they show the kind of bots you are interested in."
  call rays_initialize_visit  ## this line moved here from roaming function in 'rays_bot_boutique.rpy'
  choice ("rays_display_bot_1") "Begin Show"
  if now("sunday") and bp_first_sex_teacher==1:       ## add skip show button if you only want to date Simone
    choice("rays_date_decision") "Skip Show"    
      
##  choice("rays_leave",pos=17) "Leave"         ## COMMENT OUT, DELETE LATER...  why leave before seeing anything? you've already paid

  return

label rays_display_bot_1:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)               ## random between 2 backgrounds
  header "Raymond's Bot Boutique - 1st Model"
## 0.15.n moved flag setting earlier
##  $print "display bot 1:set rays flag to 1"
##  $rays_already_visited=1                                    ## set flag to 1 so you cannot come back the same evening
  $rays_bot=rays_boutique_bots_for_sale[rays_bot_index]      ## load current bot
  $rays_bot_index+=1                                         ## increment for next bot
  $rays_which_bot=rays_bot.model_id
  $rays_bot_count=1                                          ## viewing bot 1
  $bot_price=rays_calc_bot_price(rays_bot)
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_bot.model_id] avatar@400x600}"   ## avatar on left
  $act.set_block("c")                                        ## description and picture on right
  "Model: {mark}[rays_bot.model_name]{/}"
##  "Price: {mark}$[bot_price]{/}"
  "Price: {mark}[money_str[bot_price]]{/}"                   ## 0.11.3 use MoneyStr()
  ""
  if rays_bot.gender=="female":                              ## most likely female bot, use bot 1
    $temp_image=random.randint(11,12)
  else:
    $temp_image=random.randint(23,24)                        ## rarely male bot

## 0.15.n support clothing change
  if bp_suit_for_rays==0:                                    ## MC in original clothing (not given suit by Simone)
    $action_image= "squirrel rays ray_"+str(temp_image)
  elif now("sunday") and bp_first_sex_teacher==1:            ## MC Simone is there on Sunday after clothing change
    $action_image= "squirrel rays ray_"+str(temp_image)+"b"
  else:                                                      ## MC in suit from Simone
    $action_image= "squirrel rays ray_"+str(temp_image)+"a"

  center "{image=[action_image]@400x600}"                    ## CONSIDER REDUCING SIZE OF IMAGE!
  ""
  "[rays_bot.model_description]"
  ""
  choice(">>>rays_buy_bot_preview:{},{}".format(rays_bot_index-1,bot_price)) "Bot Info"
  choice("rays_display_bot_2") "Next Bot"
  if rays_first_boutique_visit==1:                           ## activate online on first visit only!!
    choice("rays_activate_online",pos=17) "Stop Watching"

## 0.15.n cannot leave early on Sundays with Simone
  elif bp_first_sex_teacher==0 or not now("sunday"):         ## cannot be Sunday with Simone
    choice("rays_leaving_early",pos=17) "Stop Watching"      ## function after viewing part of show
  return

label rays_display_bot_2:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)               ## random between 2 backgrounds
  header "Raymond's Bot Boutique - 2nd Model"
  $rays_bot=rays_boutique_bots_for_sale[rays_bot_index]      ## load current bot
  $rays_bot_index+=1                                         ## increment for next bot
  $rays_which_bot=rays_bot.model_id
  $rays_bot_count=2                                          ## viewing bot 2
  $bot_price=rays_calc_bot_price(rays_bot)
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_bot.model_id] avatar@400x600}"   ## avatar on left
  $act.set_block("c")                                        ##  description and picture on right
  "Model: {mark}[rays_bot.model_name]{/}"
##  "Price: {mark}$[bot_price]{/}"
  "Price: {mark}[money_str[bot_price]]{/}"                   ## 0.11.3 use MoneyStr()
  ""
  if rays_bot.gender=="female":                              ## most likely female bot, use bot 2
    $temp_image=random.randint(13,14)
  else:
    $temp_image=random.randint(23,24)                        ## rarely male bot

## 0.15.n support clothing change
  if bp_suit_for_rays==0:                                    ## MC in original clothing (not given suit by Simone)
    $action_image= "squirrel rays ray_"+str(temp_image)
  elif now("sunday") and bp_first_sex_teacher==1:            ## MC Simone is there on Sunday after clothing change
    $action_image= "squirrel rays ray_"+str(temp_image)+"b"
  else:                                                      ## MC in suit from Simone
    $action_image= "squirrel rays ray_"+str(temp_image)+"a"

  center "{image=[action_image]@400x600}"                    ## CONSIDER REDUCING SIZE OF IMAGE!
  ""
  "[rays_bot.model_description]"
  ""
  choice(">>>rays_buy_bot_preview:{},{}".format(rays_bot_index-1,bot_price)) "Bot Info"
  choice("rays_display_bot_3") "Next Bot"
  if rays_first_boutique_visit==1:                           ## activate online on first visit only!!
    choice("rays_activate_online",pos=17) "Stop Watching"

## 0.15.n cannot leave early on Sundays with Simone
  elif bp_first_sex_teacher==0 or not now("sunday"):         ## cannot be Sunday with Simone
    choice("rays_leaving_early",pos=17) "Stop Watching"      ## function after viewing part of show
  return

label rays_display_bot_3:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)               ## random between 2 backgrounds
  header "Raymond's Bot Boutique - 3rd Model"
  $rays_bot=rays_boutique_bots_for_sale[rays_bot_index]      ## load current bot
  $rays_bot_index+=1                                         ## increment for next bot
  $rays_which_bot=rays_bot.model_id
  $rays_bot_count=3                                          ## viewing bot 3
  $bot_price=rays_calc_bot_price(rays_bot)
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_bot.model_id] avatar@400x600}"   ## avatar on left
  $act.set_block("c")                                        ##  description and picture on right
  "Model: {mark}[rays_bot.model_name]{/}"
##  "Price: {mark}$[bot_price]{/}"
  "Price: {mark}[money_str[bot_price]]{/}"                   ## 0.11.3 use MoneyStr()
  ""
  if rays_bot.gender=="female":                              ## most likely female bot, use bot 3
    $temp_image=random.randint(15,16)
  else:
    $temp_image=random.randint(23,24)                        ## rarely male bot

## 0.15.n support clothing change
  if bp_suit_for_rays==0:                                    ## MC in original clothing (not given suit by Simone)
    $action_image= "squirrel rays ray_"+str(temp_image)
  elif now("sunday") and bp_first_sex_teacher==1:            ## MC Simone is there on Sunday after clothing change
    $action_image= "squirrel rays ray_"+str(temp_image)+"b"
  else:                                                      ## MC in suit from Simone
    $action_image= "squirrel rays ray_"+str(temp_image)+"a"

  center "{image=[action_image]@400x600}"                    ## CONSIDER REDUCING SIZE OF IMAGE!
  ""
  "[rays_bot.model_description]"
  ""
  choice(">>>rays_buy_bot_preview:{},{}".format(rays_bot_index-1,bot_price)) "Bot Info"
  choice("rays_display_bot_4") "Next Bot"
  if rays_first_boutique_visit==1:                           ## activate online on first visit only!!
    choice("rays_activate_online",pos=17) "Stop Watching"

## 0.15.n cannot leave early on Sundays with Simone
  elif bp_first_sex_teacher==0 or not now("sunday"):         ## cannot be Sunday with Simone
    choice("rays_leaving_early",pos=17) "Stop Watching"      ## function after viewing part of show
  return

label rays_display_bot_4:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)               ## random between 2 backgrounds
  header "Raymond's Bot Boutique - 4th Model"
  $rays_bot=rays_boutique_bots_for_sale[rays_bot_index]      ## load current bot
  $rays_bot_index+=1                                         ## increment for next bot
  $rays_which_bot=rays_bot.model_id
  $rays_bot_count=4                                          ## viewing bot 4
  $bot_price=rays_calc_bot_price(rays_bot)
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_bot.model_id] avatar@400x600}"   ## avatar on left
  $act.set_block("c")                                        ##  description and picture on right
  "Model: {mark}[rays_bot.model_name]{/}"
##  "Price: {mark}$[bot_price]{/}"
  "Price: {mark}[money_str[bot_price]]{/}"                   ## 0.11.3 use MoneyStr()
  ""
  if rays_bot.gender=="female":                              ## most likely female bot, use bot 1 again
    $temp_image=random.randint(17,18)
  else:
    $temp_image=random.randint(23,24)                        ## rarely male bot

# 0.15.n support clothing change
  if bp_suit_for_rays==0:                                    ## MC in original clothing (not given suit by Simone)
    $action_image= "squirrel rays ray_"+str(temp_image)
  elif now("sunday") and bp_first_sex_teacher==1:            ## MC Simone is there on Sunday after clothing change
    $action_image= "squirrel rays ray_"+str(temp_image)+"b"
  else:                                                      ## MC in suit from Simone
    $action_image= "squirrel rays ray_"+str(temp_image)+"a"

  center "{image=[action_image]@400x600}"                    ## CONSIDER REDUCING SIZE OF IMAGE!
  ""
  "[rays_bot.model_description]"
  ""
  choice(">>>rays_buy_bot_preview:{},{}".format(rays_bot_index-1,bot_price)) "Bot Info"
  choice("rays_display_bot_5") "Next Bot"
  if rays_first_boutique_visit==1:                           ## activate online on first visit only!!
    choice("rays_activate_online",pos=17) "Stop Watching"

## 0.15.n cannot leave early on Sundays with Simone
  elif bp_first_sex_teacher==0 or not now("sunday"):         ## cannot be Sunday with Simone
    choice("rays_leaving_early",pos=17) "Stop Watching"      ## function after viewing part of show
  return

label rays_display_bot_5:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)               ## random between 2 backgrounds
  header "Raymond's Bot Boutique - 5th Model"
  $rays_bot=rays_boutique_bots_for_sale[rays_bot_index]      ## load current bot
  $rays_bot_index+=1                                         ## increment for next bot
  $rays_which_bot=rays_bot.model_id
  $rays_bot_count=5                                          ## viewing bot 5
  $bot_price=rays_calc_bot_price(rays_bot)
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_bot.model_id] avatar@400x600}"   ## avatar on left
  $act.set_block("c")                                        ##  description and picture on right
  "Model: {mark}[rays_bot.model_name]{/}"
##  "Price: {mark}$[bot_price]{/}"
  "Price: {mark}[money_str[bot_price]]{/}"                   ## 0.11.3 use MoneyStr()
  ""
  if rays_bot.gender=="female":                              ## most likely female bot, use bot 2 again
    $temp_image=random.randint(19,20)
  else:
    $temp_image=random.randint(23,24)                        ## rarely male bot

# 0.15.n support clothing change
  if bp_suit_for_rays==0:                                    ## MC in original clothing (not given suit by Simone)
    $action_image= "squirrel rays ray_"+str(temp_image)
  elif now("sunday") and bp_first_sex_teacher==1:            ## MC Simone is there on Sunday after clothing change
    $action_image= "squirrel rays ray_"+str(temp_image)+"b"
  else:                                                      ## MC in suit from Simone
    $action_image= "squirrel rays ray_"+str(temp_image)+"a"

  center "{image=[action_image]@400x600}"                    ## CONSIDER REDUCING SIZE OF IMAGE!
  ""
  "[rays_bot.model_description]"
  ""
  choice(">>>rays_buy_bot_preview:{},{}".format(rays_bot_index-1,bot_price)) "Bot Info"
  choice("rays_display_bot_6") "Next Bot"
  if rays_first_boutique_visit==1:                           ## activate online on first visit only!!
    choice("rays_activate_online",pos=17) "Stop Watching"

## 0.15.n cannot leave early on Sundays with Simone
  elif bp_first_sex_teacher==0 or not now("sunday"):         ## cannot be Sunday with Simone
    choice("rays_leaving_early",pos=17) "Stop Watching"      ## function after viewing part of show
  return

label rays_display_bot_6:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)               ## random between 2 backgrounds
  header "Raymond's Bot Boutique - Final Model"
  $rays_bot=rays_boutique_bots_for_sale[rays_bot_index]      ## load current bot
  $rays_bot_index+=1                                         ## increment for next bot
  $rays_which_bot=rays_bot.model_id
  $rays_bot_count=6                                          ## viewing bot 6
  $bot_price=rays_calc_bot_price(rays_bot)
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_bot.model_id] avatar@400x600}"   ## avatar on left
  $act.set_block("c")                                        ##  description and picture on right
  "Model: {mark}[rays_bot.model_name]{/}"
##  "Price: {mark}$[bot_price]{/}"
  "Price: {mark}[money_str[bot_price]]{/}"                   ## 0.11.3 use MoneyStr()
  ""
  if rays_bot.gender=="female":                              ## most likely female bot, use bot 3 again
    $temp_image=random.randint(21,22)
  else:
    $temp_image=random.randint(23,24)                        ## rarely male bot

# 0.15.n support clothing change
  if bp_suit_for_rays==0:                                    ## MC in original clothing (not given suit by Simone)
    $action_image= "squirrel rays ray_"+str(temp_image)
  elif now("sunday") and bp_first_sex_teacher==1:            ## MC Simone is there on Sunday after clothing change
    $action_image= "squirrel rays ray_"+str(temp_image)+"b"
  else:                                                      ## MC in suit from Simone
    $action_image= "squirrel rays ray_"+str(temp_image)+"a"

  center "{image=[action_image]@400x600}"                    ## CONSIDER REDUCING SIZE OF IMAGE!
  ""
  "[rays_bot.model_description]"
  ""
  choice(">>>rays_buy_bot_preview:{},{}".format(rays_bot_index-1,bot_price)) "Bot Info"

## 0.15.n insert call to decision when Simone is at Raymond's on Sunday after delivering Sucky Bot
  $global bp_first_sex_teacher
  if now("sunday") and bp_first_sex_teacher==1:              ## Simone is at Raymond's on Sundays - first sex is set when you deliver Sucky Bot
    choice("rays_date_decision",pos=17) "Show Over"
## end insertion, next line was if - changed to elif

  elif rays_first_boutique_visit==1:                         ## activate online on first visit only!!
    choice("rays_activate_online",pos=17) "Show Over"
  else:
    choice("rays_show_over",pos=17) "Show Over"
  return

label rays_leaving_early:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)               ## random between 2 backgrounds
  header "Raymond's Bot Boutique - Leaving Early"
  "You feel uncomfortable and decide to leave the show early."
  "{size=-22} "
  $temp_image=random.randint(25,26)

# 0.15.n support clothing change - function not used on Sundays when Simone is there
  if bp_suit_for_rays==0:                                    ## MC in original clothing (not given suit by Simone)
    $action_image= "squirrel rays ray_"+str(temp_image)
  else:                                                      ## MC in suit from Simone
    $action_image= "squirrel rays ray_"+str(temp_image)+"a"

  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Everyone is paying attention to the show and don't even notice you leaving."
  if rays_first_boutique_visit==1:                           ## activate online on first visit only!
    choice("rays_activate_online",pos=17) "Leave"
  else:
    choice("rays_leave",pos=17) "Leave"                      ## function after viewing part of show
  return

## 0.15.n FOR SUNDAY WITH SIMONE insert 2 functions which replace the 'rays_show_over' function below the insert
##   1st function is called after from viewing the last bot (2 functions above) and provides the Yes/No decision for going home with Simone
##       if you select yes you go to 'sd_arriving' in the file 'date_simone.rpy'
##       if you select no you call the 2nd function
##   2nd is used if you select No and don't go home with Simone and it goes to 'rays_leave' (3 functions below)

label rays_date_decision:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)             ## random between 2 backgrounds
  header "Raymond's Bot Boutique - Show is Over"
  $global rays_bot_count
  $rays_bot_count=6                                        ## if you used the 'skip show' button force the show to reach the end
  "After the last bot you discuss the show with {mark}[ns_teacher_name]{/} briefly but soon she changes the subject."
  "{size=-22} "
  $temp_image=random.randint(35,36)
  $action_image= "squirrel rays ray_"+str(temp_image)+"b"  ## function only used on Sundays with Simone
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "{mark}[ns_teacher_name]{/} asks; {say}It's early and I'm not teaching tonight, would you like to come home with me?{/}"
  choice("sd_arriving",cost=[("energy",3)]) "Yes"
  choice("rays_decide_no") "No"
  return

label rays_decide_no:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)             ## random between 2 backgrounds
  header "Raymond's Bot Boutique - Going Home"
  "You tell {mark}[ns_teacher_name]{/} that you're very sorry but you can't do it tonight."
  "{size=-22} "
  $temp_image=random.randint(39,40)
  $action_image= "squirrel rays ray_"+str(temp_image)+"b"  ## function only used on Sundays with Simone
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "You say goodbye and as you're leaving {mark}[ns_teacher_name]{/} looks upset while talking with the host which makes you feel bad."
  call mc_update_relation(ns_teacher_name,-2,0)            ## lose 2 relationship point
  $mc.mood.give_xp(randint(-50,-30))                       ##  large mood decrease
  choice("rays_leave") "Leave"
  return

## end of 0.15.n insert

label rays_show_over:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)               ## random between 2 backgrounds
  header "Raymond's Bot Boutique - Show is Over"
  "When the show ends the host thanks everyone for coming and reminds us there is a show every evening."
  "{size=-22} "
  $temp_image=random.randint(27,28)

# 0.15.n support clothing change - function not used on Sundays when Simone is there
  if bp_suit_for_rays==0:                                    ## MC in original clothing (not given suit by Simone)
    $action_image= "squirrel rays ray_"+str(temp_image)
  else:                                                      ## MC in suit from Simone
    $action_image= "squirrel rays ray_"+str(temp_image)+"a"

  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "You feel a little out of place heres so you quickly head for the door. Everyone else begins slowly making their way to the door."
  if rays_first_boutique_visit==1:                           ## activate online on first visit only!
    choice("rays_activate_online",pos=17) "Leave"
  else:
    choice("rays_leave",pos=17) "Leave"                      ## function after viewing part of show
  return

label rays_buy_bot_preview(bot_n_and_price):
  python:
    bot_n,sep,price=bot_n_and_price.partition(",")
    bot_n=int(bot_n)
    rays_bot=rays_boutique_bots_for_sale[bot_n]
    price=int(price)
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)           ## random between 2 backgrounds
  header "Raymond's Bot Boutique - Bot Information"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_bot.model_id] avatar@400x600}"  ## avatar on left
  $act.set_block("c")                                       ## description and picture on right
  "Model: {mark}[rays_bot.model_name]{/}"
  "Rate: {mark}[rays_bot.rate]{/}"
##  "Price: {mark}$[price]{/}"
  "Price: {mark}[money_str[bot_price]]{/}"                  ## 0.11.3 use MoneyStr()
  ""
  "[rays_bot.model_description]"
  ""
  "Default Name: {mark}[rays_bot.name]{/}"
  $rays_traits=[trait for trait in rays_bot.psychocore.traits if not trait.hidden]
  if rays_traits:
    python:
      temp_text=""
      for rays_trait in rays_traits:
        desc=rays_trait.description
        if rays_trait.inherent:
          if temp_text=="":
            temp_text=rays_trait.name
          else:
            temp_text=temp_text+", "+rays_trait.name
  else:
    $temp_text="None"
  "Traits: {mark}[temp_text]{/}"
  python:
    temp_text=[]
    for slot in rays_bot.outfit_slots:
      part_id=rays_bot.item_on_slot(slot)
      text_line=str(part_id.slot)+": {mark}"+part_id.name+" ("+part_id.rate+"){/}"
      temp_text.append(text_line)
  $n=0
  while n<len(temp_text):
    $text_line=temp_text[n]
    "[text_line]"
    $n+=1
##  $act.add_screen("bot_preview",rays_bot.id,("info","psychocore","chassis","stats","skills","traits","parts","-parts_desc","-defects"))

  $rays_available_capsule=home.available_capsules
  $rays_available_space=workshop.available_space
  call sr24_add_bot_ok                                   ## sets 'sr24_rooom_for_bot=1 if there is room
  if sr24_room_for_bot==1:                               ## space available, button active
    choice("rays_buy_bot_do:{}".format(bot_n),cost=[("money",price)]) "Buy [rays_bot.name]"
  else:
    choice("") "Shop Full"
  if rays_bot_count==1:
    choice ("rays_display_bot_2") "Don't Buy Bot"
  elif rays_bot_count==2:
    choice ("rays_display_bot_3") "Don't Buy Bot"
  elif rays_bot_count==3:
    choice ("rays_display_bot_4") "Don't Buy Bot"
  elif rays_bot_count==4:
    choice ("rays_display_bot_5") "Don't Buy Bot"
  elif rays_bot_count==5:
    choice ("rays_display_bot_6") "Don't Buy Bot"
  elif rays_bot_count==6:
    if rays_first_boutique_visit==1:                     ## activate online on first visit only!!
      choice("rays_activate_online") "Don't Buy Bot"
    else:
      choice("rays_show_over") "Don't Buy Bot"
  return

label rays_buy_bot_do(bot):
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)           ## random between 2 backgrounds
  header "Raymond's Bot Boutique - Purchased Bot"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_which_bot] avatar@400x600}"  ## avatar on left
  $act.set_block("c")                                    ## description and picture on right
  $rays_bot=rays_boutique_bots_for_sale.pop(int(bot))
  $rays_bot_index-=1                                     ## decrement index because bot removed from list
  call sr24_add_bot_do(rays_bot)                         ## space check in calling function-priority:capsule then storage
  "You buy {mark}[rays_bot]{/}, model {mark}[rays_bot.model_name]{/}."
  $rays_bought_bot=1                                     ## set flag for this visit (will not activate online)
  if rays_bot_count==1:
    choice ("rays_display_bot_2") "Continue"
  elif rays_bot_count==2:
    choice ("rays_display_bot_3") "Continue"
  elif rays_bot_count==3:
    choice ("rays_display_bot_4") "Continue"
  elif rays_bot_count==4:
    choice ("rays_display_bot_5") "Continue"
  elif rays_bot_count==5:
    choice ("rays_display_bot_6") "Continue"
  elif rays_bot_count==6:
    if rays_first_boutique_visit==1:                     ## activate online on first visit only!!
      choice("rays_activate_online") "Continue"
    else:
      choice("rays_show_over") "Continue"
  return

label rays_leave:                                    ## use "rays_bot_count" to know if leaving early (1-5) or at the end (6)
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)       ## random between 2 backgrounds
  header "Raymond's Bot Boutique"
  if rays_first_boutique_visit==1:
    $rays_first_boutique_visit=0                     ## clear flag after first visit
    "That sure was an interesting show! I'm sure glad I had a free pass though, it's a high class place so it's really expensive."
  else:
    "Another expensive evening at {mark}Ray's Bot Boutique{/} looking at high priced bots and having fancy drinks."
  if rays_online_activated==1:                       ## online was just activated, custom text one time only
    $rays_online_activated=2                         ## increment flag to avoid displaying one time text again
    extend " I'm glad the guy told me about {mark}Ray's Online{/} and gave me access. I'll have to check it out when I get home."    
  "{size=-16} "
  if bp_suit_for_rays==0:                            ## MC original outfit
    $action_image= "squirrel rays ray_50" 
  else:                                              ## MC in Suit
    $action_image= "squirrel rays ray_50a" 
  center "{image=[action_image]@760x600}"
  "{size=-16} "
  if rays_bot_count<6:                               ## you left before the end of the show

## 0.15.n add support for clothing change - leave early not used on Sundays when Simone is there
    if bp_suit_for_rays==0:                          ## MC in original clothing (not given suit by Simone)
      "It feels good to get out of that place, I don't really fit in and everyone either ignores me or gives me funny looks."
    else:                                            ## MC in suit from Simone 
      "I'm glad to get out of that place, since I'm wearing a nice suit no one bothers me but this still isn't my type of place."
  else:                                              ## you stayed until the end of the show
    if bp_suit_for_rays==0:                          ## MC in original clothing (not given suit by Simone)
      "Even though I feel a little out of place the drinks were good and I had fun checking out the great luxury bots they sell."
      ""
    elif now("sunday") and bp_first_sex_teacher==1:  ## MC Simone is there on Sunday after clothing change
      "I feel bad not accepting {mark}[ns_teacher_name]'s{/} invitation. If I'm not prepared to go to her place maybe I shouldn't go to {mark}Raymond's{/} on Sundays."
      ""
    else:                                            ## MC in new suit from Simone
      "It was a good show, they have great luxury bots at {mark}Raymond's{/} and the drinks were good too."
      ""   

  while rays_boutique_bots_for_sale:                 ## clean up, clear rays boutique list
    $rays_bot=rays_boutique_bots_for_sale.pop()
    $rays_bot.remove()
    $rays_bot=None
  $rays_boutique_bots_for_sale=None
  choice("goto_home",pos=16,key="home") "[home]"
  choice("goto_street",pos=17,key="cancel") "[street]"
  return

##=========BOUTIQUE SUPPORTING FUNCTIONS

init python:
  def rays_generate_bots():                                                            ## generate list of 6 luxury bots
    notify.disable()
    rv=[]                                                                              ## empty array to hold the 6 bots
    rays_target="test"                                                                 ## 'target' for function below never used in DSCS
    rays_tags=[]                                                                       ## 'tags' list for function below is used in DSCS
    rays_tags.append("luxury")                                                         ## add luxury to tag list for function below
    models=[]                                                                          ## create empty array to hold luxury model bot list
## next line sends the empty array and the 2 parameters created above to the 'generate_bot' function
    process_event("generate_bot",models,rays_target,rays_tags)
## result: 'models' contains 6 luxury bots to sell this time in a 2 item tuple array: bot class name and luxury weight value
    rays_bot_numbers=[]                                                                ## empty array to hold 6 numbers from available luxury bots
    for n in range(len(models)):                                                       ## create a list of numbers from 0 to (1- luxury bots) in game
      rays_bot_numbers.append(n)                                                       ## append number to list
    rays_selected_numbers=random.sample(rays_bot_numbers, 6)                           ## select 6 numbers from list with no duplicates
##    print rays_selected_numbers  ##debug line
    for n in range(6):                                                                 ## create 6 bots using 'models' - 0 to 5 array range
      temp=models[rays_selected_numbers[n]]                                            ## returns 2 item tuple for each of the 6 bots
      bot_cls=getattr(store,"SexBot"+temp[0],None)                                     ## get bot class: learned 'getattr' and class is 1st item
      temp_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))       ## creates bot with all default values using the bot class 
# next line inserted in v0.6.0beta, bug fix courtesy of My_Shaky
      store.global_bots_counter+=1
      generate_bot_warranty_seals(temp_bot,default_generate_bot_warranty_seals_table)  ## warranty seals
      rv.append(temp_bot)                                                              ## add bot to array
##    print rv  ##debug line
    notify.enable()
    return rv

  def rays_calc_bot_price(rays_bot_p):  ## python function

## 1) get bot base price using rate
## 2) get parts prices for default bot parts and sum them
## 3) get number of traits and multiply by trait value based upon bot rate
## 4) add up base price, sum of part prices, and trait value
## 5) multiply by markup value
##    print "START rays_calc_bot_price"
    temp_rate=rays_bot_p.rate
##    print "Bot Rate:",temp_rate
    temp0=base_bot_model_prices[temp_rate]
##    print "bot base price:",temp0
    temp_price_mult=getattr(rays_bot_p,"price_mult")
    if temp_price_mult==0:
      temp_price_mult=1
##    print "Bot Price Mult:",temp_price_mult
    temp1=0                                             ## holds sum of part prices
    for slot in rays_bot_p.outfit_slots:
##      print "START part calc:",slot
      part=rays_bot_p.item_on_slot(slot)
      part_s=part.id
##      print "part:",part_s
      n=0                                               ## loop index
      part_n=0                                          ## index of part
##      print "Length of rays_all_parts_list:",len(rays_all_parts_list)
      for n in range(0,len(rays_all_parts_list)):       ## go through parts list find the correct item
        temp_id=rays_all_parts_list[n][0]               ## element 0 is id
        temp_id="bot_part_"+temp_id
##        print "temp_id:",temp_id,"part_s:",part_s
        if temp_id==part_s:                             ## id matches string value of part (I hope!
          part_n=n                                      ## store the index of the part in an integer
##          print "found the index:",part_n
          break                                         ## since we've found it "break" out of the loop
      part_s=str(part_n)                                ## the 'rays_calc_part_price' function requires a string
      part_price=rays_calc_part_price(part_s)
##      print "part_price:",part_price
      temp1+=part_price
##      print "END part calc:",slot
##    print "Parts Sum:",temp1
    temp2=len(rays_bot_p.psychocore.traits)             ## count number of default traits bot - no bad traits when purchased at store
##    print "Traits:",temp2
    if rays_bot_p.rate=="F" or rays_bot_p.rate=="E" or rays_bot_p.rate=="D" or rays_bot_p.rate=="C":
      temp2=temp2*rays_trait_price
##      print "Traits Price (standard):",temp2
    elif rays_bot_p.rate=="B" or rays_bot_p.rate=="A" or rays_bot_p.rate=="S":
      temp2=temp2*rays_trait_price_luxury
      
##      print "Traits Price (luxury):",temp2

##    print"temp0:",temp0,"type:",type(temp0)
##    print"temp1:",temp1,"type:",type(temp1)
##    print"temp2:",temp2,"type:",type(temp2)
##    print "Base Bot Price:",temp0+temp1+temp2

    rays_bot_markup=rays_bot_markup_dict[rays_bot_p.rate]
##    print "rays+bot_markup:",rays_bot_markup
    temp_price=(temp0+temp1+temp2)*rays_bot_markup*temp_price_mult
    temp_price=int(temp_price/100)*100
    rv=int(temp_price)
##    print "Marked Up Final Price:",rv
##    print "END rays_calc_bot_price"
    return rv

##============RAYS ONLINE STORE================

##  $temp_image=random.randint(27,28)
##  $action_image= "squirrel rays ray_"+str(temp_image)


label rays_activate_online:
  $temp_image=random.randint(1,2)
  $game_bg="rays_boutique bg_"+str(temp_image)           ## random between 2 backgrounds
  if rays_bot_count<6:                                   ## leaving early
    header "Raymond's Bot Boutique - Leaving Early"
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "squirrel rays ray_29"
    center "{image=[action_image]@400x600}"
    ""
    $temp_image=random.randint(25,26)
    $action_image= "squirrel rays ray_"+str(temp_image)
    center "{image=[action_image]@400x600}"
    ""
    $act.set_block("c")
    "The host notices you leaving and hurries over to talk to you before you make it to the door. You turn around to face him and he says:"
    ""
    "{say}I'm sorry you're leaving early. I have to get back to the show but I want to tell you about our online store and give you access. We sell lower priced bots and all types of parts online.{/}"
    ""
    "The host quickly returns to the show but you're glad he gave you access to {mark}Ray's Online{/}. You're sure it will be more useful than the boutique right now."
  else:                                                  ## stayed until end
    header "Raymond's Bot Boutique - Show is Over"
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "squirrel rays ray_30"
    center "{image=[action_image]@400x600}"
    ""
    $temp_image=random.randint(27,28)
    $action_image= "squirrel rays ray_"+str(temp_image)
    center "{image=[action_image]@400x600}"
    ""
    $act.set_block("c")
    "As you're heading for the door the host asks you to wait a minute. You turn around to face him and he says:"
    ""
    "{say}We haven't seen you here before, I hope you enjoyed the evening. If you don't mind me saying, you aren't our typical client here. Let me tell you about our online store and give you access. We sell lower priced bots and all types of parts online.{/}"
    ""
    "You take the information about {mark}Ray's Online{/} thinking this might be more worthwhile than the boutique until your shop becomes more successful."
  $rays_online_activated=1                               ## activate the online store and avoid repeat
  ""
  $quests.where_to_get_bots.add_method("sr24_rays_online","you can find non-luxury bots for sale at {mark}Ray's Online{/}, accessible through your {mark}[netconsole]{/}")
  $quests.where_to_get_bot_parts.add_method("sr24_rays_online","you can find bot parts for sale at {mark}Ray's Online{/}, accessible through your {mark}[netconsole]{/}")
  choice ("rays_leave",pos=17) "Continue"                ## go to normal leave screen
  return

label rays_online_store:
  $rays_part_top_row=0                                      ## reset top row counter on select part type (slot) and select part screens
  $rays_current_row=1                                       ## reset current row counter on select part type (slot) screen
  $game_bg="home computer"                                  ## should be bedroom at computer
  header "[netconsole] - Ray's Bots Online"
  "Please select our fine bot store or our full service parts store."
  ""
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")                                       ## generic female bot image on left
  $temp_image=random.randint(32,34)
  $action_image= "squirrel rays ray_"+str(temp_image)       ## random 1 of 3
  center "{image=[action_image]@400x600}"
  $act.set_block("c")                                       ## Outline of bot image on right
  $action_image= "squirrel rays ray_31"                     ## only 1 image for parts
  center "{image=[action_image]@400x600}"
  call rays_create_slots_list                               ## create slots list and part markup list each time online store is entered
  call rays_create_parts_list                               ## create parts list each time online store is entered
  if rays_online_bot_list==0:                               ## when flag is clear you need to generate a new list - cleared every morning in 'squirrel_home_workout_main.rpy'
    $rays_online_bot_list=1                                 ## set flag so you use same list until tomorrow

## POSSIBLE BUG FIX IN v0.6.0beta 
    while rays_online_bots_for_sale:                        ## clean up, clear rays online list
      $flea_bot=rays_online_bots_for_sale.pop()
      $flea_bot.remove()
      $flea_bot=None
    $rays_online_bots_for_sale=None

    $rays_online_bots_for_sale=rays_online_generate_bots()  ## generate array containing up to 12 non-luxury bots
  choice("rays_online_bots") "Bot Store"
  choice("rays_online_parts",pos=3) "Parts Store"
  choice("goto_home",pos=16,key="home") "Log out"
  choice("netconsole_net_sites",pos=17,key="cancel") "Back"
  return

label rays_online_bots:
  $game_bg="home computer"                       ## should be bedroom at computer
  header "[netconsole] - Ray's Bot's Online"
## GRAPHICS on left
  $act.start_block("l:352 c:content_width-352")
  $act.set_block("l")
  ""
  ""
  $temp_image=random.randint(32,34)
  $action_image= "squirrel rays ray_"+str(temp_image)       ## random 1 of 3
  center "{image=[action_image]@320x480}"
  ## TEXT on right
  $act.set_block("c")
  "{good}Online Bot Store: Today's Selection{/}"
  ""
  "Please select any of these fine bots for more information:"
  ""
  $bot_n=0
  while bot_n<len(rays_online_bots_for_sale):
    $rays_bot=rays_online_bots_for_sale[bot_n]
    $bot_n+=1
    $bot_price=rays_calc_bot_price(rays_bot)
    $money_tag="{bad}" if bot_price>mc.money else "{mark}"
##    "#[bot_n] - model: {mark}[rays_bot.model_name]{/}, price: [money_tag]$[bot_price]{/}"
    "#[bot_n] - model: {mark}[rays_bot.model_name]{/}, price: [money_tag][money_str[=bot_price]]{/}"         ## 0.11.3 use MoneyStr()
    choice(">>>rays_online_bot_preview:{},{}".format(bot_n-1,bot_price)) "#[bot_n] - [rays_bot.model_name]"
    $bot=None
  choice("goto_home",pos=16,key="home") "Log out"
  choice("rays_online_store",pos=17,key="cancel") "Back"
  return

label rays_online_bot_preview(bot_n_and_price):
  python:
    bot_n,sep,price=bot_n_and_price.partition(",")
    bot_n=int(bot_n)
    rays_bot=rays_online_bots_for_sale[bot_n]
    price=int(price)
  header "[netconsole] - Ray's Bot's Online"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_bot.model_id] avatar@400x600}"  ## avatar on left
  $act.set_block("c")                                       ## description and picture on right
  "Model: {mark}[rays_bot.model_name]{/}"
  "Rate: {mark}[rays_bot.rate]{/}"
##  "Price: {mark}$[price]{/}"
  "Price: {mark}[money_str[price]]{/}"                      ## 0.11.3 use MoneyStr()
  ""
  "[rays_bot.model_description]"
  ""
  "Default Name: {mark}[rays_bot.name]{/}"
  $rays_traits=[trait for trait in rays_bot.psychocore.traits if not trait.hidden]
  if rays_traits:
    python:
      temp_text=""
      for rays_trait in rays_traits:
        desc=rays_trait.description
        if rays_trait.inherent:
          if temp_text=="":
            temp_text=rays_trait.name
          else:
            temp_text=temp_text+", "+rays_trait.name
  else:
    $temp_text="None"
  "Traits: {mark}[temp_text]{/}"
  python:
    temp_text=[]
    for slot in rays_bot.outfit_slots:
      part_id=rays_bot.item_on_slot(slot)
      text_line=str(part_id.slot)+": {mark}"+part_id.name+" ("+part_id.rate+"){/}"
      temp_text.append(text_line)
  $n=0
  while n<len(temp_text):
    $text_line=temp_text[n]
    "[text_line]"
    $n+=1
  $rays_available_capsule=home.available_capsules
  $rays_available_space=workshop.available_space
  call sr24_add_bot_ok             ## sets 'sr24_rooom_for_bot=1 if there is room
  if sr24_room_for_bot==1:
    $rays_which_bot=rays_bot.model_id
    choice("rays_online_buy_bot_do:{}".format(bot_n),cost=[("money",price)]) "Buy [rays_bot.name]"
  else:
    choice("") "Shop Full"
  choice("rays_online_bots") "Back"
  return

label rays_online_buy_bot_do(rays_bot_p):
  $game_bg="home computer"                                  ## should be bedroom at computer
  header "[netconsole] - Ray's Bot's Online"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [rays_which_bot] avatar@400x600}"     ## avatar on left
  $act.set_block("c")                                       ## description and picture on right
  $pop_number=int(rays_bot_p)
  $rays_bot_p=rays_online_bots_for_sale[pop_number]
  call sr24_add_bot_do(rays_bot_p)                                 ## space check in calling function-priority: capsule then storage
  "You buy {mark}[rays_bot_p]{/}, model {mark}[rays_bot_p.model_name]{/}."
## next 9 lines inserted in v0.6.0beta, bug fix courtesy of My_Shaky
  python:
    notify.disable()
    bot_cls=find_character_cls(rays_online_bots_for_sale[pop_number].id[:rays_online_bots_for_sale[pop_number].id.rfind("_")])
    bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))
    bot.name=randchoice(bot.name_variants)
    store.global_bots_counter+=1
    generate_bot_warranty_seals(bot,default_generate_bot_warranty_seals_table)
    rays_online_bots_for_sale[pop_number] = bot
    notify.enable()
  choice ("rays_online_bots") "Continue"
  return

label rays_online_parts:
  $rays_part_top_row=0                                       ## reset top row counter on select part type (slot) and select part screens
  $game_bg="home computer"                                   ## should be bedroom at computer
  header "[netconsole] - Ray's Bot's Online"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  ""
  $action_image= "squirrel rays ray_31"                     ## only 1 image for parts
  center "{image=[action_image]@320x480}"
  ## TEXT on right
  $act.set_block("c")
  "{good}Online Parts Store{/}"
  ""
  "Please select which type of part you would like to purchase:"
  ""
  $rays_first_slot=(rays_current_row-1)*6                    ## row 1=0, row 2=6, row 3=12, etc.
  $rays_last_slot=len(rays_all_slots_list)                   ## set last slot to end of list
##  $print "Slot Count:",rays_last_slot
  $temp_float=float(rays_last_slot-0.1)                      ## create a floating version of the integer minus a little
  $rays_last_row=int(temp_float/6)+1                         ## should be 2 for vanilla game, 3 if you add Daedalron Bots, etc.
##  $print "Last Row:",rays_last_row
  if rays_last_slot>rays_first_slot+12:                      ##  if NOT true display all, if true cannot display all
    $rays_last_slot=rays_first_slot+12                       ##  last displayed slot will be 12 more than first displayed slot - 2 full rows
  $count=0
  $max_count=rays_last_slot-rays_first_slot
  while count < max_count:                                   ##  count is number of slots to display - -1 because we start with 0
    $pop_number=rays_first_slot+count
    $rays_part_slot=rays_all_slots_list[pop_number][0]       ## replace 'pop' function - list item [0] is slot id
    $rays_part_slot_name=rays_all_slots_list[pop_number][1]  ## list item 1 is slot name
    $count+=1
    $temp0=pop_number+1                                      ## pop number is array index, add 1 to start with 1
    "#[temp0] - {mark}[rays_part_slot_name]{/}"
    choice("rays_online_parts_type:"+rays_part_slot) "#[temp0] - [rays_part_slot_name]"
  if rays_last_row<3:                                        ##  only 2 rows; Down=NO, UP=NO
    choice(None,pos=14) "Scroll Up"
    choice(None,pos=15) "Scroll Down"
  elif rays_last_row>rays_current_row+1:                     ##  CANNOT display last row; Down=Yes
    if rays_current_row>1:                                   ##  Top row NOT 1; Up=Yes
      choice("rays_scroll_up",pos=14) "Scroll Up"
    else:                                                    ##  Top row 1; Up=NO
      choice(None,pos=14) "Scroll Up"
    choice("rays_scroll_down",pos=15) "Scroll Down"
  else:                                                      ##  CAN display last row; Down=No
    if rays_current_row>1:                                   ##  Top row NOT 1; Up=Yes
      choice("rays_scroll_up",pos=14) "Scroll Up"
    else:                                                    ##  Top row 1; Up=NO
      choice(None,pos=14) "Scroll Up"
    choice(None,pos=15) "Scroll Down"
  choice("goto_home",pos=16,key="home") "Log out"
  choice("rays_online_store",pos=17,key="cancel") "Back"
  return

label rays_online_parts_type(slot_p):                 ## receives slot ID in 'rays_all_slots_list' from array of buttons
  $rays_part_slot=slot_p                              ## put the parameter passed back into global variable
  $n=int(0)
  while n<len(rays_all_slots_list):                   ## iterate through slots list to find name
    if rays_all_slots_list[n][0]==slot_p:
      $temp1=rays_all_slots_list[n][0]
      $rays_part_slot_name=rays_all_slots_list[n][1]  ##1 is name
    $n+=1
  $game_bg="home computer"                            ## should be bedroom at computer
  header "[netconsole] - Ray's Bot's Online"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  ""
  $action_image= "squirrel rays ray_31"                     ## only 1 image for parts
  center "{image=[action_image]@320x480}"
  ## TEXT on right
  $act.set_block("c")
  "{good}[rays_part_slot_name] List{/}"
  ""
  "Please select one of these fine bot parts for more information:"
  ""
  $n=int(0)                                                                      ## counter into 'rays_all_parts_list'
  $m=int(0)                                                                      ## counter for parts to actually display (want 12)
  $rays_part_type_total=0
  while n<len(rays_all_parts_list):                                              ## go through parts list to extract parts for this slot
    $temp1=rays_all_parts_list[n][6]                                             ## element 6 is slot
    if temp1==slot_p:                                                            ## part slot must match passed 'slot' parameter
      $rays_part_type_total+=1                                                   ## increment rays_part_type_total
      if m>=rays_part_top_row and m<rays_part_top_row+12:                        ## skip hits until desired top row reached, keep 0 through 11
        $part_id=rays_all_parts_list[n][0]                                       ## element 0 is id
        $part_name=rays_all_parts_list[n][1]                                     ## element 1 is name
        $part_rate=rays_all_parts_list[n][2]                                     ## element 2 is rate
        $s=str(m+1)
        "#[s] - part: {mark}[part_name]{/} - rate: {mark}[part_rate]{/}"
        choice(">>>rays_online_part_preview:"+str(n)) "#[s] - [part_name]"       ## n is the index into 'rays_all_parts_list
      $m+=1 
    $n+=1
  if rays_part_top_row==0:                                                       ## at the top, inactive 'scroll up'
    choice(None,pos=14) "Scroll Up"
  else:                                                                          ## not at top, active 'scroll up'
    choice("rays_scroll_up_parts",pos=14) "Scroll Up"
  if rays_part_type_total<=rays_part_top_row+12:                                 ## on last page, inactive 'scroll down'
    choice(None,pos=15) "Scroll Down"
  else:                                                                          ## another page, active 'scroll down'
    choice("rays_scroll_down_parts",pos=15) "Scroll Down"
  choice("goto_home",pos=16,key="home") "Log out"
  choice("rays_online_parts",pos=17,key="cancel") "Back"      ## have to go back to part selection so entry into part type works properly
  return

label rays_online_part_preview(part_s):          ## parameter passed is STRING with position of part in 'rays_all_parts_list'
  $part_n=int(part_s)                            ## convert string to integer required to access list
  $game_bg="home computer"                       ## should be bedroom at computer
  header "[netconsole] - Ray's Bot's Online"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  ""
  $action_image= "squirrel rays ray_31"                     ## only 1 image for parts
  center "{image=[action_image]@320x480}"
  ## TEXT on right
  $act.set_block("c")
##  "Position in parts array: [part_s]"
##  "Required: $part_price=rays_calc_part_price(part_id)"
##  ""
  $rays_part_rate=rays_all_parts_list[part_n][2]              ## element 2 is rate
  $rays_part_base_price=base_bot_part_prices[rays_part_rate]  ## look up base price for the part rating
  $rays_price_mult=rays_all_parts_list[part_n][5]             ## element 5 is price_mult
  $slot_key=rays_all_parts_list[part_n][6]                    ## element 6 is slot
  $rays_part_price=rays_calc_part_price(part_s)               ## parameter passed is STRING with position of part in 'rays_all_parts_list'
  $temp0=rays_all_parts_list[part_n][1]
  "Part: {mark}[temp0]{/}"                                    ## element 1 is name
  $temp0=rays_all_parts_list[part_n][2]
  "Rate: {mark}[temp0]{/}"                                    ## element 2 is rate
  if rays_part_price<=mc.money:
##    "Price: {mark}$[rays_part_price]{/}"
    "Price: {mark}[money_str[rays_part_price]]{/}"            ## 0.11.3 use MoneyStr()
    choice("rays_online_part_buy_do:{}".format(part_n),cost=[("money",rays_part_price)]) "Buy Part"    ## sends unicode of number in parts "list of lists"
  else:
    "Price: {bad}[rays_part_price]{/}"
    choice(None) "Buy Part"                                   ## sends unicode of number in parts "list of lists"
  ""
  $temp0=rays_all_parts_list[part_n][4]
  "Description: {mark}[temp0]{/}"                             ## element 4 is description
  ""
##  "rays_part_rate: [rays_part_rate]"
##  "rays_part_base_price: [rays_part_base_price]"
##  "rays_price_mult: [rays_price_mult]"
  $temp0=rays_part_markup[slot_key]
##  "rays_part_markup: [temp0]"
  choice("rays_online_parts_type:"+rays_part_slot) "Cancel"
  choice("goto_home",pos=16,key="home") "Log out"
  choice("rays_online_parts",pos=17,key="cancel") "Back"      ## have to go back to part selection so entry into part type works properly
  return

label rays_online_part_buy_do(part_s):                    ## parameter received is a STRING with position of part in 'rays_all_parts_list'
  $part_n=int(part_s)                                     ## need integer to access list
  $temp0=rays_all_parts_list[part_n][1]                   ##1 is part name
  $game_bg="home computer"                                ## should be bedroom at computer
  header "[netconsole] - Ray's Bot's Online"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $action_image= "squirrel rays ray_31"                     ## only 1 image for parts
  center "{image=[action_image]@320x480}"
  ## TEXT on right
  $act.set_block("c")
  ""
  "You buy the {mark}[temp0]{/} part..."
  ""

  $part_slot=rays_all_parts_list[part_n][6]               ## element 6 is slot: save this to return to buy same part type screen
  $part_key=rays_all_parts_list[part_n][0]                ## element 0 is id
  $part_key="bot_part_"+part_key
  $part_class=modded_bot_part_classes[part_key]
  $part_id=part_class.id
  $workshop.add_item(part_id)
  choice("rays_online_parts_type:"+rays_part_slot) "Continue"
  choice("goto_home",pos=16,key="home") "Log out"
  choice("rays_online_parts",pos=17,key="cancel") "Back"  ## cannot go back to same type of part
  return

##============ONLINE STORE - SUPPORTING FUNCTIONS================

init python:
  def rays_calc_part_price(part_s):
    part_n=int(part_s)                                         ## need integer to access list
    rays_part_rate=rays_all_parts_list[part_n][2]              ## element 2 is rate
    rays_part_base_price=base_bot_part_prices[rays_part_rate]  ## look up base price for the part rating
##    print "rays_part_base_price:",rays_part_base_price
    rays_price_mult=rays_all_parts_list[part_n][5]             ## element 5 is price_mult
##    print "rays_price_mult:",rays_price_mult
    slot_key=rays_all_parts_list[part_n][6]                    ## element 6 is slot
##    print "slot_key:",slot_key
    rays_part_rate_mult=rays_part_rate_markup_dict[rays_part_rate]
##    print "rays_part_rate_mult:",rays_part_rate_mult
    rays_part_price=rays_part_base_price*rays_price_mult*rays_part_markup[slot_key]*rays_part_rate_mult
##    print "rays_part_price:",rays_part_price
    rv=int(rays_part_price/10)*10                              ## truncate down to even 10
##    print "rays_part_price (rounded):",rv
    return rv

label rays_scroll_up:    ##  new scroll function
  $rays_current_row-=2
  return "rays_online_parts"

label rays_scroll_down:  ##  new scroll function
  $rays_current_row+=2
  return "rays_online_parts"

label rays_scroll_up_parts:
  $rays_part_top_row-=12
  return ("rays_online_parts_type:"+rays_part_slot)
    
label rays_scroll_down_parts:
  $rays_part_top_row+=12
  return ("rays_online_parts_type:"+rays_part_slot)

label rays_create_slots_list:
##  NEED TO TEST USING DAEDALRON BOTS to test scroll up and scroll down
  python:
    rays_all_slots_list=[]                                       ## ensure list is empty at start
    rays_temp_slots=load_info_table_from_mods("bot_part_slots")  ## get list of all slot names - will include vanilla slots
##    print "Number of Slots:",len(rays_temp_slots)
##    print "START rays_temp_slots"
##    print rays_temp_slots
##    print "end rays_temp_slots"
    temp0=[]
    for temp0 in rays_temp_slots:
##      print "Item:",temp0
## create 'list of lists' with (id=0,name=1,list_priority=2,category_price_mult=3)
      temp1=rays_temp_slots[temp0].get(u'id')
      temp2=rays_temp_slots[temp0].get(u'name')
      temp3=rays_temp_slots[temp0].get(u'list_priority')
      temp4=rays_temp_slots[temp0].get(u'category_price_mult')
      rays_all_slots_list.append([temp1,temp2,temp3,temp4])      ## append data to list
    rays_all_slots_list.sort(key=lambda x: x[2])                 ## sort the COMPLETED list IN PLACE using [2] - list_priority
##    print "START slot list"
##    print rays_all_slots_list
##    print "END slot list"
## create 'rays_part_markup here
    for n in range(0,len(rays_all_slots_list)):            ## skip items 0 through 10 - vanilla part are already on the markup list
      temp5=rays_all_slots_list[n][0]                      ## item 1 is id
      temp6=rays_all_slots_list[n][3]                      ## item 3 is category_price_mult
##      print "category_price_mult:",temp6
      if temp6<2:
        temp6=2
##        print "Set category_price_mult to minimum:",temp6
      temp6=rays_markup_slope*temp6+rays_markup_intercept  ## linear estimate calculation
##      print "temp6:",temp6
      temp7=int(temp6*100+0.5)                             ## round to 2 decimal places part 1
##      print "temp7:",temp7
      temp8=float(temp7)
##      print "temp8:",temp8
      temp6=temp8/100                                      ## truncate to 2 decimal places part 2
##      print "temp6:",temp6
##      print "slot:",temp5,"markup:",temp6
      rays_part_markup[temp5]=temp6                        ## add key,value to dict
##    print "START rays_part_markup"
##    print rays_part_markup
##    print "END rays_part_markup"
    rays_temp_slots=[]                                           ## clear the temporary slot list, no longer needed
  return

label rays_create_parts_list:
  python:
    rays_all_parts_list=[]                                  ## ensure list is empty at start
    rays_temp_parts=load_info_table_from_mods("bot_parts")  ## load parts
##    print "Number of Parts:",len(rays_temp_parts)
    temp0=[]
    for temp0 in rays_temp_parts:
##      print "Item:",temp0
## create 'list of lists' with (id=0, name=1, rate=2, rate_level=3, description=4, price_mult=5, slot=6)
      temp1=rays_temp_parts[temp0].get(u'id')
      temp2=rays_temp_parts[temp0].get(u'name')
      temp3=rays_temp_parts[temp0].get(u'rate')
      if temp3=="S":
        temp_level=7
      elif temp3=="A":
        temp_level=6
      elif temp3=="B":
        temp_level=5
      elif temp3=="C":
        temp_level=4
      elif temp3=="D":
        temp_level=3
      elif temp3=="E":
        temp_level=2
      else:
        temp_level=1
      temp4=rays_temp_parts[temp0].get(u'description')
      temp5=rays_temp_parts[temp0].get(u'price_mult')
      temp6=rays_temp_parts[temp0].get(u'slot')
      if "missing" not in temp2:                                                      ## if 'missing' NOT there add part (omit 'missing parts')
        rays_all_parts_list.append([temp1,temp2,temp3,temp_level,temp4,temp5,temp6])  ## append data to list
    rays_all_parts_list.sort(key=lambda x:-x[3])                                      ## sort the COMPLETED list IN PLACE using [3] (rate level)
##    print "START rays_all_parts_list"
##    print rays_all_parts_list
##    print "END rays_all_parts_list"
    rays_temp_parts=[]                                                                ## clear the temp parts list, no longer needed
  return

init python:
##  NEED TO TEST USING ShakyMod_parts to have lots of parts to fill test previous and next
  def rays_make_part_list(top_row_p):
    rv=[]
    for n in range(0,len(rays_all_parts_list)):              ## go through parts list to extract parts for this slot'
      temp0=rays_all_parts_list[n][6]                        ## element 6 is slot
      if temp0==slot:                                        ## part slot must match passed 'slot' parameter
        rv.append(n)                                         ## only need list of part position because 'rays_all_parts_list' is global
    return rv

init python:
  def rays_online_generate_bots():                                                     ##  generate list of 12 non-luxury bots
    notify.disable()
    rv=[]                                                                              ## empty array to hold the 12 bots
    rays_target="flea_market_buy_bot"                                                  ## 'target' for function below never used in DSCS
    rays_tags=[]                                                                       ## 'tags' list for function below is used in DSCS
    rays_tags.append("cheap")                                                          ## add cheap to tag list for function below
    rays_tags.append("nice")                                                           ## add nice to tag list for function below
    rays_tags.append("good")                                                           ## add good to tag list for function below
    models=[]                                                                          ## empty array to hold cheap/nice/good model bot list
## next line sends the empty array and the 2 parameters created above to the 'generate_bot' function
    process_event("generate_bot",models,rays_target,rays_tags)
## result: 'models' contains all 'cheap', 'nice', and 'good' bots in the game in a 2 item tuple array: bot class name and weight value
    non_luxury_models=[]                                                               ## array to hold final list
    for n in range(len(models)):                                                       ## loop through all models found
      temp_bot_model=models[n]                                                         ## grab next bot model
      temp_bot_model_cls=getattr(store,"SexBot"+temp_bot_model[0],None)                ## get bot class: learned 'getattr' and class is 1st item
      target_weight=temp_bot_model_cls.list_target_tag_chances.get("luxury")           ## look for 'luxury' tag weight

##      print "temp_bot_model:",temp_bot_model          ##debug line
##      print "temp_bot_model_cls:",temp_bot_model_cls  ##debug line
##      print "target_weight:",target_weight            ##debug line

      if target_weight is None or target_weight==0:                                    ## if nothing comes back or it's set to 0 it's a non-luxury bot
        non_luxury_models.append(temp_bot_model)                                       ## add the model to the final array
      temp_bot_model=[]                                                                ## clear for next time through loop

##    print "START non_luxury_models"  ##debug line
##    print non_luxury_models          ##debug line
##    print "END non_luxury_models"    ##debug line

    rays_bot_numbers=[]                                                                ## empty array to hold 12 numbers from available C&D bots
    for n in range(len(non_luxury_models)):                                            ## create a list of numbers from 0 to 1- C&D bots in game
      rays_bot_numbers.append(n)                                                       ## append number to list
    if len(rays_bot_numbers)>12:
      rays_selected_numbers=random.sample(rays_bot_numbers, 12)  ## select 12 numbers from list with no duplicates
      rays_bot_numbers=[]
      rays_bot_numbers=rays_selected_numbers
##      print rays_selected_numbers  ##debug line
    how_many_bots=len(rays_bot_numbers)
    for n in range(how_many_bots):                                                     ## create 12 bots using 'models' - 0 to 11 array range
      temp=non_luxury_models[rays_bot_numbers[n]]                                      ## returns 2 item tuple for each of the 12 bots
      bot_cls=getattr(store,"SexBot"+temp[0],None)                                     ## get bot class: learned 'getattr' and class is 1st item
      temp_bot=bot_cls(id="{}_#{}".format(bot_cls.id,store.global_bots_counter))       ## creates bot with all default values using the bot class 
      store.global_bots_counter+=1
      generate_bot_warranty_seals(temp_bot,default_generate_bot_warranty_seals_table)  ## warranty seals
      rv.append(temp_bot)                                                              ## add bot to array
##    print rv  ##debug line
    notify.enable()
    return rv


