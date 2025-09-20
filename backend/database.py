from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from config import MONGODB_URL, DATABASE_NAME

client = MongoClient(MONGODB_URL)
db = client[DATABASE_NAME]

def get_user_by_username(username: str):
    return db.users.find_one({"username": username})

def get_user_by_email(email: str):
    return db.users.find_one({"email": email})

def create_user(user_data: dict):
    return db.users.insert_one(user_data)

def get_all_sweets():
    sweets = list(db.sweets.find())
    for sweet in sweets:
        sweet["id"] = str(sweet["_id"])
        del sweet["_id"]
    return sweets

def get_sweet_by_id(sweet_id: str):
    return db.sweets.find_one({"_id": ObjectId(sweet_id)})

def get_sweet_by_name(name: str):
    return db.sweets.find_one({"name": name})

def create_sweet(sweet_data: dict):
    return db.sweets.insert_one(sweet_data)

def update_sweet(sweet_id: str, update_data: dict):
    return db.sweets.update_one(
        {"_id": ObjectId(sweet_id)},
        {"$set": update_data}
    )

def delete_sweet(sweet_id: str):
    return db.sweets.delete_one({"_id": ObjectId(sweet_id)})

def update_sweet_quantity(sweet_id: str, quantity_change: int):
    return db.sweets.update_one(
        {"_id": ObjectId(sweet_id)},
        {"$inc": {"quantity": quantity_change}}
    )
