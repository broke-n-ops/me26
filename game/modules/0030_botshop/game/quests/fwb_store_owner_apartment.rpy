## stop forcing MC to pay for Ruthie's apartment but if you don't it's game over
## 'bp_force_store_owner_rent' variable declared in 'business_parthers' on line 34
## 'bp_force_store_owner_rent' is set to 1 in 'business_parthers' on line 1283
## OLD LOCATION - effect of 'bp_force_store_owner_rent' in 'friends_with_benefits.rpy' line 1877, comment these lines out
## NEW LOCATION - 'friends_with_benefits.rpy' event handler function line 139
## add a 1 day delay between you clicking on "No" and the escalation event

##===== entry point function =====

label fwb_escalate_apartment_rent():
  $global bp_force_store_owner_rent
  $game_bg="home bg"
  $game_bgm="home bgm"

  if bp_force_store_owner_rent==1:          ## first call triggers visit from Earl
    $bp_force_store_owner_rent=2            ## increment escalation level
    header "{mark}[gn_diner_owner_name]{/} Visits Your Shop"
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $action_image= "quests friends_with_benefits fwb_216"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_217"
    center "{image=[action_image]@400x600}"
    ##  TEXT
    $act.set_block("c")
    "You hear the door open and see {mark}[gn_diner_owner_name]{/} entering the shop. He's never come into the shop before, I wonder if something is wrong?"
    ""
    "He walks over; {say}Hi {mark}[mc.name]{/}, there is something I'd like to tell you about because I believe it is important to you.{/} This doesn't sound good; {mcsay}What's wrong {mark}[gn_diner_owner_name]{/}?"
    ""
    "{mark}[gn_diner_owner_name]{/} says; {say}They are considering raising {mark}[gn_store_owner_name]'s{/} rent next month and she told me she won't be able to afford it. She's very worried.{/}"
    extend " I'm not sure how to react; {mcsay}That's bad news {mark}[gn_diner_owner_name]{/}, I hope she will be OK.{/}"
    choice("escalation1_screen2") "Continue"

  elif bp_force_store_owner_rent==2:        ## second call triggers call from Simone
    $bp_force_store_owner_rent=3            ## increment escalation level
    header "You Receive a Call from {mark}[ns_teacher_name]{/}"
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $action_image= "quests friends_with_benefits fwb_218"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_219"
    center "{image=[action_image]@400x600}"
    ##  TEXT
    $act.set_block("c")
    ""
    "You receive a call from {mark}[ns_teacher_name]{/} and she sounds upset; {say}Hi {mark}[mc.name]{/}, I'm sure you know about {mark}[gn_store_owner_name]'s{/} rent situation. what are you going to do about it?{/}"
    ""
    ""
    ""
    "At first I'm not sure how to reply but eventually I say; {mcsay}Hi {mark}[ns_teacher_name]{/}, yes I've heard and I'm thinking maybe I should help her out."
    choice("escalation2_screen2") "Continue"

  elif bp_force_store_owner_rent==3:        ## third call is game over event
    header "You Receive a Call from {mark}[ns_teacher_name]{/}"
    ##  GRAPHICS
    $act.start_block("l:440 c:content_width-440")
    $action_image= "quests friends_with_benefits fwb_220"
    center "{image=[action_image]@400x600}"
    ""
    $action_image= "quests friends_with_benefits fwb_221"
    center "{image=[action_image]@400x600}"
    ##  TEXT
    $act.set_block("c")
    "You receive a call from {mark}[ns_teacher_name]{/} and she is angry; {say}Hi {mark}[mc.name]{/}, I guess you're not the man I thought you were. {mark}[gn_store_owner_name]{/} just moved in with me and neither of us ever want to see you again.{/}"
    extend " {say}Our partnership is over and I've blacklisted you with all my contacts so you can forget selling high priced bots anywhere around here. I really expected more from you.{/} Without waiting for a reply she hangs up."
    ""
    "{bad}Oh no! I didn't expect to get blacklisted as well as losing the partnership and relationships. I think I'm in big trouble!{/}"
    choice("escalation3_screen2") "Continue"
  return

##============ escalation 1 additional screens ============

label escalation1_screen2():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[gn_diner_owner_name]{/} Visits Your Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_222"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_223"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{mark}[gn_diner_owner_name]{/} hesitates before saying; {say}You two are friends and your shop is doing well now, can't you afford to help her out?{/}"
  extend " I reply; {mcsay}I've been thinking about that and trying to decide if I can afford it.{/} {mark}[gn_diner_owner_name]{/} looks me in the eye; {say}I hope you make the right decision.{/}"
  ""
  ""
  "After a brief silence {mark}[gn_diner_owner_name]{/} says; {say}I have to get back to the diner. Please help {mark}[gn_store_owner_name]{/} out, she's really worried.{/}"
  extend " I reply; {mcsay}Thanks for telling me about this {mark}[gn_diner_owner_name]{/}, it certainly makes my decision more urgent.{/}"
  choice("escalation1_screen3") "Continue"
  return

label escalation1_screen3():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "{mark}[gn_diner_owner_name]{/} Visits Your Shop"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_224"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_225"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  ""
  "{mark}[gn_diner_owner_name]{/} looks at me for a short time without saying anything and then turns around and slowly leaves the shop."
  ""
  ""
  ""
  ""
  "I've been thinking about helping {mark}[gn_store_owner_name]{/} out for a while now. If I don't help her out she'll probably have to live in her store. I guess I need to make a decision."
  choice("<<<") "Continue"
  return

##============ escalation 2 additional screen ============

label escalation2_screen2():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "You Receive a Call from {mark}[ns_teacher_name]{/}"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_226"
  center "{image=[action_image]@400x600}"
  ""
  $action_image= "quests friends_with_benefits fwb_227"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "{mark}[ns_teacher_name]{/} sounds angry; {say}Listen kid, I've helped you make a lot of money so I know you can afford to help her out. If you don't then I'll have to help her and if that happens our partnership is over!{/} Without waiting for a reply she hangs up on me."
  ""
  ""
  "Wow, she's pretty upset. If I don't help {mark}[gn_store_owner_name]{/} out I'll lose everything, my partnership with {mark}[ns_teacher_name]{/} and probably my relationships with both her and {mark}[gn_store_owner_name]{/}. Do I really want to sacrifice all of that?"
  choice("<<<") "Continue"
  return

##============ escalation 3 additional screens ============

label escalation3_screen2():
  $game_bg="home bg"
  $game_bgm="home bgm"
  header "You Receive a Call from {mark}[ns_teacher_name]{/}"
  ##  GRAPHICS
  $act.start_block("l:440 c:content_width-440")
  $action_image= "quests friends_with_benefits fwb_228"
  center "{image=[action_image]@400x600}"
  ##  TEXT
  $act.set_block("c")
  "Everyone in the neighborhood liked {mark}[gn_store_owner_name]{/} so they look the other way whenever they see me."
  ""
  "Since I can't sell bots to rich people I can only continue handling customers who walk into the shop and selling bots and parts on the grey net."
  ""
  "{bad}I spend the rest of my life running my little shop in a neighborhood full of people who won't talk to me. Too bad I didn't do things differently.{/}"
  choice("fwb_escalate_apartment_rent_game_over",hint="{bad}Bad Ending{/}") "Continue"
  return


label fwb_escalate_apartment_rent_game_over:
  $set_interaction("ending")
  $act["ending_type"]="bad"
  $game_bg="black"
  ""
  "executed 'fwb_escalate_apartment_rent_game_over'"
  ""
  $exit_main_loop=True
  return