transform tf_ending_bad:
  matrixcolor TintMatrix("#FFF")
  0.5
  linear 2.0 matrixcolor TintMatrix("#F00")

transform tf_ending_good:
  matrixcolor TintMatrix("#FFF")
  0.5
  linear 2.0 matrixcolor TintMatrix("#4CF")

screen interaction_ending(act_data):
  $ending_type=act_data.get("ending_type","bad")
  button:
    xfill True
    yfill True
    text "The End" align (0.5,0.5) size 128 at getattr(store,"tf_ending_"+ending_type)
    action Return()
  key "dismiss" action Return()
  key "cancel" action Return()
