init python:
  class FitTextDisplayable(renpy.Displayable):
    def __init__(self,content,prefix,content_style="ui_text",wh=None,**kwargs):
      super(FitTextDisplayable,self).__init__(**kwargs)
      self.content=content
      self.prefix=prefix
      self.content_style=content_style
      self.size=0
      content_style=getattr(style,content_style)
      self.wh=wh if wh else (content_style.xmaximum,content_style.ymaximum)
    def render(self,width,height,st,at):
      w,h=self.wh
      for self.size in range(self.size,48):
        rv=Text("{size=-"+str(self.size)+"}"+self.content+"{/size}",style=self.content_style)
        rv.set_style_prefix(self.prefix+"_",False)
        rv=rv.render(w,h,st,at)
        if rv.width<=w and rv.height<=h:
          break
      return rv
