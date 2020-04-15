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
	rounds = request.form.get("rounds")
	distance = request.form.get("distance")
	if not form.validate():
		return render_template("log/newsession.html", form=form)
	return render_template("log/newresults.html", form=ResultForm(), rounds=rounds, distance=distance)


@app.route("/results/createresults/<rounds>&<distance>", methods=["POST"])
@login_required
def results_create(rounds, distance):
	form = ResultForm(request.form)
	results = []
	results = request.form.get("results").splitlines()
	errorMessage = validateResults(rounds, results)
	if errorMessage != "":
		flash(errorMessage)
		return render_template("log/newresults.html", form=form, rounds=rounds, distance=distance)
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
		r.distance = distance
		r.session_id = session.id
		db.session.add(r)
	db.session.commit()
	return redirect(url_for("list_recent"))


import re


def validateResults(rounds, results):
	regex = re.compile('..:..:..')
	matches = [string for string in results if re.match(regex, string)]
	if (len(matches) != len(results)):
		return "Inserted results do not match requested form"
	if (len(results) != int(rounds)):
		return "Wrong number of inserted results"
	return ""


@app.route("/results/modify/", methods=["GET", "POST"])
@login_required
def select_modified():
	if request.method == "GET":
		recentsessions = {}
		sessions = Session.query.filter_by(account_id=current_user.id).all()
		for session in sessions:
			resultsInSession = Result.query.filter_by(session_id=session.id).all()
			recentsessions[(session.id, session.date)] = Result.query.filter_by(session_id=session.id).all()
		return render_template("log/selectmodified.html", recent = recentsessions)


@app.route("/results/<result_id>", methods=["GET"])
@login_required
def results_delete(result_id):
	r = Result.query.get(result_id)

	db.session().delete(r)
	db.session().commit()

	return redirect(url_for("list_recent"))
