##  function that counts the number of identical parts
##    receives slot id, part id, integrity value, defect count
##    returns count of items that match

init python:
  def fn_part_count(slot,part,integrity,defects):
##    print "running fn_part_count"
    item_count=0
    for n,item in enumerate(workshop.inventory):
##      print slot,item.slot
##      print part,item.id
##      print integrity,item.integrity
##      print defects,item.defects
      if item.slot==slot:
##        print "slot match"
        if item.id==part:
##          print "part match"
          if item.integrity==integrity:
##            print "integrity match"
            if item.defects==defects:
##              print "defects match"
              item_count=item_count+1
##              print "item count: ",item_count
    return item_count