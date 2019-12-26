from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import StringField, PasswordField, TextAreaField, SubmitField,DateField,IntegerField


class RegisterForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(), Length(min=4, max=40)])
    username = StringField("Username", validators=[DataRequired(), Length(max=10)])
    email = StringField("Email", validators=[Email("Invalid Email"), Length(max=80)])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm', message="Passwords Do Not Match")])
    confirm = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[Email("Invalid Email"), Length(max=80)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")


class DebtorCreationForm(FlaskForm):
    supplier_name=StringField("Name of Supplier",validators=[DataRequired(),Length(max=40)])
    date_supplied=DateField("Date",validators=[DataRequired()],format='%d-%m-%Y')
    amount=IntegerField("Amount",validators=[DataRequired()])
    