label home_add_buttons:
  call home_workout_buttons           ## uses location 5 (top row, far right), ALWAYS USED
 ## call karaoke_button                 ## DO NOT DO THIS, BAD IDEA!!!  uses location 16 (ONLY EVENING) - share with dating Ruthie which is only at night
  call mob_quest_buttons              ## uses locations 12 and 13, ONLY DURING QUEST - 0.15.n moved from 15 and 16 to allow karaoke button to use 16
  call good_neighbor_buttons          ## 0.8.0 uses location 12, ONLY DURING QUEST
  call friends_with_benefits_button   ## 0.11.n uses location 15 (ONLY MORNING) and 16 (ONLY NIGHT) - mob quest must be done for this to start, 15 DURING QUEST, 16 DURING AND AFTER QUEST
  call bot_monitor_button             ## 0.12.8 uses location 6 - ALWAYS USED
  call business_partners_buttons      ## 0.14.0 uses locations 12 for sucky bot, 13 for bot check, 14 for deliver bots, ONLY DURING QUEST
  call cheat_buttons                  ## TESTING PURPOSES ONLY!!! uses locations 8, 9, and 10 (all on second row)
  return

##  Button Numbers:

##   0   1   2   3   4   5
##   6   7   8   9  10  11
##  12  13  14  15  16  17 