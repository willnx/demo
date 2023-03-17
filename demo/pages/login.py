from flask import Blueprint, make_response, redirect, render_template, request
from logs import get_logger

from database import auth

page = Blueprint("login", __name__, url_prefix="/login")
log = get_logger(__name__)


@page.route("/", methods=["GET"])
def get_login_page():
    return render_template("login.html")


@page.route("/", methods=["POST"])
def login():
    name, password = request.form.get("name"), request.form.get("password")
    token = auth.user_login(name, password)
    if not token:
        return render_template("login.html", error="Login failure."), 401
    original_page = request.cookies.get("original_page", "/")
    resp = make_response(redirect(original_page))
    resp.set_cookie("session", value=token, secure=True)
    return resp


@page.route("/delete", methods=["GET"])
def logout():
    resp = redirect("/login")
    resp.delete_cookie("session")
    return resp
