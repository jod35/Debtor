from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,Length,EqualTo
from wtforms import StringField,PasswordField,TextAreaField,SubmitField

class RegisterForm(FlaskForm):
    name=StringField("Full Name",validators=[DataRequired(),Length(min=4,max=40)])
    username=StringField("Username",validators=[DataRequired(),Length(max=10)])
    email=StringField("Email",validators=[Email("Invalid Email"),Length(max=80)])
    password=StringField("Password",validators=[DataRequired(),EqualTo('confirm',message="Passwords Do Not Match")])
    password=StringField("Password")
    submit=SubmitField("Sign Up")

