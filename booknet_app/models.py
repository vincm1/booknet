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
        self.name = username
        self.email = email
        self.passwort = passwort
    
    def __repr__(self):
        f"User with {self.id} and {self.name} created on {self.registration_date}."
    
    def create_user():
        pass