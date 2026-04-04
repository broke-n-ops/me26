define default_bot_price_skill_mods={
  "bot_combat":      (1.0,"mul_exp3",0.0,3.5),
  "bot_electronics": (1.0,"mul_exp3",0.0,3.0),
  "bot_mechanics":   (1.0,"mul_exp3",0.0,3.0),
  "bot_sex":         (1.0,"mul_exp3",0.0,3.0),
  "bot_social":      (1.0,"mul_exp3",0.0,3.0),
  }

define bot_price_skills_unimportant={
  "bot_combat":      (1.0,"mul_exp3",0.0,1.0),
  "bot_electronics": (1.0,"mul_exp3",0.0,1.0),
  "bot_mechanics":   (1.0,"mul_exp3",0.0,1.0),
  "bot_sex":         (1.0,"mul_exp3",0.0,1.0),
  "bot_social":      (1.0,"mul_exp3",0.0,1.0),
  }

define bot_price_ignore_skills={
  }

init python:
  def bot_price_function(bot,**kwargs):
    """
    base_price_mult: float, default 1.0
    skill_mods: dict of skill: (skill_mod,mod_type,min_level_mod,max_level_mod)
    part_price_mult: float, default 1.0
    part_low_bound: int, default 25
    chassis_integrity_mult: float, default 0.5
    """

##    print("bot price",bot)

## start with base model price
    base_price_mult=kwargs.get("base_price_mult",1.0)
    price=int(round(bot.base_price*base_price_mult))

##    print("  base price",price)

## apply skill level mods, if any
    skill_mods=kwargs.get("skill_mods",default_bot_price_skill_mods)
    for skill_id,(skill_mod,mod_type,min_level_mod,max_level_mod) in sorted(skill_mods.items()):
      max_level=getattr(bot,skill_id).max_level
      min_level=getattr(bot,skill_id).min_level
      level=getattr(bot,skill_id).level
      price_mod=(max_level_mod-min_level_mod)*(level-min_level)/float(max_level-min_level)+min_level_mod
      neg_price_mod=price_mod<0
      price_mod=abs(price_mod)
      if mod_type=="add":
        price_mod=price_mod*skill_mod
      elif mod_type=="add_exp2":
        price_mod=price_mod**2*skill_mod
      elif mod_type=="add_exp3":
        price_mod=price_mod**3*skill_mod
      elif mod_type in ("mul","mult"):
        price_mod=1.0+(price_mod-1.0)*skill_mod
      elif mod_type in ("mul_exp2","mult_exp2"):
        price_mod=1.0+(price_mod**2-1.0)*skill_mod
      elif mod_type in ("mul_exp3","mult_exp3"):
        price_mod=1.0+(price_mod**3-1.0)*skill_mod
      if neg_price_mod:
        price_mod=-price_mod
      if mod_type in ("add","add_exp2","add_exp3"):

##        print("  skill",skill_id,level,"+",int(round(price_mod)))

        price=int(round(price+price_mod))
      elif mod_type in ("mul","mult","mul_exp2","mult_exp2","mul_exp3","mult_exp3"):

##        print("  skill",skill_id,level,getattr(bot,skill_id).level_name,"*",price_mod)

        price+=int(round(bot.base_price*price_mod))
## apply chassis parts mods
    part_price_mult=kwargs.get("part_price_mult",1.0)
    part_low_bound=kwargs.get("part_low_bound",25)
    for slot in bot.outfit_slots:
      part=bot.item_on_slot(slot)
      if part and part.integrity>=part_low_bound:
        price_mod=part.base_price*(1.0+(part.integrity/100.0-1.0)*part_price_mult)
        for defect in part.defects:
          price_mod*=defect.part_price_mult
        price=int(round(price+price_mod))

##        print("  part",part,"+",int(round(price_mod)))

## apply chassis integrity mod
    chassis_integrity_mult=kwargs.get("chassis_integrity_mult",0.5)
    price_mod=1.0+(bot.chassis.integrity/100.0-1.0)*chassis_integrity_mult

##    print("  chassis mult *",price_mod)

    price=int(round(price*price_mod))
## was TBD in DSCS
## apply psychocore traits mods - add 4% per trait to the price regardless of the type of trait or if it's inherent
    traits=[trait for trait in bot.psychocore.traits if not trait.hidden]
    if traits:
      for trait in traits:
        if trait.trait_type=="good":
          price=price*1.025
        elif trait.trait_type=="bad":
          price = price*0.975
## was TBD in DSCS
## apply psychocore stability mod - subtract from 0$ to 20% from price" - multiplier values are 100% = 1.00, 0%=0.80, linear interpolation between
    price_mod=bot.psychocore.stability*0.002+0.8
    price=int(round(price*price_mod))

##    print("  final price",price)

    return price

  def bot_part_price_function(part,flat_price_below=0):
    integrity=max(flat_price_below,part.integrity)
    price=part.base_price*(integrity/100.0)**2
    for defect in part.defects:
      price*=defect.part_price_mult
    return price
