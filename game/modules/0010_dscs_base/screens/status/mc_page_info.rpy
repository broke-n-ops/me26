screen status_mc_page_info(act_data):

## 0.11.n inserted global variable references for displaying business and personal skills
  $global mc_business_rate
  $global mc_business_status
  $global mc_business_desc
  $global mc_personal_rate
  $global mc_personal_status
  $global mc_personal_desc
## end of insertion

  $char=find_character(act_data.get("char","mc"))
  text "{=label_text}Status - Info{/}\n" xalign 0.5
  side "l c":
    vbox:
## 0.11.n change 2 lines: xsize 530 into 370 and xalign 0.5 to 0.2
##      xsize 530
      xsize 370
## 0.9.1 - replace 1 line
##      text "{image=mc avatar@470x600}" xalign 0.5
##      add "mc avatar@470x600" xalign 0.5
      add "mc avatar@340x600" xalign 0.20
    vbox:
      use info_row("Name:","{mark}"+char.name+"{/}")
      use vdiv
      for stat in char.stats_order:
        $stat=char.stats[stat]
        if not stat.hidden:
          if stat.stat_type=="mc_stat":
            use info_row(stat.name,"{size=-8}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {mark}"+stat.level_name+"{/}")
      for orifice in ("oral","vaginal","anal"):
        use info_row("{size=-8}Warranty seals broken ({mark}"+orifice+"{/}):{/}","{size=-8}{mark}"+str(mc["warranty_seals_broken_"+orifice])+"{/}{/}")
      use vdiv
      text "Skills"
      python:
        stats=[]
        for stat in char.stats_order:
          stat=char.stats[stat]
          if not stat.hidden:
            if stat.stat_type=="mc_skill":
              stats.append(stat)
      if stats:
        for stat in stats:
          use info_row("{size=-4}{mark}   - "+stat.name+"{/}{/}","{size=-12}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {size=-4}{mark}"+stat.level_name+"{/}{/}")
## 0.11.n 2 lines omitted, will always have at least business and personal skills and frankly all others too
##      else:
##        text "{info}You have no useful skills{/}" xalign 0.5 text_align 0.5
## 0.11.n insert business and personal skills
      use info_row("{size=-4}{mark}   - Business{/}{/}","{size=-12}{color=#888}(n.a.){/}{/} {size=-4}{mark}"+mc_business_rate+"{/}{/}")
      $temp_text=mc_business_status+": "+mc_business_desc.get(mc_business_status)
      use info_row("{size=-10}{info}        - "+temp_text+"{/}{/}")
      use info_row("{size=-4}{mark}   - Personal","{size=-12}{color=#888}(n.a.){/}{/} {size=-4}{mark}"+mc_personal_rate+"{/}{/}")
      $temp_text=mc_personal_status+": "+mc_personal_desc.get(mc_personal_status)
      use info_row("{size=-10}{info}        - "+temp_text+"{/}{/}")
      use vdiv
      use interaction_content(act_data)


