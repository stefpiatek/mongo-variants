from flask_wtf import FlaskForm

from wtforms.validators import DataRequired
from wtforms import StringField, SelectMultipleField


class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    FIELD_CHOICES = (
        ("maf", "MAF"), ("variant_type", "Variant Type"),
        ("hgvs", "HGVS"), ("consequence", "Consequence"),
        ("genome_build", "Genome Build"), ("strand", "Strand")
    )
    extra_fields = SelectMultipleField("Extra fields", choices=FIELD_CHOICES)
