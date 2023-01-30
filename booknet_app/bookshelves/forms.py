from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired
from booknet_app import db
from booknet_app.models import Bookshelf
class BookshelfForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    beschreibung = TextAreaField('Was macht das Shelf aus?')
    submit = SubmitField('Buchrregal hinzufügen')

class ISBNForm(FlaskForm):
    bookshelf = SelectField('Bookshelf', choices=[], name="bookshelf_name", validators=[DataRequired()])
    isbn = HiddenField()
    submit = SubmitField('Buch hinzugfügen!')