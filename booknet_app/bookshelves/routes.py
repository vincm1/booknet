from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from booknet_app import db
from booknet_app.bookshelves.forms import AddShelveForm
from booknet_app.models import Bookshelf

bookshelves = Blueprint('bookshelves', __name__)

@bookshelves.route('/add_bookshelf', methods=['GET', 'POST'])
@login_required
def add_bookshelf():

    form = AddShelveForm()

    if form.validate_on_submit() and request.method == 'POST':
        bookshelf = Bookshelf(name=form.name.data, user_id=current_user.id)
        db.session.add(bookshelf)
        db.session.commit()
        return redirect(url_for('users.user_bookshelves'))

    return render_template('bookshelve/bookshelves.html',form=form)
