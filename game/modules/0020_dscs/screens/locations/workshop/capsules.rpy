screen workshop_capsules():
  python:
    if sr24_power_level==1:                ## level 1 is like the original game
      capsules_bots=home.sexbots[0:6]
    else:                                  ## levels 2-4 capsule screen shows up to 5 bots per page
      if sr24_capsules_screen_page==0:     ## bots 0 to 4
        capsules_bots=home.sexbots[0:5]    ## makes range 0 to 4
      elif sr24_capsules_screen_page==1:   ## bots 5 to 9
        capsules_bots=home.sexbots[5:10]   ## makes range 5 to 9## makes range 5 to 9
      elif sr24_capsules_screen_page==2:   ## bots 10 to 14
        capsules_bots=home.sexbots[10:15]  ## makes range 10 to 14
      else:                                ## must be page 3, bots 10 to 14
        capsules_bots=home.sexbots[15:20]  ## makes range 15 to 19
    move_btn_size=(100,48)

  grid 2 3:
    xspacing 100
    yspacing 24
    allow_underfull True
    for bot_n,bot in enumerate(capsules_bots):
      $bot_n=bot_n+5*sr24_capsules_screen_page
##      $print "capsule ",bot_n,"Status: ",capsule_upgrade_status[bot_n]
      if capsule_upgrade_status[bot_n]==0:
        $AI_installed=None
      else:
        $AI_installed=1

      vbox:
        xsize (content_width-100)//2
        side "l c":
          spacing 24
          vbox:
            xsize 226
            if bot:
              if workshop.available_space>0 and not bot["mission"]:
                use ui_choice(">>>workshop_capsules_move_to_storage:"+str(bot_n),title="Move to storage",size=(200,48),align=0.5)
              else:
                use ui_choice(None,title="Move to storage",size=(200,48),align=0.5)
              null height 4
              text "{mark}"+bot.name+"{/}" xalign 0.5
              text "{size=-8}"+bot.model_name+"{/}" xalign 0.5
              null height 4
              hbox:
                xalign 0.5
                if len(home.sexbots)>1:
                  use ui_choice(">>>workshop_capsules_move_up:"+str(bot_n),title="<<<",size=move_btn_size)
                  use ui_choice(">>>workshop_capsules_move_down:"+str(bot_n),title=">>>",size=move_btn_size)
                else:
                  use ui_choice(None,title="<<<",size=move_btn_size)
                  use ui_choice(None,title=">>>",size=move_btn_size)
          vbox:
            xfill True
            null height 48+4
            if bot is False:
              text "{info}Capsule #"+str(bot_n+1)+"{/}" xalign 0.5
            else:
              text "Capsule {mark}#"+str(bot_n+1)+"{/}" xalign 0.5
            if (bot or bot is None) and AI_installed:
              use info_row("{size=-8}Stability AI:{/}","{size=-8}{mark}Level "+str(capsule_upgrade_status[bot_n])+"{/}{/}")
            else:
              use info_row("{info}{size=-8}Stability AI:{/}{/}","{size=-8}{info}(none){/}{/}")
            null height 4
            hbox:
              xalign 0.5
              ## 0.12.8 add bot monitor
              if bot_monitor_status[bot_n]==0:
                use ui_choice("select_bot_monitor:"+str(bot_n),title="Monitor",size=move_btn_size)
              else:
                use ui_choice(None,title="Monitor",size=move_btn_size)
              ## end addition      
              if capsule_upgrade_status[bot_n]<=3:
                use ui_choice("select_capsule_upgrade:"+str(bot_n),title="Upgrade AI",size=move_btn_size)
              else:
                use ui_choice(None,title="Upgrade AI",size=move_btn_size)
