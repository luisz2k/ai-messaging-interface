from flask import Flask, jsonify, request
from flask_cors import CORS
from src.ai_agent import get_ai_response
import logging

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from AI Messaging Backend!"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    logging.info(f"Received user message: {user_message}")
    
    # Get response from AI agent
    try:
        ai_response = get_ai_response(user_message)
        logging.info(f"AI response: {ai_response}")
    except Exception as e:
        logging.error(f"Error getting AI response: {str(e)}", exc_info=True)
        ai_response = "Sorry, I encountered an error while processing your message."
    
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)