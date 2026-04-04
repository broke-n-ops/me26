## ===== added to support more than 6 capsules =====

init python:
  sr24_capsule_page=0                                  ## pages are 0 (bots 0-4), 1 (bots 5-9), 2 (bots 10-14), and 3 (bots 15-19)
  sr24_capsule_flag=False                              ## set to 'True' when viewing capsules, clear to 'False' in 'home' and 'workout' screens

label sr24_capsule_next_page():                        ## 0-4 bots are on page "0"
  $sr24_capsule_page+=1                                ## increment page number
  $sr24_capsules_screen_page=sr24_capsule_page
  if len(home.sexbots)<=10 and sr24_capsule_page>1:    ## 5-9 bots are on page "1"
    $sr24_capsule_page=0                               ## reset to page "0"
    $sr24_capsules_screen_page=sr24_capsule_page
  elif len(home.sexbots)<=15 and sr24_capsule_page>2:  ## 10-14 bots are on page "2"
    $sr24_capsule_page=0                               ## reset to page "0"
    $sr24_capsules_screen_page=sr24_capsule_page
  elif sr24_capsule_page>3:                            ## 15-19 bots are on page "3", there cannot be a page 4
    $sr24_capsule_page=0                               ## reset to page "0"
    $sr24_capsules_screen_page=sr24_capsule_page
  $save_premode_interaction()                          ## saves the previous interaction so you can replay it
  $replay_premode_interaction()                        ## replays the previous interaction, see above
  return

## 0.14 added a previous button to the capsule selection buttons on the bottom right of the screen

label sr24_capsule_prev_page():                        ## 0-4 bots are on page "0"
  $sr24_capsule_page-=1                                ## decrement page number
  $sr24_capsules_screen_page=sr24_capsule_page
  if sr24_capsule_page<0:                              ## was on page 0, must loop back to the highest page
    if len(home.sexbots)>15:                           ## more than 15 capsules, highest page is "3"
      $sr24_capsule_page=3                             ## reset to page "3"
      $sr24_capsules_screen_page=sr24_capsule_page
    elif len(home.sexbots)>10:                         ## 11 - 15 capsules, highest page "2"
      $sr24_capsule_page=2                             ## reset to page "3"
      $sr24_capsules_screen_page=sr24_capsule_page
    else:                                              ## we're using pages so we must have between 7 and 10 capsules, highest page "1" 
      $sr24_capsule_page=1                             ## reset to page "2"
      $sr24_capsules_screen_page=sr24_capsule_page
  $save_premode_interaction()                          ## saves the previous interaction so you can replay it
  $replay_premode_interaction()                        ## replays the previous interaction, see above
  return

##===== end of addition =====

label set_side_info_bot(bot_id):
  $current_side_info_bot=bot_id
  $save_premode_interaction()
  $replay_premode_interaction()
  return

screen bot_side_info_tabs():
  vbox:
    grid 2 3:
      allow_underfull True
      python:
        bots=[bot.id for bot in home.sexbots if bot]
        next_bot=None
        if bots:
          if current_side_info_bot in bots:
            next_bot=bots[(bots.index(current_side_info_bot)+1)%len(bots)]
          else:
            next_bot=bots[0]
        if current_side_info_bot and len(bots)==1:
          next_bot=None
      if sr24_max_capsules<=6:                    ##  use original code until capsule capacity increased
        for n in range(0,sr24_max_capsules):
          if n<len(home.sexbots):
            $bot=home.sexbots[n]
            if bot:
              use ui_choice(">>>set_side_info_bot:"+bot.id,title="C"+str(n+1)+"-"+bot.name,hint=bot.model_name,key=("K_TAB" if bot.id==next_bot else None),selected_if=current_side_info_bot==bot.id,keyboard_focus=False)
            else:
              use ui_choice(None,title="C"+str(n+1)+"-"+"Empty")
          else:
            use ui_choice(None)
      else:                                          ## use new code to support more than 6 capsules
        $first_capsule=sr24_capsule_page*5
        $last_capsule=first_capsule+5
        $tab_shortcut_active=0                        ## set to 1 when a 'tab' shortcut key is on the screen
        for n in range(first_capsule,last_capsule):
          if n<len(home.sexbots):
            $bot=home.sexbots[n]
            if bot:
              if bot.id==next_bot:
                $tab_shortcut_active=1
## 0.12.8 deactivate bot buttons when using bot monitor or interacting from storage
              if using_bot_monitor==0 and interacting_from_storage==0:
## 0.14 trying to add a key to the first bot on the page
                if n==first_capsule:
                  use ui_choice(">>>set_side_info_bot:"+bot.id,title="C"+str(n+1)+"-"+bot.name,hint=bot.model_name,key="q",selected_if=current_side_info_bot==bot.id,keyboard_focus=False)    
                elif bot.id==next_bot:
                  use ui_choice(">>>set_side_info_bot:"+bot.id,title="C"+str(n+1)+"-"+bot.name,hint=bot.model_name,key="K_TAB",selected_if=current_side_info_bot==bot.id,keyboard_focus=False)
                else:
                  use ui_choice(">>>set_side_info_bot:"+bot.id,title="C"+str(n+1)+"-"+bot.name,hint=bot.model_name,key=None,selected_if=current_side_info_bot==bot.id,keyboard_focus=False)    
                  ##  ORIGINAL LINE    use ui_choice(">>>set_side_info_bot:"+bot.id,title="C"+str(n+1)+"-"+bot.name,hint=bot.model_name,key=("K_TAB" if bot.id==next_bot else None),selected_if=current_side_info_bot==bot.id,keyboard_focus=False)
              else:
                use ui_choice(None,title="C"+str(n+1)+"-"+bot.name,hint=bot.model_name)
            else:
              use ui_choice(None,title="C"+str(n+1)+"-"+"Empty")
          else:
            use ui_choice(None)
## 0.12.8 deactivate next button when using bot monitor or interacting with bot from storage
## 0.14 split large 'Next' button into smaller 'Prev' and 'Next' buttons
        hbox:
          if home.sexbots>5 and using_bot_monitor==0 and interacting_from_storage==0:
            use ui_choice(">>>sr24_capsule_prev_page",title="Prev",key="p",size=(91,72),keyboard_focus=False)
            use ui_choice(">>>sr24_capsule_next_page",title="Next",key="n",size=(92,72),keyboard_focus=False)
          else:
            use ui_choice(None,title="Prev",size=(91,72))
            use ui_choice(None,title="Next",size=(92,72))
screen interaction_default(act_data):
  style_prefix "interaction_default"
  hbox:
    align (0.5,0.5)
    ysize (1080-32)
    spacing 8
    side "c b":
      xsize 384
      yfill True
      spacing 8
      use interaction_game_status(act_data)
      use interaction_mode_buttons
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
    side "t c b":
      xsize 384
      yfill True
      spacing 8
      use ui_frame:
        use quick_menu
      use ui_frame(ysize=True,scroll=True):
        use bot_side_info(current_side_info_bot)
      use ui_frame:
        use bot_side_info_tabs
