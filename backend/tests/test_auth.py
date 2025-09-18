import pytest
from fastapi.testclient import TestClient
from database import get_collection

def test_register_user(client, sample_user_data):
    """Test user registration."""
    response = client.post("/api/auth/register", json=sample_user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == sample_user_data["email"]
    assert data["username"] == sample_user_data["username"]
    assert data["is_admin"] == sample_user_data["is_admin"]
    assert "id" in data
    assert "password" not in data

def test_register_duplicate_user(client, sample_user_data):
    """Test registration with duplicate email/username."""
    # First registration
    client.post("/api/auth/register", json=sample_user_data)
    
    # Second registration with same email
    response = client.post("/api/auth/register", json=sample_user_data)
    assert response.status_code == 400
    assert "already registered" in response.json()["detail"]

def test_login_success(client, sample_user_data):
    """Test successful login."""
    # Register user first
    client.post("/api/auth/register", json=sample_user_data)
    
    # Login
    response = client.post("/api/auth/login", data={
        "email": sample_user_data["email"],
        "password": sample_user_data["password"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials(client, sample_user_data):
    """Test login with invalid credentials."""
    # Register user first
    client.post("/api/auth/register", json=sample_user_data)
    
    # Login with wrong password
    response = client.post("/api/auth/login", data={
        "email": sample_user_data["email"],
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert "Incorrect email or password" in response.json()["detail"]

def test_login_nonexistent_user(client):
    """Test login with non-existent user."""
    response = client.post("/api/auth/login", data={
        "email": "nonexistent@example.com",
        "password": "password"
    })
    assert response.status_code == 401
    assert "Incorrect email or password" in response.json()["detail"]
