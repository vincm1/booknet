from booknet_app import db
from datetime import datetime

class User(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    passwort = db.Column(db.String)
    registration_date = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, passwort):
        self.name = name
        self.passwort = passwort
    
    def __repr__(self):
        f"User with {self.id} and {self.name} created on {self.registration_date}."