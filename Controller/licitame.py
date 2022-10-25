#!/usr/bin/python3
"""
Main application controller for Holberton MVP
"""

from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user,  current_user
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from datetime import datetime


app=Flask(__name__, template_folder='../View', static_folder='../View')
# Config connection from licitame app file to LicitaMeDB database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://licitame:Password-2022@localhost/LicitaMeDB'
# Turn off this warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Adding a secret key
app.config['SECRET_KEY']='Pass2022'
# Config the pool for uploads
app.config['UPLOAD_FOLDER']='./pool'
# Config max upload file size to 10MB
app.config['MAX_CONTENT_PATH']= 1024*1024*10
# Create the database instance
db  = SQLAlchemy(app)
# Use bcrypt so i can hash the passwords
bcrypt = Bcrypt(app)

# This part of login manager will allow handle things on login
# Loading users from credentials
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Company(db.Model):
    __tablename__ = 'Company'
    # The id column is the Company's identity column
    CompanyId        = db.Column(db.Integer, primary_key=True)
    CompanyName      = db.Column(db.String(20), nullable=False, unique=True)
    RUT              = db.Column(db.String(12), nullable=False, unique=True)
    RSocial          = db.Column(db.String(45), nullable=True)
    Address           = db.Column(db.String(45), nullable=True)
    State            = db.Column(db.String(45), nullable=True)
    City             = db.Column(db.String(45), nullable=True)
    Phone            = db.Column(db.String(20), nullable=True)
    CreationDate     = db.Column(db.DateTime, default=datetime.utcnow)
    ModificationDate = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    # The id column is the user's identity column
    id           = db.Column(db.Integer, primary_key=True)
    CompanyId    = db.Column(db.Integer, db.ForeignKey("Company.CompanyId"))
    CustomerName = db.Column(db.String(45), nullable=False, unique=True)
    Phone        = db.Column(db.String(20), nullable=True)
    Email        = db.Column(db.String(45), nullable=False, unique=True)
    Birthdate    = db.Column(db.Date, nullable=True)
    Address      = db.Column(db.String(45), nullable=True)
    State        = db.Column(db.String(45), nullable=True)
    City         = db.Column(db.String(45), nullable=True)
    Password     = db.Column(db.String(80), nullable=False)
    CreationDate = db.Column(db.DateTime, default=datetime.utcnow)
    ModificationDate = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Request(db.Model):
    __tablename__ = 'Request'
    # The id column is the user's identity column
    RequestId     = db.Column(db.Integer, nullable=False, primary_key=True)
    CompanyId     = db.Column(db.Integer, db.ForeignKey("Company.CompanyId"))
    id            = db.Column(db.Integer, db.ForeignKey("User.id"))
    Category      = db.Column(db.String(45), nullable=False)
    Description   = db.Column(db.Text(64000), nullable=False)
    Title         = db.Column(db.String(45), nullable=False)
    FileId        = db.Column(db.String(10), nullable=False)
    StartingDate  = db.Column(db.Date, nullable=True)
    FinishingDate = db.Column(db.Date, nullable=True)
    StatusCode    = db.Column(db.Integer, nullable=True)
    CreationDate = db.Column(db.DateTime, default=datetime.utcnow)
    ModificationDate = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Bid(db.Model):
    __tablename__ = 'Bid'
    # The id column is the user's identity column
    BidId         = db.Column(db.Integer, nullable=False, primary_key=True)
    BidNumber     = db.Column(db.String(10), nullable=False)
    RequestId     = db.Column(db.Integer, db.ForeignKey("Request.RequestId"))
    id            = db.Column(db.Integer, db.ForeignKey("User.id"))
    CompanyId     = db.Column(db.Integer, db.ForeignKey("Company.CompanyId"))
    Category      = db.Column(db.String(45), nullable=False)
    FileId        = db.Column(db.String(10), nullable=False)
    CurrencyCode  = db.Column(db.Integer, nullable=True)
    StatusCode    = db.Column(db.Integer, nullable=True)
    TotalAmount   = db.Column(db.Numeric(12,2))
    StartingDate  = db.Column(db.Date)
    FinishingDate = db.Column(db.Date)

class RegisterForm(FlaskForm):
    #Company
    CompanyName = StringField(validators=[
                           InputRequired(),
                           Length(min=2, max=45)],
                           render_kw={"placeholder": "CompanyName"})
    RUT = StringField(validators=[
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
                           Length(min=3, max=45)],
                           render_kw={"placeholder": "CustomerName"})
    Phone = StringField(validators=[
                           InputRequired(),
                           Length(min=4, max=20)],
                           render_kw={"placeholder": "Phone"})
    Password = PasswordField(validators=[
                             InputRequired(),
                             Length(min=8, max=20),
                             EqualTo('Confirm', message='Passwords must match')],
                             render_kw={"placeholder": "Password"})
    Confirm  = PasswordField(validators=[
                             InputRequired(),
                             Length(min=8, max=20)],
                             render_kw={"placeholder": "Repeat Password"})
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
    submit = SubmitField('sign_up')

def add_relationship(self, RUT):
    existing_Company_RUT = Company.query.filter_by(RUT=RUT.data).first()
    if existing_Company_RUT:
        raise ValidationError('That RUT already exists. Already registered? Signin please.')

# The username must be unique, i.e. each name
# User must be different
def validate_username(self, CustomerName):
    existing_user_username = User.query.filter_by(CustomerName=CustomerName.data).first()
    if existing_user_username:
        raise ValidationError('That username already exists. Please choose a different one.')
# Signin Form validators
class SigninForm(FlaskForm):
    CustomerName = StringField(validators=[InputRequired(),
                                     Length(min=3, max=45)],
                                     render_kw={"placeholder": "CustomerName"})
    Password = PasswordField(validators=[InputRequired(),
                                     Length(min=8, max=20)],
                                     render_kw={"placeholder": "Password"})
    submit = SubmitField('signin')

# Create Request Form validators
class RequestForm(FlaskForm):
    Title = StringField(validators=[InputRequired(),
                                     Length(min=3, max=45)],
                                     render_kw={"placeholder": "Title"})
    Description = StringField(validators=[InputRequired(),
                                     Length(min=3, max=64000)],
                                     render_kw={"placeholder": "Description"})
    Category = StringField(validators=[InputRequired(),
                                     Length(min=3, max=45)],
                                     render_kw={"placeholder": "Category"})
    FinishDate = StringField(validators=[InputRequired(),
                                     Length(min=9, max=11)],
                                     render_kw={"placeholder": "FinishDate"})
    submit = SubmitField('create_request')


# Create Bid Form validators
class BidForm(FlaskForm):

    StartingDate = StringField(validators=[InputRequired(),
                                     Length(min=9, max=11)],
                                     render_kw={"placeholder": "StartingDate"})
    FinishDate = StringField(validators=[InputRequired(),
                                     Length(min=9, max=11)],
                                     render_kw={"placeholder": "FinishDate"})
    CurrencyCode = StringField(validators=[InputRequired(),
                                     Length(min=1, max=1)],
                                     render_kw={"placeholder": "Currency"})
    TotalAmount = StringField(validators=[InputRequired(),
                                     Length(min=1, max=15)],
                                     render_kw={"placeholder": "TotalAmount"})
    submit = SubmitField('create_request')


@app.route('/', strict_slashes=False)
def index():
    return render_template('landing_page.html')

@app.route('/signin', methods=['GET', 'POST'],  strict_slashes=False)
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(CustomerName=form.CustomerName.data).first()
        if user:
            if bcrypt.check_password_hash(user.Password, form.Password.data):
                login_user(user)
                flash('Logged in successfully!')
                return redirect(url_for('home'))

    return render_template('sign_in.html', form=form)# I will pass this form in my html template

@app.route('/sign_up', methods=['GET', 'POST'], strict_slashes=False)
def sign_up():
    form = RegisterForm()
    # The code for registration
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.Password.data)
        new_company = Company(CompanyName=form.CompanyName.data, RUT=form.RUT.data, RSocial=form.RSocial.data)
        new_user = User(CustomerName=form.CustomerName.data, Password=hashed_password, Email=form.Email.data)
        db.session.add(new_company)
        db.session.commit()
        company = Company.query.filter_by(RUT=form.RUT.data).first()
        new_user = User(CompanyId=company.CompanyId, CustomerName=form.CustomerName.data, Password=hashed_password, Email=form.Email.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('signin'))
        #each time the form is valid we will create
        #immediately a hashed version of this mdps (so that the mdps is encrypted)
        #In order to have a secure registration process

    return render_template ('sign_up.html', form=form)

@app.route('/home', strict_slashes=False)
@login_required
def home():
    return render_template ('home.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('signin'))

@app.route('/editclient', strict_slashes=False)
#@login_required
def edit_client():
    return 'edit client'

@app.route('/create_request', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def create_request():
    form = RequestForm()
    # The code to insert new request
    if form.validate_on_submit():
        new_request = Request(id=current_user.id,
                              CompanyId=current_user.CompanyId,
                              StatusCode=0,
                              Title=form.Title.data,
                              Description=form.Description.data,
                              Category=form.Category.data,
                              FinishDate=form.FinishDate.data,)
        db.session.add(new_reuqest)
        db.session.commit()
        # Must redirect to view "Request by id" (request just created)
        return redirect(url_for('home'))
    return render_template ('request.html')

@app.route('/request/<int:request_id>', strict_slashes=False)
@login_required
def request_by(request_id):
        # View Request by ID
        request = Request.query.filter_by(RequestId=id).first()
        if request.id == current_user.id:
            return render_template('my_request.html', request=request)
        return render_template('request_inside.html', request=request)

@app.route('/create_bid/<int:request_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def create_bid(request_id):
    form = BidForm()
    # The code to insert new request
    if form.validate_on_submit():
        new_bid = Bid(id=current_user.id,
                      CompanyId=current_user.CompanyId,
                      StatusCode=0,
                      TotalAmount=form.TotalAmount.data,
                      StartingDate=form.StartingDate.data,
                      FinishDate=form.FinishDate.data,
                      CurrencyCode=form.CurrencyCode.data)
        db.session.add(new_reuqest)
        db.session.commit()
        # Must redirect to view "Request by id" (request just created)
        return redirect(url_for('home'))
    return render_template ('bid.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)
