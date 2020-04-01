from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.models import Result, Session
from application.forms import SessionForm, ModifyForm

@app.route("/results", methods=["GET"])
@login_required
def results_list():
    return render_template("results/list.html", results = Result.query.filter_by(account_id=current_user.id).all())

@app.route("/results/new", methods=["GET", "POST"])
@login_required
def session_create():
    if request.method == "GET":
        return render_template("results/new.html", form = SessionForm())

    form = SessionForm(request.form)

    if not form.validate():
        return render_template("results/new.html", form=form)

    #muist tarkistaa et kentässä on jotai! ei voia validoida atm
    s = Session()
    r = Result(request.form.get("description"))
    r.account_id = current_user.id
    r.session_id = s.id

    db.session.add(s)
    db.session().add(r)
    db.session().commit()

    return redirect(url_for("results_list"))

@app.route("/results/modify/<result_id>", methods=["GET", "POST"])
@login_required
def results_modify(result_id):
    if request.method == "GET":
        return render_template("results/modify.html", result_id = result_id,
                           form = ModifyForm(newtext = Result.query.get(result_id).description))

    form = ModifyForm(request.form)
    if not form.validate():
        return render_template("results/modify.html", result_id=result_id, form=form)

    newText = request.form.get("newtext")
    r = Result.query.get(result_id)
    r.description = newText
    db.session().commit()

    return redirect(url_for("results_list"))

@app.route("/results/<result_id>", methods=["GET"])
@login_required
def results_delete(result_id):
    r = Result.query.get(result_id)

    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("results_list"))
