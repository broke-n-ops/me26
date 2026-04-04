##  Variables for Scrolling Slots  -  section added by squirrel
init python:
  rays_current_row=0    ##  Used in file 'store_raysbotshop.rpy'

label netconsole_net_sites:
  header "[netconsole] - Bookmarks"
  ""
  "I keep useful sites on the net in my {mark}Bookmarks{/} although there's not much here. Most sites require {mark}credentials{/} or {mark}paid subscriptions{/} to view them, I can't believe they used to let anyone visit net sites for free!"
  ""
  "Damn, I miss the old free porn sites! {mark}Gr8Pron{/} blocked me again, maybe I should figure out a new way to hack into the site!"
  ""
  "Social media is a waste of time so I don't bother hacking into {mark}FaceNet{/} and since I never graduated from high school why bother hacking into {mark}JobScout{/}!"
  ""
  "I like {mark}WikiKnowsIt{/} but they blocked my hack a long time ago and I've been too busy, or maybe just too lazy, to figure out a new one."
  ""
##  $print "inside netconsole_net_sites.rpy - rays_online_activated:",rays_online_activated
  if rays_online_activated!=0:                               ##  Ray's online store is active - could be 1 or 2 so not 0 works
    "At least the guy at {mark}Raymond's Bot Boutique{/} gave me access credentials to {mark}Ray's Bots Online{/}."
  call random_event("roaming_net_sites")                     ## 0.9.1 - fixed, was "grey_net"
  if _return=="default":
    choice(None) "Gr8Pron"
    choice(None) "FaceNet"
    choice(None) "JobScout"
    choice(None) "WikiKnowsIt"
    if rays_online_activated!=0:                             ## Ray's online store is active - could be 1 or 2 so not 0 works
      $rays_current_row=1                                    ## set current row to 1
      choice(">>>rays_online_store") "Ray's Online"
    choice("goto_home",pos=16,key="home") "Log out"
    choice("roaming_netconsole",pos=17,key="cancel") "Back"
  $process_event("roaming_finalize_net_sites")               ## 0.9.1 - fixed, was "grey_net"
  $process_event("roaming_finalize","net_sites")             ## 0.9.1 - fixed, was "grey_net"
  return