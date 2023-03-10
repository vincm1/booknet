from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from booknet_app import db
from booknet_app.bookshelves.forms import BookshelfForm, ISBNForm
from booknet_app.models import Bookshelf
from booknet_app.models import User
from config import google_api_key, openai_key
### Google Books Api ### 
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

service = build('books', 'v1', developerKey=google_api_key)

bookshelves = Blueprint('bookshelves', __name__)

### API Google books Call function with multiple ISBNs  ###
def search_books_by_isbn(isbns):
        books = []
        # Call the Books API to search for multiple books by ISBN
        for isbn in isbns:
            try:
                print(isbn)
                result = service.volumes().list(
                    q=f"isbn:{isbn}",
                ).execute()

                books.append(result['items'])
            except HttpError as error:
                print(f'An error occurred: {error}')
        
        return books

@bookshelves.route('/add_bookshelf', methods=['GET', 'POST'])
@login_required
def add_bookshelf():

    form = BookshelfForm()

    if form.validate_on_submit() and request.method == 'POST':
        bookshelf = Bookshelf(name=form.name.data, beschreibung=form.beschreibung.data, isbns=[], user_id=current_user.id)
        db.session.add(bookshelf)
        db.session.commit()
        return redirect(url_for('users.user_bookshelves', username=current_user.username))

    return render_template('bookshelve/bookshelves.html',form=form)

@login_required
@bookshelves.route('/bookshelf/<int:bookshelf_id>', methods=['GET','POST'])
def bookshelf(bookshelf_id):
    bookshelf = Bookshelf.query.get_or_404(bookshelf_id)
    form = BookshelfForm()
    isbns = bookshelf.isbns
    books = search_books_by_isbn(isbns)
    return(render_template('bookshelves/bookshelf.html', bookshelf=bookshelf, bookeshelf_id=bookshelf.id, form=form, books=books, type_isbn=type(isbns)))

@login_required
@bookshelves.route('/bookshelf/<int:bookshelf_id>/edit', methods=['GET', 'POST'])
def edit_bookshelf(bookshelf_id):
    bookshelf = Bookshelf.query.get_or_404(bookshelf_id)

    if bookshelf.user_id != current_user.id:
        abort(403)

    form = BookshelfForm()

    if form.validate_on_submit() and request.method == "POST":
        bookshelf.name = form.name.data
        bookshelf.name = form.name.data
        bookshelf.isbns.append(form.isbns.data)
        db.session.commit()
        flash('Bookshelf erfolgreich geupdatet!')
        return(render_template('bookshelves/bookshelf.html', bookshelf=bookshelf, bookeshelf_id=bookshelf.id, form=form))
        

    elif request.method == "GET":
        form.name.data = bookshelf.name
        form.beschreibung.data = bookshelf.beschreibung

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


@login_required
@bookshelves.route('/add_isbn', methods=['POST'])
def add_isbn():
    form_3 = ISBNForm()
      
    user_bookshelves = db.session.query(Bookshelf.name).filter_by(user_id=current_user.id).all()
    choices = []
        
    for choice in user_bookshelves:
        choices.append(choice[0])
        
    form_3.bookshelf.choices = choices
    
    if form_3.validate_on_submit():
        
        bookshelf = db.session.query(Bookshelf).filter_by(name=form_3.bookshelf.data).first()
        isbn = str(form_3.isbn.data)
        print(bookshelf.isbns)
        bookshelf.isbns.append(isbn)
        print(bookshelf.isbns)
        db.session.commit()
        
        return redirect(url_for('users.user_bookshelves', username=current_user.username))

@login_required
@bookshelves.route('/delete_isbn', methods=['GET', 'POST'])
def delete_isbn(bookshelf_id):

    if form_validate_on_submit():
        
        
        print(bookshelf_id)
        #db.session.commit()
            
    return redirect(request.referrer)