from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import NumberRange


class ResultForm(FlaskForm):
	results = TextAreaField(render_kw={"placeholder": "hh:mm:ss"})

	class Meta:
		csrf = False


class SessionForm(FlaskForm):
	rounds = IntegerField(validators=[NumberRange(min=1, max=15)], render_kw={"placeholder": "rounds"})
	distance = IntegerField(validators=[NumberRange(min=1, max=100000)], render_kw={"placeholder": "distance in m"})

	class Meta:
		csrf = False


class ModifyForm(FlaskForm):
	distance = IntegerField("distance (m):", validators=[NumberRange(min=1)])
	time = StringField("time:")

	class Meta:
		csrf = False

