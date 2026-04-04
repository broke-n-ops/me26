screen status_mc_page_expertise(act_data):
  $char=find_character(act_data.get("char","mc"))
  text "{=label_text}Status - Expertise{/}\n" xalign 0.5
  python:
    models=[]
    parts=[]
    for stat in char.stats_order:
      stat=char.stats[stat]
      if stat.stat_type=="expertise_bot_model":
        models.append(stat)
      elif stat.stat_type=="expertise_bot_part":
        parts.append(stat)
  text "{size=+8}Bot Models Expertise{/}"
  if models:
    $models.sort(key=lambda stat:stat.name.lower())
    $rows=(len(models)+1)//2
    grid 2 rows:
      xspacing 100
      allow_underfull True
      for stat in models:
        vbox:
          xsize (content_width-100)//2
          use info_row("{mark}"+stat.name+"{/}","{size=-8}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {mark}"+stat.level_name+"{/}")
  else:
    text "{info}You have no specific expertise in bot models{/}" xalign 0.5 text_align 0.5
  use vdiv
  text "{size=+8}Bot Parts Expertise{/}"
  if parts:
    $parts.sort(key=lambda stat:stat.name.lower())
    $rows=(len(parts)+1)//2
    grid 2 rows:
      xspacing 100
      allow_underfull True
      for stat in parts:
        vbox:
          xsize (content_width-100)//2
          use info_row("{mark}"+stat.name+"{/}","{size=-8}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {mark}"+stat.level_name+"{/}")
  else:
    text "{info}You have no specific expertise in bot parts{/}" xalign 0.5 text_align 0.5
  use vdiv
  use interaction_content(act_data)
