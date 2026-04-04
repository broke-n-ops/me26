screen status_sexbot(act_data):
  style_prefix "mode_status"
  $char=find_character(act_data["char"])
  side "c b":
    xsize 1108
    yfill True
    spacing 8
    use ui_frame(scroll=True):
      use ui_scrollbox(True,id="interaction_default_content",update=update_interaction,main_viewport=True):
        vbox:
          xsize content_width
          xalign 0.5
          null height 32
          $renpy.use_screen("status_sexbot_page_{}".format(act_data.get("status_page","info")),act_data)
          null height 32
    python:
      choices=[None]*18
      choices[0]=choice_info("mode_status:"+char.id+",info",title="Info",key="1",)
      choices[1]=choice_info("mode_status:"+char.id+",chassis",title="Chassis",key="2")
      choices[17]=choice_info("<<<leave_mode",pos=17,key="cancel")
    use interaction_choices(act_data,choices)
