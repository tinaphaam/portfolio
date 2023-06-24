from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tina'}
    posts = [
        {
            'author': {'username': 'Edmond'},
            'body': 'Beautiful day in Hawaii!'
        },
        {
            'author': {'username': 'Beau'},
            'body': 'I like to go on walks!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)
