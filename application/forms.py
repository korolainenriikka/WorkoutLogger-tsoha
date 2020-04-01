from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class ResultForm(FlaskForm):
    description = StringField("description", [validators.DataRequired()])

    class Meta:
        csrf = False

class ModifyForm(FlaskForm):
    newtext = StringField("edit description", [validators.DataRequired()])

    class Meta:
        csrf = False


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired()])
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    repeatPassword = PasswordField("Repeat password", [validators.DataRequired(), validators.equal_to("password")])

    class Meta:
        csrf = False