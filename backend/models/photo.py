from .db import db
from datetime import datetime

class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    
    # AI labels (e.g., "Beach", "Wedding")
    tags = db.Column(db.Text) 

    # Relationship: A photo can have multiple detected faces
    faces = db.relationship('Face', backref='source_photo', lazy=True, cascade="all, delete-orphan")