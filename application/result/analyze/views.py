from flask import render_template
from flask_login import login_required, current_user

from application import app
from application.result.models import Conditioning, Session, Result, Strength, Workout


@app.route("/analyze/", methods=["GET"])
@login_required
def list_recent():
	recent_sessions = return_recent_results()
	return render_template("result/analyze/list.html", recent=recent_sessions)

def return_recent_results():
	recent_sessions = {}
	sessions = Session.query.filter_by(account_id=current_user.id).all()
	for session in sessions:
		results_to_list = []
		results_in_session = Result.query.filter_by(session_id=session.id).all()
		for result in results_in_session:
			strength_result = Strength.query.filter_by(id=result.id).one_or_none()
			conditioning_result = Conditioning.query.filter_by(id=result.id).one_or_none()
			if (strength_result is not None):
				workout = Workout.query.filter_by(id=strength_result.workout_id).one()
				distance_or_reps = strength_result.reps
				time_or_weight = str(strength_result.weight) + " kg"
			else:
				workout = Workout.query.filter_by(id=conditioning_result.workout_id).one()
				distance_or_reps = str(conditioning_result.distance) + " m"
				time_or_weight = conditioning_result.time
			results_to_list.append((workout.name, distance_or_reps, time_or_weight))
		recent_sessions[(session.id, session.date)] = results_to_list

	return recent_sessions

@app.route("/analyze/show_run_pbs", methods=["GET"])
@login_required
def list_running_pbs():
	return render_template("result/analyze/run_pbs.html", pbs=Conditioning.find_personal_bests())

@app.route("/analyze/show_strength_pbs", methods=["GET"])
@login_required
def list_strength_pbs():
	return render_template("result/analyze/strength_pbs.html", pbs=Strength.find_personal_bests())

@app.route("/analyze/showactivity", methods=["GET"])
@login_required
def show_activity():
	return render_template("result/analyze/activity.html", count=Session.count_sessions_last_30_days())



