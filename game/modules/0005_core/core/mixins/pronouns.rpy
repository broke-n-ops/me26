init -700 python:
  class Pronouncer(object):
    def __init__(self,*args,**kwargs):
      super(Pronouncer,self).__init__()
      self.owner=kwargs.get("owner")
    @property
    def owner(self):
      return find_character(self._owner)
    @owner.setter
    def owner(self,owner):
      owner=find_character(owner)
      self._owner=getattr(find_character(owner),"id",None)
    def __call__(self,kind="he"):
      char=self.owner
      gender=char.gender
      if kind in ("he","she","heshe"):
        rv="he" if gender=="male" else "she"
      elif kind in ("his","her","hisher"):
        rv="his" if gender=="male" else "her"
      elif kind in ("him","himher"):
        rv="him" if gender=="male" else "her"
      elif kind in ("hishers","hers",):
        rv="his" if gender=="male" else "hers"
      elif kind in ("name","name's","posname"):
        rv=char.name+"'" if char.name.lower().endswith("s") else char.name+"'s"
      elif kind in ("mr","mrs"):
        rv="Mr." if gender=="male" else "Mrs."
      else:
        rv=kind
#      rv="{color=#F0F}"+rv+"{/}"
      return rv
    def __getitem__(self,key):
      return self(key)

  class PronounsMixin(object):
    gender="male"
    def __init__(self,*args,**kwargs):
      super(PronounsMixin,self).__init__()
      self.pronoun=Pronouncer(owner=self)
    @property
    def heshe(self):
      return self.pronoun("heshe")
    @property
    def hisher(self):
      return self.pronoun("hisher")
    @property
    def himher(self):
      return self.pronoun("himher")
    @property
    def he(self):
      return self.pronoun("he")
    @property
    def she(self):
      return self.pronoun("she")
    @property
    def his(self):
      return self.pronoun("his")
    @property
    def her(self):
      return self.pronoun("her")
    @property
    def him(self):
      return self.pronoun("him")
    @property
    def posname(self):
      return self.pronoun("name's")
