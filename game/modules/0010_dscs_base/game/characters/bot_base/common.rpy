init -900 python:
  def load_info_table_from_mods(table_id,id_entry="id"):
    rv={}
    for mod in game_mods:
      table=mod.get(table_id)
      if table:
        for info in table:
          id=info.get(id_entry)
          if id and not info.get("do_not_register",False):
            if id.startswith("-"):
              rv={k:v for k,v in rv.items() if not fnmatch.fnmatchcase(k,id[1:])}
            else:
              rv[id]=info
    return rv
