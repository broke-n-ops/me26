screen status_mc(act_data):
  style_prefix "mode_status"
  $char=find_character(act_data.get("char","mc"))
  side "c b":
    xsize 1108
    yfill True
    spacing 8
    use ui_frame:
      use ui_scrollbox(True,id="interaction_default_content",update=update_interaction,main_viewport=True):
        vbox:
          xsize content_width
          xalign 0.5
          null height 32
          $renpy.use_screen("status_mc_page_{}".format(act_data.get("status_page","info")),act_data)
          null height 32
    python:
      choices=[None]*18
      choices[0]=choice_info("mode_status:mc,info",title="Info",key="1",)
      choices[1]=choice_info("mode_status:mc,expertise",title="Expertise",key="2")
      choices[2]=choice_info("mode_status:mc,reputation",title="Reputation",key="3")
      choices[3]=choice_info("mode_status:mc,property",title="Property",key="4")
      choices[4]=choice_info("mode_status:mc,inventory",title="Inventory",key="5")
## 0.11.n button for new screen: 'Relationships'
      choices[5]=choice_info("mode_status:mc,relationships",title="Relationships",key="6")
      choices[17]=choice_info("<<<leave_mode",pos=17,key="cancel")
    use interaction_choices(act_data,choices)
