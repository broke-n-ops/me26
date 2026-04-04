## The conversation between Ruthie and the MC about the 3-way relationship with Simone

## uses event handler in 'business_partners.rpy'

## initialize variables

init python:
  bp_replay_conversation=0         ## option to replay conversation in hot tub, flag set to 1 for conditional branch within the scene in 'business_partners.rpy'
                                   ## set to 1 in the function when the option is presented, reset to 0 in the function you return to
                                   ## First Hot Tub Function for entry: bpdbp2_17
                                   ## Last Hot Tub Function for return:

## functions

## preparing to go

label relationship_conversation_1:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Time for a Difficult Conversation"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_1"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_2"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  ""
  "It's time to head over to {mark}[gn_store_owner_name]'s{/} to talk about last night. I need to be prepared for our conversation so before I go over I should think about what I want to say."
  ""
  ""
  ""
  ""
  "Thinking about what everyone said last night is probably the best place to start..."
  $bp_replay_conversation=1     ## set flag for replay
  choice("bpdbp2_18") "Replay"
  return
  
label relationship_conversation_2:
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "Time for a Difficult Conversation"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_3"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_4"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{size=-8} "
  "That's everything we said about relationships and I still don't know what {mark}[gn_store_owner_name]{/} is thinking or what she wants to do. I'm a little nervous about all of this but at least she didn't seem angry or upset."
  ""
  ""
  ""
  "Oh well, nothing to do but walk over to her apartment so we can talk about what we want to do."
  choice("relationship_conversation_3") "Leave Home"
  return

## arrive at Ruthie's

label relationship_conversation_3:
  $game.location="store_owner_apartment"         ## move location to Ruthie's apartment
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_5"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_6"
  center "{image=[action_image]@400x600}"
  $act.set_block("c")
  "I'm nervous as I enter {mark}[gn_store_owner_name]'s{/} apartment but she greets me enthusiasticly which makes me think this might not be so bad. We embrace and I notice there is the usual bottle of wine waiting for us on the sofa table which is certainly another good sign."
  ""
  "{size=-8} "
  "She says; {say}Hey, don't look so worried, everything is fine. Let's sit down and figure this thing out together.{/} As we sit down together I try a little humor; {mcsay}I am a little nervous, I was thinking about wearing a bullet proof vest.{/}"
  choice("relationship_conversation_4") "Continue"
  return

label relationship_conversation_4:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_7"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_8"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "She smiles and says; {say}At first I was hurt but then I was angry and if you'd been there you might have needed that vest!{/} Before I say anything she continues; {mark}[ns_teacher_name]{/} {say}helped me sort out my feelings, she's really open and honest about everything.{/}"
  ""
  "{size=-8} "
  "This sounds promising; {mcsay}From the first time I met her when she came to my shop I had a good feeling about her. Maybe I shouldn't say this but I had the biggest crush on her when I was taking her class.{/} {mark}[gn_store_owner_name] says; {say}She is pretty hot isn't she?{/}"
  choice("relationship_conversation_5") "Continue"
  return

label relationship_conversation_5:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_9"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_10"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "I'm a little surprised at {mark}[gn_store_owner_name]'s{/} last comment; {mcsay}So you think she's hot too? Is that part of this whole thing?{/} {mark}[gn_store_owner_name]{/} looks down; {say}To be honest I'm not sure, maybe it is part of it. Now it's my turn to worry, how do you feel about that?{/}"
  ""
  "{size=-12} "
  "{mark}[gn_store_owner_name]{/} looks worried as she waits for me to say something. I hadn't considered this; {mcsay}I don't know, something like this never entered my mind. It's not a bad thing, just a surprise.{/} She looks relieved; {say}I was a little afraid you'd get up and leave.{/}"
  choice("relationship_conversation_6") "Continue"
  return

label relationship_conversation_6:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_11"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_12"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "I think we both need a moment to collect our thoughts so I say; {mcsay}How about I pour each of us a glass of wine before we continue?{/} {mark}[gn_store_owner_name]{/} smiles; {say}Great idea, thanks.{/} I pour two glasses and say with a smile; {mcsay}I think we're OK, no one is bleeding yet!{/}"
  ""
  "{size=-22} "
  "We each take a sip of wine and {mark}[gn_store_owner_name]{/} smiles saying; {say}Hey, I thought all guys wanted two women at the same time and most like the idea of watching two hot women together.{/} I can tell she's joking; {mcsay}Of course, we're all perverts and that's all we ever think about!{/}"
  choice("relationship_conversation_7") "Continue"
  return

label relationship_conversation_7:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_13"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_14"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{mark}[gn_store_owner_name]{/} gets a little more serious; {say}Actually I think another woman involved is a little scary but also kind of exciting too. What do you think?{/} I consider it; {mcsay}Honestly, although it's exciting I'm not sure I can make two women happy at the same time.{/}" 
  ""
  "{size=-12} "
  "{mark}[gn_store_owner_name]{/} says; {say}I don't think you have anything to worry about, we've done it multiple times most nights and I'm sure you'd be fine.{/} She looks down before continuing; {say}I'm afraid that because {mark}[ns_teacher_name]{/} is so hot you'll lose interest in me.{/}"
  choice("relationship_conversation_8") "Continue"
  return

label relationship_conversation_8:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_15"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_16"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "I have to get that thought out of her head; {mcsay}That's not going to happen! We have a great relationship and nothing is going to change that. Yes, she's hot but you're hot too and I'm very lucky to be with you. If you don't want to do this then we won't do it.{/}"
  ""
  "{size=-12} "
  "While listening to me {mark}[gn_store_owner_name]'s{/} eyes start watering. Without saying anything she hugs me and we hold each other for a minute before she says; {say}Thank you, that makes me feel a lot better.{/} Drying her eyes she says; {say}Give me a minute{/}."
  choice("relationship_conversation_9") "Continue"
  return

label relationship_conversation_9:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_17"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_18"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{mark}[gn_store_owner_name]{/} says; {say}That was so nice, you made me very happy.{/} Then she continues; {say}We need to talk more though. In addition to being really hot {mark}[ns_teacher_name]{/} is your business partner and both of us like her a lot. This could be a good thing for all three of us.{/}"
  ""
  "{size=-12} "
  "I'm glad she's feeling better: {mcsay}I think you're right about all of that but you need to be comfortable with it, are you sure you'd be OK?{/} {mark}[gn_store_owner_name]{/} gives me smile; {say}You give me confidence, if we don't do this I think I'll regret it.{/}"
  choice("relationship_conversation_10") "Continue"
  return

label relationship_conversation_10:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_19"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_20"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{size=-20} "
  "I think we've decided so I lean over and say playfully ; {mcsay}Maybe we should both be a little daring and give this 3 person relationship a try.{/} {mark}[gn_store_owner_name]{/} hesitates but then she follows my lead; {say}Yes, you're absolutely right. Let's do this crazy thing.{/}"
  ""
  "{size=-20} "
  "I give her a brief hug and say; {mcsay}That was difficult but I think we've figured things out.{/} Then I lean back and exclaim; {mcsay}Yes! I'm really looking forward to having two hot babes at the same time! Wow, how did I get so lucky?{/}"
  choice("relationship_conversation_11") "Continue"
  return

label relationship_conversation_11:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_21"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_22"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{size=-12} "
  "{mark}[gn_store_owner_name]{/} gives me a playful look saying; {say}There's only one hot babe here right now, will that be enough for you?{/} Taking hold of her hand I say; {mcsay}You're always enough for me, we'll have many nights like this.{/}"
  ""
  "{size=-6} "
  "She fakes looking shocked; {say}Are you kidding? We'll have more conversations like this? How many teachers are there at that night school?{/} I reply; {mcsay}I think it's around 10! Well actually I think she recently hired an assistant making it 2.{/}"
  choice("relationship_conversation_12") "Continue"
  return

label relationship_conversation_12:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_23"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_24"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{size=-12} "
  "I try to explain myself; {mcsay}All I meant was that {mark}[ns_teacher_name]{/} is busy at night with her school and we're both busy during the day so there will be a lot of time for just the two of us.{/} She smiles; {say}Relax silly, I'm just teasing.{/}"
  ""
  "{size=-6} "
  "I change the subject; {mcsay}Actually there is one more thing we should discuss. {mark}[ns_teacher_name]{/} also said 'in pairs'. That includes you and I but it's also includes two other possibilities; you with her and her with me. How do you feel about these other pairs?{/}"
  choice("relationship_conversation_13") "Continue"
  return

label relationship_conversation_13:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_25"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_26"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{size=-12} "
  "After thinking for a minute {mark}[gn_store_owner_name]{/} says; {say}When {mark}[ns_teacher_name]{/} told me about you two after I calmed down we discussed jealousy. She made good points and convinced me that it's unnecessary. I'm think I'm OK with it.{/}"
  ""
  "{size=-6} "
  "She seems uncertain so I say; {mcsay}I guess time will tell but if it bothers you we need to talk about it. What about you and {mark}[ns_teacher_name]{/}?{/} She hesitates and says; {say}I don't know. I've never really thought much about other women before.{/}"
  choice("relationship_conversation_14") "Continue"
  return

label relationship_conversation_14:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_27"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_28"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{size=-22} "
  "I tell {mark}[gn_store_owner_name]{/}; {mcsay}I'm OK with you and {mark}[ns_teacher_name]{/} together but you shouldn't do anything you don't want to do.{/} Then I add; {mcsay}I know you were joking but the idea of watching you two is exciting. I guess all of us guys really are perverts!{/}"
  ""
  "{size=-6} "
  "{mark}[gn_store_owner_name]{/} smiles; {say}Well you'll just have to wait. {mark}[ns_teacher_name]{/} said she won't pressure me so nothing will happen unless I bring it up.{/} I say; {mcsay}That sounds like {mark}[ns_teacher_name]{/}, she always knows exactly what each person needs.{/}"
  choice("relationship_conversation_15") "Continue"
  return

label relationship_conversation_15:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_29"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_30"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{size=-24} "
  "{mark}[gn_store_owner_name]{/} smiles and says; {say}Yes, she is very smart and nice as well as very hot! Maybe some day I'll be ready for something like that.{/} Then she changes the subject; {say}Enough discussion, I'm really tired and I think it's bed time.{/}"
  ""
  "{size=-16} "
  "This has been a difficult evening so I give her a hug and say; {mcsay}You're right, we've had a very difficult conversation tonight and although I'm with a really hot babe both of us are tired. Maybe we should just go to sleep this time.{/}"
  choice("relationship_conversation_16") "Continue"
  return

label relationship_conversation_16:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_31"
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_32"
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{size=-12} "
  "{mark}[gn_store_owner_name]{/} says playfully; {say}Sure you say that now, but you're a pervert guy and once we're in bed I think a certain part of you will make you change your mind! If necessary I'll give that part of you a little help!{/}"
  ""
  "{size=-6} "
  "Her playfulness is making me hard; {mcsay}I think that part of me heard you and is already trying to change my mind. Let's go to bed and you can continue helping him change my mind.{/} She smiles; {say}Let's go, I have a lot to tell him!{/}"
  choice("relationship_conversation_17") "Continue"
  return

label relationship_conversation_17:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $action_image="squirrel relationship_conversation rc_33"   ## walking towards bedroom door
  center "{image=[action_image]@400x600}"
  ""
  $action_image="squirrel relationship_conversation rc_34"   ## Ruthie topless in her bedroom
  center "{image=[action_image]@400x600}"
  ""
  $act.set_block("c")
  "{size=-12} "
  "We both get up and as we head to her bedroom {mark}[gn_store_owner_name]{/} looks down at my crotch and says playfully; {say}Now if he continues to resist we will both have to work 'hard' to change his mind if you know what I mean.{/}"
  ""
  "{size=-2} "
  "When we enter her bedroom {mark}[gn_store_owner_name]{/} pulls down her top and looks down at my crotch again; {say}Let's see if these two can help us convince him to stay awake a little longer.{/} I surrender; {mcsay}I can't resist any longer, the four of you have convinced me!{/}"
  choice("relationship_conversation_18") "Continue"
  return


## sex

label relationship_conversation_18:               ## fully undressed and in bed
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(189,190)
  $action_image= "squirrel relationship_conversation rc_35"
  "{mark}[gn_store_owner_name]{/} is so sexy, I'm glad she didn't want to sleep! We help each other to get undressed and then lie down together on her bed."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She says; {say}I'm glad the four of us could convince you to stay awake!{/} I smile and reply; {mcsay}Me too, it was pretty silly of me to think we'd just go to sleep.{/}"
  choice("relationship_conversation_19") "Continue"
  return

label relationship_conversation_19:              ## blow job
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(189,190)
  $action_image= "squirrel relationship_conversation rc_36"
  "{mark}[gn_store_owner_name]{/} pushes me onto my back saying; {say}I need to reward the part of you that helped me convince you to stay awake!{/} and she slides down the bed."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I'm already hard but she uses her tongue to make me even harder; {mcsay}That feels nice, he's enjoying his reward!{/} {mark}[gn_store_owner_name]{/} moans as she sucks my cock." 
  choice("relationship_conversation_20") "Continue"
  return

label relationship_conversation_20:              ## eating pussy
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(191,192)
  $action_image= "squirrel relationship_conversation rc_37"
  "{mark}[gn_store_owner_name]{/} climbs up and sits on my face; {say}I'm ready for that wild tongue of yours!{/} She's really into it and I'm happy to enjoy her pussy."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "At first I tease her and she says; {say}C'mon, you can do better than that!{/} so I stop teasing and move my tongue faster. She moans; {say}Yes, that's more like it...{/}"
  choice("relationship_conversation_21") "Continue"
  return

label relationship_conversation_21:             ## missionary
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(195,196)
  $action_image= "squirrel relationship_conversation rc_38"
  "I throw {mark}[gn_store_owner_name]{/} over on her back and climb on top of her. She says; {say}Yes, I'm ready for you !{/} so I push my cock all the way into her soaking wet pussy."
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "{mark}[gn_store_owner_name]{/} cries; {say}Yes, fuck me hard!{/} and I pound her fast and deep for a long time. After a while I can't hold back: {mcsay}I'm cumming!{/} and we cum together." 
  choice("relationship_conversation_22") "Continue"
  return


## sleep

label relationship_conversation_22:
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"
  $temp_int=random.randint(205,207)
  $action_image= "squirrel relationship_conversation rc_39"
  "Afterwards we lie together and I say; {mcsay}You were fantastic, I'm glad you changed my mind.{/} She replies; {say}Well it did take all four of us ganging up on you!{/}"
  "{size=-22} "
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Afer a few minutes {mark}[gn_store_owner_name]{/} says; {say}I guess you've earned it so the four of us will let you sleep now.{/} After a brief kiss we both fall asleep easily."
  $mc.mood.give_xp(randint(30,50))                  ## large mood increase
  choice("sleep_after_date_copy") "Sleep"
  return

label sleep_after_date_copy:     ## at Ruthie's apartment, MC has Raymond's suit
  $game.location="store_owner_apartment"
  $game_bg="apartment bg_apartment"
  header "[gn_store_owner_name]'s Apartment"    
  
## THIS IS A DIFFERENCE FROM THE NORMAL SLEEP WHERE THE TIME ADVANCE IS AFTER FITNESS, HOUSEKEEPER, CAPSULES, AND ROLL FLAGS
  "Last night while you and {mark}[gn_store_owner_name]{/} figured things out:"
  "{size=-22} "
  call role_mission_manager_schedule
  "{size=-16} "
  $now.advance()             ## advance time so you get up in the morning
  "This morning:"
  "{size=-22} "
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_124"
  center "{image=[action_image]@345x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_211"  ## new clothes picture
  center "{image=[action_image]@345x600}"
  ##  TEXT
  $act.set_block("c")
  "In the morning we wake up together and I get out of bed first saying; {mcsay}I'm really glad last night worked out so well.{/} As she throws on her robe {mark}[gn_store_owner_name]{/} replies; {say}I'm glad we could talk you into having some fun!{/}"
  ""
  "{size=-16} "
  "At the door we share a passionate kiss before I leave for the shop. While I'm walking home I enjoy thinking about last night."
  "{size=-22} "
  call mc_update_relation(gn_store_owner_name,3,0)
  $mc.mood.give_xp(randint(6,12))                   ## small mood increase
  choice("sleep_after_date2") "Continue"            ## the FWB function can be used, all images and text come from functions it calls
  return