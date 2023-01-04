from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from booknet_app import db
from booknet_app.bookshelves.forms import BookshelfForm
from booknet_app.models import Bookshelf
from booknet_app.models import User

bookshelves = Blueprint('bookshelves', __name__)

@bookshelves.route('/add_bookshelf', methods=['GET', 'POST'])
@login_required
def add_bookshelf():

    form = BookshelfForm()

    if form.validate_on_submit() and request.method == 'POST':
        bookshelf = Bookshelf(name=form.name.data, user_id=current_user.id)
        db.session.add(bookshelf)
        db.session.commit()
        return redirect(url_for('users.user_bookshelves', username=current_user.username))

    return render_template('bookshelve/bookshelves.html',form=form)

@login_required
@bookshelves.route('/bookshelf/<int:bookshelf_id>', methods=['GET','POST'])
def bookshelf(bookshelf_id):
    bookshelf = Bookshelf.query.get_or_404(bookshelf_id)
    form = BookshelfForm()
    return(render_template('bookshelves/bookshelf.html', bookshelf=bookshelf, bookeshelf_id=bookshelf.id, form=form))

@login_required
@bookshelves.route('/bookshelf/<int:bookshelf_id>/edit', methods=['GET', 'POST'])
def edit_bookshelf(bookshelf_id):
    bookshelf = Bookshelf.query.get_or_404(bookshelf_id)

    if bookshelf.user_id != current_user.id:
        abort(403)

    form = BookshelfForm()

    if form.validate_on_submit() and request.method == "POST":
        bookshelf.name = form.name.data
        db.session.commit()
        flash('Bookshelf erfolgreich geupdatet!')
        return(render_template('bookshelves/bookshelf.html', bookshelf=bookshelf, bookeshelf_id=bookshelf.id, form=form))
        

    elif request.method == "GET":
        form.name.data = bookshelf.name

    return render_template('bookshelves/bookshelf.html', form=form)

@login_required
@bookshelves.route('/bookshelf/<int:bookshelf_id>/delete', methods=['POST'])
def delete_bookshelf(bookshelf_id):
    bookshelf = Bookshelf.query.get_or_404(bookshelf_id)

    if bookshelf.user_id != current_user.id:
        abort(403)
    
    db.session.delete(bookshelf)
    db.session.commit()

    flash("Bookshelf deleted!")
    
    return redirect(url_for('users.user_bookshelves', username=current_user.username))