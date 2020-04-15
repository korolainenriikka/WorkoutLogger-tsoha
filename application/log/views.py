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
	# workout = request.form.get("workout")
	sets = request.form.get("rounds")
	reps = request.form.get("distance")
	if not form.validate():
		return render_template("log/newsession.html", form=form)
	return render_template("log/newresults.html", form=ResultForm(), sets=sets, reps=reps, errorMessage="")


@app.route("/results/createresults/<sets>&<reps>", methods=["POST"])
@login_required
def results_create(sets, reps):
	form = ResultForm(request.form)
	results = []
	results = request.form.get("results").splitlines()
	errorMessage = validateResults(sets, reps, results)
	if errorMessage != "":
		flash(errorMessage)
		return render_template("log/newresults.html", form=form, sets=sets, reps=reps, errorMessage=errorMessage)
	# luodaan tietoo: session(id,date, account_id) resultcond(session_id)
	for result in results:
		print(result)

	s = Session()
	s.account_id = current_user.id
	db.session.add(s)
	db.session.commit()
	session = Session.query.order_by(Session.id.desc()).first()
	for result in results:
		r = Result()
		r.time = datetime.datetime.strptime(result, '%H:%M:%S').time()
		r.distance = reps
		r.session_id = session.id
		db.session.add(r)
	db.session.commit()
	return redirect(url_for("list_recent"))


import re


def validateResults(sets, reps, results):
	regex = re.compile('..:..:..')
	matches = [string for string in results if re.match(regex, string)]
	if (len(matches) != len(results)):
		return "Inserted results do not match requested form"
	if (len(results) == sets):
		return "Wrong number of inserted results"
	return ""


@app.route("/results/modify/<result_id>", methods=["GET", "POST"])
@login_required
def results_modify(result_id):
	if request.method == "GET":
		return render_template("log/modify.html", result_id=result_id,
							   form=ModifyForm(newtext=Result.query.get(result_id).description))

	form = ModifyForm(request.form)
	if not form.validate():
		return render_template("log/modify.html", result_id=result_id, form=form)

	newText = request.form.get("newtext")
	r = Result.query.get(result_id)
	r.description = newText
	db.session().commit()

	return redirect(url_for("list_recent"))


@app.route("/results/<result_id>", methods=["GET"])
@login_required
def results_delete(result_id):
	r = Result.query.get(result_id)

	db.session().delete(r)
	db.session().commit()

	return redirect(url_for("list_recent"))
