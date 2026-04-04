init python:
  def generate_bot_part(target,*tags):
    parts=[]
    process_event("generate_bot_part",parts,target,tags)
    if parts:
      part=randwchoice(parts)
      if part:
        part=find_item_cls(part)()
        return part
