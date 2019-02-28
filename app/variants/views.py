from flask import render_template, redirect, url_for, request

from flask_login import login_required

from .. import mongo
from . import variants, forms


@variants.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@variants.route("/search", methods=['GET', 'POST'])
@login_required
def search():
    form = forms.SearchForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # add validation logic for range?
            search = form.search.data
            search = search.lstrip("chr")
            chrom, positions = search.split(":")
            start, end = [int(x) for x in positions.split('-')]
            var_list = mongo.db.variants.find({
                '$and':[
                    {'mappings.seq_region_name':chrom},
                    {'mappings.start':{'$gte':start}},
                    {'mappings.end':{'$lte':end}}
                ]
            })
            extra_fields = form.extra_fields.data
            return render_template("search.html", form=form, var_list=var_list, extra_fields=extra_fields)
        else:  # form not valid
            return render_template("search.html", form=form)
    else:  # not POST
        return render_template("search.html", form=form)


@variants.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)


        next = request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return redirect(next or url_for('search'))
    return render_template('login.html', form=form)


@variants.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
