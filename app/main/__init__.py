"""Blueprint to view all of the pages on the website."""
import flask


main_bp = flask.Blueprint("main", __name__)

from . import routes
