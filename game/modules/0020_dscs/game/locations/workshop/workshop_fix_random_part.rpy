init python:
  def workshop_get_repairable_parts():
    parts=[]
    for part_n,part in enumerate(workshop.inventory):
      defects=[(defect_n,defect) for defect_n,defect in enumerate(part.defects)]
      if defects:
        defects.sort(key=lambda x: (100-x[1].integrity_cap,x[1].fix_progress))
        if defects[-1][1].repairable:
          parts.append(("defect",part_n,defects[-1][0]))
          continue
      if part.integrity<part.integrity_cap:
        parts.append(("repair",part_n))
    return parts

  def workshop_get_random_repairable_part():
    parts=workshop_get_repairable_parts()
    return randchoice(parts) if parts else None

  def label_workshop_fix_random_part_action_info(**kwargs):
    if workshop_get_random_repairable_part():
      kwargs["cost"]=[("energy",1)]
    else:
      kwargs["action"]=None
      kwargs["hint"]="{hint}no repairable parts{/}"
    return kwargs

label workshop_fix_random_part:
  $workshop_random_tinker_target=workshop_get_random_repairable_part()
  if workshop_random_tinker_target:
    "You check your inventory and select random damaged part."
    ""
    if workshop_random_tinker_target[0]=="repair":
      return "workshop_fix_part:"+str(workshop_random_tinker_target[1])+",workshop_fix_random_part"
    else:
      return "workshop_fix_part_defect:"+str(workshop_random_tinker_target[1])+","+str(workshop_random_tinker_target[2])+",workshop_fix_random_part"
  else:
    return "<<<"
