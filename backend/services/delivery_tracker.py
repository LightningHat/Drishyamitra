from models.db import db
from models.delivery import DeliveryHistory
import logging

logger = logging.getLogger(__name__)

def log_delivery_activity(user_id, photo_id, method, recipient, status):
    """
    Centralized delivery tracker service.
    Logs metadata such as medium, timestamp, and recipient details.
    """
    try:
        new_log = DeliveryHistory(
            user_id=user_id,
            photo_id=photo_id,
            method=method, # 'Email' or 'WhatsApp'
            recipient=recipient,
            status=status # 'Success' or 'Failed'
        )
        db.session.add(new_log)
        db.session.commit()
        logger.info(f"📊 Delivery Activity Logged: {method} to {recipient} [{status}]")
        return True
    except Exception as e:
        db.session.rollback()
        logger.error(f"❌ Failed to track delivery: {e}")
        return False