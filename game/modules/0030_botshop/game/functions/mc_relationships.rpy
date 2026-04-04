## Relationships - Ruthie and Simone

##  Scale used for 'Value' - 'Status'
##    0-10    - Acquaintance
##    11-30   - Friend
##    31-60   - Flirting
##    61-100  - Friends with Benefits
##    101-140 - Lovers

## Initialize variables

init python:
  mc_so_value=0       ## value with store owner using scale above
  mc_so_status=""     ## status with store owner, starts null
  mc_nst_value=0      ## value with teacher using scale above
  mc_nst_status=""
  mc_rel_desc={
    "Lovers": "Partners for now, maybe for life, and the sex is great.",
    "Friends with Benefits": "Into each other for now and the sex is great.",
    "Flirting": "It's lots of fun and maybe I'll get lucky one day.",
    "Friend": "Having fun with each other, might lead to something.",
    "Acquaintance": "We've met but we don't know each other very well."}
    
## 0.15.n add day counters for relationship loss with both Simone and Ruthie (simplify her system)
  mc_nst_date_counter=0    ## add 1 every day you do not date Simone - at 10 days reminder warning - at 14 days lose 1 relationship point and reset counter
  mc_so_date_counter=0     ## add 1 every day you do not date Ruthie - at 4 days reminder warning - at 5 days lose 1 relationship point and reset counter

## FUNCTIONS

label mc_update_relation(u_name,u_amount,u_silent):  ## called whenever a relationship is increased or decreased
  $global gn_store_owner_name
  $global mc_so_value
  $global mc_so_status
  $global ns_teacher_name
  $global mc_nst_value
  $global mc_nst_status
  $local_text=""                        ## start with empty string
  $local_status_change=0                ## clear flag for status change
  if u_name==gn_store_owner_name:

##    $print "updating mc_so_value: ",mc_so_value
##    $print "updating mc_so_status: ",mc_so_status

    $mc_so_value+=u_amount         ## update value
    if mc_so_value<0:                   ## 0 is min
      $mc_so_value=0
    elif mc_so_value>140:               ## 140 is max
      $mc_so_value=140

##    $print "new mc_so_value: ",mc_so_value
##    $print "new mc_so_status: ",mc_so_status

    if mc_so_status=="":                ## haven't met yet
      $mc_so_status="Acquaintance"
      $local_status_change=2            ## special case for first meeting
    elif mc_so_status=="Acquaintance":
      if mc_so_value>10:
        $mc_so_status="Friend"
        $local_status_change=1
    elif mc_so_status=="Friend":
      if mc_so_value<11:
        $mc_so_status="Acquaintance"
        $local_status_change=-1
      if mc_so_value>30:
        $mc_so_status="Flirting"
        $local_status_change=1
    elif mc_so_status=="Flirting":
      if mc_so_value<31:
        $mc_so_status="Friend"
        $local_status_change=-1
      if mc_so_value>60:
        $mc_so_status="Friends with Benefits"
        $local_status_change=1
    elif mc_so_status=="Friends with Benefits":
      if mc_so_value<61:
        $mc_so_status="Flirting"
        $local_status_change=-1
      if mc_so_value>100:
        $mc_so_status="Lovers"
        $local_status_change=1
    elif mc_so_status=="Lovers":
      if mc_so_value<101:
        $mc_so_status="Friends with Benefits"
        $local_status_change=-1
    if local_status_change!=0 and not u_silent:  ## if silent no text displayed, not used in 0.11.n
      if local_status_change==2:                 ## first meeting is special case
        $local_text= "{i}{mark}You met {good}[gn_store_owner_name]{/} who is now your {good}[mc_so_status]{/}{/}{/}"
        "{size=-20} "                            ## minimal line feed
        "[local_text]"                           ## display message if status changed
      else:
        if local_status_change==1:
          $local_text="improved to"
        else:
          $local_text="reverted to"
        $local_text= "{i}{mark}Your relationship with {good}[gn_store_owner_name]{/} "+local_text+" {good}[mc_so_status]{/}{/}{/}"
        "{size=-20} "                            ## minimal line feed
        "[local_text]"                           ## display message if status changed
  elif u_name==ns_teacher_name:

##    $print "updating mc_nst_value: ",mc_nst_value
##    $print "updating mc_nst_status: ",mc_nst_status

    $mc_nst_value+=u_amount         ## update value
    if mc_nst_value<0:                   ## 0 is min
      $mc_nst_value=0
    elif mc_nst_value>140:               ## 140 is max
      $mc_nst_value=140

##    $print "new mc_nst_value: ",mc_nst_value
##    $print "new mc_nst_status: ",mc_nst_status

    if mc_nst_status=="":                ## haven't met yet
      $mc_nst_status="Acquaintance"
      $local_status_change=2             ## special case for first meeting
    elif mc_nst_status=="Acquaintance":
      if mc_nst_value>10:
        $mc_nst_status="Friend"
        $local_status_change=1
    elif mc_nst_status=="Friend":
      if mc_nst_value<11:
        $mc_nst_status="Acquaintance"
        $local_status_change=-1
      if mc_nst_value>30:
        $mc_nst_status="Flirting"
        $local_status_change=1
    elif mc_nst_status=="Flirting":
      if mc_nst_value<31:
        $mc_nst_status="Friend"
        $local_status_change=-1
      if mc_nst_value>60:
        $mc_nst_status="Friends with Benefits"
        $local_status_change=1
    elif mc_nst_status=="Friends with Benefits":
      if mc_nst_value<61:
        $mc_nst_status="Flirting"
        $local_status_change=-1
      if mc_nst_value>100:
        $mc_nst_status="Lovers"
        $local_status_change=1
    elif mc_nst_status=="Lovers":
      if mc_nst_value<101:
        $mc_nst_status="Friends with Benefits"
        $local_status_change=-1
    if local_status_change!=0 and not u_silent:   ## if silent no text displayed, not used in 0.11.n
      if local_status_change==2:                  ## first meeting is special case
        $local_text= "{i}{mark}You met {good}[ns_teacher_name]{/} who is now your {good}[mc_nst_status]{/}{/}{/}"
        "{size=-20} "                             ## minimal line feed
        "[local_text]"                            ## display message if status changed
      else:
        if local_status_change==1:
          $local_text="improved to"
        else:
          $local_text="reverted to"
        $local_text= "{i}{mark}Your relationship with {good}[ns_teacher_name]{/} "+local_text+" {good}[mc_nst_status]{/}{/}{/}"
        "{size=-20} "                             ## minimal line feed
        "[local_text]"                            ## display message if status changed
  call mc_update_personal()                       ## update the mc's personal status
  return

## 0.15.n add function called every night to handle the relationship deterioration counters and actual loss

label update_relationship_counters:  ## these will fire before dating begins, handle it!!
## Simone:
  $global mc_nst_date_counter
  if bp_first_sex_teacher==1:                            ## dating with Simone has begun
    if mc_nst_date_counter>=14:                          ## >= is just in case, could be ==
      $mc_nst_date_counter=0                             ## reset counter
      call mc_update_relation(ns_teacher_name,-1,1)      ## lose 1 relationship point - last value 1 sets to silent MUST TEST!!!
    else:
      $mc_nst_date_counter+=1                             ## increment counter 
## Ruthie:
  $global mc_so_date_counter
  if fwb_date_available==1:                              ## dating with Ruthie has begun
    if mc_so_date_counter>=5:                            ## >= is just in case, could be ==
      $mc_so_date_counter=0                              ## reset counter
      call mc_update_relation(gn_store_owner_name,-1,1)  ## lose 1 relationship point - last value 1 sets to silent MUST TEST!!!
    else:
      $mc_so_date_counter+=1                             ## increment counter

##  $print "Simone Counter: ",mc_nst_date_counter
##  $print "Ruthie Counter: ",mc_so_date_counter

  return