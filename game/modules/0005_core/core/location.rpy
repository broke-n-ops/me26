default all_locations={}

init -500 python:
  locations_cls_by_id={}

  def find_location(location):
    if isinstance(location,str):
      location=all_locations.get(location)
    return location if isinstance(location,Location) else None

  def find_location_cls(location_id):
    return locations_cls_by_id.get(location_id)

  class LocationMeta(type):
    def __init__(cls,name,bases,dct):
      if "id" not in dct:
        cls.id=name[9:] if name.lower().startswith("location_") else name
      set_default_property(cls,"name")
      set_default_property(cls,"unlocked")
      if not dct.get("do_not_register",False):
        locations_cls_by_id[cls.id]=cls
    def __call__(cls,*args,**kwargs):
      rv=super(LocationMeta,cls).__call__(*args,**kwargs)
      rv.init(*args,**kwargs)
      return rv

  class Location(StatsMixin,InventoryMixin,FlagsMixin,EventProcessorMixin,GameObject,metaclass=LocationMeta):
    object_type="location"
    do_not_register=True
    id=None
    name="- location -"
    parent=None
    unlocked=True
    notify_unlocked=False
    def __init__(self,*args,**kwargs):
      self.id=kwargs.pop("id",self.id)
      super(Location,self).__init__(*args,**kwargs)
      all_locations[self.id]=self
    def init(self,*args,**kwargs):
      pass
    def remove(self):
      if all_locations.get(self.id) is self:
        all_locations.pop(self.id)
      if getattr(store,self.id,None) is self:
        delattr(store,self.id)
    def __str__(self):
      return str(self.name)
    def set_unlocked(self,unlocked):
      if not self._unlocked:
        self._unlocked=unlocked
        if unlocked:
          process_event("location_unlocked",self)
