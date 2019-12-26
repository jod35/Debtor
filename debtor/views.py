from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager, db, app
from .forms import LoginForm, RegisterForm
from .models import User


@app.route('/debtors')
def index():
    form = LoginForm()
    return render_template('index.html', form=form)


@app.route('/debtors/signup', methods=['GET', 'POST'])
def create_account():

    form = RegisterForm()

    if form.validate_on_submit():
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        pass_hash = request.form.get('password')

        args = {
            'name': name,
            'username': username,
            'email': email,
            'pass_hash': generate_password_hash(pass_hash)
        }

        new_user = User(**args)
        db.session.add(new_user)
        db.session.commit()
        flash("User Account Created Successfully!!")
        return redirect(url_for('create_account'))

    return render_template('sign.html', form=form)


@app.route('/debtors/list')
def see_lists():
    return render_template('')
