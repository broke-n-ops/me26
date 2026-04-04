## 0.9.n file no longer needed, function never called because greynet bbs was simplified

# label netconsole_grey_net:
  # header "[netconsole] - Grey Net"
  # "The Grey Net is a great place if you want to do something you're not supposed to. Various servers spread over multiple networks enable you to be anonymous if you know what you're doing. You have to be careful though. If you make a mistake there are a lot of black hats running wild who can trace you."
  # ""
  # "Not everything here is legal and sometimes the illegal stuff is dangerous but the Grey Net provides links to software, services and contacts you wouldn't find normally. Whatever you want, you can find it here. As long as you can pay."
  # ""
  # call random_event("roaming_grey_net")
  # if _return=="default":
    # choice(">>>netconsole_grey_market_bbs") "Grey Market BBS"
    # choice("goto_home",pos=16,key="home") "Log out"
    # choice("<<<",pos=17,key="cancel") "Back"
  # $process_event("roaming_finalize_grey_net")
  # $process_event("roaming_finalize","grey_net")
  # return
