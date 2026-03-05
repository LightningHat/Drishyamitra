from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.db import db
from models.photo import Photo
from models.face import Face
from models.person import Person
from services.ai_service import process_image_pipeline
from services.recognition_service import identify_face
import json

face_bp = Blueprint('faces', __name__)

@face_bp.route('/api/faces/process/<int:photo_id>', methods=['POST'])
@jwt_required()
def process_faces(photo_id):
    current_user_id = get_jwt_identity()
    photo = Photo.query.filter_by(id=photo_id, user_id=current_user_id).first_or_404()

    # 1. Execute DeepFace Pipeline
    ai_data = process_image_pipeline(photo.filepath)
    if not ai_data:
        return jsonify({"error": "AI processing failed"}), 500

    results = []
    
    # 2. Loop through every face detected in the photo
    for i, face_obj in enumerate(ai_data['faces']):
        embedding = face_obj['embedding']
        area = face_obj['facial_area'] # [x, y, w, h]
        
        # Try to identify the person
        matched_person = identify_face(embedding, current_user_id)
        
        # 3. Create Face record
        new_face = Face(
            photo_id=photo.id,
            location_data=json.dumps(area),
            embedding=embedding,
            age=ai_data['analysis'][i]['age'],
            gender=ai_data['analysis'][i]['dominant_gender'],
            emotion=ai_data['analysis'][i]['dominant_emotion'],
            person_id=matched_person.id if matched_person else None
        )
        db.session.add(new_face)
        
        results.append({
            "face_id": i,
            "identified_as": matched_person.name if matched_person else "Unknown",
            "age": new_face.age,
            "emotion": new_face.emotion
        })

    db.session.commit()
    return jsonify({
        "message": f"Detected {len(results)} faces.",
        "details": results
    }), 200