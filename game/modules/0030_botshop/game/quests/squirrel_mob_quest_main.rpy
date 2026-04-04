init python:
## NOTE: Bot salesman was moved to 'store_raysbotshop.rpy' in version 0.4.n
  mobprotection_luxury_bot_flag=0             ## 0= no visit yet, 1-5=young guy/old man, 6=done, bought bot
  mp_found_female_bot=0                       ##ADDED in v0.1.2 with male bots, kid/old man need to deliver a female bot!!!

##  Flag Variables for handling 'no empty capsule' - will be no empty location as of 0.4.n
  mobprotection_clear_capsule_flag=0          ## flag for young guy/old man

##  NOTE: Bot criteria are reset during execution, values here irrelevant
  mobprotection_bot_rating="1"                ## initial values NOT used
  mobprotection_part_rating=""                ## OMIT THIS LINE FOR VANILLA VERSION, Part Rating reverse logic
  mobprotection_part_test_pass=1              ## OMIT THIS LINE FOR VANILLA VERSION
  mobprotection_combat_skill="FEDCBAS"
  mobprotection_electronics_skill="FEDCBAS"
  mobprotection_mechanics_skill="FEDCBAS"
  mobprotection_sex_skill="FEDCBAS"
  mobprotection_social_skill="FEDCBAS"
  mobprotection_integrity_minimum=100
  mobprotection_stability_minimum=100
  
##  NOTE: If no bot to give pay instead: increments each time for difficulty, never allowed twice in a row
  mobprotection_payment=100000
  mobprotection_payment_increment=100000
  mobprotection_payment_flag=0                ##  1 when payment made
  
##  NOTE: Special Bot criteria are SET HERE and NEVER CHANGE
  mobprotection_delivered_special_bot=0          ##  1 when delivered
  mobprotection_special_bot_rating=5             ##  B
  mobprotection_special_bot_part_rating="FEDCB"  ##  A+  OMIT THIS LINE FOR VANILLA VERSION, Part Rating reverse logic
  mobprotection_special_bot_part_test_pass=1     ##  flag  OMIT THIS LINE FOR VANILLA VERSION
  mobprotection_special_bot_sex_skill="AS"
  mobprotection_special_bot_social_skill="AS"
  mobprotection_special_bot_integrity_minimum=100
  mobprotection_special_bot_stability_minimum=100

##  variable added for graphics, need to know which event is being processed to select pictures
  mobprotection_current_event=0                  ## will be set in each event function

  class Quest_mobprotection(Quest):
    payment_day="Friday"
    name="Mob Protection(SL)"
    class phase_1_extortion1:
      description="""
        Now that my business is established I wonder if the local mob is going to notice me. I sure hope not!

        """

    class phase_2_extortion2:  ##  describe Combat Bot level 1
      description="""
        The mobsters demanded I give them a bot like this {mark}next Friday{/}.

        Bot: {mark}Female, D+{/}
        {b}Combat{/} Skill: {mark}D+{/}
        All Parts: {mark}D+{/}
        Integrity: {mark}100%{/}
        Stability: {mark}100%{/}

        I better do this right or they'll probably kill me!

        """
    class phase_3_extortion3:  ##  describe Sex Bot level 1
      description="""
        The mobsters demanded I give them a bot like this {mark}next Friday{/}.

        Bot: {mark}Female, D+{/}
        {b}Sex{/} Skill: {mark}D+{/}
        All Parts: {mark}D+{/}
        Integrity: {mark}100%{/}
        Stability: {mark}100%{/}

        I better do this right, I don't want the pervert boss to be mad at me!

        """
    class phase_4_extortion4:  ##  describe Combat Bot level 2
      description="""
        The mobsters demanded I give them a bot like this {mark}next Friday{/}.

        Bot: {mark}Female, D+{/}
        {b}Combat{/} Skill: {mark}C+{/}
        All Parts: {mark}C+{/}
        Integrity: {mark}100%{/}
        Stability: {mark}100%{/}

        I better do this right or they'll probably kill me!

        """
    class phase_5_extortion5:  ##  describe Sex Bot level 2
      description="""
        The mobsters demanded I give them a bot like this {mark}next Friday{/}.

        Bot: {mark}Female, D+{/}
        {b}Sex{/} Skill: {mark}C+{/}
        All Parts: {mark}C+{/}
        Integrity: {mark}100%{/}
        Stability: {mark}100%{/}

        I better do this right, I don't want the pervert boss to be mad at me!

        """
    class phase_6_extortion6:  ##  describe Techie Bot level 1
      description="""
        The mobsters demanded I give them a bot like this {mark}next Friday{/}.

        Bot: {mark}Female, D+{/}
        {b}Electronics{/} Skill: {mark}B+{/}
        {b}Mechanics{/} Skill: {mark}B+{/}  
        All Parts: {mark}D+{/}
        Integrity: {mark}100%{/}
        Stability: {mark}100%{/}

        I think the mob plans to use this bot to handle their computer systems.
        Maybe I could get access to their data? I need to get out of this mess somehow.

        """
    class phase_7_extortion7:  ##  describe Combat Bot level 3
      description="""
        The mobsters demanded I give them a bot like this {mark}next Friday{/}.

        Bot: {mark}Female, C+{/}
        {b}Combat{/} Skill: {mark}B+{/}
        All Parts: {mark}B+{/}
        Integrity: {mark}100%{/}
        Stability: {mark}100%{/}

        I better not mess with their combat bots, they'd probably kill me!

        """
    class phase_8_extortion8:  ##  describe Sex Bot level 3
      description="""
        The mobsters demanded I give them a bot like this {mark}next Friday{/}.

        Bot: {mark}Female, C+{/}
        {b}Sex{/} Skill: {mark}B+{/}
        All Parts: {mark}B+{/}
        Integrity: {mark}100%{/}
        Stability: {mark}100%{/}

        I think I should use a {mark}B+ bot{/} with {mark}A+ parts{/} and {mark}A+ sex skill{/} to make sure the boss likes the bot.
        Plus I should give her {mark}A+ social skill{/} and maybe she will be able to help me get out of this mess.

        """

    class phase_9_extortion9:  ##  describe Combat Bot level 3
      description="""
        The mobsters demanded I give them a bot like this {mark}next Friday{/}.

        Bot: {mark}Female, C+{/}
        {b}Combat{/} Skill: {mark}B+{/}
        All Parts: {mark}B+{/}
        Integrity: {mark}100%{/}
        Stability: {mark}100%{/}

        I better not mess with their combat bots, they'd probably kill me!

        """
##  keep looping through 8 and 9 until the special bot is delivered

##  phase 10 activated when special sex bot delivered, duplicate combat bot demand description
##  when phase 10 event fires mobsters don't show, go to phase 11

    class phase_10_extortion10:
      description="""
        The mobsters demanded I give them a bot like this {mark}next Friday{/}.

        Bot: {mark}Female, C+{/}
        {b}Combat{/} Skill: {mark}B+{/}
        All Parts: {mark}B+{/}
        Integrity: {mark}100%{/}
        Stability: {mark}100%{/}

        I better not mess with their combat bots, they'd probably kill me!

        """

##  phase 11 activated when mobsters don't show up
##  when phase 11 event fires quest ends

    class phase_11_extortion11:
      description="""
        The three mobsters didn't show up last Friday. I'm not complaining but I wonder why?

        Maybe they'll be back next week, I should have their bot ready just in case. It sure would be great if they never came back though!

        """

    class phase_1000_mobprotection_done:
      description="The last bot you gave them brought down the entire mob so you don't have to build bots for them any longer!"
      
    class phase_2000_mobprotection_failed:
            description="You didn't deliver bots and couldn't pay so they destroyed your shop."

##=========BORDER WITH EVENT HANDLER==========

init python hide:
  @event_handler("time_advanced")
  def mobprotection_event():
    if now("morning"):                                ##  Restrict quest start to morning
      if quests.exiled_engineer.finished:             ##  Only start once 'Exiled Engineer' is finished (actual quest is 'Framed!', left code alone)
        if not quests.mobprotection.started:          ##  To prevent starting quest again
          queue_event("mobprotection_start_event")    ##  THIS FUNCTION MUST INCLUDE A START QUEST LINE
    if now("friday","evening"):
      if quests.mobprotection=="extortion1":
        queue_event("quest_mobprotection_event1")
      elif quests.mobprotection=="extortion2":
        queue_event("quest_mobprotection_event2")
      elif quests.mobprotection=="extortion3":
        queue_event("quest_mobprotection_event3")
      elif quests.mobprotection=="extortion4":
        queue_event("quest_mobprotection_event4")
      elif quests.mobprotection=="extortion5":
        queue_event("quest_mobprotection_event5")
      elif quests.mobprotection=="extortion6":
        queue_event("quest_mobprotection_event6")
      elif quests.mobprotection=="extortion7":
        queue_event("quest_mobprotection_event7")
      elif quests.mobprotection=="extortion8":
        queue_event("quest_mobprotection_event8")
      elif quests.mobprotection=="extortion9":
        queue_event("quest_mobprotection_event9")
      elif quests.mobprotection=="extortion10":
        queue_event("quest_mobprotection_event10")
      elif quests.mobprotection=="extortion11":
        queue_event("quest_mobprotection_event11")
    if now("afternoon"):                                  ##..luxury bot offers - young guy/old man is daily BUT dealer is only tuesday afternoon
      if not mobprotection_luxury_bot_flag==6:            ##  'not 6' = true means young guy/old man bot still in play
##        queue_event("quest_mobprotection_event12")        ##  TEMPORARY FOR TESTING!!! Replace with following 6 lines after testing
        if quests.mobprotection=="extortion8":            ##  phase 8 is when first Sex Bot 3 is requested
          queue_event("quest_mobprotection_event12")
        elif quests.mobprotection=="extortion9":          ##  phase 9 is when Combat Bot 3 is requested, this one is repeated
          queue_event("quest_mobprotection_event12")
        elif quests.mobprotection=="extortion10":         ##  phase 10 is when Sex Bot 3 is requested again, this one is repeated
          queue_event("quest_mobprotection_event12")

##  ADDED IN SR24 0.4.n to make sure old man doesn't stop until you've bought the bot
        elif quests.mobprotection=="extortion11":         ##  phase 11 is waiting for conclusion
          queue_event("quest_mobprotection_event12")
        elif quests.mobprotection=="mobprotection_done":  ##  finished quest, phase 1000
          queue_event("quest_mobprotection_event12")
    if mobprotection_clear_capsule_flag==1:               ##  capsules were full when trying to buy first bot
      queue_event("quest_mobprotection_event13")          ##  young guy/old man situation ONLY
  return

##============================START QUEST FUNCTION=======================

label mobprotection_start_event:
  $game_bg="home workspace"
  header "Visit from a Neighbor"
  ##  GRAPHICS - 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_1" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_2"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_3"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_4"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_5"
  center "{image=[action_image]@400x600}"
  ##  TEXT - on right and aligned with pictures
  $act.set_block("c")
  "While I was working {mark}[gn_store_owner_name]{/} who owns the corner store came in with a smile on her face and said:"
  ""
  "{say}Hi, haven't seen you in a while. Your shop is looking pretty good.{/}"
  ""
  ""
  "She leaned on my desk and we chatted for a little while. {mark}[gn_store_owner_name]'s{/} pretty cute and it was fun talking with her! The shop is sort of lonely sometimes. After a while she leaned in and asked quietly:"
  ""
  ""
  ""
  "{say}Has the mob come in to bother you yet? I've been forced to pay them for 'protection' for years. It makes it difficult to stay in business around here.{/}"
  ""
  ""
  ""
  "Her question surprised me, I don't know anything about the local mob. When I told her I didn't know what she was talking about she quickly turned around and started to leave the shop."
  ""
  ""
  "{mark}[gn_store_owner_name]{/} turned around as she left and had fear in her voice when she said:" 
  ""
  "{say}Sorry, forget I said anything.{/}"
  ""
  "I wonder what she's talking about?"
  ""
## 0.11.n added relationship gain with limit to prevent FWB
  $global mc_so_value
  if mc_so_value<50:                                  ## do NOT allow FWB until FWB quest end
    call mc_update_relation(gn_store_owner_name,1,0)  ## relationship gain for visiting
  $quests.start_quest("mobprotection")     ##  starts the quest, shouldn't happen twice!!
  $gn_store_owner_rename=1
  choice("continue") "Continue"
  return

##==========================================BORDER WITH EVENT FUNCTIONS=======================

label quest_mobprotection_event1:    ##  preamble finished, no comments
  $mobprotection_current_event=1
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_6" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_7"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_8"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_9"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_10"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  "Three shady looking guys come into your shop, an old small guy with a cigar and two huge goons that don't even look real! The big guys are really scary and they are obviously carrying! The small guy walks up to me and says:"
  ""
  "'{say}We've heard you're pretty good at building bots. It would be a shame if something happened to your nice little shop. If you build us bots we'll be happy to{/} {mark}protect{/} {say}your nice little shop so it doesn't{/} {mark}accidentally blow up{/}{say}. We'll be back{/} {mark}next Friday evening{/} {say}to collect a bot like this.{/}'"
  ""
  ""
  "He reaches into his jacket and pulls out a piece of paper. After glancing at the paper he glares at me and hands it over. The paper has requirements for a bot:"
  ""
  ""
  ""
  "Bot: {mark}Female, D+{/}"
  "{b}Combat{/} Skill: {mark}D+{/}"
  "All Parts: {mark}D+{/}"
  "Integrity: {mark}100%%{/}"
  "Stability: {mark}100%%{/}"
  ""
  ""
  "After handing you the paper he glares at me menicingly and all three guys leave your shop. They seemed serious, maybe I should build them a bot by {mark}next Friday{/}."
  ""
  "I put the paper into the Journal so I can look it up later if I forget."
  ""
##Combat Bot 1
  $mobprotection_bot_rating=3                 ##  D+
  $mobprotection_part_rating="FE"             ##  D+     ##  OMIT FOR VANILLA VERSION, Part Rating reverse logic
  $mobprotection_combat_skill="DCBAS"         ##  D+
  $mobprotection_electronics_skill="FEDCBAS"  ##  Any
  $mobprotection_mechanics_skill="FEDCBAS"    ##  Any
  $mobprotection_sex_skill="FEDCBAS"          ##  Any
  $mobprotection_social_skill="FEDCBAS"       ##  Any
  $mobprotection_integrity_minimum==100       ##  100%
  $mobprotection_stability_minimum==100       ##  100%
  $quests.mobprotection.advance()
  choice("mob_bad_story") "Continue"
  return

label mob_bad_story:                              ## store owner sees mob visit your shop, tells you bad story about mob
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")

  $action_image= "quests mob_protection mp_197"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_198"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_199"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_200"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_201"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_202"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")                             ## TEMP TEXT!!!!!
  "Right after they left {mark}[gn_store_owner_name]{/} came into the store looking scared and asks:"
  "{size=-12} {/}"
  "{say}I just saw those guys leave, are you OK? What did they say to you?{/}"
  ""
  "I decided to trust {mark}[gn_store_owner_name]{/} and told her what they said:"
  "{size=-12} {/}"
  "{mcsay}They demanded that I give them a bot. The big guys looked like bad news but I can't afford to give away bots.{/}"
  ""
  "{mark}[gn_store_owner_name]{/} looks frightened and says:"
  "{size=-12} {/}"
  "{say}You have to{/} {mark}[mc.name]{/}{say}! That vacant lot on the next block used to be{/} {mark}Billy's Scooters Store{/} {say} but Billy decided not to pay. He died in his store when it exploded!{/}"
  ""
  "I've seen that empty lot, that's pretty scary! {mark}[gn_store_owner_name]{/} continued:"
  "{size=-12} {/}"
  "{say}The last tenent here wouldn't pay and one day the building was empty and he was gone! No one knows what happened to him. Please do what they say, I don't want anything to happen to you!{/}"
  ""
  "I guess these guys are serious! I tell {mark}[gn_store_owner_name]{/}:"
  "{size=-12} {/}"
  "{mcsay}OK, you convinced me. I'll give them the bot they demanded.{/}"
  ""
  "{mark}[gn_store_owner_name]{/} looks relieved and says:"
  "{size=-12} {/}"
  "{say}Good, I don't want you to disappear like the last guy! Sorry, I need to get back to my store, see you later.{/}"
  ""
  "After she left I thought about the situation. I can't give away bots forever, I have to find some way to get out of this. I considered building combat bots and fighting but I have no idea how big this mob is so I better not take the risk. {mark}I have to think of a different way{/}."
## 0.11.n added relationship gain with limit to prevent FWB
  $global mc_so_value
  if mc_so_value<50:                                  ## do NOT allow FWB until FWB quest end
    call mc_update_relation(gn_store_owner_name,1,0)  ## relationship gain for visiting
  choice("<<<") "Continue"
  return

label quest_mobprotection_event2:    ##  no previous bot to comment on
  $mobprotection_current_event=2
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_11" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_12"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_13"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "The same three guys from last week come back to the shop. I had a feeling these guys were serious! The big guys still don't look real! The small guy says:"
  ""
  ""
  ""
  "'{say}We're here to collect payment for the{/} {mark}protection{/} {say}we provided last week. Your shop has been safe from{/} {mark}accidental explosions{/} {say}hasn't it? Well, what have you got for us?{/}"
  ""
  call mobprotection_deliver_bot
  return

label quest_mobprotection_event3:    ##  comment on Combat Bot level 1 delivered last week
  $mobprotection_current_event=3
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_22" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_23"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_24"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "Once again the familiar three guys come back to the shop. The small guy walks up to me, takes a puff on his cigar, and blows smoke right in my face! After glaring at me for a minute, he says:"
  ""
  ""
  "'{say}You do good work, the combat bot you gave us last week has been working out very, very well. We do good work too, your shop didn't{/} {mark}blow up{/} {say}did it? You scratch our back and we scratch your back! So, what have you got for us this time?{/}"
  ""
  call mobprotection_deliver_bot
  return
  
label quest_mobprotection_event4:    ##  comment on Sex Bot level 1 delivered last week
  $mobprotection_current_event=4
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_30" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_31"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_32"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "The same three guys came back again, don't they have anyone else they can send? The big guys make some scary threats while the small guy says:"
  ""
  ""
  "'{say}The boss was really happy with the cute little sex bot you gave us last week. He's been smiling all week! We're back again to collect payment for the{/} {mark}protection{/} {say}we provided last week. There weren't any{/} {mark}explosions{/} {say}were there? Let's see what you've got for us this week.{/}'"
  ""
  call mobprotection_deliver_bot
  return

label quest_mobprotection_event5:    ##  comment on Combat Bot level 2 delivered last week
  $mobprotection_current_event=5
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_38" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_39"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_40"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "I guess they don't have anyone else because the same three shady looking guys came into the shop. After taking a few puffs on his cigar the small guy says:"
  ""
  ""
  "'{say}You do nice work, the combat bot you gave us is really good at convincing our competitors to leave us alone! You keep this up and we'll keep{/} {mark}protecting{/} {say}your nice little shop. So, let's see what you have for us this time.{/}'"
  ""
  call mobprotection_deliver_bot
  return

label quest_mobprotection_event6:    ##  comment on Sex Bot level 2 delivered last week
  $mobprotection_current_event=6
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_48" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_49"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_50"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "The same three shady guys came back to the shop. The small guy puffed his cigar, walked up to me and blew smoke in my face again. He waited a minute then said:"
  ""
  ""
  ""
  "'{say}The boss really likes your last sex bot, he says it really keeps him warm at night! He looked tired when he told us to keep{/} {mark}protecting{/} {say}your nice little shop. Let's see what you have for us this week.{/}'"
  ""
  ""
  call mobprotection_deliver_bot
  return

label quest_mobprotection_event7:    ##  comment on Techie Bot level 1 delivered last week
  $mobprotection_current_event=7
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_56" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_57"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_58"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "The same three shady guys came back, the big guys still don't look real and I hate the cigar smoke! As usual, the small guy is the spokesman and he says:"
  ""
  ""
  "'{say}The boss said your techie bot is saving him a ton of time cooking the books and it gives him a lot more time to play with his toy! I guess we'll keep{/} {mark}protecting{/} {say}your nice little shop. Let's see what you have for us this week.{/}'"
  ""
  call mobprotection_deliver_bot
  return

label quest_mobprotection_event8:    ##  comment on Combat Bot level 3 delivered last week (THIS ONE REPEATS!!)
  $mobprotection_current_event=8
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_64" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_65"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_66"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  "As expected, the same three shady guys came back to the shop again. They are smiling this time but I'm still tired of them! The small guy always has his smelly cigar but at least he's not blowing smoke in my face. He's sounds excited when he says:"
  ""
  "'{say}That combat bot you gave us last week is a real killer! You should see what happens to people who cross us! You keep this up and we'll be happy to keep{/} {mark}protecting{/} {say}your shop. We got a good thing going here! What did you make us this time?{/}"
  call mobprotection_deliver_bot
  return
  
label quest_mobprotection_event9:    ##  comment on Sex Bot level 3 delivered last week (THIS ONE REPEATS!!)
  $mobprotection_current_event=9
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_76" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_77"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_78"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "Once more the same three guys came back to the shop. Is it Friday again already? At least they are in a good mood! The small guy with the cigar is smiling as he says:"
  ""
  ""
  "'{say}The boss is wild about your latest sex bot, he says it keeps him warm at night! As expected, the noises coming from his room are driving us crazy. He ordered us to keep{/} {mark}protecting{/} {say}your nice little shop so let's see what you made for us this time!{/}"
  ""
  call mobprotection_deliver_bot
  return

label quest_mobprotection_event10:    ##  event fires one week after special bot delivered
  $mobprotection_current_event=10
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_92" 
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "Hey, it's Friday and this is when the mobsters usually show up. That's strange, I wonder why they aren't here? It makes me nervous, are they up to something? "
  ""
  "Maybe they'll come in later tonight? If they don't come in later it's going to be hard to sleep tonight."
  ""
  "Well I better be ready if they come in later.  If they don't come in tonight maybe they'll come back next Friday?"
  ""
  $quests.mobprotection.advance()
  choice("<<<") "Continue"
  return

label quest_mobprotection_event11:    ##  event fires one week after mobsters don't show
  $mobprotection_current_event=11
  call quest_mobprotection_good_ending_done
  return

label quest_mobprotection_event12:
  $mobprotection_current_event=12
  call quest_mobprotection_first_luxury_bot_offer
  return

label quest_mobprotection_event13:
  $mobprotection_current_event=13
  call quest_mobprotection_first_clear_capsule
  return

##======================================================== BORDER WITH CODE TO DELIVER BOTS

label mobprotection_deliver_bot:    ##  Uses global variables set at the beginning of this file
  python:
    bots=[]
    for bots_storage in (home.sexbots,workshop.sexbots):
      for bot in bots_storage:
        if bot and bot.action_allowed("sell"):
          if not bot.do_not_sell:
            if not bot["mission"]:
              if bot.chassis.integrity>=mobprotection_integrity_minimum:                     ##  tested and done
                if bot.psychocore.stability>=mobprotection_stability_minimum:                ##  tested and done
                  if bot.gender=="female" and bot.rate_level>=mobprotection_bot_rating:      ##  revised
                    if bot.bot_combat.level_name in mobprotection_combat_skill:              ##  tested and done
                      if bot.bot_electronics.level_name in mobprotection_electronics_skill:  ##  tested and done
                        if bot.bot_mechanics.level_name in mobprotection_mechanics_skill:    ##  tested and done
                          if bot.bot_sex.level_name in mobprotection_sex_skill:              ##  tested and done
                            if bot.bot_social.level_name in mobprotection_social_skill:      ##  tested and done
                              mobprotection_part_test_pass=1
                              for slot in bot.outfit_slots:
                                part=bot.item_on_slot(slot)
                                if part.rate in mobprotection_part_rating:
                                  mobprotection_part_test_pass=0
                                  break                            ##  stop testing if a failure is found, will only go on if no failures found
                              if mobprotection_part_test_pass==1:
                                bot_price=bot_price_function(bot)  ## DO NOT OMIT, FIX INDENTATION FOR VANILLA VERSION
                                bots.append([bot,bot_price])       ## DO NOT OMIT, FIX INDENTATION FOR VANILLA VERSION
    bots=bots[:12]
  if bots:
    ""
    "Good thing I have a bot for them this time! I'm sure they'd blow up my shop if I didn't."
    ""
    $bot_n=0
    while bots:
      $bot,bot_price=bots.pop(0)
      $bot_n+=1
      "#[bot_n] - {mark}[bot]{/}, model: {mark}[bot.model_name]{/}"
      choice("mobprotection_give_bot_do:{}".format(bot.id)) "Give them #[bot_n]"
  else:
    $bot=None
    ""
    ""
    ""
    "Oh shit, I don't have a bot for them! I better ask for more time."
    ""
    choice("quest_mobprotection_ask_for_time") "Ask for time"
  return

label mobprotection_give_bot_do(bot):                 ##  2 VERSIONS: THREATENING VISITS 2-7 AND NICE 8-9
  $bot=find_character(bot)
  header "Mob 'Protection'"
  if mobprotection_current_event<=7:                  ##  2-7 - GOONS THREATENING
    ##  GRAPHICS 2 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    ""
    $action_image= "quests mob_protection mp_14"      ##  does not show gurney
    center "{image=[action_image]@400x600}"
    ""
    ""
    ""
    if (mobprotection_current_event % 2)==0:          ##  even number events have a bot on the gurney, odd do not (% is python remainder function)
      $action_image= "quests mob_protection mp_15"    ##  bot on gurney
    else:
      $action_image= "quests mob_protection mp_16"    ##  no bot on gurney
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "You tell them the bot is in the back room and you will go back and get [bot.himher]. As you start to leave to get the bot the small guy says:"
    ""
    ""
    "{say}Don't get any smart ideas. We'll be waiting here{/} {mark}protecting{/} {say}your shop so don't take too long! My guys have very itchy fingers!{/}"
    ""
    ""
    "You look back as you go to the back room to get {mark}[bot]{/} and see the big guys carry very big guns!"
    ""
  else:                                               ##  8-9 REPEAT - GOONS NICE
    ##  GRAPHICS 2 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    ""
    $action_image= "quests mob_protection mp_67"      ##  does not show gurney
    center "{image=[action_image]@400x600}"
    ""
    ""
    ""
    if mobprotection_current_event==8:                ##  visit 8 has bot on the gurney
      $action_image= "quests mob_protection mp_68"    ##  bot on gurney
    else:
      $action_image= "quests mob_protection mp_69"    ##  no bot on gurney
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "You tell them the bot is in the back room and you will go back and get [bot.himher]. As you start to leave to get the bot the small guy is in a good mood and says:"
    ""
    "{say}OK kid, we'll be waiting right here taking good care of your nice little shop. You've been making good bots for us, we can't wait to see the next one so don't take too long!{/}"
    ""
    ""
    "You look back as you go to the back room to get {mark}[bot]{/} and see they didn't draw their guns this time. That's a nice change!"
    ""
  $mobprotection_payment_flag=0  ##  RESET FLAG TO BE ABLE TO PAY NEXT TIME
##  Determine if you've given them the 'Special Bot' that ends the quest
  python:
    if bot.chassis.integrity>=mobprotection_special_bot_integrity_minimum:
      if bot.psychocore.stability>=mobprotection_special_bot_stability_minimum:
        if bot.rate_level>=mobprotection_special_bot_rating:
          if bot.bot_sex.level_name in mobprotection_special_bot_sex_skill:
            if bot.bot_social.level_name in mobprotection_special_bot_social_skill:
              mobprotection_special_bot_part_test_pass=1
              for slot in bot.outfit_slots:
                part=bot.item_on_slot(slot)
                if part.rate in mobprotection_special_bot_part_rating:
                  mobprotection_special_bot_part_test_pass=0
                  break                            ##  stop testing if a failure is found, will only go on if no failures found
              if mobprotection_special_bot_part_test_pass==1:
                mobprotection_delivered_special_bot=1    ##  set special bot to delivered
  $move_sexbot(bot,None)
  $bot=None
  choice("mobprotection_demand_next_bot") "Continue"
  return

##=======================================================BORDER WITH CODE TO DEMAND NEXT BOT

label mobprotection_demand_next_bot:
##  'extortion1' - no action needed, only the preamble
##  'extortion2' - last week NOTHING,            this week Combat Bot level 1, next week Sex Bot level 1
##  'extortion3' - last week Combat Bot level 1, this week Sex Bot level 1,    next week Combat Bot level 2
##  'extortion4' - last week Sex Bot level 1,    this week Combat Bot level 2, next week Sex Bot level 2
##  'extortion5' - last week Combat Bot level 2, this week Sex Bot level 3,    next week Techie Bot level 1
##  'extortion6' - last week Sex Bot level 2,    this week Techie Bot level 1, next week Combat Bot level 3
##  'extortion7' - last week Techie Bot level 1, this week Combat Bot level 3, next week Sex Bot level 3
##  'extortion8' - last week Combat Bot level 3, this week Sex Bot level 3,    next week Combat Bot level 3 (repeated as needed)
##  'extortion9' - last week Sex Bot level 3,    this week Combat Bot level 3, next week Sex Bot level 3 (repeated as needed)

  if quests.mobprotection=="extortion2":  ##  receive Combat Bot level 1 - demand Sex Bot level 1
    header "Mob 'Protection'"
    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_17"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_18"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_19"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_20"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_21"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    "A few minutes later you return and show the bot to the gangsters. They look skeptical of the bot I built for them, I hope it's good enough. If it's not I'm sure they'll find a way to make my life miserable. Without even looking at me the small guy with the cigar says:"
    ""
    ""
    "'{say}Hey, this bot looks pretty good but it better meet our needs. If it does we'll keep{/} {mark}protecting{/} {say}your nice little shop.{/}'"
    ""
    ""
    ""
    "Without even looking at me the small guy changed the subject:"
    ""
    "'{say}The boss wants to have a little fun so we'll be back next{/} {mark}Friday evening{/} {say}to collect another bot built like this just for him.{/}'"
    ""
    ""
    "After saying that he finally turns toward me and gives me a dirty look as he hands me a paper with the requirements:"
    ""
    "Bot: {mark}Female, D+{/}"
    "{b}Sex{/} Skill: {mark}D+{/}"
    "All Parts: {mark}D+{/}"
    "Integrity: {mark}100%%{/}"
    "Stability: {mark}100%%{/}"
    ""
    "So the boss wants a toy to play with! I put the paper into the Journal so I can look it up later if I forget."
    ""

##Sex Bot 1 level 1
    $mobprotection_bot_rating=3                 ##  D+
    $mobprotection_part_rating="FE"             ##  D+     ##  OMIT FOR VANILLA VERSION, Part Rating reverse logic
    $mobprotection_combat_skill="FEDCBAS"       ##  Any
    $mobprotection_electronics_skill="FEDCBAS"  ##  Any
    $mobprotection_mechanics_skill="FEDCBAS"    ##  Any
    $mobprotection_sex_skill="DCBAS"            ##  D+
    $mobprotection_social_skill="FEDCBAS"       ##  Any
    $mobprotection_integrity_minimum==100       ##  100%
    $mobprotection_stability_minimum==100       ##  100%

    $mc.mood.give_xp(randint(-50,-30))
    $quests.mobprotection.advance()
    choice("<<<") "Continue"
    return

  elif quests.mobprotection=="extortion3":  ##  receive Sex Bot level 1 - demand Combat Bot level 2
    header "Mob 'Protection'"
    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_25"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_26"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_27"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_28"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_29"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "They all look over your sex bot and even the big goons want to reach out and touch her. They look her up and down for a while and then the small guy with the cigar says:"
    ""
    ""
    "'{say}Hey, this bot is kind of cute, you better hope that the boss thinks so too! If the boss likes it we'll keep{/} {mark}protecting{/} {say}your nice little shop.{/}'"
    ""
    ""
    ""
    "The small guy doesn't take his eyes off your sex bot while he says:"
    ""
    "'{say}We're raising the bar on the type of bot we want. We'll be back next{/} {mark}Friday evening{/} {say}to collect a bot built like this.{/}'"
    ""
    ""
    "Finally the small guy turns to me and hands me a paper that says the requirements are:"
    ""
    "Bot: {mark}Female, D+{/}"
    "{b}Combat{/} Skill: {mark}C+{/}"
    "All Parts: {mark}C+{/}"
    "Integrity: {mark}100%%{/}"
    "Stability: {mark}100%%{/}"
    ""
    "After giving me the paper he glares at me as they leave the shop. They want better combat skills, I better deliver! I put the paper into the Journal so I can look it up later if I forget."
    ""

##Combat Bot 2 level 2
    $mobprotection_bot_rating=3                 ##  D+
    $mobprotection_part_rating="FED"            ##  C+     ##  OMIT FOR VANILLA VERSION, Part Rating reverse logic
    $mobprotection_combat_skill="CBAS"          ##  C+
    $mobprotection_electronics_skill="FEDCBAS"  ##  Any
    $mobprotection_mechanics_skill="FEDCBAS"    ##  Any
    $mobprotection_sex_skill="FEDCBAS"          ##  Any
    $mobprotection_social_skill="FEDCBAS"       ##  Any
    $mobprotection_integrity_minimum==100       ##  100%
    $mobprotection_stability_minimum==100       ##  100%

    $mc.mood.give_xp(randint(-50,-30))
    $quests.mobprotection.advance()
    choice("<<<") "Continue"
    return

  elif quests.mobprotection=="extortion4":  ##  receive Combat Bot level 2 - demand Sex Bot level 2
    header "Mob 'Protection'"
    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_33"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_34"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_35"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_36"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_37"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "The three of them examine your combat bot closely. They seem skeptical, I hope she's OK. While looking at the combat bot the small guy with the cigar says:"
    ""
    ""
    ""
    "'{say}This bot looks good but it better be tough because our work is demanding. Remember, if you deliver the goods we keep{/} {mark}protecting{/} {say}your nice little shop.{/}'"
    ""
    ""
    ""
    "Although he keeps examining the combat bot, the small guy says:"
    ""
    "'{say}The boss is getting tired of the toy you gave him. We'll be back next{/} {mark}Friday evening{/} {say}to collect a better toy for him built like this.{/}'"
    ""
    ""
    "As usual, the small guy turns to me and hands me a paper with the requirements:"
    ""
    "Bot: {mark}Female, D+{/}"
    "{b}Sex{/} Skill: {mark}C+{/}"
    "All Parts: {mark}C+{/}"
    "Integrity: {mark}100%%{/}"
    "Stability: {mark}100%%{/}"
    ""
    "Just like last time, after handing you the paper he glares at me before all three guys leave. I better make a good toy to keep the boss happy! I put the paper into the Journal so I can look it up later if I forget."
    ""

##Sex Bot 2 level 2
    $mobprotection_bot_rating=3                 ##  D+
    $mobprotection_part_rating="FED"            ##  C+     ##  OMIT FOR VANILLA VERSION, Part Rating reverse logic
    $mobprotection_combat_skill="FEDCBAS"       ##  Any
    $mobprotection_electronics_skill="FEDCBAS"  ##  Any
    $mobprotection_mechanics_skill="FEDCBAS"    ##  Any
    $mobprotection_sex_skill="CBAS"             ##  C+
    $mobprotection_social_skill="FEDCBAS"       ##  Any
    $mobprotection_integrity_minimum==100       ##  100%
    $mobprotection_stability_minimum==100       ##  100%

    $mc.mood.give_xp(randint(-50,-30))
    $quests.mobprotection.advance()
    choice("<<<") "Continue"
    return

  elif quests.mobprotection=="extortion5":  ##  receive Sex Bot level 2 - demand Techie Bot level 1
    header "Mob 'Protection'"
    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_41"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_42"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_43"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_44"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_45"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_46"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_47"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "The three of them enjoy looking over the sex bot!. They all reach out to see what she feels like too! While still drooling over your sex bot the small guy says:"
    ""
    ""
    ""
    "'{say}Well it looks like you did a good job on the outside but we won't know for sure until the boss bangs her! As long as he gets his rocks off we'll keep{/} {mark}protecting{/} {say}your nice little shop.{/}'"
    ""
    ""
    ""
    ""
    "Still without taking his eyes off the sex bot the small guy says:"
    ""
    ""
    ""
    "'{say}This time it's really important for you to read the requirements. We'll be back next{/} {mark}Friday evening{/} {say}to collect a bot built like this. Don't get any stupid idea to put non-standard programming in this bot or we'll be very angry!{/}'"
    ""
    ""
    ""
    "He finally turned to look at me and hand over a paper with some unusual requirements:"
    ""
    "Bot: {mark}Female, D+{/}"
    "{b}Electronics{/} Skill: {mark}B+{/}"
    "{b}Mechanics{/} Skill: {mark}B+{/}"
    "All Parts: {mark}D+{/}"
    "Integrity: {mark}100%%{/}"
    "Stability: {mark}100%%{/}"
    ""
    "After giving me the paper he glared at me for a little while and then they left the shop. Well this is different! I guess they want a bot to run their computer systems. It would be nice to program the bot to sabotage their information but that would be too risky. I wonder what else I could do? I put the paper into the Journal so I can look it up later if I forget."
    ""

##Techie Bot level 1
    $mobprotection_bot_rating=3                 ##  D+
    $mobprotection_part_rating="FE"             ##  D+     ##  OMIT FOR VANILLA VERSION, Part Rating reverse logic
    $mobprotection_combat_skill="FEDCBAS"       ##  Any
    $mobprotection_electronics_skill="BAS"      ##  B+
    $mobprotection_mechanics_skill="BAS"        ##  B+
    $mobprotection_sex_skill="FEDCBAS"          ##  Any
    $mobprotection_social_skill="FEDCBAS"       ##  Any
    $mobprotection_integrity_minimum==100       ##  100%
    $mobprotection_stability_minimum==100       ##  100%

    $mc.mood.give_xp(randint(-50,-30))
    $quests.mobprotection.advance()
    choice("<<<") "Continue"
    return

  elif quests.mobprotection=="extortion6":  ##  receive Techie Bot level 1 - demand Combat Bot level 3
    header "Mob 'Protection'"
    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_51"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_52"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_53"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_54"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_55"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "The three goons take a long look at the techie bot but you can't tell what they're thinking. While staring at the bot the small guy says:"
    ""
    ""
    ""
    "'{say}Too bad you can't tell if a techie is any good until they do some work. As long as the boss is happy with the bot's work we'll keep{/} {mark}protecting{/} {say}your nice little shop.{/}'"
    ""
    ""
    ""
    "The small guy gets tired of looking at the bot so he looks over at me and says:"
    ""
    "'{say}Since you're so good we're upping the bar again. We'll be back next{/} {mark}Friday evening{/} {say}to collect a combat bot built like this.{/}'"
    ""
    "He walks over to me and hands me the usual paper with the requirements:"
    ""
    "Bot: {mark}Female, C+{/}"
    "Combat Skill: {mark}B+{/}"
    "All Parts: {mark}B+{/}"
    "Integrity: {mark}100%%{/}"
    "Stability: {mark}100%%{/}"
    ""
    "After handing you the paper the small guy gives me the evil eye and then they leave. At least no more smoke! I'm sure they'd kill me if I sabotaged a combat bot. I put the paper into the Journal so I can look it up later if I forget."
    ""

##Combat Bot level 3 (initial version)
    $mobprotection_bot_rating=4                 ##  C+
    $mobprotection_part_rating="FEDC"           ##  B+     ##  OMIT FOR VANILLA VERSION, Part Rating reverse logic
    $mobprotection_combat_skill="BAS"           ##  B+
    $mobprotection_electronics_skill="FEDCBAS"  ##  Any
    $mobprotection_mechanics_skill="FEDCBAS"    ##  Any
    $mobprotection_sex_skill="FEDCBAS"          ##  Any
    $mobprotection_social_skill="FEDCBAS"       ##  Any
    $mobprotection_integrity_minimum==100       ##  100%
    $mobprotection_stability_minimum==100       ##  100%

    $mc.mood.give_xp(randint(-50,-30))
    $quests.mobprotection.advance()
    choice("<<<") "Continue"
    return

  elif quests.mobprotection=="extortion7":  ##  receive Combat Bot level 3 - demand Sex Bot level 3
    header "Mob 'Protection'"
    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_59"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_60"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_61"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_62"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_63"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_47"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "The three guys look the combat bot over closely. At least this time the small guy didn't blow smoke at me! While he's still looking at the bot he says:"
    ""
    ""
    ""
    "'{say}This better be a tough bot or you're in big trouble! If it ain't tough enough we'll stop {mark}protecting{/} your nice little shop and you never know what could happen then.{/}'"
    ""
    ""
    ""
    "The small guy keeps staring at the combat bot's tits but he still says to me:"
    ""
    "'{say}The boss loved his last toy but he believes you can do better. We'll be back next{/} {mark}Friday evening{/} {say}to collect another toy.{/}'"
    ""
    "Same ritual! The small guy eventually turns his attention to me and hands me a paper with the requirements:"
    ""
    "Bot: {mark}Female, C+{/}"
    "{b}Sex{/} Skill: {mark}B+{/}"
    "All Parts: {mark}B+{/}"
    "Integrity: {mark}100%%{/}"
    "Stability: {mark}100%%{/}"
    ""
    "After they left I thought maybe I can sabotage the sex bot and get myself out of this mess! She could gather information for me! I should {mark}exceed all the requirements to keep the boss interested and make her very smart so she can gather information without getting caught{/}."
    ""
    "I put the paper {mark}along with my idea{/} into the Journal so I can look it up later if I forget."
    ""

##Sex Bot level 3 (initial version)
    $mobprotection_bot_rating=4                 ##  C+
    $mobprotection_part_rating="FEDC"           ##  B+     ##  OMIT FOR VANILLA VERSION, Part Rating reverse logic
    $mobprotection_combat_skill="FEDCBAS"       ##  Any
    $mobprotection_electronics_skill="FEDCBAS"  ##  Any
    $mobprotection_mechanics_skill="FEDCBAS"    ##  Any
    $mobprotection_sex_skill="BAS"              ##  B+
    $mobprotection_social_skill="FEDCBAS"       ##  Any
    $mobprotection_integrity_minimum==100       ##  100%
    $mobprotection_stability_minimum==100       ##  100%

    $mc.mood.give_xp(randint(-50,-30))
    $quests.mobprotection.advance()
    choice("<<<") "Continue"
    return

  elif quests.mobprotection=="extortion8":  ##  comment on Sex Bot level 3, demand Combat Bot level 3 - this will be repeated indefinately
    header "Mob 'Protection'"
    if mobprotection_delivered_special_bot==1:             ##  DELIVERING THE 'SPECIAL BOT'
    
      ##  GRAPHICS 5 fixed pictures on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_85"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_86"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_87"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_88"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_89"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_90"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_91"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      "As expected, the three guys start drooling while looking over this sex bot. They all want to get their hands on her! I trained her to hide her social skill so they won't notice anything different about her. Finally the small guy says:"
      ""
      ""
      "'{say}I'm sure the boss is really going to like this one! The noises coming from his room will keep us up all night! We'll keep{/} {mark}protecting{/} {say}your nice little shop and we'll be back next{/} {mark}Friday evening{/} {say}to collect another combat bot.{/}'"
      ""
      ""
      "As usual, the small guy keeps staring at her tits and muttering something I can't quite understand. He's so predictable! The two unreal looking goons never smile but I can tell they are enjoying themselves."
      ""
      ""
      "I wonder what they'll do if they figure out she's got high social skill? If they complain I should be able to talk my way out of it. After all, they didn't say what not to do! I'll just claim I was trying to be helpful."
      ""
      "After a long time the small guy finally tears himself away from the bot. He turns to me and hands me the usual paper saying:"
      ""
      "'{say}You do good work, kid. Here's what we want next week.{/}'"
      ""
      "Bot: {mark}Female, C+{/}"
      "{b}Combat{/} Skill: {mark}B+{/}"
      "All Parts: {mark}B+{/}"
      "Integrity: {mark}100%%{/}"
      "Stability: {mark}100%%{/}"
      ""
      ""
      "The small guy gave me a big smile and then they all left. Let's hope my special bot learns something useful so I can get myself out of this situation. It's out of my control now, nothing I can do but worry. I put the paper into the Journal so I can look it up later if I forget."
      ""
    else:                                                  ##  DELIVERING A NORMAL 'B' LEVEL SEX BOT (not 'special bot')
      ##  GRAPHICS 5 fixed pictures on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_70"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_71"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_72"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_73"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_74"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_75"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      "The three guys begin drooling while looking over your latest sex bot. They all want to get their hands on her! I'll bet their boss doesn't let them play with his toys though. Finally the small guy says:"
      ""
      ""
      "'{say}I think the boss is really going to like this one! The noises coming from his room will keep us up all night! We'll keep{/} {mark}protecting{/} {say}your nice little shop and we'll be back next{/} {mark}Friday evening{/} {say}to collect another combat bot.{/}'"
      ""
      ""
      "The small guy keeps staring at her tits and muttering something I can't quite understand. He's going to have a heart attack! The two goons never smile but I can tell they are enjoying the scenery too."
      ""
      ""
      ""
      "After a long time the small guy finally tears himself away from the bot. He turns to me and hands me the usual paper saying:"
      ""
      "'{say}You do good work, kid. Here's what we want next week.{/}'"
      ""
      "Bot: {mark}Female, C+{/}"
      "{b}Combat{/} Skill: {mark}B+{/}"
      "All Parts: {mark}B+{/}"
      "Integrity: {mark}100%%{/}"
      "Stability: {mark}100%%{/}"
      ""
      "The small guy gave me a big smile and then they all left. They're friendly now but I still need a way out of this. {mark}Sabotaging combat bots would probably get me killed though.{/} I put the paper into the Journal so I can look it up later if I forget."
      ""
##Combat Bot level 3 (repeats version, same as initial version)
    $mobprotection_bot_rating=4                 ##  C+
    $mobprotection_part_rating="FEDC"           ##  B+     ##  OMIT FOR VANILLA VERSION, Part Rating reverse logic
    $mobprotection_combat_skill="BAS"           ##  B+
    $mobprotection_electronics_skill="FEDCBAS"  ##  Any
    $mobprotection_mechanics_skill="FEDCBAS"    ##  Any
    $mobprotection_sex_skill="FEDCBAS"          ##  Any
    $mobprotection_social_skill="FEDCBAS"       ##  Any
    $mobprotection_integrity_minimum==100       ##  100%
    $mobprotection_stability_minimum==100       ##  100%

    $mc.mood.give_xp(randint(-50,-30))
    if mobprotection_delivered_special_bot==1:
      $quests.mobprotection.advance(10)
    else:
      $quests.mobprotection.advance()
    choice("<<<") "Continue"
    return

  elif quests.mobprotection=="extortion9":  ##  comment on Combat Bot level 3, demand Sex Bot level 3 - this will be repeated indefinately
    header "Mob 'Protection'"
    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_79"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_80"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_81"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_82"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_83"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_84"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    "The two big guys examine your latest combat bot with great interest. I tried hard to make this one they would like! While they examine the bot the small guy turns to me and says:"
    ""
    ""
    "'{say}I'm sure this combat bot will be great! All the assholes who defy us will never know what hit them! Don't worry, we'll keep{/} {mark}protecting{/} {say}your nice little shop and we'll be back next{/} {mark}Friday evening{/} {say}to collect another cute, sexy toy for the boss's harem.{/}'"
    ""
    "I pretend to be excited too, no point in pissing them off. They like the looks of this combat bot so I'll stick with this style when they ask for more combat bots. It will be easier that way and I can get back to running my real business faster."
    ""
    ""
    "After a while the small guy comes over and hands me a paper with the requirements:"
    ""
    "Bot: {mark}Female, C+{/}"
    "{b}Sex{/} Skill: {mark}B+{/}"
    "All Parts: {mark}B+{/}"
    "Integrity: {mark}100%%{/}"
    "Stability: {mark}100%%{/}"
    ""
    "After handing me the paper they left. To get out of this I should sabotage a sex bot so she'll gather information for me! Here's what I should do:"
    ""
    "Use a {mark}B+ bot{/} with {mark}A+ parts{/} and give her {mark}A+ sex skill{/} to keep the boss interested."
    "Give her {mark}A+ social skills{/} so she can gather information without getting caught."
    ""

##Sex Bot level 3 (repeats version, same as initial version)
    $mobprotection_bot_rating=4                 ##  C+
    $mobprotection_part_rating="FEDC"           ##  B+     ##  OMIT FOR VANILLA VERSION, Part Rating reverse logic
    $mobprotection_combat_skill="FEDCBAS"       ##  Any
    $mobprotection_electronics_skill="FEDCBAS"  ##  Any
    $mobprotection_mechanics_skill="FEDCBAS"    ##  Any
    $mobprotection_sex_skill="BAS"               ##  B+
    $mobprotection_social_skill="FEDCBAS"       ##  Any
    $mobprotection_integrity_minimum==100       ##  100%
    $mobprotection_stability_minimum==100       ##  100%

    $mc.mood.give_xp(randint(-50,-30))
    $quests.mobprotection.advance(8)    ##  This one loops back to keep the last two phases alternating indefinately
    choice("<<<") "Continue"
    return

##======================================================== BORDER WITH CODE FOR SELECTING BOTS, SUCCESS, AND FAILURE

label quest_mobprotection_ask_for_time:
  $game_bg="home workspace"
  header "Mob 'Protection'"

##  NO BOT: SET FLAG FOR TESTING "CAN'T PAY TWICE IN A ROW!!!"
##  $mobprotection_payment_flag=1
  
  if mobprotection_payment_flag==1:               ##  paid for extra week last time, initiate game over
    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_166"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_167"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_168"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "You beg them for more time but they get really, really angry! The big guys threaten you and the short guy yells at you:"
    ""
    ""
    ""
    "{say}We already gave you an extra week the last time we were here, don't you remember what we said?{/} {bad}The boss never gives two extensions in a row!{/} {say}We're out of here and without our{/} {mark}protection{/} {say}your shop could have an{/} {mark}accident{/}{say}. Good luck, you'll need it!{/}"
    ""
    ""
    ""
    "They turn around and leave the shop. They are really mad, I think I'm in trouble!"
    ""
    choice("quest_mobprotection_bad_ending_failed") "Continue"
  else:                                                 ##  pay for an extra week

##  NO BOT: INCREASE PAYMENT FOR TESTING "NOT ENOUGH MONEY TO PAY"
##    $mobprotection_payment=99999999

    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_161"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_162"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "You ask if you can have more time to build the bot for them and the short guy says:"
    ""
    "{say}That makes us very unhappy. It also makes the boss very unhappy. We can give you another week this time but it will cost you{/} {mark}$[mobprotection_payment]{/}{say}. Pay up or else we'll have to stop{/} {mark}protecting{/} {say}your shop. Who knows what might happen then.{/}"
    ""
    ""
    if mc.money>= mobprotection_payment:
      "What choice do I have?"
      choice("quest_mobprotection_make_payment",cost=[("money",mobprotection_payment)]) "Pay for Time"
    else:
      "Uh oh, I don't have that much money! What do I do?"
      choice("quest_mobprotection_beg_insufficient_money") "Continue"
  return

label quest_mobprotection_make_payment:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  ""
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_163"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_164"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_165"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "You hand over the money to the short guy and he counts it slowly and carefully. He stares at you for a while and then says:"
  ""
  "{say}OK, we'll take this to the boss and I'm sure he'll give you another week. You better have the bot we asked for when we come back next week.{/}"
  ""
  "{say}If you don't have the bot next week remember this:{/} {bad}The boss will NOT give you an extension two times in a row.{/} {say}You know what that means, right? We stop{/} {mark}protecting{/} {say}your shop and something really bad could happen!{/}" 
  ""
  "They turn and leave the shop. You breath a sigh of relief and decide you better have their bot next week."
  $mobprotection_payment+=mobprotection_payment_increment
  $mobprotection_payment_flag=1  ## SET FLAG TO PAID: NO TWO IN A ROW
  choice("<<<") "Continue"
  return

label quest_mobprotection_good_ending_done:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_93" 
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "The mobsters didn't show again. This is really strange, that's two weeks in a row. I decided to search the net to see what I could find out."
  choice("mobprotection_pressconference1") "Continue"
  return

label quest_mobprotection_beg_insufficient_money:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_166"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_167"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_168"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "You tell them you don't have that much money and they get really, really angry! The big guys threaten you and the short guy yells at you:"
  ""
  ""
  ""
  "{say}You screwed up big time kid! If you don't have our bot and you don't have any money what good are you? We're out of here and without our{/} {mark}protection{/} {say}your shop could have an{/} {mark}accident{/}{say}.{/}"
  ""
  ""
  ""
  "They turn around and leave the shop. They are really mad, I think I'm in trouble!"
  ""
  choice("quest_mobprotection_bad_ending_failed") "Continue"
  return

label quest_mobprotection_bad_ending_failed:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_169"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "This can't be good, I wonder what they're going to do? Should I leave? Where would I go?"
  ""
  ""
  ""
  "{bad}Before you can do anything there's a huge explosion!  You, your bots, and your entire shop all go up in flames!{/}"
  choice("quest_mobprotection_game_over",hint="{bad}Bad Ending{/}") "Continue"
  return

label quest_mobprotection_game_over:
  $set_interaction("ending")
  $act["ending_type"]="bad"
  $game_bg="black"
  ""
  "executed 'quest_mobprotection_bad_ending_failed'"
  ""
  $exit_main_loop=True
  return

##======================================================== BORDER WITH FIRST LUXURY BOT PURCHASE SECTION

label quest_mobprotection_first_luxury_bot_offer:
  $game_bg="home workspace"
  header "A Strange Guy Comes to the Shop"
  if mobprotection_luxury_bot_flag==0:                 ##  this is young guy first visit
    $mobprotection_luxury_bot_flag=1
    ##  GRAPHICS 5 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_116"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_117"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_118"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_119"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "A scared looking kid comes into the shop. He looks like he hasn't slept for days! He has a beat up bot he's dragging along with him."
    ""
    ""
    ""
    "I can see the bot is a {mark}luxury model{/} but it's hard to tell which one because it looks like it's been through a war. The kid comes up to me and in an excited voice says:"
    ""
    ""
    ""
    "{say}You've got to help me!{/} {bad}If I don't come up with $50,000 they'll kill me!{/} {say}I know this bot is in bad shape but it's a luxury model and I'm sure you can fix it. Please, I need the money! I'll give you this bot for{/} {mark}$50,000{/}, {say}c'mon man help me out!{/}"
    ""
    "That's a lot of money. Why should I help this guy out,it's not my problem! On the other hand maybe a luxury model is just what I need to make that special sex bot for the boss. It may not work and it's a lot of money, what should I do?"
  elif mobprotection_luxury_bot_flag==1:               ##  this is young guy second visit
    $mobprotection_luxury_bot_flag=2
    ##  GRAPHICS 1 fixed pictures on left              ##TEMPORARY FOR SIZING
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_120"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_121"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_122"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_123"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "The kid comes back looking even worse than yesterday and he's dragging the same beat up {mark}luxury bot{/} along with him. It is a luxury model but it sure looks like hell."
    ""
    ""
    ""
    ""
    "He comes up to me with panic in his eyes and in an even more excited voice says:"
    ""
    ""
    ""
    "{say}Please, no one else will help me!{/} {bad}They'll kill me tomorrow night if I don't come up with $50,000{/}! {say}It's a luxury bot, I know you can fix it up real good! C'mon man I'm desperate!{/}"
    ""
    ""
    "I sort of feel sorry for the guy, I wonder what he did? Should I help him out? It may be worth a try making a special luxury sex bot for the boss. If it doesn't work I'm out a lot of money, what should I do?"
  elif mobprotection_luxury_bot_flag==2:               ##  this is young guy third visit
    $mobprotection_luxury_bot_flag=3
    ##  GRAPHICS 1 fixed pictures on left              ##TEMPORARY FOR SIZING
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_124"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_125"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_126"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_127"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "The desperate kid comes back again looking worse than ever and he's still dragging the beat up {mark}luxury bot{/} along with him."
    ""
    ""
    ""
    ""
    ""
    "He comes up to me looking like a sad dog and says quietly:"
    ""
    ""
    ""
    "{say}I've asked everyone. I guess you'll turn me down again but I came back because I don't know where else to go.{/} {bad}They'll kill me tonight if you don't buy the bot.{/} {say}Please, I'm begging you.{/} {mark}$50,000{/}{say},what do you say?{/}"
    ""
    ""
    "Wow, this guy is really down in the dumps. I guess I would be too in his shoes. Should I do a good deed? Will making the boss a special luxury sex bot really matter? What should I do?"
  elif mobprotection_luxury_bot_flag==3:               ##  this is old guy first visit
    $mobprotection_luxury_bot_flag=4
    ##  GRAPHICS 1 fixed pictures on left              ##TEMPORARY FOR SIZING
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_128"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_129"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_130"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_131"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "An old man with a kind face comes into the shop walking slowly and pushing a wheelbarrow. I glance at the wheelbarrow and to my surprise he's got the same beat up {mark}luxury bot{/} the young guy offered me!"
    ""
    ""
    "He comes up to me slowly with a smile on his face and says:"
    ""
    "{say}I saved a young man from some thugs last night by paying his debts.{/} {bad}They would have killed him. What's this world coming to?{/} {say}I'm an old man and I can't afford this but I couldn't let them kill him. You fix bots, I'm hoping you can use this one. Will you buy it from me for{/} {mark}$50,000{/}{say}?{/}"
    ""
    "I guess that young guy wasn't kidding! Maybe the guys after him were the same guys making me give away my bots."
    ""
    "I feel bad for this kind old man but it really isn't my problem. Should I buy it to make that special luxury sex bot for the boss or not? It would really help out the old man too."
  elif mobprotection_luxury_bot_flag==4:               ##  this is old guy second visit
    $mobprotection_luxury_bot_flag=5
    ##  GRAPHICS 1 fixed pictures on left              ##TEMPORARY FOR SIZING
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_132"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_133"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_134"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_135"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "The same old man comes into the shop again. Just like yesterday he's walking slowly and pushing a wheelbarrow. Of course he has the same beat up {mark}luxury bot{/}."
    ""
    ""
    ""
    ""
    ""
    "He comes up to me with that same slow walk and says:"
    ""
    ""
    ""
    "{say}I'm sure you remember me from yesterday. You are a nice person and I'm sure you want to help me out. I'm an old man and I really need the money. I know you can fix this bot up and make a profit. All I ask is{/} {mark}$50,000{/}{say}. Please do the right thing.{/}"
    ""
    ""
    "This guys story is really getting to me. He's probably right that I could make a profit. I could also make that special luxury sex bot for the boss which might get me out of my trouble. Should I buy it?"
  elif mobprotection_luxury_bot_flag==5:               ##  this is old guy third visit and repeats until you buy the bot, no increment on flag
    ##  GRAPHICS 1 fixed pictures on left              ##TEMPORARY FOR SIZING
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_136"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_137"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_138"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_139"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "The old man with his wheelbarrow and the beat up {mark}luxury bot{/} comes into the shop again. This is really getting to me."
    ""
    ""
    ""
    ""
    ""
    "He's smiling as he comes up to me with that same slow walk and says:"
    ""
    ""
    ""
    ""
    "{say}I'm back again. I'm a patient man. I'll be back every day until you decide to do the right thing. We both know you can make a profit. Will you pay me{/} {mark}$50,000{/} {say}for this bot or will I be coming back tomorrow?{/}"
    ""
    ""
    "This guy is driving me crazy. He makes me feel guilty but it's not my problem. I could make a profit or I could also make that special luxury sex bot for the boss which might get me out of my trouble. Should I buy it?"
    ""
  if mc.money>=50000:
    choice("quest_mobprotection_buy_first_luxury_bot") "Buy the Bot"
    choice("mobprotection_refuse_first_luxury_bot") "Refuse"
  else:
    "{bad}Oops, it doesn't matter what I want to do because I don't have $50,000 anyway!{/}"
    ""
    "You tell them you don't have that kind of money and send them on their way."
    ""    
    choice("continue") "I Can't Afford It"
  return
  
label quest_mobprotection_buy_first_luxury_bot:
  header "A Strange Guy Comes to the Shop"
## CHANGE IN SR24 v0.4.n
##  if home.available_capsules>=1:
  call sr24_add_bot_ok         ## sets 'sr24_rooom_for_bot=1 if there is room
  if sr24_room_for_bot==1:     ## use this before adding a bot, make an 'else:' give a chance to make space
    if mobprotection_luxury_bot_flag<=3:               ##  KID
      ##  GRAPHICS 1 fixed pictures on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_146"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_147"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_148"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_149"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_150"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      ""
      "You tell the scared young guy that you'll buy the bot. He lights up when he hears that and says:"
      ""
      ""
      ""
      "{say}Wow man, how can I thank you! You just saved my life! If I can I'll return the favor, I'll do anything I can.{/}"
      ""
      "You tell him it's OK and tell him to wait while you get the money from your room."
      ""
      ""
      ""
      "When you return you notice that he just dropped the bot on the floor. Well it's in such bad shape that it probably didn't make any difference!"
      ""
      ""
      "Before you hand him the money you warn him that if he gets into trouble like this again you may not be able to help him. He considers what you said and then says:"
      ""
      "{say}I understand, I'll stay out of trouble.{/}"
      ""
      "After you give him the money he runs out of the shop. You take a look at the bot and realize it's going to be a lot of work because it's in worse shape than you thought. Oh well, at least I've got the tools and skills to do it."
      ""
    else:                                              ##  OLD MAN
      ##  GRAPHICS 1 fixed pictures on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_151"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_152"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_153"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_154"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_155"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      ""
      "You tell the old man that you'll buy the bot but you need to go to your room to get the money. His smile gets a little brighter when he hears that'"
      ""
      ""
      ""
      ""
      "You return with the money and hand it over. As you're handing him the money the old man says quietly:"
      ""
      ""
      ""
      "{say}Thank you young man, I knew you were a good person. Before I saved a young man's life and now you have saved an old man's life.{/}"
      ""
      ""
      ""
      "The old man holds the wheelbarrow to steady it while you pull the bot out of the wheelbarrow. While doing this he says:"
      ""
      "{say}Young man, if you ever need advice old men have life experience they can share.{/}"
      ""
      "The old man quietly leaves the shop with his empty wheelbarrow. You take a look at the bot and realize it's going to be a lot of work because it's in worse shape than you thought. Oh well, at least I've got the tools and skills to do it."
      ""
    $mc.money=mc.money-50000                           ##  subtract $50,000 to pay for the bot
    call mobprotection_generate_damaged_luxury_bot     ##  generate the bot (note that a 'luxury' bot mod may be substituted)
    $mobprotection_luxury_bot_flag=6                   ##  set the flag to 6 because you bought the bot
    choice("<<<") "Continue"                           ##  After buying bot just continue
  else:                                                ##  you need to clear out a capsule before you can buy it
    if mobprotection_luxury_bot_flag<=3:               ##  KID
      ##  GRAPHICS 1 fixed pictures on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_146"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_147"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      ""
## CHANGE IN SR24 v0.4.n
      "You tell him you're going to buy the bot but you need to clear some space for it. You tell him to come back in a few hours. He says 'OK' and then leaves the shop with the bot."
      ""
      ""
      ""
      "I need to clear space for the bot: {mark}Can I clear some space or will I have to sell a bot?{/}"
      ""
    else:                                              ##  OLD MAN
      ##  GRAPHICS 1 fixed pictures on left            ##TEMPORARY FOR SIZING
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_151"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_156"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      ""
      "You tell him you're going to buy the bot but you need to clear out a capsule to have a place to put it. You tell him to come back in a few hours. He says 'OK' and then leaves the shop with the bot."
      ""
      ""
      ""
      "I need to clear a capsule: {mark}Do I have storage space available or will I have to sell a bot?{/}"
      ""
    $mobprotection_clear_capsule_flag=1                ##  set flag so he'll come back next time
    choice("<<<") "Continue"
  return

label mobprotection_refuse_first_luxury_bot:
  header "A Strange Guy Comes to the Shop"
  if mobprotection_luxury_bot_flag<=3:                 ##  KID
    ##  GRAPHICS 1 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_140"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_141"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_142"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "You tell the young guy you're not going to buy the bot."
    ""
    ""
    ""
    ""
    ""
    "He looks terrified and begs you to change your mind but you ignore him."
    ""
    ""
    ""
    ""
    ""
    "Eventually he gives up and leaves in tears."
    ""
  else:                                                ##  OLD MAN
    ##  GRAPHICS 1 fixed pictures on left
    $act.start_block("l:440 c:content_width-440")
    $act.set_block("l")
    $action_image= "quests mob_protection mp_143"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_144"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests mob_protection mp_145"
    center "{image=[action_image]@400x600}"
    ##  TEXT on right ? about alignment
    $act.set_block("c")
    ""
    "You tell the old man you're not going to buy the bot."
    ""
    ""
    ""
    ""
    ""
    "He looks disappointed but picks up his wheelbarrow and then quietly asks you to change your mind."
    ""
    ""
    ""
    ""
    "You say 'No' and he turns around and walks out of the shop pushing his wheelbarrow."
    ""
  choice("<<<") "Continue"
  return

label quest_mobprotection_first_clear_capsule:
  $game_bg="home workspace"
  header "A Strange Guy Comes to the Shop"
  $mobprotection_clear_capsule_flag=0                  ##  reset flag so you don't repeat this!!!
## CHANGE IN SR24 v0.4.n
##  if home.available_capsules>=1:                       ##  you cleared a capsule you buy the bot
  call sr24_add_bot_ok                                 ## sets 'sr24_rooom_for_bot=1 if there is room: you cleared space for the bot
  if sr24_room_for_bot==1:                             ## use this before adding a bot, make an 'else:' you didn't clear space
    if mobprotection_luxury_bot_flag<=3:               ##  KID
      ##  GRAPHICS 1 fixed pictures on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_157"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_158"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_148"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_149"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_150"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      ""
      "After a few hours the kid selling the beat up {mark}luxury bot{/} comes back and says:"
      ""
      "{say}Are you ready to buy the bot now?{/}"
      ""
      ""
      ""
      "You tell the kid you'll buy the bot but you have to get the money from your room. The kid looks really happy."
      ""
      ""
      ""
      ""
      "When you return you notice that he just dropped the bot on the floor. Well it's in such bad shape that it probably didn't make any difference!"
      ""
      ""
      ""
      "Before you hand him the money you warn him that if he gets into trouble like this again you may not be able to help him. He considers what you said and then says:"
      ""
      "{say}I understand, I'll stay out of trouble.{/}"
      ""
      "After you give him the money he runs out of the shop. You take a look at the bot and realize it's going to be a lot of work because it's in worse shape than you thought. Oh well, at least I've got the tools and skills to do it."
      ""
    else:                                              ##  OLD MAN
      ##  GRAPHICS 1 fixed pictures on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_159"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_160"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_152"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_153"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_154"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_155"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      ""
      "After a few hours the old man selling the beat up {mark}luxury bot{/} comes back and says:"
      ""
      "{say}Are you ready to buy the bot now?{/}"
      ""
      ""
      ""
      "You tell the old man you'll buy the bot but you have to get the money from your room. The old man looks really happy."
      ""
      ""
      ""
      ""
      "You return with the money and hand it over. As you're handing him the money the old man says quietly:"
      ""
      ""
      ""
      ""
      "{say}Thank you young man, I knew you were a good person. Before I saved a young man's life and now you have saved an old man's life.{/}"
      ""
      ""
      "The old man holds the wheelbarrow to steady it while you pull the bot out of the wheelbarrow. While doing this he says:"
      ""
      "{say}Young man, if you ever need advice old men have life experience they can share.{/}"
      ""
      "The old man quietly leaves the shop with his empty wheelbarrow. You take a look at the bot and realize it's going to be a lot of work because it's in worse shape than you thought. Oh well, at least I've got the tools and skills to do it."
      ""
    $mc.money=mc.money-50000                           ##  subtract $50,000 to pay for the bot
    call mobprotection_generate_damaged_luxury_bot     ##  generate the bot (note that any 'luxury' bot mod may be substituted)
    $mobprotection_luxury_bot_flag=6                   ##  set the flag to 6 because you bought the bot
    choice("continue") "Continue"
    return
  else:                                                ##  you didn't clear the capsule, say you changed your mind
    if mobprotection_luxury_bot_flag<=3:               ##  KID
      ##  GRAPHICS 1 fixed pictures on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_157"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_141"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_142"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      ""
      "After a few hours the kid selling the beat up {mark}luxury bot{/} comes back and says:"
      ""
      "{say}Are you ready to buy the bot now?{/}"
      ""
      ""
      ""
      "You tell him you changed your mind and you don't want to purchase the bot. He looks terrified and begs you to change your mind but you ignore him."
      ""
      ""
      ""
      ""
      "Eventually he gives up and leaves in tears."
      ""
    else:                                              ##  OLD MAN
      ##  GRAPHICS 1 fixed pictures on left
      $act.start_block("l:440 c:content_width-440")
      $act.set_block("l")
      $action_image= "quests mob_protection mp_159"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_144"
      center "{image=[action_image]@400x600}"
      ""
      $action_image= "quests mob_protection mp_145"
      center "{image=[action_image]@400x600}"
      ##  TEXT on right ? about alignment
      $act.set_block("c")
      ""
      "After a few hours the old man selling the beat up {mark}luxury bot{/} comes back and says:"
      ""
      "{say}Are you ready to buy the bot now?{/}"
      ""
      ""
      "You tell him you changed your mind and you don't want to purchase the bot. He looks disappointed but picks up his wheelbarrow and then quietly asks you to change your mind."
      ""
      ""
      ""
      "You say 'No' and he turns around and walks out of the shop pushing his wheelbarrow."
      ""
    choice("continue") "Continue"
  return

label mobprotection_generate_damaged_luxury_bot:
  python:
    notify.disable()
    mp_found_female_bot=0
    while mp_found_female_bot==0:                              ##  Keep looping until a female bot is found
      found_bot=generate_bot("dump_site_scavenge","luxury")    ##  Use dump site scavenge routine, make sure you get a luxury female bot, afterwards increase damages!!!!!
      if found_bot.gender=="female":
        mp_found_female_bot=1
    for slot in found_bot.outfit_slots:
      found_bot.chassis[slot].apply_damage(1000)                ##  want severe damage: was (randint(5,125)) - this causes all parts irrepairable, perfect
    generate_bot_warranty_seals(found_bot,dump_site_generate_bot_seals_table)
    found_bot.psychocore.stability=1
    notify.enable()
## CHANGE IN SR24 v0.4.n
##  $home.add_sexbot(found_bot)
  call sr24_add_bot_do(found_bot)         ## add bot to capsule if available, storage space if necessary
  $found_bot=None
  return "default"

##===========================BORDER WITH PRESS CONFERENCE ENDING SCENES===============================

label mobprotection_pressconference1:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_94"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_95"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_96"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_97"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_98" 
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_99" 
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "I found a link to a recording of a press conference held at city hall last week about some mob bust. {mark}It started with the mayor talking but on her left are my bots!{/}"
  ""
  ""
  ""
  ""
  "The mayor introduced the guy standing next to my bots and said he's the DA in this city. Wish I could afford his tailor!  I guess he's going to tell the story."
  ""
  ""
  ""
  ""
  ""
  "The audience is pretty big, I guess this must be important! {mark}I wonder what my bots are doing there?{/}"
  ""
  ""
  ""
  ""
  "The DA is pretty boring, get to the point dude!  I guess all of this stuff happened almost two weeks ago, maybe that's why the thugs didn't show up to collect another bot."
  ""
  ""
  ""
  "These two cops busted the entire mob? Either they're really good or they had help. The thugs who came to my shop were pretty big, how'd these two cops handle them?"
  ""
  ""
  ""
  "{mark}He says that my bots were important!{/} They came to the police station offering to turn in the mob! I thought they'd come to me but instead they went directly to the police!"
  choice("mobprotection_mobbusted1") "Continue"
  return

label mobprotection_mobbusted1:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_100"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_101"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_102"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")

  ""
  "The DA said my bots told the police where the mob's hideout is and that there would be a lot of evidence there. I guess they raided their hangout first. Nice place! {mark}Hey, I recognize those two!{/}"
  ""
  ""
  ""
  "The cops burst in and the thugs went for their guns sitting on the table. Their entertainment bots scattered, {mark}I guess they don't want to get caught in the crossfire!{/}"
  ""
  ""
  ""
  ""
  "{mark}Wow, before those two giant thugs could even reach their guns the cops plugged them full of holes!{/} I guess those two won't be bothering me or anyone else again!"
  choice("mobprotection_mobbusted2") "Continue"
  return

label mobprotection_mobbusted2:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_103"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_104"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_105"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "After they knocked off the thugs they went to the room where my techie bot cooked their books. The mob sure gave her a dump to work in, what assholes! {mark}Wow, I recognize that one too!{/}"
  ""
  ""
  ""
  "The old guy looks mad but there's not much he can do about it is there! My techie bot doesn't seem too concerned, I guess she knew the cops were coming. These two cops are pretty good!"
  ""
  ""
  ""
  "The woman cop is interested in what my techie bot has been doing for the mob. I guess she's going to find out while the other cop takes the mobster out. {mark}Great, no more of his smoke in my face!{/}"
  choice("mobprotection_mobbusted3") "Continue"
  return

label mobprotection_mobbusted3:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_106"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_107"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_108"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "The last place they went is the office of the mob boss, {mark}I guess that's him with his hands all over my bot!{/} Doesn't look like he knows what's coming does it! Enjoy my bot for the last time dude!"
  ""
  ""
  ""
  "When the cops burst in he sure looked surprised! He knows he's in big, big trouble! My bot looks happy to see the cops, {mark}I guess all that social skill training I gave her really paid off!{/}"
  ""
  ""
  ""
  "Just like before, the woman cop is interested in collecting evidence. {mark}Look at all that gold! And they use stacks of cash for computer tables!{/} I'm glad the boss is done playing around with my bots!"
  choice("mobprotection_pressconference2") "Continue"
  return

label mobprotection_pressconference2:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_109"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_110"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_111"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_112"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_113"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  ""
  "The DA said that no one knows where the bots came from or why they turned against the mob but he's very happy they did. The evidence the bot's provided and what was found in the mob's hideout will put them behind bars for a long, long time."
  ""
  ""
  "After he was done talking, the DA introduced the mayor who needs to put her face in front of the crowd again. Look at her acting like she doesn't want to steal the show, of course she wants the publicity and the credit for busting the mob!"
  ""
  ""
  "At least the mayor didn't speak too long! First she thanked the 'brave police officers' who busted the mob. She's right though, I wouldn't be able to do what they did. {mark}Never thought I'd be admiring cops but this time I am!{/}" 
  ""
  ""
  "Then she turned to thank my bots and 'whoever trained them'. She said the city owes that person a great debt. Sure, like they would pay me! {mark}Look at my bot doing a curtsy, she's pretty spunky!{/} I really did a good job with her!"
  ""
  ""
  ""
  "They closed with a shot of the crowd's applause. {mark}A standing ovation!{/} I'm glad I found this recording on the net, now I know what happened."
  choice("mobprotection_afterpressconference") "Continue"
  return

label mobprotection_afterpressconference:
  $game_bg="home workspace"
  header "Mob 'Protection'"
  ##  GRAPHICS 5 fixed pictures on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image= "quests mob_protection mp_114"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests mob_protection mp_115"
  center "{image=[action_image]@400x600}"
  ##  TEXT on right ? about alignment
  $act.set_block("c")
  "{good}Wow! The entire mob was busted and they are all going to jail!{/} My plan didn't go exactly as I expected it to but the outcome is great! I'm glad the mob won't bother me or anyone else again!"
  ""
  ""
  ""
  "I better not brag about building these bots for the mob, it could backfire on me. I gave the mob combat bots too and I don't want to be blamed for anything they did!"
  ""
  $quests.mobprotection.finish()
## 0.11.n added call to update mc's business skill
  call mc_update_business
  choice("<<<") "Continue"
  return