default persistent.log_loaded_mods=False
default persistent.log_modded_entries=False

init -9999 python:

    import _ast

    jsonplus_safe_names={
        "None": None,
        "True": True,
        "False": False,
        "none": None,
        "null": None,
        "nil": None,
        "true": True,
        "false": False,
        "yes": True,
        "no": False,
    }

    def load_jsonplus_convert(node):
        if isinstance(node, _ast.Constant):
            if isinstance(node.value, (str, int, float, bool, type(None))):
                return node.value
        elif isinstance(node, _ast.Tuple):
            return tuple(map(load_jsonplus_convert, node.elts))
        elif isinstance(node, _ast.List):
            return list(map(load_jsonplus_convert, node.elts))
        elif isinstance(node, _ast.Dict):
            return {
                load_jsonplus_convert(key): load_jsonplus_convert(value)
                for key, value in zip(node.keys, node.values)
            }
        elif isinstance(node, _ast.Name):
            if node.id in jsonplus_safe_names:
                return jsonplus_safe_names[node.id]
        elif isinstance(node, _ast.UnaryOp) and isinstance(node.op, (_ast.UAdd, _ast.USub)):
            operand = load_jsonplus_convert(node.operand)
            if isinstance(operand, (int, float)):
                return operand if isinstance(node.op, _ast.UAdd) else -operand
        raise ValueError("malformed jsonplus string")

    jsonplus_convert_fn=load_jsonplus_convert

    def load_jsonplus(json,fn="<string>"):
        json=compile(json,fn,"eval",_ast.PyCF_ONLY_AST).body
        rv=load_jsonplus_convert(json)
        return rv

    def log_loaded_mods():
        return persistent.log_loaded_mods and not renpy.emscripten

    def log_modded_entries():
        return persistent.log_modded_entries and not renpy.emscripten

    game_modules=[]

    def find_game_modules():
        rv=[]
        json_files=sorted((fn for fn in renpy.list_files() if fn.lower().endswith("module.json")))
        for fn in json_files:
            s=renpy.file(fn).read().decode("utf8").replace(chr(0xFEFF),"").replace(chr(0xFFFE),"")
            module_info=load_jsonplus(s,fn)
            module_info["json_path"]=fn
            rv.append(module_info)
        return rv

    def load_game_modules():
        for module_info in game_modules:
            module_id=module_info["id"]
            module_path=module_info["path"].rstrip("/")
            renpy.config.search_prefixes.insert(0,module_path+"/")
            renpy.config.search_prefixes.insert(0,module_path+"/assets/")
            if log_loaded_mods():
                print("Found module:",module_id)

    game_modules=find_game_modules()
    load_game_modules()

python early:
    renpy.parser.word_regexp=r"[a-zA-Z_\u00a0-\ufffd][$@0-9a-zA-Z_\u00a0-\ufffd]*"

init python:
    class ModuleLabelFinder(dict):
        def get(self,key,default=None):
            if not isinstance(key,str):
                return super(ModuleLabelFinder,self).get(key,default)
            rv=super(ModuleLabelFinder,self).get(key)
            if rv is None:
                for module_info in reversed(game_modules):
                    rv=module_info["id"]+"@"+key
                    if rv in renpy.game.script.namemap:
                        break
                    rv=None
            if rv is None:
                rv=default
            return rv

    config.label_overrides=ModuleLabelFinder()
