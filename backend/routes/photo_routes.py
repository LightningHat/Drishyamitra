import os
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from models.db import db
from models.photo import Photo
from tasks import process_photo_background

photo_bp = Blueprint('photos', __name__)

@photo_bp.route('/api/photos/upload', methods=['POST'])
@jwt_required()
def upload_photo():
    """
    Handles bulk photo uploads and triggers background AI recognition.
    Returns 202 Accepted to ensure non-blocking user interaction.
    """
    current_user_id = get_jwt_identity()
    
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # 1. Secure File Saving
    filename = secure_filename(file.filename)
    unique_filename = f"user_{current_user_id}_{filename}"
    save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(save_path)

    try:
        # 2. Register Metadata in SQL
        new_photo = Photo(
            filename=unique_filename,
            filepath=save_path,
            user_id=current_user_id
        )
        db.session.add(new_photo)
        db.session.commit()
        
        # 3. REQUIREMENT: Trigger Background AI Service (Asynchronous)
        # .delay() sends the task to Redis/Celery queue
        process_photo_background.delay(new_photo.id, current_user_id)

        return jsonify({
            "message": "Upload successful. AI processing started in background.",
            "photo_id": new_photo.id,
            "status": "processing"
        }), 202 

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Upload failed: {str(e)}"}), 500