from flask_wtf import FlaskForm
from wtforms import Form, FieldList, PasswordField, validators, ValidationError, StringField, FormField

from application.models import User


#class ResultForm(FlaskForm):
#    description = StringField("description", [validators.DataRequired()])
#
#    class Meta:
#        csrf = False

class SessionForm(Form):
    result1 = StringField("description", [validators.DataRequired()])
    result2 = StringField("description", [validators.DataRequired()])
    result3 = StringField("description", [validators.DataRequired()])

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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    class Meta:
        csrf = False