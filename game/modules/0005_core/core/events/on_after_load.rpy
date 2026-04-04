init python hide:
  @event_handler("after_load",-5)
  def init_new_locations():
    for loc_id,loc_cls in sorted(locations_cls_by_id.items()):
      if loc_id and not loc_id.startswith("_"):
        if loc_id not in all_locations:
          setattr(store,loc_id,loc_cls())

  @event_handler("after_load",-4)
  def init_new_characters():
    for char_id,char_cls in sorted(characters_cls_by_id.items()):
      if char_id and not char_id.startswith("_"):
        if char_id not in all_characters:
          setattr(store,char_id,char_cls())

  @event_handler("after_load",-3)
  def init_new_quests():
    for quest_id,quest_cls in sorted(quests_cls_by_id.items()):
      if quest_id and not quest_id.startswith("_"):
        if not quest_id in all_quests:
          if not quest_cls.repeatable:
            quest_cls()

  @event_handler("after_load",-2)
  def init_maturity():                       ## items added in 0.11.n - put in values for for saved games if blank
## store owner relationship
    global mc_so_value
    global mc_so_status

##    print "initial mc_so_value: ",mc_so_value
##    print "initial mc_so_status: ",mc_so_status

    if mc_so_value==0:                       ## save from an version before 0.11.n
      if quests.goodneighbor.finished:
        mc_so_value=27                       ## friend level, almost up to flirting level, guess but must be at least 26
        mc_so_status="Friend"
      elif quests.mobprotection.finished:
        mc_so_value=11                       ## friend level, barely in level, quest includes 2, assume 9 store visits during framed and mob quest
        mc_so_status="Friend"
      elif quests.exiled_engineer.finished:
        mc_so_value=2                        ## acquaintance level, assume you've visited store 2 times during framed
        mc_so_status="Acquaintance"
## teacher relationship
    global mc_nst_value
    global mc_nst_status

##    print "initial mc_nst_value: ",mc_nst_value
##    print "initial mc_nst_status: ",mc_nst_status

    if mc_nst_value==0:                      ## save from an older version
      if quests.karaoke.finished:
        mc_nst_value=35                      ## flirting level, assume you reached limit
        mc_nst_status="Flirting"
      elif quests.nightschool.finished:
        mc_nst_value= 8                      ## acquaintance level, school gives 8
        mc_nst_status="Acquaintance"
      elif quests.nightschool.started:
        mc_nst_value= 1                      ## acquaintance level, Simone must have visited for 1
        mc_nst_status="Acquaintance"

##    print "final mc_so_value: ",mc_so_value
##    print "final mc_so_status: ",mc_so_status
##    print "final mc_nst_value: ",mc_nst_value
##    print "final mc_nst_status: ",mc_nst_status

## personal skill - must be done after relationships because it's based upon them

    global mc_so_value
    global mc_nst_value
    global mc_personal_rate
    global mc_personal_status
    if mc_so_value>100 and mc_nst_value>100:   ## S - both are lovers - impossible in 0.11.n, Simone can't reach FWB
      mc_personal_rate="S"
      mc_personal_status="TBD"
    elif mc_so_value>100 or mc_nst_value>100:  ## A - one is a lover - can be done in 0.11.n with Ruthie
      mc_personal_rate="A"
      mc_personal_status="Charming"
    elif mc_so_value>60 and mc_nst_value>60:   ## A - both are friends with benefits - impossible in 0.11.n, Simone can't reach FWB
      mc_personal_rate="A"
      mc_personal_status="Charming"
    elif mc_so_value>60 or mc_nst_value>60:    ## B = one is a friend with benefits - can be done in 0.11.n with Ruthie
      mc_personal_rate="B"
      mc_personal_status="Confident"
    elif mc_so_value>30 and mc_nst_value>30:   ## B - both are flirting - can be done in 0.11.n
      mc_personal_rate="B"
      mc_personal_status="Confident"
    elif mc_so_value>30 or mc_nst_value>30:    ## C - one is flirting - can be done in 0.11.n
      mc_personal_rate="C"
      mc_personal_status="Inexperienced"
    elif mc_so_value>10 and mc_nst_value>10:   ## D - both are friends - can be done in 0.11.n
      mc_personal_rate="D"
      mc_personal_status="Shy"
    elif mc_so_value>10 or mc_nst_value>10:    ## E - one is a friend - can be done in 0.11.n
      mc_personal_rate="E"
      mc_personal_status="Awkward"
## if none of the above are true remain F-Clueless

## business skill
    global mc_business_rate
    global mc_business_status
## future road map: highest active line is "if", all others are "elif"
##  if quests.revenge.finished:            ## ultimate line is always "if", this is 'game end' event
##    mc_business_rate="S"
##    mc_business_status="Master"
##  if quests.businesspartners.finished:  ## change to "elif" when lines above are activated
##    mc_business_rate="A"
##    mc_business_status="Journeyman"
##  if quests.businesspartners.started:   ## change to "elif" when any of the lines above are activated
##    mc_business_rate="B"
##    mc_business_status="Apprentice"
    if quests.goodneighbor.finished:       ## highest possibility in 0.11.n, change to "elif" when any of the lines above are activated
      mc_business_rate="C"
      mc_business_status="Savvy"
    elif quests.mobprotection.finished:
      mc_business_rate="D"
      mc_business_status="Novice"
    elif quests.exiled_engineer.finished:
      mc_business_rate="E"
      mc_business_status="Rookie"
## if none of the above are true remain F-Clueless