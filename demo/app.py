import flask
from pages.login import login_page


def make_app():
    app = flask.Flask(__name__)
    app.register_blueprint(login_page)
    return app
