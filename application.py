from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DEBUG = False

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

def init_db():
    import models
    from sqlalchemy_utils.functions import database_exists, create_database
    if not database_exists(db.engine.url):
        create_database(db.engine.url)
        db.create_all()

def reset_db():
    db.drop_all()
    init_db()

@app.cli.command('initdb')
def init_db_command():
    init_db()
    print("Database initialized.")

@app.cli.command('resetdb')
def reset_db_command():
    reset_db()
    print("Database dropped and reinitialized.")

if __name__ == '__main__':
    app.run()
