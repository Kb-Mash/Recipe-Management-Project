# routes and views
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Recipe
from . import db

# define our Blueprint
views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html', user=current_user)

@views.route('/dashboard')
@login_required
def dashboard():
    user_recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', recipes=user_recipes, user=current_user)

@views.route('/add_recipe', methods=['POST', 'GET'])
@login_required
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']

        # Create a new recipe instance
        recipe = Recipe(
            recipe_name=title,
            recipe_description=description,
            recipe_ingredients=ingredients,
            recipe_instructions=instructions,
            user_id=current_user.id
        )
        # Save the recipe to the database
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('views.dashboard'))

    return render_template('add_recipe.html', user=current_user)
