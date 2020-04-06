from flask import render_template
from flask_login import login_required, current_user

from application import app, admin_permission
from application.models import Result, Session

@app.route("/analyze/", methods=["GET"])
@login_required
def list_recent():
    results = Result.query.join(Session).filter_by(account_id=current_user.id).all()
    return render_template("analyze/list.html", results = results)

@app.route("/analyze/showactivity", methods=["GET"])
@login_required
@admin_permission.require()
def show_activity():
    return render_template("analyze/activity.html", count=Session.count_sessions_last_30_days())
