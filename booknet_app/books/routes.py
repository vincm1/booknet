from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from booknet_app import db
from booknet_app.books.forms import AddBookForm, SearchBookForm
from booknet_app.models import Book
from config import google_api_key
### Google Books Api ### 
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


books = Blueprint('books', __name__)

service = build('books', 'v1', developerKey=google_api_key)

def search_books(query, max_results=40, start_index=0):
        try:
            # Call the Books API to search for books
            results = service.volumes().list(
                q=query,
                maxResults=max_results,
                startIndex=start_index
            ).execute()
            # Print the results
            return results
           
        except HttpError as error:
            print(f'An error occurred: {error}')
# Search for books about Python programming
# search_books('python programming')

@books.route('/search', methods=['GET','POST'])
@login_required
def book_search():
    
    form = SearchBookForm()

    if form.validate_on_submit() and request.method == "POST":
    
        suchwort = form.suchwort.data
        results = search_books(suchwort)
        books = results['items']
         
        return render_template('books/search_book.html', form=form, results=results, books=books)

    return render_template('books/search_book.html', form=form)

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