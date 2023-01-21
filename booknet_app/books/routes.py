import json
from random import randint
from flask import Flask, Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from booknet_app import db
from booknet_app.books.forms import SearchBookForm, ChatForm
from booknet_app.models import Book
from config import google_api_key, openai_key
### Google Books Api ### 
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
### Openai ###
import openai

books = Blueprint('books', __name__)

service = build('books', 'v1', developerKey=google_api_key)

openai.api_key = openai_key
model_engine = "text-davinci-003" 

### API Call functions ###
def search_books(query, max_results=randint(1,40), start_index=0):
    try:
            # Call the Books API to search for books
        results = service.volumes().list(
            q=query,
            maxResults=max_results,
            startIndex=start_index
        ).execute()
            # Print the results
            
        return results["items"]
           
    except HttpError as error:
            print(f'An error occurred: {error}')
# Search for books about Python programming
# search_books('python programming')

def openai_chat(prompt):
    completion = openai.Completion.create( 
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.9,
    )
    return completion


@books.route('/search', methods=['GET','POST'])
@login_required
def book_search():
    
    form = SearchBookForm()
    form_2 = ChatForm()
    
    if form.validate_on_submit():
            
        print(form.submit.data)
        suchwort = form.suchwort.data
        books = search_books(suchwort)
            
        book_list = {}
            
        for book in books:
            book_id = book['id']
            book_list[book_id] = book
        
        return render_template('books/search_book.html', form=form, form_2=form_2, books=books, book_list=book_list, search_findings=len(book_list))
    
    if form_2.validate_on_submit():
        prompt = form_2.prompt.data
        result = openai_chat(prompt)
        
        return render_template('books/search_book.html', form_2=form_2, form=form, result=result.choices[0].text, collapsable_open=True)
    
    return render_template('books/search_book.html', form=form, form_2=form_2)

@books.route('/chat', methods=['GET','POST'])
@login_required
def chat():
    
    form = SearchBookForm()
    form_2 = ChatForm()
    
    if form_2.validate_on_submit() and request.method == "POST":
        prompt = form_2.prompt.data
        response = openai_chat(prompt)

        return reditec("books/search_book.html", form=form, form_2=form_2, result=response.choices[0].text)
    
    result = result.args.get("response")
    return render_template("books/search_book.html", result=result)