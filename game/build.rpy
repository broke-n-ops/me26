init -999 python:
    do_not_build_modules=[]

    def module_filter(module):
        return module not in do_not_build_modules

init 9999 python hide:
    build.classify("**~",None)
    build.classify("**.~*",None)
    build.classify("**/!todo!.txt",None)
    build.classify("**.bak",None)
    build.classify("**/.**",None)
    build.classify("**/#**",None)
    build.classify("**/thumbs.db",None)
    build.classify("**.bat",None)
    build.classify("**.cmd",None)
    build.classify("**.md",None)
    build.classify("game/saves/**",None)
    build.classify("game/cache/**",None)
    build.classify("tools/**.**",None)
    build.classify("wip/**.**",None)
    build.classify("doc/**.**",None)
    build.classify("**.py",None)
    build.classify("**/build_config.*",None)
    build.classify("**/local_config.*",None)

    archives={}

    for module_info in game_modules:
        module_mask="game/"+module_info["path"].strip("/")+"/**"
        if module_filter(module_info["id"]):
            module_archive=module_info.get("archive",build_default_archive)
        else:
            module_archive=None
        archives.setdefault(module_archive,[]).append(module_mask)

    for archive,file_masks in archives.items():
        if archive and archive!="archive":
            build.archive(archive)
        for file_mask in file_masks:
            build.classify(file_mask,archive)


    if build_default_archive not in archive:
        build.archive(build_default_archive)

    build.classify("**.rpyc",build_default_archive)
    build.classify("**.rpy",build_default_archive)
