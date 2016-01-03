from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {"nickname": 'Darrel'}
    posts = [
        {
            'author': {'nickname': 'Master Chief'},
            'body': 'Beautiful day in Seattle!'
        },
        {
            'author': {'nickname': 'Agent Locker'},
            'body': 'All hail the conquering hero!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
