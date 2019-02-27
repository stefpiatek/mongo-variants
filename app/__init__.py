from flask import Flask
from flask_pymongo import PyMongo
from .config import Config # create

mongo = PyMongo()

def create_app():
    global mongo
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    mongo.init_app(app)
    from .variants import variants as variants_blueprint

    app.register_blueprint(variants_blueprint)

    return app


