from flask import Blueprint, current_app, render_template, flash, request, redirect, url_for, session
from booknet_app import db
from flask_login import login_user, login_required, logout_user, current_user
from booknet_app.users.forms import RegistrationForm, LoginForm, EditUserForm
from booknet_app.stores.forms import StoreForm
from booknet_app.bookshelves.forms import BookshelfForm
from booknet_app.models import User, Store, Bookshelf
from booknet_app.picture_handler import save_profile_picture

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
    
    if form.validate_on_submit() and request.method == 'POST':
        if form.profile_pic.data:
            picture_file = save_profile_picture(form.profile_pic.data)
            current_user.profile_picture = picture_file
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        
        db.session.commit()
        flash('Profil erfolgreich geändert!')
        
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_picture = url_for('static', filename='profile_pics/' + current_user.profile_picture)
    return render_template('users/account.html', form=form, profile_picture=profile_picture)

@users.route("/<username>/stores")
def user_stores(username):
    form = StoreForm()
    user = User.query.filter_by(username=username).first_or_404()
    stores = Store.query.filter_by(user=user).order_by(Store.storename.desc())
    return render_template('users/user_stores.html', stores=stores, user=user, form=form)

@users.route("/<username>/bookshelves")
def user_bookshelves(username):
    form = BookshelfForm()
    user = User.query.filter_by(username=username).first_or_404()
    bookshelves = Bookshelf.query.filter_by(user=user).order_by(Bookshelf.name.desc())
    return render_template('users/user_bookshelves.html', bookshelves=bookshelves, user=user, form=form)