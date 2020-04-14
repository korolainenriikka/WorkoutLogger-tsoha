from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from wtforms import StringField, validators

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
	#workout = request.form.get("workout")
	sets = request.form.get("sets")
	reps = request.form.get("repetitions")
	if not form.validate():
		return render_template("log/newsession.html", form=form)
	return render_template("log/newresults.html", form=ResultForm(), sets=sets, reps=reps)


@app.route("/results/createresults/<sets><reps>", methods=["POST"])
@login_required
def results_create(sets, reps):
	form = ResultForm(request.form)
	results = []
	results = request.form.get("results").splitlines()
	if not validateResults(sets, reps, results):
		return render_template("log/newresults.html", form=form)
	for result in results:
		print(result)

def validateResults(sets, reps, results):
	if(results.len()!= sets):
		return False
	return True

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
