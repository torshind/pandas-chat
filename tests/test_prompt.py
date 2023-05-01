import numpy as np
import pandas as pd

from pandas_ai.action import Action


def test_drop():
    action = Action(
        api="openai",
        api_key="sk-YOUR_KEY",
    )

    X = pd.DataFrame(np.random.rand(10, 3), columns=["col1", "col2", "col3"])
    prompt = "drop a column named column from a DataFrame named X"

    X = action.create_and_run(
        prompt=prompt,
        column="col2",
        X=X,
    )
    print(action)
    print(X)

    X = action.run(
        column="col1",
        X=X,
    )
    print(X)


def test_apply_sub():
    action = Action(
        api="openai",
        api_key="sk-YOUR_KEY",
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
    print(X)

    func = np.sqrt
    X = action.run(
        X1=X1,
        X2=X2,
        func=func,
    )
    print(X)
