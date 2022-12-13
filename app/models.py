from datetime import datetime
from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True, unique=True)
    last_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    phone = db.Column(db.String(32), index=True, unique=True)
    body = db.Column(db.String(1000), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) 

    def __repr__(self):
        return '<Contact {} {}>'.format(self.first_name, self.last_name)
