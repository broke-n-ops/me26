init python:

##===variables===

  gn_store_owner_name="Ruthie"
  gn_store_owner_rename=0          ## set to 1: first visit to store and beginning of Mob Quest just in case
  gn_diner_owner_name="Earl"
  gn_diner_owner_rename=0          ## set to 1: first visit to diner and beginning of Good Neighbor Quest just in case
  gn_retired_fighter_name="Louis"
  gn_retired_fighter_rename=0      ## set to 1: first visit to bar (no other events as of0.9.n)

##====================RENAME FUNCTION FOR MC AND TEACHER
##  0.8.n - modified to a single button here and a screen with a button for each character

label hw_rename_characters:
## update available characters
  if quests.mobprotection.started or quests.mobprotection.finished:       ## activate store owner rename - introduced when mob protection starts, finished is for old saves
    $gn_store_owner_rename=1
  if quests.nightschool.started and quests.nightschool.phase.num_id>=2:   ## activate teacher rename PART 1 - activated in phase 2 'introduction' in night school
    $ns_teacher_rename=1
  elif quests.nightschool.finished:                                       ## activate teacher rename PART 2 - for old saves where night school was already finished
    $ns_teacher_rename=1
  if quests.goodneighbor.started or quests.goodneighbor.finished:         ## activate diner owner rename - introduced when good neighbor starts, finished is for old saves
    $gn_diner_owner_rename=1
  $game_bg="home bg"          ##  home background 
  header "Rename Characters"
  ""
  "Select the character you would like to rename:"
  ""
  "{mark}MC's{/} name is {mark}[mc.name]{/}"
  ""
  choice("hw_rename_mc",key="1") "MC"
  if ns_teacher_rename==1:
    "{mark}Teacher's{/} name is {mark}[ns_teacher_name]{/}"
    ""
    choice("hw_rename_teacher",key="2") "Teacher"
  if gn_store_owner_rename==1:
    "{mark}Store Owner's{/} name is {mark}[gn_store_owner_name]{/}"
    ""
    choice("hw_rename_store_owner",key="3") "Store Owner"
  if gn_diner_owner_rename==1:
    "{mark}Diner Owner's{/} name is {mark}[gn_diner_owner_name]{/}"
    ""
    choice("hw_rename_diner_owner",key="4") "Diner Owner"
  if gn_retired_fighter_rename==1:
    "{mark}Retired Fighter's{/} name is {mark}[gn_retired_fighter_name]{/}"
    ""
    choice("hw_rename_retired_fighter",key="5") "Retired Fighter"
  choice("goto_home",key="cancel",pos=17) "Done"
  return

label hw_rename_mc:
  $game_bg="home bg"  ##  home background 
  header "Rename MC"
  $act.start_block("l:440 c:content_width-440")
  center "{image=mc avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "MC's current name is {mark}[mc.name]{/}."
  ""
  # # "ns_teacher_rename: [ns_teacher_rename]"          ##  FOR DEBUGGING, DELETE LATER!!!!
  # # ""
  $rename_mc_to=mc.name
  $act.add_screen("ui_input","rename_mc_to","intro_rename_mc",'validate_mc_name("{}")',xalign=0.5,width=300,allowed_chars=allowed_mc_name_chars)
##  v0.6.0 added key for enter key on number pad and enter key
  choice("hw_rename_mc_do",key=("K_KP_ENTER","K_RETURN"),sensitive_if="$not validate_mc_name(rename_mc_to)") "Confirm Name"
  choice("hw_rename_characters",key="cancel") "Cancel"
  return

label hw_rename_mc_do:
  $game_bg="home bg"  ##  home background
  header "Rename MC"
  $mc.name=rename_mc_to
  $act.start_block("l:440 c:content_width-440")
  center "{image=mc avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "MC's new name is {mark}[mc.name]{/}."
  ""
  choice("hw_rename_characters") "Continue"
  return

label hw_rename_teacher:
  $game_bg="home bg"       ##  home background 
  header "Rename Teacher"
  $act.start_block("l:440 c:content_width-440")
  center "{image=teacher avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "Teacher's current name is {mark}[ns_teacher_name]{/}."
  ""
  ""
  $rename_mc_to=ns_teacher_name
  $act.add_screen("ui_input","rename_mc_to","intro_rename_mc",'validate_mc_name("{}")',xalign=0.5,width=300,allowed_chars=allowed_mc_name_chars)
##  v0.6.0 added key for enter key on number pad and enter key
  choice("hw_rename_teacher_do",key=("K_KP_ENTER","K_RETURN"),sensitive_if="$not validate_mc_name(rename_mc_to)") "Confirm Name"
  choice("hw_rename_characters",key="cancel") "Cancel"
  return

label hw_rename_teacher_do:
  $game_bg="home bg"       ##  home background
  header "Rename Teacher"
  $ns_teacher_name=rename_mc_to
  $act.start_block("l:440 c:content_width-440")
  center "{image=teacher avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "Teacher's new name is {mark}[ns_teacher_name]{/}."
  ""
  choice("hw_rename_characters") "Continue"
  return

label hw_rename_store_owner:
  $game_bg="home bg"           ##  home background 
  header "Rename Store Owner"
  $act.start_block("l:440 c:content_width-440")
  center "{image=store_owner avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "Store Owner's current name is {mark}[gn_store_owner_name]{/}."
  ""
  ""
  $rename_mc_to=gn_store_owner_name
  $act.add_screen("ui_input","rename_mc_to","intro_rename_mc",'validate_mc_name("{}")',xalign=0.5,width=300,allowed_chars=allowed_mc_name_chars)
##  v0.6.0 added key for enter key on number pad and enter key
  choice("hw_rename_store_owner_do",key=("K_KP_ENTER","K_RETURN"),sensitive_if="$not validate_mc_name(rename_mc_to)") "Confirm Name"
  choice("hw_rename_characters",key="cancel") "Cancel"
  return

label hw_rename_store_owner_do:
  $game_bg="home bg"           ##  home background
  header "Rename Store Owner"
  $gn_store_owner_name=rename_mc_to
  $act.start_block("l:440 c:content_width-440")
  center "{image=store_owner avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "Store Owner's new name is {mark}[gn_store_owner_name]{/}."
  ""
## 0.11.n add 1 line
  $Location_store_owner_apartment.name=gn_store_owner_name+"'s Apartment"
  choice("hw_rename_characters") "Continue"
  return

label hw_rename_diner_owner:
  $game_bg="home bg"           ##  home background 
  header "Rename Diner Owner"
  $act.start_block("l:440 c:content_width-440")
  center "{image=diner_owner avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "Diner Owner's current name is {mark}[gn_diner_owner_name]{/}."
  ""
  ""
  $rename_mc_to=gn_diner_owner_name
  $act.add_screen("ui_input","rename_mc_to","intro_rename_mc",'validate_mc_name("{}")',xalign=0.5,width=300,allowed_chars=allowed_mc_name_chars)
##  v0.6.0 added key for enter key on number pad and enter key
  choice("hw_rename_diner_owner_do",key=("K_KP_ENTER","K_RETURN"),sensitive_if="$not validate_mc_name(rename_mc_to)") "Confirm Name"
  choice("hw_rename_characters",key="cancel") "Cancel"
  return

label hw_rename_diner_owner_do:
  $game_bg="home bg"           ##  home background
  header "Rename Diner Owner"
  $gn_diner_owner_name=rename_mc_to
  $act.start_block("l:440 c:content_width-440")
  center "{image=diner_owner avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "Diner Owner's new name is {mark}[gn_diner_owner_name]{/}."
  ""
  choice("hw_rename_characters") "Continue"
  return

label hw_rename_retired_fighter:
  $game_bg="home bg"               ##  home background 
  header "Rename Retired Fighter"
  $act.start_block("l:440 c:content_width-440")
  center "{image=retired_fighter avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "Retired Fighter's current name is {mark}[gn_retired_fighter_name]{/}."
  ""
  ""
  $rename_mc_to=gn_retired_fighter_name
  $act.add_screen("ui_input","rename_mc_to","intro_rename_mc",'validate_mc_name("{}")',xalign=0.5,width=300,allowed_chars=allowed_mc_name_chars)
##  v0.6.0 added key for enter key on number pad and enter key
  choice("hw_rename_retired_fighter_do",key=("K_KP_ENTER","K_RETURN"),sensitive_if="$not validate_mc_name(rename_mc_to)") "Confirm Name"
  choice("hw_rename_characters",key="cancel") "Cancel"
  return

label hw_rename_retired_fighter_do:
  $game_bg="home bg"                ##  home background
  header "Rename Retired Fighter"
  $gn_retired_fighter_name=rename_mc_to
  $act.start_block("l:440 c:content_width-440")
  center "{image=retired_fighter avatar@400x600}"
  $act.set_block("c")
  ""
  ""
  "Retired Fighter's new name is {mark}[gn_retired_fighter_name]{/}."
  ""
  choice("hw_rename_characters") "Continue"
  return