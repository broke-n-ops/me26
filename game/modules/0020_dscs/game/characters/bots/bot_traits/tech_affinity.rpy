init -10 python:
  class BotTraitTechAffinity(BotTrait):
    do_not_register=True
    category="tech_affinity"
    xp_mult=1.0
    def on_calc_effective_xp(self,char,stat,xp):
      if stat.id in ("bot_mechanics","bot_electronics") and xp>0:
        xp=int(round(xp*self.xp_mult))
      return xp

init python:
  class BotTrait_tech_smart(BotTraitTechAffinity):
    name="Tech smart"
    description="Learn tech-related things faster."
    trait_type="good"
    evolve_into=[("tech_smart2",100)]
    xp_mult=1.5

  class BotTrait_tech_smart2(BotTraitTechAffinity):
    name="Tech smart+"
    description="Learn tech-related things much faster."
    trait_type="good"
    evolve_into=[("tech_smart3",100)]
    devolve_into=[("tech_smart",100)]
    xp_mult=2.5

  class BotTrait_tech_smart3(BotTraitTechAffinity):
    name="Tech smart++"
    description="Learn tech-related things extremely fast."
    trait_type="good"
    devolve_into=[("tech_smart2",100)]
    xp_mult=5.0

  class BotTrait_tech_dumb(BotTraitTechAffinity):
    name="Tech dumb"
    description="Learn tech-related things slower."
    trait_type="bad"
    evolve_into=[("tech_dumb2",100)]
    xp_mult=0.75

  class BotTrait_tech_dumb2(BotTraitTechAffinity):
    name="Tech dumb+"
    description="Learn tech-related things much slower."
    trait_type="bad"
    evolve_into=[("tech_dumb3",100)]
    devolve_into=[("tech_dumb",100)]
    xp_mult=0.5

  class BotTrait_tech_dumb3(BotTraitTechAffinity):
    name="Tech dumb++"
    description="Learn tech-related things extremely slow."
    trait_type="bad"
    devolve_into=[("tech_dumb2",100)]
    xp_mult=0.15

init python:
  class BotTrait_tech_smart_inherent(BotTraitTechAffinity):
    name="Tech smart"
    description="Learn tech-related things faster."
    trait_type="good"
    inherent=True
    evolve_into=[("tech_smart2_inherent",100)]
    xp_mult=1.5

  class BotTrait_tech_smart2_inherent(BotTraitTechAffinity):
    name="Tech smart+"
    description="Learn tech-related things much faster."
    trait_type="good"
    evolve_into=[("tech_smart3_inherent",100)]
    devolve_into=[("tech_smart_inherent",100)]
    xp_mult=2.5

  class BotTrait_tech_smart3_inherent(BotTraitTechAffinity):
    name="Tech smart++"
    description="Learn tech-related things extremely fast."
    trait_type="good"
    devolve_into=[("tech_smart2_inherent",100)]
    xp_mult=5.0

init python hide:
  @event_handler("stat_xp_granted")
  def add_tech_traits(char,stat,xp):
    if isinstance(char,SexBot):
      if stat.id in ("bot_mechanics","bot_electronics") and xp>0:
        stability_threshold=100
        xp_threshold=50
        roll_threshold=90
        if char.psychocore.stability<=stability_threshold:
          trait=char.psychocore.has_trait_category("tech_affinity")
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
              trait=randchoice(["tech_smart","tech_dumb"])
              trait=char.psychocore.add_trait(trait)
    return xp
