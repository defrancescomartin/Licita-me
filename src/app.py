<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for

=======
from flask import Flask, render_template
from flask_login import login_required
>>>>>>> bbcd49e705b3d1f14b31c82878f7a8e8904c3ee9
from config import config

app=Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods =['GET','POST'])
def login():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template('/auth/login.html')
    else:
        return render_template('/auth/login.html')

@app.route('/home')
@login_required
def home():
    return render_template ('home.html')

@app.route('/signin')
def sign_in():
    return render_template ('sign_in.html')

@app.route('/signup')
def sign_up():
    return render_template ('signup1.html')

@app.route('/editclient')
@login_required
def edit_client():
    return 'edit client'

@app.route('/createrequest')
@login_required
def create_request():
    return render_template ('request.html')

@app.route('/createbid')
@login_required
def create_bid():
    return render_template ('bid.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(port = 3000, debug = True)
