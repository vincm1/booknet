from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

from booknet_app.models import User

class AddStoreForm(FlaskForm):
    storename = StringField('Storename', validators=[DataRequired()])
    adresse = StringField('Adresse', validators=[DataRequired()])
    beschreibung = TextAreaField('Was macht den Store unique?')
    submit = SubmitField('Store hinzufügen')
