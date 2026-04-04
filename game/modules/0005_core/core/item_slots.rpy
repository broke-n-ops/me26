init -600 python:
  item_slots_by_id={}

  def find_item_slot(item_slot):
    return item_slot if isinstance(item_slot,ItemSlotMeta) else item_slots_by_id.get(item_slot)

  class ItemSlotMeta(type):
    def __init__(cls,name,bases,dct):
      if "id" not in dct:
        cls.id=name[9:] if name.lower().startswith("itemslot_") else name
      if not dct.get("do_not_register",False):
        item_slots_by_id[cls.id]=cls
    def __eq__(cls,other):
      return cls is other or cls.id==other
    def __ne__(cls,other):
      return not cls.__eq__(other)
    def __str__(cls):
      return str(cls.name)
    def __call__(cls,*args,**kwargs):
      rv=super(ItemSlotMeta,cls).__call__(*args,**kwargs)
      rv.init(*args,**kwargs)
      return rv

  class ItemSlot(object,metaclass=ItemSlotMeta):
    do_not_register=True
    id=None
    name="-item slot-"
