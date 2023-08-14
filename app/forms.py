from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    reference = StringField('User ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

class GenreForm(FlaskForm):
    genres = ["pop", "rap", "rock", "urbano latino", "hip hop", "trap latino", "dance pop", "reggaeton", "pop rap", "modern rock", "trap", "latin pop", "classic rock"]
    myField = SelectField('Field name', choices = genres, validators = [DataRequired()])
    submit = SubmitField('Submit')
