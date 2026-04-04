##===NEW MODULE IN SR24 WITH 3 FUNCTIONS
##  1) Determine if there is room for a new bot - available capsule or available storage space
##  2) Add a bot to the first available capsule or if necessary the first available storage space

##=======VARIABLES/FLAGS=======
init python:
  sr24_room_for_bot=0            ## flag variable set by "sr24_add_bot_ok()" function: 0=cannot add bot, 1=ok to add bot

##==========FUNCTIONS==========

label sr24_add_bot_ok:                                           ## check for capsule or storage space
  if home.available_capsules>=1 or workshop.available_space>=1:
    $sr24_room_for_bot=1                                         ## return 1 if OK to add bot
  else:
    $sr24_room_for_bot=0                                         ## return 0 if no room to add bot
  return

label sr24_add_bot_do(bot_p):
##  $print "Inside 'sr24_add_bot_do'"
  if home.available_capsules>0:
    $home.add_sexbot(bot_p)                                     ## add bot to capsule if available, return 1
  elif workshop.available_space>0:
    $workshop.add_sexbot(bot_p)                                 ## add bot to storage if no capsule, return 1
  return

##===========EXAMPLES===========

##    call sr24_add_bot_ok()
##    if sr24_room_for_bot==1:    ## conditional test: >0 OR ==1 OR !=0 means there is space

##    call sr24_add_bot_do(bot)   ## no return, MUST check for space BEFORE calling this function!!!