screen workshop_quirks_info(bot,page=None,add_number=False):
  python:
    bot=find_character(bot)
    traits=[trait for trait in bot.psychocore.traits if not trait.hidden]
    if page is not None:
      traits=traits[page*workshop_bot_quirks_per_page:(page+1)*workshop_bot_quirks_per_page]
    rows=(len(traits)+1)//2
  grid 2 rows:
    allow_underfull True
    xspacing 100
    for trait_n,trait in enumerate(traits):
      vbox:
        xsize (content_width-100)//2
        python:
          if add_number:
            title="{mark}#"+str(trait_n+1)+"{/} - {"+trait.trait_color+"}"+trait.name+"{/}"
          else:
            title="{"+trait.trait_color+"}"+trait.name+"{/}"
          desc=trait.description
          if trait.inherent:
            desc+=" {mark}Inherent.{/}"
          elif trait.automatic:
            desc+=" {mark}Automatic.{/}"
        use info_row(title,"Level: {mark}"+str(trait.progress)+"{/}")
        text "{size=-8}{info}"+desc+"{/}{/}"
        use vdiv
