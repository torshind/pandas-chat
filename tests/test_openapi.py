import numpy as np
import pandas as pd

from pandas_chat.action import Action


def test_drop():
    action = Action(
        api="openai",
        api_key="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",
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
        api_key="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",
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


def test_sw():
    action = Action(
        api="hugchat",
    )

    df = pd.DataFrame(
        {
            "title": [
                "Phantom Menace",
                "Attack of the clones",
                "Revenge of the Sith",
                "New hope",
                "Empire strikes again",
                "Return of the Jedi",
                "Force awakens",
                "Last Jedi",
                "Rise of Skywalker",
            ],
            "vote": [
                7.1,
                8.2,
                10,
                9.4,
                10,
                8.9,
                5,
                0,
                3,
            ],
            "year": [
                1999,
                2002,
                2005,
                1977,
                1980,
                1983,
                2015,
                2017,
                2019,
            ],
        }
    )
    prompt = "return the value of the 'title' column with the highest value in the 'vote' column"

    X = action.create_and_run(
        prompt=prompt,
        df=df,
    )
    print(action)
    print(X)

    X = action.run(
        df=df,
    )
    print(X)
