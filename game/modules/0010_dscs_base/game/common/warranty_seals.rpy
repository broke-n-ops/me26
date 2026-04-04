init python:
  def generate_bot_warranty_seals(bot,table):
    for orifice,broken in table.items():
      if isinstance(broken,(list,tuple)):
        broken=randint(*broken)
      bot["warranty_seal_"+orifice]=broken<=0

init python:
  def break_warranty_seals(bot,orifices=("oral","vaginal","anal"),by_mc=False):
    for orifice in orifices:
      if orifice!="vaginal" or bot.gender!="male":
        if bot["warranty_seal_"+orifice]==True:
          if by_mc:
            mc["warranty_seals_broken_"+orifice]+=1
            bot["warranty_seal_"+orifice]="broken by mc"
          else:
            bot["warranty_seal_"+orifice]=False

label break_warranty_seals(bot,orifices=("oral","vaginal","anal"),by_mc=False):
  $orifice_n=0
  while orifice_n<len(orifices):
    $orifice=orifices[orifice_n]
    $orifice_n+=1
    if orifice!="vaginal" or bot.gender!="male":
      if bot["warranty_seal_"+orifice]==True:
        if by_mc:
          "{size=-8}You {bad}break{/} [bot.hisher] {mark}[orifice]{/} warranty seal.{/}"
          $mc["warranty_seals_broken_"+orifice]+=1
          $bot["warranty_seal_"+orifice]="broken by mc"
        else:
          "{size=-8}[bot.hisher!c] {mark}[orifice]{/} warranty seal is {bad}broken{/}.{/}"
          $bot["warranty_seal_"+orifice]=False
  return
