default persistent.ui_frame_alpha=80

define ui_frame_alpha_min=30
define ui_frame_alpha_max=90

#define ui_frame_background="#000808BB"
define ui_frame_background="#000808"
define ui_frame_border_color="#000"

screen ui_frame(xfill=True,ysize=None,bg=ui_frame_background,scroll=False):
  fixed:
    fit_first True
    frame:
      background Transform(bg,alpha=min(1.0,max(0.0,persistent.ui_frame_alpha/100.0)))
      if xfill:
        xfill xfill
      if ysize is True:
        yfill True
      elif ysize:
        ysize ysize
      padding ((4,4) if scroll else (8,4))
      transclude
    fixed:
      ysize 4
      add ui_frame_border_color
    fixed:
      ysize 4
      yalign 1.0
      add ui_frame_border_color

screen frame_border(border="#000"):
  side "t c b":
    fixed:
      ysize 4
      add border
    side "l c r":
      fixed:
        xsize 4
        add border
      fixed:
        fit_first True
        transclude
      fixed:
        xsize 4
        add border
    fixed:
      ysize 4
      add border
