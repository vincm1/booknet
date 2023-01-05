from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

from booknet_app.models import User

class StoreForm(FlaskForm):
    storename = StringField('Storename', validators=[DataRequired()])
    storebild = FileField('Storefoto', validators=[FileAllowed(['png', 'jpg'])])
    adresse = StringField('Adresse', validators=[DataRequired()])
    beschreibung = TextAreaField('Was macht den Store unique?')
    submit = SubmitField('Store hinzufügen')
    
class EditStoreForm(FlaskForm):
    storename = StringField('Storename')
    storebild = FileField('Storefoto', validators=[FileAllowed(['png', 'jpg'])])
    adresse = StringField('Adresse')
    beschreibung = TextAreaField('Was macht den Store unique?')
    submit = SubmitField('Store hinzufügen')
