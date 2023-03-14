# Creating form login and register page
from .models import User_Login
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder: Username"})

    password = StringField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder: Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_username = User_Login.query.filter_by(
            username=username.data).first()
        if existing_username:
            raise ValidationError(
                'Username alreay existed. Please choose different name')


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder: Username"})

    password = StringField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={"placeholder: Password"})

    submit = SubmitField('Login')
