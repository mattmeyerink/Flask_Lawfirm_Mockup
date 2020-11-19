"""Contains the routing information for each of the pages."""
import flask
from config import Config
from . import main_bp
from flask_login import current_user, login_required


@main_bp.route("/")
def show_homepage():
    context = {
        "pagename": "homepage"
    }
    return flask.render_template("homepage.html", **context)

@main_bp.route("/whoweare/")
def show_whoweare():
    context = {
        "pagename": "weare"
    }
    return flask.render_template("whoweare.html", **context)

@main_bp.route("/whatwedo/")
def show_whatwedo():
    context = {
        "pagename": "whatwedo"
    }
    return flask.render_template("whatwedo.html", **context)

@main_bp.route("/whereweare/")
def show_whereweare():
    context = {
        "pagename": "whereweare"
    }
    return flask.render_template("whereweare.html", **context)

@main_bp.route("/attorneys/")
def show_attorney():
    context = {
        "pagename": "attorney"
    }
    return flask.render_template("attorney.html", **context)

@main_bp.route("/contactus/")
def show_contactus():
    context = {
        "pagename": "homepage"
    }
    return flask.render_template("contactus.html", **context)
