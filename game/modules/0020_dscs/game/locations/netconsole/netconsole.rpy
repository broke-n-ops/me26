init python:
  class Location_netconsole(Location):
    name="NetConsole"

define label_goto_netconsole_action_info={
  "title": "[netconsole]",
  }

init python:
  def generate_netconsole_entry_point():
    rv=randchoice(game_tunings["netconsole_entry_points"])
    subs={
      "hex_rnd8": "{:08X}".format(randint(0,0xFFFFFFFF)),
      "hex_rnd8_2": "{:08X}".format(randint(0,0xFFFFFFFF)),
      "hex_rnd8_3": "{:08X}".format(randint(0,0xFFFFFFFF)),
      "hex_rnd8_4": "{:08X}".format(randint(0,0xFFFFFFFF)),
    }
    rv=rv.format(**subs)
    return rv

  def generate_netconsole_ip():
    rv=[randint(1,255),randint(1,255),randint(1,999),randint(300,999)]
    renpy.random.shuffle(rv)
    return ".".join((str(part) for part in rv))

label enter_netconsole:
  $netconsole["entry_point"]=generate_netconsole_entry_point()
  $netconsole["ip"]=generate_netconsole_ip()
  return "goto_netconsole"

label goto_netconsole:
  $game.location="netconsole"
  return "roaming"

label roaming_netconsole:
  $game_bg="home computer"
  $game_bgm="home bgm"
  header "[netconsole]"
  "NetConsole v.17.2.394"
  ""
  "User: {mark}[mc]{/}"
  "Password: {info}************{/}"
  "Bio4FA: {mark}confirmed{/}"
  ""
  "Mesh Network: {mark}26X9A{/}"
  "Access point: {mark}[netconsole[entry_point]]{/}"
  "Assigned IP: {mark}[netconsole[ip]]{/}"
  call random_event("roaming_netconsole")
  if _return=="default":
    choice(None) "Messages"
## 0.9.n simplified grey net bbs by removing intermediate screen
##    choice("netconsole_grey_net") "Grey Net"
    choice(">>>netconsole_grey_market_bbs") "Grey Market BBS"
    choice(None) "Programs"
    choice(None) "Games"
    choice("netconsole_net_sites") "Bookmarks"                 ## ADDED IN 0.4.N FOR RAY'S ONLINE STORE
    choice("goto_home",pos=17,key=["home","cancel"]) "Log out"
  $process_event("roaming_finalize_netconsole")
  $process_event("roaming_finalize","netconsole")
  return
