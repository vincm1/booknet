from booknet_app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    passwort_hash = db.Column(db.String, nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.now)

    stores = db.relationship('Store', backref='creator', lazy=True)
    bookshelves = db.relationship('Bücherregale', backref='user', lazy=True)

    def __init__(self, username, email, passwort):
        self.username = username
        self.email = email
        self.passwort_hash = generate_password_hash(passwort)
    
    def check_passwort(self,passwort):
        return check_password_hash(self.passwort_hash,passwort)
    
    def __repr__(self):
        f"User with {self.id} and {self.username} {self.email} {self.passwort_hash} created on {self.registration_date}."
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

class Buchregal(db.Model):

    __tablename__ = "buchregale"

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(300), nullable=False)

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
    
    def __repr__(self):
        f"Buchregal von {self.user_id} name: {self.name}"
class Store(db.Model):

    __tablename__ = 'stores'

    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    storename = db.Column(db.String(300), unique=True, nullable=False)
    adresse = db.Column(db.String(), nullable=False)
    beschreibung = db.Column(db.Text())

    def __init__(self, storename, adresse, beschreibung, user_id):
        self.storename = storename
        self.adresse = adresse 
        self.beschreibung = beschreibung
        self.user_id = user_id
    
    def __repr__(self):
        f"{self.storename} mit ID: {self.id} wurde von user:{self.user_id} angelegt."