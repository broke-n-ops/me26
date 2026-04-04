init python:
  text_replace_table=[
#    ("{~","{image="),
    ("{bad}","{color=#F00}"),
    ("{good}","{color=#0F0}"),
    ("{info}","{color=#AAA}"),
    ("{hint}","{color=#666}"),
    ("{say}","{color=#FE8}"),
#    ("{mcsay}","{color=#6AF}"),  ## Radnor commented this out and replaced it with the line below to dim the color
#    ("{mcsay}","{color=#6BD}"),  ## Both this and the original above are too dim for the background images in SR24
    ("{mcsay}","{color=#0BF}"),   ## SR24 0.11.n revised to look better in SR24
    ("{mark}","{color=#6D8}"),
    ("{_}","\xA0"),                                             ## nbsp
    ("{ }","\xA0"),                                             ## nbsp
    ("{*}","\u2022"),                                           ## bullet
  ]

  def patched_text_set_text(self,text,*args,**kwargs):
    rv=self.set_text.original(self,text,*args,**kwargs)
    for sn,s in enumerate(self.text):
      if isinstance(s,str):
        ## process generic tags/replacements
        for rfrom,rto in text_replace_table:
          s=s.replace(rfrom,rto)
        self.text[sn]=s
    return rv

  if not hasattr(Text.set_text,"original"):
    patched_text_set_text.original=Text.set_text
    Text.set_text=patched_text_set_text
