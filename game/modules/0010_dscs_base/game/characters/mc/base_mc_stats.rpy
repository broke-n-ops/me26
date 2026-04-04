init -10 python:
  class MCStat(BaseStat):
    do_not_register=True
    stat_type="mc_stat"
    min_level=-3
    max_level=3
    default_level=0
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
## 0.14 Added 4+ and 5+ display values as well as 5- and 4-
## main reason was for large gains when selling luxury bots in the 'Business Partners' quest
    def xp_gain_msg(cls,char,stat,xp):
      if xp>=450:
        return "{good}"+stat.name+"+++++{/}"
      elif xp>=250:
        return "{good}"+stat.name+"++++{/}"
      elif xp>=100:
        return "{good}"+stat.name+"+++{/}"
      elif xp>=25:
        return "{good}"+stat.name+"++{/}"
      elif xp>0:
        return "{good}"+stat.name+"+{/}"
      elif xp<=-450:
        return "{bad}"+stat.name+"-----{/}"
      elif xp<=-250:
        return "{bad}"+stat.name+"----{/}"
      elif xp<=-100:
        return "{bad}"+stat.name+"---{/}"
      elif xp<=-25:
        return "{bad}"+stat.name+"--{/}"
      elif xp<0:
        return "{bad}"+stat.name+"-{/}"
    def level_changed_msg(cls,char,stat,old_level,level):
      if level>old_level:
        return char.name+" "+stat.name.lower()+" {good}improved{/} to {mark}"+stat.level_name_str(level)+"{/}"
      else:
        return char.name+" "+stat.name.lower()+" {bad}lowered{/} to {mark}"+stat.level_name_str(level)+"{/}"

  #############################################################################

  class MCSkill(BaseStat):
    do_not_register=True
    stat_type="mc_skill"
    min_level=1
    max_level=7
    default_level=min_level
    level_names="FEDCBAS"
    can_learn_from_xp=True
    notify_xp_granted=True
    notify_level_changed=True
    notify_stat_learned=True
    notify_stat_unlearned=True
    xp_to_next_level=[
      1000,
      2250,
      5000,
      10000,
      22500,
      50000,
      99999,
      ]

  #############################################################################

  class Expertise(BaseStat):
    do_not_register=True
    stat_type=None
    min_level=0
    max_level=6
    default_level=0
    level_names="FEDCBAS"
    can_learn_from_xp=True
    notify_xp_granted=True
    notify_level_changed=True
    notify_stat_learned=True
    notify_stat_unlearned=True
    xp_to_next_level=[
      1000,
      2250,
      5000,
      10000,
      22500,
      50000,
      99999,
      ]
    def xp_gain_msg(self,char,stat,xp):
      if xp>=450:
        return "Expertise: {mark}"+stat.name+"{/} {good}+++++{/}"
      elif xp>=250:
        return "Expertise: {mark}"+stat.name+"{/} {good}++++{/}"
      elif xp>=100:
        return "Expertise: {mark}"+stat.name+"{/} {good}+++{/}"
      elif xp>=25:
        return "Expertise: {mark}"+stat.name+"{/} {good}++{/}"
      elif xp>0:
        return "Expertise: {mark}"+stat.name+"{/} {good}+{/}"
      elif xp<=-450:
        return "Expertise: {mark}"+stat.name+"{/} {bad}-----{/}"
      elif xp<=-250:
        return "Expertise: {mark}"+stat.name+"{/} {bad}----{/}"
      elif xp<=-100:
        return "Expertise: {mark}"+stat.name+"{/} {bad}---{/}"
      elif xp<=-25:
        return "Expertise: {mark}"+stat.name+"{/} {bad}--{/}"
      elif xp<0:
        return "Expertise: {mark}"+stat.name+"{/} {bad}-{/}"
    def level_changed_msg(self,char,stat,old_level,level):
      msg="Your expertise with {mark}"+stat.name+"{/} "
      if self.stat_type=="expertise_bot_model":
        msg+="bot model "
      else:
        msg+="bot part "
      if level>old_level:
        msg+="{good}improved{/} to {mark}"+stat.level_name_str(level)+"{/}"
      else:
        msg+="{bad}lowered{/} to {mark}"+stat.level_name_str(level)+"{/}"
      return msg
    def learned_msg(self,char,stat):
      msg="You started to learn about {mark}"+stat.name+"{/} "
      if self.stat_type=="expertise_bot_model":
        msg+="bot model "
      else:
        msg+="bot part "
      msg+="inner workings"
      return msg

  #############################################################################

  class Reputation(BaseStat):
    do_not_register=True
    stat_type="rep"
    min_level=-3
    max_level=3
    default_level=0
    level_names=[
      ["{color=#F00}Enemy{/}","F"],
      ["{color=#840}Hostile{/}","E"],
      ["{color=#880}Unfriendly{/}","D"],
      ["Neutral","C"],
      ["{color=#484}Associate{/}","B"],
      ["{color=#080}Good{/}","A"],
      ["{color=#0F0}Ally{/}","S"],
      ]      
    can_learn_from_xp=True
    notify_xp_granted=True
    notify_level_changed=True
    notify_stat_learned=True
    notify_stat_unlearned=True
    xp_to_next_level=[
      3000, # 0->1
      2000, # 1->2
      1000, # 2->3
       500, # 3->4
      1000, # 4->5
      2000, # 5->6
      3000, # 6
      ]
    def xp_gain_msg(cls,char,stat,xp):
      if xp>=450:
        return "Rep: {mark}"+stat.name+"{/} {good}+++++{/}"
      elif xp>=250:
        return "Rep: {mark}"+stat.name+"{/} {good}++++{/}"
      elif xp>=100:
        return "Rep: {mark}"+stat.name+"{/} {good}+++{/}"
      elif xp>=25:
        return "Rep: {mark}"+stat.name+"{/} {good}++{/}"
      elif xp>0:
        return "Rep: {mark}"+stat.name+"{/} {good}+{/}"
      elif xp<=-450:
        return "Rep: {mark}"+stat.name+"{/} {bad}-----{/}"
      elif xp<=-250:
        return "Rep: {mark}"+stat.name+"{/} {bad}----{/}"
      elif xp<=-100:
        return "Rep: {mark}"+stat.name+"{/} {bad}---{/}"
      elif xp<=-25:
        return "Rep: {mark}"+stat.name+"{/} {bad}--{/}"
      elif xp<0:
        return "Rep: {mark}"+stat.name+"{/} {bad}-{/}"
    def level_changed_msg(cls,char,stat,old_level,level):
      if level>old_level:
        return "Your reputation with {mark}"+stat.name+"{/} {good}improved{/} to {mark}"+stat.level_name_str(level)+"{/}"
      else:
        return "Your reputation with {mark}"+stat.name+"{/} {bad}lowered{/} to {mark}"+stat.level_name_str(level)+"{/}"
    def learned_msg(cls,char,stat):
## changed in 0.8 when the 'Neighborhood' group was created
##      return "You contacted {mark}"+stat.name+"{/}"
      return "The {mark}"+stat.name+"{/} group noticed you."
    def unlearned_msg(cls,char,stat):
##      return "You lost contact with {mark}"+stat.name+"{/}"
      return "The {mark}"+stat.name+"{/} group lost interest in you."

  #############################################################################

  class MCReputation(BaseStat):
    do_not_register=True
    stat_type="mc_rep"
    min_level=1
    max_level=7
    default_level=1
    level_names="FEDCBAS"
    can_learn_from_xp=True
    notify_xp_granted=True
    notify_level_changed=True
    notify_stat_learned=True
    notify_stat_unlearned=True
    xp_to_next_level=[
      1000,
      2250,
      5000,
      10000,
      22500,
      50000,
      99999,
      ]
## 0.12.n revised cutoff values for +,++,+++,-,--,---: related to 'pr_overall_scale', if 1.0 settings are 180, 90 - in 0.12.5 value is 1.2
    def xp_gain_msg(cls,char,stat,xp):                              
      if xp>=432:
        return "Personal rep: {mark}"+stat.name+"{/} {good}+++++{/}"
      elif xp>=324:
        return "Personal rep: {mark}"+stat.name+"{/} {good}++++{/}"
      elif xp>=216:
        return "Personal rep: {mark}"+stat.name+"{/} {good}+++{/}"
      elif xp>=108:
        return "Personal rep: {mark}"+stat.name+"{/} {good}++{/}"
      elif xp>0:
        return "Personal rep: {mark}"+stat.name+"{/} {good}+{/}"
      elif xp<=-432:
        return "Personal rep: {mark}"+stat.name+"{/} {bad}-----{/}"
      elif xp<=-324:
        return "Personal rep: {mark}"+stat.name+"{/} {bad}----{/}"
      elif xp<=-216:
        return "Personal rep: {mark}"+stat.name+"{/} {bad}---{/}"
      elif xp<=-108:
        return "Personal rep: {mark}"+stat.name+"{/} {bad}--{/}"
      elif xp<0:
        return "Personal rep: {mark}"+stat.name+"{/} {bad}-{/}"
    def level_changed_msg(cls,char,stat,old_level,level):
      if level>old_level:
        return "Your reputation as {mark}"+stat.name+"{/} {good}improved{/} to {mark}"+stat.level_name_str(level)+"{/}"
      else:
        return "Your reputation as {mark}"+stat.name+"{/} {bad}lowered{/} to {mark}"+stat.level_name_str(level)+"{/}"
    def learned_msg(cls,char,stat):
      return "People heard about you as {mark}"+stat.name+"{/}"
    def unlearned_msg(cls,char,stat):
      return "People forgot you was a {mark}"+stat.name+"{/}"
