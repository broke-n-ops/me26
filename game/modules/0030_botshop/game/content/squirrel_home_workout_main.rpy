## ====================INIT VARIABLES v1.0 & 1.1

init python:

## 0.10.n moved to 'workshop_upgrade' which is where it belongs
  # # ## variable added for workshop power upgrade in version 0.5.n
  # # sr24_power_upgrade_counter=0         ## countdown from payment for power upgrade until it takes place

  hw_fitness_level=0                   ##  sum of strength and stamina: ranges from 'FF'=2 to 'SS'=14 - 2-4=5AP, 5-7=6AP, 8-10=7AP, 11-13=8AP, 14=9AP
  hw_previous_max_energy_base=0        ##  set before updating to determine if it changed
  hw_equipment_level=0                 ##  increases as you purchase equipment:0=none, 10=everything
  hw_workout_ap_cost=1                 ##  equipment levels 0 to 3 = 1, levels 4 to 10 = 2
  hw_building_gym=0                    ##  set to 1 when purchasing gym, construction boss shows you gym next monday
  hw_equipment_purchased=""            ##  set text to equipment being purchased
  hw_equipment_price=0                 ##  set value to equipment being purchased
  hw_delivery_pending=0                ##  set to 1 at each purchase, delivery next day, reset to 0 during delivery
  hw_last_workout=0                    ##  counter for number of days since last workout, effects daily loss of strength & stamina
  hw_workouts_today=0                  ##  counter of daily workouts, 2nd is half effective, 3rd or more is useless
  hw_first_workout=0                   ##  set to 1 when you have equipment and workout, flag for daily fitness loss function
  hw_found_rockys=0                    ##  set to 1 after initiating sales calls from Ray's Dealer
  hw_bought_everything=0               ##  set to 1 when the "done message" is read

## variables used when you cannot pay for the home gym (equipment is easier, they just don't give it to you)
  hw_cannot_pay=0                      ##  set to 1 if you can't pay for the gym construction
    ##  gym locked
    ##  20% (<hw_homegym_interest> variable) added to amount every week
    ##  collection agent will come by every week
    ##  when you exceed $150,000 (<hw_homegym_maxdebt> variable) owed they kill you (game over)
  hw_debt_amount=0                     ##  add 20% every week when a collection agent visits instead of the salesman
  hw_first_collection=0                ##  set flag to 1 in first collection visit to change subsequent text

## six variables used to apply workout impact and daily fitness loss
  hw_equipment_impact=0                ##  holds equipment related value during calculations
  hw_skill_impact=0                    ##  holds skill level related value during calculations
  hw_skill_value=0                     ##  holds final workout impact calculated using variables below
  hw_min_value=0                       ##  minimum value for randomizing outcomes
  hw_max_value=0                       ##  maximum value for randomizing outcomes
  hw_entry_value=0                     ##  final randomized value for entry

## START OF VARIABLES USED FOR CALCULATIONS - MODDERS: EASY TWEAKING HERE (ACTUAL PURPOSE WAS PLAY BALANCING)
   ## Equipment related impact on Workouts which increase Strength (new skill), Stamina (new skill), and MOOD
   ## Equipment Cost - nothing is free!
   ## Daily loss of Strength and Stamina if you do NOT Workout - Use it or lose it
   ## AP cannot fall below 5, if you never Workout this mod has no effect except a few extra clicks
   ## Leveling up a new skill 3 times increases AP (see line 11 above)
   ## Saves made using this mod will NOT work without mod because of new skills
   ## Skill calculations within the game require higher gains/losses at higher levels (looks strange)

## INITIAL VALUES INTENT
   ## Values set and tested before adding randomizer of +/- 15% (randomness is typical game behavior)
   ## Gain: Based upon working out 1 time per day every day (no skipping days) AND starting with 0 xp towards the next level
     ## Values adjusted to make all levels equivalent - larger increases at higher levels
     ## Poorly equipped gym - 4 strength, 4 stamina takes 13.6 days to level up - result of forumla
     ## Mid-point equipped gym - 12 strength, 12 stamina takes 7.0 days to level up - single point calibration
     ## Maximum equipped gym - 24 strength, 24 stamina takes 4.6 days to level up - result of formula
   ## Loss: Based upon not working out at all AND starting with the highest possible xp within the level
     ## Values adjusted to make all levels equivalent - larger decreases at higher levels
     ## Level down in 10 days at all levels

## WORKOUT GAIN SECTION

## WORKOUTS WITHOUT EQUIPMENT AT START
  hw_no_equipment_min=2      ##  ALWAYS USE EVEN NUMBERS, DIVIDE BY 2 SHOULD BE INTEGER
  hw_no_equipment_max=10     ##  ALWAYS USE EVEN NUMBERS, DIVIDE BY 2 SHOULD BE INTEGER

## Workout Gain formula example: (hw_level_f_gain)/(hw_workouts_today)*(hw_equipment1)**(hw_fudgefactor_gain)
   ## 1st workout fully effective, 2nd workout same day half effective
   ## Additional workouts on same day have no effect (code logic - not calculation)

## Exponential 'fudge factor' applied to equipment values to tune gain from workouts, recommend stay <= 1
   ## increasing will magnify the impact each piece of equipment makes, workouts become more effective
  hw_fudgefactor_gain=0.6

## base values for determining gain from workout at each strength and stamina level, higher numbers = more gain
## levels are non-linear but not fully exponential: leveling up is much easier at lower levels
## these values are designed to turn it into a more linear range: range / gain = 31.2 (arbitrary value, tuned in testing)
## with hindsight there are better ways to achieve this goal but this approach works OK
  hw_level_f_base_gain=32    ##  range - 1,000
  hw_level_e_base_gain=72    ##  range - 2,250
  hw_level_d_base_gain=160   ##  range - 5,000
  hw_level_c_base_gain=320   ##  range - 10,000
  hw_level_b_base_gain=720   ##  range - 22,500
  hw_level_a_base_gain=1600  ##  range - 50,000
  hw_level_s_base_gain=3200  ##  range - 99,999

## LOSS FROM NOT WORKING OUT SECTION

## Loss from not working out formula example: (hw_level_f_loss)*(hw_last_workout)**(hw_fudgefactor_loss)
   ## no loss incurred if you worked out that day

## Exponential 'fudge factor' applied to number of days since last workout, recommend stay <= 1
   ## decreasing will reduce the loss of strength and stamina each day when not working out
  hw_fudgefactor_loss=0.6

## base values for determining loss from not working out at each strength and stamina level, greater negative numbers = more loss
  hw_level_f_base_loss=-37
  hw_level_e_base_loss=-84
  hw_level_d_base_loss=-187
  hw_level_c_base_loss=-374
  hw_level_b_base_loss=-842
  hw_level_a_base_loss=-1871
  hw_level_s_base_loss=-3743

## EXERCISE EQUIPMENT VARIABLES - IMPACT ON WORKOUTS AND COST TO PURCHASE

## 40 variables define each piece of exercise equipment, higher numbers - more impact or cost
   ## note 1: Strength, Stamina, and Mood of the fully equipped gym all equal 24, not mandatory
   ## note 2: equipment prices are arbitrary

## level 1
  hw_barbell_strength=4
  hw_barbell_stamina=2
  hw_barbell_mood=1
  hw_barbell_price=1500
## level 2
  hw_benchpress_strength=5
  hw_benchpress_stamina=1
  hw_benchpress_mood=1
  hw_benchpress_price=2500
## level 3
  hw_exercisebike_strength=1
  hw_exercisebike_stamina=4
  hw_exercisebike_mood=1
  hw_exercisebike_price=4500
## level 4
  hw_homegym_strength=0
  hw_homegym_stamina=0
  hw_homegym_mood=12                   ##  includes yoga mat for bots to do yoga and playtime with mc
  hw_homegym_price=50000
  hw_homegym_maxdebt=150000            ##  maximum allowed gym debt - exceeding this is 'game over'
##  hw_homegym_maxdebt=73000             ##  set value lower for testing purposes, after 2 collection agent visits killer comes on 3rd visit
  hw_homegym_interest=1.2              ##  multiplier for 20% interest
##  level 5
  hw_treadmill_strength=0
  hw_treadmill_stamina=5
  hw_treadmill_mood=1
  hw_treadmill_price=6500
##  level 6
  hw_tv_strength=0
  hw_tv_stamina=0
  hw_tv_mood=4
  hw_tv_price=3500
##  level 7
  hw_punchingbag_strength=4
  hw_punchingbag_stamina=3
  hw_punchingbag_mood=1
  hw_punchingbag_price=2000
##  level 8
  hw_ellipticaltrainer_strength=2
  hw_ellipticaltrainer_stamina=4
  hw_ellipticaltrainer_mood=1
  hw_ellipticaltrainer_price=5500
##  level 9
  hw_pullupbar_strength=4
  hw_pullupbar_stamina=1
  hw_pullupbar_mood=1
  hw_pullupbar_price=1000
##  level 10
  hw_rowingmachine_strength=4
  hw_rowingmachine_stamina=4
  hw_rowingmachine_mood=1
  hw_rowingmachine_price=4500

## variables below are for the daily loss of strength and stamina (use it or lose it!) - need higher impact at higer levels
## note: values calculated as percentage of full scale for each level

## END OF VARIABLES USED TO CALCULATE WORKOUT IMPACT - MODDERS: EASY TWEAKING ABOVE

## set of 30 variables using individual equipment values above to calculate values for each equipment level
  hw_equipment1_strength=hw_barbell_strength
  hw_equipment2_strength=hw_equipment1_strength+hw_benchpress_strength
  hw_equipment3_strength=hw_equipment2_strength+hw_exercisebike_strength
  hw_equipment4_strength=hw_equipment3_strength+hw_homegym_strength
  hw_equipment5_strength=hw_equipment4_strength+hw_treadmill_strength
  hw_equipment6_strength=hw_equipment5_strength+hw_tv_strength
  hw_equipment7_strength=hw_equipment6_strength+hw_punchingbag_strength
  hw_equipment8_strength=hw_equipment7_strength+hw_ellipticaltrainer_strength
  hw_equipment9_strength=hw_equipment8_strength+hw_pullupbar_strength
  hw_equipment10_strength=hw_equipment9_strength+hw_rowingmachine_strength

  hw_equipment1_stamina=hw_barbell_stamina
  hw_equipment2_stamina=hw_equipment1_stamina+hw_benchpress_stamina
  hw_equipment3_stamina=hw_equipment2_stamina+hw_exercisebike_stamina
  hw_equipment4_stamina=hw_equipment3_stamina+hw_homegym_stamina
  hw_equipment5_stamina=hw_equipment4_stamina+hw_treadmill_stamina
  hw_equipment6_stamina=hw_equipment5_stamina+hw_tv_stamina
  hw_equipment7_stamina=hw_equipment6_stamina+hw_punchingbag_stamina
  hw_equipment8_stamina=hw_equipment7_stamina+hw_ellipticaltrainer_stamina
  hw_equipment9_stamina=hw_equipment8_stamina+hw_pullupbar_stamina
  hw_equipment10_stamina=hw_equipment9_stamina+hw_rowingmachine_stamina

  hw_equipment1_mood=hw_barbell_mood
  hw_equipment2_mood=hw_equipment1_mood+hw_benchpress_mood
  hw_equipment3_mood=hw_equipment2_mood+hw_exercisebike_mood
  hw_equipment4_mood=hw_equipment3_mood+hw_homegym_mood
  hw_equipment5_mood=hw_equipment4_mood+hw_treadmill_mood
  hw_equipment6_mood=hw_equipment5_mood+hw_tv_mood
  hw_equipment7_mood=hw_equipment6_mood+hw_punchingbag_mood
  hw_equipment8_mood=hw_equipment7_mood+hw_ellipticaltrainer_mood
  hw_equipment9_mood=hw_equipment8_mood+hw_pullupbar_mood
  hw_equipment10_mood=hw_equipment9_mood+hw_rowingmachine_mood

##====================INIT VARIABLES v2.0 WITH IMAGES

  hw_bedroomtoyflag=0          ##  0=no bedroom toy, 1=bedroon toy - for morning wakeup
  hw_imagemin=0                ##  holder for lowest image number in range of random images
  hw_imagemax=0                ##  holder for highest image number in range of random images
  hw_imagenumber=0             ##  holder for image number selected randomly
  hw_randomimagelist=[0]       ##  list holder for list of potential first images
  hw_selectedimagelist=[0]     ##  list holder for list of actual first images
  hw_freeyogalessons=5         ##  count down for free yoga lessons when you buy the home gym
  hw_wheretoinstall=""         ##  install location for equipment delivery
  hw_deliveryarrives=0         ##  2 sets of pictures: 1 for desk(#318) or 2 by bot gurney(#321)
  hw_training_cost=500         ##  cost for yoga or boxing training
  hw_random_text=1             ##  for yoga and boxing at level 10 have 3 versions of text
  hw_yoga_exercise=0.04        ##  multiplier of full scale for strength and stamina
  hw_yoga_mood=10              ##  average mood increase for yoga
  hw_yoga_social=125           ##  average social skill increase for yoga
  hw_yoga_sex=20               ##  average sex benefit for yoga, increases at higher levels, 100 in levels 8-10
  hw_yoga_mechanics=20         ##  average mechanics benefit for yoga, increases at higher levels
  hw_yoga_electronics=20       ##  average electronics benefit for yoga, increases at higher levels
  hw_yoga_computers=20         ##  average computers benefit for yoga, increases at higher levels
  hw_boxing_exercise=0.12      ##  multiplier of full scale for strength and stamina
  hw_boxing_mood=5             ##  average mood increase for boxing
  hw_boxing_combat=125         ##  average combat benefit for boxing, level throughout
  hw_boxing_sex=100            ##  average sex benefit for boxing, higher levels only
  hw_fullscale_f=1000          ##  xp to advance F to E - these are in the game, added here for convenience
  hw_fullscale_e=2250          ##  xp to advance E to D
  hw_fullscale_d=5000          ##  xp to advance E to D
  hw_fullscale_c=10000         ##  xp to advance E to D
  hw_fullscale_b=22500         ##  xp to advance E to D
  hw_fullscale_a=50000         ##  xp to advance E to D
  hw_fullscale_s=99999         ##  xp maximum for S

##====================CREATE STRENGTH AND STAMINA SKILL CLASSES

init python:

  class MCSkill_strength(MCSkill):
    id="strength"
    name="Strength"

  class MCSkill_stamina(MCSkill):
    id="stamina"
    name="Stamina"

##============EVENT HANDLING FUNCTIONS========

init python hide:
  @event_handler("time_advanced")
  def homeworkout_event_1():
    if now("wednesday","afternoon"):
      if hw_equipment_level<=9 and hw_found_rockys!=0:  ## found Rocky's on the net and don't have all equipment yet
        queue_event("hw_salesman_visit")
    elif now("thursday", "afternoon"):
      if hw_delivery_pending==1:
        queue_event("hw_equipment_delivery")
    elif now("thursday", "evening"):
      if hw_equipment_level==10:                        ## have everything
        if hw_bought_everything==0:                     ## bought everything flag still 0, function sets flag so called only once
          queue_event("hw_done_message")
    elif now("tuesday", "afternoon"):
      if hw_building_gym==1:
        queue_event("hw_gym_done")

##====================FUNCTION FOR SELECTING WORKOUT

label home_workout_action:         ##  CAN'T CHANGE THIS FUNCTION NAME OR SAVES WILL BREAK
  if hw_equipment_level<=3:        ##  only exercise is available
    call hw_workout_exercise
  elif hw_equipment_level<=6:      ##  exercise and yoga available
    $game_bg="home bg"
    header "Home"
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $hw_imagenumber=random.randint(365,367)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    if hw_workouts_today>0:          ##  already worked out today, cannot do yoga
      if hw_freeyogalessons<=0:      ##  no free yoga lessons left
        "I go to my bedroom and change into my workout clothes. I already worked out today and I'm a little tired. Yoga lessons would be a waste of money, should I do my normal {mark}exercise{/}?"
      else:
        "I go to my bedroom and change into my workout clothes. I already worked out today and I'm a little tired. Yoga lessons would be a waste of time, should I do my normal {mark}exercise{/}?"
    else:                            ##  first workout of the day, can do exercise or yoga
      if hw_freeyogalessons<=0:      ##  no free lessons left
        "I go to my bedroom and change into my workout clothes. Should I do my normal {mark}exercise{/} or should I take a {mark}yoga lesson{/} with that hot yoga training bot?"
      else:
        "I go to my bedroom and change into my workout clothes. Should I do my normal {mark}exercise{/} or should I try one of the {mark}free yoga lessons{/} with that hot yoga training bot?"
    ""
    choice("hw_workout_exercise",cost=[("energy",hw_workout_ap_cost)],hint="[hw_workout_ap_cost] AP") "Exercise"    ##  must always have this button but it could be inactive
    if hw_workouts_today==0:         ##  first workout of the day, add yoga button
      if hw_freeyogalessons<=0:      ##  no free lessons left
        choice("hw_wait_yoga",cost=[("energy",hw_workout_ap_cost),("money",hw_training_cost)],hint="[hw_workout_ap_cost] AP, $[hw_training_cost]") "Yoga Training"
      else:
        choice("hw_wait_yoga",cost=[("energy",hw_workout_ap_cost)],hint="[hw_workout_ap_cost] AP") "Yoga Training"
    choice("<<<") "Changed my mind"  ##  must always have this button
  else:                              ## exercise, yoga, and boxing available
    $game_bg="home bg"
    header "Home"
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $hw_imagenumber=random.randint(365,367)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    if hw_workouts_today>0:          ##  already worked out today, cannot do either yoga or boxing
      "I go to my bedroom and change into my workout clothes. I already worked out today and I'm a little tired. Yoga or boxing lessons would be a waste of time and money, should I do my normal {mark}exercise{/}?"
    else:                            ##  first workout of the day, can do anything
      if hw_freeyogalessons<=0:      ##  no free yoga lessons left
        "I go to my bedroom and change into my workout clothes. Should I do my normal {mark}exercise{/}, should I take a {mark}yoga lesson{/} with that hot yoga training bot, or should I take a {mark}boxing lesson{/} with that sexy boxing training bot?"
      else:
        "I go to my bedroom and change into my workout clothes. Should I do my normal {mark}exercise{/}, should I try one of the {mark}free yoga lessons{/} with that hot yoga training bot, or should I take a {mark}boxing lesson{/} with that sexy boxing training bot?"
    ""
    choice("hw_workout_exercise",cost=[("energy",hw_workout_ap_cost)],hint="[hw_workout_ap_cost] AP") "Exercise"    ##  must always have this button but it could be inactive
    if hw_workouts_today==0:         ##  first workout of the day, can do anything
      if hw_freeyogalessons<=0:      ##  no free lessons left
        choice("hw_wait_yoga",cost=[("energy",hw_workout_ap_cost),("money",hw_training_cost)],hint="[hw_workout_ap_cost] AP, $[hw_training_cost]") "Yoga Training"
      else:
        choice("hw_wait_yoga",cost=[("energy",hw_workout_ap_cost)],hint="[hw_workout_ap_cost] AP") "Yoga Training"
      choice("hw_wait_boxing",cost=[("energy",hw_workout_ap_cost),("money",hw_training_cost)],hint="[hw_workout_ap_cost] AP, $[hw_training_cost]") "Boxing Training"
    choice("<<<") "Changed my mind"  ##  must always have this button
  return

##====================FUNCTIONS FOR EXERCISING

label hw_workout_exercise:
  $game_bg="home bg"             ##  home background
  if hw_equipment_level <=3:
    header "Home - Bedroom"
  else:
    header "Home - Gym"
  $hw_workouts_today+=1          ##  increment daily workout counter
  $hw_last_workout=0             ##  reset the 'days since last workout' counter
  if hw_workouts_today<=2:       ##  any more workouts bypass with no effect
    if hw_equipment_level>=1:    ##  with equipment workouts have strong impact
      call hw_select_exercise_images
      ##  TEXT
      $act.set_block("c")
      ""
      "It feels good to workout, I'm stronger and have more endurance!"
      ""
      call hw_update_strength
      call hw_update_stamina
      if hw_workouts_today==1:      ##  first workout of the day
        ""
        ""
        "I always feel great after a workout, I should keep this up!"
        ""
      else:                         ##  second workout of the day, half the effect (more no effect)
        ""
        ""
        "I'm really tired, I'm not sure working out twice in one day is such a great idea."
        ""
      call hw_update_mood
    else:                        ##  with no equipment workouts have low impact
      ##  GRAPHICS
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $hw_imagenumber=random.randint(34,36)    ##  SEMI-HARD CODE - SIMPLE
      $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
      $hw_imagenumber=random.randint(37,39)    ##  SEMI-HARD CODE - SIMPLE
      $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
      center "{image=[action_image]@400x600}"
      ""
      ##  TEXT
      $act.set_block("c")
      $hw_first_workout=1                         ##  establishes that Strength and Stamina have been created
      ""
      if hw_workouts_today==1:                    ##  full benefit for first workout
        "You do a few situps and pushups in your room. It's not much but it's all I can do, this neighborhood is too dangerous to go for a run."
        ""
        $hw_entry_value=random.randint(hw_no_equipment_min,hw_no_equipment_max)
        $mc.give_xp("strength",hw_entry_value)
        $hw_entry_value=random.randint(hw_no_equipment_min,hw_no_equipment_max)
        $mc.give_xp("stamina",hw_entry_value)
      elif hw_workouts_today==2:                  ##  benefit halved for second workout
        "After doing a few situps and pushups you wonder if working out more than once a day is worth it."
        ""
        $hw_entry_value=random.randint(hw_no_equipment_min//2,hw_no_equipment_max//2)
        $mc.give_xp("strength",hw_entry_value)    ##  low benefit for situps and pushups
        $hw_entry_value=random.randint(hw_no_equipment_min//2,hw_no_equipment_max//2)
        $mc.give_xp("stamina",hw_entry_value)     ##  low benefit for situps and pushups
      if hw_found_rockys==0:
        call hw_initiate_dealer_visits
        return                                    ##  need to exit before creating the 'continue' button
      if hw_delivery_pending==1:                  ##  This is only used between ordering barbells and receiving them, very rare!
        ""
        "This seems like I'm wasting my time, I can't wait for my {mark}new bar bells{/} to be delivered."
      else:
        ""
        "Maybe I should buy some fitness equipment from the {mark}Rocky's dealer{/} when he comes in."
      ""
  else:                          ## 3rd workout bypass
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image="squirrel_mods home_workout hw_335"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    "I tried to work out but I was too tired and ended uptaking a nap. What a waste of time."
    ""
  choice("<<<") "Continue"
  return

label hw_update_strength:
  if hw_equipment_level==1:
    $hw_equipment_impact=hw_equipment1_strength
  elif hw_equipment_level==2:
    $hw_equipment_impact=hw_equipment2_strength
  elif hw_equipment_level==3:
    $hw_equipment_impact=hw_equipment3_strength
  elif hw_equipment_level==4:
    $hw_equipment_impact=hw_equipment4_strength
  elif hw_equipment_level==5:
    $hw_equipment_impact=hw_equipment5_strength
  elif hw_equipment_level==6:
    $hw_equipment_impact=hw_equipment6_strength
  elif hw_equipment_level==7:
    $hw_equipment_impact=hw_equipment7_strength
  elif hw_equipment_level==8:
    $hw_equipment_impact=hw_equipment8_strength
  elif hw_equipment_level==9:
    $hw_equipment_impact=hw_equipment9_strength
  elif hw_equipment_level==10:
    $hw_equipment_impact=hw_equipment10_strength

  if mc.strength.level==1:
    $hw_skill_impact=hw_level_f_base_gain
  elif mc.strength.level==2:
    $hw_skill_impact=hw_level_e_base_gain
  elif mc.strength.level==3:
    $hw_skill_impact=hw_level_d_base_gain
  elif mc.strength.level==4:
    $hw_skill_impact=hw_level_c_base_gain
  elif mc.strength.level==5:
    $hw_skill_impact=hw_level_b_base_gain
  elif mc.strength.level==6:
    $hw_skill_impact=hw_level_a_base_gain
  elif mc.strength.level==7:
    $hw_skill_impact=hw_level_s_base_gain

  $hw_skill_value=round(hw_skill_impact/hw_workouts_today*hw_equipment_impact**hw_fudgefactor_gain,2)
  $hw_min_value=hw_skill_value*0.85
  $hw_max_value=hw_skill_value*1.15
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  $mc.give_xp("strength",hw_entry_value)         ##  real version after testing
  return

label hw_update_stamina:
  if hw_equipment_level==1:
    $hw_equipment_impact=hw_equipment1_stamina
  elif hw_equipment_level==2:
    $hw_equipment_impact=hw_equipment2_stamina
  elif hw_equipment_level==3:
    $hw_equipment_impact=hw_equipment3_stamina
  elif hw_equipment_level==4:
    $hw_equipment_impact=hw_equipment4_stamina
  elif hw_equipment_level==5:
    $hw_equipment_impact=hw_equipment5_stamina
  elif hw_equipment_level==6:
    $hw_equipment_impact=hw_equipment6_stamina
  elif hw_equipment_level==7:
    $hw_equipment_impact=hw_equipment7_stamina
  elif hw_equipment_level==8:
    $hw_equipment_impact=hw_equipment8_stamina
  elif hw_equipment_level==9:
    $hw_equipment_impact=hw_equipment9_stamina
  elif hw_equipment_level==10:
    $hw_equipment_impact=hw_equipment10_stamina

  if mc.stamina.level==1:
    $hw_skill_impact=hw_level_f_base_gain
  elif mc.stamina.level==2:
    $hw_skill_impact=hw_level_e_base_gain
  elif mc.stamina.level==3:
    $hw_skill_impact=hw_level_d_base_gain
  elif mc.stamina.level==4:
    $hw_skill_impact=hw_level_c_base_gain
  elif mc.stamina.level==5:
    $hw_skill_impact=hw_level_b_base_gain
  elif mc.stamina.level==6:
    $hw_skill_impact=hw_level_a_base_gain
  elif mc.stamina.level==7:
    $hw_skill_impact=hw_level_s_base_gain

  $hw_skill_value=round(hw_skill_impact/hw_workouts_today*hw_equipment_impact**hw_fudgefactor_gain,2)
  $hw_min_value=hw_skill_value*0.85
  $hw_max_value=hw_skill_value*1.15
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                             ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("stamina",hw_entry_value)            ##  real version after testing
  return

label hw_update_mood:                              ##  value low and hidden, no need to randomize
  if hw_equipment_level==1:
    $hw_equipment_impact=int(hw_equipment1_mood/2)
  elif hw_equipment_level==2:
    $hw_equipment_impact=int(hw_equipment2_mood/2)
  elif hw_equipment_level==3:
    $hw_equipment_impact=int(hw_equipment3_mood/2)
  elif hw_equipment_level==4:
    $hw_equipment_impact=int(hw_equipment4_mood/2)
  elif hw_equipment_level==5:
    $hw_equipment_impact=int(hw_equipment5_mood/2)
  elif hw_equipment_level==6:
    $hw_equipment_impact=int(hw_equipment6_mood/2)
  elif hw_equipment_level==7:
    $hw_equipment_impact=int(hw_equipment7_mood/2)
  elif hw_equipment_level==8:
    $hw_equipment_impact=int(hw_equipment8_mood/2)
  elif hw_equipment_level==9:
    $hw_equipment_impact=int(hw_equipment9_mood/2)
  elif hw_equipment_level==10:
    $hw_equipment_impact=int(hw_equipment10_mood/2)
  $mc.mood.give_xp(hw_equipment_impact)
  return

label hw_select_exercise_images:
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")    ##  set up graphics only once
  $act.set_block("l")
  if hw_equipment_level==1:    ##  barbells - bedroom
    $hw_imagenumber=random.randint(40,42)               ##  first image random selection
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    if hw_imagenumber==40:
      $action_image="squirrel_mods home_workout hw_41"  ##  40,41
      center "{image=[action_image]@400x600}"
    elif hw_imagenumber==41:
      $action_image="squirrel_mods home_workout hw_42"  ##  41,42
      center "{image=[action_image]@400x600}"
    else:
      $action_image="squirrel_mods home_workout hw_40"  ##  42,40
      center "{image=[action_image]@400x600}"
  elif hw_equipment_level==2:  ##  benchpress - bedroom
    $hw_imagenumber=random.randint(49,51)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(43,45)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
  elif hw_equipment_level==3:  ##  exercisebike - bedroom - 55-57
    $hw_imagenumber=random.randint(55,57)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(52,54)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(46,48)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
  elif hw_equipment_level==4:  ##  no new equipment - gym
    $hw_imagenumber=random.randint(100,102)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(79,81)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(58,60)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
  elif hw_equipment_level==5:  ##  treadmill - gym
    $hw_randomimagelist=[61,82,103,121]
    $hw_selectedimagelist=random.sample(hw_randomimagelist, 3)
  elif hw_equipment_level==6:  ##  TV but no new equipment - gym
    $hw_randomimagelist=[64,85,106,124]
    $hw_selectedimagelist=random.sample(hw_randomimagelist, 3)
  elif hw_equipment_level==7:  ##  punchingbag - gym
    $hw_randomimagelist=[67,88,109,127,139]
    $hw_selectedimagelist=random.sample(hw_randomimagelist, 3)
  elif hw_equipment_level==8:  ##  ellipticaltrainer
    $hw_randomimagelist=[70,91,112,130,142,151]
    $hw_selectedimagelist=random.sample(hw_randomimagelist, 3)
  elif hw_equipment_level==9:  ##  pullupbar - gym
    $hw_randomimagelist=[73,94,115,133,145,154,160]
    $hw_selectedimagelist=random.sample(hw_randomimagelist, 3)
  elif hw_equipment_level==10:  ##  rowingmachine - gym
    $hw_randomimagelist=[76,97,118,136,148,157,163,166]
    $hw_selectedimagelist=random.sample(hw_randomimagelist, 3)
  if hw_equipment_level>=5:     ##  levels 1-4 don't use lists
    $hw_imagemin=hw_selectedimagelist[0]
    $hw_imagemax=hw_imagemin+2
    $hw_imagenumber=random.randint(hw_imagemin,hw_imagemax)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagemin=hw_selectedimagelist[1]
    $hw_imagemax=hw_imagemin+2
    $hw_imagenumber=random.randint(hw_imagemin,hw_imagemax)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagemin=hw_selectedimagelist[2]
    $hw_imagemax=hw_imagemin+2
    $hw_imagenumber=random.randint(hw_imagemin,hw_imagemax)
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
  ""                              ##  blank line at end entered only once
  $hw_randomimagelist=[0]         ##  clear list
  $hw_selectedimagelist=[0]       ##  clear list
  return

##====================FUNCTIONS FOR YOGA TRAINING

label hw_wait_yoga:
  $game_bg="home bg"             ##  home background
  header "Home - Workshop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $hw_imagenumber=random.randint(368,369)    ##  SEMI-HARD CODE - SIMPLE
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(370,371)    ##  SEMI-HARD CODE - SIMPLE
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  ""
  if hw_freeyogalessons>=1:
    "After signing up for the free lesson I went to the workshop to wait for the yoga trainer. They said it would be less than 10 minutes, I wonder how they do that?"
    ""
    ""
    ""
    "I told the yoga training bot to come with me to the gym. She's really hot, even if I don't like the yoga it will be fun to watch her!"
  else:                         ## out of free lessons
    "After paying for the lesson I went to the workshop to wait for the yoga trainer. They said it would be less than 10 minutes, I wonder how they do that?"
    ""
    ""
    ""
    "I told the yoga training bot to come with me to the gym. I was skeptical about yoga but it's actually fun and improves my concentration!"
  ""
  choice("hw_workout_yoga") "Continue"
  return


label hw_workout_yoga:
  $game_bg="home bg"             ##  home background
  header "Home - Gym"
  $hw_workouts_today+=1          ##  increment daily workout counter
  $hw_last_workout=0             ##  reset the 'days since last workout' counter
  if hw_freeyogalessons>=1:
    $hw_freeyogalessons-=1       ##  subtract a free lesson if any are left
  if hw_equipment_level>=8:      ##  increase sex benefit when sex with bot trainer starts
    $hw_yoga_sex=100
  call hw_show_yoga_images
  call hw_show_yoga_text
  call hw_yoga_results
  choice("<<<") "Continue"
  return

label hw_show_yoga_images:
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if hw_equipment_level==4:
    $hw_imagenumber=random.randint(235,237)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(238,240)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(241,243)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  elif hw_equipment_level==5:
    $hw_imagenumber=random.randint(244,246)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(247,249)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(250,252)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  elif hw_equipment_level==6:
    $hw_imagenumber=random.randint(253,255)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(256,258)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(259,261)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  elif hw_equipment_level==7:
    $hw_imagenumber=random.randint(262,264)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(265,267)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(268,270)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  elif hw_equipment_level==8:
    $hw_imagenumber=random.randint(271,273)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(274,276)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(277,279)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  elif hw_equipment_level==9:
    $hw_imagenumber=random.randint(280,282)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(283,285)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(286,288)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  else:     ##  must be 10
    $hw_imagenumber=random.randint(376,384)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(385,393)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(394,402)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  return

label hw_show_yoga_text:
  ##  TEXT
  $act.set_block("c")
  if hw_equipment_level==4:      ##  images: watch-watch-teach
    ""
    "The lesson starts with me watching her demonstrate a few yoga poses. She looks really good but I'm not sure about doing yoga myself, I feel a little silly."
    ""
    "After a while I join her and we do a few yoga poses together. It's harder than it looks! She says yoga is both physical and mental. Improved concentration and focus will provide many benefits. We'll see."
    ""
  elif hw_equipment_level==5:    ##  images: watch-watch-teach
    ""
    "As usual, the lesson starts with me watching her demonstate a couple of yoga poses. There sure are a lot of different poses! She looks great, I wonder if I can do these poses?"
    ""
    "When we start doing yoga poses together I realize it is actually fun! I also think my concentration and ability to focus is improving. Maybe she's right that this is good for me."
    ""
  elif hw_equipment_level==6:    ##  images: teach-teach-couple
    ""
    "The lesson starts with us doing yoga poses together. Even though I'm posing with her I still check her out occasionally! With a hot trainer I guess this yoga stuff isn't so bad."
    ""
    "After a while she says we should try a couples pose and to make it more interesting she takes of her yoga outfit! Wow, it's hard to concentrate on the pose but I like the direction this is going!"
    ""
  elif hw_equipment_level==7:    ##  images: teach-couple-couple
    ""
    "As usual, the lesson starts with us doing yoga poses together. This is fine but I tell her I want to do more of the couples poses. She strips off her yoga outfit to get ready for couples poses."
    ""
    "I take off my shirt and we try a few couples poses. The poses are hard but I enjoy checking her out while we're posing! I can't believe I'm enjoying yoga and getting benefits from doing it too."
    ""
  elif hw_equipment_level==8:    ##  images: teach-couple-sex(bj)
    ""
    "We start the lesson doing yoga poses together but pretty quickly I tell her I want to do more of the couples poses. I think she expected me to say that! She strips off her yoga outfit."
    ""
    "I take off my shirt and we do a few couples poses. She notices me checking her out and says we can do more than yoga if I want. Of course I want! She drops to her knees and gives me a blow job. I love yoga!"
    ""
  elif hw_equipment_level==9:    ##  images: teach-couple-sex(titjob)
    ""
    "We start by doing yoga poses together. This is OK but I prefer the couples poses, especially since she does them naked! I think she knows I'm anxious to move on to couples poses."
    ""
    "She strips and I take off my shirt so we can do a few couples poses. After a few poses she says I should sit down on my bench press so she can give me a tit job. I love yoga!"
    ""
  else:                          ##  must be 10: images: couple-sex-sex: fucking in 3 positions
    $hw_random_text=random.randint(1,3)    ##  select 1 of 3 messages since this will repeat
    if hw_random_text==1:
      ""
      "The yoga training bot asks me if I want to go straight to couples poses and I'm all for it! She strips off her yoga outfit and I take off my shirt for a few yoga poses."
      ""
      "We do a few yoga poses which are difficult but they are also fun and a good workout for both body and mind. After the yoga workout she knows what I want and we have sex to finish the lesson."
      ""
    elif hw_random_text==2:
      ""
      "I tell the yoga training bot that I want to go straight to couples poses this time! I take off my shirt while I enjoy watching her strip off her yoga outfit!"
      ""
      "I enjoy doing the couples yoga poses. Not only do I get to check out the training bot but doing yoga is helping me a lot. After the poses we end the lesson with sex. These yoga lessons are great!"
      ""
    else:    ##  must be 3
      ""
      "Before I can say anything the yoga training bot strips off her yoga outfit for couples poses. She really is hot! While checking her out I take off my shirt so we can begin."
      ""
      "The couples yoga poses are challenging but I enjoy doing them and I appreciate the benefits I get from doing yoga. When we're done with the poses we finish the lesson with hot sex. I love yoga lessons!"
      ""
  return

label hw_yoga_results:    ##  NOTE: MC always has all default skills (bots may not!!)
##  STRENGTH - must have if doing yoga
  if mc.strength.level==1:
    $hw_skill_value=hw_fullscale_f*hw_yoga_exercise
  elif mc.strength.level==2:
    $hw_skill_value=hw_fullscale_e*hw_yoga_exercise
  elif mc.strength.level==3:
    $hw_skill_value=hw_fullscale_d*hw_yoga_exercise
  elif mc.strength.level==4:
    $hw_skill_value=hw_fullscale_c*hw_yoga_exercise
  elif mc.strength.level==5:
    $hw_skill_value=hw_fullscale_b*hw_yoga_exercise
  elif mc.strength.level==6:
    $hw_skill_value=hw_fullscale_a*hw_yoga_exercise
  elif mc.strength.level==7:
    $hw_skill_value=hw_fullscale_s*hw_yoga_exercise
  $hw_min_value=hw_skill_value*0.75                 ##  created value, game does NOT give 2x
  $hw_max_value=hw_skill_value*1.25                 ##  created value, game does NOT give 2x
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("strength",hw_entry_value)
##  STAMINA - must have if doing yoga
  if mc.stamina.level==1:
    $hw_skill_value=hw_fullscale_f*hw_yoga_exercise
  elif mc.stamina.level==2:
    $hw_skill_value=hw_fullscale_e*hw_yoga_exercise
  elif mc.stamina.level==3:
    $hw_skill_value=hw_fullscale_d*hw_yoga_exercise
  elif mc.stamina.level==4:
    $hw_skill_value=hw_fullscale_c*hw_yoga_exercise
  elif mc.stamina.level==5:
    $hw_skill_value=hw_fullscale_b*hw_yoga_exercise
  elif mc.stamina.level==6:
    $hw_skill_value=hw_fullscale_a*hw_yoga_exercise
  elif mc.stamina.level==7:
    $hw_skill_value=hw_fullscale_s*hw_yoga_exercise
  $hw_min_value=hw_skill_value*0.75                 ##  created value, game does NOT give 2x
  $hw_max_value=hw_skill_value*1.25                 ##  created value, game does NOT give 2x
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("stamina",hw_entry_value)
##  SOCIAL
  $hw_min_value=hw_yoga_social*0.375                ##  game gives 2x, 75% / 2
  $hw_max_value=hw_yoga_social*0.625                ##  game gives 2x, 125% /2
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("social",hw_entry_value)
##  SEX
  $hw_min_value=hw_yoga_sex*0.375                   ##  game gives 2x, 75% / 2
  $hw_max_value=hw_yoga_sex*0.625                   ##  game gives 2x, 125% /2
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("sex",hw_entry_value)
##  MECHANICS
  $hw_min_value=hw_yoga_mechanics*0.375             ##  game gives 2x, 75% / 2
  $hw_max_value=hw_yoga_mechanics*0.625             ##  game gives 2x, 125% /2
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("mechanics",hw_entry_value)
##  ELECTRONICS
  $hw_min_value=hw_yoga_electronics*0.375           ##  game gives 2x, 75% / 2
  $hw_max_value=hw_yoga_electronics*0.625           ##  game gives 2x, 125% /2
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("electronics",hw_entry_value)
##  COMPUTERS
  $hw_min_value=hw_yoga_computers*0.375             ##  game gives 2x, 75% / 2
  $hw_max_value=hw_yoga_computers*0.625             ##  game gives 2x, 125% /2
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("computers",hw_entry_value)
##  MOOD
  $hw_min_value=hw_yoga_mood*0.375                  ##  game gives 2x, 75% / 2
  $hw_max_value=hw_yoga_mood*0.625                  ##  game gives 2x, 125% /2
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.mood.give_xp(hw_entry_value)
  return

##====================FUNCTIONS FOR BOXING TRAINING

label hw_wait_boxing:
  $game_bg="home bg"             ##  home background
  header "Home - Workshop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  ""
  $hw_imagenumber=random.randint(372,373)    ##  SEMI-HARD CODE - SIMPLE
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(374,375)    ##  SEMI-HARD CODE - SIMPLE
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  ""
  "After paying for the lesson I went to the workshop to wait for the boxing trainer. They said it would be less than 10 minutes, I wonder how they do that?"
  ""
  ""
  ""
  "I told her to come with me to the gym. She really hot, it will be hard to concentrate on boxing! Once she starts hitting me I'll start paying attention!"
  choice("hw_workout_boxing") "Continue"
  return

label hw_workout_boxing:
  $game_bg="home bg"             ##  home background
  header "Home - Gym"
  $hw_workouts_today+=1          ##  increment daily workout counter
  $hw_last_workout=0             ##  reset the 'days since last workout' counter
  call hw_show_boxing_images
  call hw_show_boxing_text
  call hw_boxing_results
  choice("<<<") "Continue"
  return

label hw_show_boxing_images:
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if hw_equipment_level==7:
    $hw_imagenumber=random.randint(403,405)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(406,408)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(409,411)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  elif hw_equipment_level==8:
    $hw_imagenumber=random.randint(412,414)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(415,417)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(418,420)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  elif hw_equipment_level==9:
    $hw_imagenumber=random.randint(421,423)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(424,426)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(427,429)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  else:    ##  must be 10
    $hw_imagenumber=random.randint(430,438)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(439,447)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(448,456)    ##  SEMI-HARD CODE - SIMPLE
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
  return

label hw_show_boxing_text:
  ##  TEXT
  $act.set_block("c")
  if hw_equipment_level==7:      ##  images: bag-bag-spar
    ""
    "The boxing lesson starts by taking turns beating up on my punching bag. The training bot gives me a bunch of pointers and following her advice my punches start having more effect. Pretty cool!"
    ""
    "Later she strips off her clothes and says were going to spar, wow! She shows me how to keep my arms up and defend myself but it's hard to concentrate on boxing. What a chassis on that bot!"
  elif hw_equipment_level==8:    ##  images: bag-bag-spar
    ""
    "As usual, we start the lesson starts by taking turns beating up on my punching bag. I can tell my punches are stronger, good technique really helps! Checking her out is great too, "
    ""
    "Later she strips and we start sparring. I'm doing a little better than before but she's fast and it's hard to tag her. Unfortunately she has no problem tagging me, thank god she has a limiter or I'd be hurting!"
    ""
  elif hw_equipment_level==9:    ##  images: bag-spar-sex(bj)
    ""
    "We begin the lesson taking turns beating up on my punching bag. My technique is improving and I'm getting faster, maybe I'll tag her this time! I'd like to do more than boxing, I wonder if that's OK."
    ""
    "Later we start sparring and unfortunately she still has no problem tagging me! As a way of apologizing she takes off her gloves, drops to her knees, and gives me a blow job. Sure feels better than getting punched!"
    ""
  else:                          ##  must be 10: images: bag-spar-sex: fucking in 3 positions, 1 anal
    $hw_random_text=random.randint(1,3)    ##  select 1 of 3 messages since this will repeat
    if hw_random_text==1:
      ""
      "As usual, we start by beating up on my punching bag, at least it's good exercise! Before long she strips off her clothes and says it's time to spar. I hope I can tag her this time!"
      ""
      "We spar for a while and occasionally I tag her. It feels good but she's probably just letting me do it. When we're done sparring she knows what I want and we have sex to finish the lesson."
      ""
    elif hw_random_text==2:
      ""
      "Once again we abuse my punching bag to start the lesson. It's a good workout but I'm thinking about what will come next! After a while she gets naked and says it's time to spar. I never get tired of looking at her!"
      ""
      "I'm getting better so sparring is more fun than it used to be but I still think she's toying with me. Finally she drops the gloves and we have a little post-boxing sex. These boxing lessons are great!"
      ""
    else:    ##  must be 3
      ""
      "First we take turns hitting the punching bag but I'm impatient and say it's time to spar. She replies by stripping off her clothes to get ready. She's really hot and I always enjoy checking her out."
      ""
      "Sparring with her is really a good workout, she's so fast. Thank god for the limiter or I'd probably be dead! Before I'm too tired she drops her gloves so we can finish the lesson with a more enjoyable workout."
      ""
  return

label hw_boxing_results:    ##  NOTE: MC always has all default skills (bots may not!!)
##  STRENGTH - must have if boxing
  if mc.strength.level==1:
    $hw_skill_value=hw_fullscale_f*hw_boxing_exercise
  elif mc.strength.level==2:
    $hw_skill_value=hw_fullscale_e*hw_boxing_exercise
  elif mc.strength.level==3:
    $hw_skill_value=hw_fullscale_d*hw_boxing_exercise
  elif mc.strength.level==4:
    $hw_skill_value=hw_fullscale_c*hw_boxing_exercise
  elif mc.strength.level==5:
    $hw_skill_value=hw_fullscale_b*hw_boxing_exercise
  elif mc.strength.level==6:
    $hw_skill_value=hw_fullscale_a*hw_boxing_exercise
  elif mc.strength.level==7:
    $hw_skill_value=hw_fullscale_s*hw_boxing_exercise
  $hw_min_value=hw_skill_value*0.75                 ##  created value, game does NOT give 2x
  $hw_max_value=hw_skill_value*1.25                 ##  created value, game does NOT give 2x
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("strength",hw_entry_value)
##  STAMINA - must have if boxing
  if mc.stamina.level==1:
    $hw_skill_value=hw_fullscale_f*hw_boxing_exercise
  elif mc.stamina.level==2:
    $hw_skill_value=hw_fullscale_e*hw_boxing_exercise
  elif mc.stamina.level==3:
    $hw_skill_value=hw_fullscale_d*hw_boxing_exercise
  elif mc.stamina.level==4:
    $hw_skill_value=hw_fullscale_c*hw_boxing_exercise
  elif mc.stamina.level==5:
    $hw_skill_value=hw_fullscale_b*hw_boxing_exercise
  elif mc.stamina.level==6:
    $hw_skill_value=hw_fullscale_a*hw_boxing_exercise
  elif mc.stamina.level==7:
    $hw_skill_value=hw_fullscale_s*hw_boxing_exercise
  $hw_min_value=hw_skill_value*0.75                 ##  created value, game does NOT give 2x
  $hw_max_value=hw_skill_value*1.25                 ##  created value, game does NOT give 2x
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("stamina",hw_entry_value)
##  COMBAT
  $hw_min_value=hw_boxing_combat*0.375              ##  game gives 2x, 75% / 2
  $hw_max_value=hw_boxing_combat*0.625              ##  game gives 2x, 125% /2
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.give_xp("combat",hw_entry_value)
##  SEX
  if hw_equipment_level>=9:                         ##  start sex benefit when sex with training bot begins
    $hw_min_value=hw_boxing_sex*0.375               ##  game gives 2x, 75% / 2
    $hw_max_value=hw_boxing_sex*0.625               ##  game gives 2x, 125% /2
    $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
    if hw_entry_value<1:                            ##  minimum gain is 1
      $hw_entry_value=1
    $mc.give_xp("sex",hw_entry_value)
##  MOOD
  $hw_min_value=hw_boxing_mood*0.75
  $hw_max_value=hw_boxing_mood*1.25
  $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
  if hw_entry_value<1:                              ##  minimum gain is 1
    $hw_entry_value=1
  $mc.mood.give_xp(hw_entry_value)
  return

##====================FUNCTIONS FOR INITIATING VISITS FROM RAY'S DEALER

label hw_initiate_dealer_visits:
  ""
  "Maybe if I had some exercise equipment my workouts would be more effective. I should search the net for exercise equipment."
  choice("hw_equipment_search") "Search the Net"
  return

label hw_equipment_search:
  $game_bg="home bg"             ##  home background
  header "Home - Bedroom"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel_mods home_workout hw_333"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_334"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "There are a lot of options but most of them are too expensive. I don't want to spend a lot of money on bad stuff."
  ""
  ""
  ""
  "I decided to try {mark}Rocky's Fitness{/}. I started a chat and found out that a Rocky's dealer is in my area on {mark}Wednesday afternoons{/}. They took my address and said someone would stop by then. We'll see what they have to offer."
  ""
  $hw_found_rockys=1                   ##  set flag so the dealer starts visiting
  choice("<<<") "Continue"
  return

##====================FUNCTIONS FOR PURCHASING EQUIPMENT FROM RAY'S DEALER

 ##  Note: payment and incrementing equipment level will happen upon delivery or completion of home gym

label hw_salesman_visit:       ##  Salesman visit: 10 equipment purchases at levels 0 through 9, when level reaches 10 falls through for no action
  if hw_equipment_level==0:
    call hw_salesman_1
  elif hw_cannot_pay!=0:       ##  COULD NOT PAY FOR GYM AND WENT TO COLLECTIONS
    call hw_collection_agent
  elif hw_equipment_level==1:
    call hw_salesman_2
  elif hw_equipment_level==2:
    call hw_salesman_3
  elif hw_equipment_level==3:
    call hw_salesman_4
  elif hw_equipment_level==4:
    call hw_salesman_5
  elif hw_equipment_level==5:
    call hw_salesman_6
  elif hw_equipment_level==6:
    call hw_salesman_7
  elif hw_equipment_level==7:
    call hw_salesman_8
  elif hw_equipment_level==8:
    call hw_salesman_9
  elif hw_equipment_level==9:
    call hw_salesman_10
  return

label hw_salesman_1:    ##  BARBELLS
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="Bar Bells"
  $hw_equipment_price=hw_barbell_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(169,171)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(172,174)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "A salesman from Rocky's Gym Equipment comes to the shop to sell you a set of {mark}Bar Bells{/}.  The price is {mark}$[hw_equipment_price]{/}."
  ""
  ""
  ""
  ""
  ""
  "If you buy it they will collect the payment when they deliver it tomorrow."
  ""
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_salesman_2:    ##  BENCH PRESS
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="Bench Press"
  $hw_equipment_price=hw_benchpress_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(169,171)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(172,174)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "A salesman from Rocky's Gym Equipment comes to the shop to sell you a {mark}Bench Press{/}.  The price is {mark}$[hw_equipment_price]{/}."
  ""
  ""
  ""
  ""
  ""
  "If you buy it they will collect the payment when they deliver it tomorrow."
  ""
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_salesman_3:    ##  EXERCISE BIKE
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="Exercise Bike"
  $hw_equipment_price=hw_exercisebike_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(169,171)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(172,174)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "A salesman from Rocky's Gym Equipment comes to the shop to sell you an {mark}Exercise Bike{/}.  The price is {mark}$[hw_equipment_price]{/}."
  ""
  ""
  ""
  ""
  ""
  "If you buy it they will collect the payment when they deliver it tomorrow."
  ""
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_salesman_4:    ##  HOME GYM
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="Home Gym"
  $hw_equipment_price=hw_homegym_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel_mods home_workout hw_175"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_176"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_177"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_178"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "The salesman from {mark}Rocky's Gym Equipment{/} comes to the shop with a nice looking bot in a yoga outfit. He knows I have no more space, I wonder what's up?"
  ""
  ""
  ""
  "He says we should discuss a great deal while the bot clears my table and starts doing yoga poses, pretty hot! The salesman says they can build me a great new {mark}Home Gym{/} and shows me a brochure."
  ""
  ""
  ""
  "While I'm staring at the bot he says they can build a home gym into my unused basement for {mark}$[hw_equipment_price]{/} and I don't pay until they complete it which takes about a week."
  ""
  ""
  ""
  "He says I'll get {mark}five free yoga lessons{/} with a bot like the one he brought and tells me that he does yoga to increase fitness and concentration and sometimes just to {mark}play with the bot afterwards!{/}"
  ""
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_salesman_5:    ##  TREADMILL
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="Treadmill"
  $hw_equipment_price=hw_treadmill_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(169,171)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(172,174)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "A salesman from Rocky's Gym Equipment comes to the shop to sell you a {mark}Treadmill{/}.  The price is {mark}$[hw_equipment_price]{/}."
  ""
  ""
  ""
  ""
  ""
  "If you buy it they will collect the payment when they deliver it tomorrow."
  ""
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_salesman_6:    ##  TV
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="TV"
  $hw_equipment_price=hw_tv_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(169,171)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(172,174)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "A salesman from Rocky's Gym Equipment comes to the shop to sell you a {mark}TV{/} to install in your home gym.  The price is {mark}$[hw_equipment_price]{/}."
  ""
  ""
  ""
  ""
  ""
  "If you buy it they will collect the payment when they deliver and install it tomorrow."
  ""
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_salesman_7:    ##  PUNCHING BAG
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="Punching Bag"
  $hw_equipment_price=hw_punchingbag_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel_mods home_workout hw_179"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_181"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_182"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_180"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "The salesman from {mark}Rocky's Gym Equipment{/} comes to the shop with a well built bot wearing boxing gloves. She looks pretty tough but also sexy as hell, I wonder what's up?"
  ""
  ""
  "We sit down and the bot starts demonstrating boxing moves which is both hot and intimidating! The salesman says he can sell you a {mark}Punching Bag{/} for {mark}$[hw_equipment_price]{/}."
  ""
  ""
  ""
  "While I'm watching the bot and her moves he says it would be good to know how to fight living in a neighborhood like this and that I can get {mark}boxing lessons from a bot like this one{/}."
  ""
  ""
  ""
  "He says she's well trained and has limiters to prevent her from hurting you during training. He also tells me that he loves sparring with the training bot and also {mark}playing with her afterwards!{/}"
  ""
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_salesman_8:    ##   ELLIPTICAL TRAINER
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="Elliptical Trainer"
  $hw_equipment_price=hw_ellipticaltrainer_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(169,171)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(172,174)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "A salesman from Rocky's Gym Equipment comes to the shop to sell you an {mark}Elliptical Trainer{/}.  The price is {mark}$[hw_equipment_price]{/}."
  ""
  ""
  ""
  ""
  ""
  "If you buy it they will collect the payment when they deliver it tomorrow."
  ""
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_salesman_9:    ##  PULL-UP BAR
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="Pull-Up Bar"
  $hw_equipment_price=hw_pullupbar_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(169,171)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(172,174)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "A salesman from Rocky's Gym Equipment comes to the shop to sell you a {mark}Pull-Up Bar{/}.  The price is {mark}$[hw_equipment_price]{/}."
  ""
  ""
  ""
  ""
  ""
  "If you buy it they will collect the payment when they deliver and install it tomorrow."
  ""
  $hw_equipment_purchased="Pull-Up Bar"
  $hw_equipment_price=hw_pullupbar_price
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_salesman_10:    ##   ROWING MACHINE
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  $hw_equipment_purchased="Rowing Machine"
  $hw_equipment_price=hw_rowingmachine_price
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(169,171)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(172,174)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "A salesman from Rocky's Gym Equipment comes to the shop to sell you a {mark}Rowing Machine{/}.  The price is {mark}$[hw_equipment_price]{/}."
  ""
  ""
  ""
  ""
  ""
  "If you buy it they will collect the payment when they deliver it tomorrow."
  ""
  choice("hw_buy_equipment",hint="[hw_equipment_price]") "Purchase"
  choice("hw_do_not_buy") "Don't Purchase"
  return

label hw_buy_equipment:
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if hw_equipment_level==3:     ##  PURCHASING HOME GYM - YOGA BOT
    $action_image="squirrel_mods home_workout hw_186"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_187"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_188"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_189"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    "It would be great to have a home gym and yoga training might be fun too. You tell the salesman you'll buy the {mark}home gym{/} while the bot continues to do yoga poses."
    ""
    ""
    ""
    "The salesman says that's fantastic and shows off the bot that I'm staring at. He says I'll love having a {mark}home gym{/} and the {mark}free yoga lessons{/} too!"
    ""
    ""
    ""
    ""
    "I'm a little sad when she stops posing and they both start to leave. She looks back at me as they're leaving and I feel a little foolish waving goodbye to a bot!"
    ""
    ""
    ""
    "After they left I noticed he left the brochure for me to look at later if I want. {mark}I better make sure I have the money to pay for the gym when it's finished!{/}"
    ""
    $hw_building_gym=1          ##  SET FLAG FOR BUILDING GYM
  elif hw_equipment_level==6:   ##  PURCHASING PUNCHING BAG - BOXING BOT
    $action_image="squirrel_mods home_workout hw_190"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_191"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_192"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_193"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    "Learning to box would improve my fighting skills both for safety and for training bots. You tell the salesman you'll buy the {mark}punching bag{/} and even the bot looks happy!"
    ""
    ""
    "The salesman says that's fantastic and shows off the bot that I'm staring at. {mark}He says I will benefit from learning to box and with this bot it will be fun too!{/}"
    ""
    ""
    ""
    ""
    "I'm a little sad when she stops posing and they both start to leave. She looks back at me as they're leaving and I get a sense of deja vu when I wave goodbye to a bot again!"
    ""
    ""
    "After they left I thought about boxing training with the hot boxing bot. {mark}I better make sure I have the money to pay for the punching bag when it's delivered tomorrow.{/}"
    ""
    $hw_delivery_pending=1      ##  SET FLAG FOR DELIVERY
  else:
    $hw_imagenumber=random.randint(183,185)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(339,341)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    ""
    "You decide to purchase the {mark}[hw_equipment_purchased]{/}."
    ""
    ""
    ""
    ""
    ""
    "I have to make sure I have {mark}$[hw_equipment_price]{/} to pay for the equipment when they deliver it tomorrow."
    ""
    $hw_delivery_pending=1      ##  SET FLAG FOR DELIVERY
  choice("<<<") "Continue"
  return

label hw_do_not_buy:
  $game_bg="home workspace"
  header "Rocky's Dealer Comes to the Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if hw_equipment_level==3:     ##  PURCHASING HOME GYM - YOGA BOT
    $action_image="squirrel_mods home_workout hw_197"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_198"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_199"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_200"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    "I decide that I can't afford this and tell the salesman I won't be able to buy the home gym right now while the bot continues to do yoga poses."
    ""
    ""
    ""
    "The salesman says he knows it's a big purchase. The bot continues to do yoga poses as he hands me the brochure saying I should keep it just in case."
    ""
    ""
    ""
    ""
    "I'm a little sad when she stops posing and they both start to leave.  She looks back at me as they're leaving and I wonder about {mark}yoga lessons with benefits!{/}"
    ""
    ""
    ""
    "After they left I looked at the brochure again and wondered if I should have bought the gym. {mark}Fitness training is good for me and a home gym would make it even better{/}."
    ""
  elif hw_equipment_level==6:   ##  PURCHASING PUNCHING BAG - BOXING BOT
    $action_image="squirrel_mods home_workout hw_201"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_202"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_203"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_204"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    "I'm not sure about boxing and decide not to purchase the punching bag. You tell the salesman no and the bot drops her arms and looks surprised."
    ""
    ""
    ""
    ""
    "The salesman says I really should learn boxing while the bot leans away looking disapointed or is that just my imagination?"
    ""
    ""
    ""
    "I'm a little sad when they both start to leave.  She looks back at me as they're leaving and now I think she looks angry. {mark}That's crazy, it's just a bot!{/}"
    ""
    ""
    ""
    ""
    "After they left I thought about it and wondered if I made a mistake. {mark}Boxing could be a valuable skill and playing with that bot would be fun!{/}"
    ""
  else:
    $hw_imagenumber=random.randint(194,196)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    $hw_imagenumber=random.randint(342,344)    ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    ""
    "You think about it and decide not to purchase the equipment."
    ""
    ""
    ""
    "The salesman tries to change your mind for a little while but he eventually gives up and leaves."
    ""
  choice("<<<") "Continue"
  return

##====================FUNCTIONS FOR EQUIPMENT DELIVERY FROM ED'S DELIVERY SERVICE EQUIPMENT

label hw_equipment_delivery:     ##  Delivery: 9 deliveries at levels 0,1,2,4,5,6,7,8,9 - level 3 is home gym which is different

  if hw_delivery_pending!=0:     ##  Delivery is pending
    $hw_delivery_pending=0       ##  Reset pending flag before calling functions
  $game_bg="home workspace"
  header "Big Ed's Delivery Service Comes to the Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_deliveryarrives=random.randint(0,1)                 ##  allows picking from 2 sets - 318-320 and 321-323
  if hw_deliveryarrives==0:
    $hw_imagenumber=random.randint(318,320)               ##  first image random selection
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    if hw_imagenumber==318:
      $action_image="squirrel_mods home_workout hw_319"  ##  318,319
      center "{image=[action_image]@400x600}"
    elif hw_imagenumber==319:
      $action_image="squirrel_mods home_workout hw_320"  ##  319,320
      center "{image=[action_image]@400x600}"
    else:                                                ##  must be 320
      $action_image="squirrel_mods home_workout hw_318"  ##  320,318
      center "{image=[action_image]@400x600}"
  else:                                                  ##  hw_deliveryarrives must be 1
    $hw_imagenumber=random.randint(321,323)              ##  first image random selection
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    if hw_imagenumber==321:
      $action_image="squirrel_mods home_workout hw_322"  ##  321,322
      center "{image=[action_image]@400x600}"
    elif hw_imagenumber==322:
      $action_image="squirrel_mods home_workout hw_323"  ##  322,323
      center "{image=[action_image]@400x600}"
    else:                                                ##  must be 323
      $action_image="squirrel_mods home_workout hw_321"  ##  323,321
      center "{image=[action_image]@400x600}"                                               ## must be
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "Big Ed's delivery service arrives to deliver the {mark}[hw_equipment_purchased]{/} you purchased from {mark}Rocky's Gym Equipment{/}."
  ""
  ""
  ""
  ""
  ""
  "If you want to accept delivery you must have {mark}$[hw_equipment_price]{/} to pay the delivery man."
  ""
  if mc.money>=hw_equipment_price:  ##  you have enough money to pay
    choice("hw_acceptdelivery") "Accept Delivery"
  choice("hw_refusedelivery") "Refuse Delivery"
  return

label hw_acceptdelivery:
  $game_bg="home workspace"
  header "Big Ed's Delivery Installs Equipment"
  if hw_equipment_level<=2:    ##  install in bedroom
    $hw_wheretoinstall="bedroom"
  else:                        ##  install in gym
    $hw_wheretoinstall="gym"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if hw_deliveryarrives==0:                              ##  was set in hw_delivery (chooses desk vs gurney)
    $hw_imagenumber=random.randint(345,347)              ##  first image random selection - accept
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
  else:                                                  ##  hw_deliveryarrives must be 1
    $hw_imagenumber=random.randint(348,350)              ##  first image random selection - acept
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
  ""
  if hw_equipment_level==0:    ##  barbells    ##  second image is installing equipment, no relation to first picture
    $hw_imagenumber=random.randint(357,359)    ##  SEMI-HARD CODE - SIMPLE
  elif hw_equipment_level==1:  ##  benchpress
    $hw_imagenumber=random.randint(208,210)    ##  SEMI-HARD CODE - SIMPLE
  elif hw_equipment_level==2:  ##  exercisebike
    $hw_imagenumber=random.randint(211,213)    ##  SEMI-HARD CODE - SIMPLE 
  elif hw_equipment_level==4:  ##  treadmill (3=gym skipped - done differently)
    $hw_imagenumber=random.randint(217,219)    ##  SEMI-HARD CODE - SIMPLE
  elif hw_equipment_level==5:  ##  TV
    $hw_imagenumber=random.randint(220,222)    ##  SEMI-HARD CODE - SIMPLE
  elif hw_equipment_level==6:  ##  punchingbag
    $hw_imagenumber=random.randint(223,225)    ##  SEMI-HARD CODE - SIMPLER
  elif hw_equipment_level==7:  ##  ellipticaltrainer
    $hw_imagenumber=random.randint(226,228)    ##  SEMI-HARD CODE - SIMPLE
  elif hw_equipment_level==8:  ##  pullupbar
    $hw_imagenumber=random.randint(229,231)    ##  SEMI-HARD CODE - SIMPLE
  elif hw_equipment_level==9:  ##  rowingmachine
    $hw_imagenumber=random.randint(232,234)    ##  SEMI-HARD CODE - SIMPLE
  ##  GRAPHICS CONTINUED
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  if hw_wheretoinstall=="gym":
    $hw_imagenumber=random.randint(457,459)    ##  SEMI-HARD CODE - SIMPLE - third image, no relation to first two
  else:
    $hw_imagenumber=random.randint(324,326)    ##  SEMI-HARD CODE - SIMPLE - third image, no relation to first two
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  ""
  "You tell the delivery guy you'll accept the delivery."
  ""
  ""
  ""
  ""
  ""
  "He brings the {mark}[hw_equipment_purchased]{/} in and installs it in your {mark}[hw_wheretoinstall]{/}."
  ""
  ""
  ""
  ""
  ""
  if hw_wheretoinstall=="gym":  ## equipment installed in gym payment is in workshop
    "The delivery man returns to the shop to tell you the equipment is installed and after you pay him he leaves."
  else:                         ## equipment was installed in bedroom you pay him there
    "You get the money for the equipment from your cabinet and after you pay him the delivery man leaves."
  ""
  $mc.money-=hw_equipment_price    ##  pay for the equipment
  $hw_equipment_level+=1           ##  increment equipment level
  $hw_delivery_pending=0           ##  After delivery function reset flag
  choice("<<<") "Continue"
  return

label hw_refusedelivery:
  $game_bg="home workspace"
  header "Big Ed's Delivery Service Comes to the Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if hw_deliveryarrives==0:                              ##  was set in hw_delivery (chooses desk vs gurney)
    $hw_imagenumber=random.randint(351,353)              ##  first image random selection - refuse
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(327,329)              ##  second image random selection - delivery guy mad
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
  else:                                                  ##  hw_deliveryarrives must be 1
    $hw_imagenumber=random.randint(354,356)              ##  first image random selection - refuse
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(330,332)              ##  second image random selection - delivery guy mad
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  ""
  "You tell the guy you won't accept delivery of the {mark}[hw_equipment_purchased]{/}."
  ""
  ""
  ""
  ""
  ""
  "He glares at you like he wants to kill you before he turns around and leaves."
  ""
  choice("<<<") "Continue"
  return

##====================FUNCTION FOR COMPLETION OF THE HOME GYM

label hw_gym_done:
  $game_bg="home workspace"
  header "New Home Gym"
  $hw_building_gym=0                                   ##  reset variable to prevent doing it again!
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel_mods home_workout hw_362"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_215"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""

  ##  TEXT
  $act.set_block("c")
  ""
  "The construction boss tells you they're done building your home gym and wants to show it to you.  You stop what you're doing and follow him downstairs."
  ""
  ""
  "{mark}Wow, the gym is really great!{/} The construction boss says they got your equipment from your bedroom and set it up in the gym. He also points out the yoga mats for your {mark}free yoga lessons{/}."
  ""
  "You need {mark}$[hw_homegym_price]{/} to pay for the gym."

  ## If mc.money==0:      ##  ALTERNATE LINE FOR DEBUGGING SET SO YOU CANNOT PAY

  if mc.money>=hw_homegym_price:  ##  you have enough money to pay
    choice("hw_payforgym") "Pay for Gym"
  choice("hw_donotpayforgym") "Don't Pay for Gym"
  return

label hw_payforgym:
  $game_bg="home workspace"
  header "New Home Gym"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel_mods home_workout hw_363"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_290"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "{mark}You tell the construction boss the gym looks great{/} and then ask him to wait a few minutes while you get the money."
  ""
  ""
  ""
  "You leave briefly to get the money. When you return you hand it over to the construction boss and then he leaves."
  ""
  $hw_equipment_level+=1                ##  increment equipment level
  $mc.money=mc.money-hw_homegym_price   ##  pay for gym upon completion
  $hw_workout_ap_cost=2                 ##  more intensive workout in home gym
  choice("<<<") "Continue"
  return

label hw_donotpayforgym:
  $game_bg="home workspace"
  header "New Home Gym"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel_mods home_workout hw_292"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_293"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_297"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_364"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "You tell the guy you don't have enough money to pay for the gym. He gets really angry and says; {say}I'm putting an{/} {bad}electronic lock{/}{say} on the gym until you pay up{/}."
  ""
  ""
  ""
  "Then he says; {say}Starting tomorrow a{/} {bad}collection agent{/} {say}will come every{/} {bad}Wednesday afternoon{/} {say}to collect the debt. He will{/} {bad}add 20 percent interest{/} {say}each time and will{/} {bad}NOT{/} {say}accept partial payment{/}."
  ""
  ""
  ""
  "Finally he stares into your eyes and shows you a picture of a large ugly looking guy and says; {say}If you ever see this guy it will be the{/} {bad}last thing you'll ever see{/}."
  ""
  ""
  ""
  "Wow, these guys don't fool around, {mark}I better come up with the money!{/} At least he put my equipment back in my bedroom before he locked the gym and left."
  ""
  $hw_debt_amount=hw_homegym_price      ##  set debt to the price of the gym
  $hw_cannot_pay=1                      ##  set flag to start collections
  choice("<<<") "Continue"
  return

##====================FUNCTIONS FOR DID NOT PAY FOR THE HOME GYM

label hw_collection_agent:
  $game_bg="home workspace"
  header "The Collection Agent Comes to the Shop"
  $hw_debt_amount=int(hw_debt_amount*hw_homegym_interest)   ##  add 20% each week
  if hw_debt_amount>hw_homegym_maxdebt:            ##  debt over limit, game over
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image="squirrel_mods home_workout hw_315"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    $action_image="squirrel_mods home_workout hw_316"    ##  HARD CODE - SINGLE USE
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    "A different man you've never seen before comes to the shop. {bad}Oh no, he looks like the man in the picture!{/}"
    ""
    ""
    ""
    "He looks you in the eye and tells you your debt is {bad}more than $[hw_homegym_maxdebt]{/}."
    ""
    "{bad}Without saying anything else he pulls out a gun, shoots you in the gut, and watches you bleed to death.{/}"
    ""
    choice("hw_bad_ending",hint="{bad}Bad Ending{/}") "Continue"
  else:
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $hw_imagenumber=random.randint(298,300)              ##  first image random selection - refuse
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    $hw_imagenumber=random.randint(301,303)              ##  first image random selection - refuse
    $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
    center "{image=[action_image]@400x600}"
    ""
    ##  TEXT
    $act.set_block("c")
    ""
    if hw_first_collection==0:    ##  set to 0 at start of game
      $hw_first_collection=1      ##  set to 1 to change text for repeat collection agent visits
      "A well-dressed man comes to the shop. {mark}At least he doesn't look like the guy in the picture the construction boss showed me!{/}"
      ""
      ""
      ""
      "I get up to talk to him and he tells me he's here to collect the debt for my {mark}home gym{/}. He says I owe {bad}$[hw_debt_amount]{/}."
    else:
      "The same well-dressed collection agent comes into the shop again. He's not very friendly but as long as it's him I think I'm OK."
      ""
      ""
      ""
      "I know what he's here for and I get up to talk to him. He tells me the debt for my {mark}home gym{/} has increased to {bad}$[hw_debt_amount]{/}."
    ""
    "Should I pay him?"
    ""
    choice("hw_pay_debt",cost=[("money",hw_debt_amount)]) "Pay Off Debt"
    choice("hw_do_not_pay") "Don't Pay Off Debt"
  return

label hw_pay_debt:
  $game_bg="home workspace"
  header "The Collection Agent Comes to the Shop"
  $hw_equipment_level+=1                ##  increment equipment level
  $hw_building_gym=0                    ##  reset variable once gym built to prevent doing it again!
  $hw_workout_ap_cost=2                 ##  more intensive workout in home gym
  $hw_cannot_pay=0                      ##  reset flag since debt is paid
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel_mods home_workout hw_305"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_306"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "You tell the man to wait while you go get the money. You return from your bedroom and hand the man a large stack of money to pay your debt."
  ""
  ""
  ""
  ""
  "After receiving payment the collection agent counts the money. When he's satisfied that it's all there he leaves."
  ""
  choice("<<<") "Continue"
  return

label hw_do_not_pay:
  $game_bg="home workspace"
  header "The Collection Agent Comes to the Shop"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(308,310)              ##  first image random selection - talks
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(311,313)              ##  second image random selection - leaves and thinking
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  if hw_debt_amount*hw_homegym_interest<hw_homegym_maxdebt:         ##  next week will still be less than your debt
    "You tell the man you aren't paying the debt today. He says; {say}It's your choice but I would pay off the debt if I were you. If the{/} {bad}debt exceeds $[hw_homegym_maxdebt]{/} {say}a different man will come to your shop and you really,{/} {bad}REALLY{/} {say}don't want to see him{/}."
    ""
    ""
    "He kept staring at me for a minute and then he turned around and left."
    ""
    "You remember the picture the contruction boss showed you with a similar warning. {mark}I better pay up!{/}"
    ""
  else:                                             ##  NEXT WEEK WILL EXCEED THE MAXIMUM DEBT
    ""
    "You tell the man you aren't paying the debt today. The man stares at me for a minute and then says; {say}You just made a big,{/} {bad}BIG mistake{/}{say}. You can't say you weren't warned.{/}"
    ""
    ""
    "Without saying anything else he turned around and left."
    ""
    "They said there would be severe consequences if I exceed the debt limit. {mark}I think I'm in trouble!{/}"
    ""
  choice("<<<") "Continue"
  return
  
label hw_bad_ending:
  $set_interaction("ending")
  $act["ending_type"]="bad"
  $game_bg="black"
  ""
  "executed 'hw_bad_ending'"
  ""
  $exit_main_loop=True
  return

##====================FUNCTIONS FOR CALCULATING DAILY FITNESS LOSS, FITNESS LEVEL, AND BEDROOM TOY

label hw_fitness_update:         ##  Daily loss of strength and stamina, calculate fitness level

## Added in version 0.4.n for Ray's Bot Boutique and Ray's Online
## 0.15.n moved next 2 lines to sleep functions in 'home_rest.rpy' and 'friends_with_benefits.rpy'
##  $rays_already_visited=0          ## reset visit flag so you can only go once an evening
##  $rays_online_bot_list=0          ## reset flag so new bot list is generated when online store opened

  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  if hw_workouts_today>=1:                     ##  one or more workouts yesterday
    $hw_imagenumber=random.randint(336,338)              ##  first image random selection - talks
  else:
    $hw_imagenumber=random.randint(4,6)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel_mods home_workout hw_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  $hw_imagenumber=random.randint(1,3)        ##  SEMI-HARD CODE - SIMPLE - NEED MIN/MAX LATER
  $action_image="squirrel botshop sq_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  if hw_first_workout==0:        ##  NEVER worked out means no strength and stamina to lose
    ""
    "Time to get out of bed and start a new day."
    ""
    "I still feel tired, maybe I should start working out to get in better shape."
    ""
    ""
    "Let's start the day with a cup of coffee, I need something to wake me up."
    ""
  elif hw_workouts_today>=1:     ##  you did at least one workout today
    $hw_last_workout=0           ##  reset the last workout counter
    ""
    "Time to get out of bed and start a new day."
    ""
    "I feel great this morning since I worked out yesterday!"
    ""
    ""
    "After my morning coffee I'll be ready to get a lot done today."
    ""
  else:                          ##  you did not work out today (and have worked out at least once)
    $hw_last_workout+=1          ##  increment the 'days since last workout' counter
    ""
    "Time to get out of bed and start a new day."
    ""
    "I feel sluggish this morning, maybe it's because I didn't work out yesterday."
    ""
    ""
    "Let's start the day with a cup of coffee, I need to get some work done today."
    ""
    if mc.strength.level_name=="F":
      $hw_skill_impact=hw_level_f_base_loss
    elif mc.strength.level_name=="E":
      $hw_skill_impact=hw_level_e_base_loss
    elif mc.strength.level_name=="D":
      $hw_skill_impact=hw_level_d_base_loss
    elif mc.strength.level_name=="C":
      $hw_skill_impact=hw_level_c_base_loss
    elif mc.strength.level_name=="B":
      $hw_skill_impact=hw_level_b_base_loss
    elif mc.strength.level_name=="A":
      $hw_skill_impact=hw_level_a_base_loss
    elif mc.strength.level_name=="S":
      $hw_skill_impact=hw_level_s_base_loss
    $hw_skill_value=round(hw_skill_impact*hw_last_workout**hw_fudgefactor_loss,2)
    $hw_min_value=hw_skill_value*0.85
    $hw_max_value=hw_skill_value*1.15
    $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
    if mc.strength.level_name!="F" or mc.strength.xp!=0:
      $mc.give_xp("strength",hw_entry_value)         ##  real version after testing
    if mc.stamina.level_name=="F":
      $hw_skill_impact=hw_level_f_base_loss
    elif mc.stamina.level_name=="E":
      $hw_skill_impact=hw_level_e_base_loss
    elif mc.stamina.level_name=="D":
      $hw_skill_impact=hw_level_d_base_loss
    elif mc.stamina.level_name=="C":
      $hw_skill_impact=hw_level_c_base_loss
    elif mc.stamina.level_name=="B":
      $hw_skill_impact=hw_level_b_base_loss
    elif mc.stamina.level_name=="A":
      $hw_skill_impact=hw_level_a_base_loss
    elif mc.stamina.level_name=="S":
      $hw_skill_impact=hw_level_s_base_loss
    $hw_skill_value=round(hw_skill_impact*hw_last_workout**hw_fudgefactor_loss,2)
    $hw_min_value=hw_skill_value*0.85
    $hw_max_value=hw_skill_value*1.15
    $hw_entry_value=round(random.uniform(hw_min_value,hw_max_value),2)
    if mc.stamina.level_name!="F" or mc.stamina.xp!=0:
      $mc.give_xp("stamina",hw_entry_value)            ##  real version after testing
  $hw_previous_max_energy_base=mc.max_energy_base
  call hw_update_fitness
  if hw_previous_max_energy_base>mc.max_energy_base:   ##  level went down from nightly loss
    ""
    "You know what they say: Use it or lose it!"
    "{bad}Lost 1 AP per turn{/}"
    ""
  elif hw_previous_max_energy_base<mc.max_energy_base:
    "These workouts are really making a difference!"
    "{good}Gained 1 AP per turn{/}"
    ""
  $hw_workouts_today=0            ##  reset the workouts today counter for the new day
##  choice("<<<") "Continue"
  return

label hw_update_fitness:          ##  only allow 1 level increase/decrease each night, in this mod 2 cannot happen anyway
  $hw_fitness_level=mc.strength.level+mc.stamina.level
  if hw_fitness_level<=4:         ##  condition for 5 AP is 0 to 4 - minimum AP - FF to EE
    if mc.max_energy_base>=6:
      $mc.max_energy_base-=1
  elif hw_fitness_level<=7:       ##  condition for 6 AP is 5 to 7 - DE to CD
    if mc.max_energy_base>=7:
      $mc.max_energy_base-=1
    elif mc.max_energy_base<=5:
      $mc.max_energy_base+=1
  elif hw_fitness_level<=10:       ##  condition for 7 AP is 8 to 10 - CC to BB
    if mc.max_energy_base>=8:
      $mc.max_energy_base-=1
    elif mc.max_energy_base<=6:
      $mc.max_energy_base+=1
  elif hw_fitness_level<=13:       ##  condition for 8 AP is 11 to 13, - AB to SA
    if mc.max_energy_base>=9:
      $mc.max_energy_base-=1
    elif mc.max_energy_base<=7:
      $mc.max_energy_base+=1
  elif hw_fitness_level>=14:       ##  condition for 9 AP is 14 - maximum AP - SS only
    if mc.max_energy_base<9:
      $mc.max_energy_base+=1
##  DELETED FOLLOWING LINE IN VERSION 0.2.0 - MOVED FUNCTION TO 'mc.rpy' BY UPDATING 'mc(self).max_energy'
##  $mc.energy=mc.max_energy_base    ##  set energy to new level
  return

label hw_bedroom_toy:
  $assistants=active_bots_with_role_tag("bedroom_toy")
  if assistants:
    $hw_bedroomtoyflag=1
  else:
    $hw_bedroomtoyflag=0
  $assistants=None
  return

##====================FINAL MESSAGE AFTER BUYING EVERYTHING

label hw_done_message:
  $game_bg="home bg"             ##  home background
  header "Home - Bedroom"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel_mods home_workout hw_333"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel_mods home_workout hw_334"    ##  HARD CODE - SINGLE USE
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  "I received a message from Rocky's which says:"
  ""
  "{say}Congratulations! You have purchased our home gym and Rocky's entire portfolio of home exercise equipment. Your Rocky's sales rep will no longer visit your shop on Wednesday afternoons.{/}"
  ""
  "{say}Since you've purchased both the home gym and the punching bag we hope you continue taking advantage of our excellent yoga and boxing training bots.{/}"
  ""
  "{say}Thank you for being a Rocky's customer, we hope you enjoy keeping in shape!  Stay healty, stay strong!{/}"
  ""
  $hw_bought_everything=1    ##  SET FLAG SO SALESMAN DOES NOT COME AGAIN
  choice("<<<") "Continue"
  return