import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq Client
# Ensure GROQ_API_KEY is set in your backend/.env file
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_chatbot_response(user_query):
    """
    Connects to Groq Cloud API to process natural language queries.
    Uses Llama 3.3 70B or Mixtral 8x7B as per project description.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are Drishyamitra, a helpful AI Photo Manager. You help users organize, find, and share photos. When asked to find photos, interpret details like names, dates, locations, or objects."
                },
                {
                    "role": "user",
                    "content": user_query,
                }
            ],
            model="llama-3.3-70b-versatile", # Or "mixtral-8x7b-32768"
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Groq API Error: {e}")
        return f"I'm sorry, I'm having trouble connecting to my AI brain right now. (Error: {str(e)})"