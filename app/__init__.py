from flask import Flask
from flask_pymongo import PyMongo
from .config import Config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
import flask_nav
from flask_nav import elements


mongo = PyMongo()

login_manager = LoginManager()
login_manager.login_view = 'variants.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


db = SQLAlchemy()
nav = flask_nav.Nav()

logged_out = elements.Navbar('Variant App',
    elements.View('Variant search', 'variants.search'),
    elements.View('Log in', 'variants.login'),
)

logged_in = elements.Navbar('Variant App',
    elements.View('Variant search', 'variants.search'),
    elements.View('Log out', 'variants.logout'),
)
nav.register_element('logged_in', logged_in)
nav.register_element('logged_out', logged_out)

def create_app():
    global mongo
    global db
    global user_datastore
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    mongo.init_app(app)
    Bootstrap(app)
    Security(app, user_datastore)
    nav.init_app(app)

    from .variants import variants as variants_blueprint

    app.register_blueprint(variants_blueprint)

    return app


from app.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
