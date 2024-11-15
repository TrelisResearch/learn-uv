# Things you can do with uv

## Basic

1. Create a virtual environment
```
uv venv
```

2. Install dependencies
```
uv install -r requirements.txt
```
or 
```
uv pip install matplotlib numpy
uv pip freeze > requirements.txt
```

3. Run a command
> No need to activate the venv, uv will by default run in the environment set by VIRTUAL_ENV, then CONDA_PREFIX if present, and then .venv .
```
uv run draw-circle.py
```

## BONUS

1. Use a specific version of python when setting up the venv:
```
uv venv --python 3.12.4
```
uv will install it if not present on your system (btw, it will be a uv install, not system-wide).
