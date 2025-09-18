from fastapi import APIRouter, HTTPException, status, Depends
from datetime import datetime, timedelta
from database import get_collection
from models import UserCreate, User, Token, LoginRequest
from auth import verify_password, get_password_hash, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/register", response_model=User)
async def register(user_data: UserCreate):
    users_collection = get_collection("users")
    
    # Check if user already exists
    existing_user = users_collection.find_one({"$or": [{"email": user_data.email}, {"username": user_data.username}]})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already registered"
        )
    
    # Hash password and create user
    hashed_password = get_password_hash(user_data.password)
    
    # Set admin status based on username
    is_admin = user_data.username in ["admin", "shopadmin", "newadmin"]
    
    user_dict = {
        "email": user_data.email,
        "username": user_data.username,
        "password": hashed_password,
        "is_admin": is_admin,
        "created_at": datetime.utcnow()
    }
    
    result = users_collection.insert_one(user_dict)
    user_dict["id"] = result.inserted_id
    del user_dict["password"]  # Don't return password
    
    return User(**user_dict)

@router.post("/login", response_model=Token)
async def login(login_data: LoginRequest):
    users_collection = get_collection("users")
    
    username = login_data.username
    password = login_data.password
    
    # Find user by username
    user = users_collection.find_one({"username": username})
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verify password
    if not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
