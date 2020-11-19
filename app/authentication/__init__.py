from flask import Blueprint

auth_bp = Blueprint('authentication', __name__, url_prefix='/authentication')

from . import routes, models