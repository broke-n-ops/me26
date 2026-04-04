init python early:
  def version_number(version):
    if not version or version[-1]==".":  ## if version doesn't exist or if it ends in a period it is corrupted
      return minimal_supported_version
    else:
      v=""
      for c in version:
        if c in "0123456789.":
          v+=c
        else:
          break
      v=(int(n) for n in v.split("."))
      return tuple(v)

label after_load:
  $process_event("after_load")
  return
