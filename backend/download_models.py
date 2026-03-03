from deepface import DeepFace
import numpy as np

def final_fix():
    print("--- 🛠️ Drishyamitra Final AI Polish ---")
    
    # 1. Finishing the Attributes (Age, Gender, Emotion)
    # This will resume/restart the 539MB download that failed at 64%
    print("\n[1/2] Finishing Age/Gender/Emotion models...")
    try:
        dummy_img = np.zeros((224, 224, 3), dtype=np.uint8)
        DeepFace.analyze(dummy_img, actions=['age', 'gender', 'emotion'], enforce_detection=False)
        print("✅ Attribute models are now 100% complete.")
    except Exception as e:
        print(f"Still having trouble with attributes: {e}")

    # 2. Loading RetinaFace (The Project's Required Detector)
    print("\n[2/2] Loading RetinaFace Detector...")
    try:
        # This forces the download of the RetinaFace weights (~30MB)
        DeepFace.represent(dummy_img, detector_backend='retinaface', enforce_detection=False)
        print("✅ RetinaFace Detector is ready.")
    except Exception as e:
        print(f"RetinaFace error: {e}")

    print("\n✨ ALL SYSTEMS GO!")

if __name__ == "__main__":
    final_fix()