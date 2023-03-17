from flask import Blueprint, render_template
from logs import get_logger

from .utils import require_session

page = Blueprint("home", __name__, url_prefix="/")
log = get_logger(__name__)


@page.route("/", methods=["GET"])
@require_session
def home(token):
    return render_template("home.html")
