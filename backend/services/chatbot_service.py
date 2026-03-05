import os
import json
import logging
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)

# Initialize Groq Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_chatbot_response(user_query, user_context=""):
    """
    Connects to Groq Cloud (Llama 3.3 70B).
    Interprets natural language and extracts search parameters.
    """
    try:
        # System instructions to guide the AI's behavior
        system_prompt = (
            "You are Drishyamitra AI, an intelligent photo management assistant. "
            "Your job is to help users find and share photos from their collection. "
            "You have access to names of people in the gallery. "
            "If a user wants to search for someone, try to extract their name. "
            f"Context: The user currently has these people labeled in their gallery: {user_context}. "
            "Always be helpful, polite, and concise."
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            model="llama-3.3-70b-versatile", # Per project requirement
            temperature=0.7,
            max_tokens=500
        )

        response_text = chat_completion.choices[0].message.content
        logger.info(f"🤖 Chatbot processed query: {user_query}")
        return response_text

    except Exception as e:
        logger.error(f"❌ Chatbot Service Error: {str(e)}")
        return "I'm having trouble connecting to my brain (Groq API). Please check your API key."

def interpret_search_intent(user_query):
    """
    Advanced: Asks the AI to return a JSON object for database filtering.
    Example: 'Show me Priya' -> {"intent": "search", "target": "Priya"}
    """
    try:
        instruction = (
            "Analyze the user's query and return ONLY a JSON object. "
            "If they want to search, use {'action': 'search', 'person': 'name'}. "
            "If they want to share, use {'action': 'share', 'person': 'name', 'method': 'whatsapp/email'}. "
            "If it is just a greeting, use {'action': 'none'}."
        )

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": user_query}
            ],
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception:
        return {"action": "none"}