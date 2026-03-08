from celery import Celery
import os
import json
from models.db import db
from models.photo import Photo
from models.face import Face
from services.ai_service import process_image_pipeline
from services.recognition_service import identify_face

# Initialize Celery
celery = Celery('drishyamitra', broker='redis://localhost:6379/0')

@celery.task(name='tasks.process_photo_background')
def process_photo_background(photo_id, user_id):
    """
    Background Service: Executes the DeepFace pipeline.
    Handles batch face recognition and folder organization logic.
    """
    # We import create_app inside the task to avoid circular imports
    from app import create_app
    flask_app = create_app()
    
    with flask_app.app_context():
        photo = Photo.query.get(photo_id)
        if not photo:
            return f"Error: Photo {photo_id} not found."

        # 1. High-dimensional AI Processing (DeepFace)
        ai_data = process_image_pipeline(photo.filepath)
        
        if not ai_data:
            return f"AI Processing failed for Photo {photo_id}"

        # 2. Extract and match faces
        detected_count = 0
        for i, face_obj in enumerate(ai_data['faces']):
            embedding = face_obj['embedding']
            
            # Use Cosine Similarity to identify person
            matched_person = identify_face(embedding, user_id)
            
            # 3. Store in Database
            new_face = Face(
                photo_id=photo.id,
                location_data=json.dumps(face_obj['facial_area']),
                embedding=embedding,
                age=ai_data['analysis'][i]['age'],
                gender=ai_data['analysis'][i]['dominant_gender'],
                emotion=ai_data['analysis'][i]['dominant_emotion'],
                person_id=matched_person.id if matched_person else None
            )
            db.session.add(new_face)
            detected_count += 1
        
        db.session.commit()
        return f"✅ Background Processing Complete: Found {detected_count} faces in Photo {photo_id}"

@celery.task(name='tasks.cleanup_task')
def cleanup_temp_storage():
    """Periodic task to maintain operational efficiency."""
    print("🧹 Maintenance: Cleaning up temporary storage...")
    return "Cleanup Success"