from inspect import getmembers, isfunction
from types import ModuleType

import openai


def import_code(code):
    module = ModuleType("model")
    exec(code, module.__dict__)
    return module


openai.api_key = "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"

prompt = "write a python module with a function that converts an input string to uppercase"

reply = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    max_tokens=64,
    temperature=0.5,
)

print(reply)

module = import_code(reply["choices"][0]["text"])
functions_list = getmembers(module, isfunction)
print(functions_list[0][1]("pippo pluto e paperino"))
