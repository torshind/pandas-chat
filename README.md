# pandas-chat
pandas-chat is a python library that uses LLMs prompts to analyze and process pandas data in a conversational way.

# Installation
You can install pandas-chat using pip:
```
pip install pandas-chat
```

# LLMs supported
`api="openai"`

`api="hugchat"`
# Usage example
## Creation
### Input
```
import numpy as np
import pandas as pd
from pandas_chat.action import Action

action = Action(
    api="openai",
    api_key="API_KEY",
)

X1 = pd.DataFrame(np.random.rand(10, 3), columns=["col1", "col2", "col3"])
X2 = pd.DataFrame(np.random.rand(10, 3), columns=["col1", "col2", "col3"])
func = np.square
prompt = "apply function func to X1 and then subtract X2 from X1"

X = action.create_and_run(
    prompt=prompt,
    X1=X1,
    X2=X2,
    func=func,
)
print(action)
```
### Output
```
Reply with a python module using pandas; this module will have one function with arguments X1, X2, func; this function will perform what is described by the following instructions delimited by <<< and >>>; <<<apply function func to X1 and then subtract X2 from X1>>>;
verify that the reply has all the necessary imports, that it contains only valid python code, and that the keywords used are present in the official documentation of the libraries from which they came;
don't include any explanations in your reply, returning only python code.

import pandas as pd

def apply_func(X1, X2, func):
    result = X1.apply(func) - X2
    return result
```
## Run stored function
```
func = np.sqrt
X = action.run(
    X1=X1,
    X2=X2,
    func=func,
)
```
# Contributing
We welcome contributions from the community. Please see our contributing guidelines for more information.

# License
This project is licensed under the BSD 3-Clause License - see the LICENSE.md file for details.

# TODO
- [ ] use logging
- [ ] use env var for api key
- [ ] real tests
- [ ] add CI/CD
- [ ] add semantic release
- [ ] add other LLMs
