from .db import db
from datetime import datetime

class DeliveryHistory(db.Model):
    __tablename__ = 'delivery_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('photos.id'), nullable=False)
    method = db.Column(db.String(20)) # 'Email' or 'WhatsApp'
    recipient = db.Column(db.String(100))
    status = db.Column(db.String(20)) # 'Success' or 'Failed'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)