# AFP workshop on Functional Programming in Python

## Overview

The code in this repository is supplementary material and examples for the
talk "Functional Programming in Python" (keynote file available in repo).
It illustrates many of the concepts mentioned in the talk

## Dependencies

- virtualenv (this project uses virtualenv)

## Setup

1. Setup virtualenv environment (I store the environment in `venv` here
but you can set it up in any directory you want):
```
virtualenv --python=python3 venv
```

2. activate the environment (the following commands work on Linux and Mac OS X,
but will not work on Windows)

```
source venv/bin/activate
```

3. use `pip` to install the third-party libraries from requirements.txt

```
pip install -r requirements.txt
```

