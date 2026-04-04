style chassis_part_description:
  size 20
  xalign 0.5
  text_align 0.5

style chassis_part_defect:
  color "#F00"
  size 20
  xalign 0.5
  text_align 0.5

init python:
  def chassis_part_status_str(part,count=1,show_rate=True):
    rv="{bad}*{/}" if part.defects else ""
    rv+="{size=-8}{info}("+str(part.integrity)+"%){/}{/} "
    rv+="{bad}" if part.is_disabled else "{mark}"
    rv+=part.name+"{/}"
    if count>1:
      rv+="{size=-8}x{/}{mark}"+str(count)+"{/}"
    if show_rate=="auto":
      if game.difficulty==1 or mc.has_stat("expertise_"+part.id):
        rv+=" {size=-8}{info}("+part.rate+"){/}{/}"
      elif not game.hardcore:
        rv+=" {size=-8}{info}(?){/}{/}"
    elif show_rate:
      rv+=" {size=-8}{info}("+part.rate+"){/}{/}"
    return rv

screen chassis_part_info(char,part_slot,show_descriptions=True,show_defects=True,show_rate=True,slot_mark="",slot_text=None):
  vbox:
    xfill True
    python:
      part_count=1
      if char is None:
        part=part_slot
        if isinstance(part,(list,tuple)):
          part_count,part_inv_n,part=part
        slot=find_item_slot(part.slot)
      else:
        slot=find_item_slot(part_slot)
        part=char.item_on_slot(slot)
    if part:
      if slot_text is None:
        $slot_text=slot.name
      use info_row(slot_text+slot_mark,chassis_part_status_str(part,part_count,show_rate))
      if show_descriptions:
        text "{info}"+part.description+"{/}" style "chassis_part_description"
      if show_defects:
        for defect in part.defects:
          if defect.repairable:
            $defect_repair=" {info}(fixed "+str(defect.fix_progress)+"%){/}"
          else:
            $defect_repair=" {info}(irrepairable){/}"
          $disabling=" {info}(disabling){/}" if defect.disabling else ""
          text defect.description+defect_repair+disabling style "chassis_part_defect"
    else:
      use info_row(slot.name,"{bad}missing{/}")

define most_damaged_part_mark="{bad}*{/}"

screen chassis_parts_info(parts,show_descriptions=True,item_caption=None):
  grid 2 1:
    xspacing 100
    vbox:
      xsize (content_width-100)//2
      for part_n,part in enumerate(parts):
        if part:
          if part_n<len(parts)//2:
            if item_caption:
              $caption=item_caption%(part_n+1) if "%s" in item_caption else item_caption
              text caption xalign 0.5
            use chassis_part_info(None,part,show_descriptions)
            use vdiv
    vbox:
      xsize (content_width-100)//2
      for part_n,part in enumerate(parts):
        if part:
          if part_n>=len(parts)//2:
            if item_caption:
              $caption=item_caption%(part_n+1) if "%s" in item_caption else item_caption
              text caption xalign 0.5
            use chassis_part_info(None,part,show_descriptions)
            use vdiv
