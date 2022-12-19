from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from booknet_app import db
from booknet_app.books.forms import AddBookForm
from booknet_app.models import Book


books = Blueprint('books', __name__)

@books.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    
    form = AddBookForm()

    if form.validate_on_submit() and request.method == "POST":
        book = Book(titel=form.titel.data, author=form.author.data, isbn=form.isbn.data, user_id=current_user.id)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books.all_books'))

    return render_template('books/add_book.html', form=form)

@books.route('/all_books', methods=['GET'])
@login_required
def all_books():
    
    books = db.session.query(Book).all()

    return render_template("books/all_books.html", books=books)