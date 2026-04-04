init -100 python:
  bot_part_defects_cls_by_id={}

  def find_bot_part_defect_cls(bot_part_cls_id):
    return bot_part_defects_cls_by_id.get(bot_part_cls_id)

  class BotPartDefectMeta(type):
    def __init__(cls,name,bases,dct):
      if "id" not in dct:
        cls.id=name[14:] if name.lower().startswith("botpartdefect_") else name
      if not dct.get("do_not_register",False):
        bot_part_defects_cls_by_id[cls.id]=cls
    def __str__(cls):
      return cls.name

  class BotPartDefect(object,metaclass=BotPartDefectMeta):
    do_not_register=True
    name="bot part defect"
    description="- bot part defect description -"
    fix_requirements=[]
    can_apply_multiple=False
    disabling=False
    repairable=True
    destroyed=False
    difficulty=1.0
    part_price_mult=1.0
    xp_mult=1
    def __init__(self,*args,**kwargs):
      super(BotPartDefect,self).__init__()
      self.fix_progress=kwargs.get("fix_progress",0)
      self.integrity_cap=kwargs.get("integrity_cap",100)
    @property
    def fix_progress(self):
      return self._fix_progress
    @fix_progress.setter
    def fix_progress(self,fix_progress):
      self._fix_progress=min(100,max(0,fix_progress))
    def flavor_text(self,situation):
      return ""
    def __str__(self):
      return self.name

init 70 python:
  modded_bot_part_defect_classes={}

  def load_bot_part_defects_from_mods():
    defects_info=load_info_table_from_mods("bot_part_defects")
    for defect_id,defect in sorted(defects_info.items()):
      if defect:
        defect_cls_dct=defect.copy()
        defect_cls_name="BotPartDefect_"+defect_id
        defect_cls=type(defect_cls_name,(BotPartDefect,),defect_cls_dct)
        setattr(store,defect_cls_name,defect_cls)
        modded_bot_part_defect_classes[defect_id]=defect_cls
        if log_modded_entries():
          print("Loaded modded bot part defect:",defect_id)

  load_bot_part_defects_from_mods()
