define transition_speed_min=1.0 ## 1.0 - 50%, 2.0 - 100%, 3.0 - 150%, 4.0 - 200%
define transition_speed_max=4.0
define transition_speed_default=2.0

default persistent.transition_speed_factor=transition_speed_default
default persistent.in_game_transitions=True

define config.enter_transition=Dissolve(0.5)
define config.exit_transition=Dissolve(0.5)
define config.intra_transition=Dissolve(0.5)
define config.after_load_transition=Dissolve(0.5)
define config.end_game_transition=Dissolve(1.0)
define config.end_splash_transition=Dissolve(1.0)
define config.enter_yesno_transition=Dissolve(0.25)
define config.exit_yesno_transition=Dissolve(0.25)
define config.game_main_transition=Dissolve(0.5)
define config.main_game_transition=Dissolve(0.5)

define config.window_show_transition=None
define config.window_hide_transition=None

define splashscreen_transition=Dissolve(1.0)
define intro_transition=Dissolve(1.0)
define interaction_transition=Dissolve(0.5)

define dissolve=Dissolve(0.3)
