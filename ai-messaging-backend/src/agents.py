from src.database import get_db

def get_agents():
    db = get_db()
    return list(db.agents.find({}, {'_id': False}))

def add_agent(agent_data):
    db = get_db()
    db.agents.insert_one(agent_data)
    return True