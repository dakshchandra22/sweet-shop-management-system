import pytest
import asyncio
from fastapi.testclient import TestClient
from pymongo import MongoClient
from main import app
from database import get_database

# Test database
TEST_DATABASE_NAME = "sweet_shop_test"

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)

@pytest.fixture
def test_db():
    """Create a test database."""
    client = MongoClient("mongodb://localhost:27017")
    db = client[TEST_DATABASE_NAME]
    yield db
    # Clean up after tests
    client.drop_database(TEST_DATABASE_NAME)

@pytest.fixture
def sample_user_data():
    """Sample user data for testing."""
    return {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword123",
        "is_admin": False
    }

@pytest.fixture
def sample_admin_data():
    """Sample admin user data for testing."""
    return {
        "email": "admin@example.com",
        "username": "admin",
        "password": "adminpassword123",
        "is_admin": True
    }

@pytest.fixture
def sample_sweet_data():
    """Sample sweet data for testing."""
    return {
        "name": "Chocolate Bar",
        "category": "Chocolate",
        "price": 2.50,
        "quantity": 100
    }
