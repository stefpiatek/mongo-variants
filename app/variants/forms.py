from flask_wtf import FlaskForm

from wtforms.validators import DataRequired
from wtforms import (StringField, IntegerField)


class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])

