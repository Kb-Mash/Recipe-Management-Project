# setup Flask application

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy() # database object
DB_NAME = "database.db" # to-do - env variable

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'sdjdjks ksjksjd' # to-do - env variable
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # to-do - env variable
    db.init_app(app) # initialize database

    # register views for our application
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # script to check if database exists, if not, create it
    from .models import User, Recipe

    # create a database within Flask application context
    with app.app_context():
        create_database()

    return app

"""
older version - create_all(app=app)
version 2.0.0, Flask-SQLAlchemy deprecated the app argument
use current application context - current_app proxy object
"""
def create_database():
    with current_app.app_context():
        if not path.exists('recipe_website/' + DB_NAME):
            db.create_all()
            print('Created Database!')
