import os
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from models.db import db
from models.photo import Photo

photo_bp = Blueprint('photos', __name__)

@photo_bp.route('/api/photos/upload', methods=['POST'])
@jwt_required()
def upload_photo():
    current_user_id = get_jwt_identity()
    
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # 1. Validation & Storage
    filename = secure_filename(file.filename)
    unique_filename = f"u{current_user_id}_{filename}"
    save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
    file.save(save_path)

    # 2. Metadata Registration
    try:
        new_photo = Photo(
            filename=unique_filename,
            filepath=save_path,
            user_id=current_user_id
        )
        db.session.add(new_photo)
        db.session.commit()
        
        return jsonify({
            "message": "Photo metadata registered",
            "photo_id": new_photo.id,
            "url": unique_filename
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database registration failed"}), 500