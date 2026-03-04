from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import jsonify

def role_required(required_role):
    """
    Decorator to restrict access to users with a specific role.
    Usage: @role_required('admin')
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            # Ensure a valid JWT is present
            verify_jwt_in_request()
            # Extract claims from the token
            claims = get_jwt()
            
            if claims.get("role") == required_role or claims.get("role") == "admin":
                return fn(*args, **kwargs)
            else:
                return jsonify({"error": f"Access forbidden: {required_role} role required"}), 403
        return decorator
    return wrapper