from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for, session
from booknet_app import db
from flask_login import login_user, login_required, logout_user, current_user
from booknet_app.users.forms import RegistrationForm, LoginForm, EditUserForm
from booknet_app.stores.forms import StoreForm
from booknet_app.bookshelves.forms import AddShelveForm
from booknet_app.models import User, Store, Bookshelf

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def user_login():

    form = LoginForm()
    
    if form.validate_on_submit() and request.method == "POST":

        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_passwort(form.passwort.data):
            login_user(user, remember=False)
            return redirect(url_for('books.book_search'))
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

@users.route('/account', methods=['GET', 'POST'])
def edit_user():
    
    form = EditUserForm()
    
    if form.validate_on_submit() and request.method == "POST":
    
        current_user.username = form.username.data
        current_user.email = form.email.data

        db.session.commit()
        
        flash('Profil erfolgreich geändert!')

    return render_template('users/account.html', form=form)

@users.route("/<username>/stores")
def user_stores(username):
    form = StoreForm()
    user = User.query.filter_by(username=username).first_or_404()
    stores = Store.query.filter_by(creator=user).order_by(Store.storename.desc())
    return render_template('users/user_stores.html', stores=stores, user=user, form=form)

@users.route("/<username>/bookshelves")
def user_bookshelves(username):
    form = AddShelveForm()
    user = User.query.filter_by(username=username).first_or_404()
    bookshelves = Bookshelf.query.filter_by(creator=user).order_by(Bookshelf.name.desc())
    return render_template('users/user_bookshelves.html', bookshelves=bookshelves, user=user, form=form)