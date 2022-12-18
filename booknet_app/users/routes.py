from flask import Flask, Blueprint, render_template, flash, request
from booknet_app import db
from booknet_app.users.forms import RegistrationForm
from booknet_app.models import User

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login_user():
    return render_template('users/login.html')

@users.route('/signup', methods=['GET', 'POST'])
def signup_user():
    
    form = RegistrationForm()
    
    if form.validate_on_submit() and request.method == "POST":
        user = User(username=form.username.data, email=form.email.data, passwort=form.passwort.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Erfolgreich angemeldet')
        
    return render_template('users/signup.html', form=form)