from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, session
from app import app, db
from app.forms import LoginForm, RegistrationForm, AuthForm, GenreForm
import terraAuth
import spotifyAuth
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import User, get_latest_bpm_for_user
from load import save_activity_data, save_body_data, save_sleep_data, load_health_data
from generatePlaylist import generate_playlist


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
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
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/auth', methods=['GET', 'POST'])
@login_required
def auth():
    form = AuthForm()
    if form.validate_on_submit():
        if form.submit.data:
            terraAuth.set(current_user.username)
        if form.submit2.data:
            session['spotifyToken'] = spotifyAuth.get(current_user.username)
        return redirect(url_for('auth'))
    return render_template('auth.html',  title='Connect', form=form)

@app.route('/gen', methods=['GET', 'POST'])
@login_required
def gen():
    form = GenreForm()
    if form.validate_on_submit():
        load_health_data(current_user.username)
        latest_health = get_latest_bpm_for_user(current_user.username) or 120
        session['playlistID'] = generate_playlist(current_user.username, session.get('spotifyToken', None), str(form.myField), latest_health)
        return redirect(url_for('display'))
    return render_template('gen.html', title='Create', username="Nishad", form=form)

@app.route('/display')
@login_required
def display():
    print(session.get('playlistID', None))
    return render_template('display.html', title='Display', playlistID=session.get('playlistID'))