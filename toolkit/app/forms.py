from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is already taken. Please choose a different username.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email address is already taken. Please choose a different email address.")

class PostForm(FlaskForm):
    post = TextAreaField("Say something", validators = [DataRequired(), Length(min=1, max=1400)])
    submit = SubmitField("Submit")