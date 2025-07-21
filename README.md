# Wine Prediction Model

This application provides a simple Class Prediction model trained using the
`RandomForestClassifier` from scikit-learn and the `load_wine` dataset offered from the same library.

The app is exposed using `FastAPI`, with a single GET route available in the builtin `/docs`

- GET /predict_wine

## To train the model

I removed scikitlearn from requirements to get a lightweight build
1. pipenv install scikit-learn


## How to work with Python virtual environments and launch FastAPI server 

In the root folder:

1. `pipenv --venv` ***to understand wich venv are you in***
2. `export PIPENV_VENV_IN_PROJECT=1` ***to be sure that you will create a new venv in the project scope***
3. `pipenv install` ***to install the dependencies***
4. in vscode Cmd+Shif+P -> Python: select interpreter -> select the new venv
5. in the terminal, be sure that you see the venv name before the root folder name (should be the same always)
6. `fastapi dev main.py` ***To launch the server***