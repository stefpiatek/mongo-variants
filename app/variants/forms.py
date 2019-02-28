from flask_wtf import FlaskForm

from wtforms.validators import DataRequired
from wtforms import StringField, SelectMultipleField, SubmitField, ValidationError


class SearchForm(FlaskForm):
    search = StringField('Search region', validators=[DataRequired()])
    FIELD_CHOICES = (
        ("maf", "MAF"), ("variant_type", "Variant Type"),
        ("hgvs", "HGVS"), ("consequence", "Consequence"),
        ("genome_build", "Genome Build"), ("strand", "Strand")
    )
    extra_fields = SelectMultipleField("Extra fields", choices=FIELD_CHOICES)
    submit = SubmitField("Search for variants")

    def validate_search(self, field):
        search = field.data.lstrip("chr")
        base_error = "Please use format chr:start-end"
        try:
            chrom, positions = search.split(":")
        except ValueError:
            raise ValidationError(f'{base_error}, issue with ":" found')
        try:
            start, end = [int(x) for x in positions.split('-')]
        except ValueError:
            raise ValidationError(f'{base_error}, issue with "-" found')
