screen modding_request():
  style_prefix "game_mods"
  tag menu
  use game_menu(scroll=True,right_panel="game_mods_right_panel"):
    vbox:
      xsize content_width
      xalign 0.5
      null height 32
      label "{size=-10}Modding {mark}Sexbot Restoration 2124{/} (SR24)" xalign 0.5
      use vdiv
      text ""
      text "{good}Please Do:{/} Make mods that add to the game!"
      text ""
      text "{bad}Please Don't:{/} Please don't create mods that alter the quests in the game that make up the SR24 story line. These quests are identified within the game like this: {mark}Framed!(SL){/}. Changing the activities and events in the story line quests will make the story inconsistent and illogical. I cannot prevent you from doing this, all I can do is ask."
      text ""
      text "{good}Please Do:{/} If you decide not to respect my request regarding changing the SR24 story line quests please create your own game rather than calling what you are doing a mod for SR24. I publish the source code for SR24 for this purpose. The only restriction is that you must mention {mark}Radnor{/} and {mark}'Defective Sexbot Chop Shop' (DSCS){/} because he requested this of anyone who uses his source code. {mark}Note: You must use Renpy version 7.4.11 because the source code is not compatible with more recent versions of Renpy.{/}"
      text ""
      text "{good}Suggestion:{/} When modding other people's games please be considerate. If they ask you not to make a particular mod of their game honor their request."