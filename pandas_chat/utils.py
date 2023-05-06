import re

from types import ModuleType


def import_code(code):
    module = ModuleType("model")
    exec(code, module.__dict__)
    return module


def extract_code(text):
    code = re.search(r'```(?:python)?(.*?)```', text, re.DOTALL)
    if code:
        code = code.group(1)
        try:
            compile(code, "<string>", "exec")
            return code.strip()
        except Exception as e:
            return str(e)
    else:
        return text
