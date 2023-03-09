import atexit
import contextlib
import functools

from psycopg2 import extras, pool


class Database:
    APP = None

    def __init__(self, username, password, hostname, db_name, port, min_conn, max_conn):
        self.pool = pool.ThreadedConnectionPool(
            min_conn,
            max_conn,
            host=hostname,
            user=username,
            password=password,
            database=db_name,
            port=port,
        )

    def init_app(self, app):
        app.config["db_conn_pool"] = self.pool
        Database.APP = app
        atexit.register(self.pool.closeall)


def get_conn(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if Database.APP is None:
            raise RuntimeError("Application not initialized")
        conn = Database.APP.config["db_conn_pool"].getconn()
        with conn.cursor(cursor_factory=extras.DictCursor) as cursor:
            try:
                resp = func(cursor, *args, **kwargs)
            finally:
                Database.APP.config["db_conn_pool"].putconn(conn)
        return resp

    return inner
