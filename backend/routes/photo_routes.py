from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os
from services.ai_service import process_new_photo
from models.db import db

photo_bp = Blueprint('photos', __name__)
UPLOAD_FOLDER = 'data/uploads'

@photo_bp.route('/api/upload', methods=['POST'])
@jwt_required()
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Trigger AI Recognition (Milestone 3 Preview)
    # We call our AI service to get age, emotion, and faces
    ai_results = process_new_photo(filepath)

    return jsonify({
        "message": "Upload successful",
        "analysis": ai_results['analysis'] if ai_results else "No faces detected"
    }), 200