# setup Flask application

from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

# access environment variables
SECRET_KEY = os.environ.get('SECRET_KEY')
DB_NAME = os.environ.get('DB_NAME')

db = SQLAlchemy() # database object

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
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

    # login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader # decorator
    def load_user(id):
        return User.query.get(int(id)) # how to load a user from the database - id is a string, convert to int

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
