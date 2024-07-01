from flask import Flask, jsonify, request
from flask_cors import CORS
from src.database import get_db
from src.agents import get_agents, add_agent

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from AI Messaging Backend!"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    # Here you would typically process the message and get a response from your AI agent
    # For now, we'll just echo the message back
    ai_response = f"I received your message: {user_message}"
    
    return jsonify({"response": ai_response})

if __name__ == '__main__':
    app.run(debug=True)