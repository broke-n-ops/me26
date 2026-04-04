init python:
  class Game(BaseGame):
    default_pc="mc"
    difficulty_ids={
      "easy": 1,
      "normal": 2,
      "hard": 3,
      "hardcore": 4,
      1: "easy",
      2: "normal",
      3: "hard",
      4: "hardcore",
    }
    def __init__(self):
      super(Game,self).__init__()
      self.current_mode=None
      self.difficulty=2
    @property
    def difficulty_id(self):
      return self.difficulty_ids[self.difficulty]
    @property
    def hardcore(self):
      return game_tunings.get(self.difficulty_id+"_difficulty_hardcore_mode")
    def mc_xp_rate(self,stat,xp=0):
      stat=find_stat(stat)
      xp_rate=game_tunings.get(self.difficulty_id+"_difficulty_mc_xp_rate",{})
      xp_rate=xp_rate.get(stat.id,1.0)
      if isinstance(xp_rate,str):
        xp_rate=eval(xp_rate,globals(),{"xp":xp,"stat":stat})
      return xp_rate
    def bot_xp_rate(self,bot,stat,xp=0):
      stat=find_stat(stat)
      xp_rate=game_tunings.get(self.difficulty_id+"_difficulty_bots_xp_rate",{})
      xp_rate=xp_rate.get(stat.id,1.0)
      if isinstance(xp_rate,str):
        xp_rate=eval(xp_rate,globals(),{"bot":bot,"xp":xp,"stat":stat})
      return xp_rate
