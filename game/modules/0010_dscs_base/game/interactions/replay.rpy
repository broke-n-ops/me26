init -100 python:
  class InteractionReplayInteraction(Interaction):
    id="replay"
    def __init__(self,replay_info):
      super(InteractionReplayInteraction,self).__init__()
      self.act_info=replay_info[0]
      store.game_call_stack=replay_info[1]
      store.game_current_label=replay_info[2]
      store.game_current_label_type=replay_info[3]
      store.update_interaction=True
    def finalize(self):
      return self.act_info

default premode_interaction=None

init python:
  def save_premode_interaction():
    store.premode_interaction=((act_screen,act_args,act_kwargs),prev_game_call_stack[:-1],prev_current_label,prev_current_label_type)

  def replay_premode_interaction():
    set_interaction("replay",premode_interaction)
