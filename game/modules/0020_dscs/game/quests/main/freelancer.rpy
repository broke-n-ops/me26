init python:
  class Quest_freelancer(Quest):
    name="Freelancer"
    class phase_1_free_roam:
      description="No debts, no ties, no set paths. Now what to do?...Maybe find a better shop and place to live?  I'll need money for that!"
    class phase_1000_done:
      description="I'm not working by myself any more! I'll make more money in a business partnership with {mark}[ns_teacher_name]{/} and it will be fun too!"
    class phase_2000_failed:
      description="-failed-"
