import os

class DevConfig():
    DEBUG = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "postgresql://sziegler:devpassword@gatorlfpostgres.cfk7jbe8i73l.us-east-1.rds.amazonaws.com:5432/postgres"
    FLASK_ENV = "development"
    SECRET_KEY = os.urandom(32)

class TestConfig():
    pass

class ProdConfig():
    pass
