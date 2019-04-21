from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CSRFProtect

import os
import config

app = Flask(__name__)
app.config.from_object(config.DevConfig)

csrf = CSRFProtect(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import routes
