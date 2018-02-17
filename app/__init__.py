"""
Fabco Workorder System
Solomon Bothwell
ssbothwell@gmail.com
"""
import os
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy Instance
db = SQLAlchemy()

# Component Imports
import app.models
import app.validators
from app.controllers import controllers



def create_app(database_config):
    # Generate Flask instance
    app = Flask(__name__)
    # Set deployment context from environment variable
    #app.config.from_object(os.environ['APP_SETTINGS'])
    app.config.from_object(database_config)
    # Create SQLAlchemy instance
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(controllers, url_prefix='/')

    return app

