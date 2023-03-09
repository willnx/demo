from .base import get_conn


@get_conn
def user_ok(conn, username, password):
    sql = """\
    select count(1) as user_ok from users where name = %s and password = %s
    """
    conn.execute(sql, (username, password))
    resp = conn.fetchone()
    return bool(resp["user_ok"])
