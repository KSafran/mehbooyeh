"""application factory"""
from flask import Flask
from .routes import BLUEPRINT
from .config import database_uri
from .model import db


def create_app():
    """makes the application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    db.init_app(app)
    app.register_blueprint(BLUEPRINT)
    return app
