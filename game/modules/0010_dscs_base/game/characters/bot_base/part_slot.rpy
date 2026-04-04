init -99 python:
  class BotPartSlot(ItemSlot):
    do_not_register=True

  modded_bot_part_slot_classes={}

  def load_bot_part_slots_from_mods():
    slots_info=load_info_table_from_mods("bot_part_slots")
    for slot_id,slot in sorted(slots_info.items()):
      if slot:
        slot_cls_dct=slot.copy()
        slot_cls_name="BotPartSlot_"+slot_id
        slot_cls=type(slot_cls_name,(BotPartSlot,),slot_cls_dct)
        setattr(store,slot_cls_name,slot_cls)
        modded_bot_part_slot_classes[slot_id]=slot_cls
        if log_modded_entries():
          print("Loaded modded bot part slot:",slot_id)

  load_bot_part_slots_from_mods()
