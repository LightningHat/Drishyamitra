from models.face import Face
from models.person import Person
from services.ai_service import calculate_similarity
import logging

logger = logging.getLogger(__name__)

def identify_face(new_embedding, user_id, threshold=0.4):
    """
    Matches a new embedding against existing faces in the database for a specific user.
    Returns Person object if matched, else None.
    """
    # 1. Fetch all known faces for this user from the database
    # (In a real production app, we would use a Vector DB like Pinecone here)
    known_faces = Face.query.join(Person).filter(Person.user_id == user_id).all()
    
    best_match = None
    highest_score = 0

    for face in known_faces:
        score = calculate_similarity(new_embedding, face.embedding)
        if score > threshold and score > highest_score:
            highest_score = score
            best_match = face.identity # The 'Person' linked to this face

    if best_match:
        logger.info(f"✅ Match Found: {best_match.name} (Score: {highest_score:.2f})")
    else:
        logger.info("👤 No match found. This is a new individual.")

    return best_match