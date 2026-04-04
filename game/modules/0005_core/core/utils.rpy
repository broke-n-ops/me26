init -950 python:
  import sys
  import math
  import pygame
  import random
  import inspect
  import fnmatch

  class NotFoundCls(object):
    def __nonzero__(self):
      return False
    def __len__(self):
      return 0
  NotFound=NotFoundCls()

  class classproperty(object):
    def __init__(self, fget):
      self.fget=fget
    def __get__(self, owner, cls):
      return self.fget(cls)

  def force_property(cls,f_name):
    f=getattr(cls,f_name,None)
    if callable(f):
      f=getattr(f,"im_func",getattr(f,"fget",f))
      setattr(cls,f_name,property(f))

  def force_classproperty(cls,f_name):
    f=getattr(cls,f_name,None)
    if callable(f):
      f=getattr(f,"im_func",getattr(f,"fget",f))
      setattr(cls,f_name,classproperty(f))

  def force_method(cls,f_name):
    f=getattr(cls,f_name,None)
    if callable(f):
      f=getattr(f,"im_func",getattr(f,"fget",f))
      setattr(cls,f_name,f)

  def force_classmethod(cls,f_name):
    f=getattr(cls,f_name,None)
    if callable(f):
      f=getattr(f,"im_func",getattr(f,"fget",f))
      setattr(cls,f_name,classmethod(f))

  def force_staticmethod(cls,f_name):
    f=getattr(cls,f_name,None)
    if callable(f):
      f=getattr(f,"im_func",getattr(f,"fget",f))
      setattr(cls,f_name,staticmethod(f))

  def set_default_property(cls,name):
    default_value=getattr(cls,name)
    if isinstance(default_value,property):
      default_value=getattr(cls,"_"+name)
    setattr(cls,"_"+name,default_value)
    if isinstance(default_value,(list,tuple)):
      setattr(cls,"default_"+name,default_value[:])
    elif isinstance(default_value,dict):
      setattr(cls,"default_"+name,default_value.copy())
    else:
      setattr(cls,"default_"+name,default_value)
    getter=getattr(cls,"get_"+name,None)
    if not getter:
      getter=lambda self,name="_"+name: getattr(self,name)
    setter=getattr(cls,"set_"+name,None)
    if not setter:
      setter=lambda self,value,name="_"+name: setattr(self,name,value)
    setattr(cls,name,property(getter,setter))

  def set_gameobject_property(cls,name,category):
    default_value=getattr(cls,name)
    if isinstance(default_value,property):
      default_value=getattr(cls,"_"+name)
    setattr(cls,"_"+name,default_value)
    if isinstance(default_value,(list,tuple)):
      setattr(cls,"default_"+name,default_value[:])
    elif isinstance(default_value,dict):
      setattr(cls,"default_"+name,default_value.copy())
    else:
      setattr(cls,"default_"+name,default_value)
    find_fn=eval("find_"+category)
    getter=lambda self,name="_"+name,find_fn=find_fn: find_fn(getattr(self,name))
    setter=lambda self,value,name="_"+name,find_fn=find_fn: setattr(self,name,getattr(find_fn(value),"id",None))
    setattr(cls,name,property(getter,setter))

  def randwchoice(items):
    total_w=int(sum(w for item,w in items)*1000)
    if total_w<=0:
      return items[0][0] if items else None
    roll=renpy.random.randint(0,total_w-1)
    for item,w in items:
      roll-=int(w*1000)
      if roll<0:
        return item
  renpy.random.wchoice=randwchoice

  def randint(a,b):
    if a>b:
      a,b=b,a
    return renpy.random.randint(int(a),int(b))

  def randchoice(*args,**kwargs):
    return renpy.random.choice(*args,**kwargs)

  def label_call(label,*args,**kwargs):
    return (label,args,kwargs)
