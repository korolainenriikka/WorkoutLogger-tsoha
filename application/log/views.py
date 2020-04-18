import datetime

from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application import app, db
from application.models import Result, Session
from application.forms import ResultForm, ModifyForm, SessionForm


@app.route("/results/new/")
@login_required
def session_log():
	return render_template("log/newsession.html", form=SessionForm())


@app.route("/results/newresults/", methods=["GET", "POST"])
@login_required
def results_log():
	form = SessionForm(request.form)
	rounds = request.form.get("rounds")
	distance = request.form.get("distance")
	if not form.validate():
		return render_template("log/newsession.html", form=form)
	return render_template("log/newresults.html", form=ResultForm(), rounds=rounds, distance=distance)


@app.route("/results/createresults/<rounds>&<distance>", methods=["POST"])
@login_required
def results_create(rounds, distance):
	form = ResultForm(request.form)
	results = request.form.get("results").splitlines()
	error_message = validate_results(rounds, results)
	if error_message != "":
		flash(error_message)
		return render_template("log/newresults.html", form=form, rounds=rounds, distance=distance)

	s = Session()
	s.account_id = current_user.id
	db.session.add(s)
	db.session.commit()
	session = Session.query.order_by(Session.id.desc()).first()
	for result in results:
		r = Result()
		r.time = datetime.datetime.strptime(result, '%H:%M:%S').time()
		r.distance = distance
		r.session_id = session.id
		db.session.add(r)
	db.session.commit()
	return redirect(url_for("list_recent"))



def validate_results(rounds, results):
	for result in results:
		try:
			datetime.datetime.strptime(result, '%H:%M:%S')
		except:
			return "Incorrect data format"
	if (len(results) != int(rounds)):
		return "Incorrect number of inserted results"
	return ""


@app.route("/results/modify/", methods=["GET", "POST"])
@login_required
def select_modified():
	if request.method == "GET":
		recent_sessions = {}
		sessions = Session.query.filter_by(account_id=current_user.id).all()
		for session in sessions:
			recent_sessions[(session.id, session.date)] = Result.query.filter_by(session_id=session.id).all()
		return render_template("log/selectmodified.html", recent=recent_sessions)


@app.route("/results/modify/<result_id>", methods=["GET", "POST"])
@login_required
def result_modify(result_id):
	if request.method == "GET":
		return render_template("log/modify.html", form=ModifyForm(distance=Result.query.get(result_id).distance,
																  time=Result.query.get(result_id).time),
							   result_id=result_id)


	form = ModifyForm(request.form)
	if not form.validate():
		return render_template("log/modify.html", result_id=result_id, form=form)

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

	results_in_session = Result.query.filter_by(session_id=r.session_id).all()
	if(len(results_in_session) == 1):
		s = Session.query.get(r.session_id)
		db.session.remove(s)

	db.session().commit()

	return redirect(url_for("list_recent"))
