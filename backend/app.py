import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

# Import the Database instance and Models
# (Importing models here is crucial for db.create_all() to work)
from models.db import db
from models.user import User
from models.photo import Photo
from models.face import Face
from models.person import Person
from models.delivery import DeliveryHistory

# Import Blueprints (Routes)
from routes.main_routes import main_bp
from routes.auth_routes import auth_bp
from routes.photo_routes import photo_bp
from routes.chatbot_routes import chat_bp

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # --- 1. Configuration ---
    # Database: Default to local SQLite if DATABASE_URL not in .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///data/drishyamitra.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # JWT Security
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'develop-key-replace-in-prod')
    
    # Upload Settings
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'data', 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB Limit

    # --- 2. Initialize Extensions ---
    CORS(app)
    db.init_app(app)
    jwt = JWTManager(app)

    # --- 3. Register Blueprints (Modular Routes) ---
    app.register_blueprint(main_bp)   # Basic health checks
    app.register_blueprint(auth_bp)   # Login/Register
    app.register_blueprint(photo_bp)  # Upload/Gallery
    app.register_blueprint(chat_bp)   # AI Assistant

    # --- 4. Database & Folder Initialization ---
    with app.app_context():
        # Create data/uploads directory if missing
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
            print(f"Created folder: {app.config['UPLOAD_FOLDER']}")
            
        # Create all tables in drishyamitra.db based on the models
        db.create_all()
        print("✅ Relational Database Schema Initialized.")

    # --- 5. Global Error Handlers ---
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    print(f"🚀 Drishyamitra Backend starting on http://localhost:{port}")
    app.run(debug=True, port=port)