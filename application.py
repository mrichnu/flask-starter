from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import hello_page 
import os

DEBUG = os.environ.get('FLASK_DEBUG') == 'True'

def create_app(database_uri, debug=False):
    app = Flask(__name__)
    app.config.update(
        DEBUG=debug,
        SECRET_KEY=os.environ.get('FLASK_SECRET_KEY', os.urandom(24)),
        SQLALCHEMY_DATABASE_URI = database_uri
    )
    app.register_blueprint(hello_page)
    return app

def get_database_uri():
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')
    return 'postgresql://{0}:{1}@{2}/{3}'.format(
        db_username, db_password, db_host, db_name)

if __name__ == '__main__':
    app = create_app(get_database_uri(), DEBUG)
    app.run()
