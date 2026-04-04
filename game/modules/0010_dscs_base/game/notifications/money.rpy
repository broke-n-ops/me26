init python hide:
  notification_categories["money"]=("Money","normal")

  @event_handler("money_changed")
  def money_changed(char,old_money,money):
    if char and char.notify_money_changed:
      delta=money-old_money
      if delta<0:
        msg="{bad}Lost{/} "+money_str(-delta)+"."
      else:
        msg="Gained "+money_str(delta)+"."
      game_notification(msg,"money","money_changed")
