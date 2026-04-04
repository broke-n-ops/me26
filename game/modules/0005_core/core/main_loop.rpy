default exit_main_loop=False
default game_call_stack=[]
default game_current_label=None
default game_current_label_type=None
default update_interaction=False
default game_bg=None
default game_bgm=None
default default_main_loop_label="roaming"

define special_labels_id={
  "roaming": "roaming",
  "mode_": "mode",
  }

screen main_loop_controller():
  pass

label main_loop_interact:
  call screen main_loop_controller
  return _return

init python:
  default_bgm=[bgm for bgm in dir(audio) if bgm.startswith("default_bgm ")]

  def default_bgm_callback():
    if not main_menu:
      if hasattr(store,"game"):
        if not has_audio(game_bgm):
          if not renpy.music.get_playing():
            if default_bgm:
              renpy.music.play(randchoice(default_bgm),loop=False)

  renpy.music.set_queue_empty_callback(default_bgm_callback)

label start_main_loop:
  $exit_main_loop=False
  $reset_interaction("default")
label main_loop:
  while not exit_main_loop:
    $set_interaction("default")
    if (not game_call_stack or (len(game_call_stack)==1 and game_call_stack[0]==default_main_loop_label)) and pending_events:
      $event_label,event_label_args,event_label_kwargs=pending_events.pop(0)
      $game_current_label=[event_label,event_label_args,event_label_kwargs]
      $game_current_label_type="event"
      call expression event_label pass (*event_label_args,**event_label_kwargs)
      if _return=="continue":
        jump main_loop
    else:
      $current_label,tmp,current_label_args=game_call_stack[-1].partition(":")
      python hide:
        current_label_type="label"
        for prefix,label_type in special_labels_id.items():
          if current_label.startswith(prefix):
            current_label_type=label_type
        if len(game_call_stack)>1:
          current_label_type="sub_"+current_label_type
        store.game_current_label=[current_label,(current_label_args,),{}]
        store.game_current_label_type=current_label_type
      if current_label_args:
        call expression current_label pass(current_label_args)
      else:
        call expression current_label
    if not _return:
      if has_audio(game_bgm):
        $renpy.music.play(game_bgm,if_changed=True)
      elif renpy.music.get_playing() not in default_bgm:
        $renpy.music.stop()
      if game_bg:
        scene expression game_bg
      else:
        scene
      python:
        act_screen,act_args,act_kwargs=act.finalize()
        reset_interaction("default")
        renpy.hide_screen("interaction")
        renpy.show_screen(act_screen,*act_args,_tag="interaction",**act_kwargs)
        if persistent.in_game_transitions:
          renpy.transition(interaction_transition)
        notify.counters.clear()        ##  SQUIRREL24: LINE ADDED TO RESET NOTIFICATIONS IN SR24 0.3.1
      call main_loop_interact from _call_main_loop_interact
    python:
      prev_game_call_stack=game_call_stack
      prev_current_label=game_current_label
      prev_current_label_type=game_current_label_type
      if isinstance(_return,str):
        update_interaction=_return.startswith("~")
        if update_interaction:
          _return=_return.lstrip("~ ")
        if _return.startswith(">>>"):
          game_call_stack.append(_return.lstrip("> "))
        elif _return.startswith("<<<"):
          if game_call_stack:
            game_call_stack.pop()
          if not game_call_stack:
            game_call_stack.append(default_main_loop_label)
          if _return.lstrip("< "):
            if game_call_stack:
              game_call_stack[-1]=_return.lstrip("< ")
            else:
              game_call_stack.append(_return.lstrip("< "))
        elif _return!="continue":
          if game_call_stack:
            game_call_stack[-1]=_return
          else:
            game_call_stack.append(_return)
  if isinstance(exit_main_loop,str):
    jump expression exit_main_loop
  return
