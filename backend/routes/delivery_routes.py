from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.delivery import DeliveryHistory

delivery_bp = Blueprint('delivery', __name__)

@delivery_bp.route('/api/delivery/history', methods=['GET'])
@jwt_required()
def get_history():
    user_id = get_jwt_identity()
    history = DeliveryHistory.query.filter_by(user_id=user_id).all()
    
    output = []
    for item in history:
        output.append({
            "id": item.id,
            "method": item.method,
            "recipient": item.recipient,
            "status": item.status,
            "timestamp": item.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        })
        
    return jsonify(output), 200