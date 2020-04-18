from flask import render_template
from flask_login import login_required

from application import admin_permission, User, app
from application.result.models import Session


@app.route("/auth/manage_users/listusers", methods=["GET"])
@login_required
@admin_permission.require()
def list_users():
	return render_template("auth/manage_users/user_stats.html", users=User.query.all(),
						   countSesh=Session.count_sessions(),
						   countUser=User.count_users())