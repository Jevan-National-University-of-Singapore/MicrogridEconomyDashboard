# ESP 4902 (Final Year Project)
This repo contains all the material for the microgrid dashboard

# Dependencies
_Currently only have 2 dependecies so have no requirements.txt_

- pyside6 (`pip install pyside6`)
- numpy-financial(`pip install numpy-financial`)

## Architecture
Database: python SQLite
Backend (model): python (pyside)
Frontend (view): pyside QML
Frontend-backend-interface (control): pyside QML (javascript)

## Stack
entry: `main.py`
`main.py` initialises the backend codes, database and the GUI thread.


## Source Tree
`src` contains all the backends and logic
`qml` contains all the .qml file which dictates the UI of the program

entry point is `main.py` which can be found in src.

## TO DO
1. Move hourly solar charging and hourly charging demand into the technical section under their respecitve sections
2. Perhaps make the model as a single year first then for the five year anaylsis create 5 of it.

<!-- diagram for software architecture and features -->
