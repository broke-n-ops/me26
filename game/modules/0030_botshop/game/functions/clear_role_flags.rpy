## function called every turn end by calling within'rest', 'sleep', and 'work'
## last call after all roles are executed so flag already took effect if set
## acts on all bots in capsules
## no flags for 'bedroom toy' and 'housekeeper' which have no delay

label clear_role_delay_flags:

## techie role
  $assistants=active_bots_with_role_tag("techie")
  $bot_count=0
  while bot_count<len(assistants):
    $temp_bot=assistants[bot_count]
    $temp_bot[0].tech_just_assigned=0
    $bot_count+=1
  $assistants=None

## clerk role
  $assistants=active_bots_with_role_tag("clerk")
  $bot_count=0
  while bot_count<len(assistants):
    $temp_bot=assistants[bot_count]
    $temp_bot[0].clerk_just_assigned=0
    $bot_count+=1
  $assistants=None

## shopkeeper role
  $assistants=active_bots_with_role_tag("shopkeeper")
  $bot_count=0
  while bot_count<len(assistants):
    $temp_bot=assistants[bot_count]
    $temp_bot[0].shpkpr_just_assigned=0
    $bot_count+=1
  $assistants=None

## master techie role
  $assistants=active_bots_with_role_tag("master_techie")
  $bot_count=0
  while bot_count<len(assistants):
    $temp_bot=assistants[bot_count]
    $temp_bot[0].mt_just_assigned=0
    $bot_count+=1
  $assistants=None

## senior techie role
  $assistants=active_bots_with_role_tag("senior_techie")
  $bot_count=0
  while bot_count<len(assistants):
    $temp_bot=assistants[bot_count]
    $temp_bot[0].st_just_assigned=0
    $bot_count+=1
  $assistants=None

## bot manager role
  $assistants=active_bots_with_role_tag("mission_manager")
  $bot_count=0
  while bot_count<len(assistants):
    $temp_bot=assistants[bot_count]
    $temp_bot[0].mgr_just_assigned=0
    $bot_count+=1
  $assistants=None

## bot trainer role - 0.12.n
  $assistants=active_bots_with_role_tag("bot_trainer")
  $bot_count=0
  while bot_count<len(assistants):
    $temp_bot=assistants[bot_count]
    $temp_bot[0].bt_just_assigned=0
    $bot_count+=1
  $assistants=None
  
  return