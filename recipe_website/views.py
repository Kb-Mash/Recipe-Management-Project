# routes and views
from flask import Blueprint, render_template
# define our Blueprint
views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')
