import os
import logging
from deepface import DeepFace
import numpy as np

# Configure AI Logger
logger = logging.getLogger(__name__)

def process_image_pipeline(image_path):
    """
    Executes the DeepFace Pipeline:
    1. Detection: RetinaFace (Robust under angles/lighting)
    2. Alignment: MTCNN (Landmark extraction)
    3. Representation: Facenet512 (Numerical vector encoding)
    """
    try:
        logger.info(f"🧠 AI Pipeline started for: {image_path}")
        
        # We use represent() because it combines detection, alignment, and encoding in one pass
        results = DeepFace.represent(
            img_path=image_path,
            model_name='Facenet512',
            detector_backend='retinaface', # Per requirements: RetinaFace detection
            enforce_detection=False,
            align=True # This internalizes MTCNN landmark alignment
        )

        # Also get attributes (Age, Gender, Emotion) for better tagging
        analysis = DeepFace.analyze(
            img_path=image_path,
            actions=['age', 'gender', 'emotion'],
            detector_backend='retinaface',
            enforce_detection=False,
            silent=True
        )

        return {
            "faces": results,    # Contains 'embedding' and 'facial_area'
            "analysis": analysis # Contains 'age', 'dominant_gender', 'dominant_emotion'
        }

    except Exception as e:
        logger.error(f"❌ Pipeline Error: {str(e)}")
        return None

def calculate_similarity(embedding1, embedding2):
    """
    Uses Cosine Similarity to match faces.
    Values closer to 1.0 mean the faces are more identical.
    """
    a = np.array(embedding1)
    b = np.array(embedding2)
    distance = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return distance