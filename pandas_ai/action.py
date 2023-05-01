from inspect import getmembers, isfunction
from typing import Any, Dict

from .factory import call_api
from .utils import import_code


class Action:
    def __init__(
        self,
        api: str,
        api_key: str = None,
    ):
        self.api = api
        self.api_key = api_key

        self._code = None
        self._module = None

    def create_and_run(
        self,
        prompt: str,
        params: Dict[str, Any] = {},
        library: str = "pandas",
        **kwargs,
    ):
        self._code = call_api(
            api=self.api,
            api_key=self.api_key,
            params=params,
            prompt=prompt,
            library=library,
            **kwargs,
        )
        print(self._code)
        self._module = import_code(self._code)

        functions_list = getmembers(self._module, isfunction)

        return functions_list[0][1](**kwargs)
