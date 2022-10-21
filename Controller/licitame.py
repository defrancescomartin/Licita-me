#!/usr/bin/python3
"""
Main application controller for Holberton MVP
"""

from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user,  current_user
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


app=Flask(__name__, template_folder='../View', static_folder='../View')
# Config connection from licitame app file to LicitaMeDB database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://licitame:Password-2022@localhost/LicitaMeDB'
# Turn off this warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Adding a secret key
app.config['SECRET_KEY']='Pass2022'
# Create the database instance
db  = SQLAlchemy(app)
# Use bcrypt so i can hash the passwords
bcrypt = Bcrypt(app)

# This part of login manager will allow handle things on login
# Loading users from credentials
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'

@app.route('/', strict_slashes=False)
def index():
    return render_template('landing_page.html')

@app.route('/signin', strict_slashes=False)
def signin():
    return render_template('sign_in.html')

@app.route('/signup', strict_slashes=False)
def signup():
        return render_template('sign_up.html')

@app.route('/home', strict_slashes=False)
@login_required
def home():
    return render_template ('home.html')

@app.route('/signup', strict_slashes=False)
def sign_up1():
    return render_template ('sign_up.html')

@app.route('/signup2', strict_slashes=False)
def sign_up2():
    return render_template ('signup2.html')

@app.route('/signup3', strict_slashes=False)
def sign_up3():
    return render_template ('signup3.html')

@app.route('/editclient', strict_slashes=False)
@login_required
def edit_client():
    return 'edit client'

@app.route('/createrequest', strict_slashes=False)
@login_required
def create_request():
	return 'Create request'
    #return render_template ('request.html')

@app.route('/createbid', strict_slashes=False)
@login_required
def create_bid():
	return 'Create bid'
    #return render_template ('bid.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)
