from pydantic import BaseModel

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

class MessageResponse(BaseModel):
    message: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
