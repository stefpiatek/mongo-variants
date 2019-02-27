from flask import render_template, redirect, url_for, request

from .. import mongo
from . import variants, forms


@variants.route("/", methods=['GET', 'POST'])
def search():
    form = forms.SearchForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # add validation logic for range?
            search = form.search.data
            search = search.lstrip("chr")
            chrom, positions = search.split(":")
            start, end = [int(x) for x in positions.split('-')]
            var_list = mongo.db.variants.find(
                {'$and':[{'mappings.seq_region_name':chrom},
                    {'mappings.start':{'$gte':start}},
                    {'mappings.end':{'$lte':end}}]})
            return render_template("search.html", form=form, var_list=var_list)
        else:
            return render_template("search.html", form=form)
    else:
        return render_template("search.html", form=form)
