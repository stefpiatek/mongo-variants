import pathlib
from .secret_info import SECRET_KEY, SECURITY_PASSWORD_SALT

base_dir = pathlib.Path(__file__).absolute().parent.parent

class Config:
    WTF_CSRF_ENABLED = True
    DEBUG = True
    TESTING = True
    SECRET_KEY = SECRET_KEY
    MONGO_URI = "mongodb://localhost:27017/variant_database"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir}/users.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = SECURITY_PASSWORD_SALT
    SECURITY_REGISTERABLE = True
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_POST_LOGIN_VIEW = "/search"
    SECURITY_POST_REGISTER_VIEW = "/search"

    @staticmethod
    def init_app(app):
        pass
