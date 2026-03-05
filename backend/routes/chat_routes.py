from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.chatbot_service import get_chatbot_response, interpret_search_intent
from models.person import Person

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/api/chat/ask', methods=['POST'])
@jwt_required()
def ask_assistant():
    """
    Handles user queries like 'Who is in my last photo?' or 'Find Priya'.
    Returns a natural language response.
    """
    current_user_id = get_jwt_identity()
    data = request.get_json()
    user_query = data.get('query')

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    # 1. Fetch context (Names of people this user has already labeled)
    known_people = Person.query.filter_by(user_id=current_user_id).all()
    names_list = ", ".join([p.name for p in known_people])

    # 2. Get natural language response from Groq
    ai_answer = get_chatbot_response(user_query, user_context=names_list)

    # 3. (Optional) Extract intent for the Frontend to trigger actions
    intent = interpret_search_intent(user_query)

    return jsonify({
        "answer": ai_answer,
        "intent": intent,
        "status": "success"
    }), 200