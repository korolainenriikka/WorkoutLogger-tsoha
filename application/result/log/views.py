import datetime

from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.result.models import Result, Session, Conditioning, Strength, Workout
from application.result.forms import ModifyConditioningForm, RunSessionForm, StrengthSessionForm, ModifyStrengthForm


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
		recent_sessions = return_recent_results()
		return render_template("result/log/select_modified.html", recent=recent_sessions)


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
				distance_or_reps = str(strength_result.reps) + " x"
				time_or_weight = str(strength_result.weight) + " kg"
				results_to_list.append((workout.name, distance_or_reps, time_or_weight, result.id, "strength"))
			else:
				workout = Workout.query.filter_by(id=conditioning_result.workout_id).one()
				distance_or_reps = str(conditioning_result.distance) + " m"
				time_or_weight = conditioning_result.time
				results_to_list.append((workout.name, distance_or_reps, time_or_weight, result.id, "conditioning"))

		recent_sessions[(session.id, session.date)] = results_to_list

	return recent_sessions


@app.route("/results/modify_conditioning/<result_id>", methods=["GET","POST"])
@login_required
def result_modify_conditioning(result_id):
	if request.method=="GET":
		return render_template("result/log/modify_conditioning.html",
							   form=ModifyConditioningForm(distance=Conditioning.query.get(result_id).distance,
														   time=Conditioning.query.get(result_id).time),
							   result_id=result_id)

	r = Result.query.get(result_id)
	s = Session.query.get(r.session_id)
	if s.account_id != current_user.id:
		flash("modifying others' results is not allowed")
		return (redirect(url_for('index')))
	form = ModifyConditioningForm(request.form)
	try:
		datetime.datetime.strptime(form.time.data, '%H:%M:%S')
	except:
		flash("Incorrect data format")
		return render_template("result/log/modify_conditioning.html", result_id=result_id, form=form)

	if not form.validate():
		return render_template("result/log/modify_conditioning.html", result_id=result_id, form=form)

	new_distance = request.form.get("distance")
	new_time = request.form.get("time")
	c = Conditioning.query.get(result_id)
	c.distance = new_distance
	c.time = datetime.datetime.strptime(new_time, '%H:%M:%S').time()
	db.session().commit()

	return redirect(url_for("list_recent"))

@app.route("/results/modify_strength/<result_id>", methods=["GET", "POST"])
@login_required
def result_modify_strength(result_id):
	if request.method == "GET":
		return render_template("result/log/modify_strength.html",
							   form=ModifyStrengthForm(reps=Strength.query.get(result_id).reps,
														   weight=Strength.query.get(result_id).weight),
							   result_id=result_id)

	form = ModifyStrengthForm(request.form)

	r = Result.query.get(result_id)
	s = Session.query.get(r.session_id)
	if s.account_id != current_user.id:
		flash("modifying others' results is not allowed")
		return (redirect(url_for('index')))

	if not form.validate():
		return render_template("result/log/modify_strength.html", result_id=result_id, form=form)

	new_reps = request.form.get("reps")
	new_weight = request.form.get("weight")
	s = Strength.query.get(result_id)
	s.reps = new_reps
	s.weight = new_weight
	db.session().commit()

	return redirect(url_for("list_recent"))


@app.route("/results/<result_id>", methods=["GET", "POST"])
@login_required
def results_delete(result_id):
	r = Result.query.get(result_id)
	c = Conditioning.query.get(result_id)
	s = Strength.query.get(result_id)
	session = Session.query.get(r.session_id)
	if session.account_id != current_user.id:
		flash("deleting others' results is not allowed")
		return(redirect(url_for('index')))

	db.session().delete(r)
	if s is not None:
		db.session().delete(s)
	if c is not None:
		db.session().delete(c)
	db.session().commit()

	results_in_session = Result.query.filter_by(session_id=r.session_id).all()
	if (len(results_in_session) == 0):
		s = Session.query.get(r.session_id)
		db.session.delete(s)

	db.session().commit()

	return redirect(url_for("list_recent"))
