default persistent.play_maximized_movie_audio=False
## 0.9.2 addition suggested by 'MikasaTanikawa' to create setting for increasing size of images or leave as is - 1 of 2
default persistent.maximize_to_fullscreen=False

screen view_image_at_max(img):
  modal True
  $img=img.partition("@")[0]
  $xysize=(int(config.screen_width*1.0),int(config.screen_height*1.0))
  if persistent.play_maximized_movie_audio:
    if renpy.has_image(img+"#fullscreen"):
      $img=img+"#fullscreen"
  button:
    add "#000C"

## 0.9.2 change suggested by 'MikasaTanikawa' to increase size of small images based upon setting - change 2 of 2
    if persistent.maximize_to_fullscreen:
        add Transform(img,xysize=xysize,fit="contain") align (0.5,0.5)
    else:
        add Transform(img,xysize=xysize,fit="scale-down") align (0.5,0.5)
## end of change
    action Hide("view_image_at_max")
  key "cancel" action Hide("view_image_at_max")
  key "dismiss" action Hide("view_image_at_max")

init python:
  class MaxableImage(renpy.Displayable):
    def __init__(self,img,img_src,**kwargs):
      super(MaxableImage,self).__init__(**kwargs)
      self.img=renpy.displayable(img)
      self.img_src=img_src
      self.wh=(0,0)
      self.needRedraw = 1
    def render(self,width,height,st,at):
      img_render=renpy.render(self.img,width,height,st,at)
      self.wh=img_render.get_size()
      render=renpy.Render(*self.wh)
      render.blit(img_render,(0,0))
      if self.needRedraw != 0:
        renpy.redraw(self,0)
        self.needRedraw = 0
      return render
    def event(self,ev,x,y,st):
      if renpy.map_event(ev,"mouseup_1"):
        if 0<=x<self.wh[0] and 0<=y<self.wh[1]:
          Show("view_image_at_max",None,self.img_src)()
      return self.img.event(ev,x,y,st)
    def visit(self):
      return [self.img]
    def per_interact(self):
      self.needRedraw = 1
      renpy.redraw(self,0)

init python:
  def find_game_image_variant(image):
    if "[" in image:
      image=preprocess_text(image)
    image=check_asset_packs(image)
    if ":" in image:
      parts=image.split()
      root=parts[0]
      attr=tuple(parts[1:-1])
      wanted_len=len(attr)
      start=parts[-1][1:]
      variants=[]
      for img in renpy.display.image.image_attributes[root]:
        if len(img)>wanted_len:
          if img[:wanted_len]==attr:
            if img[wanted_len].startswith(start) and not img[-1].endswith("_preview"):
              variants.append(root+" "+" ".join(img))
      if variants:
        return randchoice(variants)
    else:
      return image

  def patched_lookup_displayable_prefix(d):
    if isinstance(d,str):
      if not d.startswith("#"):
        d=check_asset_packs(d)
        img_src=d
        if "@" in d:
          d,sep,size=d.partition("@")
          if "x" in size:
            size=[eval(v) for v in size.split("x")]
          else:
            size=eval(size)
            if not isinstance(size,(list,tuple)):
              size=(size,None)
        else:
          size=None
        if ":" in d:
          d=find_game_image_variant(d)
        if size:
          return MaxableImage(Transform(d,xysize=size,fit="scale-down"),img_src)
    return renpy.easy.lookup_displayable_prefix.original(d)

  if not hasattr(renpy.easy.lookup_displayable_prefix,"original"):
    patched_lookup_displayable_prefix.original=renpy.easy.lookup_displayable_prefix
    renpy.easy.lookup_displayable_prefix=patched_lookup_displayable_prefix
