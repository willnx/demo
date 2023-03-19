import time

import jwt

from demo.settings import settings

from .base import get_conn


@get_conn
def user_login(conn, username, password):
    sql = """\
    select count(1) as user_ok from users where name = %s and password = %s
    """
    conn.execute(sql, (username, password))
    resp = conn.fetchone()
    token = ""
    if resp["user_ok"]:
        token = generate_token(username)
    return token


def generate_token(username, session_lenght=settings.SESSION_LENGHT):
    now = int(time.time())
    claims = {
        "exp": now + session_lenght,
        "iat": now,
        "username": username,
        "version": 1,  # version of the token
    }
    token = jwt.encode(claims, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token


def decode_token(token):
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
