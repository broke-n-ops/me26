screen workshop_storage():
  python:
    move_btn_size=(100,48)
    page=workshop_storage_page
    per_page=workshop_sexbots_storage_upgrade_space
    bots=workshop.sexbots[page*per_page:(page+1)*per_page]
    max_page=workshop.max_sexbots//per_page
  text "Railing {mark}#"+str(page+1)+"{/} of [max_page]" xalign 0.5
  grid 2 3:
    xspacing 100
    yspacing 24
    allow_underfull True
    for n,bot in enumerate(bots):
      vbox:
        xsize (content_width-100)//2
        side "l c":
          spacing 24
          vbox:
            xsize 226
            if bot and home.available_capsules>0 and not bot["mission"]:
              use ui_choice(">>>workshop_storage_move_to_capsule:"+str(page*per_page+n),title="Move to capsule",size=(200,48),align=0.5)
            else:
              use ui_choice(None,title="Move to capsule",size=(200,48),align=0.5)
            if bot:
              text "{mark}[bot]{/}" xalign 0.5
              text "{size=-8}[bot.model_name]{/}" xalign 0.5  ## 0.14 make model name white to match how it looks on capsules screen
            else:
              text "{info}Empty{/}" xalign 0.5
              text "{size=-8} {/}" xalign 0.5

## 0.14 trying to make it possible to move bots around in storage - all buttons reduced in height from 56 to 48 (capsules use 48) lines 3,21, and23
            if bot:
              hbox:
                xalign 0.5
                if len(home.sexbots)>1:
                  use ui_choice(">>>workshop_storage_move_up:"+str(page*per_page+n),title="<<<",size=move_btn_size)
                  use ui_choice(">>>workshop_storage_move_down:"+str(page*per_page+n),title=">>>",size=move_btn_size)
                else:
                  use ui_choice(None,title="<<<",size=move_btn_size)
                  use ui_choice(None,title=">>>",size=move_btn_size)
## 0.14 end of insertion


          vbox:
            null height 15   ## 0.14 was 4, try 15
            text ""
            if bot:
              use info_row("{size=-8}Chassis:{/}","{size=-8}{mark}"+str(bot.chassis.integrity)+"%{/}{/}")
              null height 2  ## 0.14 add a little space
              use info_row("{size=-8}PsychoCore:{/}","{size=-8}"+bot.psychocore.status_str+"{/}")
            else:
              use info_row("{size=-8} {/}","{size=-8} {/}")
              null height 2  ## 0.14 add a little space
              use info_row("{size=-8} {/}","{size=-8} {/}")
            null height 3   ## 0.14 was 4, try 5
            hbox:
              xalign 0.5
              if bot:
                use ui_choice(">>>enter_mode:mode_status:"+bot.id,title="Status",size=move_btn_size)
                if bot["mission"]:
                  use ui_choice(None,title="Interact",size=move_btn_size,hint="{hint}on mission{/}")
                else:
                  use ui_choice(">>>workshop_storage_interact:"+bot.id,title="Interact",size=move_btn_size,cost=[("energy",1)])
              else:
                use ui_choice(None,title="Status",size=move_btn_size)
                use ui_choice(None,title="Interact",size=move_btn_size,hint="{hint}1 AP{/}")
