from datetime import datetime
from booknet_app import db, login_manager
from sqlalchemy import JSON
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.ext.mutable import MutableList

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    passwort_hash = db.Column(db.String, nullable=False)
    profile_picture = db.Column(db.String, nullable=True, default="default_profile_picture.png")
    registration_date = db.Column(db.DateTime, default=datetime.now)

    stores = db.relationship("Store", backref="user", lazy=True)
    bookshelves = db.relationship("Bookshelf", backref="user", lazy=True)

    def __init__(self, username, email, passwort):
        self.username = username
        self.email = email
        self.passwort_hash = generate_password_hash(passwort)
        
    def check_passwort(self, passwort):
        return check_password_hash(self.passwort_hash, passwort)

    def __repr__(self):
        f"User with {self.id} and {self.username} {self.email}."

class Bookshelf(db.Model):

    __tablename__ = "bookshelves"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(300), nullable=False)
    beschreibung = db.Column(db.Text(), nullable=True)
    isbns = db.Column(MutableList.as_mutable(JSON), nullable=True)

    def __init__(self, user_id, name, beschreibung, isbns):
        self.user_id = user_id
        self.name = name
        self.beschreibung = beschreibung
        self.isbns = isbns 
        
    def __repr__(self):
        f"Buchregal von {self.user_id} name: {self.name}"
        
class Store(db.Model):

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    storename = db.Column(db.String(300), unique=True, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    store_bild = db.Column(db.String, nullable=True, default="book_store.jpg")
    seats = db.Column(db.Integer, nullable=False)
    adresse = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    beschreibung = db.Column(db.Text())
    creation_date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, storename, category, store_bild, seats, adresse, city, beschreibung, user_id):
        self.storename = storename
        self.store_bild = store_bild
        self.adresse = adresse
        self.beschreibung = beschreibung
        self.category = category
        self.seats = seats
        self.city = city
        self.user_id = user_id

    def __repr__(self):
        f"{self.storename} mit ID: {self.id} wurde von user:{self.user_id} angelegt."