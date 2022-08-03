from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import (
    StringField, PasswordField,
    BooleanField, FileField,
    TextAreaField, SubmitField
    )



class LoginUser(FlaskForm):
    name = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Enter')