define robosechs_bot_price_skills={
  "bot_combat":      (1.0,"mul_exp3",0.0,0.0),
  "bot_electronics": (1.0,"mul_exp3",0.0,0.0),
  "bot_mechanics":   (1.0,"mul_exp3",0.0,0.0),
  "bot_sex":         (1.0,"mul_exp3",0.0,3.0),
  "bot_social":      (1.0,"mul_exp3",0.0,1.5),
  }

define robosechs_bot_integrity_minimum=75

define robosechs_bot_stability_minimum=75

define robosechs_bot_price_cap=50000

label robosechs_sell_bot:
  header "[robosechs] - Selling bot"
  "You enter a quiet office in the back and ask if they are interested in buying bots."
  "{say}Well, we are always looking to restock our female bot toys, but we are not going to pay for combat or techie; only sexual prowess and maybe a basic understanding of social norms are interesting. Also, we want them{/} {mark}stable{/} {say}and in{/} {mark}good condition{/}{say}.{/}"
##  "{say}Oh, and we are not going to pay over [money_str[robosechs_bot_price_cap]], even if you bring proper lux tech. It's just not worth it for us, toys degrade too quickly here.{/}"
  "{say}Also, we won't pay over [money_str[robosechs_bot_price_cap]] unless the dealer is well known and is selling luxury tech. Too many incompetant assholes sell us bots that don't last very long working here.{/}"
  $quests.where_to_sell_bots.add_method("robosechs","{mark}[robosechs]{/} will buy your bots, as long as they are well trained in sex and in good condition")
  ""
  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot and bot.action_allowed("sell"):
          if not bot.do_not_sell:
            if not bot["mission"]:
              if bot.gender=="female":                                    ##  ADDED IN VERSION 0.1.0 TO AVOID MALE BOTS
                if bot.chassis.integrity>=robosechs_bot_integrity_minimum:
                  if bot.psychocore.stability>=robosechs_bot_stability_minimum:
                    if bot.bot_sex>="D":
                      bot_price=bot_price_function(bot,skill_mods=robosechs_bot_price_skills,base_price_mult=0.1,part_price_mult=0.25)
                         
 ## 0.12.n add reputation to cap price value
                      price_cap_increase=price_rep_robosechs()
                      revised_price_cap=robosechs_bot_price_cap+price_cap_increase
                      bot_price=min(revised_price_cap,bot_price)

                      if bot_price>0:
                        bots.append([bot,bot_price])
    bots=bots[:12]
  if bots:
    "You show information and scans of your bots that fit their requirements."
    ""
    $bot_n=0
    while bots:
      $bot,bot_price=bots.pop(0)
      $bot_n+=1
      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}, price: [money_str[bot_price]]."
      choice("robosechs_sell_bot_do:{}".format(bot.id),cost=[("money",-bot_price)]) "Sell #[bot_n]"
    choice("<<<",pos=17,key="cancel") "Back"
  else:
    "{mcsay}Female bots with sexual and social skills, good chassis integrity, and stable. Got it, will keep in mind.{/}"
    choice("<<<") "Continue"
  $bot=None
  return

label robosechs_sell_bot_do(bot):
  header "[robosechs] - Selling bot"
  $bot=find_character(bot)
  "You sell {mark}[bot]{/}."
## 0.12.n add reputations
  if bot.rate=="D":                                      ## dealer rep based upon bot's rate
    $temp=calc_pr_rep_gain("rep_mc_dealer","xs_g")       ## extra small gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif bot.rate=="C":
    $temp=calc_pr_rep_gain("rep_mc_dealer","s_g")        ## small gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif bot.rate=="B":
    $temp=calc_pr_rep_gain("rep_mc_dealer","m_g")        ## medium gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif bot.rate=="A":
    $temp=calc_pr_rep_gain("rep_mc_dealer","l_g")        ## large gain
    $mc.give_xp("rep_mc_dealer",temp)
  elif bot.rate=="S":
    $temp=calc_pr_rep_gain("rep_mc_dealer","xl_g")       ## extra large gain
    $mc.give_xp("rep_mc_dealer",temp)
  if bot.bot_sex=="D":                                   ## sex trainer rep based upon bot's sex skill
    $temp=calc_pr_rep_gain("rep_mc_sexmachine","xs_g")   ## extra small gain
    $mc.give_xp("rep_mc_sexmachine",temp)
  elif bot.bot_sex=="C":   
    $temp=calc_pr_rep_gain("rep_mc_sexmachine","s_g")    ## small gain
    $mc.give_xp("rep_mc_sexmachine",temp)
  elif bot.bot_sex=="B": 
    $temp=calc_pr_rep_gain("rep_mc_sexmachine","m_g")    ## medium gain
    $mc.give_xp("rep_mc_sexmachine",temp)
  elif bot.bot_sex=="A": 
    $temp=calc_pr_rep_gain("rep_mc_sexmachine","l_g")    ## large gain
    $mc.give_xp("rep_mc_sexmachine",temp)
  elif bot.bot_sex=="S":
    $temp=calc_pr_rep_gain("rep_mc_sexmachine","xl_g")   ## extra large gain
    $mc.give_xp("rep_mc_sexmachine",temp)
  $move_sexbot(bot,None)
  $bot=None
  choice("<<<") "Continue"
  return
