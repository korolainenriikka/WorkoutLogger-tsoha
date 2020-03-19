from application import app, db
from flask import redirect, render_template, request, url_for
from application.results.models import Result

@app.route("/results", methods=["GET"])
def results_index():
    return render_template("results/list.html", results = Result.query.all())

@app.route("/results/new")
def results_form():
    return render_template("results/new.html")

@app.route("/results/", methods=["POST"])
def results_create():
    r = Result(request.form.get("name"))

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("results_index"))

@app.route("/results/modify/<result_id>")
def results_modify(result_id):
    return render_template("results/modify.html", result_id=result_id)

@app.route("/results/saveModified/<result_id>", methods=["POST"])
def results_saveModified(result_id):
    r = Result.query.get(result_id)
    r.description = "muokkkkkois"
    db.session.commit()

    return redirect(url_for("results_index"))
