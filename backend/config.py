import os
import logging
from sqlalchemy import create_engine

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    # Use environment variable or fallback to local SQLite
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///data/drishyamitra.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'drishyamitra-dev-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-dev-key')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data', 'uploads')

def init_db_engine():
    """
    Manual engine initialization to verify connection 
    and log the process as per project requirements.
    """
    uri = Config.SQLALCHEMY_DATABASE_URI
    try:
        engine = create_engine(uri)
        engine.connect()
        logger.info(f"✅ Successfully connected to database at: {uri}")
        return engine
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        return None