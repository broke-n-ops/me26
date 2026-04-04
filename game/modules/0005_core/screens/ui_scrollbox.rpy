default saved_scroll_positions={}

init python hide:
  @event_handler("after_load")
  def reset_scroll_positions():
    saved_scroll_positions.clear()

init python:
  class UIScrollPos(object):
    def __init__(self,id):
      super(UIScrollPos,self).__init__()
      self.id=id
    def __call__(self,value):
      saved_scroll_positions[self.id]=int(value)
      pygame.mouse.set_pos(pygame.mouse.get_pos())
      renpy.restart_interaction()

screen ui_scrollbox(add_left_padding=True,id=None,update=False,main_viewport=False):

##  $print "id: ",id

  $temp=saved_scroll_positions.get(id,0)

##  $print "saved_scroll_position.get(id,0): ",temp
##  $print "sr24_capsule_flag: ",sr24_capsule_flag
##  $print "BEFORE - update: ",update

  if id=="interaction_default_content" and sr24_capsule_flag:  ## BOTH interaction flag set and it's the main viewport
    $update=True                                               ## while on capsule screen save scroll location

##  $print "AFTER - update: ",update

  viewport:
    xfill True
    mousewheel True
    if main_viewport:
      pagekeys True
    if renpy.android:
      draggable True
    scrollbars "vertical"
    if id:
      yadjustment ui.adjustment(changed=UIScrollPos(id))
      yinitial (saved_scroll_positions.get(id,0) if update else 0)
    frame:
      background None
      left_padding 4+(20 if add_left_padding else 0)
      right_padding 4
      vbox:
        xfill True
        clipping True
        null height 0
        transclude
