from services.ai_service import process_new_photo
import os

# Put any image file (jpg or png) in your backend folder and rename it to 'test.jpg'
# Or just use an absolute path to any photo on your computer
test_image = "test.jpg" 

if not os.path.exists(test_image):
    print(f"Please put a file named {test_image} in this folder to run the test!")
else:
    print("AI is starting. If this is the first time, it will download ~500MB of data. Please wait...")
    data = process_new_photo(test_image)
    if data:
        print("✅ AI Setup Successful!")
        print(f"Detected Age: {data['analysis'][0]['age']}")
        print(f"Dominant Emotion: {data['analysis'][0]['dominant_emotion']}")
    else:
        print("❌ AI Setup Failed. Check terminal errors.")