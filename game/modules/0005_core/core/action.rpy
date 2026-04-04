init -100 python:
  class GameAction(Action):
    def __init__(self,action,action_cost=None,hint=None,sensitive_if=True,selected_if=False):
      super(GameAction,self).__init__()
      self.action=action
      self.action_cost=action_cost
      self.hint=hint
      self.sensitive_if=sensitive_if
      self.selected_if=selected_if
    def __call__(self):
      if not self.get_selected():
        if hasattr(store,"game"):
          game.pc.apply_action_cost(self.action_cost)
        action=self.action
        if isinstance(action,str):
          if action.startswith("$"):
            action=action[1:]
            if not action.startswith("!"):
              exec(action)
              renpy.restart_interaction()
            else:
              exec(action[1:])
            return
          elif action.startswith("="):
            return eval(action[1:])
        elif isinstance(action,(list,tuple,Action)):
          return renpy.run_action(action)
        return action
    def get_sensitive(self):
      if self.get_selected():
        return True
      if hasattr(store,"game") and not game.pc.check_action_cost(self.action_cost)[0]:
        return False
      action=self.action
      if action:
        if isinstance(action,(list,tuple,Action)):
          return renpy.is_sensitive(action)
        condition=self.sensitive_if
        if isinstance(condition,str) and condition.startswith("$"):
          return bool(eval(condition[1:]))
        return bool(condition)
    def get_selected(self):
      action=self.action
      if isinstance(action,(list,tuple,Action)):
        return renpy.is_selected(action)
      condition=self.selected_if
      if isinstance(condition,str) and condition.startswith("$"):
        return bool(eval(condition[1:]))
      return bool(condition)
##    def get_tooltip(self):
##      action=self.action
##      if isinstance(action,(list,tuple,Action)):
##        return renpy.display.behavior.get_tooltip(action)
##      return self.hint
