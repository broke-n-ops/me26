define config.window_icon="gui/window_icon.png"

define config.has_sound=True
define config.has_music=True
define config.has_voice=True

init python:
  if has_audio("main_menu_bgm"):
    config.main_menu_music="main_menu_bgm"
  else:
    config.main_menu_music=None
  if has_audio("game_menu_bgm"):
    config.game_menu_music="game_menu_bgm"
  else:
    config.game_menu_music=None

define config.fade_music=0.5
define config.main_menu_music_fadein=0
define config.context_fadein_music=0
define config.context_fadeout_music=0

define config.default_sfx_volume=1.0
define config.default_music_volume=0.5
define config.default_voice_volume=0.0

define config.default_fullscreen=True

default preferences.text_cps=0
default preferences.afm_time=15

###############################################################################

define config.window="hide"
define config.narrator_menu=False

define config.autosave_slots=6
define config.quicksave_slots=6
define config.has_autosave=True
define config.has_quicksave=True
define config.autosave_on_choice=False
define config.autosave_on_quit=True

define config.thumbnail_width = 320
define config.thumbnail_height = 180

define config.optimize_texture_bounds=True
define config.mouse_hide_time=None

define config.gl2=True

###############################################################################

define config.allow_skipping=False

#define config.hard_rollback_limit=25
#define config.rollback_length=25
#define config.rollback_enabled=True
