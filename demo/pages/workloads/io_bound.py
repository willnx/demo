import random

from flask import Blueprint, render_template

from demo.database.io_bound import block_on_db
from demo.logs import get_logger
from demo.pages.utils import require_session

page = Blueprint("io_bound", __name__, url_prefix="/workloads/io_bound")
log = get_logger(__name__)


@page.route("/", methods=["GET"])
@require_session
def io_bound(token):
    ms = block_on_db()
    return render_template("io_bound.html", blocked=ms, username=token["username"])
