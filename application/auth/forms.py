from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError, validators
from wtforms.validators import DataRequired

from application.auth.models import User


class LoginForm(FlaskForm):
	username = StringField(render_kw={"placeholder": "Username"})
	password = PasswordField(render_kw={"placeholder": "Password"})

	class Meta:
		csrf = False

class RegisterForm(FlaskForm):
	name = StringField(validators=[DataRequired(), validators.length(min=5, max=50)], render_kw={"placeholder": "Full "
																											"name"})
	username = StringField(validators=[DataRequired(), validators.length(max=50)], render_kw={"placeholder":
																								  "Username"})
	password = PasswordField(validators=[DataRequired(), validators.length(min=5, max=30)], render_kw={"placeholder":
																								  "Password"})
	repeatPassword = PasswordField(validators=[DataRequired(), validators.equal_to("password")],
								   render_kw={"placeholder": "Repeat password"})

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	class Meta:
		csrf = False
