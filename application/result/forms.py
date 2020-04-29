from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import NumberRange, Length

class RunSessionForm(FlaskForm):
	rounds = IntegerField(validators=[NumberRange(min=1, max=15)], render_kw={"placeholder": "rounds"})
	distance = IntegerField(validators=[NumberRange(min=1, max=100000)], render_kw={"placeholder": "distance in m"})

	class Meta:
		csrf = False

class StrengthSessionForm(FlaskForm):
	workout = StringField(validators=[Length(min=3, max=30)], render_kw={"placeholder":"workout"})
	sets = IntegerField(validators=[NumberRange(min=1, max=15)], render_kw={"placeholder": "sets"})
	reps = IntegerField(validators=[NumberRange(min=1, max=50)], render_kw={"placeholder": "repetitions"})

	class Meta:
		csrf = False

class ModifyConditioningForm(FlaskForm):
	distance = IntegerField("distance (m)", validators=[NumberRange(min=1, max=100000)])
	time = StringField("time")

	class Meta:
		csrf = False

class ModifyStrengthForm(FlaskForm):
	reps = IntegerField("reps", validators=[NumberRange(min=1, max=15)])
	weight = IntegerField("weight", validators=[NumberRange(min=1, max=300)])

	class Meta:
		csrf = False

