from application import app
from flask import render_template, request


@app.route("/results/new/")
def tasks_form():
    return render_template("results/new.html")


@app.route("/results/", methods=["POST"])
def tasks_create():
    print(request.form.get("name"))

    return "hello world!"
