## 0.10.n copied functions from 'workshop_fix_random_bot.rpy' for use with the 'master_techie' role
## bot manager integrity minimum reduced to 90% so you must make sure they don't fix themselves

init python:
  def mgr_get_repairable_bots(bot_assistant):
    bots=[]
    for bot in home.sexbots:
      if bot:

##        print "bot: ",bot
##        print "bot_assistant: ",bot_assistant
##        if bot!=bot_assistant:
##          print "NOT equal"
##        else:
##          print "EQUAL"

        if not bot["mission"] and bot!=bot_assistant:      ## bypass the current master techie, they can fix each other though
          for slot,part in bot.outfit.items():
            defects=[(defect_n,defect) for defect_n,defect in enumerate(part.defects)]
            if defects:
              defects.sort(key=lambda x: (100-x[1].integrity_cap,x[1].fix_progress))
              if defects[-1][1].repairable:
                bots.append(("defect",bot.id,slot,defects[-1][0]))
                continue
##  fix in version 0.0.6 to prevent repairing a 'missing part' - part.rate for missing parts is "", all others are FEDCBAS
##  this routine builds a list of possible parts in bots to repair, let's not append a missing part to the list
            ##if part.integrity<part.integrity_cap:                  ##  ORIGINAL LINE
            if part.integrity<part.integrity_cap and part.rate:    ##  NEW LINE

                bots.append(("repair",bot.id,slot))

##    print bots

    return bots

  def mgr_get_random_repairable_bot(bot_assistant):
    bots=mgr_get_repairable_bots(bot_assistant)
    return randchoice(bots) if bots else None