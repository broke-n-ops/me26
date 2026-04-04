init -50 python:
  class GreyMarketOffer(object):
    id=None
    category="trade"
    title="- offer title -"
    appear_condition=True
    chance=100
    duration=1
    allow_duplicates=False
    request=[]
    reward=[]
    cooldown=0
    def __init__(self):
      super(GreyMarketOffer,self).__init__()
      if isinstance(self.title,(list,tuple)):
        self.title=randchoice(self.title)
      if isinstance(self.duration,(list,tuple)):
        self.duration=randint(self.duration[0],self.duration[1])
      if isinstance(self.cooldown,(list,tuple)):
        self.cooldown=randint(self.cooldown[0],self.cooldown[1])
      if self.reward:
        if not isinstance(self.reward,(list,tuple)):
          self.reward=[self.reward]
        rewards=[]
        for reward_info in self.reward:
          if isinstance(reward_info,(list,tuple)):
            reward_info=randchoice(reward_info)
          if reward_info["type"]=="part":
            reward=reward_info["id"]
            if isinstance(reward,(list,tuple)):
              reward=randchoice(reward)
            reward=find_item_cls("bot_part_"+reward)()
            if reward_info.get("damage"):
              damage=reward_info["damage"]
              if isinstance(damage,(list,tuple)):
                damage=randint(damage[0],damage[1])
              minimal_integrity=reward_info.get("minimal_integrity",1)
              reward.apply_damage(damage,minimal_integrity,True)
            if reward_info.get("hidden"):
              reward.hidden_reward=True
            rewards.append(reward)
          else:
            rewards.append(reward_info)
        self.reward=rewards
    @property
    def request_description(self):
      rv=[]
      request=self.request
      if isinstance(request,dict):
        if request["type"]=="part":
          if "id" in request:
            rv.append("part: {mark}"+find_item_cls(request["id"]).name+"{/}")
          elif "slot" in request:
            rv.append("part category: {mark}"+find_item_slot("bot_"+request["slot"]).name+"{/}")
          if "rate" in request:
            rv.append("part rate: {mark}"+request["rate"][0]+"+{/}")
          if "minimal_integrity" in request:
            rv.append("minimal integrity: {mark}"+str(request["minimal_integrity"])+"%{/}")
          if "defects_allowed" in request:
            if request["defects_allowed"]:
              rv.append("can have defects: {mark}yes{/}")
        elif request["type"]=="bot":
          if "gender" in request:
            rv.append("bot model gender: {mark}"+request["gender"]+"{/}")
          if "rate" in request:
            rv.append("bot model rate: {mark}"+request["rate"][0]+"+{/}")
          if "skills" in request:
            for skill_id,skill_rate in sorted(request["skills"].items()):
              skill=find_stat("bot_"+skill_id)
              rv.append("{mark}"+skill.name+"{/} skill: {mark}"+skill_rate[0]+"+{/}")
          if "minimal_integrity" in request:
            rv.append("minimal integrity: {mark}"+str(request["minimal_integrity"])+"%{/}")
          if "stable_psychocore" in request:
            if request["stable_psychocore"]=="yes":
              rv.append("minimal stability: {mark}stable{/}")
          if "defects_allowed" in request:
            if request["defects_allowed"]:
              rv.append("can have defects: {mark}yes{/}")
        elif request["type"]=="money":
          value=request["value"]
          if isinstance(value,str):
            value=eval(value,{"reward_price":self.reward_price})
          rv.append(money_str(value))
      rv="\n".join((("- " if s else "")+s for s in rv))
      return rv
    @property
    def reward_description(self):
      rv=[]
      for reward in self.reward:
        if isinstance(reward,dict):
          if reward["type"]=="money":
            if rv:
              rv.append("")
            value=reward["value"]
            if isinstance(value,str):
              rv.append("{mark}money, varied{/}")
            else:
              rv.append(money_str(value))
        elif isinstance(reward,BotPart):
          if rv:
            rv.append("")
          rv.append("{mark}"+reward.name+"{/}")
          rv.append("rate: {mark}"+reward.rate+"{/}")
          rv.append("integrity: {mark}"+str(reward.integrity)+"%{/}")
          if reward.defects:
            rv.append("defects: "+", ".join("{bad}"+defect.name+"{/}" for defect in reward.defects))
      rv="\n".join((("- " if s else "")+s for s in rv))
      return rv
    def list_request_options(self,max_length=None):
      request=self.request
      rv=None
      if isinstance(request,dict):
        if request["type"]=="part":
          rv=[]
          perfect=[]                                           ## variable added in 0.9.0 for de-duplication of parts in lines 133 through 139
          for item_n,item in enumerate(workshop.inventory):
            if item.do_not_sell:
              continue
            if "id" in request:
              if item!=request["id"]:
                continue
            elif "slot" in request:
              if item.slot!="bot_"+request["slot"]:
                continue
            if "rate" in request:
              if item.rate not in request["rate"]:
                continue
            if "minimal_integrity" in request:
              if item.integrity<int(request["minimal_integrity"]):
                continue
            if not request.get("defects_allowed",False) and item.defects:
              continue
## 0.9.0 - 6 lines: 4 new, 2 copies of existing line: de-duplicate parts in perfect condition-damaged and/or defective parts still duplicated
            if not item.defects and item.integrity==100:  ## first added line: if item in perfect condition
              if not item.id in perfect:                  ## second added line: check if this perfect condition item has already been added
                rv.append(("part",item_n,item))           ## existing line, only indentation adjusted: add the perfect condition item since it's not a duplicate
                perfect.append(item.id)                   ## third added line: add perfect condition item to list to avoid duplication
            else:                                         ## added in 0.9.1 - fourth added line: handle items NOT in perfect condition
              rv.append(("part",item_n,item))             ## added 0.9.1 - duplicate of existing line: add imperfect items
        elif request["type"]=="bot":
          rv=[]
          for storage_id,storage in (("home",home.sexbots),("workshop",workshop.sexbots)):
            for bot_n,bot in enumerate(storage):
              if bot:
                if bot.do_not_sell:
                  continue
                if bot["mission"]:
                  continue
                if "gender" in request:
                  if bot.gender.lower()!=request["gender"].lower():
                    continue
                if "rate" in request:
                  if bot.rate not in request["rate"]:
                    continue
                if "skills" in request:
                  skill_reqs_met=True
                  for skill_id,skill_rate in sorted(request["skills"].items()):
                    skill_reqs_met=skill_reqs_met and getattr(bot,"bot_"+skill_id).level_name in skill_rate
                  if not skill_reqs_met:
                    continue
                if "minimal_integrity" in request:
                  if bot.chassis.integrity<int(request["minimal_integrity"]):
                    continue
                if "stable_psychocore" in request:
                  if request["stable_psychocore"]=="yes":
                    if bot.psychocore.stability<75:
                      continue
                if not request.get("defects_allowed",False) and bot.chassis.has_defects:
                  continue
                rv.append(("bot",bot.id,bot))
        elif request["type"]=="money":
          value=request["value"]
          if isinstance(value,str):
            value=eval(value,{"reward_price":self.reward_price})
          rv={"money":int(value)}
      else:
        rv=request
      if max_length and isinstance(rv,(list,tuple)):
        rv=rv[:max_length]
      return rv
    @property
    def reward_price(self):
      price=0
      if self.reward:
        for reward in self.reward:
          if isinstance(reward,Item):
            price+=int(bot_part_price_function(reward))
      return price

init -10 python:
  modded_grey_market_offers={}

  def load_grey_market_offers_from_mods():
    offers_info=load_info_table_from_mods("grey_market_offers")
    for offer_id,offer in sorted(offers_info.items()):
      if offer:
        offer_cls_dct=offer.copy()
        offer_cls_name="GreyMarketOffer_"+offer_id
        offer_cls=type(offer_cls_name,(GreyMarketOffer,),offer_cls_dct)
        setattr(store,offer_cls_name,offer_cls)
        modded_grey_market_offers[offer_id]=offer_cls
        if log_modded_entries():
          print("Loaded modded Grey Market offer:",offer_id)

  load_grey_market_offers_from_mods()

init python:
  def generate_grey_market_offer():
    current_offers={}
    for offer in grey_market.offers:
      current_offers[offer.id]=current_offers.get(offer.id,0)+1
    offers=[]
    for offer_id,offer in sorted(modded_grey_market_offers.items()):
      if offer_id in grey_market.offers_cooldowns:
        continue
      if callable(offer.appear_condition):
        if not offer.appear_condition():
          continue
      elif isinstance(offer.appear_condition,str):
        if not eval(offer.appear_condition):
          continue
      elif not offer.appear_condition:
        continue
      if offer.allow_duplicates is True:
        allowed=9001
      elif offer.allow_duplicates is False:
        allowed=1
      else:
        allowed=int(offer.allow_duplicates)
      if current_offers.get(offer_id,0)<allowed and offer.chance>0:
        offers.append((offer,offer.chance))
    if offers:
      offer=randwchoice(offers)
      if offer:
        return offer()
