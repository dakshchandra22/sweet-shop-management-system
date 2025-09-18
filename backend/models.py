from pydantic import BaseModel, EmailStr, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from typing import Optional, Any
from datetime import datetime
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type: Any, _handler: Any) -> Any:
        from pydantic_core import core_schema
        return core_schema.no_info_plain_validator_function(cls.validate)

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, _core_schema: Any, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        return {"type": "string"}

# User Models
class UserBase(BaseModel):
    email: str
    username: str
    is_admin: bool = False

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: PyObjectId
    created_at: datetime

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Sweet Models
class SweetBase(BaseModel):
    name: str
    category: str
    price: float
    quantity: int

class SweetCreate(SweetBase):
    pass

class SweetUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

class Sweet(SweetBase):
    id: PyObjectId
    created_at: datetime
    updated_at: datetime

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Auth Models
class LoginRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Purchase/Restock Models
class PurchaseRequest(BaseModel):
    quantity: int

class RestockRequest(BaseModel):
    quantity: int
