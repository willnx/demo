import atexit
import contextlib

from psycopg2 import pool


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

    @classmethod
    @contextlib.contextmanager
    def get_conn(cls):
        if cls.APP is None:
            raise RuntimeError("Application not initialized")
        conn = cls.APP.config["db_conn_pool"].getconn()
        yield conn
        cls.APP.config["db_conn_pool"].putconn(conn)
