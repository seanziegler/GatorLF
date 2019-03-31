from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
import os

from config import DevConfig

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DevConfig.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import routes
