from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

DEBUG = False
SECRET_KEY = os.urandom(24)

app = Flask(__name__)
app.config.from_object(__name__)

# note that the environment variable `FLASK_SETTINGS` MUST contain the name of
# a config file containing at a minimum the `SQLALCHEMY_DATABASE_URI` and
# `SECRET_KEY` settings.
app.config.from_envvar('FLASK_SETTINGS')

# flask_sqlalchemy setup
db = SQLAlchemy(app)

# import views to mount them on the app. This could be refactored to use the
# Blueprints functionality.
from views import *
