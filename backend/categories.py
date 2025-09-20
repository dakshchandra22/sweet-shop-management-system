"""
Category management business logic
"""

from fastapi import HTTPException
from database import (
    get_all_categories, get_category_by_id, get_category_by_name,
    create_category, update_category, delete_category, get_sweets_by_category
)
from models import Category, CategoryUpdate
from datetime import datetime

def get_categories(active_only: bool = False):
    """Get all categories, optionally filtered by active status"""
    return get_all_categories(active_only)

def get_category(category_id: str):
    """Get a specific category by ID"""
    category = get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    category["id"] = str(category["_id"])
    del category["_id"]
    return category

def create_new_category(category: Category):
    """Create a new category"""
    # Check if category with same name already exists
    existing_category = get_category_by_name(category.name)
    if existing_category:
        raise HTTPException(status_code=400, detail="Category with this name already exists")
    
    category_data = {
        "name": category.name,
        "description": category.description,
        "is_active": category.is_active,
        "created_at": datetime.utcnow()
    }
    
    result = create_category(category_data)
    category_data["id"] = str(result.inserted_id)
    del category_data["created_at"]
    return category_data

def update_existing_category(category_id: str, category_update: CategoryUpdate):
    """Update an existing category"""
    # Check if category exists
    existing_category = get_category_by_id(category_id)
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    # Prepare update data (only include non-None fields)
    update_data = {}
    if category_update.name is not None:
        # Check if new name conflicts with existing category
        if category_update.name != existing_category["name"]:
            conflicting_category = get_category_by_name(category_update.name)
            if conflicting_category:
                raise HTTPException(status_code=400, detail="Category with this name already exists")
        update_data["name"] = category_update.name
    
    if category_update.description is not None:
        update_data["description"] = category_update.description
    
    if category_update.is_active is not None:
        update_data["is_active"] = category_update.is_active
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No valid fields to update")
    
    result = update_category(category_id, update_data)
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="No changes made")
    
    # Return updated category
    return get_category(category_id)

def delete_existing_category(category_id: str):
    """Delete an existing category"""
    # Check if category exists
    existing_category = get_category_by_id(category_id)
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    result = delete_category(category_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=400, detail="Failed to delete category")
    
    return {"message": "Category deleted successfully"}

def get_category_sweets(category_id: str):
    """Get all sweets in a specific category"""
    # Check if category exists
    category = get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return get_sweets_by_category(category["name"])
