import requests
import os
import time
import logging

logger = logging.getLogger(__name__)

WHATSAPP_SERVICE_URL = "http://localhost:3001/send-photo"

def send_whatsapp_with_retry(phone_number, caption, photo_path, retries=2):
    """
    Sends photo to WhatsApp via Node microservice.
    Includes simple retry mechanism for robustness.
    """
    payload = {
        "phone": phone_number,
        "caption": caption,
        "imagePath": os.path.abspath(photo_path)
    }

    for attempt in range(retries + 1):
        try:
            response = requests.post(WHATSAPP_SERVICE_URL, json=payload, timeout=30)
            if response.status_code == 200:
                result = response.json()
                if result.get('success'):
                    return True, "Success"
            
            logger.warning(f"⚠️ WhatsApp attempt {attempt+1} failed: {response.text}")
            if attempt < retries:
                time.sleep(2) # Wait before retry
                
        except Exception as e:
            logger.error(f"❌ WhatsApp Service Connection Error: {str(e)}")
            if attempt < retries:
                time.sleep(2)

    return False, "Failed after retries"