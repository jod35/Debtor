from flask import render_template,redirect,url_for,request
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager,db,app
from .forms import LoginForm,RegisterForm


@app.route('/debtors')
def index():
    form=LoginForm()
    return render_template('index.html',form=form)

@app.route('/debtors/signup')
def create_account():
    form=RegisterForm()
    return render_template('sign.html',form=form)

@app.route('/debtors/list')
def see_lists():
    return render_template('')