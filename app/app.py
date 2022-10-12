from flask import Flask

app=Flask(__name__)

@app.route('/')
def Index():
    return 'Landing Page!'

@app.route('/home')
@login_required
def home():
    return 'Home page'

@app.route('/sign_in')
def sign_in():
    return 'sign in'

@app.route('/sign_up')
def sign_up():
    return 'sign up'

@app.route('/edit_client')
@login_required
def edit_client():
    return 'edit client'

@app.route('/delete_account')
@login_required
def delete_account():
    return 'delete account'

@app.route('/create_request')
@login_required
def create_request():
    return 'create request'

@app.route('/create_bid')
@login_required
def create_bid():
    return 'create bid'


if __name__=='__main__':
    app.run(port = 3000, debug = True)
