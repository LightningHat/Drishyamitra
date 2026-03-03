import requests
import os

WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL", "http://localhost:3001")

def send_whatsapp_photo(phone_number, caption, photo_path):
    """
    Sends a request to the Node.js WhatsApp service.
    Phone number format: '919876543210' (Country code + Number)
    """
    payload = {
        "phone": phone_number,
        "caption": caption,
        "imagePath": os.path.abspath(photo_path) # Absolute path is required
    }
    
    try:
        response = requests.post(f"{WHATSAPP_API_URL}/send-image", json=payload)
        return response.json()
    except Exception as e:
        print(f"WhatsApp API Error: {e}")
        return {"success": False, "error": str(e)}