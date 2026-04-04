## function to make sure male bots will be scavenged at the dump at least 15% of the time: code courtesy of Mr_Shaky
## called "on demand" at the beginning of the 'dump_site_scavenge_bot' function in 'dump_site_scavenge_events.rpy'

label adjust_male_bot_weights():
  python:
      
##    print "running the adjust male bot weight function"
    
    min_ratio=float(0.315)  ## this ratio results in 23.95% male bots scavenged, vanilla game is 24.08% male bots
    w_m_bots = sum([modded_bot_model_classes[bot].list_target_tag_chances.get("all", 0) for bot in modded_bot_model_classes if modded_bot_model_classes[bot].gender=="male"])
    w_f_bots = sum([modded_bot_model_classes[bot].list_target_tag_chances.get("all", 0) for bot in modded_bot_model_classes if modded_bot_model_classes[bot].gender=="female"])
    current_ratio=(w_m_bots+0.01)/(w_f_bots+0.01)   ## the "+0.01" is used to force float instead of int

##    print "w_m_bots: ",w_m_bots,"  w_f_bots: ",w_f_bots,"  current_ratio: ",current_ratio,"  min_ratio: ",min_ratio
##    print "if current_ratio < min_ratio then adjustments are made"

    if current_ratio<min_ratio:
      adjust_div = current_ratio/min_ratio          ## both values are float so no need for addition of a small amount

##      print "adjust_div: ",adjust_div

      for bot in modded_bot_model_classes:

        if modded_bot_model_classes[bot].gender == "male" and modded_bot_model_classes[bot].list_target_tag_chances.get("all", False):

##          print "original value: ",modded_bot_model_classes[bot].list_target_tag_chances["all"]

          modded_bot_model_classes[bot].list_target_tag_chances["all"] /= adjust_div

##          print "revised value: ",modded_bot_model_classes[bot].list_target_tag_chances["all"]

  return