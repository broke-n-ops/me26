screen status_mc_page_reputation(act_data):
  $char=find_character(act_data.get("char","mc"))
  text "{=label_text}Status - Reputation{/}\n" xalign 0.5
  $reputations=[]
  for stat in char.stats_order:
    $stat=char.stats[stat]
    if not stat.hidden:
      if stat.stat_type=="mc_rep":
        $reputations.append(stat)
  text "{size=+8}Personal Reputation{/}"
  if reputations:
    $reputations.sort(key=lambda stat:stat.name.lower())
    $rows=(len(reputations)+1)//2
    grid 2 rows:
      xspacing 100
      allow_underfull True
      for stat in reputations:
        vbox:
          xsize (content_width-100)//2
          use info_row("{mark}"+stat.name+"{/}","{size=-8}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {mark}"+stat.level_name+"{/}")
  else:
    text "{info}You have not made a reputation for yourself yet{/}" xalign 0.5 text_align 0.5
  use vdiv
  $reputations=[]
  for stat in char.stats_order:
    $stat=char.stats[stat]
    if not stat.hidden:
      if stat.stat_type=="rep":
        $reputations.append(stat)
  text "{size=+8}Groups Reputation{/}"
  if reputations:
    $reputations.sort(key=lambda stat:stat.name.lower())
    $rows=(len(reputations)+1)//2
    grid 2 rows:
      xspacing 100
      allow_underfull True
      for stat in reputations:
        vbox:
          xsize (content_width-100)//2
          use info_row("{mark}"+stat.name+"{/}","{size=-8}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {mark}"+stat.level_name+"{/}")
  else:
    text "{info}You have no connections or reputation among groups{/}" xalign 0.5 text_align 0.5
  use vdiv
  use interaction_content(act_data)
