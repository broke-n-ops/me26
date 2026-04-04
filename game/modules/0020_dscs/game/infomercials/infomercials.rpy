screen infomercial_rg_vs_mt():
  style_prefix "infomercial"
  vbox:
    text "RheinGerate models are fine but for a little more money you can do much better with the Mitsutachi luxury line.\n\nIf money is no object then Elite Robotics is the place to go!"

screen infomercial_patreon():
  style_prefix "infomercial"
  vbox:
    text "Like game?"
    text ""
    text "Let us know on Discord!"

screen infomercial_hover_to_pause():
  style_prefix "infomercial"
  vbox:
    text "Hints&tips here changing too fast?"
    text ""
    text "Hover mouse over this area to pause slider."

screen infomercial_mouse_keys():
  style_prefix "infomercial"
  vbox:
    text "Some key shortcuts also have mouse variants"
    text ""
    use info_row("{mark}esc{/}","{mark}right button{/}")
    use info_row("{mark}home{/}","{mark}middle button\nclicking wheel{/}")

screen infomercial_keys():
  style_prefix "infomercial"
  vbox:
    text "Some rarely used key shortcuts"
    text ""
    use info_row("{mark}ctrl+pageup{/}","rollback")
    use info_row("{mark}ctrl+s{/}","take screenshot")
    use info_row("{mark}alt+enter\nF11{/}","display mode")
    use info_row("{mark}ctrl+h{/}","hide interface\nshow background")
    use info_row("{mark}ctrl+g{/}","renderer settings")

screen infomercial_click_image_to_max():
  style_prefix "infomercial"
  vbox:
    text "You can view full size image or movie if you click on it"
    text ""
    text "Click anywhere again or press {mark}esc{/} to get back to game"
