##init -999 python:
  ## tooltip hack
  ## don't show tooltip if button is selected
##  def patched_button_get_tooltip(self):
##    if self.is_selected():
##      return None
##    return self._get_tooltip.original(self)

##  if not hasattr(Button._get_tooltip,"original"):
##    patched_button_get_tooltip.original=Button._get_tooltip
##    Button._get_tooltip=patched_button_get_tooltip
