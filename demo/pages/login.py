from flask import Blueprint, render_template
from lib.database import Database

login_page = Blueprint("login", __name__, url_prefix="/login")


@login_page.route("/")
def get_login_page():
    with Database.get_conn() as conn:
        print("woot")
    return render_template("login.html")
