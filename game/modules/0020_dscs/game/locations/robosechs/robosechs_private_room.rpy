define label_robosechs_private_room_action_info={"cost": [("money",100),("energy",3)]}

label robosechs_private_room:
  header "[robosechs] - Private Entertainment"
  "You look for a vacant private room and access control terminal. After selecting available toys, you enter the room and sit."
  ""
  $act.start_block("l:440 c:content_width-440")
  $act.set_block("l")
  python:
    models=[]
    process_event("generate_bot",models,"robosechs_private_room",("cheap","nice","good"))
    renpy.random.shuffle(models)
    models=models[:randint(1,2)]
  while models:
    python:
      model_id=find_character_cls(models.pop()[0]).model_id
      action_images=[]
      action_images.append(find_game_image_variant("bots [model_id] :bj"))
      action_images.append(find_game_image_variant("bots [model_id] :sex"))
      action_images=[action_image for action_image in action_images if action_image]
      action_image=randchoice(action_images) if action_images else None
    if action_image:
      center "{image=[action_image]@400x600}"
      ""
  $act.set_block("c")
  "Even after closing the door, you can still hear music outside."
  "Soon it is suppressed by some active noise canceller and replaced with a warm ambient, accompanied by the smell of a mild stimulant."
  "Your entertainment joins you a few minutes after."
  $mc.mood.give_xp(randint(75,250))
  $mc.sex.give_xp(randint(20,75))
  ""
  "That was entertaining indeed."
  $act.end_block()
  call random_event("robosechs_private_room")
  if _return=="default":
    choice("<<<") "Continue"
  return
