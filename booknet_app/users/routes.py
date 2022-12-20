from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from booknet_app import db
from flask_login import login_user, login_required, logout_user
from booknet_app.users.forms import RegistrationForm, LoginForm
from booknet_app.models import User

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def user_login():

    form = LoginForm()
    
    if form.validate_on_submit() and request.method == "POST":

        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_passwort(form.passwort.data):
            login_user(user, remember=False)
            return redirect(url_for('books.all_books'))
        else:
            flash("Falsche Anmeldedaten!")
    
    return render_template('users/login.html', form=form)

@users.route('/signup', methods=['GET', 'POST'])
def signup_user():
    
    form = RegistrationForm()
    
    if form.validate_on_submit() and request.method == "POST":
        user = User(username=form.username.data, email=form.email.data, passwort=form.passwort.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Erfolgreich angemeldet')
        return redirect(url_for('users.user_login'))

    return render_template('users/signup.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))