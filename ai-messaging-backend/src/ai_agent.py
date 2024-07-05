from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')[:5]}...")  # Print first 5 characters for verification

def get_ai_response(user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in get_ai_response: {str(e)}")
        return "Sorry, I encountered an error while processing your message."