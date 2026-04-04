style about_text is cs_center

screen about():
  style_prefix "about"
  tag menu
  use game_menu():
    vbox:
      xsize content_width
      align (0.5,0.0)
      null height 32
      label "Credits" xalign 0.5
    vbox:
      align (0.5,0.5)
      text "{size=24}Creator of Defective Sexbot Chop Shop:"
      text "{size=24}{mark}  Radnor{/}{/}"
      ##use vdiv
      text "{size=16} {/}"
      text "{size=24}Developer of Sexbot Restoration 2124 variant:"
      text "{size=24}{mark}  squirrel24{/}{/}"
      ##use vdiv
      text "{size=16} {/}"
      text "{size=24}DSCS Mod Developers Providing Inspiration:{/}"
      text "{size=24}{mark}  Mr_Shaky{/}{/}{size=16}  -  ShakyMod_Parts, ShakyMod_Names, ShakyMod_IllegalFights{/}"
      text "{size=24}{mark}  Daedalron{/}{/}{size=16}  -  Daedalron_bots (sex and ears parts), Missing Parts, Defective Bots{/}"
      text "{size=24}{mark}  ZOM{/}{/}{size=16}  -  zom_vaginas (sex parts) and zom_grey_pigeon_store (Ray's Online){/}"
      text "{size=24}{mark}  Mineride{/}{/}{size=16}  -  Fight_Club (from MR- Missions Pack){/}"
      text "{size=16} {/}"
      ##null height 64
      text "{size=24}Thank you for giving the Sexbot Restoration 2124 variant of DSCS a try!{/}"
    vbox:
      align (0.5,1.0)
      yoffset -16
      text "{size=-8}{hint}Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]{/}{/}" text_align 0.5
