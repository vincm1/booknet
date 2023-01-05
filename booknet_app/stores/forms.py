from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

from booknet_app.models import Store

def check_storename(self, field):
    if Store.query.filter_by(storename=field.data).first():
        raise ValidationError("Store exisitiert bereits!")

class StoreForm(FlaskForm):
    storename = StringField('Storename', validators=[DataRequired(), check_storename])
    storebild = FileField('Storefoto', validators=[FileAllowed(['png', 'jpg'])])
    adresse = StringField('Adresse', validators=[DataRequired()])
    beschreibung = TextAreaField('Was macht den Store unique?')
    submit = SubmitField('Store hinzufügen')
    
class EditStoreForm(FlaskForm):
    storename = StringField('Storename', validators=[check_storename])
    storebild = FileField('Storefoto', validators=[FileAllowed(['png', 'jpg'])])
    adresse = StringField('Adresse')
    beschreibung = TextAreaField('Was macht den Store unique?')
    submit = SubmitField('Store hinzufügen')
