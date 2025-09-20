"""
Pytest configuration and fixtures for Sweet Shop Management System tests
"""

import pytest
import os
import sys
from unittest.mock import Mock, patch
from fastapi.testclient import TestClient
from pymongo import MongoClient
from datetime import datetime

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import app
from database import get_user_by_username, create_user
from auth import hash_password

@pytest.fixture
def client():
    """Create a test client for the FastAPI application"""
    return TestClient(app)

@pytest.fixture
def test_db():
    """Create a test database connection"""
    # Use a test database
    test_mongodb_url = os.getenv("TEST_MONGODB_URL", "mongodb://localhost:27017")
    test_db_name = "sweet_shop_test"
    
    client = MongoClient(test_mongodb_url)
    db = client[test_db_name]
    
    # Clean up before each test
    db.users.delete_many({})
    db.sweets.delete_many({})
    
    yield db
    
    # Clean up after each test
    db.users.delete_many({})
    db.sweets.delete_many({})
    client.close()

@pytest.fixture
def sample_user_data():
    """Sample user data for testing"""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "TestPassword123!",
        "is_admin": False
    }

@pytest.fixture
def sample_admin_data():
    """Sample admin user data for testing"""
    return {
        "username": "admin",
        "email": "admin@example.com",
        "password": "AdminPassword123!",
        "is_admin": True
    }

@pytest.fixture
def sample_sweet_data():
    """Sample sweet data for testing"""
    return {
        "name": "Test Sweet",
        "description": "A delicious test sweet",
        "category": "Test",
        "price": 25.0,
        "quantity": 50,
        "image_url": "https://example.com/test.jpg"
    }

@pytest.fixture
def auth_headers(client, test_db, sample_user_data):
    """Create authentication headers for testing"""
    # Register user through API
    register_response = client.post("/api/auth/register", json=sample_user_data)
    if register_response.status_code != 200:
        raise Exception(f"Registration failed: {register_response.text}")
    
    # Login to get token
    response = client.post("/api/auth/login", json={
        "username": sample_user_data["username"],
        "password": sample_user_data["password"]
    })
    
    if response.status_code != 200:
        raise Exception(f"Login failed: {response.text}")
    
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def admin_headers(client, test_db, sample_admin_data):
    """Create admin authentication headers for testing"""
    # Register admin user through API
    register_response = client.post("/api/auth/register", json=sample_admin_data)
    if register_response.status_code != 200:
        raise Exception(f"Registration failed: {register_response.text}")
    
    # Login to get token
    response = client.post("/api/auth/login", json={
        "username": sample_admin_data["username"],
        "password": sample_admin_data["password"]
    })
    
    if response.status_code != 200:
        raise Exception(f"Login failed: {response.text}")
    
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def mock_database(test_db):
    """Mock database operations for testing"""
    with patch('database.client') as mock_client:
        mock_client.return_value = test_db.client
        mock_client.return_value.__getitem__.return_value = test_db
        yield test_db
