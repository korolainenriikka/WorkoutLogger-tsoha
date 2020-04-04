from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db, dynamic
from application.models import Result, Session
from application.forms import ResultForm, ModifyForm

@app.route("/results/new", methods=["GET", "POST"])
@login_required
def session_create():
    if request.method == "GET":
        return render_template("log/new.html", form = ResultForm())

    form = ResultForm(request.form)

    if not form.validate():
        return render_template("log/new.html", form=form)

    s = Session()
    s.account_id = current_user.id
    db.session.add(s)

    thisSession = Session.query.order_by(Session.id.desc()).first()
    r1 = Result(request.form.get("description"))
    r1.account_id = current_user.id
    r1.session_id = thisSession.id

    db.session().add(r1)
    db.session().commit()

    return redirect(url_for("list_recent"))

@app.route("/results/modify/<result_id>", methods=["GET", "POST"])
@login_required
def results_modify(result_id):
    if request.method == "GET":
        return render_template("log/modify.html", result_id = result_id,
                           form = ModifyForm(newtext = Result.query.get(result_id).description))

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



