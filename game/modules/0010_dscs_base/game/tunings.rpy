init -1950 python:
  def sanitize_mod_game_tunings(mod):
    tunings=mod.get("dscs_tunings")
    if isinstance(tunings,dict):
      tunings={k.lower():v for k,v in tunings.items()}
      mod["dscs_tunings"]=tunings

  game_mods_sanitizers.append(sanitize_mod_game_tunings)

init -1850 python:
  game_tunings={}

  def load_game_tunings_from_mods():
    for mod in game_mods:
      tunings=mod.get("dscs_tunings")
      if tunings:
        game_tunings.update(tunings)

  load_game_tunings_from_mods()
