default persistent.game_notifications={}

init -999 python:
  notification_categories={}

  def game_notification(msg,notification_category,notification_msg_category=None):
    if msg:
      mode=notification_categories.get(notification_category,("---","normal"))[1]
      mode=(persistent.game_notifications or {}).get(notification_category,mode)
      if mode=="small":
        msg="{size=-8}"+msg+"{/}"
      if mode!="hidden":
        notify(msg,category=notification_msg_category)

screen preferences_notifications():
  style_prefix "preferences"
  python:
    categories=[(id,title,default) for id,(title,default) in notification_categories.items()]
    categories.sort(key=lambda cat: cat[1].lower())
    for cat_id,cat_title,cat_default in categories:
      persistent.game_notifications.setdefault(cat_id,cat_default)
  vbox:
    spacing 16
    for cat_id,cat_title,cat_default in categories:
      side "c r":
        xfill True
        text cat_title yalign 0.5
        hbox:
          align (1.0,0.5)
          for title,value in [("Normal","normal"),("Small","small"),("Hidden","hidden")]:
            use ui_choice(SetDict(persistent.game_notifications,cat_id,value),title=title,size=pref_btn_size,style_suffix="med")
#  null height 16
#  text "{info}Changes will be visible during the next interaction{/}" xalign 0.5 text_align 0.5
