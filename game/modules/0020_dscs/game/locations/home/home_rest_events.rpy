init python hide:
  @random_event("home_sleep")
  def home_sleep_none():
    return None,100

  @random_event("home_sleep")
  def home_sleep_debt_nightmare():
    if mc.money<mc.debt_pending:
      return "home_sleep_debt_nightmare_init",20

label home_sleep_debt_nightmare_init:
  choice("home_sleep_debt_nightmare") "Sleep"
  return

label home_sleep_debt_nightmare:
  header "[workshop]"
  "Shop is empty, maybe the recent attacks nearby is the reason everyone is staying home."
  ""
  "Oh, someone enters, finally some business."
  "{say}Hello there. Nice shop you have! Really nice.{/}"
  "Well, customer is money, even if weird one. {mcsay}Hi, can i help?{/}"
  "{say}Yes, I am looking for one heart implant, model {mark}36-HX9{/} to be precise.{/}"
  "{mcsay}I'm afraid only model {mark}36-HX9{/} I have is inside my own chest, not to mention I mostly deal in bots. But if you leave an order I may ask around for it and notify you when I have a seller.{/}"
  "{say}Oh, don't worry, [mc.pronoun[mr]][mc], I'll take the one you have now. You owe my client a lot of money and he's afraid this is the only way he'll ever get it back. GET [mc.himher!u] TO THE CHAIR!{/}"
  "Dozens of hands grabs you from every direction, tearing your clothes, scratching your skin and moving you to huge operational chair. A masked person approaches you - {say}Do not flail, extreme adrenalyne levels may impact the implant and ...{/}"
  choice("home_sleep_debt_nightmare_end") "AAAAAAAAA!!!"
  return

label home_sleep_debt_nightmare_end:
  header "[home] - Sleep"
  "{mcsay}NOOO! FUCK! Fuck! Fuck... Shit...{/}"
  ""
  "No one grabbing you, no one around. Your shirt and bed is wet with cold sweat."
  ""
  "It was just a nightmare. Your personal, recurring nightmare since you left home and have to worry about money. Where does this heart implant idea come from anyway? Dreams are weird!"
  ""
  "You undress, change bedsheets, and try to get back to sleep."
  ""
  "You can't stop thinking about how hard it is to make money. If you just had more money maybe the nightmares would stop."
  $mc.givexp("mood",randint(-300,-50))
  ""
  "{mcsay}Shit... Fuck you all, I'll figure this out! One day I'll be rich!{/}"
  choice("home_sleep_finish") "Sleep"
  return
