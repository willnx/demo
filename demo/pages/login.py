from flask import Blueprint, render_template

login_page = Blueprint("login", __name__, url_prefix="/login")


@login_page.route("/")
def get_login_page():
    return render_template("login.html")
