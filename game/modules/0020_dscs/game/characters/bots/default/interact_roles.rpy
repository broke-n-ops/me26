label interact_default_roles(bot):
  header "[bot] - Roles"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [bot.model_id] avatar@400x600}"
  $act.set_block("c")
  $roles=sorted(bot.roles[:],key=lambda role:(role.list_priority,role.name.lower()))
  $roles=[role for role in roles if not role.hidden]
  if roles:
    if bot not in home.sexbots:
      "{mark}[bot]{/} is stored at offline storage and {bad}not doing [bot.hisher] roles{/}."
    "[bot.hisher!c] current roles:"
    while roles:
      $role=roles.pop(0)
      ""
      "{mark}[role]{/} - [role.description!i]"
      $role_tags=[modded_bot_role_tags[role_tag] for role_tag in role.role_tags.keys()]
      $role_tags.sort(key=lambda role_tag: role_tag["list_priority"])
      while role_tags:
        $role_tag=role_tags.pop(0)
        $role_tag=role_tag["description"]
        "{size=-8}{info}[role_tag!i]{/}{/}"
  else:
    "{mark}[bot]{/} does not have any roles assigned."
  $act.end_block()
  $roles=sorted(bot_roles_cls_by_id.items(),key=lambda role:(role[1].list_priority,role[1].default_name.lower()))
  $roles=[(role_id,role) for (role_id,role) in roles if not role.hidden and role.selectable]
  while roles:
    $role_id,role=roles.pop(0)
    if not bot.action_allowed("change_role"):
      choice(None,hint="{hint}not allowed{/}") "[role]"
    else:
##      $print "role_id: ",role_id
      if role_id=="senior_techie":
        interact("role_management,"+role_id,hint="{info}(parts){/}") "[role]"
      elif role_id=="master_techie":
        interact("role_management,"+role_id,hint="{info}(bots){/}") "[role]"
      else:
        interact("role_management,"+role_id) "[role]"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  $role=None
  return

label interact_default_role_management(bot,role_id):
  python:
    role=find_bot_role_cls(role_id)
    role_reqs=role.check_requirements(bot)[1][:]
  header "[bot] - [role]"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [bot.model_id] avatar@400x600}"
  $act.set_block("c")
  "[role.description!i]"
  $role_tags=[modded_bot_role_tags[role_tag] for role_tag in role.role_tags.keys()]
  $role_tags.sort(key=lambda role_tag: role_tag["list_priority"])
  while role_tags:
    $role_tag=role_tags.pop(0)
    $role_tag=role_tag["description"]
    "{size=-8}{info}[role_tag!i]{/}{/}"
  ""
  "Requirements:"
  if role_reqs:
    while role_reqs:
      $req_met,req_desc=role_reqs.pop(0)
      if req_met:
        "- [req_desc]"
      else:
        "- [req_desc] {bad}{size=-8}(req not met){/}{/}"
  else:
    "{info}This role has no requirements{/}"
  $act.end_block()
  if bot.can_remove_role(role_id):
    interact("^remove_role,"+role_id,hint="Remove role") "[role]"
  elif bot.can_add_role(role_id):
    interact("^add_role,"+role_id,hint="Add role") "[role]"
  elif len(bot.roles)>=bot.psychocore.max_roles:
    choice(None,hint="{hint}low autonomy{/}") "[role]"
  else:
    choice(None,hint="{bad}reqs not met{/}") "[role]"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  $role=None
  return

label interact_default_add_role(bot,role_id):
  $role=find_bot_role_cls(role_id)
  header "[bot] - Add role"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [bot.model_id] avatar@400x600}"
  $act.set_block("c")
  if renpy.has_label("bot_role_add_"+role_id):
    call expression "bot_role_add_"+role_id pass (bot,)
  else:
    "You explain to [bot] [bot.hisher] role as {mark}[role]{/}."

## 0.10.n set role just changed tag
##  $print "role_id: ",role_id

  if now("morning"):
    $start_time="this afternoon"
  elif now("afternoon"):
    $start_time="this evening"
  elif now("evening"):
    if role_id=="housekeeper" or role_id=="mission_manager":  ## roles that works at night (bedroom toy handled below)
      $start_time="tonight"
    else:                                                     ## all other roles (not working at night)
      $start_time="tomorrow morning"
  else:                                                       ## must be night
    $start_time="tomorrow morning"
  if role_id=="bedroom_toy":                                  ## bedroom toy role only at night, overwrite start time
    $start_time="tonight"
  ""
  "[bot] will begin performing [bot.hisher] new role {mark}[start_time]{/}."

  if role_id=="senior_techie":
    $bot.st_just_assigned=1
  elif role_id=="master_techie":
    $bot.mt_just_assigned=1
  elif role_id=="clerk":
    $bot.clerk_just_assigned=1
  elif role_id=="techie":
    $bot.tech_just_assigned=1
  elif role_id=="shopkeeper":
    $bot.shpkpr_just_assigned=1
  elif role_id=="mission_manager":
    $bot.mgr_just_assigned=1
  elif role_id=="bot_trainer":    ## 0.12.n
    $bot.bt_just_assigned=1

  $bot.add_role(role_id)
  $act.end_block()
  choice("<<<") "Continue"
  $role=None
  return

label interact_default_remove_role(bot,role_id):
  $role=find_bot_role_cls(role_id)
  header "[bot] - Remove role"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [bot.model_id] avatar@400x600}"
  $act.set_block("c")
  if renpy.has_label("bot_role_remove_"+role_id):
    call expression "bot_role_remove_"+role_id pass (bot,)
  else:
    "You tell [bot] [bot.heshe] is no longer going to be {mark}[role]{/}."
  $bot.remove_role(role_id)
  $act.end_block()
  choice("<<<") "Continue"
  $role=None
  return
