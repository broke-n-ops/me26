init -2000 python:
    import io
    import os
    import zipfile

    zip_archives={}

    init_notes=[]

    def load_zip_archive(zip_fn,f):
        zip=zipfile.ZipFile(f)
        index={}
        zip_archives[zip_fn]={
            "filename": zip_fn,
            "archive": zip,
            "files": index,
        }
        for fn in zip.infolist():
            if not fn.filename.endswith("/"):
                index[fn.filename]="zip"

    def load_zip_archives():
        for zip_fn in os.listdir(renpy.config.savedir):
            if zip_fn.lower().endswith(".zip"):
                init_notes.append(("Found mod in storage folder:",zip_fn))
                zip_fn=os.path.join(renpy.config.savedir,zip_fn)
                load_zip_archive(zip_fn,open(zip_fn,"rb"))
        for zip_fn in renpy.list_files():
            if zip_fn.lower().endswith(".zip"):
                init_notes.append(("Found mod in game assets:",zip_fn))
                load_zip_archive(zip_fn,renpy.file(zip_fn))

    def zip_archive_scan_callback(add, seen):
        files=renpy.loader.game_files
        for zip_fn,zip in sorted(zip_archives.items()):
            for fn in zip["files"]:
                add(None,fn,files,seen)

    def zip_archive_file_callback(name):
        for zip_fn,zip in zip_archives.items():
            if name in zip["files"]:
                with zip["archive"].open(name,"r") as f:
                    rv=io.BytesIO(f.read())
                return rv
        return None

    load_zip_archives()
    if hasattr(renpy.loader, "scandirfiles_callbacks"):
        renpy.loader.scandirfiles_callbacks.insert(1, zip_archive_scan_callback)
    if hasattr(renpy.loader, "file_open_callbacks"):
        renpy.loader.file_open_callbacks.insert(2, zip_archive_file_callback)

    if hasattr(renpy.loader, "cleardirfiles"):
        renpy.loader.cleardirfiles()
    renpy.list_files()

init -1999 python:
    game_mods_sanitizers=[]

init -1900 python:
    game_mods=[]

    asset_packs=[]

    def check_asset_packs(img):
        for mod in reversed(game_mods):
            image_prefixes=mod.get("asset_packs") or []
            for prefix_from,prefix_to in reversed(sorted(image_prefixes)):
                if prefix_from and img.startswith(prefix_from):
                    return prefix_to+img[len(prefix_from):]
        return img
    
    def load_game_mods():
        rv=[]
        json_files=sorted((fn for fn in renpy.list_files() if fn.lower().endswith(".json")))
        for fn in json_files:
            s=renpy.file(fn).read().decode("utf8").replace(chr(0xFEFF),"").replace(chr(0xFFFE),"").rstrip().rstrip(",")
            s="\n".join([("" if sline.strip().startswith("//") else sline) for sline in s.splitlines()])
            try:
                mod=load_jsonplus(s,fn)
                if "mod_id" in mod:
                    mod["mod_filename"]=fn
                    mod["mod_loading_error"]=None
                    mod["mod_loading_notes"]=[]
                    for mod_sanitizer in game_mods_sanitizers:
                        mod_sanitizer(mod)
                    mod["mod_priority"]=mod.get("mod_priority",0)
                    rv.append(mod)
                    if log_loaded_mods():
                        print("Found game mod:",fn)
            except Exception as e:
                mod={}
                mod["mod_id"]="<failed to load>"
                mod["mod_filename"]=fn
                mod["mod_priority"]=9999
                mod["loading_notes"]=[]
                mod["mod_loading_error"]=str(e)
                rv.append(mod)
                if not renpy.emscripten:
                    print(e)
                    print("Game mod failed to load:",fn)
        rv=sorted(rv,key=lambda mod: (mod["mod_priority"],mod["mod_id"],mod["mod_filename"]))
        return rv
    
    game_mods=load_game_mods()
