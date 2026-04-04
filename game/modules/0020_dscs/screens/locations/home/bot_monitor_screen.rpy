## Screens for the 'Bot Monitor' software

screen avatar_repair_buttons(bot,page_number_str,bm_defective_bot):
  hbox:
    add "bots [bot.model_id] avatar@64x90" align (0.0,0.0)
    vbox:
      if bot.chassis.integrity<100 and mc.energy>0:  
        use ui_choice("bm_repair_bot:"+bot.id+" "+page_number_str,title="Tinker (1AP)",prepare=True,size=(150,46),keyboard_focus=False)
      else:
        use ui_choice(None,title="Tinker (1AP)",prepare=True,size=(150,46),keyboard_focus=False)
        
## 0.15.1 if defective bot noticed make inactive button
      if bm_defective_bot==1:
          
##        $print "defective bot noticed, display inactive button"  
          
        use ui_choice(None,title="Stabilize (1AP)",prepare=True,size=(150,46),keyboard_focus=False)  ## inactive stability button
      elif bot.psychocore.stability<100 and not bot.chassis.is_disabled and mc.energy>0:             ## conditions necessary for an active button
        
##        $print "Normal bot or defective bot not noticed, display active button"

        use ui_choice("bm_stabilize_bot:"+bot.id+" "+page_number_str,title="Stabilize (1AP)",prepare=True,size=(150,46),keyboard_focus=False)
      else:                                                                                          ## conditions NOT met for active stability button

##        $print "Normal bot or defective bot not noticed but conditions not met, display inactive button"

        use ui_choice(None,title="Stabilize (1AP)",prepare=True,size=(150,46),keyboard_focus=False)  ## inactive stability button

##  $print "end of button display, bm_defective_bot: ",bm_defective_bot
  

screen avatar_inactive_buttons(bot):
  hbox:
    add "bots [bot.model_id] avatar@64x90" align (0.0,0.0)
    vbox:
      use ui_choice(None,title="Tinker (1AP)",prepare=True,size=(150,46),keyboard_focus=False)
      use ui_choice(None,title="Stabilize (1AP)",prepare=True,size=(150,46),keyboard_focus=False) 

screen bot_information_text(bot,position,page_number_str,bm_defective_bot):
  
##  $print  
##  $print "Screen Function Parameters: ",bot,position,page_number_str
##  $print "Bot Condition - Integrity: :",bot.chassis.integrity," Stability: ",bot.psychocore.stability
##  $print

  $tmp_text=""
  $tmp_text2=""
  $disp_text=[]
  $disp_text.append("{size=-8}C"+str(position)+": "+"{mark}"+bot.name+"{/}{/}")
  $disp_text.append("{size=-8}Model: {mark}"+bot.model_name+"{/}{/}")
  if position!=0:                                                                ## position=0 means don't display the bot's info
    $tmp_text=str(bot.chassis.integrity)+"%"
    if len(tmp_text)==2:
      $tmp_text="  "+tmp_text
    elif len(tmp_text)==3:
      $tmp_text=" "+tmp_text
    $tmp_text=colorize_percent_string(tmp_text,bot.chassis.integrity)

##    $print
##    $print "DRAWING INFORMATION"
##    $print "bot: ",bot," integrity: ",bot.chassis.integrity," stability: ",bot.psychocore.stability
##    $print
    
    $tmp_text2=colorize_required_percent_string(bot.chassis.integrity,bot.task_req_integrity)
    $disp_text.append("{size=-8}Integrity: "+tmp_text+"{space=8}Duties Require: "+tmp_text2+"{/}")

## 0.15.1 insert/modify for defective bots 'Read Error' message
    if bm_defective_bot!=1:                        ## display the stability information normally
 
##      $print "Normal bot or defective not noticed, display information"

      $tmp_text=str(bot.psychocore.stability)+"%"
      if len(tmp_text)==2:
        $tmp_text="  "+tmp_text
      elif len(tmp_text)==3:
        $tmp_text=" "+tmp_text
      $tmp_text=colorize_percent_string(tmp_text,bot.psychocore.stability)
      $tmp_text2=colorize_required_percent_string(bot.psychocore.stability,bot.task_req_stability)
      $disp_text.append("{size=-8}Stability: "+tmp_text+"{space=10}Duties Require: "+tmp_text2+"{/}")
    else:        ## display error for defective bot

##      $print "Defective bot noticed, display read error"

      $tmp_text="{bad}Read Error{/}{space=135}"
      $disp_text.append("{size=-8}Stability: "+tmp_text)
## end of innsert/modify

  else:
    $disp_text[2]="{size=-8}blank integrity"
    $disp_text[3]="{size=-8}blank stability"
  hbox:
    text "{size=-24} {/}"
  hbox:
    xfill True
    text disp_text[0] xalign 0.0 text_align 0.0 layout "nobreak"
    text disp_text[2] xalign 1.0 text_align 1.0
  hbox:
    text "{size=-19} {/}"
  hbox:
    xfill True
    text disp_text[1] xalign 0.0 text_align 0.0 layout "nobreak"
    text disp_text[3] xalign 1.0 text_align 1.0

screen bot_on_mission(bot,position):
  $tmp_text=""
  $disp_text=[]
  $disp_text.append("{size=-8}C"+str(position)+": "+"{mark}"+bot.name+"{/} is on a mission and cannot be monitored.{/}")
  hbox:
    text disp_text[0] xalign 0.0
    
screen bot_monitor_inactive(bot,position):
  $tmp_text=""
  $disp_text=[]
  $disp_text.append("{size=-8}C"+str(position)+": "+"{mark}"+bot.name+"{/} cannot be monitored because 'bot monitor' is not activated.{/}")
  hbox:
    text disp_text[0] xalign 0.0

##screen empty_capsule(position,monitor_active):
screen empty_capsule(position):
  $tmp_text=""
  $disp_text=[]
  if bot_monitor_status[position-1]==1:             ## capsule index is one less than position, capsule is licensed
    $disp_text.append("{size=-8}C"+str(position)+": {mark}Empty{/}            ({mark}Bot Monitor{/} is licensed and activated on this capsule)")
  else:                                             ##  capsule is not licensed
    $disp_text.append("{size=-8}C"+str(position)+": {mark}Empty{/}            ({mark}Bot Monitor{/} is {mark}NOT{/} licensed on this capsule)")
  hbox:
    text disp_text[0] xalign 0.0

screen replace_parts(bot,position):
  $tmp_text=""
  $disp_text=[]
  $disp_text.append("{size=-8}C"+str(position)+": "+"{mark}"+bot.name+"{/} has missing or irrepairable parts which must be replaced.{/}")
  hbox:
    text disp_text[0] xalign 0.0


screen draw_divider():
  
  if home.max_sexbots!=6:                           ## normal spacing
    $tmp_txt=' '*333
    text "{size=-16}{info}{u}"+tmp_txt+"{/}{/}{/}"
    text "{size=-21} {/}"
  else:                                             ## when displaying 6 capsules the divider must be compressed
    $tmp_txt=' '*998
    text "{size=-25}{info}{u}"+tmp_txt+"{/}{/}{/}"  ## -25 is the largest value that works here
    text "{size=1} {/}"