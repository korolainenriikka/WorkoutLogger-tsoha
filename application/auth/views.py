from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

from application import app, db
from application.models import User
from application.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    rightPassword = check_password_hash(user.password_hash, form.password.data)

    if not rightPassword:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout", methods = ["GET", "POST"])
@login_required
def auth_logout():
    logout_user()
    return redirect("/")

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)
    if not form.validate():
        return render_template("auth/registerform.html", form=form)

    u = User(request.form.get("name"), request.form.get("username"), request.form.get("password"))
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))
