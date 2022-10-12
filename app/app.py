from flask import Flask

app=Flask(__name__)

@app.route('/')
def Index():
    return 'Landing Page!'

@app.route('/home')
def home():
    return 'Home page'

@app.route('/add_client')
def add_client():
    return 'add client'

@app.route('/edit_client')
def edit_client():
    return 'edit client'

@app.route('/delete_client')
def delete_client():
    return 'delete client'

if __name__=='__main__':
    app.run(port = 3000, debug = True)