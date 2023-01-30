from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

from booknet_app.models import User

class SearchBookForm(FlaskForm):
    suchwort = StringField('Buch suchen', validators=[DataRequired()])
    submit = SubmitField('Suche')

class ChatForm(FlaskForm):
    prompt = StringField('Wonach suchst du?', validators=[DataRequired()])
    submit = SubmitField('Senden')