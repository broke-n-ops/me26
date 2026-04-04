define pref_btn_size=(180,56)

style preferences_title is cs_header

screen preferences():
  style_prefix "preferences"
  tag menu
  $pages=[
    ("system","System","System settings"),
    ("notifications","Notifications","Notification settings"),
    ("game","Game","Game settings"),
    ]
  default preferences_page="system"
  use game_menu(scroll=True):
    vbox:
      xsize content_width
      xalign 0.5
      null height 32
      text [title for id,name,title in pages if id==preferences_page][0] style "preferences_title"
      use vdiv
      hbox:
        xalign 0.5
        for id,name,title in pages:
          use ui_choice(SetScreenVariable("preferences_page",id),title=name,size=pref_btn_size,style_suffix="med")
      use vdiv
      $renpy.use_screen("preferences_"+preferences_page)
      null height 32
