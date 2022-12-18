from booknet_app import db
from datetime import datetime

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    passwort = db.Column(db.String(15), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, email, passwort):
        self.username = username
        self.email = email
        self.passwort = passwort
    
    def __repr__(self):
        f"User with {self.id} and {self.username} {self.email} {self.passwort} created on {self.registration_date}."

class Book(db.Model):

    __tablename__ = 'books'

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    titel = db.Column(db.String(300), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.Integer)

    def __init__(self, titel, author, isbn, user_id):
        self.titel = titel
        self.author = author 
        self.isbn = isbn
        self.user_id = user_id
    
    def __repr__(self):
        f"Buch mit ID: {self.id} und Titel {self.titel} wurde von user:{self.user_id} angelegt."