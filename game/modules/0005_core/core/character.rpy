default all_characters={}

init -100 python:
  characters_cls_by_id={}

  def find_character(char):
    if isinstance(char,str):
      char=all_characters.get(char)
    return char if isinstance(char,Char) else None

  def find_character_cls(char_id):
    return characters_cls_by_id.get(char_id)

  def create_character(char_id,*args,**kwargs):
    cls=find_character_cls(char_id)
    return cls(*args,**kwargs) if cls else None

  class CharMeta(type):
    def __init__(cls,name,bases,dct):
      if "id" not in dct:
        cls.id=name[5:] if name.lower().startswith("char_") else name
      set_default_property(cls,"name")
      set_gameobject_property(cls,"location","location")
      if not dct.get("do_not_register",False):
        characters_cls_by_id[cls.id]=cls
    def __call__(cls,*args,**kwargs):
      rv=super(CharMeta,cls).__call__(*args,**kwargs)
      rv.init(*args,**kwargs)
      return rv

  class Char(PronounsMixin,MoneyMixin,InventoryMixin,StatsMixin,FlagsMixin,EventProcessorMixin,GameObject,metaclass=CharMeta):
    object_type="char"
    do_not_register=True
    id=None
    name=None
    location=None
    def __init__(self,*args,**kwargs):
      self.id=kwargs.pop("id",self.id)
      super(Char,self).__init__(*args,**kwargs)
      all_characters[self.id]=self
      self.activity=None
    def init(self,*args,**kwargs):
      pass
    def remove(self):
      if all_characters.get(self.id) is self:
        all_characters.pop(self.id)
      if getattr(store,self.id,None) is self:
        delattr(store,self.id)
    def __str__(self):
      return str(self.name)
    def set_location(self,location):
      location=find_location(location)
      old_location=self.location
      if location!=old_location:
        self._location=getattr(location,"id",None)
        if self==game.pc:
          process_event("location_changed",old_location,location)
          process_event("update_state")
    def at(self,location,activity=None):
      location=find_location(location)
      if location==self._location:
        if not activity or activity==self.activity:
          return True
      return False
    def ai(self):
      self.location=None
      self.activity=None
    def effective_stat(self,stat):
      level=stat.level
      if level is not None:
        level=self.process_event("calc_effective_stat:1",stat,level)
      return level
    def effective_xp(self,stat,xp):
      xp=int(round(self.process_event("calc_effective_xp:1",stat,xp)))
      return xp
