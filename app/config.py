import os
from .secret_info import SECRET_KEY, SECURITY_PASSWORD_SALT

class Config:
    WTF_CSRF_ENABLED = True
    DEBUG = True
    TESTING = True
    SECRET_KEY = SECRET_KEY
    MONGO_URI = "mongodb://localhost:27017/variant_database"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = SECURITY_PASSWORD_SALT

    @staticmethod
    def init_app(app):
        pass
