from flask import render_template
from flask_login import login_required, current_user

from application import app
from application.result.models import Conditioning, Session, Result

@app.route("/analyze/", methods=["GET"])
@login_required
def list_recent():
	recent_sessions = {}
	sessions = Session.query.filter_by(account_id=current_user.id).all()
	for session in sessions:
		recent_sessions[(session.id, session.date)] = Result.query.filter_by(session_id=session.id).all()
	return render_template("result/analyze/list.html", recent=recent_sessions)

@app.route("/analyze/showpbs", methods=["GET"])
@login_required
def list_pbs():
	return render_template("result/analyze/pbs.html", pbs=Conditioning.find_personal_bests())

@app.route("/analyze/showactivity", methods=["GET"])
@login_required
def show_activity():
	return render_template("result/analyze/activity.html", count=Session.count_sessions_last_30_days())



