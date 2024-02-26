from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255))
    recipe_description = db.Column(db.String(10000))
    recipe_ingredients = db.Column(db.String(10000))
    recipe_instructions = db.Column(db.String(10000))
    # recipe_image = db.Column(db.String(150)) to-do - add image
    date = db.Column(db.DateTime(timezone=True), default=db.func.now()) # default - automatically set the date and time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin): # UserMixin - flask login - current_user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    recipes = db.relationship('Recipe') # relationship between user and recipe, one to many

    def __str__(self):
        return self.username
