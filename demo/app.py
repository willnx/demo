import atexit

import flask
import psycopg2
from database.base import Database
from pages import login
from settings import settings


def make_app():
    app = flask.Flask(__name__)
    app.register_blueprint(login.page)
    db = Database(
        min_conn=settings.DB_MIN_CONN,
        max_conn=settings.DB_MAX_CONN,
        hostname=settings.DB_HOSTNAME,
        username=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        db_name=settings.DB_DATABASE,
        port=settings.DB_PORT,
    )
    db.init_app(app)

    return app
