init python:
  class Char_mc(Char):
    notify_xp_granted=True
    notify_level_changed=True
    notify_stat_learned=True
    notify_stat_unlearned=True
    notify_money_changed=True

    status_screen="status_mc"
    status_side_screen="status_side_mc"

    gender="male"

    name="Metzger"
    location="home"

    default_stats=[
      ("mood",-1,0.25),
      ("despair",None,0),

      ("combat",None,0),
      ("computers",None,0),
      ("electronics",None,0),
      ("mechanics",None,0),
      ("sex",None,0),
      ("social",None,0),

#      ("rep_mc_trainer",None,0),
#      ("rep_mc_fighter",None,0),

#      ("rep_mitsutachi",-2,0.5),
#      ("rep_rheingerate",0,0.5),
#      ("rep_rivetheads",1,0.62),
       ("rep_syndicate",-3,1),

      ]

    max_energy_base=5

    initial_debt=1000000
    initial_weekly_payments=[1000,2000,3000,5000,10000,15000,20000,30000,50000]

    origin="You were a geeky kid and spent most of your time tinkering with broken down sexbots instead of studying in school.\nSince you never studied you never graduated from high school.\n\nYour parents were fed up and kicked you out when you turned 18. At least they gave you a little money.\nYou decided to rent space in an old warehouse and try to start a business repairing sexbots.\n\nUnfortunately you learned that starting a business is difficult. You've been struggling to make ends meet for almost a year. Maybe if you'd studied at school you'd have a better chance of making this work!"

    def __init__(self,*args,**kwargs):
      super(Char_mc,self).__init__(*args,**kwargs)
      self.energy=self.max_energy
      self.debt=self.initial_debt
      self.weekly_payments=self.initial_weekly_payments
      self.debt_pending=0
      self._traits=[]
      self._implants={}
      self._software=[]

    @property
    def energy(self):
      return self._energy
    @energy.setter
    def energy(self,energy):
      self._energy=max(0,energy)

    @property
    def max_energy(self):
      max_energy=self.max_energy_base
      ## add max energy bonus from workshop upgrades and achievements here - COMMENT BY RADNOR
      return max_energy

    def on_time_advanced(self):
##  MODIFIED BY SQUIRREL IN VERSION 0.2.0 OF SR24
      ##self.energy=self.max_energy                  ##  was
      self.energy=self.max_energy+housekeeper_bonus  ##  is

    def action_cost_to_str(self,cost):
      if isinstance(cost,(list,tuple)):
        if len(cost)==2:
          if cost[0]=="money":
            if cost[1]<0:
##              return "+"+str(abs(cost[1]))+"{size=-4}${/}"
##              return "+{size=-4}${/}"+str(abs(cost[1]))
              return "+$"+str(abs(cost[1]))                   ## 0.11.3 moved $ to beginning and do NOT reduce size
            else:
##              return str(cost[1])+"{size=-4}${/}"
##              return "{size=-4}${/}"+str(cost[1])
              return "$"+str(cost[1])                         ## 0.11.3 moved $ to beginning and do NOT reduce size
              
          elif cost[0]=="char_points":
            return str(cost[1])+"{size=-4}CP{/}"
          elif cost[0]=="energy":
            return str(cost[1])+"{size=-4}AP{/}"
          elif cost[0]=="time":
            return "Time"+(("{size=-4}{hint}x{/}{/}"+str(cost[1])) if cost[1]>1 else "")
          else:
            return "{}: {}".format(cost[0],cost[1])
        elif len(cost)==3:
          return cost[0]
      return str(cost)
    def check_action_cost(self,action_cost):
      rv=[]
      affordable=True
      if action_cost:
        for cost in action_cost:
          if isinstance(cost,str):
            rv.append((True,self.action_cost_to_str(cost)))
          elif isinstance(cost,(list,tuple)):
            if len(cost)==2:
              if cost[0]=="time":
                cost_affordable=True
              else:
                cost_affordable=getattr(self,cost[0])>=cost[1]
              affordable=affordable and cost_affordable
              rv.append((cost_affordable,self.action_cost_to_str(cost)))
            elif len(cost)==3:
              cost_affordable=eval(cost[2])
              affordable=affordable and cost_affordable
              rv.append((cost_affordable,self.action_cost_to_str(cost)))
      return affordable,rv
    def apply_action_cost(self,action_cost):
      if action_cost:
        for cost in action_cost:
          if isinstance(cost,(list,tuple)):
            if len(cost)==2:
              if cost[0]=="time":
                now.advance(cost[1])
              else:
                setattr(self,cost[0],getattr(self,cost[0])-cost[1])
            elif len(cost)==3:
              exec(cost[1])

    def calc_part_repair_progress(self,bot,part,bonus=0):
      skills=[(getattr(self,skill).level,weight) for skill,weight in part.repair_skills]
      total_weight=sum((weight for level,weight in skills))
      skill=sum((level*weight/float(total_weight) for level,weight in skills))
      model_expertise=getattr(self,"expertise_"+bot.model_id).level if bot else 0
      part_expertise=getattr(self,"expertise_"+part.id).level
      base=max(1,int((skill*5+model_expertise*2+part_expertise*3+bonus)/float(part.difficulty)))
      return max(1,randint(base,base*2))

    def calc_part_defect_repair_progress(self,bot,part,defect,bonus=0):
      skills=[(getattr(self,skill).level,weight) for skill,weight in part.repair_skills]
      total_weight=sum((weight for level,weight in skills))
      skill=sum((level*weight/float(total_weight) for level,weight in skills))
      model_expertise=getattr(self,"expertise_"+bot.model_id).level if bot else 0
      part_expertise=getattr(self,"expertise_"+part.id).level
      base=max(1,int((skill*5+model_expertise*2+part_expertise*3+bonus)/float(part.difficulty)))
      return max(1,randint(base*2,base*5))

    def calc_stability_progress(self,bot):
      skill=self.computers.level
      model_expertise=getattr(self,"expertise_"+bot.model_id).level
      base=max(1,skill*2+model_expertise*2)
      return max(1,randint(base//2,base*2))

    def calc_pscychocore_quirk_progress(self,bot,quirk):
      skills=[(getattr(self,skill).level,weight) for skill,weight in quirk.repair_skills]
      total_weight=sum((weight for level,weight in skills))
      skill=sum((level*weight/float(total_weight) for level,weight in skills))
      model_expertise=getattr(self,"expertise_"+bot.model_id).level
      base=max(1,int(round((skill*4+model_expertise*4)/float(quirk.difficulty))))
      return max(1,randint(base//2,base*2))

    def on_calc_effective_xp(self,stat,xp):
      return xp*game.mc_xp_rate(stat,xp)
