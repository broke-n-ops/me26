init -700 python:
  class MoneyStr(object):
    def __call__(self,money):
      no_color_tags=isinstance(money,str) and money.startswith("=")
      if no_color_tags:
        money=money[1:]
      try:
        money=int(money)
      except:
        money=eval(money)
      neg=money<0
      money=abs(money)
      parts=[]
      while money:
        money,part=divmod(money,1000)
        parts.insert(0,"{:03d}".format(part) if money else str(part))
      if not parts:
        parts=["0"]
      parts=",".join(parts)
      if no_color_tags:
##        return ("-" if neg else "")+parts+"{size=-8}${/}"
##        return ("-" if neg else "")+"{size=-8}${/}"+parts
        return ("-" if neg else "")+"$"+parts                                 ## 0.11.3 put $ at beginning and do NOT reduce size
      else:
##        return ("{bad}-" if neg else "{mark}")+parts+"{size=-8}${/}{/}"
##        return ("{bad}-" if neg else "{mark}")+"{size=-8}${/}"+parts+"{/}"
        return ("{bad}-" if neg else "{mark}")+"$"+parts+"{/}"               ## 0.11.3 put $ at beginning and do NOT reduce size
    def __getitem__(self,money):
      return self(money)
  money_str=MoneyStr()

  class MoneyMixin(object):
    notify_money_changed=False
    def __init__(self,*args,**kwargs):
      super(MoneyMixin,self).__init__()
      self._money=0
    @property
    def money(self):
      return self._money
    @money.setter
    def money(self,money):
      silent=False
      if isinstance(money,(list,tuple)):
        money,silent=money
      notify.disable("money_changed",silent)
      if money!=self._money:
        old_money=self._money
        self._money=money
        if old_money!=money:
          process_event("money_changed",self,old_money,money)
      notify.enable("money_changed",silent)
    @property
    def money_str(self):
      return money_str(self.money)
    def add_money(self,money,silent=False):
      self.money=(self.money+money,silent)
    def remove_money(self,money,silent=False):
      self.money=(self.money-money,silent)
