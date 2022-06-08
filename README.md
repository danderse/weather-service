# How to Run

NOTE: Steps 3-5 should be run from this directory

## 1. Ensure python 3 is installed

  The following assume that "python" references python3 via an alias, path update, pyenv, or similar

## 2. Ensure the correct version of pip (python package installer) is in use

  ```python -m ensurepip --upgrade```

## 3. Create a virtual environment

  ```python -m venv .```

## 4. Install the dependencies

  ```pip install -r requirements.txt```

## 5. Run the server

  ```
  export FLASK_APP=weather
  flask run
  ```

## 6. Hit the endpoint

  ```curl localhost:5000/current-weather/<lat>/<lon>```