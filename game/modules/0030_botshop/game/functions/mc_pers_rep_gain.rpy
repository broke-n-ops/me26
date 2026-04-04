## 0.14 reduced the gains in 'bot trainer' and 'techbot trainer' which are too fast
## 0.14 increased randomness by reducing the lower limit - more spread always in lower direction

init python:
  pr_overall_scale=1.2         ## OVERALL scale factor for personal reputation gains; uses difficulty level
  pr_dealer_scale=1.0          ## scale factor for 'Bot Dealer role
  pr_trainer_scale=0.4         ## scale factor for 'Bot Trainer' role - v0.14 reduced: was 1.0
  pr_fighter_scale=1.0         ## scale factor for 'CombatBot Trainer' role
  pr_hacker_scale=1.0          ## scale factor for 'Hacker' role
  pr_mechanic_scale=1.0        ## scale factor for 'Mechanic' role
  pr_sexmachine_scale=1.0      ## scale factor for 'SexBot Trainer' role
  pr_tech_trainer_scale=0.4    ## scale factor for 'TechBot Trainer' role - v0.14 reduced: was 1.0

  
  def get_overall_scale():     ## function to get overall scale factor during calculations
    if game.difficulty==1:
      return 1.8
    elif game.difficulty==2:
      return 1.6
    elif game.difficulty==3:
      return 1.4
    else:
      return 1.2
      
  def calc_pr_rep_gain(rep_id,value):  ## receive reputation name and value text string in code, return integer gain or loss
    global pr_overall_scale
    global pr_dealer_scale
    global pr_trainer_scale
    global pr_fighter_scale
    global pr_hacker_scale
    global pr_mechanic_scale
    global pr_sexmachine_scale
    global pr_tech_trainer_scale    

#    print "rep_id: ",rep_id," value: ",value

## 0.14 reduced the low end number of the randomizer values about 1/3
    if value=="xs_g":
      temp0=randint(3,45)      ## was 5
    elif value=="s_g":
      temp0=randint(10,110)    ## was 15
    elif value=="m_g":
      temp0=randint(30,200)    ## was 50
    elif value=="l_g":
      temp0=randint(50,300)    ## was 75
    elif value=="xl_g":
      temp0=randint(60,400)    ## was 100
    elif value=="xs_l":
      temp0=randint(-45,-3)    ## was -5
    elif value=="s_l":
      temp0=randint(-110,-10)  ## was -15 
    elif value=="m_l":
      temp0=randint(-200,-30)  ## was -50
    elif value=="l_l":
      temp0=randint(-300,-50)  ## was -75
    elif value=="xl_l":
      temp0=randint(-400,-60)  ## was -100
    else:
      return 0                     ## invalid parameter received, return 0

#    print "Initial random number: ",temp0
    
    temp1=get_overall_scale()

#    print "overall scale: ",temp1
    
    if rep_id=="rep_mc_dealer":
      
##      print "dealer scale: ",pr_dealer_scale
##      print "total scale: ", pr_dealer_scale*temp1
##      print "Result to return: ",int(temp0*temp1*pr_dealer_scale)
      
      temp=temp0*temp1*pr_dealer_scale
    elif rep_id=="rep_mc_trainer":
      temp=temp0*temp1*pr_trainer_scale
    elif rep_id=="rep_mc_fighter":
      temp=temp0*temp1*pr_fighter_scale
    elif rep_id=="rep_mc_hacker":
      temp=temp0*temp1*pr_hacker_scale
    elif rep_id=="rep_mc_mechanic":
      temp=temp0*temp1*pr_mechanic_scale
    elif rep_id=="rep_mc_sexmachine":
      temp=temp0*temp1*pr_sexmachine_scale
    elif rep_id=="rep_mc_tech_trainer":
      temp=temp0*temp1*pr_tech_trainer_scale

##    print "rep_id: ",rep_id," value: ",value," return: ",temp

    return int(temp)
    
      
      