from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager, db, app
from .forms import LoginForm, RegisterForm
from .models import User
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/debtors', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        email = request.form.get('email')
        password_candidate = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.pass_hash, password_candidate):
            login_user(user)
            return redirect(url_for('user_dashboard'))
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
def user_dashboard():
    return render_template('lists.html')
