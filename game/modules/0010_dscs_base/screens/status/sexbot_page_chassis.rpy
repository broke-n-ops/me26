screen status_sexbot_page_chassis_status(char,show_descriptions=True):
  $char=find_character(char)
  python:
    part=char.chassis.most_damaged_part
    mark_slot=part.slot.id if part.integrity<100 else None
    if char.chassis.integrity:
      entries=[("Chassis integrity","{mark}"+str(char.chassis.integrity)+"%{/}")]
    else:
      entries=[("Chassis integrity","{bad}disabled{/}")]
    for part_slot_n,part_slot in enumerate(char.outfit_slots):
      entries.append(part_slot)
  grid 2 1:
    xspacing 100
    vbox:
      xsize (content_width-100)//2
      use vdiv
      for n,entry in enumerate(entries):
        if n<=(len(entries)-1)//2:
          if isinstance(entry,str):
            use chassis_part_info(char,entry,show_descriptions,slot_mark=most_damaged_part_mark if entry==mark_slot else "")
          else:
            use info_row(entry[0],entry[1])
          use vdiv
    vbox:
      xsize (content_width-100)//2
      use vdiv
      for n,entry in enumerate(entries):
        if n>(len(entries)-1)//2:
          if isinstance(entry,str):
            use chassis_part_info(char,entry,show_descriptions,slot_mark=most_damaged_part_mark if entry==mark_slot else "")
          else:
            use info_row(entry[0],entry[1])
          use vdiv

screen status_sexbot_page_chassis(act_data):
  $char=find_character(act_data["char"])
  text "{=label_text}Status - Chassis{/}\n" xalign 0.5
  use status_sexbot_page_chassis_status(char)
  use interaction_content(act_data)
