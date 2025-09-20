from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models import User, UserLogin, Sweet, Purchase, Restock, Category, CategoryUpdate
from auth import register_user, login_user, get_current_user
from sweets import get_all_sweets, create_sweet, update_sweet, delete_sweet, purchase_sweet, restock_sweet
from categories import get_categories, get_category, create_new_category, update_existing_category, delete_existing_category, get_category_sweets

router = APIRouter()
security = HTTPBearer()

def get_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return get_current_user(credentials.credentials)

@router.post("/auth/register")
def register(user: User):
    return register_user(user)

@router.post("/auth/login")
def login(user: UserLogin):
    return login_user(user)

@router.get("/sweets")
def get_sweets():
    return get_all_sweets()

@router.post("/sweets")
def add_sweet(sweet: Sweet, current_user: str = Depends(get_user)):
    return create_sweet(sweet, current_user)

@router.put("/sweets/{sweet_id}")
def update_sweet_route(sweet_id: str, sweet: Sweet, current_user: str = Depends(get_user)):
    return update_sweet(sweet_id, sweet, current_user)

@router.delete("/sweets/{sweet_id}")
def delete_sweet_route(sweet_id: str, current_user: str = Depends(get_user)):
    return delete_sweet(sweet_id, current_user)

@router.post("/sweets/{sweet_id}/purchase")
def purchase_sweet_route(sweet_id: str, purchase: Purchase, current_user: str = Depends(get_user)):
    return purchase_sweet(sweet_id, purchase, current_user)

@router.post("/sweets/{sweet_id}/restock")
def restock_sweet_route(sweet_id: str, restock: Restock, current_user: str = Depends(get_user)):
    return restock_sweet(sweet_id, restock, current_user)

# Category routes
@router.get("/categories")
def get_categories_route(active_only: bool = Query(False, description="Filter only active categories")):
    return get_categories(active_only)

@router.get("/categories/{category_id}")
def get_category_route(category_id: str):
    return get_category(category_id)

@router.post("/categories")
def create_category_route(category: Category, current_user: str = Depends(get_user)):
    return create_new_category(category)

@router.put("/categories/{category_id}")
def update_category_route(category_id: str, category_update: CategoryUpdate, current_user: str = Depends(get_user)):
    return update_existing_category(category_id, category_update)

@router.delete("/categories/{category_id}")
def delete_category_route(category_id: str, current_user: str = Depends(get_user)):
    return delete_existing_category(category_id)

@router.get("/categories/{category_id}/sweets")
def get_category_sweets_route(category_id: str):
    return get_category_sweets(category_id)
