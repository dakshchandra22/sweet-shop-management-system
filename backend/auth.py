from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from database import get_user_by_email, get_user_by_username, create_user
from models import User, UserLogin, TokenResponse
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

def validate_password_strength(password: str) -> bool:
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)
    is_long_enough = len(password) >= 8
    
    return has_upper and has_lower and has_digit and has_special and is_long_enough

def register_user(user: User) -> dict:
    if get_user_by_email(user.email) or get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Email or username already registered")
    
    if not validate_password_strength(user.password):
        raise HTTPException(
            status_code=400, 
            detail="Password must be at least 8 characters long and contain uppercase, lowercase, number, and special character"
        )
    
    hashed_password = hash_password(user.password)
    is_admin = user.username in ["admin", "shopadmin"]
    
    user_data = {
        "email": user.email,
        "username": user.username,
        "password": hashed_password,
        "is_admin": is_admin,
        "created_at": datetime.utcnow()
    }
    
    result = create_user(user_data)
    return {"message": "User created successfully", "user_id": str(result.inserted_id)}

def login_user(user: UserLogin) -> TokenResponse:
    user_data = get_user_by_username(user.username)
    if not user_data or not verify_password(user.password, user_data["password"]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    token = create_token({"sub": user.username})
    return TokenResponse(access_token=token, token_type="bearer")

def get_current_user(token: str) -> str:
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    username = verify_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return username

def is_admin(username: str) -> bool:
    user_data = get_user_by_username(username)
    return user_data.get("is_admin", False) if user_data else False
