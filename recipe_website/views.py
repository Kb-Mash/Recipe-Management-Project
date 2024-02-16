# routes and views
from flask import Blueprint

# define our Blueprint
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Hello</h1>"


