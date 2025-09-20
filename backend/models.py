from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    email: str
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Sweet(BaseModel):
    name: str
    category: str
    price: float
    quantity: int

class Purchase(BaseModel):
    quantity: int

class Restock(BaseModel):
    quantity: int

class Category(BaseModel):
    name: str
    description: str
    is_active: bool = True

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class MessageResponse(BaseModel):
    message: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
