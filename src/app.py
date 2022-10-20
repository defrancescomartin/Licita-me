from flask import Flask, render_template

from config import config

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('/auth/login.html')

@app.route('/home')
def home():
    return 'Home page'

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(port = 3000, debug = True)