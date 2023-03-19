import time

from .base import get_conn


@get_conn
def block_on_db(conn):
    start = time.time()
    sql = """select pg_sleep(random() / 100);"""
    conn.execute(sql)
    conn.fetchall()
    end = int((time.time() - start) * 1000)  # miliseconds
    return end
