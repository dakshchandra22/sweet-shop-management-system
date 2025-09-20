"""
Simple Categories Management
Easy to understand implementation
"""

from fastapi import HTTPException
from database import get_all_categories, get_category_by_name, create_category
from datetime import datetime

def get_categories():
    """Get all categories - simple function"""
    categories = get_all_categories()
    # Convert ObjectId to string for JSON serialization
    for category in categories:
        if '_id' in category:
            category['id'] = str(category['_id'])
            del category['_id']
    return categories

def create_new_category(category_data):
    """Create a new category - simple function"""
    # Check if category already exists
    existing = get_category_by_name(category_data["name"])
    if existing:
        raise HTTPException(status_code=400, detail="Category with this name already exists")
    
    # Add timestamp
    category_data["created_at"] = datetime.utcnow()
    category_data["is_active"] = True
    
    # Save to database
    result = create_category(category_data)
    
    # Return the created category with ID (convert ObjectId to string)
    response_data = {
        "name": category_data["name"],
        "description": category_data["description"],
        "is_active": category_data["is_active"],
        "id": str(result.inserted_id)
    }
    
    return response_data
