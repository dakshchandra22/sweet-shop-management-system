from pymongo import MongoClient
import os

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DATABASE_NAME = "sweet_shop"

client = MongoClient(MONGO_URL)
database = client[DATABASE_NAME]

def get_database():
    return database

def get_collection(collection_name):
    return database[collection_name]
