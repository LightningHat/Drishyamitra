from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models.db import db
from models.photo import Photo
from models.face import Face
from services.ai_service import process_new_photo
import json

face_bp = Blueprint('faces', __name__)

@face_bp.route('/api/faces/process/<int:photo_id>', methods=['POST'])
@jwt_required()
def detect_faces(photo_id):
    photo = Photo.query.get_or_404(photo_id)
    
    # 1. Trigger AI Detection Service
    ai_results = process_new_photo(photo.filepath)
    
    if not ai_results:
        return jsonify({"message": "No faces detected"}), 200

    # 2. Store Embedding Vectors in DB
    detected_faces_count = 0
    for face_data in ai_results['analysis']:
        # Extract location and embedding
        region = face_data['region'] # [x, y, w, h]
        
        new_face = Face(
            photo_id=photo.id,
            location_data=json.dumps(region),
            embedding=ai_results['embeddings'][detected_faces_count]['embedding'],
            age=face_data['age'],
            gender=face_data['dominant_gender'],
            emotion=face_data['dominant_emotion']
        )
        db.session.add(new_face)
        detected_faces_count += 1
    
    db.session.commit()
    return jsonify({
        "message": f"Processed {detected_faces_count} faces",
        "faces": ai_results['analysis']
    }), 200