from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.db import db
from models.photo import Photo
from models.delivery import DeliveryHistory
from services.email_service import send_photo_email
import logging

delivery_bp = Blueprint('delivery', __name__)
logger = logging.getLogger(__name__)

@delivery_bp.route('/api/delivery/email', methods=['POST'])
@jwt_required()
def share_via_email():
    """
    Endpoint to share a photo via email.
    Logs every transaction in DeliveryHistory.
    """
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    photo_id = data.get('photo_id')
    recipient = data.get('recipient')
    subject = data.get('subject', 'Shared Photo from Drishyamitra')
    message = data.get('message', 'Hello, please see the attached photo.')

    # 1. Validation
    if not photo_id or not recipient:
        return jsonify({"error": "Missing photo_id or recipient"}), 400

    photo = Photo.query.filter_by(id=photo_id, user_id=current_user_id).first()
    if not photo:
        return jsonify({"error": "Photo not found"}), 404

    # 2. Trigger Email Service
    success, status_msg = send_photo_email(
        recipient_email=recipient,
        subject=subject,
        body_text=message,
        photo_path=photo.filepath
    )

    # 3. Requirement: Log transaction in DeliveryHistory model
    try:
        new_log = DeliveryHistory(
            user_id=current_user_id,
            photo_id=photo.id,
            method="Email",
            recipient=recipient,
            status="Success" if success else "Failed"
        )
        db.session.add(new_log)
        db.session.commit()
    except Exception as e:
        logger.error(f"❌ Database Logging Error: {e}")

    if success:
        return jsonify({"message": "Email delivered successfully"}), 200
    else:
        return jsonify({"error": f"Delivery failed: {status_msg}"}), 500