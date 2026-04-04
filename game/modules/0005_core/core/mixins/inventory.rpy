init -700 python:
  class InventoryMixin(object):
    default_outfit_slots=[]
    notify_inventory_changed=False
    def __init__(self,*args,**kwargs):
      super(InventoryMixin,self).__init__()
      self.outfit_slots=self.default_outfit_slots[:]
      self.inventory=[]
      self.outfit={}
    def item_on_slot(self,slot):
      slot=find_item_slot(slot)
      if slot:
        return self.outfit.get(slot.id)
    def equipped(self,item):
      for slot,equipped_item in sorted(self.outfit.items()):
        if equipped_item is item:
          return equipped_item
    def has_item(self,item,count_equipped=True):
      for owned_item in self.inventory:
        if owned_item is item:
          return owned_item
      if count_equipped:
        return self.equipped(item)
    def add_item(self,item,silent=False,**kwargs):
      notify.disable("inventory_changed",silent)
      if isinstance(item,str):
        item=find_item_cls(item)(**kwargs)
      self.inventory.append(item)
      process_event("inventory_item_added",self,item)
      notify.enable("inventory_changed",silent)
      return item
    def remove_item(self,item,unequip=True,silent=False):
      notify.disable("inventory_changed",silent)
      if unequip and self.equipped(item):
        self.unequip(item,silent=silent)
      for item_n,owned_item in enumerate(self.inventory):
        if owned_item is item:
          self.inventory.pop(item_n)
          process_event("inventory_item_removed",self,item)
          break
      notify.enable("inventory_changed",silent)
      return item
    def can_equip_item(self,item):
      if self.has_item(item,False):
        slot=item.slot
        if slot and slot.id in self.outfit_slots:
          if not self.equipped(item):
            return slot.id
      return False
    def can_unequip_item(self,item):
      return self.equipped(item)
    def equip(self,item,silent=False,**kwargs):
      notify.disable("outfit_changed",silent)
      if isinstance(item,str):
        item=find_item_cls(item)(**kwargs)
        slot=item.slot
        if slot and slot.id in self.outfit_slots:
          self.add_item(item,silent=silent)
      if self.has_item(item,False):
        slot=item.slot
        if slot and slot.id in self.outfit_slots:
          equipped_item=self.item_on_slot(slot)
          if equipped_item is not item:
            if equipped_item:
              self.unequip(equipped_item,silent=silent)
            self.inventory.remove(item)
            self.outfit[slot.id]=item
            process_event("outfit_item_equipped",self,item)
      notify.enable("outfit_changed",silent)
    def unequip(self,item_or_slot,silent=False):
      notify.disable("outfit_changed",silent)
      if isinstance(item_or_slot,(str,ItemSlot)):
        item=self.item_on_slot(item_or_slot)
      else:
        item=item_or_slot
      if self.can_unequip_item(item):
        slot=item.slot
        if slot and slot.id in self.outfit_slots:
          self.outfit[slot.id]=None
          self.inventory.append(item)
          process_event("outfit_item_unequipped",self,item)
      notify.enable("outfit_changed",silent)
    def on_calc_effective_stat(self,stat,level):
      for slot,item in sorted(self.outfit.items()):
        handler=getattr(item,"on_calc_effective_stat",None)
        if callable(handler):
          level=handler(self,item,stat,level)
      return level
    def on_calc_effective_xp(self,stat,xp):
      for slot,item in sorted(self.outfit.items()):
        handler=getattr(item,"on_calc_effective_xp",None)
        if callable(handler):
          xp=handler(self,item,stat,xp)
      return xp
