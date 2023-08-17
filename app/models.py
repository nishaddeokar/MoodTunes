from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    genre = db.Column(db.String(128))
    health_id = db.Column(db.Integer, db.ForeignKey('health.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Health(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    body_id = db.Column(db.Integer, db.ForeignKey('body.id'))
    sleep_id = db.Column(db.Integer, db.ForeignKey('sleep.id'))
    user_id = db.relationship('User', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<ID {}>'.format(self.id)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bpm = db.Column(db.Integer)
    met_value = db.Column(db.Integer)
    bmr = db.Column(db.Float)
    total_burned_calories = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    health_id = db.relationship('Health', backref='health', lazy='dynamic')

    def __repr__(self):
        return '<BPM {}>'.format(self.bpm)

class Body(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estimated_fitness_age = db.Column(db.Integer)
    blood_pressure = db.Column(db.Float)
    bmi = db.Column(db.Float)
    body_temperature = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    health_id = db.relationship('Health', backref='health', lazy='dynamic')

    def __repr__(self):
        return '<BMI {}>'.format(self.bmi)

class Sleep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_REM_events = db.Column(db.Integer)
    num_wakeup_events = db.Column(db.Integer)
    sleep_efficiency = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    health_id = db.relationship('Health', backref='health', lazy='dynamic')

    def __repr__(self):
        return '<Sleep Efficiency {}>'.format(self.sleep_efficiency)