## Bot Sales: Reputation Gain Functions

## BBS Offers:      bot dealer for all
##                  for specific offers: fighter, sexmachine, tech_trainer, use "trainer" for personal assistant
##                  effect: increases cap price, calculations unchanged

## Robosechs:       bot dealer and sexmachine
##                  effect: increases cap price, calculations unchanged

## Flea Market:     bot dealer and mechanic
##                  effect: increases cap price, calculations unchanged

## 3 things above   formula uses 2 reputations, r1 and r2 with FEDCBAS or 1234567
##                  ((r1 + r2) * mult1 - subt) ^ exp * mult2

## UFC Fight Boss:  bot dealer and fighter
##                  effect: adds to the price which is fixed

init python:
  bbs_bot_offer_type=""      ## this will contain the type of offer based upon 'offer.id'
                             ## it's used when accepting a bot offer:
                                 ##  file:      netconsole_grey_market_bbs.rpy
                                 ##  function:  label netconsole_grey_market_accept_offer(offer_n_request_details): 
                             ## existing function calls are complex, I'm afraid I'll break them so I'm making it global
                             ## it consists of a key word in the offer that identifies which type of bot it is
                             ## this key word must appear in BBS offer mods or they will not get a price increase from reputations
                             ## for combat bots the key word is:   combat
                             ## for sex bots the key word is:      sextoy
                             ## for tech bots the key word is:     repairbot
                             ## for social (personal assistants):  personal

init python:

  def price_rep_bbs_offer(offer_id):           ## offer_id is string from offer, returns dollar value to add to cap
    bbs_mult1=20
    bbs_subt=40                                ## value must be 2x mult1 or function blows up
    bbs_exp=2
    bbs_mult2=2
    split_values = re.split(r'[(_]',offer_id)  ## breaks 'offer_id' into words ...
    combat_test="combat"                       ## ... unique word in offers for combat trained bots
    sex_test="sextoy"                          ## ... unique word in offers for sex trained bots
    tech_test="repairbot"                      ## ... unique work in offers for tech trained bots (either or both elec and mech)
    assistant_test="personal"                  ## ... unique word in offers for social trained bots (personal assistant)

## populate global variable first so it is set even if there is no price increase
    global bbs_bot_offer_type
    if combat_test in split_values:
      bbs_bot_offer_type=combat_test
    elif tech_test in split_values:
      bbs_bot_offer_type=tech_test
    elif sex_test in split_values:
      bbs_bot_offer_type=sex_test
    elif assistant_test in split_values:
      bbs_bot_offer_type=assistant_test
      
##    print "SET: bbs_bot_offer_type: ",bbs_bot_offer_type

##    temp_return=1                                ## FOR TESTING ONLY, makes sure the function was called!!!
    temp_return=0                                ## return 0 if any roles missing, it has no effect

    if "rep_mc_dealer" not in mc.stats:          ## if no dealer rep nothing added, only true when you sell your first bot
      return temp_return
    if combat_test in split_values:              ## if combat bot request ...
      if "rep_mc_fighter" not in mc.stats:       ## ... and no combat rep nothing added
        return temp_return
    elif tech_test in split_values:              ## if techie bot request ...
      if "rep_mc_tech_trainer" not in mc.stats:  ## ... and no tech rep nothing added 
        return temp_return
    elif sex_test in split_values:               ## if sex bot request ...
      if "rep_mc_sexmachine" not in mc.stats:    ## ... and no sex rep nothing added
        return temp_return
    elif assistant_test in split_values:         ## if personal assistant (social) bot request ...
      if "rep_mc_trainer" not in mc.stats:       ## ... and no trainer rep nothing added
        return temp_return
    else:                                        ## error condition: not a bot offer OR bot offer missing key word
      return temp_return

 ##   return 10000  ## FOR TEST PURPOSES, BYPASSES THE ACTUAL REPUTATION TESTS

    rep1=mc.rep_mc_dealer.level
    if combat_test in split_values:    
      rep2=mc.rep_mc_fighter.level
    elif tech_test in split_values:  
      rep2=mc.rep_mc_tech_trainer.level
    elif sex_test in split_values:
      rep2=mc.rep_mc_sexmachine.level
    elif assistant_test in split_values:
      rep2=mc.rep_mc_trainer.level

##    print "rep1: ",rep1, "rep2: ",rep2," bbs_mult1: ",bbs_mult1," bbs_subt: ",bbs_subt
##    print "mantissa: ",(rep1+rep2)*bbs_mult1-bbs_subt
##    print "bbs_exp: ",bbs_exp
##    print "exponent: ",bbs_exp
##    print "result: ",((rep1+rep2)*bbs_mult1-bbs_subt)**bbs_exp
##    print "bbs_mult2: ",bbs_mult2
##    print "final result: ",(((rep1+rep2)*bbs_mult1-bbs_subt)**bbs_exp)*bbs_mult2
    
    temp_value=(((rep1+rep2)*bbs_mult1-bbs_subt)**bbs_exp)*bbs_mult2    ## ((r1 + r2) * mult1 - subt) ^ exp * mult2
    temp_value=round(temp_value)                                        ## round off in case of floating point math oddities
    temp_return=int(temp_value)                                         ## must be 'int'
    return temp_return  

  def price_rep_robosechs():                 ## returns dollar value to add to cap
    rob_mult1=10
    rob_subt=20                              ## value must be 2x mult1 or function blows up
    rob_exp=2
    rob_mult2=1.5
    temp_return=0
    if "rep_mc_dealer" not in mc.stats:      ## if no dealer rep nothing added, only true when you sell your first bot
      return temp_return
    if "rep_mc_sexmachine" not in mc.stats:  ## if no sex bot trainer rep nothing added
      return temp_return
    rep1=mc.rep_mc_dealer.level
    rep2=mc.rep_mc_sexmachine.level
    temp_value=((rep1+rep2)*rob_mult1-rob_subt)**rob_exp*rob_mult2  ## ((r1 + r2) * mult1 - subt) ^ exp * mult2
    temp_value=round(temp_value)                                    ## round off in case of floating point math oddities
    temp_return=int(temp_value)                                     ## must be 'int'
    return temp_return

  def price_rep_flea_market():             ## returns dollar value to add to cap
    fmk_mult1=5
    fmk_subt=10                            ## value must be 2x mult1 or function blows up
    fmk_exp=2
    fmk_mult2=4
    temp_return=0
    if "rep_mc_dealer" not in mc.stats:    ## if no dealer rep nothing added, only true when you sell your first bot
      return temp_return    
    if "rep_mc_mechanic" not in mc.stats:  ## if no mechanic rep nothing added
      return temp_return    
    rep1=mc.rep_mc_dealer.level
    rep2=mc.rep_mc_mechanic.level
    temp_value=((rep1+rep2)*fmk_mult1-fmk_subt)**fmk_exp*fmk_mult2  ## ((r1 + r2) * mult1 - subt) ^ exp * mult2
    temp_value=round(temp_value)                                    ## round off in case of floating point math oddities
    temp_return=int(temp_value)                                     ## must be 'int'
    return temp_return

  def price_rep_ufc_fight():              ## returns dollar value to add to price
    ufc_mult1=10
    ufc_subt=20                           ## value must be 2x mult1 or function blows up
    ufc_exp=2
    ufc_mult2=1.5
    temp_return=0
    if "rep_mc_dealer" not in mc.stats:   ## if no dealer rep nothing added, only true when you sell your first bot
      return temp_return    
    if "rep_mc_fighter" not in mc.stats:  ## if no mechanic rep nothing added
      return temp_return  
    rep1=mc.rep_mc_dealer.level
    rep2=mc.rep_mc_fighter.level
    temp_value=((rep1+rep2)*ufc_mult1-ufc_subt)**ufc_exp*ufc_mult2  ## ((r1 + r2) * mult1 - subt) ^ exp * mult2
    temp_value=round(temp_value)                                    ## round off in case of floating point math oddities
    temp_return=int(temp_value)                                     ## must be 'int'
    return temp_return