from flask import Blueprint, render_template

from database import auth

page = Blueprint("login", __name__, url_prefix="/login")

from logs import get_logger


@page.route("/", methods=["GET"])
def get_login_page():
    return render_template("login.html")


@page.route("/", methods=["POST"])
def try_login():
    if not auth.user_ok(username="foo", password="ilovecatz"):
        return render_template("login.html"), 401
