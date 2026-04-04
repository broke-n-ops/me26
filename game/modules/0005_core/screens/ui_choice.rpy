default persistent.force_keyboard_focus=False

init -1 python:
  debug_show_ui_choice_areas=False

define ui_choice_color="#6AF"
define ui_choice_hover_color="#8CF"
define ui_choice_insensitive_color="#666"
define ui_choice_selected_idle_color=ui_choice_color
define ui_choice_selected_hover_color=ui_choice_hover_color

define ui_choice_subtitle_color="#48D"

style ui_choice_title is button_text:
  layout "nobreak"
  color ui_choice_color
  hover_color ui_choice_hover_color
  insensitive_color ui_choice_insensitive_color
  selected_idle_color ui_choice_selected_idle_color
  selected_hover_color ui_choice_selected_hover_color

style ui_choice_subtitle is button_text:
  layout "nobreak"
  size 20
  color ui_choice_subtitle_color

style ui_choice_title_small is ui_choice_title:
  size 18
style ui_choice_subtitle_small is ui_choice_subtitle

style ui_choice_title_med is ui_choice_title:
  size 24
style ui_choice_subtitle_med is ui_choice_subtitle

style ui_choice_keys:
  layout "nobreak"
  size 18
  color "#AAA"
  pos (1.0,0.0)
  anchor (1.0,0.5)
  offset (0,6)

screen ui_choice(action_or_info,size=(183,72),focus_priority=None,**kwargs):
  python:
    if isinstance(action_or_info,dict):
      info=action_or_info.copy()
    else:
      info={"action": action_or_info}
    info.update(kwargs)
    if info.pop("prepare",False):
      info=choice_info(**info)
    action=info.get("action")
    title=info.get("title","---")
    hint=info.get("hint")
    action_cost=info.get("cost")
    keysym=info.get("keysym",info.get("key",[]))
    align=info.get("align",0)
    if not isinstance(keysym,(list,tuple)):
      keysym=[keysym]
    sensitive_if=info.get("sensitive_if",True)
    selected_if=info.get("selected_if",False)
    style_suffix=info.get("style_suffix",None)
    keyboard_focus=info.get("keyboard_focus",True) or persistent.force_keyboard_focus
    if hasattr(store,"game"):
      affordable,action_cost_desc=game.pc.check_action_cost(action_cost)
    else:
      affordable,action_cost_desc=True,[]
    if affordable:
      action_cost_desc=[cost[1] for cost in action_cost_desc]
    else:
      action_cost_desc=["{color="+("#666" if cost[0] else "#F00")+"}"+cost[1]+"{/}" for cost in action_cost_desc]
    action_cost_desc=", ".join(action_cost_desc)
    if action_cost_desc:
      if affordable:
        subtitle=action_cost_desc
      else:
        subtitle="{color=#666}"+action_cost_desc+"{/}"
    else:
      subtitle=hint
    choice_id="{}~{}".format((action if isinstance(action,str) else type(action)),title)
    if affordable:
      action=GameAction(action,action_cost,hint,sensitive_if,selected_if)
    else:
      action=None
  if title!="---":
    python:
      title_size=(size[0]-28+6,size[1]-16+6)
      tf_title=Transform(align=(0.5,0.5))
      titleplus_size=(size[0]-28+6,size[1]-30-8+6)
      tf_titleplus=Transform(xalign=0.5,yanchor=0.5,ypos=8+(size[1]-30-8)//2)
      subtitle_size=(size[0]-28+6,26+6)
      tf_subtitle=Transform(xalign=0.5,ypos=1.0,yoffset=-32-4)
      title_style="ui_choice_title_{}".format(style_suffix) if style_suffix else "ui_choice_title"
      subtitle_style="ui_choice_subtitle_{}".format(style_suffix) if style_suffix else "ui_choice_subtitle"
    fixed:
      fit_first True
      if isinstance(align,(list,tuple)):
        align align
      elif align:
        xalign align
      button:
        focus choice_id
        keyboard_focus bool(keyboard_focus)
        if focus_priority:
          default_focus focus_priority
        frame:
          xysize size
          background Frame("ui btn_idle",14,14)
          hover_background Frame("ui btn_hover",14,14)
          insensitive_background Frame("ui btn_insensitive",14,14)
          selected_background Frame("ui btn_hover",14,14)
          if debug_show_ui_choice_areas:
            if subtitle:
              fixed:
                xysize subtitle_size
                at tf_subtitle
                add "#0F04"
              fixed:
                xysize titleplus_size
                at tf_titleplus
                add "#F004"
            else:
              fixed:
                xysize title_size
                at tf_title
                add "#F004"
          if subtitle:
            foreground tf_subtitle(FitTextDisplayable(subtitle,"idle",subtitle_style,subtitle_size))
        if subtitle:
          foreground tf_titleplus(FitTextDisplayable(title,"idle",title_style,titleplus_size))
          hover_foreground tf_titleplus(FitTextDisplayable(title,"hover",title_style,titleplus_size))
          insensitive_foreground tf_titleplus(FitTextDisplayable(title,"insensitive",title_style,titleplus_size))
          selected_idle_foreground tf_titleplus(FitTextDisplayable(title,"selected_idle",title_style,titleplus_size))
          selected_hover_foreground tf_titleplus(FitTextDisplayable(title,"selected_hover",title_style,titleplus_size))
        else:
          foreground tf_title(FitTextDisplayable(title,"idle",title_style,title_size))
          hover_foreground tf_title(FitTextDisplayable(title,"hover",title_style,title_size))
          insensitive_foreground tf_title(FitTextDisplayable(title,"insensitive",title_style,title_size))
          selected_idle_foreground tf_title(FitTextDisplayable(title,"selected_idle",title_style,title_size))
          selected_hover_foreground tf_title(FitTextDisplayable(title,"selected_hover",title_style,title_size))
        action action
      for key in keysym:
        if key:
          key key action action
      text ", ".join([ui_key_name(key) for key in keysym if isinstance(key,str)]) style "ui_choice_keys"
  else:
    frame:
      if isinstance(align,(list,tuple)):
        align align
      elif align:
        xalign align
      xysize size
      background Frame("ui btn_insensitive",14,14)
