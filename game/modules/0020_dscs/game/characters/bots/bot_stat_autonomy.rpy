init python:
  class BotStat_autonomy(BotSkill):
    id="autonomy"
    name="Autonomy"
    stat_type="bot_stat"

    def on_calc_effective_xp(self,char,stat,xp):
      if isinstance(char,SexBot):
        if stat.id=="autonomy":
          if not char.chassis.cpu or stat>=char.psychocore.autonomy_cap:
            return 0
        elif stat.level>char.autonomy.level:
          xp=xp//((stat.level-char.autonomy.level)**2+1)
      return xp

init python hide:
  @event_handler("stat_xp_granted")
  def sexbot_autonomy_xp_from_skills(char,stat,xp):
    if isinstance(char,SexBot):
      if stat.stat_type=="bot_skill":
        if stat.id!="autonomy":
          if xp>0:
            char.give_xp("autonomy",xp//3)
