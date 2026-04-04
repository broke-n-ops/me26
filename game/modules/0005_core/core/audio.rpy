init -100 python:
  class AudioChannelPrefix(object):
    def __init__(self,prefix=""):
      super(AudioChannelPrefix,self).__init__()
      if prefix and prefix[-1]!=" ":
        prefix+=" "
      self.prefix=prefix
    def __add__(self,other):
      if isinstance(other,str):
        rv=getattr(audio,self.prefix+other,None)
        if not rv:
          rv=getattr(audio,other,None)
        if rv:
          return rv
      return other

  def prepare_audio_channels():
    for channel_id,channel in renpy.audio.audio.channels.items():
      prefix=channel_id if isinstance(channel_id,str) else "sound"
      channel.file_prefix=AudioChannelPrefix(prefix)
    config.auto_channels={id:(mixer,AudioChannelPrefix(prefix or "sound"),suffix) for id,(mixer,prefix,suffix) in config.auto_channels.items()}

  prepare_audio_channels()

  def has_audio(name):
    if isinstance(name,str):
      return getattr(audio,name,False)
    return False
