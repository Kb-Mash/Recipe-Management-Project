# login - authorization
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET']) # methods - allow user to send data to the server (POST) and to receive data from the server (GET)
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password1 = request.form['password1']
        password2 = request.form['password2']

        # message flashing
        if len(email) < 3:
            flash("Email must be greater than 3 characters", category="error")
        elif len(username) < 2:
            flash("Username must be greater than 1 character", category="error")
        elif len(password1) < 8:
            flash("Password must be 8 characters or more", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        else:
            flash("Account created", category="success")

    return render_template("sign_up.html")
