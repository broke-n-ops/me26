## Maturity Skills - Business and Personal

##  Grade    Business     Personal
##    F      Clueless     Clueless
##    E      Rookie       Awkward
##    D      Novice       Shy
##    C      Savvy        Inexperienced
##    B      Apprentice   Confident
##    A      Journeyman   Charming
##    S      Master       TBD

## Initialize variables

init python:
  mc_business_rate="F"            ## letter
  mc_business_status="Clueless"   ## text
  mc_business_desc={
    "Master": "Can do it all; work alone and lead partnerships.",
    "Journeyman": "Works alone well and participates in partnerships.",
    "Apprentice": "Works alone well and learning about partnerships.",
    "Savvy": "Making money and working strategically. What's next?",
    "Novice": "Making money and starting to think strategically.",
    "Rookie": "Making money and starting to figure things out.",
    "Clueless": "Struggling to make ends meet."
    }
  mc_personal_rate="F"            ## letter
  mc_personal_status="Clueless"   ## text
  mc_personal_desc={
    "TBD": "You've developed your own little harem.",
    "Charming": "Women find you attractive and want to be with you.",
    "Confident": "Comfortable with people and developing relationships.",
    "Inexperienced": "Found someone special and trying to get closer.",
    "Shy": "Found a couple of friends and better at conversations.",
    "Awkward": "Found a friend and learning how to talk with people.",
    "Clueless": "No close friends and has trouble talking with people."
    }

## FUNCTIONS

label mc_update_business():  ## call function when it will be displayed

##  $print "mc_update_business was executed"

  $global mc_business_rate
  $global mc_business_status
## future road map: highest active line is "if", all others are "elif"
##  if quests.revenge.finished:            ## ultimate line is always "if", this is 'game end' event
##    $mc_business_rate="S"
##    $mc_business_status="Master"
##  if quests.businesspartners.finished:  ## change to "elif" when lines above are activated
##    $mc_business_rate="A"
##    $mc_business_status="Journeyman"
##  if quests.businesspartners.started:   ## change to "elif" when any of the lines above are activated
##    $mc_business_rate="B"
##    $mc_business_status="Apprentice"
  if quests.goodneighbor.finished:       ## highest possibility in 0.11.n, change to "elif" when any of the lines above are activated
    $mc_business_rate="C"
    $mc_business_status="Savvy"
  elif quests.mobprotection.finished:
    $mc_business_rate="D"
    $mc_business_status="Novice"
  elif quests.exiled_engineer.finished:
    $mc_business_rate="E"
    $mc_business_status="Rookie"
## if none of the above are true remain F-Clueless
  return
  
label mc_update_personal():    ## function called every time a relationship value is changed
  $global mc_so_value
  $global mc_nst_value
  $global mc_personal_rate
  $global mc_personal_status
  if mc_so_value>100 and mc_nst_value>100:   ## S - both are lovers - impossible in 0.11.n, Simone can't reach FWB
    $mc_personal_rate="S"
    $mc_personal_status="TBD"
  elif mc_so_value>100 or mc_nst_value>100:  ## A - one is a lover - can be done in 0.11.n with Ruthie
    $mc_personal_rate="A"
    $mc_personal_status="Charming"
  elif mc_so_value>60 and mc_nst_value>60:   ## A - both are friends with benefits - impossible in 0.11.n, Simone can't reach FWB
    $mc_personal_rate="A"
    $mc_personal_status="Charming"
  elif mc_so_value>60 or mc_nst_value>60:    ## B = one is a friend with benefits - can be done in 0.11.n with Ruthie
    $mc_personal_rate="B"
    $mc_personal_status="Confident"
  elif mc_so_value>30 and mc_nst_value>30:   ## B - both are flirting - can be done in 0.11.n
    $mc_personal_rate="B"
    $mc_personal_status="Confident"
  elif mc_so_value>30 or mc_nst_value>30:    ## C - one is flirting - can be done in 0.11.n
    $mc_personal_rate="C"
    $mc_personal_status="Inexperienced"
  elif mc_so_value>10 and mc_nst_value>10:   ## D - both are friends - can be done in 0.11.n
    $mc_personal_rate="D"
    $mc_personal_status="Shy"
  elif mc_so_value>10 or mc_nst_value>10:    ## E - one is a friend - can be done in 0.11.n
    $mc_personal_rate="E"
    $mc_personal_status="Awkward"
  return