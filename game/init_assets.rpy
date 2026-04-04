default persistent.preload_assets = True

init -1900 python:
  preload_assets_condition = "False if renpy.emscripten else persistent.preload_assets"

init -1800 python:
  config.audio_directory = None

  def scan_audio_files():
    preload_assets = eval(preload_assets_condition)
    for file_path in renpy.list_files():
      if file_path.lower().endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus", ".flac")):
        parts = file_path.split("/")
        if "assets" in parts:
          parts = parts[parts.index("assets") + 1:]
        if parts and parts[0] in ["audio"]:
          parts.pop(0)
          while parts and parts[0] in ["locations"]:
            parts.pop(0)
          if parts:
            parts[-1] = parts[-1].rsplit(".", 1)[0]
            name = " ".join(parts)
            if preload_assets:
              with renpy.file(file_path) as file_obj:
                audio_data = AudioData(bytes(file_obj.read()), file_path)
              audio.__dict__[name] = audio_data
            else:
              audio.__dict__[name] = file_path

  scan_audio_files()

init -1800 python:
  config.images_directory = None

  registered_images = {}

  def scan_image_files():
    preload_assets = eval(preload_assets_condition)
    image_map = {}
    for file_path in renpy.list_files():
      if file_path.lower().endswith((".png", ".jpg", ".webp")):
        parts = file_path.split("/")
        if "assets" in parts:
          parts = parts[parts.index("assets") + 1:]
        while parts and parts[0] in ["images", "movies", "characters", "locations"]:
          parts.pop(0)
        if parts:
          parts[-1] = parts[-1].rsplit(".", 1)[0]
          name = " ".join(parts)
          image_map[name] = file_path
    for name, file_path in image_map.items():
      if preload_assets:
        with renpy.file(file_path) as file_obj:
          image_data = im.Data(bytes(file_obj.read()), file_path)
        renpy.image(name, image_data)
      else:
        renpy.image(name, file_path)
    return image_map

  registered_images = scan_image_files()

init -1700 python:
  config.movie_mixer = "voice"

  renpy.music.register_channel("movie_fullscreen", mixer="sfx", loop=True, stop_on_mute=False, buffer_queue=False, movie=True, framedrop=True)

  def scan_movie_files():
    movie_map = {}
    for file_path in renpy.list_files():
      if file_path.lower().endswith((".webm", ".mp4", ".avi", ".mkv")):
        parts = file_path.split("/")
        if "assets" in parts:
          parts = parts[parts.index("assets") + 1:]
        while parts and parts[0] in ["images", "movies", "characters", "locations"]:
          parts.pop(0)
        if parts:
          parts[-1] = parts[-1].rsplit(".", 1)[0]
          name = " ".join(parts)
          movie_map[name] = file_path
    for name, file_path in movie_map.items():
      preview_image = name + "_preview"
      if renpy.has_image(preview_image, True):
        renpy.image(name, Movie(play=file_path, start_image=preview_image, image=preview_image))
        renpy.image(name + "#fullscreen", Movie(play=file_path, start_image=preview_image, image=preview_image, channel="movie_fullscreen"))
      else:
        renpy.image(name, Movie(play=file_path))
        renpy.image(name + "#fullscreen", Movie(play=file_path, channel="movie_fullscreen"))
    return movie_map

  registered_images.update(scan_movie_files())

init -1695 python:
  def scan_orphan_preview_images():
    images=set(registered_images)
    for name in images:
      if name.lower().endswith("_preview"):
        main=name[:-8]
        if main not in images:
          renpy.image(main,name)

  scan_orphan_preview_images()
