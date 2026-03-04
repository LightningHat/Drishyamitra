from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.chatbot_service import get_chatbot_response

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/api/chat', methods=['POST'])
@jwt_required()
def chat():
    data = request.get_json()
    user_query = data.get('query')
    
    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    # Get response from Groq/Gemini
    response = get_chatbot_response(user_query)
    
    return jsonify({"response": response}), 200