## 0.9.n - when loading a game the 'rep_syndicate' may need to be updated
## called from 'roaming_home' and flag used to avoid re-calling it again
## once a saved game has been adjusted once the flag will be saved with the game so the function is not used again

init python:
  sr24_checked_syndicate_rep=0

label check_syndicate_reputation:
  $sr24_checked_syndicate_rep=1                                  ## once it's been called you don't need to do it again
  python:
    rep_syndicate_found=0
    for stat in mc.stats:
      if stat=="rep_syndicate":
        rep_syndicate_found=1
## rep_syndicate missing, fix it based upon 'Framed!' payments
  if rep_syndicate_found==0:                                     ## rep_syndicate doesn't exist, must have opened a saved game from previous version
    $notify.disable()
    $mc.give_xp("rep_syndicate",1)                               ## give 1 xp to create the stat, if debt fully paid this is sufficient
    $notify.enable()
    if sr_game_difficulty=="- Easy" and mc.debt==250000:         ## no payments made: Easy
      $mc.rep_syndicate.level=-3
      $mc.rep_syndicate.xp=1
    elif sr_game_difficulty=="- Normal" and mc.debt==500000:     ## no payments made: Normal
      $mc.rep_syndicate.level=-3
      $mc.rep_syndicate.xp=1
    elif sr_game_difficulty=="- Hard" and mc.debt==800000:       ## no payments made: Hard
      $mc.rep_syndicate.level=-3
      $mc.rep_syndicate.xp=1
    elif sr_game_difficulty=="- Hardcore" and mc.debt==1000000:  ## no payments made: Hardcore
      $mc.rep_syndicate.level=-3
      $mc.rep_syndicate.xp=1
    elif mc.debt>0:                                                          ## some payments made
## 0.10.n for new list variables, see intro - 1 new line
      $temp=((mc.debt+0.0)/(fr_initial_debt[game.difficulty]+0.0))*-5998.65  ## amount of xp the payments made corresponds to, EMPIRICALLY DETERMINED AND ADDING 0.0 TO FORCE NON-INTEGER ARITHMATIC
      $mc_cumulative_rep_xp=6001-temp                            ## populate variable created in 0.9.n and used in 'exiled_engineer.rpy'
      $notify.disable()
      $mc.give_xp("rep_syndicate",temp)                          ## subtract xp to scale proportional to debt paid
      $notify.enable()
  return
