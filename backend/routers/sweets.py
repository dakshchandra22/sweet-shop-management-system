from fastapi import APIRouter, HTTPException, status, Depends, Query
from fastapi.security import HTTPBearer
from typing import List, Optional
from datetime import datetime
from database import get_collection
from models import Sweet, SweetCreate, SweetUpdate
from auth import get_current_user, get_current_admin_user
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=Sweet)
async def create_sweet(sweet_data: SweetCreate, current_user = Depends(get_current_admin_user)):
    sweets_collection = get_collection("sweets")
    
    # Check if sweet with same name already exists
    existing_sweet = sweets_collection.find_one({"name": sweet_data.name})
    if existing_sweet:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sweet with this name already exists"
        )
    
    sweet_dict = {
        "name": sweet_data.name,
        "category": sweet_data.category,
        "price": sweet_data.price,
        "quantity": sweet_data.quantity,
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    result = sweets_collection.insert_one(sweet_dict)
    
    # Transform for response
    response_dict = {
        "id": str(result.inserted_id),
        "name": sweet_dict["name"],
        "category": sweet_dict["category"],
        "price": sweet_dict["price"],
        "quantity": sweet_dict["quantity"],
        "created_at": sweet_dict["created_at"],
        "updated_at": sweet_dict["updated_at"]
    }
    
    return Sweet(**response_dict)

@router.get("/", response_model=List[Sweet], dependencies=[], tags=["public"])
async def get_sweets():
    sweets_collection = get_collection("sweets")
    sweets = list(sweets_collection.find())
    
    # Transform MongoDB documents to match Sweet model
    transformed_sweets = []
    for sweet in sweets:
        sweet_dict = {
            "id": str(sweet["_id"]),
            "name": sweet["name"],
            "category": sweet["category"],
            "price": sweet["price"],
            "quantity": sweet["quantity"],
            "created_at": sweet.get("created_at", datetime.utcnow()),
            "updated_at": sweet.get("updated_at", datetime.utcnow())
        }
        transformed_sweets.append(Sweet(**sweet_dict))
    
    return transformed_sweets

@router.get("/search", response_model=List[Sweet], dependencies=[], tags=["public"])
async def search_sweets(
    name: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    price_min: Optional[float] = Query(None),
    price_max: Optional[float] = Query(None)
):
    sweets_collection = get_collection("sweets")
    
    # Build search query
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if category:
        query["category"] = {"$regex": category, "$options": "i"}
    if price_min is not None or price_max is not None:
        price_query = {}
        if price_min is not None:
            price_query["$gte"] = price_min
        if price_max is not None:
            price_query["$lte"] = price_max
        query["price"] = price_query
    
    sweets = list(sweets_collection.find(query))
    
    # Transform MongoDB documents to match Sweet model
    transformed_sweets = []
    for sweet in sweets:
        sweet_dict = {
            "id": str(sweet["_id"]),
            "name": sweet["name"],
            "category": sweet["category"],
            "price": sweet["price"],
            "quantity": sweet["quantity"],
            "created_at": sweet.get("created_at", datetime.utcnow()),
            "updated_at": sweet.get("updated_at", datetime.utcnow())
        }
        transformed_sweets.append(Sweet(**sweet_dict))
    
    return transformed_sweets

@router.get("/{sweet_id}", response_model=Sweet)
async def get_sweet(sweet_id: str):
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
    
    # Transform MongoDB document to match Sweet model
    sweet_dict = {
        "id": str(sweet["_id"]),
        "name": sweet["name"],
        "category": sweet["category"],
        "price": sweet["price"],
        "quantity": sweet["quantity"],
        "created_at": sweet.get("created_at", datetime.utcnow()),
        "updated_at": sweet.get("updated_at", datetime.utcnow())
    }
    
    return Sweet(**sweet_dict)

@router.put("/{sweet_id}", response_model=Sweet)
async def update_sweet(sweet_id: str, sweet_data: SweetUpdate, current_user = Depends(get_current_admin_user)):
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
    
    # Update only provided fields
    update_data = {k: v for k, v in sweet_data.model_dump().items() if v is not None}
    if update_data:
        update_data["updated_at"] = datetime.utcnow()
        sweets_collection.update_one(
            {"_id": ObjectId(sweet_id)},
            {"$set": update_data}
        )
    
    # Return updated sweet
    updated_sweet = sweets_collection.find_one({"_id": ObjectId(sweet_id)})
    
    # Transform MongoDB document to match Sweet model
    sweet_dict = {
        "id": str(updated_sweet["_id"]),
        "name": updated_sweet["name"],
        "category": updated_sweet["category"],
        "price": updated_sweet["price"],
        "quantity": updated_sweet["quantity"],
        "created_at": updated_sweet.get("created_at", datetime.utcnow()),
        "updated_at": updated_sweet.get("updated_at", datetime.utcnow())
    }
    
    return Sweet(**sweet_dict)

@router.delete("/{sweet_id}")
async def delete_sweet(sweet_id: str, current_user = Depends(get_current_admin_user)):
    sweets_collection = get_collection("sweets")
    
    if not ObjectId.is_valid(sweet_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid sweet ID"
        )
    
    result = sweets_collection.delete_one({"_id": ObjectId(sweet_id)})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )
    
    return {"message": "Sweet deleted successfully"}
