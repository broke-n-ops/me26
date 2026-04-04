style status_side_sexbot_desc is cs_center:
  layout "subtitle"

screen status_side_sexbot(act_data):
  $char=find_character(act_data["char"])
  if char:
    use ui_frame:
      fixed:
        vbox:
          xfill True
          align (0.5,0.5)
          add FitTextDisplayable("{size=-8}"+char.model_name+"{/}","idle","cs_header",side_text_size) xalign 0.5
          use vdiv
          $desc=getattr(char,"model_description",None)
          $desc=desc or "{color=#888}No model info available{/}"
          add FitTextDisplayable(desc,"idle","status_side_sexbot_desc",(340,800)) xalign 0.5
