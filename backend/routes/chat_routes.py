from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.chatbot_service import get_chatbot_response

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/api/chat/ask', methods=['POST'])
@jwt_required()
def ask_assistant():
    data = request.get_json()
    user_query = data.get('query')
    
    if not user_query:
        return jsonify({"error": "Query required"}), 400

    # Process via Groq/Gemini Service
    response = get_chatbot_response(user_query)
    
    return jsonify({
        "status": "success",
        "answer": response
    }), 200