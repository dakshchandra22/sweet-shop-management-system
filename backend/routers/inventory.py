from fastapi import APIRouter, HTTPException, status, Depends
from database import get_collection
from models import PurchaseRequest, RestockRequest
from auth import get_current_user, get_current_admin_user
from bson import ObjectId

router = APIRouter()

@router.post("/sweets/{sweet_id}/purchase")
async def purchase_sweet(sweet_id: str, purchase_data: PurchaseRequest, current_user = Depends(get_current_user)):
    sweets_collection = get_collection("sweets")
    
    if not ObjectId.is_valid(sweet_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid sweet ID"
        )
    
    sweet = sweets_collection.find_one({"_id": ObjectId(sweet_id)})
    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )
    
    if sweet["quantity"] < purchase_data.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient quantity in stock"
        )
    
    # Update quantity
    new_quantity = sweet["quantity"] - purchase_data.quantity
    sweets_collection.update_one(
        {"_id": ObjectId(sweet_id)},
        {"$set": {"quantity": new_quantity}}
    )
    
    return {
        "message": f"Successfully purchased {purchase_data.quantity} {sweet['name']}(s)",
        "remaining_quantity": new_quantity
    }

@router.post("/sweets/{sweet_id}/restock")
async def restock_sweet(sweet_id: str, restock_data: RestockRequest, current_user = Depends(get_current_admin_user)):
    sweets_collection = get_collection("sweets")
    
    if not ObjectId.is_valid(sweet_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid sweet ID"
        )
    
    sweet = sweets_collection.find_one({"_id": ObjectId(sweet_id)})
    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )
    
    # Update quantity
    new_quantity = sweet["quantity"] + restock_data.quantity
    sweets_collection.update_one(
        {"_id": ObjectId(sweet_id)},
        {"$set": {"quantity": new_quantity}}
    )
    
    return {
        "message": f"Successfully restocked {restock_data.quantity} {sweet['name']}(s)",
        "new_quantity": new_quantity
    }
