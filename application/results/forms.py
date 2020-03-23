from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ResultForm(FlaskForm):
    description = StringField("description", [validators.DataRequired()])

    class Meta:
        csrf = False

class ModifyForm(FlaskForm):
    newtext = StringField("edit description", [validators.DataRequired()])

    class Meta:
        csrf = False
