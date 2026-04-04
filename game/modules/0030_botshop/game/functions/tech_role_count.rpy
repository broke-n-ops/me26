## count tech roles and reduce effectiveness of senior and master techie when multiple techie assignments
## techie=1, senior techie=2, master techie=4, 8=shopkeeper (techie)
## 0=none,1=techie,2=senior,3=techie+senior,4=master,5=techie+master,6=senior+master,7=techie+senior+master
## 8=shopkeeper, 9=shopkeeper+techie, 10=senior+shopkeeper, 11=senior+shopkeeper+techie
## 12=master+shopkeeper, 13=master+shopkeeper+techie, 14=master+senior+shopkeeper
## techie or senior or master: (0,1,2,4)= 0 
## techie and (senior or master): (3,5) = 2
## senior and master: (6) = 3
## techie and senior and master: (7) = 5

init python:
  def fn_tech_roles(this_bot):
    role_count=0
    roles=sorted(this_bot.roles[:],key=lambda role:(role.list_priority,role.name.lower()))
    roles=[role for role in roles if not role.hidden]
    if roles:
        
##      print "bot: :",this_bot
  
      while roles:
        role=roles.pop(0)

##        print "role.id: ",role.id

        if role.id=="techie" and not this_bot.tech_just_assigned:
          role_count+=1
        elif role.id=="senior_techie" and not this_bot.st_just_assigned:
          role_count+=2
        elif role.id=="master_techie" and not this_bot.mt_just_assigned:
          role_count+=4
        elif role.id=="shopkeeper" and not this_bot.shpkpr_just_assigned:
          role_count+=8

##      print "role_count: ",role_count

    if role_count==7 or role_count==14:                                       ## senior AND master AND (techie OR shopkeeper)
      skill_reduction=5
    elif role_count==6 or role_count== 11 or role_count==13:                  ## (senior and master) OR (shopkeeper AND techie AND (master OR senior))
      skill_reduction=3
    elif role_count==3 or role_count==5 or role_count==10 or role_count==12:  ## (senior OR master) AND (techie OR shopkeeper)
      skill_reduction=2
    else:
      skill_reduction=0

##    print "skill_reduction: ",skill_reduction

    return skill_reduction