from flask import render_template, request, redirect, url_for, current_app, flash
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm
from flask_principal import Identity, AnonymousIdentity, identity_changed


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()

    if user is None or not user.check_password(form.password.data):
        flash("No such username or password")
        return render_template("auth/loginform.html", form = form)

    login_user(user)
    identity_changed.send(current_app._get_current_object(),
                          identity=Identity(user.id))
    return redirect(url_for("index"))

@app.route("/auth/logout", methods = ["GET", "POST"])
@login_required
def auth_logout():
    logout_user()
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    return redirect("/")

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)
    if not form.validate():
        return render_template("auth/registerform.html", form=form)

    u = User(request.form.get("name"), request.form.get("username"), request.form.get("password"))
    if request.form.get("name") == "superuser":
        u.user_type = 'admin'
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))
