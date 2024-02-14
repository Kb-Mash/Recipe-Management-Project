""" module for the Flask application setup and routes """

from flask import Flask, render_template
""" To-Do - Database from flask_sqlalchemy import SQLAlchemy """

app = Flask(__name__)

"""
To-Do - Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
"""

@app.route('/')
def index():
    return render_template('index.html')
