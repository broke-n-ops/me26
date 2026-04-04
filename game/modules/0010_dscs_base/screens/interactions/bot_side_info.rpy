define interact_available_locations=("home","workshop")

screen info_row(title,value=""):
  side "c r":
    xfill True
    text title xalign 0.0 text_align 0.0 layout "nobreak"
    text value xalign 1.0 text_align 1.0

default current_side_info_bot=None

screen bot_side_info(bot_id):
  style_prefix "bot_side_info"
  $bot=find_character(bot_id)
  if bot:
    side "c b":
      use ui_scrollbox(id="bot_side_info",update=True):
        add FitTextDisplayable("{size=-8}"+bot.name+"{/}","idle","cs_header",side_text_size) xalign 0.5
        use info_row("Model:",bot.model_name)
        use vdiv
        side "l c":
##          spacing 8
          spacing 4    ## 0.9.n
          fixed:
            xysize (180,260)
            add "bots [bot.model_id] avatar@180x260" align (0.5,0.0)
          vbox:
            spacing 4           ## 0.9.n was 4, make it 3
##            use info_row("{size=-8}Rate:{/}","{size=-8}\n{/}{good}"+bot.rate+"{/}")     ## 0.9.n new line to show bot's rate
            use info_row("{size=-8}Rate:{/}","{good}"+bot.rate+"{/}")     ## 0.9.n new line to show bot's rate
            $integrity="{bad}disabled{/}" if bot.chassis.is_disabled else ("{good}"+str(bot.chassis.integrity)+"%{/}")
            use info_row("{size=-8}Chassis:{/}","{size=-8}\n{/}"+integrity)
            use info_row("{size=-8}PsychoCore:{/}","{size=-8}\n{/}"+bot.psychocore.status_str)
            use info_row("{size=-8}Autonomy:{/}","{size=-8}\n{/}{size=-8}{color=#888}("+bot.psychocore.max_roles_str+"){/}{/} {good}"+bot.autonomy.level_name+"{/}")
##            if bot["mission"]:
##              use info_row("{size=-8}On mission:{/}","{size=-8}\n{/}{size=-8}{mark}"+modded_missions[bot["mission"]].title+"{/}{/}")
#(radnor)            use info_row("{size=-8}Estimate:{/}","{size=-8}\n{/}{size=-8}"+money_str(bot_price_function(bot))+"{/}")
        use vdiv
        if bot["mission"]:
          use info_row("{size=-8}On mission:{/}","{size=-8}{good}"+modded_missions[bot["mission"]].title+"{/}{/}")
        python:
          if bot.roles:
            roles=[role for role in bot.roles if not role.hidden]
            roles.sort(key=lambda role:(role.list_priority,role.name.lower()))
            roles="\n".join(("{size=-8}{mark}"+role.name+"{/}{/}" for role in roles))
            role=None
          else:
            roles="{size=-8}{color=#888}no role set{/}{/}"
        use info_row("{size=-8}Role:{/}",roles)
        use vdiv
        python:
          stats=[find_stat(stat_id) for stat_id in bot.stats_order]
          stats=[stat for stat in stats if not stat.hidden and stat.stat_type=="bot_skill"]
          stats.sort(key=lambda stat:stat.name.lower())
        for stat in stats:
          $stat=getattr(bot,stat.id)
          $stat_progress="{size=-8}{color=#888}"+"({}%)".format(stat.progress_percent)+"{/}{/}"
          $stat_level=stat.level_name
          use info_row("{mark}"+stat.name+"{/}",stat_progress+" {mark}"+stat_level+"{/}")
        $stat=None
        $stats=None
      vbox:
        add "#000" ysize 4
        null height 4
        hbox:
          xalign 0.5
          use ui_choice(">>>enter_mode:mode_status:"+bot.id,title="Status",key="K_F3",size=pref_btn_size,keyboard_focus=False)
##0.12.8 make bot monitor bot show up on side to avoid confusion because of mis-match
          if bot["mission"] or using_bot_monitor==1:   ## either deactivates interact button
            $interact_action=None
          elif game_current_label_type=="roaming" and game.location.id in interact_available_locations:
            $interact_action=Return(">>>begin_bot_interaction:"+bot.id)
          else:
            $interact_action=None
              
          use ui_choice(interact_action,title="Interact",key="K_F4",size=pref_btn_size,keyboard_focus=False)
  else:
    text "{color=#888}No bot selected{/}" style "cs_center" yalign 0.5
