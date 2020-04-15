from flask import render_template
from flask_login import login_required, current_user

from application import app, admin_permission
from application.models import Result, Session, User


@app.route("/analyze/", methods=["GET"])
@login_required
def list_recent():
	recentsessions = {}
	sessions = Session.query.filter_by(account_id=current_user.id).all()
	for session in sessions:
		resultsInSession = Result.query.filter_by(session_id=session.id).all()
		recentsessions[(session.id, session.date)] = Result.query.filter_by(session_id=session.id).all()
	print(recentsessions)
	return render_template("analyze/list.html", recent=recentsessions)


@app.route("/analyze/showactivity", methods=["GET"])
@login_required
def show_activity():
	return render_template("analyze/activity.html", count=Session.count_sessions_last_30_days())


@app.route("/analyze/listusers", methods=["GET"])
@login_required
@admin_permission.require()
def list_users():
	return render_template("analyze/userstats.html", users=User.query.all(), countSesh=Session.count_sessions(),
						   countUser=User.count_users())
