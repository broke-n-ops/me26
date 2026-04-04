screen status_sexbot_page_info(act_data):
  $char=find_character(act_data["char"])
  text "{=label_text}Status - Info{/}\n" xalign 0.5
  side "l c":
    vbox:
      xsize 530

## 0.9.1 - replace 1 line
##      text "{image=bots [char.model_id] avatar@470x600}" xalign 0.5
      add "bots [char.model_id] avatar@470x600" xalign 0.5

    vbox:
      use info_row("Name:","{mark}"+char.name+"{/}")
      use vdiv
      use info_row("Rate:","{mark}"+char.rate+"{/}")
      use vdiv
      use info_row("Chassis integrity:","{mark}"+str(char.chassis.integrity)+"%{/}")
      for orifice in ("oral","vaginal","anal"):
        if orifice!="vaginal" or char.gender!="male":
          $seal=char["warranty_seal_"+orifice]
          if seal=="broken by mc":
            use info_row("{size=-8}Warranty seal ("+orifice+"):{/}","{size=-8}{info}Broken by you{/}{/}")
          elif seal:
            use info_row("{size=-8}Warranty seal ("+orifice+"):{/}","{size=-8}{mark}Intact{/}{/}")
          else:
            use info_row("{size=-8}Warranty seal ("+orifice+"):{/}","{size=-8}{info}Broken{/}{/}")
      use vdiv
      use info_row("PsychoCore:",char.psychocore.status_str+"/{mark}"+str(char.psychocore.stability)+"%{/}")
      use vdiv
      for stat in char.stats_order:
        $stat=char.stats[stat]
        if not stat.hidden:
          if stat.stat_type=="bot_stat":
            use info_row(stat.name+":","{size=-8}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {mark}"+stat.level_name+"{/}")
      use vdiv
      text "Skills"
      python:
        stats=[find_stat(stat_id) for stat_id in char.stats_order]
        stats=[stat for stat in stats if not stat.hidden and stat.stat_type=="bot_skill"]
        stats.sort(key=lambda stat:stat.name.lower())
      if stats:
        for stat in stats:
          $stat=getattr(char,stat.id)
          use info_row("{mark}"+stat.name+"{/}","{size=-8}{color=#888}("+"{}%".format(stat.progress_percent)+"){/}{/} {mark}"+stat.level_name+"{/}")
      else:
        text "{info}[char] has no useful skills{/}" xalign 0.5 text_align 0.5
      use vdiv
      text "Traits"
      $traits=[trait for trait in char.psychocore.traits if not trait.hidden]
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
        text "{info}[char] has no known traits{/}" xalign 0.5 text_align 0.5
## 0.13.n add DNS, Manage, Trainer, Trainee
      if char.do_not_sell:
        $tmp_string="{mark}ON{/}"
      else:
        $tmp_string="{mark}OFF{/}"
      use vdiv
      use info_row("Do Not Sell (DNS):",tmp_string)
      if char.allow_manage:
        $tmp_string="{mark}YES{/}"
      else:
        $tmp_string="{mark}NO{/}"
      use vdiv
      use info_row("Allow Management :",tmp_string)
      if char.trainee_subject=="never":
        $tmp_string="{mark}not set{/}"
      else:
        $tmp_string="{mark}"+char.trainee_subject+"{/}"
      use vdiv
      use info_row("Trainee Subject:",tmp_string)
      python:
        bot_is_trainer=False
        for role in char.roles:
          if role.id=="bot_trainer":
            bot_is_trainer=True
##            print "FOUND TRAINER ROLE"
      if bot_is_trainer:
        if char.trainer_subject=="":
          $tmp_string="{mark}not set{/}"
        else:
          $tmp_string="{mark}"+char.trainer_subject+"{/}"
        use vdiv
        use info_row("Trainer Subject:",tmp_string)
## 0.14.n add scavenge experience
      if char.scavenge_success!=0:           ## if no success don't display anything
        if char.scavenge_success<=10:
          $tmp_string="{mark}Novice{/}"
        elif char.scavenge_success<=25:
          $tmp_string="{mark}Competent{/}"
        elif char.scavenge_success<=50:
          $tmp_string="{mark}Proficient{/}"
        else:  ## 51 or more
          $tmp_string="{mark}Expert{/}"
        use vdiv
        use info_row("Scavenging:",tmp_string)      
##  START OF ADDITION FOR UFC MISSION
      $ufc_fights=char.ufc_wins+char.ufc_losses
      if ufc_fights>0:
        use vdiv
        use info_row("UFC Fight Record:","{mark}"+char.ufc_record+"{/}")
##  END OF ADDITION FOR UFC MISSION
      use interaction_content(act_data)