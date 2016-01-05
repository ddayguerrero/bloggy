from flask import render_template, flash, redirect, g, url_for, session
from app import app, lm, oid
from .forms import LoginForm
from .models import User


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


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    # Redirect to index if user exists and not authenticated
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
