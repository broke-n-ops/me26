label begin_bot_interaction(bot_id):
  $game_call_stack[-1]="end_bot_interaction"

## 0.12.8 changes to avoid bot interaction mismatch with bot side info
  if using_bot_monitor==1:                               ## bot monitor software
    $current_side_info_bot=bot_id
    $temp_int=home.sexbots.index(current_side_info_bot)
##    $print "index: ",temp_int

## 0.14.2 BUGFIX - at power level 1 with 6 capsules interacting with bot in capsule 6 from within Bot Monitor increased the page number in the capsules screen
## inserted 2 lines, changed next line from 'if' to 'elif'
    if sr24_power_level==1:
      $sr24_capsule_page=0

    elif temp_int<5:                                     ## bots 0-5 on page 0
      $sr24_capsule_page=0
    elif temp_int<10:                                    ## bots 6-10 on page 1
      $sr24_capsule_page=1
    elif temp_int<15:                                    ## bots 11-15 on page 2
      $sr24_capsule_page=2
    else:                                                ## must be bots 16-20 on page 3
      $sr24_capsule_page=3
    $sr24_capsules_screen_page=sr24_capsule_page
  elif interacting_from_storage==1:                      ## interacting from storage  
    $current_side_info_bot=bot_id
    $temp_int=workshop.sexbots.index(current_side_info_bot)
 
  return ">>>interact:"+bot_id

label end_bot_interaction:
## 0.12.8 changes to avoid bot interaction mismatch with bot side info
  if interacting_from_storage==1:                  ## was interacting from storage
    $interacting_from_storage=0                    ## clear flag
    $current_side_info_bot=remember_current_bot
    $temp_int=home.sexbots.index(current_side_info_bot)
##    $print "index: ",temp_int
    if temp_int<=5:                                ## bots 0-5 on page 0
      $sr24_capsule_page=0
    elif temp_int<=10:                             ## bots 6-10 on page 1
      $sr24_capsule_page=1
    elif temp_int<=15:                             ## bots 11=15 on page 2
      $sr24_capsule_page=2
    else:                                          ## must be bots 16-20 on page 3
      $sr24_capsule_page=3
    $sr24_capsules_screen_page=sr24_capsule_page   
  while "end_bot_interaction" in game_call_stack:
    $game_call_stack.pop()
  return "continue"

label end_bot_interaction_part(until_suffix):
  $game_call_stack.pop()
  while game_call_stack and not game_call_stack[-1].endswith(until_suffix):
    $game_call_stack.pop()
  return "continue"

init python:
  def interact(target,*args,**kwargs):
    kwargs["prepare"]=True
    if not target:
      return choice(None,*args,**kwargs)
    bot=getattr(store,"bot")
    if target.startswith("^"):
      target="interact:{},{}".format(bot.id,target.lstrip("^"))
    elif target.startswith("<"):
      target="<<<interact:{},{}".format(bot.id,target.lstrip("<"))
    else:
      target=">>>interact:{},{}".format(bot.id,target)
    return choice(target,*args,**kwargs)

init python:
  def find_interact_label(action,pattern="interact_{}{}"):
    bot=getattr(store,"bot",None)
    for actor_id in (getattr(bot,"model_id","default"),"default"):
      interact_label=pattern.format(actor_id,(("_"+action) if action else ""))
      if renpy.has_label(interact_label):
        return interact_label

  def interact_parse_args(args):
    bot_id,sep,action=args.partition(",")
    bot=find_character(bot_id)
    action,sep,action_args=action.partition(",")
    if action.startswith("!"):
      interact_action=action[1:]
    else:
      interact_action=find_interact_label(action,"interact_{}{}")
    interact_action_args=(bot,action_args) if action_args else (bot,)
    return interact_action,interact_action_args

  def label_interact_action_info(**kwargs):
    action=kwargs["action"]
    interact_action,interact_action_args=interact_parse_args(action.lstrip("~<> ").partition(":")[2].strip())
    if len(interact_action_args)>1:
      interact_action_args=interact_action_args[0].id+","+interact_action_args[1]
    else:
      interact_action_args=interact_action_args[0].id
    kwargs["action"]=interact_action+":"+interact_action_args
    rv=choice_info(**kwargs)
    rv["action"]=action
    return rv

label interact(args):
  $interact_action,interact_action_args=interact_parse_args(args)
  call expression interact_action pass (*interact_action_args)
  $bot=None
  return _return

label interact_include(interact_action):
  $interact_action=find_interact_label(interact_action,"interact_{}_include{}")
  if interact_action:
    call expression interact_action pass (bot,)
  return _return
