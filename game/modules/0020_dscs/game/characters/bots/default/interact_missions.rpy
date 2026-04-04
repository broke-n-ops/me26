label interact_default_missions(bot):
  header "[bot] - Missions"
  "What's the point of having highly sophisticated bots around if you have to do things yourself. With proper instructions and high enough skills you can send bots to do your biddings."
  ""
  $missions=list_available_missions(bot)[:12]
  if missions:
    $n=0
    while missions:
      $mission=missions.pop(0)
      $n+=1
      "#{mark}[n]{/} - {mark}[mission.title!i]{/} - [mission.description!i]"
      $reqs=list((mission.requirements or [])[:])
      $costs=list((mission.costs or [])[:])
      if reqs or costs:
        $act.start_block("l:440 c")
        $reqs_met=True
        "{size=-8}Requrements:{/}"
        if reqs:
          while reqs:
            $req_condition,req_description=reqs.pop(0)
            "{size=-8}- [req_description]{/}"
            if isinstance(req_condition,str):
              $req_condition=eval(req_condition)
            if not req_condition:
              $reqs_met=False
              extend " {size=-8}{bad}req not met{/}{/}"
        else:
          "{size=-8}{hint}No requirements{/}{/}"
        $act.set_block("c")
        "{size=-8}Costs:{/}"
        if costs:
          while costs:
            $cost=mc.action_cost_to_str(costs.pop(0))
            "{size=-8}{mark}[cost]{/}{/}"
        else:
          "{size=-8}{hint}No costs{/}{/}"
        $act.end_block()
      ""
      if reqs_met:
        interact("start_mission,"+mission.id,cost=mission.costs) "[mission.title!i]"
#        interact("start_mission,"+mission.id,hint="Send on mission") "[mission.title!i]"
      else:
        choice(None,hint="{bad}Reqs not met{/}") "[mission.title!i]"
  else:
    "{info}You can't think of any missions at the moment{/}"
  $mission=None
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return

label interact_default_start_mission(bot,mission):
  $mission=modded_missions[mission]
  header "[bot] - {mark}[mission.title!i]{/} mission"
  $act.start_block("l:440 c:content_width-440")
  center "{image=bots [bot.model_id] avatar@400x600}"
  $act.set_block("c")
  "[mission.launch_text!i]"
  python hide:
    bot["mission"]=mission.id
    duration=mission.duration
    if isinstance(duration,(list,tuple)):
      duration=randint(*duration)
    bot["mission_timer"]=duration
  $act.end_block()
  $mission=None
  choice("end_bot_interaction") "Continue"
  return
 