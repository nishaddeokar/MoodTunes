from datetime import datetime
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputForm, GenreForm
import sqlite3
import auth
import api

streak = 0

def insert(id, step, step_target, weight, weight_target, height, level):
    con = sqlite3.connect("out.db")
    con.execute("INSERT OR REPLACE INTO HEALTH_DATA (ID,WEIGHT,HEIGHT,LEVEL) \
          VALUES (?,?,?,?,?,?,?)", (id, weight, height, level))
    con.commit()
    con.close()


@app.route('/', methods=['GET', 'POST'])
@app.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        auth.get()
        return redirect(url_for('gen'))
    return render_template('input.html',  title='Sign In', form=form)

@app.route('/gen', methods=['GET', 'POST'])
def gen():
    form = GenreForm()
    if form.validate_on_submit():
        print(api.get_json())
        return redirect(url_for('display'))
    return render_template('gen.html', title='Create', username="Nishad", form=form)

@app.route('/display')
def display():
    user = {'username': 'Nishad', 'graph': 'foo.png'}
    return render_template('display.html', title='Display', user=user)