from flask_wtf import FlaskForm
from wtforms import PasswordField, validators, ValidationError, StringField, SubmitField, IntegerField, TextAreaField
from application.models import User


class ResultForm(FlaskForm):
	results = TextAreaField()

	class Meta:
		csrf = False


class SessionForm(FlaskForm):
	# workout = StringField("workout:", [validators.DataRequired()])
	sets = IntegerField("repetitions:", [validators.NumberRange(min=1)])
	repetitions = IntegerField([validators.NumberRange(min=1)])

	class Meta:
		csrf = False


class ModifyForm(FlaskForm):
	newtext = StringField("edit description", [validators.DataRequired()])

	class Meta:
		csrf = False


class LoginForm(FlaskForm):
	username = StringField(render_kw={"placeholder": "Username"})
	password = PasswordField(render_kw={"placeholder": "Password"})

	class Meta:
		csrf = False


class RegisterForm(FlaskForm):
	name = StringField([validators.DataRequired()], render_kw={"placeholder": "Full name"})
	username = StringField([validators.DataRequired()], render_kw={"placeholder": "Username"})
	password = PasswordField([validators.DataRequired()], render_kw={"placeholder": "Password"})
	repeatPassword = PasswordField([validators.DataRequired(), validators.equal_to("password")],
								   render_kw={"placeholder": "Repeat password"})

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	class Meta:
		csrf = False
