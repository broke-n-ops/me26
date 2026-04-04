default persistent.full_descriptions=False

init python:
  def hide_full_description():
    if persistent.full_descriptions:
      return False
    else:
      return True