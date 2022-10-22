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

class Company(db.Model,UserMixin):
    # The id column is the Company's identity column
    CompanyId   = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(20), nullable=False, unique=True)
    RUT         = db.Column(db.Integer, nullable=False, unique=True)
	RSocial     = db.Column(db.String(45), nullable=False)

class User(db.Model,UserMixin):
    # The id column is the user's identity column
    UserId       = db.Column(db.Integer, primary_key=True)
    CustomerName = db.Column(db.String(45), nullable=False, unique=True)
    Password     = db.Column(db.String(80), nullable=False)
	CompanyId    = db.Column(db.Integer, foreign_key=True)
	Email        = db.Column(db.String(45), nullable=False, unique=True)

class RegisterForm(FlaskForm):
	#Company
    CompanyName = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "CompanyName"})
    RUT = PasswordField(validators=[
                             InputRequired(),
                             Length(min=12, max=12)],
                             render_kw={"placeholder": "RUT"})
    RSocial = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "RSocial"})
	CompanyAddress = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "CompanyAddress"})
	CompanyState = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "CompanyState"})
	CompanyCity = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "CompanyCity"})
	CompanyPhone = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=20)],
                           render_kw={"placeholder": "CompanyPhone"})
	#User
    CustomerName = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "CustomerName"})
    Phone = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=20)],
                           render_kw={"placeholder": "Phone"})
    Password = PasswordField(validators=[
                             InputRequired(),
                             Length(min=8, max=20)],
                             render_kw={"placeholder": "Password"})
    Email = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "Email"})
    Birthdate = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "Birthdate"})
    Address = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "Address"})
	State = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "State"})
	City = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=45)],
                           render_kw={"placeholder": "City"})
    submit = SubmitField('Register')

def validate_username(self, RUT):
    existing_user_username = User.query.filter_by(RUT=CustomerName.data).first()
    if existing_user_username:
        raise ValidationError('That username already exists. Please choose a different one.')

# The username must be unique, i.e. each name
# User must be different
def validate_username(self, CustomerName):
    existing_user_username = User.query.filter_by(CustomerName=CustomerName.data).first()
    if existing_user_username:
        raise ValidationError('That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    CustomerName = StringField(validators=[InputRequired(),
                                     Length(min=4, max=45)],
                                     render_kw={"placeholder": "CustomerName"})
    Password = PasswordField(validators=[InputRequired(),
                                     Length(min=8, max=20)],
                                     render_kw={"placeholder": "Password"})
    submit = SubmitField('signin')


@app.route('/', strict_slashes=False)
def index():
    return render_template('landing_page.html')

@app.route('/signin',  strict_slashes=False)
def signin():
    return render_template('sign_in.html')

@app.route('/sign_up', strict_slashes=False)
def sign_up():
    return render_template ('sign_up.html')

@app.route('/sign_up2', strict_slashes=False)
def sign_up2():
    return render_template ('sign_up2.html')

@app.route('/sign_up3', strict_slashes=False)
def sign_up3():
    return render_template ('sign_up3.html')

@app.route('/home', strict_slashes=False)
#@login_required
def home():
    return render_template ('home.html')

@app.route('/editclient', strict_slashes=False)
#@login_required
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
