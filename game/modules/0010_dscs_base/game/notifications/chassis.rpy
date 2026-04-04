init python hide:
  notification_categories["bot_parts"]=("Bot Parts","small")

  @event_handler("chassis_part_integrity_changed")
  def bot_chassis_part_integrity_changed(char,part,change):
    if char is None or char.notify_chassis_part_integrity_changed:
      if part.notify_chassis_part_integrity_changed:
        slot=find_item_slot(part.slot)
        if change<0:
          msg="%s chassis %s integrity reduced by %s%%"%(char,slot.name.lower(),-change)
        else:
          msg="%s chassis %s integrity impoved by %s%%"%(char,slot.name.lower(),change)
        game_notification(msg,"bot_parts","chassis_part_integrity_changed")

  @event_handler("chassis_part_defect_added")
  def bot_chassis_part_defect_added(char,part,defect):
    if char is None or char.notify_chassis_part_defect_added:
      if part.notify_chassis_part_defect_added:
        slot=find_item_slot(part.slot)
        msg="%s chassis %s got new defect: {bad}%s{/}"%(char,slot.name.lower(),defect.name.lower())
        game_notification(msg,"bot_parts","chassis_part_defect_added")
