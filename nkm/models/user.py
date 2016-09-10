import hashlib
from nkm import db


class User(db.Model):
    """User Model Class"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String, unique=True)
    phash = db.Column(db.String)

    def hash_password(self, password):
        """Hashes a string using sha224"""
        return hashlib.sha224(password).hexdigest()
