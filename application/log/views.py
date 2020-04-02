from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.models import Result, Session
from application.forms import SessionForm, ModifyForm

@app.route("/results/new", methods=["GET", "POST"])
@login_required
def session_create():
    if request.method == "GET":
        return render_template("log/new.html", form = SessionForm())

    form = SessionForm(request.form)

    if not form.validate():
        return render_template("log/new.html", form=form)

    s = Session()
    db.session.add(s)

    thisSession = Session.query.order_by(Session.id.desc()).first()
    r1 = Result(request.form.get("result1"))
    r1.account_id = current_user.id
    r1.session_id = thisSession.id

    r2 = Result(request.form.get("result2"))
    r2.account_id = current_user.id
    r2.session_id = thisSession.id

    r3 = Result(request.form.get("result3"))
    r3.account_id = current_user.id
    r3.session_id = thisSession.id


    db.session().add(r1)
    db.session().add(r2)
    db.session().add(r3)
    db.session().commit()

    return redirect(url_for("results_list"))

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

    return redirect(url_for("results_list"))

@app.route("/results/<result_id>", methods=["GET"])
@login_required
def results_delete(result_id):
    r = Result.query.get(result_id)

    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("results_list"))



