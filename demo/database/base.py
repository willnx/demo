import atexit
import contextlib
import functools
import time

from psycopg2 import extras, pool

from demo.logs import get_logger

log = get_logger(__name__)


class Database:
    APP = None

    def __init__(self, username, password, hostname, db_name, port, min_conn, max_conn):
        self.pool = None
        error = None
        for _ in range(10):
            try:
                self.pool = self.get_connection_pool(
                    username, password, hostname, db_name, port, min_conn, max_conn
                )
            except Exception as doh:
                error = doh
                time.sleep(1)
            else:
                break
        if self.pool is None:
            log.error("Failed to make DB connection pool")
            raise error

    def get_connection_pool(
        self, username, password, hostname, db_name, port, min_conn, max_conn
    ):
        return pool.ThreadedConnectionPool(
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
