## 0.11.n new status screen for 'Relationships'
screen status_mc_page_relationships(act_data):
  $global mc_so_value
  $global mc_so_status
  $global mc_nst_value
  $global mc_nst_status
  $global mc_rel_desc
  $global gn_store_owner_name
  $global ns_teacher_name
  $global fwb_first_sex
  $global bp_first_sex_teacher
  
  text "{=label_text}Status - Relationships{/}\n" xalign 0.5
  if mc_so_value==0 and mc_nst_value==0:  ## no relationships yet
    use vdiv
    use vdiv
    text "You have no relationships with women."
    use vdiv
  else:
    side "l c":
      vbox:
        xsize 260
        if mc_so_value>0:                      ## you have a relationship with Ruthie
          add "store_owner avatar@210x600" xalign 0.20
          text " "
        if mc_nst_value>0:                     ## you have a relationship with Simone
          add "teacher avatar@210x600" xalign 0.20
      vbox:
        if mc_so_value>0:
          text ""
          text ""
          use info_row("{size=+4}{mark}"+gn_store_owner_name+"{/}{/}","{size=+4}{mark}"+mc_so_status+"{/}{/}")
          if fwb_first_sex==1 and mc_so_status=="Flirting":
            $temp_text="It's lots of fun and maybe I'll get lucky again."  ## custom text if you're flirting and had sex
          else:
            $temp_text=mc_rel_desc.get(mc_so_status)
          use info_row("{size=-2}- "+temp_text+"{/}")

## next line is for debugging only
##          text "[mc_so_value]"

        if mc_nst_value>0:
          if mc_so_value>0:      ## this will be 2nd avatar
            text ""
            text ""
            text ""
            text ""
            text ""
            text ""
            text ""
          else:                  ## this will be 1st avatar
            text ""
            text ""
          use info_row("{size=+4}{mark}"+ns_teacher_name+"{/}{/}","{size=+4}{mark}"+mc_nst_status+"{/}{/}")
          if bp_first_sex_teacher==1 and mc_nst_status=="Flirting":
            $temp_text="It's lots of fun and maybe I'll get lucky again."  ## custom text if you're flirting and had sex
          else:
            $temp_text=mc_rel_desc.get(mc_nst_status)
          use info_row("{size=-2}- "+temp_text+"{/}")

## next line is for debugging only
##          text "[mc_nst_value]"

  use vdiv
  use interaction_content(act_data)