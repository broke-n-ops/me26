init -10 python:
  class BotTraitCombatAffinity(BotTrait):
    do_not_register=True
    category="combat_affinity"
    xp_mult=1.0
    def on_calc_effective_xp(self,char,stat,xp):
      if stat.id=="bot_combat" and xp>0:
        xp=int(round(xp*self.xp_mult))
      return xp

init python:
  class BotTrait_combat_smart(BotTraitCombatAffinity):
    name="Combat smart"
    description="Learn combat-related things faster."
    trait_type="good"
    evolve_into=[("combat_smart2",100)]
    xp_mult=1.5

  class BotTrait_combat_smart2(BotTraitCombatAffinity):
    name="Combat smart+"
    description="Learn combat-related things much faster."
    trait_type="good"
    evolve_into=[("combat_smart3",100)]
    devolve_into=[("combat_smart",100)]
    xp_mult=2.5

  class BotTrait_combat_smart3(BotTraitCombatAffinity):
    name="Combat smart++"
    description="Learn combat-related things extremely fast."
    trait_type="good"
    devolve_into=[("combat_smart2",100)]
    xp_mult=5.0

  class BotTrait_combat_dumb(BotTraitCombatAffinity):
    name="Combat dumb"
    description="Learn combat-related things slower."
    trait_type="bad"
    evolve_into=[("combat_dumb2",100)]
    xp_mult=0.75

  class BotTrait_combat_dumb2(BotTraitCombatAffinity):
    name="Combat dumb+"
    description="Learn combat-related things much slower."
    trait_type="bad"
    evolve_into=[("combat_dumb3",100)]
    devolve_into=[("combat_dumb",100)]
    xp_mult=0.5

  class BotTrait_combat_dumb3(BotTraitCombatAffinity):
    name="Combat dumb++"
    description="Learn combat-related things extremely slow."
    trait_type="bad"
    devolve_into=[("combat_dumb2",100)]
    xp_mult=0.15

init python:
  class BotTrait_combat_smart_inherent(BotTraitCombatAffinity):
    name="Combat smart"
    description="Learn combat-related things faster."
    trait_type="good"
    inherent=True
    evolve_into=[("combat_smart2_inherent",100)]
    xp_mult=1.5

  class BotTrait_combat_smart2_inherent(BotTraitCombatAffinity):
    name="Combat smart+"
    description="Learn combat-related things much faster."
    trait_type="good"
    evolve_into=[("combat_smart3_inherent",100)]
    devolve_into=[("combat_smart_inherent",100)]
    xp_mult=2.5

  class BotTrait_combat_smart3_inherent(BotTraitCombatAffinity):
    name="Combat smart++"
    description="Learn combat-related things extremely fast."
    trait_type="good"
    devolve_into=[("combat_smart2_inherent",100)]
    xp_mult=5.0

init python hide:
  @event_handler("stat_xp_granted")
  def add_combat_traits(char,stat,xp):
    if isinstance(char,SexBot):
      if stat.id=="bot_combat" and xp>0:
        stability_threshold=100
        xp_threshold=50
        roll_threshold=90
        if char.psychocore.stability<=stability_threshold:
          trait=char.psychocore.has_trait_category("combat_affinity")
          stability_mult=1.0-char.psychocore.stability/float(stability_threshold)
          xp_mult=min(xp_threshold,xp)/float(xp_threshold)
          roll_mult=(stability_mult*xp_mult)**2
          roll=int(round(roll_threshold*roll_mult))
          if trait:
            if randint(0,100)<roll:
              evolve_progress=randint(1,35)
              trait.evolve(evolve_progress)
          else:
            if randint(0,100)<roll:
              trait=randchoice(["combat_smart","combat_dumb"])
              trait=char.psychocore.add_trait(trait)
    return xp
