from datetime import datetime
from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import LoginForm, RegistrationForm, AuthForm, GenreForm
import sqlite3
import terraAuth
import spotifyAuth
import api
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('auth')
        return redirect(url_for(next_page))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/auth', methods=['GET', 'POST'])
#@login_required
def auth():
    form = AuthForm()
    if form.validate_on_submit():
        if form.submit.data:
            terraAuth.set("queue")
        if form.submit2.data:
            session['spotifyToken'] = spotifyAuth.get("nishaddeokar")
        return redirect(url_for('auth'))
    return render_template('auth.html',  title='Connect', form=form)

@app.route('/gen', methods=['GET', 'POST'])
@login_required
def gen():
    form = GenreForm()
    if form.validate_on_submit():
        print(api.get_json())
        return redirect(url_for('display'))
    return render_template('gen.html', title='Create', username="Nishad", form=form)

@app.route('/display')
@login_required
def display():
    user = {'username': 'Nishad', 'graph': 'foo.png'}
    return render_template('display.html', title='Display', user=user)