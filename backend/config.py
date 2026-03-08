import os
import logging
import datetime
from sqlalchemy import create_engine

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    # --- Database Settings ---
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///data/drishyamitra.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # --- Security & JWT Settings ---
    SECRET_KEY = os.getenv('SECRET_KEY', 'drishyamitra-dev-key-7788')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-super-secret-key-9900')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)
    
    # --- Celery & Redis Settings ---
    # Requirement: Redis for message brokering
    CELERY_BROKER_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    RESULT_BACKEND = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # --- Storage Settings ---
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limit

def init_db_engine():
    """Manual engine initialization for logging verification."""
    uri = Config.SQLALCHEMY_DATABASE_URI
    try:
        engine = create_engine(uri)
        engine.connect()
        logger.info(f"✅ Successfully connected to database at: {uri}")
        return engine
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        return None