from application import app, db
from flask import redirect, render_template, request, url_for
from application.results.models import Result
from application.results.forms import ResultForm

@app.route("/results", methods=["GET"])
def results_index():
    return render_template("results/list.html", results = Result.query.all())

@app.route("/results/new")
def results_form():
    return render_template("results/new.html", form=ResultForm)

@app.route("/results/", methods=["POST"])
def results_create():
    r = Result(request.form.get("description"))

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("results_index"))

@app.route("/results/")
def results_delete():
    return redirect(url_for("results_index"))

@app.route("/results/modify/<result_id>")
def results_modify(result_id):
    return render_template("results/modify.html", result = Result.query.get(result_id))

@app.route("/results/savemodified/<result_id>", methods=["POST"])
def results_savemodified(result_id):
    newText = request.form.get("newtext")
    r = Result.query.get(result_id)
    r.description = newText
    db.session().commit()

    return redirect(url_for("results_index"))
