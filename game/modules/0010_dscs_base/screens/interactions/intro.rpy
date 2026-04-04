default intro_info_pages=None
default intro_info_page=None

style intro_info_small_text:
  size 24

label set_intro_info_page(page):
  $intro_info_page=page
  return "<<<"

screen interaction_intro_side_info(act_data):
  python:
    pages=intro_info_pages or []
    if intro_info_page and intro_info_page in pages:
      current=intro_info_page
      current_n=pages.index(current)
    else:
      current=pages[0] if pages else None
      current_n=0
  side "c b":
    xfill True
    yfill True
    spacing 8
    use ui_scrollbox(id="intro_side_info",update=True):
      if current:
        $renpy.use_screen("interaction_intro_info_"+current,act_data)
    vbox:
      add "#000" ysize 4
      hbox:
        xalign 0.5
        if len(pages)>1:
          use ui_choice(">>>set_intro_info_page:"+pages[(current_n-1)%len(pages)],title="<<<",size=pref_btn_size,keyboard_focus=False)
          use ui_choice(">>>set_intro_info_page:"+pages[(current_n+1)%len(pages)],title=">>>",key="K_TAB",size=pref_btn_size,keyboard_focus=False)
        else:
          use ui_choice(None,size=pref_btn_size)
          use ui_choice(None,size=pref_btn_size)

screen interaction_intro(act_data):
  style_prefix "interaction_default"
  hbox:
    align (0.5,0.5)
    ysize (1080-32)
    spacing 8
    fixed:
      xsize 384
      use ui_frame
    side "c b":
      xsize 1108
      yfill True
      spacing 8
      use ui_frame(scroll=True):
        use ui_scrollbox(id="interaction_default_content",update=update_interaction,main_viewport=True):
          vbox:
            xsize content_width
            $pass
            xalign 0.5
            null height 32
            use interaction_content(act_data)
            null height 32
      use interaction_choices(act_data)
    side "t c":
      xsize 384
      yfill True
      spacing 8
      use ui_frame:
        use quick_menu
      use ui_frame(ysize=True):
        use interaction_intro_side_info(act_data)
