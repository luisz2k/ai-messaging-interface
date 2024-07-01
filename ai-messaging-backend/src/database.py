from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['ai_messaging_db']

def get_db():
    return db