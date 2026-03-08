import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv

# Config & DB
from config import Config, init_db_engine
from models.db import db

# Models
from models.user import User
from models.photo import Photo
from models.face import Face
from models.person import Person
from models.delivery import DeliveryHistory

# Blueprints
from routes.auth_routes import auth_bp
from routes.photo_routes import photo_bp
from routes.face_routes import face_bp
from routes.chat_routes import chat_bp
from routes.delivery_routes import delivery_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extensions
    CORS(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    # Registering Modular Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(photo_bp)
    app.register_blueprint(face_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(delivery_bp)

    with app.app_context():
        # Requirement: Log initialization success
        init_db_engine()
        
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

    @app.route('/api/health')
    def health():
        return jsonify({"status": "active", "milestone": "3.5 complete"}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)