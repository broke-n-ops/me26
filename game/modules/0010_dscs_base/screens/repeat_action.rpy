default persistent.show_repeat_action=True

init python:
  def show_repeat_action():
    if persistent.show_repeat_action=="always":
      return True
    elif persistent.show_repeat_action and not game.hardcore:
      return True
    else:
      return False
