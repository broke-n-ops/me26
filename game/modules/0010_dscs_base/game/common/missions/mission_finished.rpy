label mission_finished_default(bot,result):
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [bot.model_id] avatar@240x360}"
  $act.set_block("c")
  "[result[result_text]!i]"
  call mission_finished_process_changes(bot,result)
  $act.end_block()
  return

label mission_finished_bot_dead(bot,result):
  call mission_finished_default(bot,result)
  $move_sexbot(bot,None)
  return

label mission_finished_process_changes(bot,result):
  if "call_label" in result:
    $call_label=result["call_label"]
    if isinstance(call_label,str):
      $call_label=(call_label,(),{})
    call expression call_label[0] pass(bot,*call_label[1],**call_label[2])
  if "exec" in result:
    $exec(result["exec"])
  python hide:
    if "damage" in result:
      damages={}
      for slot_id,damage_hits in result["damage"].items():
        for damage in damage_hits:
          if isinstance(damage,str):
            damage=eval(damage)
          if isinstance(damage,(list,tuple)):
            damage=randint(*damage)
          if slot_id=="any":
            slot_id=randchoice(bot.outfit_slots)
          if not slot_id.startswith("bot_"):
            slot_id="bot_"+slot_id
          if slot_id in bot.outfit_slots:
            damages[slot_id]=damages.get(slot_id,0)+damage
      for slot_id,damage in sorted(damages.items()):
        bot.chassis.apply_part_damage(slot_id,"mission",damage,1,False)
    if "xp_change" in result:
      for skill,xp in sorted(result["xp_change"].items()):
        if not skill.startswith("bot_"):
          skill="bot_"+skill
        if isinstance(xp,str):
          if xp in ("next","prev","zero"):
            bot.givexp(skill,xp)
            xp=0
          else:
            xp=eval(xp)
        if isinstance(xp,(list,tuple)):
          xp=randint(*xp)
        if xp>0:
          bot.givexp(skill,xp)
    if "loot" in result:
      for loot in result["loot"]:
        if loot["type"]=="money":
          value=loot["value"]
          if isinstance(value,str):
            value=eval(value)
          if isinstance(value,(list,tuple)):
            value=randint(*value)
          if value>0:
            mc.money+=value
        elif loot["type"]=="part":
          count=loot.get("count",1)
          if isinstance(count,str):
            count=eval(count)
          if isinstance(count,(list,tuple)):
            count=randint(*count)
          parts=[]
          process_event("generate_bot_part",parts,loot.get("event","mission_loot"),tuple(loot.get("tags",[])))
          if "filter" in loot:
            filter=loot["filter"]
            if isinstance(filter,str):
              filter=eval(filter)
            if callable(filter):
              parts=[part for part in parts if filter(find_item_cls(part[0]))]
          if parts:
            for n in range(count):
              part=randwchoice(parts)
              part=find_item_cls(part)()
              integrity=loot.get("integrity",100)
              if isinstance(integrity,str):
                integrity=eval(integrity)
              if isinstance(integrity,(list,tuple)):
                integrity=randint(*integrity)
              part.apply_damage(100-integrity,1,True)
              workshop.add_item(part)
              notify("{size=-8}Part added {mark}"+str(part)+"{/}, integrity: {mark}"+str(part.integrity)+"%{/}{/}")

##              print("loot: part",part,part.integrity)

    if "mc_xp_change" in result:
      for skill,xp in sorted(result["mc_xp_change"].items()):
        if isinstance(xp,str):
          if isinstance(xp,str):
            if xp in ("next","prev","zero"):
              mc.givexp(skill,xp)
              xp=0
            else:
              xp=eval(xp)
        if isinstance(xp,(list,tuple)):
          xp=randint(*xp)
        if xp>0:
          mc.givexp(skill,xp)
    if "mood_change" in result:
      mood_change=result["mood_change"]
      if isinstance(mood_change,str):
        mood_change=eval(mood_change)
      if isinstance(mood_change,(list,tuple)):
        mood_change=randint(*mood_change)
      mc.givexp("mood",mood_change)
  return

label mission_finished(bot):
  $bot=find_character(bot)
  $mission=modded_missions[bot["mission"]]
  header "[bot] - {mark}[mission.title!i]{/} mission"
  python hide:
    mission_result=mission.results
    while True:
      results=[]
      for result in mission_result:
        condition=result.get("condition",True)
        if isinstance(condition,str):
          condition=eval(condition)
        if condition:
          weight=result["weight"]
          if isinstance(weight,str):
            weight=eval(weight)
          results.append((result,weight))
      mission_result=randwchoice(results)
      if mission_result["type"]=="results":
        mission_result=mission_result["results"]
      else:
        break        
    store.mission_result=mission_result

##  squirrel: added 'if...elif...else' to for bypass to operate

  if "bypass_function" in mission_result:
    $bypass_function=mission_result["bypass_function"]    ##  retreive 'bypass_function' value, this is entry function name
    call expression bypass_function pass (bot)            ##  calls bypass function sending bot, mission author knows the rest
    $bot["mission"]=None                                  ##  when returns close the mission and the bot
    $mission=None
    $mission_result=None
    $bot=None
  elif renpy.has_label("mission_finished_"+mission_result["type"]):                      ##  squirrel note: only one is "bot_dead"
    call expression "mission_finished_"+mission_result["type"] pass (bot,mission_result)
    $bot["mission"]=None
    $mission=None
    $mission_result=None
    $bot=None
    choice("<<<") "Continue"
  else:
    call mission_finished_default(bot,mission_result)
    $bot["mission"]=None
    $mission=None
    $mission_result=None
    $bot=None
    choice("<<<") "Continue"

##  squirrel: I added a 'return' statement, just seemed like a good idea

  return