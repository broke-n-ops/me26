screen mode_status_char_btn(char_id,title=None,hint=None,key=None):
  fixed:
    fit_first True
    xalign 0.5
    use ui_choice("mode_status:"+char_id,title=title,hint=hint,key=key,size=(320,72),prepare=True,keyboard_focus=False)

style mode_status_left_text is cs_center

screen mode_status(act_data):
  style_prefix "mode_status"
  $char=find_character(act_data["char"])
##  $print "char: ",char
  hbox:
    align (0.5,0.5)
    ysize (1080-32)
    spacing 8
    fixed:
      xsize 384
      use ui_frame(scroll=True):
        use ui_scrollbox(id=69,update=True):    ## added 'id' and 'update' in 0.8.n using advice from 'subenji' on F95Zone
          style_prefix "mode_status_left"
          python:
            chars=[game.pc.id]+[bot.id for bot in home.sexbots if bot]+[bot.id for bot in workshop.sexbots if bot]
            next_char=None
            if len(chars)>1:
              if char.id in chars:
                next_char=chars[(chars.index(char.id)+1)%len(chars)]
              else:
                next_char=chars[0]
          null height 32
          text "You"
          use mode_status_char_btn(game.pc.id,key=("K_TAB" if next_char==game.pc.id else None))
          use vdiv
          text "Sex Bots"
## 0.10.n added bot's location to hint
          $cap_empty=1                             ## assume capsules are empty at start
          $bots=[bot for bot in home.sexbots]
          if bots:
            for bot in bots:
              if bot:
                $cap_empty=0                       ## capsules have at least 1 bot
                $cap_num=bots.index(bot)+1
                $cap_id="C"+str(cap_num)+" - "
                use mode_status_char_btn(bot.id,hint=cap_id+bot.model_name,key=("K_TAB" if next_char==bot.id else None))
##          $print "cap_empty: ",cap_empty
          $store_empty=1                           ## assume storage empty at start
          $bots=[bot for bot in workshop.sexbots]
          if bots:
            for bot in bots:
              if bot:
                $store_empty=0                     ## storage has at least 1 bot
                $store_num=bots.index(bot)
                $temp_rail=store_num//6
                $temp_pos=store_num%6
                $store_rail=str(temp_rail+1)
                $store_pos=str(temp_pos+1)
                $store_id="R"+store_rail+":P"+store_pos+" - "
                use mode_status_char_btn(bot.id,hint=store_id+bot.model_name,key=("K_TAB" if next_char==bot.id else None))
##          $print "store_empty: ",store_empty
          if cap_empty==1 and store_empty==1:
            text "{color=#888}None{/}"
          null height 32
## 0.10.n end of change
    fixed:
      xsize 1108
      yfill True
      $renpy.use_screen(char.status_screen,act_data)
    side "t c":
      xsize 384
      yfill True
      spacing 8
      use ui_frame:
        use quick_menu
      $renpy.use_screen(char.status_side_screen,act_data)
