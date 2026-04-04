init -100 python:
  bot_roles_cls_by_id={}

  def find_bot_role_cls(bot_role_cls_id):
    return bot_roles_cls_by_id.get(bot_role_cls_id)

  class BotRoleMeta(type):
    def __init__(cls,name,bases,dct):
      if "id" not in dct:
        cls.id=name[8:] if name.lower().startswith("botrole_") else name
      if not dct.get("do_not_register",False):
        bot_roles_cls_by_id[cls.id]=cls
    def __str__(cls):
      return cls.default_name

  class BotRole(object,metaclass=BotRoleMeta):
    do_not_register=True
    role_name="- role name -"
    description="- bot role description -"

    hidden=False
    selectable=True

    role_tags={}

    allowed_actions=None
    blocked_actions=None

    requirements=[]

    def __init__(self,*args,**kwargs):
      super(BotRole,self).__init__()
      self.owner=kwargs.get("owner")

    def __str__(self):
      return self.name

    @property
    def name(self):
      if isinstance(self.role_name,str):
        if self.role_name.startswith("$"):
          return eval(self.role_name[1:],{"bot":self.owner})
        else:
          return self.role_name
      return self.id

    @classproperty
    def default_name(cls):
      if isinstance(cls.role_name,str):
        if cls.role_name.startswith("$"):
          return eval(cls.role_name[1:],{"bot":None})
        else:
          return cls.role_name
      return cls.id

    @property
    def owner(self):
      return find_character(self._owner)
    @owner.setter
    def owner(self,owner):
      owner=find_character(owner)
      self._owner=getattr(find_character(owner),"id",None)

    @classmethod
    def check_requirements(cls,bot):
      reqs_met=True
      rv=[]
      for req_test,req_desc in (cls.requirements):
        if callable(req_test):
          req_test=req_test(bot)
        elif isinstance(req_test,str):
          req_test=eval(req_test,{"bot":bot})
        req_test=bool(req_test)
        reqs_met=reqs_met and req_test
        rv.append((req_test,req_desc))
      return reqs_met,rv

    def can_add(self,bot):
      return self.check_requirements(bot)[0]

    def can_remove(self,bot):
      return True

    def interact_actions(self):
      return []

init -90 python:
  modded_bot_role_tags={}
  modded_bot_roles_classes={}

  def load_bot_roles_from_mods():
    role_tags_info=load_info_table_from_mods("dscs_role_tags")
    for tag,tag_info in sorted(role_tags_info.items(),key=lambda item: (item[1]["list_priority"],item[0])):
      if tag_info:
        modded_bot_role_tags[tag]=tag_info.copy()
    roles_info=load_info_table_from_mods("dscs_roles")
    for role_id,role in sorted(roles_info.items()):
      if role:
        role_cls_dct=role.copy()
        role_cls_dct["role_name"]=role_cls_dct.pop("name",role_id)
        role_cls_name="BotRole_"+role_id
        role_cls=type(role_cls_name,(BotRole,),role_cls_dct)
        setattr(store,role_cls_name,role_cls)
        modded_bot_roles_classes[role_id]=role_cls
        if log_modded_entries():
          print("Loaded modded bot role:",role_id)

  load_bot_roles_from_mods()

init python:
  def active_bots_with_role_tag(tag,ignore=None):
    if not isinstance(ignore,(list,tuple)):
      ignore=[ignore]
    rv=[]
    for bot in home.sexbots:
      if bot and bot not in ignore and not bot.chassis.is_disabled and not bot["mission"]:
        efficiency=bot.role_tag_efficiency(tag)
        if efficiency>0:
          rv.append([bot,efficiency])
    return rv
