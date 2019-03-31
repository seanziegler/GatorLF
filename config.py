import os

class DevConfig():
    DEBUG = True
    CSRF_ENABLED = True
    #SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:pass@localhost/postgres"

class TestConfig():
    pass

class ProdConfig():
    pass
