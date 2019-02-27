import os
from .secret_info import SECRET_KEY # create

class Config:
    WTF_CSRF_ENABLED = True
    DEBUG = True
    TESTING = True
    SECRET_KEY = SECRET_KEY
    MONGO_URI = "mongodb://localhost:27017/variant_database"

    @staticmethod
    def init_app(app):
        pass
