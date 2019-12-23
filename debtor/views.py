from flask import render_template,redirect,url_for,request
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager,db,app

@app.route('/debtors')
def index():
    return render_template('index.html')