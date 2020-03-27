#!/bin/bash

source venv/bin/activate

export FLASK_ENV=development
export FLASK_APP=main.py
export FLASK_DEBUG=1
export GOOGLE_APPLICATION_CREDENTIALS='/home/sara/Descargas/flask-notes-firebase-adminsdk-2bqc5-3986d78923.json'

flask run
