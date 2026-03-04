from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    jwt_required, 
    get_jwt_identity
)
from models.db import db
from models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    """Validates request and registers a new user with hashed credentials."""
    data = request.get_json()
    
    # Request Validation
    if not data or not data.get('username') or not data.get('password') or not data.get('email'):
        return jsonify({"error": "Missing required fields"}), 400
        
    if User.query.filter_by(username=data.get('username')).first():
        return jsonify({"error": "Username already exists"}), 409

    try:
        new_user = User(
            username=data.get('username'), 
            email=data.get('email'),
            role=data.get('role', 'user')
        )
        new_user.set_password(data.get('password'))
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Account created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    """Validates credentials and returns signed Access and Refresh JWTs."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    user = User.query.filter_by(username=data.get('username')).first()

    if user and user.check_password(data.get('password')):
        # Include custom claims (role) for fine-grained access control
        additional_claims = {"role": user.role}
        access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
        refresh_token = create_refresh_token(identity=str(user.id))

        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
        }), 200

    return jsonify({"error": "Invalid username or password"}), 401

@auth_bp.route('/api/auth/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """Issues a new access token using a valid refresh token."""
    current_user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user_id)
    return jsonify(access_token=new_access_token), 200