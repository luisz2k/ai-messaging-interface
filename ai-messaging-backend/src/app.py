from flask import Flask, jsonify
from flask_cors import CORS
from src.database import get_db
from src.agents import get_agents, add_agent

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from AI Messaging Backend!"})

# Add more routes here

if __name__ == '__main__':
    app.run(debug=True)