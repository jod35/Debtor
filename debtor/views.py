from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager, db, app
from .forms import LoginForm, RegisterForm,DebtorCreationForm
from .models import User,Debt
from flask_login import login_user, logout_user, current_user, login_required
from datetime import date

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


@app.route('/debtors/dashboard')
def user_dashboard():
    return render_template('lists.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/debtors/add',methods=['GET', 'POST'])
def add_debts():
    form=DebtorCreationForm()
    today=date.today()

    if request.method == 'POST':
        args={
            'supplier_name':request.form.get('s_name'),
            'date_supplied':request.form.get('date_supplied'),
            'amount_paid':request.form.get('amount_paid'),
            'debt_amount':request.form.get('debt_amount'),
            'cleared':False,
            'balance':(int(request.form.get('debt_amount'))-int(request.form.get('amount_paid')))
        }

        new_debt=Debt(**args)
        db.session.add(new_debt)
        db.session.commit()
        flash("Record Has Been Saved Successfully")
        return redirect(url_for('add_debts'))
    return render_template('adddebt.html',form=form,today=today)

@app.route('/debtors/lists')
def view_debts():
    
    context={
        'debts':Debt.query.all()
    }
    return render_template('debts.html',**context)

#render the update template
@app.route('/debtors/details/debt_<int:debt_id>')
def debt_details(debt_id):
    

    context={
        'debt_to_update':Debt.query.get_or_404(debt_id)
    }
    return render_template('details.html',**context)

#update a record basing on its id
@app.route('/update/<int:id>',methods=['POST'])
def update_record(id):
    record_to_update=Debt.query.get_or_404(id)
    record_to_update.supplier_name = request.form.get('s_name')
    record_to_update.date_supplied=request.form.get('date_supplied')
    record_to_update.debt_amount=request.form.get('debt_amount')
    record_to_update.amount_paid=request.form.get('amount_paid')
    record_to_update.balance=(int(request.form.get('debt_amount'))-int(request.form.get('amount_paid')))

    db.session.commit()
    return redirect(url_for('view_debts'))

#delete a record basing on the ID
@app.route('/delete/<int:id>',methods=['GET', 'POST'])
def delete(id):
    debt_to_delete=Debt.query.get_or_404(id)
    db.session.delete(debt_to_delete)
    db.session.commit()
    return redirect(url_for('view_debts'))

    
@app.route('/cleared/<int:id>',methods=['POST'])
def set_to_cleared(id):
    debt_cleared=Debt.query.get_or_404(id)
    debt_cleared.cleared =True

    db.session.commit()
    return redirect(url_for('view_debts'))