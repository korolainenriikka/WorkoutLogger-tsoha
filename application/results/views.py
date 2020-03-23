from flask import redirect, render_template, request, url_for

from application import app, db
from application.results.models import Result
from application.results.forms import ResultForm, ModifyForm

@app.route("/results", methods=["GET"])
def results_index():
    return render_template("results/list.html", results = Result.query.all())

@app.route("/results/new")
def results_form():
    return render_template("results/new.html", form = ResultForm())

@app.route("/results/", methods=["POST"])
def results_create():
    form = ResultForm(request.form)

    if not form.validate():
        return render_template("results/new.html", form=form)

    r = Result(request.form.get("description"))

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("results_index"))

@app.route("/results/modify/<result_id>")
def results_modify(result_id):
    return render_template("results/modify.html", result_id = result_id,
                           form = ModifyForm(newtext = Result.query.get(result_id).description))

@app.route("/results/<result_id>", methods=["GET"])
def results_delete(result_id):
    r = Result.query.get(result_id)

    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("results_index"))

@app.route("/results/savemodified/<result_id>", methods=["POST"])
def results_savemodified(result_id):
    form = ModifyForm(request.form)
    if not form.validate():
        return render_template("results/modify.html", result_id=result_id, form=form)

    newText = request.form.get("newtext")
    r = Result.query.get(result_id)
    r.description = newText
    db.session().commit()

    return redirect(url_for("results_index"))