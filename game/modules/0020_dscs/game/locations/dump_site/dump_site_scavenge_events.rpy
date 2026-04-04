define dump_site_scavenge_bot_keep_cpu_chance=33
define dump_site_scavenge_bot_wiped=50            ## added in 0.8.1 for change to disconnect bot skills from the CPU - wiped means bot won't have skills

## added in 0.10.n for defective bot
define db_high_chance=4
define db_med_chance=3
define db_low_chance=2
define db_psychocore_decay=15.165
define db_part_damage=11.165

##  ADDED BY SQUIRREL: PARTS CAN CHANGE RANDOMLY WHEN BOTS ARE SCAVENGED PLUS "MISSING PARTS"
##  VARIABLES ALSO USED IN FLEA MARKET BUY BOT
define new_part_id="sr"          ##  new part id
define new_part_level=1          ##  new part level
define new_part_name="a"         ##  new part name
define old_part_id="sr"          ##  old part id
define old_part_level=1          ##  old part level
##define old_part_name="a"         ##  old part name - this one wasn't needed
define working_slot="a"          ##  slot being worked on

## updated in 0.8.1
define dump_site_generate_bot_mind_table=[
  ["bot_combat",(-80000,15000)],
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

init python hide:
  @random_event("dump_site_scavenge")
  def dump_site_scavenge_none():
    return "dump_site_scavenge_nothing",100

  @random_event("dump_site_scavenge")
  def dump_site_scavenge_bot():
## CHANGE IN SR24 v0.4.name
    if home.available_capsules>0 or workshop.available_space>=1:
      return "dump_site_scavenge_bot",20+(4-game.difficulty)*10
##      return "dump_site_scavenge_bot",100000    ## this is for test purposes, makes scavenging bots a sure thing every time

  @random_event("dump_site_scavenge")
  def dump_site_scavenge_part():
    return "dump_site_scavenge_part",30+(4-game.difficulty)*20

label dump_site_scavenge_nothing:

##  INSERT PICTURES AND REFORMAT TEXT

  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(1,9)    ##  SEMI-HARD CODE - SIMPLE
  ##$action_image="locations dump_site scmc_"+str(hw_imagenumber)
  $action_image="dump_site scmc_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  ""

  "After some searching, you found nothing. Oh well, maybe next time..."
  return "default"

label dump_site_scavenge_bot:

## 0.11.3 added call to adjust male bot "all" values to ensure at least 15% of the bots scavenged are male    
##  $print "about to call 'adjust_male_bot_weights' function"
  call adjust_male_bot_weights()
  
  python:
    notify.disable()
    found_bot=generate_bot("dump_site_scavenge","all")

##    print "found bot: ",found_bot,"bot model: ",found_bot.model_id,"bot model name: ",found_bot.model_name  ##DEBUG LINE

## 0.10.n Added for 'Defective Bots' new feature inspired by Daedalron

    temp=random.randint(1,100)
    
##    temp=1                                          ## FOR TESTING ONLY! guarantees defective bot
    
    if found_bot.psychocore_stability_decay_mult==1:
      db_limit=db_med_chance
    elif found_bot.psychocore_stability_decay_mult<1:
      db_limit=db_low_chance
    else:  # must be >1
      db_limit=db_high_chance
    if temp<= db_limit:                                              ## defective bot found

##      print "BEFORE"
##      print "db_psychocore_decay: ",db_psychocore_decay
##      print "found_bot.psychocore_stability_decay_mult: ",found_bot.psychocore_stability_decay_mult
##      print "db_part_damage: ",db_part_damage
##      print "found_bot.part_damage_mult: ",found_bot.part_damage_mult

      found_bot.psychocore_stability_decay_mult=db_psychocore_decay  ## fixed value identifies defective bot
      found_bot.part_damage_mult=db_part_damage

##      print "AFTER"
##      print "db_psychocore_decay: ",db_psychocore_decay
##      print "found_bot.psychocore_stability_decay_mult: ",found_bot.psychocore_stability_decay_mult
##      print "db_part_damage: ",db_part_damage
##      print "found_bot.part_damage_mult: ",found_bot.part_damage_mult

      for slot in found_bot.outfit_slots:
        working_slot=slot
        old_part_id=found_bot.item_on_slot(working_slot)      ## part to be removed
        new_part_id=scavenge_missing_part(working_slot)       ## substitute missing part
        if new_part_id<>"abort_substitution":                 ## abort when non-standard slot
          found_bot.equip(new_part_id)
          new_part_name=found_bot.chassis[working_slot]
          new_part_name.owner=found_bot
          found_bot.add_item(new_part_name)
          found_bot.remove_item(old_part_id)
          found_bot.chassis[working_slot].apply_damage(1000)  ## CAUSES IRREPAIRABLE DAMAGE
      found_bot.inventory.clear()                             ## deletes removed parts from bot's inventory
      bot_wiped=100                                           ## psychocore never wiped, value needed for text
      process_event("generate_bot_mind",found_bot,"dump_site_scavenge",dump_site_generate_bot_mind_table)
      generate_bot_warranty_seals(found_bot,dump_site_generate_bot_seals_table)
      found_bot.psychocore.stability=random.randint(30,70)    ## reset stability so it's 'quirky' or 'glitchy'
      notify.enable()

##      print "XXX--DEFECTIVE BOT-XXX"
##      print "found_bot: ",found_bot
##      print "found_bot.outfit_slots: ",found_bot.outfit_slots
##      print "decay_mult: ",found_bot.psychocore_stability_decay_mult,"     damage_mult: ",found_bot.part_damage_mult

## End of 0.10.n insertion

## ADDED BY SQUIRREL: PARTS CAN CHANGE RANDOMLY WHEN BOTS ARE SCAVENGED PLUS "MISSING PARTS"
## Indented into 'else' clause in 0.10.n

    else:  ## 0.10.n bypassed defective bot this time

##      print "NORMAL BOT"
##      print "found_bot: ",found_bot
##      print "found_bot.outfit_slots: ",found_bot.outfit_slots
##      print "decay_mult: ",found_bot.psychocore_stability_decay_mult,"     damage_mult: ",found_bot.part_damage_mult

      for slot in found_bot.outfit_slots:
        working_slot=slot
        sr_part_weight=randint(1,100)

##        print "Replacement Loop:  slot: ",slot,"          chance: ",sr_part_weight,"          original part: ",found_bot.item_on_slot(working_slot)

        if sr_part_weight>45:                                     ##  FALL THROUGH KEEPS DEFAULT PART - 45%
          old_part_id=found_bot.item_on_slot(working_slot)
          old_part_level=old_part_id.rate_level
          if sr_part_weight<=55:                                  ##  UPGRADE 1 LEVEL - 10%
            if old_part_level<7:
              new_part_level=old_part_level+1
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)

##              print "slot: ",slot,"               old part: ",old_part_id,"               new part: ",new_part_id

              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                found_bot.equip(new_part_id)
                new_part_name=found_bot.chassis[working_slot]
                new_part_name.owner=found_bot
                found_bot.add_item(new_part_name)
                found_bot.remove_item(old_part_id)
          elif sr_part_weight<=60:                                ##  UPGRADE 2 LEVELS - 5%
            if old_part_level<6:                                  ##  can increase 2
              new_part_level=old_part_level+2
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)
              
##              print "slot: ",slot,"               old part: ",old_part_id,"               new part: ",new_part_id

              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                found_bot.equip(new_part_id)
                new_part_name=found_bot.chassis[working_slot]
                new_part_name.owner=found_bot
                found_bot.add_item(new_part_name)
                found_bot.remove_item(old_part_id)
            elif old_part_level<7:                                ##  can increase 1
              new_part_level=old_part_level+1
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)

##              print "slot: ",slot,"               old part: ",old_part_id,"               new part: ",new_part_id

              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                found_bot.equip(new_part_id)
                new_part_name=found_bot.chassis[working_slot]
                new_part_name.owner=found_bot
                found_bot.add_item(new_part_name)
                found_bot.remove_item(old_part_id)
          elif sr_part_weight<=75:                                ##  DOWNGRADE 1 LEVEL - 15%
            if old_part_level>1:                                  ##  can decrease 1
              new_part_level=old_part_level-1
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)

##              print "slot: ",slot,"               old part: ",old_part_id,"               new part: ",new_part_id

              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                found_bot.equip(new_part_id)
                new_part_name=found_bot.chassis[working_slot]
                new_part_name.owner=found_bot
                found_bot.add_item(new_part_name)
                found_bot.remove_item(old_part_id)
          elif sr_part_weight<=85:                                ##  DOWNGRADE 2 LEVELS - 10%
            if old_part_level>2:                                  ##  can decrease 2
              new_part_level=old_part_level-2
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)

##              print "slot: ",slot,"               old part: ",old_part_id,"               new part: ",new_part_id

              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                found_bot.equip(new_part_id)
                new_part_name=found_bot.chassis[working_slot]
                new_part_name.owner=found_bot
                found_bot.add_item(new_part_name)
                found_bot.remove_item(old_part_id)
            elif old_part_level>1:                                ##  can decrease 1
              new_part_level=old_part_level-1
              new_part_id=scavenge_substitute_part(working_slot,new_part_level)

##              print "slot: ",slot,"               old part: ",old_part_id,"               new part: ",new_part_id

              if new_part_id<>"abort_substitution":               ##  abort when non-standard slot
                found_bot.equip(new_part_id)
                new_part_name=found_bot.chassis[working_slot]
                new_part_name.owner=found_bot
                found_bot.add_item(new_part_name)
                found_bot.remove_item(old_part_id)
          else:                                                   ##  INSERT MISSING PART AND APPLY DAMAGE - 15%
            new_part_id=scavenge_missing_part(working_slot)

##            print "slot: ",slot,"               old part: ",old_part_id,"               new part: ",new_part_id

            if new_part_id<>"abort_substitution":                 ##  abort when non-standard slot
              found_bot.equip(new_part_id)
              new_part_name=found_bot.chassis[working_slot]
              new_part_name.owner=found_bot
              found_bot.add_item(new_part_name)
              found_bot.remove_item(old_part_id)
              found_bot.chassis[working_slot].apply_damage(1000)  ##  CAUSES IRREPAIRABLE DAMAGE IN ALL CASES

##        else:  ## DEBUGGING ONLY!!
##          print "slot: ",slot,"               keep old part: ",found_bot.item_on_slot(working_slot)

      found_bot.inventory.clear()                                ##  BUG FIX in v0.2.1 - deletes removed parts from bot's inventory

##      slot_count=0  #FOR DEBUGGING ONLY!!!

      for slot in found_bot.outfit_slots:

##        slot_count+=1  #FOR DEBUGGING ONLY!!!

##        if getattr(found_bot.chassis[slot]):
        if found_bot.chassis[slot]:

##          print "No Bug:  found_bot: ",found_bot,"          found_bot.chassis[slot]:",found_bot.chassis[slot],"          slot count: ",slot_count

          found_bot.chassis[slot].apply_damage(randint(5,125))      ##  APPLYING MORE DAMAGE TO A "MISSING" PART DOESN'T MATTER

##        else:  #FOR DEBUGGING ONLY!!!
##          print "XXX-BUG-XXX:  found_bot: ",found_bot,"          slot: ",slot,"          slot count: ",slot_count

      if randint(0,100)<dump_site_scavenge_bot_keep_cpu_chance:
        new_part_id=found_bot.item_on_slot("bot_powercore")
        if new_part_id!="bot_part_sr24_powercore_missing":        ##  DON'T "DESTROY" A MISSING PART - wrecks flag!!
          found_bot.chassis.powercore.apply_damage("destroy")
      else:
        new_part_id=found_bot.item_on_slot("bot_cpu")
        if new_part_id!="bot_part_sr24_cpu_missing":              ##  DON'T "DESTROY" A MISSING PART - wrecks flag!!
          found_bot.chassis.cpu.apply_damage("destroy")
## Change in 0.8.1 to allow bots to have skills even when the CPU is destroyed. Skills are not kept in the CPU so this doesn't make sense
## Original game had only a 33% chance of bots having skills, adding 'missing parts' reduced this to an 18% chance
## This change will make it a 50% chance - half of the people wipe bots before throwing them away and half are too lazy or stupid to do this
##    if found_bot.chassis.cpu.integrity>0:  ## OLD LINE
      bot_wiped=random.randint(0,100)
      if bot_wiped>dump_site_scavenge_bot_wiped:
        process_event("generate_bot_mind",found_bot,"dump_site_scavenge",dump_site_generate_bot_mind_table)
      generate_bot_warranty_seals(found_bot,dump_site_generate_bot_seals_table)
      notify.enable()

## end of indented section from 0.10.n change

##  INSERT PICTURES AND REFORMAT TEXT (back to Renpy code here)

  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(16,21)    ##  SEMI-HARD CODE - SIMPLE
  ##$action_image="locations dump_site scmc_"+str(hw_imagenumber)
  $action_image="dump_site scmc_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  if bot_wiped>dump_site_scavenge_bot_wiped:
    "You found a discarded bot! You quickly check, it's model {mark}[found_bot.model_name]{/} and whoever threw it away didn't {mark}wipe the psychocore{/}."
    ""
    "{good}If the bot has any skills I'll get a head start on training!{/}"
  else:
    "You found a discarded bot! You quickly check, it's model {mark}[found_bot.model_name]{/} but whoever threw it away {mark}wiped the psychocore{/} before discarding it."
    ""
    "{mark}At least the psychore will be stable.{/}"
## CHANGE IN SR24 v0.4.n
  call sr24_add_bot_do(found_bot)
##  $home.add_sexbot(found_bot)
##  $print "After calling 'sr24_add_bot_do'"
  $dump_site["scavenge_loot_now"].append(("bot",found_bot))
  $found_bot=None
  return "default"

label dump_site_scavenge_part:
  python:
    notify.disable()
    found_part=generate_bot_part("dump_site_scavenge","all")
    found_part.apply_damage(randint(5,99),minimal_integrity=1)
    notify.enable()

##  INSERT PICTURES AND REFORMAT TEXT

  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $hw_imagenumber=random.randint(10,15)    ##  SEMI-HARD CODE - SIMPLE
  ##$action_image="locations dump_site scmc_"+str(hw_imagenumber)
  $action_image="dump_site scmc_"+str(hw_imagenumber)
  center "{image=[action_image]@400x600}"
  ""
  ##  TEXT
  $act.set_block("c")
  ""
  ""

  "You found a discarded bot part, seems like it is {mark}[found_part]{/}."
  $workshop.add_item(found_part)
  $dump_site["scavenge_loot_now"].append(("part",found_part))
  $found_part=None
  return "default"


##  ADDED BY SQUIRREL: PARTS CAN CHANGE RANDOMLY WHEN BOTS ARE SCAVENGED PLUS "MISSING PARTS"
##  FUNCTIONS ALSO USED IN FLEA MARKET BUY BOT

init python:
  def scavenge_substitute_part(working_slot_f,new_part_level_f):
    if working_slot_f=="bot_cpu":
      if new_part_level_f==1:
        return "bot_part_sr24_cpu_f"
      elif new_part_level_f==2:
        return "bot_part_quadx"
      elif new_part_level_f==3:
        return "bot_part_sr24_cpu_d"
      elif new_part_level_f==4:
        return "bot_part_neurotech4"
      elif new_part_level_f==5:
        return "bot_part_sr24_cpu_b"
      elif new_part_level_f==6:
        return "bot_part_neurotech7"
      elif new_part_level_f==7:
        return "bot_part_sr24_cpu_s"
    elif working_slot_f=="bot_eyes":
      if new_part_level_f==1:
        return "bot_part_sr24_eyes_f"
      elif new_part_level_f==2:
        return "bot_part_ocu7"
      elif new_part_level_f==3:
        return "bot_part_irida"
      elif new_part_level_f==4:
        return "bot_part_sr24_eyes_c"
      elif new_part_level_f==5:
        return "bot_part_sr24_eyes_b"
      elif new_part_level_f==6:
        return "bot_part_sr24_eyes_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_eyes_s"
    elif working_slot_f=="bot_ears":
      if new_part_level_f==1:
        return "bot_part_sr24_ears_f"
      elif new_part_level_f==2:
        return "bot_part_sr24_ears_e"
      elif new_part_level_f==3:
        return "bot_part_sr24_ears_d"
      elif new_part_level_f==4:
        return "bot_part_sr24_ears_c"
      elif new_part_level_f==5:
        return "bot_part_sr24_ears_b"
      elif new_part_level_f==6:
        return "bot_part_sr24_ears_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_ears_s"
    elif working_slot_f=="bot_vocoder":
      if new_part_level_f==1:
        return "bot_part_sr24_vocoder_f"
      elif new_part_level_f==2:
        return "bot_part_sr24_vocoder_e"
      elif new_part_level_f==3:
        return "bot_part_invox"
      elif new_part_level_f==4:
        return "bot_part_sr24_vocoder_c"
      elif new_part_level_f==5:
        return "bot_part_aria"
      elif new_part_level_f==6:
        return "bot_part_sr24_vocoder_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_vocoder_s"
    elif working_slot_f=="bot_powercore":
      if new_part_level_f==1:
        return "bot_part_sr24_powercore_f"
      elif new_part_level_f==2:
        return "bot_part_sr24_powercore_e"
      elif new_part_level_f==3:
        return "bot_part_nova"
      elif new_part_level_f==4:
        return "bot_part_zeux5"
      elif new_part_level_f==5:
        return "bot_part_sr24_powercore_b"
      elif new_part_level_f==6:
        return "bot_part_sr24_powercore_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_powercore_s"
    elif working_slot_f=="bot_arms":
      if new_part_level_f==1:
        return "bot_part_arms_plastic"
      elif new_part_level_f==2:
        return "bot_part_arms_plastan"
      elif new_part_level_f==3:
        return "bot_part_sr24_arms_d"
      elif new_part_level_f==4:
        return "bot_part_arms_composite"
      elif new_part_level_f==5:
        return "bot_part_sr24_arms_b"
      elif new_part_level_f==6:
        return "bot_part_sr24_arms_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_arms_s"
    elif working_slot_f=="bot_legs":
      if new_part_level_f==1:
        return "bot_part_legs_plastic"
      elif new_part_level_f==2:
        return "bot_part_legs_plastan"
      elif new_part_level_f==3:
        return "bot_part_sr24_legs_d"
      elif new_part_level_f==4:
        return "bot_part_legs_composite"
      elif new_part_level_f==5:
        return "bot_part_sr24_legs_b"
      elif new_part_level_f==6:
        return "bot_part_sr24_legs_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_legs_s"
    elif working_slot_f=="bot_skin":
      if new_part_level_f==1:
        return "bot_part_sr24_skin_f"
      elif new_part_level_f==2:
        return "bot_part_ecoskin"
      elif new_part_level_f==3:
        return "bot_part_hardskin"
      elif new_part_level_f==4:
        return "bot_part_sr24_skin_c"
      elif new_part_level_f==5:
        return "bot_part_sr24_skin_b"
      elif new_part_level_f==6:
        return "bot_part_sr24_skin_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_skin_s"
    elif working_slot_f=="bot_implants":
      if new_part_level_f==1:
        return "bot_part_sr24_implants_f"
      elif new_part_level_f==2:
        return "bot_part_sr24_implants_e"
      elif new_part_level_f==3:
        return "bot_part_sr24_implants_d"
      elif new_part_level_f==4:
        return "bot_part_sr24_implants_c"
      elif new_part_level_f==5:
        return "bot_part_sr24_implants_b"
      elif new_part_level_f==6:
        return "bot_part_sr24_implants_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_implants_s"
    elif working_slot_f=="bot_vagina":
      if new_part_level_f==1:
        return "bot_part_sr24_vagina_f"
      elif new_part_level_f==2:
        return "bot_part_sr24_vagina_e"
      elif new_part_level_f==3:
        return "bot_part_sr24_vagina_d"
      elif new_part_level_f==4:
        return "bot_part_sr24_vagina_c"
      elif new_part_level_f==5:
        return "bot_part_sr24_vagina_b"
      elif new_part_level_f==6:
        return "bot_part_sr24_vagina_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_vagina_s"
    elif working_slot_f=="bot_penis":
      if new_part_level_f==1:
        return "bot_part_sr24_penis_f"
      elif new_part_level_f==2:
        return "bot_part_sr24_penis_e"
      elif new_part_level_f==3:
        return "bot_part_sr24_penis_d"
      elif new_part_level_f==4:
        return "bot_part_sr24_penis_c"
      elif new_part_level_f==5:
        return "bot_part_sr24_penis_b"
      elif new_part_level_f==6:
        return "bot_part_sr24_penis_a"
      elif new_part_level_f==7:
        return "bot_part_sr24_penis_s"
    else:                                   ##  IGNORE NON-STANDARD SLOTS, NO GUARANTEE REPLACEMENT PARTS EXIST
      return "abort_substitution"

init python:
  def scavenge_missing_part(working_slot_g):
    if working_slot_g=="bot_cpu":
      return "bot_part_sr24_cpu_missing"
    elif working_slot_g=="bot_eyes":
      return "bot_part_sr24_eyes_missing"
    elif working_slot_g=="bot_ears":
      return "bot_part_sr24_ears_missing"
    elif working_slot_g=="bot_vocoder":
      return "bot_part_sr24_vocoder_missing"
    elif working_slot_g=="bot_powercore":
      return "bot_part_sr24_powercore_missing"
    elif working_slot_g=="bot_arms":
      return "bot_part_sr24_arms_missing"
    elif working_slot_g=="bot_legs":
      return "bot_part_sr24_legs_missing"
    elif working_slot_g=="bot_skin":
      return "bot_part_sr24_skin_missing"
    elif working_slot_g=="bot_implants":
      return "bot_part_sr24_implants_missing"
    elif working_slot_g=="bot_vagina":
      return "bot_part_sr24_vagina_missing"
    elif working_slot_g=="bot_penis":
      return "bot_part_sr24_penis_missing"
    else:                                   ##  IGNORE NON-STANDARD SLOTS, NO GUARANTEE REPLACEMENT PARTS EXIST
      return "abort_substitution"