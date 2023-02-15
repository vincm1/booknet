from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, EqualTo, Length, Email, Regexp, Optional
from booknet_app.models import User

#### Checks: Nutzername & Email bereits vorhanden. ####

def check_username(self, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError(f'Nutzername bereits registriert!')
        
def check_email(self, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError(f'Email bereits registriert!')
class RegistrationForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired(), check_username])
    email = EmailField('Email', validators=[Email(), DataRequired(), check_email])
    passwort = PasswordField('Passwort', validators=[DataRequired(), Length(min=8, message="Mindestens 8 Zeichen!"), 
                            EqualTo('passwort_bestätigen', message="Passwörter stimmen nicht überein!"),
                            Regexp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])", message="Passwort muss Sonderzeichen, Groß-Kleinschreibung.")])
    passwort_bestätigen = PasswordField('Passwort bestätigen', validators=[DataRequired()])
    submit = SubmitField('Anmelden')
    
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    passwort = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Login')

class EditUserForm(FlaskForm):
    username = StringField('Nutzername', validators=[Optional(), check_username])
    email = EmailField('Email', validators=[Email(), Optional(), check_email])
    phone = StringField('Telefon', validators=[Optional(), Regexp("^\+\d{1,3}\d{3,}$", message='Keine Telefonnummer')])
    profile_pic = FileField('Profilbild', validators=[Optional(), FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Profil speichern')