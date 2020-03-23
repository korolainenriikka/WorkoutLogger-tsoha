from flask_wtf import FlaskForm
from wtforms import StringField

class ResultForm(FlaskForm):
    description = StringField("description")

    class Meta:
        csrf = False