from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, SelectField, FieldList, HiddenField
from wtforms.validators import DataRequired
from booknet_app import db
from booknet_app.models import Bookshelf
class BookshelfForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    beschreibung = TextAreaField('Was macht das Shelf aus?')
    submit = SubmitField('Buchrregal hinzufügen')

class ISBNForm(FlaskForm):
    bookshelf = SelectField('Bookshelf', choices=[], name="bookshelf_name", validators=[DataRequired()])
    isbn = StringField(validators=[DataRequired()])
    submit = SubmitField('Buch hinzugfügen!')