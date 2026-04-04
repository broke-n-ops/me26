init python:
  def preprocess_text(s):
    if isinstance(s,str):
      parts=s.split("[<")
      for n,part in enumerate(parts):
        sub,sep,rest=part.partition(">]")
        if sep:
          parts[n]=str(eval(sub))+rest
      s="".join(parts)
      s=renpy.substitute(s)
    return s

  def narrator(what,*args,**kwargs):
    if hasattr(act,"add_line"):
      what=preprocess_text(what)
      act.add_line(what)

  def header(what,*args,**kwargs):
    if isinstance(what,str):
      what="{#=cs_center}{#header}{=label_text}"+what+"{/}\n"
    return narrator(what,*args,**kwargs)

  def center(what,*args,**kwargs):
    if isinstance(what,str):
      what="{#=cs_center}"+what
    return narrator(what,*args,**kwargs)

  def left(what,*args,**kwargs):
    if isinstance(what,str):
      what="{#=cs_left}"+what
    return narrator(what,*args,**kwargs)

  def right(what,*args,**kwargs):
    if isinstance(what,str):
      what="{#=cs_right}"+what
    return narrator(what,*args,**kwargs)

  def extend(what,*args,**kwargs):
    if hasattr(act,"extend_line"):
      what=preprocess_text(what)
      act.extend_line(what)

  class choice(object):
    def __init__(self,action,title=None,**kwargs):
      super(choice,self).__init__()
      self.action=action
      self.title=title
      self.kwargs=dict(kwargs)
      ## quite dirty hack to check how choice was called
      if not self.kwargs.pop("prepare",False):
        if title or inspect.currentframe().f_back.f_back.f_back.f_back.f_code.co_name!="eval_who":
          self(title)
    def get_choice_info(self,what=""):
      action=self.action
      title=self.title or what
      action_label=(action if isinstance(action,str) else "<None>").partition(":")[0].strip("~<> ")
      action_info=getattr(store,"label_"+action_label+"_action_info",{})
      if callable(action_info):
        action_info_arg=self.kwargs.copy()
        action_info_arg.update({"action":action,"title":title,"action_label":action_label})
        if action_info.func_code.co_argcount:
          action_info=action_info(action_info_arg)
        elif action_info.func_code.co_flags&inspect.CO_VARKEYWORDS:
          action_info=action_info(**action_info_arg)
        else:
          action_info=action_info()
      if isinstance(action_info,dict):
        action_info=action_info.copy()
        if not title:
          title=action_info.get("title")
        action_info.pop("title",None)
        title=action_info.pop("force_title",title)
      if not title:
        title="<choice>"
      title=preprocess_text(title)
      rv=self.kwargs.copy()
      rv.update({
        "action": action,
        "title": title,
        })
      rv.update(action_info)
      return rv
    def __call__(self,what,*args,**kwargs):
      if hasattr(act,"add_choice"):
        act.add_choice(**self.get_choice_info(what))

  def choice_info(action,title=None,**kwargs):
    kwargs["prepare"]=True
    return choice(action,title=title,**kwargs).get_choice_info(title)
