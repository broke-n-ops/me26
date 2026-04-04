style status_side_mc_desc is cs_center:
  layout "subtitle"

screen status_side_mc(act_data):
  $char=find_character(act_data.get("char","mc"))
  if char:
    use ui_frame:
      fixed:
        $desc=getattr(char,"origin","{color=#888}No info available{/}")
        add FitTextDisplayable(desc,"idle","status_side_mc_desc",(340,900)) align (0.5,0.5)
