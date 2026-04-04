define dump_site_scavenge_bot_chance=20
define dump_site_scavenge_bot_part_chance=30

define dump_site_scavenge_bot_keep_cpu_chance=33

define label_dump_site_scavenge_action_info={"cost":[("energy",1)]}

## updated in 0.8.1
define dump_site_generate_bot_mind_table=[
  ["bot_combat",(-800000,15000)],
  ["bot_electronics",(-80000,15000)],
  ["bot_mechanics",(-80000,15000)],
  ["bot_sex",(-80000,60000)],        ## was 75000
  ["bot_social",(-80000,60000)],     ## was 75000
  ]

define dump_site_generate_bot_seals_table={
  "oral": (-1000,2500),
  "vaginal": (-1000,1000),
  "anal": (-1000,500),
  }

label dump_site_scavenge:
  header "[dump_site] - Scavenging"
  "You hack one of the doors and enter the dump. When the guards aren't looking you run past them deep into the hills of trash. Once you are out of their sight you start looking around for anything useful."
  ""
## changed in 0.8.n, missed this in 0.4.0 when storage could be used
##  if home.available_capsules<1:
##    "You don't have free bot capsules, so you focus on searching for parts."
  call sr24_add_bot_ok()
  if sr24_room_for_bot==0:    ## conditional test: >0 OR ==1 OR !=0 means there is space
    "All your bot capsules are full and there is no room in storage so you focus on searching for parts."
  ""
  
  call random_event("dump_site_scavenge")
  if _return=="default":
    ## @@REPEAT_ACTION
    if show_repeat_action():
      choice("dump_site_scavenge") "Scavenge more"
      choice("<<<") "Back"
    else:
      choice("<<<") "Continue"
    choice("<<<",pos=17,key="cancel") "Back"
  return
