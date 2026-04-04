init -500 python:
  interactions_by_id={}

  def find_interaction_cls(interaction_id):
    return interactions_by_id.get(interaction_id)

  def reset_interaction(interaction_id,*args,**kwargs):
    store.act=find_interaction_cls(interaction_id)(*args,**kwargs)

  def set_interaction(interaction_id,*args,**kwargs):
    if store.act.id!=interaction_id:
      interaction=find_interaction_cls(interaction_id)(*args,**kwargs)
      interaction.migrate_from(store.act)
      store.act=interaction

  class InteractionMeta(type):
    def __init__(cls,name,bases,dct):
      if "id" not in dct:
        cls.id=name[12:] if name.lower().startswith("interaction_") else name
      if not dct.get("do_not_register",False):
        interactions_by_id[cls.id]=cls

  class Interaction(object,metaclass=InteractionMeta):
    do_not_register=True
    id=None
    def __init__(self):
      super(Interaction,self).__init__()
    def notify(self,notification):
      pass
    def migrate_from(self,old_interaction):
      pass
    def finalize(self):
      return None,tuple(),{}
