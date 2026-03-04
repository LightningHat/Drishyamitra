from .db import db
from datetime import datetime
from passlib.hash import bcrypt

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    # Role-based access control (user, photographer, admin)
    role = db.Column(db.String(20), default='user') 
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relational Integrity: Cascading deletes
    photos = db.relationship('Photo', backref='owner', lazy=True, cascade="all, delete-orphan")
    people = db.relationship('Person', backref='created_by', lazy=True)

    def set_password(self, password):
        """Hashes password using bcrypt before storing."""
        self.password_hash = bcrypt.hash(password)

    def check_password(self, password):
        """Verifies provided password against the stored hash."""
        return bcrypt.verify(password, self.password_hash)

    def __repr__(self):
        return f'<User {self.username}>'