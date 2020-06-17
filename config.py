import os


class DevConfig():
    DEBUG = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = ""
    FLASK_ENV = "development"
    SECRET_KEY = os.urandom(32)


class TestConfig():
    pass


class ProdConfig():
    pass
