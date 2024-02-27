# routes and views
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Recipe
from . import db
import json

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

@views.route('/update_recipe/<int:id>', methods=['POST', 'GET'])
@login_required
def update_recipe(id):
    """ sending request as a form """
    recipe = Recipe.query.get_or_404(id)

    if request.method == 'POST':
        recipe.recipe_name = request.form['title']
        recipe.recipe_description = request.form['description']
        recipe.recipe_ingredients = request.form['ingredients']
        recipe.recipe_instructions = request.form['instructions']

        db.session.commit()
        flash('Recipe updated', 'success')
        return redirect(url_for('views.dashboard'))

    return render_template('update_recipe.html', recipe=recipe, user=current_user)

@views.route('/delete-recipe/<int:id>', methods=['POST', 'GET'])
@login_required
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(recipe)
        db.session.commit()
        flash('Recipe deleted successfully!', 'success')
        return redirect(url_for('views.dashboard'))
    return render_template('delete_recipe.html', recipe=recipe, user=current_user)
