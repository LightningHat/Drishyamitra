import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app) # Allows React to communicate with Flask

# Configuration
# It will use the DATABASE_URL from .env, or default to sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///drishyamitra.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

# Initialize Database
db = SQLAlchemy(app)

# Basic Model to verify database setup
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)

# Health Check Route
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "online",
        "message": "Drishyamitra Backend is active",
        "storage_path": app.config['UPLOAD_FOLDER']
    })

if __name__ == '__main__':
    # 1. Create uploads folder if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
        print(f"Created folder: {app.config['UPLOAD_FOLDER']}")

    # 2. Initialize the Database (creates drishyamitra.db)
    with app.app_context():
        db.create_all()
        print("Database 'drishyamitra.db' initialized.")

    # 3. Start the Server
    print("Server starting on http://localhost:5000")
    app.run(debug=True, port=5000)