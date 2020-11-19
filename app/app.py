"""Main script to start the flask application serving the site."""
import flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from authentication import auth_bp
    app.register_blueprint(auth_bp)

    from main import main_bp
    app.register_blueprint(main_bp)

    return app
