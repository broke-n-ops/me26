define grey_market_max_offers=18
define grey_market_new_offers_per_time=(3,7)

init python:
  class Location_grey_market(Location):
    name="Grey Market BBS"
    def init(self,*args,**kwargs):
      self.offers=[]
      self.offers_cooldowns={}
    def fill_offers(self,count):
      while len(self.offers)<grey_market_max_offers and count>0:
        offer=generate_grey_market_offer()
        if not offer:
          break
        self.offers.append(offer)
        self.offers_cooldowns[offer.id]=max(self.offers_cooldowns.get(offer.id,0),offer.cooldown)
        count-=1
    def remove_offer(self,offer):
      if isinstance(offer,int):
        if offer<len(self.offers):
          self.offers.pop(offer)
      elif offer in self.offers:
        self.offers.remove(offer)
    def on_time_advanced(self):
      for offer in self.offers:
        offer.duration-=1
      self.offers=[offer for offer in self.offers if offer.duration>1]
      new_offers_count=randint(*grey_market_new_offers_per_time)
      cooldowns={}
      for offer_id,cooldown in self.offers_cooldowns.items():
        cooldown-=1
        if cooldown>0:
          cooldowns[offer_id]=cooldown
      self.offers_cooldowns=cooldowns
      self.fill_offers(new_offers_count)

init python hide:
  @event_handler("init_game")
  def set_initial_grey_market_offers():
    grey_market.fill_offers(grey_market_max_offers)
