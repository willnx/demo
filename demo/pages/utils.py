from flask import make_response, redirect, request

from demo.database.auth import decode_token


def require_session(func):
    def inner():
        try:
            token = decode_token(request.cookies.get("session"))
        except Exception:
            token = ""
        if not token:
            resp = make_response(redirect("/login"))
            resp.set_cookie("original_page", value=request.path, max_age=600)
            return resp
        resp = func(token)
        return resp

    return inner
