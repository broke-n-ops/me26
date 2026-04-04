## Dates with Simone - called from decision not to skip date scenes

##  Initialize new variables IF NEEDED
init python:
  sd_first_anal=-3       ## increment each date until it is 0 - when it hits 0 Simone will ask if he wants to try anal and set it to 1 and then the 'anal' button will appear
  sd_bathroom_start=0    ## it's set to 0 in 'sd_arriving' - when you reach 'vaginal 1' it's set to 1 which flags a text change the next time 'vaginal 1' is called
  sd_sex_count=0         ## limit is 3: increment in each function you have sex, when the value reaches 3 grey out the buttons
  sd_ruthie_anal_day=0   ## the day you have anal with Simone set to current day + 10 - in Ruthie date (fwb) test for current date>= value but only if >0

## arriving function - common - entry point with skip option - accept invitation button pays the AP cost

label sd_arriving:
  $game.location="teacher_apartment"
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Apartment"
## on a date, reset counter
  $global mc_nst_date_counter
  $mc_nst_date_counter=0
## increment anal flag until it's 0
  $global sd_first_anal
  if sd_first_anal<0:               ## increment until it reaches 0 then stop incrementing (starts at -3)
    $sd_first_anal+=1
## set flag for bathroom 'vaginal 1' text
  $global sd_bathroom_start
  $sd_bathroom_start=0
## reset counter for number of times you have sex this date, 3 is the limit
  $global sd_sex_count
  $sd_sex_count=0
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $temp_int=random.randint(1,2)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image= action_image+"a"
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(3,4)
  $action_image= "dates simone sd_"+str(temp_int)  
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image= action_image+"a"
  center "{image=[action_image]@400x600}"
## TEXT on right
  $act.set_block("c")
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    ""
    "{mark}[ns_teacher_name]'s{/} car with 3 of her {mark}combat bots{/} is nearby. She tells one of them to help our two karaoke bots get to each of our homes using the subway. The other two drive us to her home."
    ""
    ""
    "When we arrive at {mark}[ns_teacher_name]'s{/} home we're both aroused and anxious so we can't keep our hands off each other but after a few moments she says; {say}Have a seat, I'll get us some drinks.{/}"  
  else:                                            ## must be Sunday from Raymonds - minor changes
    ""
    "{mark}[ns_teacher_name]'s{/} car with 3 of her {mark}combat bots{/} is nearby. She tells one of them to make their way home and we get in the car with the other 2. It doesn't take us long to drive to her home."
    ""
    ""
    "When we arrive at {mark}[ns_teacher_name]'s{/} home we're both aroused and anxious so we can't keep our hands off each other but after a few moments she says; {say}Have a seat, I'll get us some drinks.{/}"  
  choice("sd_hot_tub_or_bedroom") "Continue"
  choice("goto_home", pos=17) "Skip Scene"
  return
 
label sd_hot_tub_or_bedroom:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Apartment"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $temp_int=random.randint(5,6)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(7,8)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
## TEXT on right
  $act.set_block("c")
  $action_image= "dates simone sd_"+str(temp_int)  
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    ""
    "I sit on her couch and it doesn't take long before {mark}[ns_teacher_name]{/} comes back with our drinks saying; {say}I hope you weren't waiting too long{/} as she walks over to join me."
    ""
    ""
    ""
    "{mark}[ns_teacher_name]{/} sits on my lap and puts her arms around me and says; {say}Karaoke was fun but I think we're both ready to go upstairs, would you like to play around in the hot tub or my bed?{/}"
  else:                                            ## must be Sunday from Raymonds - minor changes
    ""
    "I sit on her couch and it doesn't take long before {mark}[ns_teacher_name]{/} comes back with our drinks saying; {say}I hope you weren't waiting too long{/} as she walks over to join me."
    ""
    ""
    ""
    "{mark}[ns_teacher_name]{/} sits on my lap and puts her arms around me and says; {say}Raymond's was fun but I think we're both ready to go upstairs, should we enjoy ourselves in the hot tub or in my bed?{/}"
  choice("sd_bedroom") "Bedroom"
  choice("sd_hot_tub") "Hot Tub"
  return

##  bedroom functions
 
label sd_bedroom:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $temp_int=random.randint(9,10)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(11,12)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
## TEXT on right
  $act.set_block("c")
  $action_image= "dates simone sd_"+str(temp_int)  
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    ""
    "When we enter her bedroom {mark}[ns_teacher_name]{/} says; {say}Why don't you have a seat and relax, I'll be back in a few minutes. Don't worry, I won't keep you waiting long."
    ""
    ""
    ""
    "I sit down and {mark}[ns_teacher_name]{/} leaves for her bathroom. That could be fun, should I stay and wait for her or should I surprise her by following her into the bathroom?"
  else:                                            ## must be Sunday from Raymonds - no changes but kept separate for possible future revision
    ""
    "When we enter her bedroom {mark}[ns_teacher_name]{/} says; {say}Why don't you have a seat and relax, I'll be back in a few minutes. Don't worry, I won't keep you waiting long."
    ""
    ""
    ""
    "I sit down and {mark}[ns_teacher_name]{/} leaves for her bathroom. That could be fun, should I stay and wait for her or should I surprise her by following her into the bathroom?"
  choice("sd_bathroom") "Follow Her"
  choice("sd_bedroom_return") "Wait"
  return

label sd_bedroom_return:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  if now("Wednesday"):
    "While I was waiting I take off my jacket and soon {mark}[ns_teacher_name]{/} returns wearing pink lingerie and asks; {say}Do you like pink?{/}"
  else:
    "While I was waiting I take off my jacket and soon {mark}[ns_teacher_name]{/} returns in sexy red lingerie and asks; {say}Like what you see?{/}"
  "{size=-22} "
  $temp_int=random.randint(75,76)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image=action_image+"a"
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if now("Wednesday"):
    "She poses for me and I answer; {mcsay}I like the pink lingerie and I plan to enjoy taking it off you.{/} {mark}[ns_teacher_name]{/} says; {say}{/}"
  else: 
    "After watching her pose for me I answer; {mcsay}You look fantastic in red, too bad it won't stay on very long.{/} {mark}[ns_teacher_name]{/} says; {say}Nothing bad about that!{/}"
  choice("sd_in_bed") "Undress"
  return

label sd_in_bed:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "{mark}[ns_teacher_name]{/} joins me on the bed and we both enjoy helping each other out of our clothing. I tell her; {mcsay}You're even more beautiful without the lingerie.{/}"
  "{size=-22} "
  $temp_int=random.randint(77,78)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "As we embrace {mark}[ns_teacher_name]{/} says; {say}As nice as that suit looks on you I like you even better without it.{/}"
  choice("sd_bedroom_hj") "Hand Job"
  choice("sd_bedroom_finger") "Finger"
  choice("sd_bedroom_titjob") "Tit Job"
  choice("sd_bedroom_bj") "Blowjob"
  choice("sd_bedroom_lick") "Eat Pussy"
  choice("sd_bedroom_69") "69"
  if sd_first_anal==0:
    choice("sd_bedroom_anal", pos=17) "Skip Foreplay"          ## when anal flag reaches 0 go directly to anal (it starts at -3...)
  else:                                  
    if sd_first_anal>0:
      $temp_int=random.randint(1,5)                            ## if anal has been done at least once include it
    else:
      $temp_int=random.randint(1,4)                            ## if anal has not been done yet don't include it
    if temp_int==1:
      choice("sd_bedroom_missionary",pos=17) "Skip Foreplay"
    elif temp_int==2:
      choice("sd_bedroom_doggy",pos=17) "Skip Foreplay"
    elif temp_int==3:
      choice("sd_bedroom_cowgirl",pos=17) "Skip Foreplay"
    elif temp_int==4:
      choice("sd_bedroom_standing",pos=17) "Skip Foreplay"
    else:
      choice("sd_bedroom_anal",pos=17) "Skip Foreplay"
  return

label sd_bedroom_hj:                                         ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "We get comfortable on the bed and {mark}[ns_teacher_name]{/} reaches over to take hold of my cock saying; {say}Oooh, what a nice plaything you brought me!{/}"
  "{size=-22} "
  $temp_int=random.randint(79,80)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Her hand feels great as she moves it up and down slowly. {mcsay}You play very nicely with your toys, that feels really good.{/}"
  choice(None) "Hand Job"
  choice("sd_bedroom_finger") "Finger"
  choice("sd_bedroom_titjob") "Tit Job"
  choice("sd_bedroom_bj") "Blowjob"
  choice("sd_bedroom_lick") "Eat Pussy"
  choice("sd_bedroom_69") "69"
  if sd_first_anal==0:
    choice("sd_bedroom_anal", pos=17) "Enough Foreplay"          ## when anal flag reaches 0 go directly to anal (it starts at -3 and is incremented until it reaches 0)
  else:                                  
    if sd_first_anal>0:
      $temp_int=random.randint(1,5)                            ## if anal has been done at least once include it
    else:
      $temp_int=random.randint(1,4)                            ## if anal has not been done yet don't include it
    if temp_int==1:
      choice("sd_bedroom_missionary",pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("sd_bedroom_doggy",pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("sd_bedroom_cowgirl",pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("sd_bedroom_standing",pos=17) "Enough Foreplay"
    else:
      choice("sd_bedroom_anal",pos=17) "Enough Foreplay"
  return

label sd_bedroom_finger:                                    ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "I lean over {mark}[ns_teacher_name]{/} and take her nipple in my mouth and reach my hand down between her legs. She moans as I touch her."
  "{size=-22} "
  $temp_int=random.randint(81,82)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "{say}Ahhh, that feels nice.{/} she gasps. She's really wet, and my fingers slide in and out easily and her nipples get hard as well."
  choice("sd_bedroom_hj") "Hand Job"
  choice(None) "Finger"
  choice("sd_bedroom_titjob") "Tit Job"
  choice("sd_bedroom_bj") "Blowjob"
  choice("sd_bedroom_lick") "Eat Pussy"
  choice("sd_bedroom_69") "69"
  if sd_first_anal==0:
    choice("sd_bedroom_anal", pos=17) "Enough Foreplay"          ## when anal flag reaches 0 go directly to anal (it starts at -3 and is incremented until it reaches 0)
  else:                                  
    if sd_first_anal>0:
      $temp_int=random.randint(1,5)                            ## if anal has been done at least once include it
    else:
      $temp_int=random.randint(1,4)                            ## if anal has not been done yet don't include it
    if temp_int==1:
      choice("sd_bedroom_missionary",pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("sd_bedroom_doggy",pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("sd_bedroom_cowgirl",pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("sd_bedroom_standing",pos=17) "Enough Foreplay"
    else:
      choice("sd_bedroom_anal",pos=17) "Enough Foreplay"
  return

label sd_bedroom_titjob:                                  ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "{mark}[ns_teacher_name]{/} lies down holding her tits and says; {say}C'mon over here I've got something for you.{/} I get on top and place my cock between her tits."
  "{size=-22} "
  $temp_int=random.randint(83,84)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I move back and forth between her firm tits and she sticks out her tongue to lick the head of my cock each time I thrust forward. I'm in heaven!"
  choice("sd_bedroom_hj") "Hand Job"
  choice("sd_bedroom_finger") "Finger"
  choice(None) "Tit Job"
  choice("sd_bedroom_bj") "Blowjob"
  choice("sd_bedroom_lick") "Eat Pussy"
  choice("sd_bedroom_69") "69"
  if sd_first_anal==0:
    choice("sd_bedroom_anal", pos=17) "Enough Foreplay"          ## when anal flag reaches 0 go directly to anal (it starts at -3 and is incremented until it reaches 0)
  else:                                  
    if sd_first_anal>0:
      $temp_int=random.randint(1,5)                            ## if anal has been done at least once include it
    else:
      $temp_int=random.randint(1,4)                            ## if anal has not been done yet don't include it
    if temp_int==1:
      choice("sd_bedroom_missionary",pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("sd_bedroom_doggy",pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("sd_bedroom_cowgirl",pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("sd_bedroom_standing",pos=17) "Enough Foreplay"
    else:
      choice("sd_bedroom_anal",pos=17) "Enough Foreplay"
  return

label sd_bedroom_bj:                                           ## 2 poses, 4 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  $temp_int=random.randint(85,88)
  if temp_int<=86:                                             ## licking head
    "{mark}[ns_teacher_name]{/} lies in front of me taking my cock in her hand and using her tongue on the head. She looks up at me occasionally while working her tongue."
  else:                                                        ## sucking cock
    "I kneel on the bed and {mark}[ns_teacher_name]{/} smiles up at me before taking by hard cock into her hot, wet mouth. {mcsay}Yesss!{/} I gasp in pleasure."
  "{size=-22} "
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if temp_int<=86:                                             ## licking head
    "{mcsay}Your tongue feels amazing, you're such a tease{/} I tell her. She looks up with a smirk but doesn't say anything before her tongue goes back to work."
  else:                                                        ## sucking cock
    "{mark}[ns_teacher_name]{/} moves her mouth up and down gagging a little when she takes it too deep but she doesn't seem to mind. I moan; {mcsay}That's great, don't stop!"
  choice("sd_bedroom_hj") "Hand Job"
  choice("sd_bedroom_finger") "Finger"
  choice("sd_bedroom_titjob") "Tit Job"
  choice(None) "Blowjob"
  choice("sd_bedroom_lick") "Eat Pussy"
  choice("sd_bedroom_69") "69"
  if sd_first_anal==0:
    choice("sd_bedroom_anal", pos=17) "Enough Foreplay"          ## when anal flag reaches 0 go directly to anal (it starts at -3 and is incremented until it reaches 0)
  else:                                  
    if sd_first_anal>0:
      $temp_int=random.randint(1,5)                            ## if anal has been done at least once include it
    else:
      $temp_int=random.randint(1,4)                            ## if anal has not been done yet don't include it
    if temp_int==1:
      choice("sd_bedroom_missionary",pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("sd_bedroom_doggy",pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("sd_bedroom_cowgirl",pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("sd_bedroom_standing",pos=17) "Enough Foreplay"
    else:
      choice("sd_bedroom_anal",pos=17) "Enough Foreplay"
  return

label sd_bedroom_lick:                                    ## 2 poses, 4 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  $temp_int=random.randint(89,92)
  if temp_int<=90:                                        ## sitting on face
    "{mark}[ns_teacher_name]{/} says playfully; {say}Ever heard of a mustache ride?{/} I know what she means; {mcsay}I don't have a mustache but I'll give you a good ride anyway.{/}"
  else:                                                   ## on back classic
    "{mcsay}Lie down, I want a tasty treat{/} I demand and as she lies down {mark}[ns_teacher_name]{/} says; {say}Oooooh, I like that idea.{/} I slide down and begin licking her pussy."
  "{size=-22} "
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if temp_int<=90:                                        ## sitting on face
    "She sits on my face saying; {say}That's OK, they tickle too much!{/} I begin using my tongue to give her a good ride. {say}Ahhh, that's what I was after!{/} she gasps."
  else:                                                   ## on back classic
    "I'm enjoying myself as {mark}[ns_teacher_name]{/} says; {say}Ahhh, take it easy big boy. I want to enjoy this for a long time!{/} I look up saying; {mcsay}Spoil sport!{/} but slow down for her."
  choice("sd_bedroom_hj") "Hand Job"
  choice("sd_bedroom_finger") "Finger"
  choice("sd_bedroom_titjob") "Tit Job"
  choice("sd_bedroom_bj") "Blowjob"
  choice(None) "Eat Pussy"
  choice("sd_bedroom_69") "69"
  if sd_first_anal==0:
    choice("sd_bedroom_anal", pos=17) "Enough Foreplay"          ## when anal flag reaches 0 go directly to anal (it starts at -3 and is incremented until it reaches 0)
  else:                                  
    if sd_first_anal>0:
      $temp_int=random.randint(1,5)                            ## if anal has been done at least once include it
    else:
      $temp_int=random.randint(1,4)                            ## if anal has not been done yet don't include it
    if temp_int==1:
      choice("sd_bedroom_missionary",pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("sd_bedroom_doggy",pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("sd_bedroom_cowgirl",pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("sd_bedroom_standing",pos=17) "Enough Foreplay"
    else:
      choice("sd_bedroom_anal",pos=17) "Enough Foreplay"
  return

label sd_bedroom_69:                                           ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "{mark}[ns_teacher_name]{/} asks; {say}Would you like a little 69?{/} I like the idea; {mcsay}Sounds great, that's one of my favorite numbers.{/} She turns around on top of me."
  "{size=-22} "
  $temp_int=random.randint(93,94)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "Her warm mouth feels so good moving up and down on my cock and the taste of her pussy excites me. If we keep this up both of us will cum soon."
  choice("sd_bedroom_hj") "Hand Job"
  choice("sd_bedroom_finger") "Finger"
  choice("sd_bedroom_titjob") "Tit Job"
  choice("sd_bedroom_bj") "Blowjob"
  choice("sd_bedroom_lick") "Eat Pussy"
  choice(None) "69"
  if sd_first_anal==0:
    choice("sd_bedroom_anal", pos=17) "Enough Foreplay"          ## when anal flag reaches 0 go directly to anal (it starts at -3 and is incremented until it reaches 0)
  else:                                  
    if sd_first_anal>0:
      $temp_int=random.randint(1,5)                            ## if anal has been done at least once include it
    else:
      $temp_int=random.randint(1,4)                            ## if anal has not been done yet don't include it
    if temp_int==1:
      choice("sd_bedroom_missionary",pos=17) "Enough Foreplay"
    elif temp_int==2:
      choice("sd_bedroom_doggy",pos=17) "Enough Foreplay"
    elif temp_int==3:
      choice("sd_bedroom_cowgirl",pos=17) "Enough Foreplay"
    elif temp_int==4:
      choice("sd_bedroom_standing",pos=17) "Enough Foreplay"
    else:
      choice("sd_bedroom_anal",pos=17) "Enough Foreplay"
  return

label sd_bedroom_missionary:                              ## 1 pose, 3 pics - from skip and lick pussy
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "We're both ready and {mark}[ns_teacher_name]{/} lies down saying; {say}Put it in and give me everything you've got!{/} Her pussy is tight but also very wet and I enter easily."
  "{size=-22} "
  $temp_int=random.randint(95,97)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "After a number of slow, deep thrusts she cries out {say}Faster! I'm almost there!{/} I speed up and soon I cum inside her which makes her cum at the same time."
  $global sd_sex_count

  $global sd_first_anal
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice(None) "Missionary"
    choice("sd_bedroom_doggy") "Doggy"
    choice("sd_bedroom_cowgirl") "Cowgirl"
    choice("sd_bedroom_standing") "Standing"
    if sd_first_anal==1:
      choice("sd_bedroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_bedroom_afterwards",pos=17) "Exhausted"
  return

label sd_bedroom_doggy:                              ## 1 pose, 2 pics - from blowjob and fingering
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "I ask {mark}[ns_teacher_name]{/}; {mcsay}I'd like to take you from behind if that's OK?{/} Getting on her hands and knees she replies; {say}This bitch is in heat, I love doggy!{/}"
  "{size=-22} "
  $temp_int=random.randint(98,99)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I get behind her and enter forcefully; {mcsay}Yes! Take it!{/} I can't help myself fucking her hard, fast, and deep. She cries out; {say}Ahhh, I'm cumming!{/} as I cum inside her."
  $global sd_sex_count
  $global sd_first_anal
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_bedroom_missionary") "Missionary"
    choice(None) "Doggy"
    choice("sd_bedroom_cowgirl") "Cowgirl"
    choice("sd_bedroom_standing") "Standing"
    if sd_first_anal==1:
      choice("sd_bedroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_bedroom_afterwards",pos=17) "Exhausted"
  return

label sd_bedroom_cowgirl:                              ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "{mark}[ns_teacher_name]{/} says; {say}This girl is full of energy and wants to use it!{/} I lean back on my knees saying; {mcsay}Climb aboard, we can do this together.{/}"
  "{size=-22} "
  $temp_int=random.randint(100,101)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She lowers herself onto my cock; {say}Yessss, that feels so good!{/} After a long ride she cries; {say}Cum for me...{/} She falls back on her hands as we both cum."
  $global sd_sex_count
  $global sd_first_anal
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_bedroom_missionary") "Missionary"
    choice("sd_bedroom_doggy") "Doggy"
    choice(None) "Cowgirl"
    choice("sd_bedroom_standing") "Standing"
    if sd_first_anal==1:
      choice("sd_bedroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_bedroom_afterwards",pos=17) "Exhausted"
  return

label sd_bedroom_standing:                              ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "I surprise {mark}[ns_teacher_name]{/} by standing up and pulling her with me; {mcsay}Let's try something different, put your arm around my neck.{/} As she does I grab her leg."
  "{size=-22} "
  $temp_int=random.randint(102,103)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She's surprised but grabs my cock and puts it in position; {say}Do it big boy!{/} and we fuck standing up. Soon she cries; {say}Now, cum now!{/} and I cum inside her."
  $global sd_sex_count
  $global sd_first_anal
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_bedroom_missionary") "Missionary"
    choice("sd_bedroom_doggy") "Doggy"
    choice("sd_bedroom_cowgirl") "Cowgirl"
    choice(None) "Standing"
    if sd_first_anal==1:
      choice("sd_bedroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_bedroom_afterwards",pos=17) "Exhausted"
  return

label sd_bedroom_anal:                              ## 1 pose, 3 pics
  $global sd_first_anal
  $global sd_ruthie_anal_day
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  $temp_int=random.randint(104,106)
  if sd_first_anal==0:                           ## haven't done anal yet, Simone asks
    $sd_first_anal=1                             ## set flag to not repeat first time AND activate 'anal' button

    $sd_ruthie_anal_day=now.day+10               ## set first day that anal with Ruthie could happen - depends upon dating Ruthie!!
##    $sd_ruthie_anal_day=now.day+2                ## FOR TESTING - use 2 to make sure a delay happens

    "{mark}[ns_teacher_name]{/} looks hesitant but says; {say}Have you ever done anal with a real person?{/} I reply; {mcsay}No, only with bots but if you're offering I'd like to try it.{/}"
  else:
    if temp_int<=105:                             ## not first anal, MC asks 67% of the time
      "I'm a little hesitant but ask; {mcsay}I'd like to do anal again, are you up for it?{/} {mark}[ns_teacher_name]{/} smiles; {say}Of course don't be so nervous I like anal too.{/}"
    else:                                         ## not first anal, Simone asks 33% of the time
      "{mark}[ns_teacher_name]{/} says; {say}I'm in a wild mood, would you like to fuck me in the ass?{/} I'm pleasantly surprised; {mcsay}You've got a great ass, of course I'd like that!{/}"
  "{size=-22} "
  $temp_int=random.randint(104,106)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "{mark}[ns_teacher_name]{/} gets on top and lowers herself onto by cock. Her ass is really tight and after a short time I cum deep in her ass and surprisingly she cums too."
  $global sd_sex_count
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_bedroom_missionary") "Missionary"
    choice("sd_bedroom_doggy") "Doggy"
    choice("sd_bedroom_cowgirl") "Cowgirl"
    choice("sd_bedroom_standing") "Standing"
    choice(None) "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_bedroom_afterwards",pos=17) "Exhausted"
  return

label sd_bedroom_afterwards:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bedroom"
  "Afterwards we lay together exhausted on the bed and I tell {mark}[ns_teacher_name]{/}; {mcsay}That was wonderful, thank you so much for inviting me over.{/}"
  "{size=-22} "
  $temp_int=random.randint(107,108)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if now("Wednesday"):                            ## Karaoke
    "She replies; {say}You're welcome and you were fantastic! Sadly I have a class to teach tonight so you have to leave.{/} I'm not surprised; {mcsay}OK, I'll get dressed.{/}"
  else:                                           ## Raymond's
    "She replies; {say}You were great and I'm glad you came! Sadly I have an early meeting tomorrow so you can't stay.{/} I'm disappointed; {mcsay}OK, I'll get dressed.{/}"
  choice("sd_leaving") "Time to Leave"
  return

## bathroom functions

label sd_bathroom:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bathroom"
  "I quickly get undressed and follow {mark}[ns_teacher_name]{/} into her bathroom. Trying not to scare her I say quietly; {mcsay}You're so beautiful and sexy that I just couldn't wait.{/} "
  "{size=-22} "
  $temp_int=random.randint(57,58)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She's a little surprised as she turns her head and says; {say}Anxious are we?{/} Instead of answering I embrace her and we share a passionate kiss."
  choice("sd_bathroom_hj") "Hand Job"
  choice("sd_bathroom_finger") "Finger"
  choice("sd_bathroom_bj") "Blowjob"
  choice("sd_bathroom_lick") "Eat Pussy"
  choice("sd_bathroom_vaginal_1",pos=17) "Skip Foreplay"
  return
 
label sd_bathroom_hj:                              ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bathroom"
  "{mark}[ns_teacher_name]{/} reaches down and takes hold of my cock saying; {say}You're already hard as a rock! I guess you really were having trouble waiting for me.{/}"
  "{size=-22} "
  $temp_int=random.randint(61,62)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I put my hand on one of her breasts and give it a gentle squeeze; {mcsay}It's your fault, if you didn't turn me on so much maybe I could have waited for you.{/}"
  choice(None) "Hand Job"
  choice("sd_bathroom_finger") "Finger"
  choice("sd_bathroom_bj") "Blowjob"
  choice("sd_bathroom_lick") "Eat Pussy"
  choice("sd_bathroom_vaginal_1", pos=17) "Enough Foreplay"
  return
 
label sd_bathroom_finger:                          ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bathroom"
  "I reach down and touch {mark}[ns_teacher_name]'s{/} pussy which makes her lean back on the sink; {say}Ummhhh, your fingers feel good.{/} I lean down and suck on her nipple."
  "{size=-22} "
  $temp_int=random.randint(59,60)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She squeezes her other breast; {say}Ahhh, that feels great big boy.{/} She moans in pleasure as I push a finger deeper inside her saying; {mcsay}This is only the beginning{/}."
  choice("sd_bathroom_hj") "Hand Job"
  choice(None) "Finger"
  choice("sd_bathroom_bj") "Blowjob"
  choice("sd_bathroom_lick") "Eat Pussy"
  choice("sd_bathroom_vaginal_1", pos=17) "Enough Foreplay"
  return
  
label sd_bathroom_bj:                              ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bathroom"
  "{mark}[ns_teacher_name]{/} kneels down in front of me and looks up at me as she licks the head of my cock. It feels great and makes me beg; {mcsay}Oh yes, put it in your mouth.{/}"
  "{size=-22} "
  $temp_int=random.randint(65,66)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She smiles up at me and then takes my cock into her mouth while still using her tongue. My cock gets even harder; {mcsay}Your mouth feels so good, don't stop.{/}"
  choice("sd_bathroom_hj") "Hand Job"
  choice("sd_bathroom_finger") "Finger"
  choice(None) "Blowjob"
  choice("sd_bathroom_lick") "Eat Pussy"
  choice("sd_bathroom_vaginal_1", pos=17) "Enough Foreplay"
  return 

label sd_bathroom_lick:                            ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bathroom"
  "I tell {mark}[ns_teacher_name]{/} to sit on the edge of the sink and then I kneel down so my face is next to her pussy. She looks at me; {say}I want to feel that tongue of yours.{/}"
  "{size=-22} "
  $temp_int=random.randint(63,64)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I tease her with my tongue making her beg; {say}C'mon, you can do better!{/} I start using both fingers and tongue making her cry out; {say}Yes, that's more like it!{/}"
  choice("sd_bathroom_hj") "Hand Job"
  choice("sd_bathroom_finger") "Finger"
  choice("sd_bathroom_bj") "Blowjob"
  choice(None) "Eat Pussy"
  choice("sd_bathroom_vaginal_1", pos=17) "Enough Foreplay"
  return

label sd_bathroom_vaginal_1:                       ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bathroom"
  $global sd_bathroom_start
  if sd_bathroom_start==0:                         ## first time 'vaginal 1' is viewed on the current date
    $sd_bathroom_start=1
    "{mark}[ns_teacher_name]{/} sits on the sink and says; {say}Let's put that hard cock to good use!{/} As I press my cock against her pussy I say; {mcsay}I'm glad you're ready because I am too!{/}"
  else:                                            ## 'vaginal 1' has already been seen on this date, different text
    "{mark}[ns_teacher_name]{/} says; {say}Wow, that was great! One more?{/} I'm pretty tired but I'm still hard so I press my cock against her pussy; {mcsay}I'm ready for one more round!{/}"
  "{size=-22} "
  $temp_int=random.randint(67,68)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I push my cock inside her and as I pound her pussy she starts fingering her clit. It feels great! Finally {mark}[ns_teacher_name]{/} cries out; {say}Yes,yes...{/} and we come together."
  $global sd_sex_count
  $global sd_first_anal
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice(None) "Vaginal 1"
    choice("sd_bathroom_vaginal_2") "Vaginal 2"
    if sd_first_anal==1:
      choice("sd_bathroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_bathroom_afterwards",pos=17) "Exhausted"
  return
 
label sd_bathroom_vaginal_2:                       ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bathroom"
  "{mark}[ns_teacher_name]{/} says; {say}That was great, can we do it again?{/} Although I'm getting a little tired I'm still hard and I'm sure I can go again; {mcsay}I'd love to do it again!{/}"
  "{size=-22} "
  $temp_int=random.randint(69,70)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She leans forward for a passionate kiss as I push my cock into her pussy. She grabs her breast as I pound her pussy and before long we both cum again."
  $global sd_sex_count
  $global sd_first_anal
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_bathroom_vaginal_1") "Vaginal 1"
    choice(None) "Vaginal 2"
    if sd_first_anal==1:
      choice("sd_bathroom_anal") "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_bathroom_afterwards",pos=17) "Exhausted"
  return

label sd_bathroom_anal:                            ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bathroom"
  "{mark}[ns_teacher_name]{/} says; {say}I'd love to go again, are you up for it?{/} I decide to risk asking; {mcsay}Can we do anal this time?{/}"
  "{size=-22} "
  $temp_int=random.randint(71,72)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "{mark}[ns_teacher_name]{/} smiles and says; {say}Of course, you know I love anal too!{/} I start gently but she says; {say}Harder!{/} I thrust hard until I cum in her ass and she cums too."
  $global sd_sex_count
  $global sd_first_anal
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_bathroom_vaginal_1") "Vaginal 1"
    choice("sd_bathroom_vaginal_2") "Vaginal 2"
    choice(None) "Anal"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_bathroom_afterwards",pos=17) "Exhausted"
  return

label sd_bathroom_afterwards:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Bathroom"
  if now("Wednesday"):                            ## Karaoke
    "Afterwards {mark}[ns_teacher_name]{/} stands up and gives me a passionate kiss then says; {say}You were amazing, I'm really glad you came over after the {mark}karaoke competition{/}.{/}"
  else:                                           ## Raymond's
    "Afterwards {mark}[ns_teacher_name]{/} stands up and gives me a passionate kiss then says; {say}You were amazing, I'm really glad you were at {mark}Raymond's{/} and came over tonight.{/}"
  "{size=-22} "
  $temp_int=random.randint(73,74)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if now("Wednesday"):                            ## Karaoke
    "Then she says; {say}Sadly I have a class to teach tonight so you have to leave.{/} Of course I'm not surprised; {mcsay}I know, I'll get dressed.{/}"
  else:                                           ## Raymond's
    "Then she says; {say}Sadly I have an early meeting tomorrow morning so you can't stay.{/} I'm disappointed but I say; {mcsay}I understand, I'll get dressed.{/}"
  choice("sd_leaving") "Time to Leave"
  return

## hot tub functions

label sd_hot_tub:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $temp_int=random.randint(17,18)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(109,110)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
## TEXT on right
  $act.set_block("c")
  $action_image= "dates simone sd_"+str(temp_int)  
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    ""
    "{mark}[ns_teacher_name]{/} leads the way upstairs and I enjoy watching her walk up the steps in her tight pants. At the top she turns around and says playfully; {say}I hope you enjoyed the view pervert!"
    ""
    ""
    "When we enter the room I put both hands on her ass and say; {mcsay}I was hoping you'd invite me over after karaoke and watching you walk up the steps just now made it difficult to control myself.{/}"
  else:                                            ## must be Sunday from Raymonds - minor changes
    ""
    "{mark}[ns_teacher_name]{/} leads the way upstairs and it's exciting watching her walk up the steps in that short dress. At the top she turns around and says playfully; {say}Enjoying the view you perve?"
    ""
    ""
    "When we enter the room I put both hands on her ass and say; {mcsay}While we were at Raymond's I was hoping you'd invite me over and after watching you walk up the steps I simply can't control myself.{/}"
  choice("sd_hot_tub_undressed") "Undress"
  return

label sd_hot_tub_undressed:                               ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  "We impatiently help each other get undressed and when we're finished we embrace for a hot, passionate kiss. I think {mark}[ns_teacher_name]{/} is as excited as I am!"
  "{size=-22} "
  $temp_int=random.randint(19,20)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "{mark}[ns_teacher_name]{/} reaches down to take hold of my cock; {say}Nice and hard, that's just the way I like it. Let's get in the hot tub. {/} I'm ready and reply; {mcsay}After you!{/}"
  choice("sd_hot_tub_hj") "Hand Job"
  choice("sd_hot_tub_finger") "Finger"
  choice("sd_hot_tub_bj") "Blowjob"
  choice("sd_hot_tub_lick") "Eat Pussy"
  $temp_int=random.randint(1,5)
  if temp_int==1:
    choice("sd_hot_tub_missionary",pos=17) "Skip Foreplay"
  elif temp_int==2:
    choice("sd_hot_tub_doggy",pos=17) "Skip Foreplay"
  elif temp_int==3:
    choice("sd_hot_tub_cowgirl",pos=17) "Skip Foreplay"
  elif temp_int==4:
    choice("sd_hot_tub_side",pos=17) "Skip Foreplay"
  else:
    choice("sd_hot_tub_standing",pos=17) "Skip Foreplay"
  return

label sd_hot_tub_hj:                               ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  "{mark}[ns_teacher_name]{/} says; {say}Take a seat mister, I see a nice big, hard toy that I want to play with.{/} Sitting down and on the edge of the hot tub I reply; {mcsay}Yes ma'am!{/}"
  "{size=-22} "
  $temp_int=random.randint(21,22)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "She takes hold of my cock and strokes me up and down slowly and I ask her; {mcsay}Do you like your toy?{/} {mark}[ns_teacher_name]{/} replies; {say}Quiet mister, I'm busy.{/}"
  choice(None) "Hand Job"
  choice("sd_hot_tub_finger") "Finger"
  choice("sd_hot_tub_bj") "Blowjob"
  choice("sd_hot_tub_lick") "Eat Pussy"
  $temp_int=random.randint(1,5)
  if temp_int==1:
    choice("sd_hot_tub_missionary",pos=17) "Enough Foreplay"
  elif temp_int==2:
    choice("sd_hot_tub_doggy",pos=17) "Enough Foreplay"
  elif temp_int==3:
    choice("sd_hot_tub_cowgirl",pos=17) "Enough Foreplay"
  elif temp_int==4:
    choice("sd_hot_tub_side",pos=17) "Enough Foreplay"
  else:
    choice("sd_hot_tub_standing",pos=17) "Enough Foreplay"
  return

label sd_hot_tub_finger:                           ## 3 poses, 6 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  $temp_int=random.randint(23,28)
  if temp_int==25 or temp_int==26:                 ## Simone standing
    "In the hot tub I tell {mark}[ns_teacher_name]{/} to stand up and face the wall. She's surprised but decides to go along and says with a playful smile; {say}Yes sir!{/}"
  else:                                            ## Simone on edge of hot tub
    "I ask {mark}[ns_teacher_name] playfully{/}; {mcsay}Can you sit on the edge of the hot tub for me? I'd like to see what I'm playing with.{/} She sits down with a smile; {say}Sounds nice!{/}"
  "{size=-22} "
  
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if temp_int==25 or temp_int==26:                 ## Simone standing
    "Kneeling behind her gives me a great view and I reach up and put a finger in her wet pussy. She continues our little game; {say} Sir, what are you doing to me?"
  else:                                            ## Simone on edge of hot tub
    "I put my finger in her pussy and she's very wet; {say}I think you're just as excited as I am.{/} With a quiet moan she says; {say}You have more than one finger don't you?{/}"
  choice("sd_hot_tub_hj") "Hand Job"
  choice(None) "Finger"
  choice("sd_hot_tub_bj") "Blowjob"
  choice("sd_hot_tub_lick") "Eat Pussy"
  $temp_int=random.randint(1,5)
  if temp_int==1:
    choice("sd_hot_tub_missionary",pos=17) "Enough Foreplay"
  elif temp_int==2:
    choice("sd_hot_tub_doggy",pos=17) "Enough Foreplay"
  elif temp_int==3:
    choice("sd_hot_tub_cowgirl",pos=17) "Enough Foreplay"
  elif temp_int==4:
    choice("sd_hot_tub_side",pos=17) "Enough Foreplay"
  else:
    choice("sd_hot_tub_standing",pos=17) "Enough Foreplay"
  return

label sd_hot_tub_bj:                               ## 3 poses, 6 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  $temp_int=random.randint(29,34)
  if temp_int==29 or temp_int==30:                 ## MC standing inside tub
    "{mark}[ns_teacher_name]{/} says; {say}I need you to stand up for me, I can't breath underwater!{/} It's easy to figure out what she plans to do so I waste no time standing up."
  else:                                            ## MC sitting on edge of tub
    "{mark}[ns_teacher_name]{/} says playfully; {say}I'm thirsty Sir, please take a seat on the edge of the tub.{/} I reply playfully; {say}Certainly, I think I have just what you need!{/}"
  "{size=-22} "
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if temp_int==29 or temp_int==30:                 ## MC standing inside tub
    "It feels great when she wraps her lips around my cock and I push her head down further. {mark}[ns_teacher_name]{/} doesn't resist but I stop pushing when she gags a little."
  else:                                            ## MC sitting on edge of tub
    "{mark}[ns_teacher_name]{/} starts sucking my cock enthusiastically then stops to say; {say}I think I'm hungry too!{/} She smiles up at me before putting my cock back in her mouth."
  choice("sd_hot_tub_hj") "Hand Job"
  choice("sd_hot_tub_finger") "Finger"
  choice(None) "Blowjob"
  choice("sd_hot_tub_lick") "Eat Pussy"
  $temp_int=random.randint(1,5)
  if temp_int==1:
    choice("sd_hot_tub_missionary",pos=17) "Enough Foreplay"
  elif temp_int==2:
    choice("sd_hot_tub_doggy",pos=17) "Enough Foreplay"
  elif temp_int==3:
    choice("sd_hot_tub_cowgirl",pos=17) "Enough Foreplay"
  elif temp_int==4:
    choice("sd_hot_tub_side",pos=17) "Enough Foreplay"
  else:
    choice("sd_hot_tub_standing",pos=17) "Enough Foreplay"
  return

label sd_hot_tub_lick:                             ## 2 poses, 4 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  $temp_int=random.randint(35,38)
  if temp_int==35 or temp_int==36:                 ## Simone laying on edge of tub
    "{mark}[ns_teacher_name]{/} says; {say}I'd love to feel that wild tongue of yours, are you up for that?{/} and I reply; {mcsay}I'm always up for that{/} and she lies down on the edge of the tub."
  else:                                            ## Simone standing
    "{mark}[ns_teacher_name]{/} stands up in the tub and says; {say}I want you to put that tongue of yours to work!{/} I kneel in front of her and grab her ass to pull her towards me."
  "{size=-22} "
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if temp_int==35 or temp_int==36:                 ## Simone laying on edge of tub
    "I lean over and use my hands to spread her legs so I can taste her delicious pussy. {mark}[ns_teacher_name]{/} gasps; {say}That's it, don't stop...{/} as I use my tongue on her clit."
  else:                                            ## Simone standing
    "She looks down at me as I use my tongue on her pussy. She grabs my head saying; {say}That's nice, a little faster, yes...{/} and I flick my tongue rapidly on her clit."
  choice("sd_hot_tub_hj") "Hand Job"
  choice("sd_hot_tub_finger") "Finger"
  choice("sd_hot_tub_bj") "Blowjob"
  choice(None) "Eat Pussy"
  $temp_int=random.randint(1,5)
  if temp_int==1:
    choice("sd_hot_tub_missionary",pos=17) "Enough Foreplay"
  elif temp_int==2:
    choice("sd_hot_tub_doggy",pos=17) "Enough Foreplay"
  elif temp_int==3:
    choice("sd_hot_tub_cowgirl",pos=17) "Enough Foreplay"
  elif temp_int==4:
    choice("sd_hot_tub_side",pos=17) "Enough Foreplay"
  else:
    choice("sd_hot_tub_standing",pos=17) "Enough Foreplay"
  return

label sd_hot_tub_missionary:                       ## 2 poses, 4 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  "{mark}[ns_teacher_name]{/} lies down at the end of the tub saying; {say}I'm ready for you, come fill me up!{/} I'm ready too and put my cock at the entrance of her pussy."
  "{size=-22} "
  $temp_int=random.randint(39,42)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I push in hard and {mark}[ns_teacher_name]{/} loves it; {say}Ooohh, harder, yes...{/} and I double my efforts. Before long I cum inside her and she cries out as she cums too."
  $global sd_sex_count
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice(None) "Missionary"
    choice("sd_hot_tub_doggy") "Doggy"
    choice("sd_hot_tub_side") "Side"
    choice("sd_hot_tub_cowgirl") "Cowgirl"
    choice("sd_hot_tub_standing") "Standing"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_hot_tub_afterwards",pos=17) "Exhausted"
  return

label sd_hot_tub_doggy:                            ## 2 poses, 4 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  "I tell {mark}[ns_teacher_name]{/}; {mcsay}I want you from behind, lean over the end of the tub{/} She says playfully; {say}Oh my, you're such a tough guy!{/} as she gets into position."
  "{size=-22} "
  $temp_int=random.randint(43,46)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I look down at her ass while I push my cock into her pussy. She moans; {say}Yes! Do it hard!{/} I ram my cock deep into her pussy over and over until we both cum."
  $global sd_sex_count
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_hot_tub_missionary") "Missionary"
    choice(None) "Doggy"
    choice("sd_hot_tub_side") "Side"
    choice("sd_hot_tub_cowgirl") "Cowgirl"
    choice("sd_hot_tub_standing") "Standing"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_hot_tub_afterwards",pos=17) "Exhausted"
  return

label sd_hot_tub_side:                             ## 2 pose, 4 pics (1 is sort of doggy)
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  $temp_int=random.randint(47,50)
  if temp_int==47 or temp_int==48:                 ## this one is more like doggy
    "{mark}[ns_teacher_name]{/} says; {say}Let's do doggy a little differently and she puts her leg up on the side of the tub.{/} I tell her; {mcsay}Every way is great with you!{/} as I position my cock."
  else:
    "{mark}[ns_teacher_name]{/} moves over to the side of the tub and says; {say}Come here, let's do it a little differently this time.{/} She lies sideways on the edge of the tub."
  "{size=-22} "
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if temp_int==47 or temp_int==48:                 ## this one is more like doggy
    "I push deep into her and she turns to look at me; {say}Yes, I like it this way, harder!{/} I thrust harder and faster, it's hot watching each other as we both cum."
  else:
    "I push my cock into her and she says; {say}Do you like the view?{/} I do; {mcsay}It's great, I love looking at you!{/} We enjoy each other and when I finally cum she does too."
  $global sd_sex_count
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_hot_tub_missionary") "Missionary"
    choice("sd_hot_tub_doggy") "Doggy"
    choice(None) "Side"
    choice("sd_hot_tub_cowgirl") "Cowgirl"
    choice("sd_hot_tub_standing") "Standing"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_hot_tub_afterwards",pos=17) "Exhausted"
  return

label sd_hot_tub_cowgirl:                          ## 2 poses, 4 pics (1 is sort of missionary)
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  $temp_int=random.randint(51,54)
  if temp_int==51 or temp_int==52:                 ## this one is more like missionary
    "{mark}[ns_teacher_name]{/} sits on the side of the tub and says; {say}Kneel in front of me, let's do this together.{/} I kneel and she moves forward and we start out missionary but..."
  else:
    "I sit down in the tub and ask playfully; {say}Need a ride?{/} {mark}[ns_teacher_name]{/} smiles and says; {say}Only if you're going my way!{/} I say; {mcsay}Of course I'm going your way, hop on!{/}"
  "{size=-22} "
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if temp_int==51 or temp_int==52:                 ## this one is more like doggy
    "...she sits on my legs switching to cowgirl and then we trade off between the two positions for a long time before I finish inside her making her cum too."
  else:
    "She's full of energy riding me hard and says; {say}How far are you going?{/} Just before I cum I tell her; {mcsay}I'm going all the way!{/} and then both of us cum together."
  $global sd_sex_count
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_hot_tub_missionary") "Missionary"
    choice("sd_hot_tub_doggy") "Doggy"
    choice("sd_hot_tub_side") "Side"
    choice(None) "Cowgirl"
    choice("sd_hot_tub_standing") "Standing"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_hot_tub_afterwards",pos=17) "Exhausted"
  return

label sd_hot_tub_standing:                         ## 1 pose, 2 pics
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  "I say to {mark}[ns_teacher_name]{/}; {mcsay}The water is feeling kind of hot to me, how about standing?{/} She replies; {say}I think it's fine but let's do it!{/} as she stands up and turns around."
  "{size=-22} "
  $temp_int=random.randint(55,56)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  "I take her from behind. I pound her pussy for a long time before cumming inside her. Our legs are tired after that and we collapse in the hot tub together."
  $global sd_sex_count
  $sd_sex_count+=1
  if sd_sex_count<3:
    choice("sd_hot_tub_missionary") "Missionary"
    choice("sd_hot_tub_doggy") "Doggy"
    choice("sd_hot_tub_side") "Side"
    choice("sd_hot_tub_cowgirl") "Cowgirl"
    choice(None) "Standing"
  else:
    "{size=-10}(You've done it 3 times, no one can keep it up forever! {mark}[mc.name]{/} needs a break!){/}"
  choice("sd_hot_tub_afterwards",pos=17) "Exhausted"
  return

label sd_hot_tub_afterwards:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Hot Tub"
  "We're both tired but it feels good to relax together in the hot tub. I tell {mark}[ns_teacher_name]{/}; {mcsay}You are so beautiful and sexy, I feel so good when I'm with you.{/}"
  "{size=-22} "
  $temp_int=random.randint(111,112)
  $action_image= "dates simone sd_"+str(temp_int)
  center "{image=[action_image]@800x600}"
  "{size=-22} "
  if now("sunday"):                                ## date after Raymond's
    "She replies; {say}Ummhh, you make me feel good too.{/} She pauses briefly; {say}I'm sorry but my Monday mornings are brutal and I have to send you home.{/}"
  else:                                            ## date after karaoke
    "She replies; {say}Thanks for the compliment and I love our time together too. Unfortunately you have to go, I need to get to the school to teach class tonight.{/}"
  choice("sd_leaving") "Time to Leave"
  return

## leaving function - common

label sd_leaving:
  $temp_int=random.randint(1,3)
  $game_bg="teacher_apartment bg_"+str(temp_int)
  header "{mark}[ns_teacher_name]'s{/} Apartment"
## GRAPHICS on left
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  $temp_int=random.randint(13,14)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
  ""
  $temp_int=random.randint(15,16)
  $action_image= "dates simone sd_"+str(temp_int)
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    $action_image=action_image+"a"
  center "{image=[action_image]@400x600}"
## TEXT on right
  $act.set_block("c")
  $action_image= "dates simone sd_"+str(temp_int)  
  if now("Wednesday"):                             ## Wednesdays are from karaoke
    ""
    "I get dressed and {mark}[ns_teacher_name]{/} throws on a robe. We walk downstairs to her door and I say; {mcsay}That was wonderful, thanks for inviting me over.{/} and she replies; {say}Of course, my pleasure!{/}"
    ""
    ""
    "{mark}[ns_teacher_name]{/} has 2 of her combat bots drive me home. On the way home I think how great it was that she told me about karaoke, I am so lucky that an amazing woman like {mark}[ns_teacher_name]{/} likes me."
  else:                                            ## must be Sunday from Raymonds - minor changes
    ""
    "I get dressed and {mark}[ns_teacher_name]{/} throws on a robe. We walk downstairs to her door and I say; {mcsay}You were amazing, thank you so much for inviting me.{/} and she replies; {say}You're pretty hot yourself!{/}"
    ""
    ""
    "{mark}[ns_teacher_name]{/} has 2 of her combat bots drive me home. On the way home I think how great it is that I met her at Raymond's, {mark}[ns_teacher_name]{/} is amazing and I'm very lucky that she likes me."
  call mc_update_relation(ns_teacher_name,3,0)     ## gain 2 relationship point
  $mc.mood.give_xp(randint(30,50))               ## large mood increase
  choice("goto_home") "Go Home"
  return