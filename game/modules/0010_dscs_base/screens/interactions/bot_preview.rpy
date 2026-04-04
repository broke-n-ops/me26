screen bot_preview_info(bot,info):
  use info_row("Name:","{mark}"+bot.name+"{/}")
  use vdiv
  use info_row("Model:","{mark}"+bot.model_name+"{/}")
  if game.difficulty==1 or mc.has_stat("expertise_"+bot.model_id):
    use info_row("Rate:","{mark}"+bot.rate+"{/}")
  elif not game.hardcore:
    use info_row("Rate:","{info}?{/}")

screen bot_preview_psychocore(bot,info):
  use info_row("PsychoCore:",bot.psychocore.status_str+"/{mark}"+str(bot.psychocore.stability)+"%{/}")

screen bot_preview_chassis(bot,info):
  use info_row("Chassis integrity:","{mark}"+str(bot.chassis.integrity)+"%{/}")
  if not "hide_warranty_seals" in info:
     for orifice in ("oral","vaginal","anal"):
       if orifice!="vaginal" or bot.gender!="male":
         $seal=bot["warranty_seal_"+orifice]
         if seal=="broken by mc":
           use info_row("{size=-8}Warranty seal ("+orifice+"):{/}","{size=-8}{info}Broken by you{/}{/}")
         elif seal:
           use info_row("{size=-8}Warranty seal ("+orifice+"):{/}","{size=-8}{mark}Intact{/}{/}")
         else:
           use info_row("{size=-8}Warranty seal ("+orifice+"):{/}","{size=-8}{info}Broken{/}{/}")

screen bot_preview_stats(bot,info):
  for stat in bot.stats_order:
    $stat=bot.stats[stat]
    if not stat.hidden:
      if stat.stat_type=="bot_stat":
        use info_row(stat.name+":","{size=-8}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {mark}"+stat.level_name+"{/}")

screen bot_preview_skills(bot,info):
  text "Skills"
  python:
    stats=[find_stat(stat_id) for stat_id in bot.stats_order]
    stats=[stat for stat in stats if not stat.hidden and stat.stat_type=="bot_skill"]
    stats.sort(key=lambda stat:stat.name.lower())
  if stats:
    for stat in stats:
      $stat=getattr(bot,stat.id)
      use info_row("{mark}"+stat.name+"{/}","{size=-8}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {mark}"+stat.level_name+"{/}")
  else:
    text "{info}[bot] has no useful skills{/}" xalign 0.5 text_align 0.5

screen bot_preview_traits(bot,info):
  text "Traits"
  $traits=[trait for trait in bot.psychocore.traits if not trait.hidden]
  if traits:
    for trait in traits:
      python:
        title="{"+trait.trait_color+"}"+trait.name+"{/}"
        desc=trait.description
        if trait.inherent:
          desc+=" {mark}Inherent.{/}"
      use info_row(title,"Level: {mark}"+str(trait.progress)+"{/}")
      text "{size=-8}{info}"+desc+"{/}{/}"
  else:
    text "{info}[bot] has no known traits{/}" xalign 0.5 text_align 0.5

screen bot_preview_parts(bot,info):
  $show_description="parts_desc" in info
  $show_defects="defects" in info
  grid 2 1:
    xspacing 100
    vbox:
      xsize (content_width-100)//2
      for part_slot_n,part_slot in enumerate(bot.outfit_slots):
        if part_slot_n<(len(bot.outfit_slots)-1)//2:
          use chassis_part_info(bot,part_slot,show_description,show_defects,"auto")
          use vdiv
    vbox:
      xsize (content_width-100)//2
      for part_slot_n,part_slot in enumerate(bot.outfit_slots):
        if part_slot_n>=(len(bot.outfit_slots)-1)//2:
          use chassis_part_info(bot,part_slot,show_description,show_defects,"auto")
          use vdiv

screen bot_preview(bot,info=None):
  python:
    info=info or ("info",)
    bot=find_character(bot)
  vbox:
    xfill True
    side "l c":
      vbox:
        xsize 440
        add "bots [bot.model_id] avatar@400x600" xalign 0.5
      vbox:
        if "info" in info:
          use bot_preview_info(bot,info)
        if "chassis" in info:
          use vdiv
          use bot_preview_chassis(bot,info)
        if "psychocore" in info:
          use vdiv
          use bot_preview_psychocore(bot,info)
        if "stats" in info:
          use vdiv
          use bot_preview_stats(bot,info)
        if "skills" in info:
          use vdiv
          use bot_preview_skills(bot,info)
        if "traits" in info:
          use vdiv
          use bot_preview_traits(bot,info)
    if "parts" in info:
      use vdiv
      use bot_preview_parts(bot,info)
