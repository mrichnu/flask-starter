# Changing Tides Database App

This repository contains a web app (written with Flask) to manage a database of
materials related to carceral reform in the United States.

To start the app in local debug mode, first create a file to hold your local
settings, named e.g. `settings.cfg` containing at a minimum the `SECRET_KEY`
and `SQLALCHEMY_DATABASE_URI` settings. For example:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@host/database_name'
    SECRET_KEY = 'secret'

Then you can run the app like this:

    FLASK_SETTINGS=settings.cfg python application.py

Or, alternatively, export the `FLASK_SETTINGS` environment variable once:

    export FLASK_SETTINGS=settings.cfg
    python application.py


## Setting up the database

An `initdb` command is included to set up the database automatically:

    FLASK_APP=application.py FLASK_SETTINGS=settings.cfg flask initdb

A `resetdb` command is included as well to drop and recreate the database (use
with caution, obviously!)

    FLASK_APP=application.py FLASK_SETTINGS=settings.cfg flask resetdb
