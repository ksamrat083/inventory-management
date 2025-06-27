from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Import and register the blueprint
    from app.routes.products import products_bp
    app.register_blueprint(products_bp)

    return app
