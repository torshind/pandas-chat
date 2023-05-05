from types import ModuleType


def import_code(code):
    module = ModuleType("model")
    exec(code, module.__dict__)
    return module
