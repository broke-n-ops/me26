screen workshop_replace_part_info(part,part_options,show_descriptions=True):
  grid 2 1:
    xspacing 100
    vbox:
      xsize (content_width-50)//2
      text "Currently used part" xalign 0.5
      use vdiv
      use chassis_part_info(None,part,show_descriptions)
    vbox:
      xsize (content_width-50)//2
      text "Possible replacements" xalign 0.5
      use vdiv
      for part_n,part_option in enumerate(part_options):
        if part_n:
          use vdiv
        $part_n+=1
## 0.8.0 inserted next line and modified line after - 0.8.1 changed (12 ea) to (x12)
        $part_count=fn_part_count(part_option.slot,part_option.id,part_option.integrity,part_option.defects)
        use chassis_part_info(None,part_option,show_descriptions,slot_text="#"+str(part_n)+"  {info}{size=-8}(x"+str(part_count)+"){/}{/}")
