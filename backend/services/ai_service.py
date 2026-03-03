from deepface import DeepFace
import os

def process_new_photo(image_path):
    """
    1. Detects faces using RetinaFace.
    2. Extracts features using Facenet512.
    3. Analyzes Age, Gender, and Emotions.
    """
    try:
        # This one line triggers the automatic download of models on first run
        results = DeepFace.analyze(
            img_path = image_path, 
            actions = ['age', 'gender', 'emotion'],
            detector_backend = 'retinaface', # Most accurate (as per your description)
            enforce_detection = False
        )
        
        # This part extracts the "Face Print" (Embeddings) for recognition
        embeddings = DeepFace.represent(
            img_path = image_path, 
            model_name = 'Facenet512', # High-dimensional model (as per your description)
            detector_backend = 'retinaface'
        )

        return {
            "analysis": results,
            "embeddings": embeddings
        }
    except Exception as e:
        print(f"DeepFace Error: {e}")
        return None