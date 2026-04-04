init -100 python:
  name_tables={
    "european_names": ["EUROPEAN NAME"],
    "japanese_names": ["JAPANESE NAME"],
  }

  def load_name_tables_from_mods():
    for mod in game_mods:
      mod_name_tables=mod.get("name_tables")
      if mod_name_tables:
        name_tables.update(mod_name_tables)

  load_name_tables_from_mods()
