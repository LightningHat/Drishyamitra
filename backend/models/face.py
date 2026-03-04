from .db import db
import json

class Face(db.Model):
    __tablename__ = 'faces'
    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey('photos.id'), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True) # Null if unknown
    
    # Bounding box: [top, right, bottom, left]
    location_data = db.Column(db.Text, nullable=False) 
    
    # 512-dimension vector stored as a JSON string or Pickle
    embedding = db.Column(db.JSON, nullable=False) 
    
    # AI Attributes
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    emotion = db.Column(db.String(20))