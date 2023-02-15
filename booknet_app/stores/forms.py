from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, DateField, TimeField
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
    category = SelectField('Kategorie', choices=[('Cozy', 'Cozy'), ('Library','Library'), ('Corner Shop', 'Corner Shop'), ('Coffe Place', 'Coffe Place')])
    adresse = StringField('Adresse', validators=[DataRequired()])
    city = SelectField('Stadt', choices=[('Berlin', 'Berlin'), ('Hamburg','Hamburg'), ('München', 'München'), 
                                         ('Köln', 'Köln'), ('Düsseldorf', 'Düsseldorf'), ('Stuttgart', 'Stuttgart')])
    seats = IntegerField('Leseplätze', validators=[DataRequired()])
    beschreibung = TextAreaField('Was macht den Store unique?')
    submit = SubmitField()

class BookStoreForm(FlaskForm):
    people = IntegerField('Personen', validators=[DataRequired()])
    datum = DateField('Datum', format="%Y-%m-%d", validators=[DataRequired()])
    uhrzeit = TimeField('Uhrzeit', format="%H:%M")
    submit = SubmitField('Platz buchen')