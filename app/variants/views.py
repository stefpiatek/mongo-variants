from flask import render_template, request

from flask_security import login_required

from .. import mongo
from . import variants, forms


@variants.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@variants.route("/search", methods=["GET", "POST"])
@login_required
def search():
    form = forms.SearchForm()
    if request.method == "POST":
        if form.validate_on_submit():
            search_data = form.search.data
            search_data = search_data.lstrip("chr")
            chrom, positions = search_data.split(":")
            start, end = [int(x) for x in positions.split("-")]
            var_list = mongo.db.variants.find(
                {
                    "$and": [
                        {"mappings.seq_region_name": chrom},
                        {"mappings.start": {"$gte": start}},
                        {"mappings.end": {"$lte": end}},
                    ]
                }
            )
            extra_fields = form.extra_fields.data
            return render_template(
                "search.html", form=form, var_list=var_list, extra_fields=extra_fields
            )
        else:  # form not valid
            return render_template("search.html", form=form)
    else:  # not POST
        return render_template("search.html", form=form)
