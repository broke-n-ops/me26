screen netconsole_grey_market_request_option(n,option):
  if option[0]=="part":
    $part=option[2]
## new line in 0.9.2
    $partcount=fn_part_count(part.slot,part,part.integrity, part.defects)
    vbox:
      xsize (content_width-100)//2
##modified line in 0.9.2
      text "{mark}#[n]{/} - {mark}[part]{/}  {info}(count: [partcount]){/}"
      text "Rate: {mark}[part.rate]{/}. Integrity: {mark}[part.integrity]%{/}."
      for defect in part.defects:
        text "{size=-8}{bad}[defect]{/}{/}"
  elif option[0]=="bot":
    $bot=option[2]
    vbox:
      xsize (content_width-100)//2
      text "{mark}#[n]{/} - {mark}[bot]{/}"
      text "Model: {mark}[bot.model_name]{/}. Rate: {mark}[bot.rate]{/}."
      $has_defects=" {bad}Has defects.{/}" if bot.chassis.has_defects else ""
      text "Chassis: {mark}[bot.chassis.integrity]%{/}.[has_defects]"
      text "Stability: {mark}[bot.psychocore.status_str]{/}"

screen netconsole_grey_market_request_options(offer,request_options):
  $options=[option for option in request_options if option[0] in ("part","bot")][:12]
  grid 2 1:
    xspacing 100
    xalign 0.5
    vbox:
      spacing 16
      for n,option in enumerate(options):
        if n<(len(options)+1)//2:
          $n+=1
          use netconsole_grey_market_request_option(n,option)
    vbox:
      spacing 16
      for n,option in enumerate(options):
        if n>=(len(options)+1)//2:
          $n+=1
          use netconsole_grey_market_request_option(n,option)
