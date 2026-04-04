init -10 python:
  class BotSkill(BaseStat):
    do_not_register=True
    stat_type="bot_skill"
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
