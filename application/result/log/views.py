import datetime

from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.result.models import Result, Session, Conditioning, Strength, Workout
from application.result.forms import ModifyForm, RunSessionForm, StrengthSessionForm


@app.route("/results/new_run/")
@login_required
def run_session_log():
	return render_template("result/log/new_run_session.html", form=RunSessionForm())


@app.route("/results/new_run/", methods=["GET", "POST"])
@login_required
def running_log():
	form = RunSessionForm(request.form)
	rounds = request.form.get("rounds")
	distance = request.form.get("distance")
	if not form.validate():
		return render_template("result/log/new_run_session.html", form=form)
	return render_template("result/log/new_run.html", rounds=int(rounds), distance=distance)


@app.route("/results/new_run/<rounds>%<distance>", methods=["POST"])
@login_required
def run_results_create(rounds, distance):
	form = request.form
	error_message = validate_results(form)
	if error_message != "":
		flash(error_message)
		return render_template("result/log/new_run.html", rounds=int(rounds), distance=distance)

	s = Session()
	s.account_id = current_user.id
	db.session.add(s)
	db.session.commit()
	session = Session.query.order_by(Session.id.desc()).first()

	for value in form.values():
		if (value != ''):
			time = value
			c = Conditioning()
			c.session_id = session.id
			c.time = datetime.datetime.strptime(time, '%H:%M:%S').time()
			c.distance = distance
			c.workout_id = 1
			db.session.add(c)
			db.session.commit()

	return redirect(url_for("list_recent"))


def validate_results(results):
	for key in results.keys():
		try:
			if(key != 'submit_button'):
				datetime.datetime.strptime(results[key], '%H:%M:%S')
		except:
			return "Incorrect data format"
	return ""

@app.route("/results/new_strength_session/")
@login_required
def strength_session_log():
	return render_template("result/log/new_strength_session.html", form=StrengthSessionForm())

@app.route("/results/new_strength/", methods=["GET", "POST"])
@login_required
def strength_log():
	form = StrengthSessionForm(request.form)
	if not form.validate():
		return render_template("result/log/new_strength_session.html", form=form)
	workout = request.form.get("workout")
	sets = int(request.form.get("sets"))
	reps = request.form.get("reps")
	return render_template("result/log/new_strength.html", workout=workout, sets=sets, reps=reps)


def validate_strength_results(results):
	for key in results.keys():
		if key != 'submit_button':
			try:
				int(results[key])
				if int(results[key]) < 0 or int(results[key]) > 300:
					return "Please provide values between 0 and 300"
			except:
				return "Please provide integer values"
	return ""


@app.route("/results/new_strength/<workout>%<sets>%<reps>", methods=["POST"])
@login_required
def strength_results_create(workout, sets, reps):
	form = request.form
	error_message = validate_strength_results(form)
	if error_message != "":
		flash(error_message)
		return render_template("result/log/new_strength.html", workout=workout, sets=int(sets), reps=reps)

	s = Session()
	s.account_id = current_user.id
	db.session.add(s)
	db.session.commit()
	session = Session.query.order_by(Session.id.desc()).first()

	workout_db = Workout.query.filter_by(name = workout).one_or_none()
	if(workout_db is None):
		w = Workout()
		w.name = workout
		db.session.add(w)
		db.session.commit()
		workout_db = Workout.query.order_by(Workout.id.desc()).first()

	workout_id=workout_db.id

	for value in form.values():
		if (value != ''):
			s = Strength()
			s.session_id = session.id
			s.weight = value
			s.reps = reps
			s.workout_id = workout_id
			db.session.add(s)
			db.session.commit()

	return redirect(url_for("list_recent"))

@app.route("/results/modify/", methods=["GET", "POST"])
@login_required
def select_modified():
	if request.method == "GET":
		recent_sessions = {}
		sessions = Session.query.filter_by(account_id=current_user.id).all()
		for session in sessions:
			recent_sessions[(session.id, session.date)] = Result.query.filter_by(session_id=session.id).all()
		return render_template("result/log/select_modified.html", recent=recent_sessions)


@app.route("/results/modify/<result_id>", methods=["GET", "POST"])
@login_required
def result_modify(result_id):
	if request.method == "GET":
		return render_template("result/log/modify.html", form=ModifyForm(distance=Result.query.get(result_id).distance,
																		 time=Result.query.get(result_id).time),
							   result_id=result_id)

	form = ModifyForm(request.form)
	try:
		datetime.datetime.strptime(form.time.data, '%H:%M:%S')
	except:
		flash("Incorrect data format")
		return render_template("result/log/modify.html", result_id=result_id, form=form)

	if not form.validate():
		return render_template("result/log/modify.html", result_id=result_id, form=form)

	new_distance = request.form.get("distance")
	new_time = request.form.get("time")
	r = Result.query.get(result_id)
	r.distance = new_distance
	r.time = datetime.datetime.strptime(new_time, '%H:%M:%S').time()
	db.session().commit()

	return redirect(url_for("list_recent"))


@app.route("/results/<result_id>", methods=["GET", "POST"])
@login_required
def results_delete(result_id):
	r = Result.query.get(result_id)
	db.session().delete(r)
	db.session().commit()

	results_in_session = Result.query.filter_by(session_id=r.session_id).all()
	if (len(results_in_session) == 0):
		s = Session.query.get(r.session_id)
		db.session.delete(s)

	db.session().commit()

	return redirect(url_for("list_recent"))
