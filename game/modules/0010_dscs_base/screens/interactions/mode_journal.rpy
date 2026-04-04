style mode_journal_left_text is cs_center

screen mode_journal_page_btn(page,title,hint=None,key=None):
  fixed:
    fit_first True
    xalign 0.5
    use ui_choice("mode_journal:"+page,title=title,hint=hint,key=key,size=(320,72),prepare=True,keyboard_focus=False)

define journal_pages=[("quests","Quests"),("tasks","Tasks"),("notes","Notes")]

screen mode_journal_left_side(act_data):
  fixed:
    xsize 384
    use ui_frame(scroll=True):
      use ui_scrollbox:
        style_prefix "mode_journal_left"
        python:
          pages=[page[0] for page in journal_pages]
          page=act_data["journal_page"]
          next_page=None
          if len(pages)>1:
            if page in pages:
              next_page=pages[(pages.index(page)+1)%len(pages)]
            else:
              next_page=pages[0]
        null height 32
        for n,(page,title) in enumerate(journal_pages):
          if n:
            use vdiv
          use mode_journal_page_btn(page,title,key=("K_TAB" if next_page==page else None))
        null height 32

style journal_quest_name:
  xalign 0.5
  text_align 0.5
  size 36

style journal_quest_desc:
  first_indent 60
  newline_indent True

screen mode_journal_content(act_data):
  python:
    page,title=[(page,title) for page,title in journal_pages if page==act_data["journal_page"]][0]
    active_quests=[]
    finished_quests=[]
    failed_quests=[]
## 0.10.n inserted 1 line to support future quest list (quests not started yet)
    future_quests=[]                                                  
    for quest_id in quests_manager.quests_start_order:
      quest=find_quest(quest_id)
      if quest and quest.quest_type==page[:-1] and not quest.hidden:
        if quest.finished:
          finished_quests.append(quest)
        elif quest.failed:
          failed_quests.append(quest)
        else:
          active_quests.append(quest)
## 0.10.n inserted 5 lines to support future quest list
    for quest_name in all_quests:         
      quest_test=find_quest(quest_name)
      if quest_test and quest_test.quest_type==page[:-1]:
        if not quest_test.started:
          future_quests.append(quest_test)
  side "c b":
    xsize 1108
    yfill True
    spacing 8
    use ui_frame:
      use ui_scrollbox(True,id="interaction_default_content",update=update_interaction,main_viewport=True):
        vbox:
          xsize content_width
          xalign 0.5
          null height 32
          label "Journal - [title]" xalign 0.5
          use vdiv
## 0.10.n added 'future_quests' to the next 2 lines
          if active_quests or finished_quests or failed_quests or future_quests:
## 0.11.n stop displaying 'failed quests' information, it's not possible to have a failed quest
##            for quests_status,quests_list in [("Active",active_quests),("Finished",finished_quests),("Failed",failed_quests),("Future",future_quests)]:
            for quests_status,quests_list in [("Active",active_quests),("Finished",finished_quests),("Future",future_quests)]:
              if page=="quests":
                label quests_status+" "+page xalign 0.5
              if quests_list:
                for n,quest in enumerate(quests_list):
                  if n:
                    use vdiv
## 0.10.n inserted 1 line and indented following line to omit display of future 'notes' quests
                  if page!="notes" or quests_status!="Future":
                    text "{mark}[quest.name]{/}" style "journal_quest_name"
## 0.10.n inserted 1 line and indented 2 afterwards to NOT show descriptions for future quests
                  if quests_status!="Future":
                    $desc="\n".join([s.strip() for s in quest.description.strip().splitlines()])
                    text desc style "journal_quest_desc"
              elif page=="quests":
                text "{info}No "+quests_status.lower()+" "+page+"{/}" xalign 0.5
              use vdiv
          else:
            text "{info}No "+title.lower()+"{/}" xalign 0.5
            use vdiv
          use interaction_content(act_data)
          null height 32
    python:
      choices=[None]*18
      choices[17]=choice_info("<<<leave_mode",pos=17,key="cancel")
    use interaction_choices(act_data,choices)

screen mode_journal(act_data):
  style_prefix "mode_journal"
  hbox:
    align (0.5,0.5)
    ysize (1080-32)
    spacing 8
    use mode_journal_left_side(act_data)
    use mode_journal_content(act_data)
    side "t c":
      xsize 384
      yfill True
      spacing 8
      use ui_frame:
        use quick_menu
      use status_side_mc(act_data)
