from fastapi import HTTPException
from datetime import datetime
from database import get_all_sweets as db_get_all_sweets, get_sweet_by_id, get_sweet_by_name, create_sweet as db_create_sweet, update_sweet as db_update_sweet, delete_sweet as db_delete_sweet, update_sweet_quantity
from models import Sweet, MessageResponse, Purchase, Restock
from auth import is_admin

def get_all_sweets() -> list:
    return db_get_all_sweets()

def create_sweet(sweet: Sweet, current_user: str) -> MessageResponse:
    if not is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    if get_sweet_by_name(sweet.name):
        raise HTTPException(status_code=400, detail="Sweet already exists")
    
    sweet_data = {
        "name": sweet.name,
        "category": sweet.category,
        "price": sweet.price,
        "quantity": sweet.quantity,
        "created_at": datetime.utcnow()
    }
    
    db_create_sweet(sweet_data)
    return MessageResponse(message="Sweet added successfully")

def update_sweet(sweet_id: str, sweet: Sweet, current_user: str) -> MessageResponse:
    if not is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    existing_sweet = get_sweet_by_id(sweet_id)
    if not existing_sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    
    update_data = {
        "name": sweet.name,
        "category": sweet.category,
        "price": sweet.price,
        "quantity": sweet.quantity,
        "updated_at": datetime.utcnow()
    }
    
    result = db_update_sweet(sweet_id, update_data)
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Sweet not found")
    
    return MessageResponse(message="Sweet updated successfully")

def delete_sweet(sweet_id: str, current_user: str) -> MessageResponse:
    if not is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    result = db_delete_sweet(sweet_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Sweet not found")
    
    return MessageResponse(message="Sweet deleted successfully")

def purchase_sweet(sweet_id: str, purchase: Purchase, current_user: str) -> MessageResponse:
    sweet = get_sweet_by_id(sweet_id)
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    
    if sweet["quantity"] < purchase.quantity:
        raise HTTPException(status_code=400, detail="Not enough stock")
    
    update_sweet_quantity(sweet_id, -purchase.quantity)
    return MessageResponse(message=f"Successfully purchased {purchase.quantity} {sweet['name']}(s)")

def restock_sweet(sweet_id: str, restock: Restock, current_user: str) -> MessageResponse:
    if not is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    sweet = get_sweet_by_id(sweet_id)
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    
    update_sweet_quantity(sweet_id, restock.quantity)
    return MessageResponse(message=f"Successfully restocked {restock.quantity} {sweet['name']}(s)")
