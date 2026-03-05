from .db import db

class Face(db.Model):
    __tablename__ = 'faces'
    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey('photos.id'), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)
    
    # Store the 512 numbers as a JSON array
    embedding = db.Column(db.JSON, nullable=False) 
    location_data = db.Column(db.Text, nullable=False)
    
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    emotion = db.Column(db.String(20))