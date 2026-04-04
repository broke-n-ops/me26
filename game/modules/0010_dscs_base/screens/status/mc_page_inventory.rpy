screen status_mc_page_inventory(act_data):
  text "{=label_text}Status - Inventory{/}\n" xalign 0.5
  python:
    inventory=combine_items(workshop.inventory)
    items_by_slots={}
    for item_count,item_n,item in inventory:
      item_slot=find_item_slot(item.slot)
      items_by_slots.setdefault(item_slot.name,[]).append((item_count,item))
  if items_by_slots:
    for item_slot,items in sorted(items_by_slots.items()):
      text "{size=+8}"+item_slot+"{/}"
      
## 0.14 change sort to 'by rating' instead of 'by name' - code provided by 'nobodyzeroone' onF95Zone
## was:   $items.sort(key=lambda (item_count,item):(item.name.lower(),item.id,-item.integrity,len(item.defects)))
      $items.sort(key=lambda item: (item[1].rate.replace("S","\0"),item[1].id,-item[1].integrity,len(item[1].defects)))      
      
      for item_count,item in items:
        python:
          item_msg="{mark}"+item.name+"{/}"
## 0.8.1 changed text from "x14" to ", count: 14" and it will be there even if you have only 1
##          if item_count>1:
##            item_msg+="{size=-8}x{/}{mark}"+str(item_count)+"{/}"
          item_msg+=", count: {mark}"+str(item_count)+"{/}"
          item_msg+=", rate: {mark}"+item.rate+"{/}"
          item_msg+=", integrity: {mark}"+str(item.integrity)+"%{/} {size=-8}{info}("
          if item.integrity_cap==100:
            item_msg+=str(item.integrity_cap)
          else:
            item_msg+="{bad}"+str(item.integrity_cap)+"{/}"
          item_msg+="/100){/}{/}"
        text item_msg
        for defect in item.defects:
          python:
            defect_msg="{size=-8}{bad}"+defect.name+"{/}"
            defect_msg+=", integrity cap: "
            defect_msg+="{mark}" if defect.integrity_cap==100 else "{bad}"
            defect_msg+=str(defect.integrity_cap)+"{/}"
            if defect.repairable:
              defect_msg+=", fix progress: {mark}"+str(defect.fix_progress)+"%{/}"
            else:
              defect_msg+=", {bad}irrepairable{/}"
            defect_msg+="{/}"
          text defect_msg
        $item=None
      $items=None
      use vdiv
  else:
    text "{info}No items are currently stored in the workshop inventory{/}" xalign 0.5 text_align 0.5
  $items_by_slots=None

  use interaction_content(act_data)
