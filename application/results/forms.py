from flask_wtf import FlaskForm
from wtforms import StringField

class ResultForm(FlaskForm):
    description = StringField("description")

class ModifyForm(FlaskForm):
    newtext = StringField("edit description")

    class Meta:
        csrf = False
