from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from wtforms import ValidationError

from booknet_app.models import User
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    passwort = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Anmelden')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    passwort = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Login')