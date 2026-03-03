import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from models.db import db
from routes.main_routes import main_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///drishyamitra.db')
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'data/uploads')

    # Init DB
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(main_bp)

    # Create folders/DB
    with app.app_context():
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)