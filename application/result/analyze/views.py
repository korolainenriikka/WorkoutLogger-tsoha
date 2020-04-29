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
		recent_sessions[(session.id, session.date)] = []
		results_in_session = Result.query.filter_by(session_id=session.id).all()
		for result in results_in_session:

			recent_sessions[(session.id, session.date)].append(Conditioning.query.filter_by(id=result.id).one())
	for key in recent_sessions.keys():
		print(key)
		print(recent_sessions[key])
	return render_template("result/analyze/list.html", recent=recent_sessions)

@app.route("/analyze/showpbs", methods=["GET"])
@login_required
def list_pbs():
	return render_template("result/analyze/pbs.html", pbs=Conditioning.find_personal_bests())

@app.route("/analyze/showactivity", methods=["GET"])
@login_required
def show_activity():
	return render_template("result/analyze/activity.html", count=Session.count_sessions_last_30_days())



