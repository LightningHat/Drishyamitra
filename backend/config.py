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
    
    # Requirement: Token expiration and refresh policies
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)
    
    # --- Upload Settings ---
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB limit

def init_db_engine():
    """
    Initializes the SQLAlchemy engine manually to verify connection 
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