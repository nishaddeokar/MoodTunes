from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

class AuthForm(FlaskForm):
    submit = SubmitField('Terra')
    submit2 = SubmitField('Spotify')

class GenreForm(FlaskForm):
    genres = ["pop", "rap", "rock", "urbano latino", "hip hop", "trap latino", "dance pop", "reggaeton", "pop rap", "modern rock", "trap", "latin pop", "classic rock"]
    myField = SelectField('Field name', choices = genres, validators = [DataRequired()])
    submit = SubmitField('Submit')
