style ui_choice_title_small is ui_choice_title:
  size 22

screen quick_menu():
  $qbtn_size=(374//4,52)
  grid 4 1:
    align (0.5,0.5)
    use ui_choice(Rollback(),title="Back",key="B",size=qbtn_size,style_suffix="small",keyboard_focus=False)
    use ui_choice([SelectedIf(False),QuickSave()],title="Q.Save",key="quick_save",size=qbtn_size,style_suffix="small",keyboard_focus=False)
    use ui_choice(QuickLoad(confirm=persistent.confirm_quick_load),title="Q.Load",key="quick_load",size=qbtn_size,style_suffix="small",keyboard_focus=False)
    use ui_choice(ShowMenu("save"),title="Menu",key="lesser_game_menu",size=qbtn_size,style_suffix="small",keyboard_focus=False)
