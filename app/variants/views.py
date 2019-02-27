from flask import render_template

from .. import mongo
from . import variants

@variants.route("/")
def variant_results():
    """ Variants """
    variants = mongo.db.variants.find({"name":"rs563303847"})
    return render_template("results.html", variants=variants)
