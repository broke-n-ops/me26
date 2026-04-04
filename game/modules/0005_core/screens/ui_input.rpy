init python:
  class UIInputValue(InputValue):
    def __init__(self,variable,rv_template=None,validator=None):
      super(UIInputValue,self).__init__()
      self.variable=variable
      self.rv_template=rv_template
      self.validator=validator
    def enter(self):
      if self.validator:
        if eval(self.validator.format(self.get_text().replace('"','\\"'))):
          return
      if isinstance(self.rv_template,str):
        if "{}" in self.rv_template:
          return self.rv_template.format(self.get_text())
        else:
          return self.rv_template
    def get_text(self):
      obj,sep,var=self.variable.rpartition(".")
      return getattr(eval(obj or "store"),var,"")
    def set_text(self,s):
      obj,sep,var=self.variable.rpartition(".")
      setattr(eval(obj or "store"),var,s)
      renpy.restart_interaction()
    def get_hint(self):
      if self.validator:
        return eval(self.validator.format(self.get_text().replace('"','\\"')))
      else:
        return ""

image ui_input_caret:
  xsize 2
  "#FFF"
  block:
    linear 0.1 alpha 0.0
    0.35
    linear 0.1 alpha 1.0
    0.35
    repeat

style ui_input_frame:
  background Frame("ui input frame",8,8)
  padding (16,8)

style ui_input_input is default:
  caret "ui_input_caret"

style ui_input_hint:
  size 18
  xalign 0.5
  yoffset -8

screen ui_input(variable,rv_template=None,validator=None,width=400,xalign=0,xoffset=0,allowed_chars=None):
  style_prefix "ui_input"
  default val=UIInputValue(variable,rv_template,validator)
  fixed:
    fit_first True
    xalign xalign
    xoffset xoffset
    frame:
      xsize width
      input:
        xfill True
        pixel_width width-16*2
        if allowed_chars:
          allow allowed_chars
        value val
    text val.get_hint() style "ui_input_hint"
