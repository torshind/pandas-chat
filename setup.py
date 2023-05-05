import sys

from setuptools import find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

try:
    from skbuild import setup
except ImportError:
    print("scikit-build is required to build from source.", file=sys.stderr)
    print("Please run:", file=sys.stderr)
    print("", file=sys.stderr)
    print("  python -m pip install scikit-build")
    sys.exit(1)

setup(
    name="pandas-chat",
    version="0.0.2",
    description="pandas-ai is a python library that uses ChatGPT prompts \
        to analyze and process pandas data in a conversational way.",
    long_description=long_description,
    author="torshind",
    license="BSD 3-Clause",
    packages=find_packages(exclude=["tests.*", "tests"]),
    url="https://github.com/torshind/pandas-ai",
    keywords="pandas, chatgpt",
    install_requires=[
        "openai",
    ],
)
