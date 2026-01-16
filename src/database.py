import os
from pymongo import MongoClient
from dotenv import load_dotenv

# 1. Load your .env file
load_dotenv()

def get_portfolio_db():
    """
    Connects to the MongoDB Atlas cluster using the URI from .env
    Returns the database object.
    """
    try:
        # 2. Use the exact URI we found in Atlas
        client = MongoClient(os.getenv("MONGO_URI"))
        
        # 3. Access your specific database
        db = client["IWealthProject"] 
        return db
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return None