init -50 python:
  class Mission(object):
    id=None
    title="- mission -"
    description="- if you see this, something is wrong -"
    available=False
    requirements=[]
    duration=1
    results=[]

init -10 python:
  modded_missions={}

  def load_missions_from_mods():
    missions_info=load_info_table_from_mods("missions")
    for mission_id,mission in sorted(missions_info.items()):
      if mission_id and mission:
        mission_cls_dct=mission.copy()
        mission_cls_name="Mission_"+mission_id
        mission_cls=type(mission_cls_name,(Mission,),mission_cls_dct)
        setattr(store,mission_cls_name,mission_cls)
        modded_missions[mission_id]=mission_cls
        if log_modded_entries():
          print("Loaded modded mission:",mission_id)

  load_missions_from_mods()

init python:
  def list_available_missions(bot):
    missions=[]
    for mission_id,mission in sorted(modded_missions.items()):
      available=mission.available
      if isinstance(available,str):
        available=eval(available,globals(),{"bot":bot})
      if available:
        missions.append(mission)
    return missions
