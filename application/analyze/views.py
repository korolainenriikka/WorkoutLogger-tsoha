from flask import render_template
from flask_login import login_required, current_user

from application import app
from application.models import Result, Session

@app.route("/analyze/", methods=["GET"])
@login_required
def list_recent():
    print(current_user.id)
    results = Result.query.join(Session).filter_by(account_id=current_user.id).all()
    return render_template("analyze/list.html", results = results)

@app.route("/analyze/showactivity", methods=["GET"])
@login_required
def show_activity():
    return render_template("analyze/activity.html")

