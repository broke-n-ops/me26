init python:
  class RepMCMechanic(MCReputation):
    id="rep_mc_mechanic"
    name="Mechanic"

  class RepMCHacker(MCReputation):
    id="rep_mc_hacker"
    name="Hacker"

  class RepMCSexMachine(MCReputation):
    id="rep_mc_sexmachine"                ##  Used in mods for similar purpose, don't change this and break mods
    name="SexBot Trainer"                 ##  WAS "SexMachine" CHANGE TO "SexBot Trainer" (used in mods for same purpose)

  class RepMCTrainer(MCReputation):
    id="rep_mc_trainer"                   ##  Used in mods for similar purpose, don't change this and break mods
    name="Bot Trainer"                    ##  General purpose, add a little whenever adding "fight trainer" or "sexbot trainer"

  class RepMCFighter(MCReputation):
    id="rep_mc_fighter"                   ##  Used in mods for similar purpose, don't change this and break mods
    name="CombatBot Trainer"              ##  WAS "Fighter" CHANGE TO "CombatBot Trainer" (used in mods for same purpose)

  class RepMCTechTrainer(MCReputation):   ##  0.12.n - create when making Repair Bot mission and add to Work at shop with techies, clerks, and shopkeepers
    id="rep_mc_tech_trainer"
    name="TechBot Trainer"

  class RepMCDealer(MCReputation):        ##  0.12.n - this is for selling bots and parts, bots larger impact than parts!!
    id="rep_mc_dealer"
    name="Bot Dealer"