from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

from booknet_app.models import User

class AddBookForm(FlaskForm):
    titel = StringField('Buchtitel', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    isbn = IntegerField('ISBN')
    submit = SubmitField('Buch hinzufügen')

class SearchBookForm(FlaskForm):
    suchwort = StringField('Buch suchen', validators=[DataRequired()])
    submit = SubmitField('Suche')
