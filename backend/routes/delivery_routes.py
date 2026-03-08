from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.db import db
from models.photo import Photo
from models.delivery import DeliveryHistory
from services.whatsapp_service import send_whatsapp_with_retry

delivery_bp = Blueprint('delivery', __name__)

@delivery_bp.route('/api/delivery/whatsapp', methods=['POST'])
@jwt_required()
def share_via_whatsapp():
    """
    Automated WhatsApp delivery handler.
    Logs success/failure to DeliveryHistory for relational integrity.
    """
    current_user_id = get_jwt_identity()
    data = request.get_json()

    photo_id = data.get('photo_id')
    phone = data.get('phone') # Format: 919876543210
    message = data.get('message', 'Sharing this memory with you via Drishyamitra!')

    if not photo_id or not phone:
        return jsonify({"error": "Photo ID and Phone Number required"}), 400

    # 1. Fetch photo metadata
    photo = Photo.query.filter_by(id=photo_id, user_id=current_user_id).first()
    if not photo:
        return jsonify({"error": "Photo not found"}), 404

    # 2. Trigger automated delivery
    success, status_msg = send_whatsapp_with_retry(
        phone_number=phone,
        caption=message,
        photo_path=photo.filepath
    )

    # 3. Update database with logs
    new_log = DeliveryHistory(
        user_id=current_user_id,
        photo_id=photo.id,
        method="WhatsApp",
        recipient=phone,
        status="Success" if success else "Failed"
    )
    
    try:
        db.session.add(new_log)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Logging failed: {str(e)}"}), 500

    if success:
        return jsonify({"message": "WhatsApp message delivered", "log_id": new_log.id}), 200
    else:
        return jsonify({"error": f"WhatsApp delivery failed: {status_msg}"}), 500