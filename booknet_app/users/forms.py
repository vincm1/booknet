from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, EqualTo, Length, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[Email(), DataRequired()])
    passwort = PasswordField('Passwort', validators=[DataRequired(), Length(min=8, message="Mindestens 8 Zeichen!"), EqualTo('passwort_bestätigen', message="Passwörter stimmen nicht überein!")])
    passwort_bestätigen = PasswordField('Passwort bestätigen', validators=[DataRequired()])
    submit = SubmitField('Anmelden')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    passwort = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Login')


class EditUserForm(FlaskForm):
    username = StringField('Nutzername')
    email = EmailField('Email', validators=[Email()])
    profile_pic = FileField('Profilbild', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Profil ändern!')