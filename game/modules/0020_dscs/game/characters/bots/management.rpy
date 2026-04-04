init python:
  def move_sexbot(bot,target_storage):
    for storage in (home,workshop):
      if bot in storage.sexbots:
        if storage is not target_storage:
          storage.remove_sexbot(bot,not target_storage)
          if target_storage:
            target_storage.add_sexbot(bot)
        break
            