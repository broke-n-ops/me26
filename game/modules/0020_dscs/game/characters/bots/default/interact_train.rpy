label interact_default_train(bot):
  header "[bot] - Training"
  if bot.chassis.is_disabled:
    "{mark}[bot]{/} is too damaged to train."
  else:
    "{mark}State of the art sexbots{/} are greatly improved over previous generations. If you know what you're doing they are {mark}relatively easy to train{/} and are {mark}no longer limited to sex{/}. If you have both the {mark}knowledge and the know-how{/} you can teach them {mark}new skills{/} or you can {mark}improve their existing skills{/}."
    ""
    "Manufacturers improve some of their models using databases to give them {mark}inherent traits{/} which make them easier to train in {mark}specific skills{/}. These databases are linked into the bot's {mark}psychocore{/} and {mark}can't be altered or removed{/}."
    ""
    "{mark}Brand new bots{/} from the factories are untrained and relatively affordable with the price proportional to the quality of the chassis and parts. {mark}Trained bots with strong skills{/} are much more valuable and the {mark}right buyer will pay a lot more{/} for them."
    ""
    "I can make money repairing and restoring bots but {mark}selling trained bots{/} is where real money can be made. The challenge is {mark}making connections with the right buyers!{/}"
    interact("train_combat") "Combat"
    interact("train_electronics") "Electronics"
    interact("train_mechanics") "Mechanics"
    interact("train_sex") "Sex"
    interact("train_social") "Social"
    if bot.psychocore.stability!=100:
      interact("hack_stabilize",cost=[("energy",1)]) "Stabilize"
    else:
      choice(None,hint="{hint}already stable{/}") "Stabilize"
  choice("end_bot_interaction",pos=16,key="home") "Done"
  choice("<<<",pos=17,key="cancel") "Back"
  return
