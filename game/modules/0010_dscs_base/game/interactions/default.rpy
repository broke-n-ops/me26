init -100 python:
  class InteractionDefault(Interaction):
    id="default"
    def __init__(self):
      super(InteractionDefault,self).__init__()
      self.data={}
      self.data["content"]=[]
      self.data["choices"]=[]
      self.current_block=None
    def start_block(self,sides):
      self.end_block()
      sides=sides.split(" ")
      for n,side in enumerate(sides):
        if ":" in side:
          side,tmp,width=side.partition(":")
          width=eval(width)
        else:
          width=None
        sides[n]=(side,width)
      self.current_block=sides[0][0]
      block=("block",{})
      block[1]["sides"]=sides
      for side,width in sides:
        block[1][side]=[]
      self.data["content"].append(block)
    def end_block(self):
      self.current_block=None
    def set_block(self,block):
      self.current_block=block
    def add_choice(self,action=None,title=None,pos=None,**kwargs):
      if action=="<text>":
        choice=title
      else:
        choice={
          "title": title,
          "action": action,
          "pos": pos,
          }
        choice.update(kwargs)
      self.data["choices"].append(choice)
    def add_line(self,content):
      target=self.data["content"][-1][1][self.current_block] if self.current_block else self.data["content"]
      target.append(content)
    def extend_line(self,content):
      target=self.data["content"][-1][1][self.current_block] if self.current_block else self.data["content"]
      if target and isinstance(target[-1],str):
        target[-1]+=content
      else:
        target.append(content)
    def add_line(self,content):
      target=self.data["content"][-1][1][self.current_block] if self.current_block else self.data["content"]
      target.append(content)
    def extend_line(self,content):
      target=self.data["content"][-1][1][self.current_block] if self.current_block else self.data["content"]
      if target and isinstance(target[-1],str):
        target[-1]+=content
      else:
        target.append(content)
    def add_screen(self,screen_name,*args,**kwargs):
      self.add_line(("screen",screen_name,args,kwargs))
    def notify(self,notification):
      self.add_line(("notification",notification))
    def migrate_from(self,old_interaction):
      if hasattr(old_interaction,"data"):
        for x in old_interaction.data.get("content",[]):
          if isinstance(x,tuple):
            if x[0]=="notification":
              self.add_line(x)
            elif x[0]=="block":
              for side,width in x[1]["sides"]:
                for sx in x[1][side]:
                  if isinstance(sx,tuple) and sx[0]=="notification":
                    self.add_line(sx)
    def __setitem__(self,name,value):
      self.data[name]=value
    def __getitem__(self,name):
      return self.data.get(name)
    def finalize(self):
      return "interaction_default",(self.data,),{}
