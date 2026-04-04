init -999 python:
  class GameObject(object):
    object_type="object"
    id="object"
    def __init__(self,*args,**kwargs):
      super(GameObject,self).__init__()
    def __eq__(self,other):
      if self is other:
        return True
      elif self.id==other:
        return True
      elif isinstance(other,GameObject) and self.object_type==other.object_type and self.id==other.id:
        return True
      return False
    def __ne__(self,other):
      return not self.__eq__(other)
