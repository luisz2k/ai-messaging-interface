from flask import Flask, jsonify, request
from flask_cors import CORS
from src.ai_agent import get_ai_response
from src.workflow_manager import workflow_manager
import logging
import os

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load workflows and agents
workflow_dir = os.path.join(os.path.dirname(__file__), '..', 'workflows')
workflow_manager.load_workflows(workflow_dir)

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

@app.route('/set_workflow', methods=['POST'])
def set_workflow():
    data = request.json
    workflow_name = data.get('workflow_name')
    
    if workflow_manager.set_active_workflow(workflow_name):
        return jsonify({"message": f"Workflow '{workflow_name}' set as active."})
    else:
        return jsonify({"error": f"Workflow '{workflow_name}' not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)