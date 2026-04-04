define side_text_size=(300,1000)
define center_text_size=(content_width,1000)

style interaction_content:
  color "#FFF"
  first_indent 35      ## 0.14.0 was 60
  newline_indent True

style interaction_notification:
  color "#AAA"
  italic True
  first_indent 35      ## 0.14.0 was 60
  newline_indent True

default interaction_content_screen_counter=0

screen interaction_content_element(el):              ## 0.9.1 revise function to reduce CPU use - help provided by 'MikasaTanikawa' on F95Zone
##  $print "parameter received - el: ",el
  if isinstance(el,str):
    if el.startswith("{#="):                         ## a style preceeds the content
      $el_style,tmp,el=el[3:].partition("}")         ## extract style from el
##      $print "content with preceding style received - el starts with ('{#='), style stripped from el"
##      $print "style: ",el_style
      if el.startswith("{image="):                   ## content is 'image'
##        $print "content is image - revised el starts with ('{image=')"
##        $print "content: ",el
        $el=el[len("{image="):].split("}", 1)[0]
        frame style el_style:
          add el
      else:                                          ## content not image, treat as text displayed using style
##        $print "content not 'image', assume text & display using style"
        text el style el_style
    elif el.startswith("{image="):                   ## no style preceeding content and content is image
##        $print "image content without style received - el does NOT start with ('{#=') but does start with ('{image=')"
##        $print "content: ",el
        $el=el[len("{image="):].split("}", 1)[0]
        frame:
          add el
    else:                                            ## content is simply text without a style provided
##      $print "content is not image and no style provided, assume quoted text string"
      text el style "interaction_content"
## end of modifications in 0.9.1
  elif isinstance(el,tuple) and len(el)>0 and isinstance(el[0],str):
    if el[0]=="notification":
      text el[1] style "interaction_notification"
    elif el[0]=="screen":
      $store.interaction_content_screen_counter+=1
      $renpy.use_screen(el[1],_name="{}_{}".format(el[1],interaction_content_screen_counter),_scope=_scope,*el[2],**el[3])

screen interaction_content(act_data):
  if act_data and "content" in act_data:
    $content=[]
    for el in act_data["content"]:
      if isinstance(el,str) and "{#header}" in el:
        $content.insert(0,el)
      else:
        $content.append(el)
    for el in content:
      if isinstance(el,tuple) and len(el)>0 and (el[0]=="block"):
        $sides=" ".join((side[0] for side in el[1]["sides"]))
        side sides:
          xfill True
          for side,width in el[1]["sides"]:
            vbox:
              if width:
                xsize width
              for block_el in el[1][side]:
                use interaction_content_element(block_el)
      else:
        use interaction_content_element(el)

screen interaction_mode_buttons():
  use ui_frame:
    grid 2 1:
      align (0.5,0.5)
      use ui_choice(">>>enter_mode:mode_status",title="Status",key="K_F1",prepare=True,size=pref_btn_size,keyboard_focus=False)
      use ui_choice(">>>enter_mode:mode_journal",title="Journal",key="K_F2",prepare=True,size=pref_btn_size,keyboard_focus=False)

screen interaction_choices(act_data,choices=None):
  $choices=list(choices or ([None]*18))[:]
  use ui_frame:
    python:
      auto_pos=0
      auto_key=1
      for choice in act_data["choices"]:
        choice=choice.copy()
        choice_pos=choice.get("pos")
        if choice_pos is not None:
          choices[choice_pos]=choice
        else:
          while choices[auto_pos] is not None:
            auto_pos+=1
          choices[auto_pos]=choice
          if auto_key<=9 and choice.get("title")!="---":
            if choice.get("key") is None:
              choice["key"]=[str(auto_key)]
              auto_key+=1
    grid 6 3:
      align (0.5,0.5)
      for choice_n,choice in enumerate(choices):
        use ui_choice(choice,focus_priority=len(choices)-choice_n+1)
