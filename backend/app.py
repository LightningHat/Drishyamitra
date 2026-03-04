import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv

# Import the Database instance and Configuration
from config import Config, init_db_engine
from models.db import db

# IMPORTANT: Import all models here so Flask-Migrate (Alembic) can see them
from models.user import User
from models.photo import Photo
from models.face import Face
from models.person import Person
from models.delivery import DeliveryHistory

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # 1. Initialize Extensions
    CORS(app)
    db.init_app(app)
    migrate = Migrate(app, db) # This enables the 'flask db' commands
    jwt = JWTManager(app)

    # 2. Register Blueprints with Safety Checks
    # This prevents the app from crashing if you haven't created the route files yet
    try:
        from routes.auth_routes import auth_bp
        app.register_blueprint(auth_bp)
    except ImportError:
        print("⚠️ Warning: auth_routes.py not found. Skipping blueprint registration.")

    try:
        from routes.photo_routes import photo_bp
        app.register_blueprint(photo_bp)
    except ImportError:
        print("⚠️ Warning: photo_routes.py not found. Skipping blueprint registration.")

    try:
        from routes.chatbot_routes import chat_bp
        app.register_blueprint(chat_bp)
    except ImportError:
        print("⚠️ Warning: chatbot_routes.py not found. Skipping blueprint registration.")

    # 3. Database Initialization Logging
    with app.app_context():
        init_db_engine() # Verifies connection and logs as per requirement
        
        # Ensure upload directory exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)