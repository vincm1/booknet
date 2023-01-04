from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from booknet_app.models import User

class BookshelfForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Buchrregal hinzufügen')
