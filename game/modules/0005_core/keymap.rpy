default _game_menu_screen=None

init python:
  ## modify default renpy shortcuts

#  config.keymap["game_menu"]=["K_ESCAPE","mouseup_3","K_MENU","K_PAUSE","K_F10"]
  config.keymap["toggle_fullscreen"]=["alt_K_RETURN","alt_K_KP_ENTER","K_F11"]
  config.keymap["screenshot"]=["alt_K_s","ctrl_K_s"]
  config.keymap["hide_windows"]=["alt_K_h","ctrl_K_h"]
  config.keymap["rollback"]=["ctrl_K_PAGEUP","repeat_ctrl_K_PAGEUP","K_AC_BACK"]
  config.keymap["rollforward"]=["ctrl_K_PAGEDOWN","repeat_ctrl_K_PAGEDOWN"]
  config.keymap["accessibility"]=["alt_K_a","ctrl_K_a"]
  config.keymap["choose_renderer"]=["alt_K_g","ctrl_K_g"]
  config.keymap["self_voicing"]=[]
  config.keymap["clipboard_voicing"]=[]
  config.keymap["debug_voicing"]=[]
  config.keymap["director"]=[]
  config.keymap["help"]=[]
  config.keymap["skip"]=[]
  config.keymap["toggle_skip"]=[]
  config.keymap["fast_skip"]=[]

#  config.pad_bindings["pad_y_press"]=[]

  ## add custom game shortcuts

  config.keymap["quick_save"]=["K_F5"]
  config.keymap["quick_load"]=["K_F8"]

  config.keymap["lesser_game_menu"]=["K_MENU","K_PAUSE","K_F10"]

  config.keymap["home"]=["K_HOME","mouseup_2"]
  config.keymap["cancel"]=["K_ESCAPE","mouseup_3"]

init python:
  ## UI key names

  ui_key_names={
    "game_menu": "esc",
    "lesser_game_menu": "F10",
    "home": "home",
    "cancel": "esc",
    "quick_save": "F5",
    "quick_load": "F8",
    "K_HOME": "home",
    "K_TAB": "tab",
    "K_F1": "F1",
    "K_F2": "F2",
    "K_F3": "F3",
    "K_F4": "F4",
    "K_F5": "F5",
    "K_F6": "F6",
    "K_F7": "F7",
    "K_F8": "F8",
    "K_F9": "F9",
    "K_F10": "F10",
    "K_F11": "F11",
    "K_F12": "F12",
    "shift_K_TAB": "shift_tab",
    "K_KP_ENTER": "enter",
    "K_RETURN": "return",
    "B": "B",                    ## 0.9.m added for capital B shortcut for rollback
    "R": "R",                    ## 0.14 added to change shortcut for rename characters to R so 'n' could be used for 'next'
    }

  def ui_key_name(key):
    if len(key)==1 and "a"<=key<="z" or "1"<=key<="9":
      return key
    return ui_key_names.get(key,"")
