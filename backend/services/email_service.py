import smtplib
import os
import logging
import mimetypes
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def send_photo_email(recipient_email, subject, body_text, photo_path=None):
    """
    Composes and sends an email via Gmail SMTP.
    Handles dynamic body content and image attachments.
    """
    sender_email = os.getenv("GMAIL_EMAIL")
    sender_password = os.getenv("GMAIL_PASSWORD")

    if not sender_email or not sender_password:
        logger.error("❌ Email credentials missing in .env")
        return False, "Server configuration error"

    # 1. Compose Email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = f"Drishyamitra AI <{sender_email}>"
    msg['To'] = recipient_email
    msg.set_content(body_text)

    # 2. Handle Attachment (Requirement: fetch from storage directory)
    if photo_path:
        if not os.path.exists(photo_path):
            logger.error(f"❌ Photo not found: {photo_path}")
            return False, "Photo file not found on server"
        
        # Check file size (Requirement: handle oversized attachments)
        file_size = os.path.getsize(photo_path)
        if file_size > 20 * 1024 * 1024:  # 20MB Limit for Gmail
            return False, "File too large for email attachment"

        ctype, encoding = mimetypes.guess_type(photo_path)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)

        with open(photo_path, 'rb') as img:
            msg.add_attachment(
                img.read(),
                maintype=maintype,
                subtype=subtype,
                filename=os.path.basename(photo_path)
            )

    # 3. Secure Automated Delivery
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        logger.info(f"✅ Email successfully sent to {recipient_email}")
        return True, "Success"
    except smtplib.SMTPRecipientsRefused:
        return False, "Invalid recipient address"
    except smtplib.SMTPAuthenticationError:
        return False, "Authentication failed (Check App Password)"
    except Exception as e:
        logger.error(f"❌ SMTP Error: {str(e)}")
        return False, str(e)