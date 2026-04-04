init -10 python:
  class BotTraitSocialAffinity(BotTrait):
    do_not_register=True
    category="social_affinity"
    xp_mult=1.0
    def on_calc_effective_xp(self,char,stat,xp):
      if stat.id=="bot_social" and xp>0:
        xp=int(round(xp*self.xp_mult))
      return xp

init python:
  class BotTrait_social_smart(BotTraitSocialAffinity):
    name="Social smart"
    description="Learn social-related things faster."
    trait_type="good"
    evolve_into=[("social_smart2",100)]
    xp_mult=1.5

  class BotTrait_social_smart2(BotTraitSocialAffinity):
    name="Social smart+"
    description="Learn social-related things much faster."
    trait_type="good"
    evolve_into=[("social_smart3",100)]
    devolve_into=[("social_smart",100)]
    xp_mult=2.5

  class BotTrait_social_smart3(BotTraitSocialAffinity):
    name="Social smart++"
    description="Learn social-related things extremely fast."
    trait_type="good"
    devolve_into=[("social_smart2",100)]
    xp_mult=5.0

  class BotTrait_social_dumb(BotTraitSocialAffinity):
    name="Social dumb"
    description="Learn social-related things slower."
    trait_type="bad"
    evolve_into=[("social_dumb2",100)]
    xp_mult=0.75

  class BotTrait_social_dumb2(BotTraitSocialAffinity):
    name="Social dumb+"
    description="Learn social-related things much slower."
    trait_type="bad"
    evolve_into=[("social_dumb3",100)]
    devolve_into=[("social_dumb",100)]
    xp_mult=0.5

  class BotTrait_social_dumb3(BotTraitSocialAffinity):
    name="Social dumb++"
    description="Learn social-related things extremely slow."
    trait_type="bad"
    devolve_into=[("social_dumb2",100)]
    xp_mult=0.15

init python:
  class BotTrait_social_smart_inherent(BotTraitSocialAffinity):
    name="Social smart"
    description="Learn social-related things faster."
    trait_type="good"
    inherent=True
    evolve_into=[("social_smart2_inherent",100)]
    xp_mult=1.5

  class BotTrait_social_smart2_inherent(BotTraitSocialAffinity):
    name="Social smart+"
    description="Learn social-related things much faster."
    trait_type="good"
    evolve_into=[("social_smart3_inherent",100)]
    devolve_into=[("social_smart_inherent",100)]
    xp_mult=2.5

  class BotTrait_social_smart3_inherent(BotTraitSocialAffinity):
    name="Social smart++"
    description="Learn social-related things extremely fast."
    trait_type="good"
    devolve_into=[("social_smart2_inherent",100)]
    xp_mult=5.0

init python hide:
  @event_handler("stat_xp_granted")
  def add_social_traits(char,stat,xp):
    if isinstance(char,SexBot):
      if stat.id=="bot_social" and xp>0:
        stability_threshold=100
        xp_threshold=50
        roll_threshold=90
        if char.psychocore.stability<=stability_threshold:
          trait=char.psychocore.has_trait_category("social_affinity")
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
              trait=randchoice(["social_smart","social_dumb"])
              trait=char.psychocore.add_trait(trait)
    return xp
