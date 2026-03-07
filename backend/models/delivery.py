from .db import db
from datetime import datetime

class DeliveryHistory(db.Model):
    __tablename__ = 'delivery_history'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('photos.id'), nullable=False)
    
    method = db.Column(db.String(20), nullable=False) # 'Email' or 'WhatsApp'
    recipient = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False) # 'Success' or 'Failed'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Delivery {self.method} to {self.recipient}>'