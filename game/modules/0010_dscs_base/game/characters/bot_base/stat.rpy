init -10 python:
  class BotStat(BaseStat):
    do_not_register=True
    stat_type="bot_stat"
    min_level=0
    max_level=6
    default_level=3
    level_names=[
      ["{color=#F00}Awful{/}","{color=#F00}Very Bad{/}"],
      "{color=#840}Bad{/}",
      "{color=#880}Meh{/}",
      "Ok",
      "{color=#484}Nice{/}",
      "{color=#080}Good{/}",
      "{color=#0F0}Great{/}",
      ]      
    notify_xp_granted=True
    notify_level_changed=True
    notify_stat_learned=True
    notify_stat_unlearned=True
    xp_to_next_level=[
      3000, # 0->1 - Very Bad
      2000, # 1->2 - Bad
      1000, # 2->3 - Meh
       500, # 3->4 - Ok
      1000, # 4->5 - Nice
      2000, # 5->6 - Good
      3000, # 6    - Great
      ]
    def xp_gain_msg(cls,char,stat,xp):
      if xp>=100:
        return char.name+" {good}"+stat.name+"+++{/}"
      elif xp>=25:
        return char.name+" {good}"+stat.name+"++{/}"
      elif xp>0:
        return char.name+" {good}"+stat.name+"+{/}"
      elif xp<=-100:
        return char.name+" {bad}"+stat.name+"---{/}"
      elif xp<=-25:
        return char.name+" {bad}"+stat.name+"--{/}"
      elif xp<0:
        return char.name+" {bad}"+stat.name+"-{/}"
    def level_changed_msg(cls,char,stat,old_level,level):
      if level>old_level:
        return char.name+" "+stat.name.lower()+" {good}improved{/} to "+stat.level_name_str(level)
      else:
        return char.name+" "+stat.name.lower()+" {bad}lowered{/} to "+stat.level_name_str(level)
