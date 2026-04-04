init -500 python:
  items_cls_by_id={}

  def find_item(item):
    return item if isinstance(item,Item) else None

  def find_item_cls(item_id):
    return items_cls_by_id.get(item_id)

  class ItemMeta(type):
    def __init__(cls,name,bases,dct):
      if "id" not in dct:
        cls.id=name[5:] if name.lower().startswith("item_") else name
      if not dct.get("do_not_register",False):
        items_cls_by_id[cls.id]=cls
      set_default_property(cls,"name")
      set_default_property(cls,"description")
      set_gameobject_property(cls,"slot","item_slot")
    def __call__(cls,*args,**kwargs):
      if cls is Item:
        item_cls=find_item_cls(args[0])
        if isinstance(item_cls,ItemMeta):
          rv=item_cls(*args[1:],**kwargs)
        else:
          raise Exception("Item class not registered: {}".format(args[0]))
      else:
        rv=super(ItemMeta,cls).__call__(*args,**kwargs)
      rv.init()
      return rv
    def __str__(cls):
      return str(cls.name)

  class Item(FlagsMixin,GameObject,metaclass=ItemMeta):
    object_type="item"
    do_not_register=True
    id=None
    name="-item-"
    description="-item description-"
    category=None
    slot=None
    hidden=False
    notify_inventory_changed=True
    def __init__(self,*args,**kwargs):
      super(Item,self).__init__(*args,**kwargs)
    def init(self,*args,**kwargs):
      pass
    def __eq__(self,other):
      return self is other or self.id==other
    def __ne__(self,other):
      return not self.__eq__(other)
    def __str__(self):
      return str(self.name)
    def actions(self,char):
      return []
