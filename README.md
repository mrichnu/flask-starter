# Flask starter app

This repository contains the skeleton for a flask app with sqlalchemy
integration, flask-script example commands, and unit tests.

To start the app in local debug mode, first create a file to hold your local
settings, named e.g. `settings.cfg` containing at a minimum the `SECRET_KEY`
and `SQLALCHEMY_DATABASE_URI` settings. For example:
```
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@host/database_name'
SECRET_KEY = 'secret'
```

Then you can run the app like this:
```sh
$ FLASK_APP=application.py FLASK_SETTINGS=settings.cfg ./manage.py runserver
```

Or, alternatively, export the `FLASK_SETTINGS` and `FLASK_APP` environment
variables:
```sh
$ export FLASK_SETTINGS=settings.cfg
$ export FLASK_APP=application.py
$ ./manage.py runserver
```

For convenience, I create a `setenv.sh` file that exports the appropriate
values, and source it when I activate the virtualenv.

## Setting up the database

An `initdb` command is included to set up the database automatically:
```sh
$ FLASK_SETTINGS=settings.cfg ./manage.py initdb
```

A `resetdb` command is included as well to drop and recreate the database (use
with caution, obviously!)
```sh
$ FLASK_SETTINGS=settings.cfg ./manage.py resetdb
```

## Running the tests

Unit tests are in the `tests.py` module, and can be run like so:
```sh
$ FLASK_SETTINGS=testingsettings.cfg python test.py
```

Obviously, the file `testingsettings.cfg` must exist and have appropriate
settings for the `DEBUG` and `SQLALCHEMY_DATABASE_URI` configuration keys. It's
important to use a different `SQLALCHEMY_DATABASE_URI` for testing than for
your local development or the production database because the testing database
will be repeatedly dropped and recreated (losing all data in the database)
whenever the test suite is run.

## Adding script commands

The [Flask-Script](https://flask-script.readthedocs.io/en/latest/) package is
included and the `manage.py` module is a convenient place to add commands that
need to be run manually (or via cron) that have access to the database models
and flask app context. Just add a function with the `@manager.command`
decorator and then your function will be available as a command. For example,
if the following function were created in `manage.py`:
```python
@manager.command
def hello():
    print("Hello!")
```

You could run it from the shell with this incantation:
```sh
$ FLASK_SETTINGS=settings.cfg ./manage.py hello
Hello!
```

Note that the `runserver` and `shell` commands are available, in addition to
any commands in `manage.py`.
