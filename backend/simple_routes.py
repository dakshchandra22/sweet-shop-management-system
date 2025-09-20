"""
Simple Routes for Categories
No authentication - easy to understand
"""

from fastapi import APIRouter
from simple_categories import get_categories, create_new_category

# Create router
router = APIRouter()

@router.get("/categories")
def get_categories_route():
    """Get all categories - simple endpoint"""
    return get_categories()

@router.post("/categories")
def create_category_route(category_data: dict):
    """Create a new category - simple endpoint"""
    return create_new_category(category_data)
