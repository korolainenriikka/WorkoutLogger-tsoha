from flask import render_template
from flask_login import login_required, current_user

from application import app
from application.models import Result

@app.route("/analyze/", methods=["GET"])
@login_required
def analyze():
    return render_template("analyze/list.html")

@app.route("/analyze/list", methods=["GET"])
@login_required
def results_list():
    return render_template("analyze/list.html", results = Result.query.filter_by(account_id=current_user.id).all())
