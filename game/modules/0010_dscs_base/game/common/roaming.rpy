label roaming:
  if game_call_stack!=["roaming"]:
    $game_call_stack=[]
    return "roaming"
  call expression "roaming_"+game.location.id
  return _return
 