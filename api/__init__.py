"""application factory"""
from flask import Flask
from .routes import BLUEPRINT
from .config import database_uri, secret_key
from .model import db

db = db
def create_app():
    """makes the application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SECRET_KEY'] = secret_key
    with app.app_context():
        db.init_app(app)
    app.register_blueprint(BLUEPRINT)
    return app
