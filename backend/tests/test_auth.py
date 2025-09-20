"""
Test cases for authentication functionality
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from datetime import datetime

class TestAuthentication:
    """Test authentication endpoints and functionality"""
    
    def test_user_registration_success(self, client, test_db, sample_user_data):
        """Test successful user registration"""
        response = client.post("/api/auth/register", json=sample_user_data)
        
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "User created successfully" in data["message"]
        assert "user_id" in data
        
        # Verify user was created in database
        user = test_db.users.find_one({"username": sample_user_data["username"]})
        assert user is not None
        assert user["email"] == sample_user_data["email"]
        assert user["is_admin"] == False
    
    def test_user_registration_duplicate_username(self, client, test_db, sample_user_data):
        """Test registration with duplicate username"""
        # Create first user
        client.post("/api/auth/register", json=sample_user_data)
        
        # Try to create user with same username
        duplicate_data = sample_user_data.copy()
        duplicate_data["email"] = "different@example.com"
        
        response = client.post("/api/auth/register", json=duplicate_data)
        
        assert response.status_code == 400
        assert "already registered" in response.json()["detail"]
    
    def test_user_registration_duplicate_email(self, client, test_db, sample_user_data):
        """Test registration with duplicate email"""
        # Create first user
        client.post("/api/auth/register", json=sample_user_data)
        
        # Try to create user with same email
        duplicate_data = sample_user_data.copy()
        duplicate_data["username"] = "differentuser"
        
        response = client.post("/api/auth/register", json=duplicate_data)
        
        assert response.status_code == 400
        assert "already registered" in response.json()["detail"]
    
    def test_user_registration_weak_password(self, client, test_db, sample_user_data):
        """Test registration with weak password"""
        weak_password_data = sample_user_data.copy()
        weak_password_data["password"] = "weak"
        
        response = client.post("/api/auth/register", json=weak_password_data)
        
        assert response.status_code == 400
        assert "Password must be at least 8 characters" in response.json()["detail"]
    
    def test_user_login_success(self, client, test_db, sample_user_data):
        """Test successful user login"""
        # Register user first
        client.post("/api/auth/register", json=sample_user_data)
        
        # Login
        login_data = {
            "username": sample_user_data["username"],
            "password": sample_user_data["password"]
        }
        
        response = client.post("/api/auth/login", json=login_data)
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "token_type" in data
        assert data["token_type"] == "bearer"
    
    def test_user_login_invalid_credentials(self, client, test_db, sample_user_data):
        """Test login with invalid credentials"""
        # Register user first
        client.post("/api/auth/register", json=sample_user_data)
        
        # Login with wrong password
        login_data = {
            "username": sample_user_data["username"],
            "password": "wrongpassword"
        }
        
        response = client.post("/api/auth/login", json=login_data)
        
        assert response.status_code == 401
        assert "Incorrect username or password" in response.json()["detail"]
    
    def test_user_login_nonexistent_user(self, client, test_db):
        """Test login with non-existent user"""
        login_data = {
            "username": "nonexistent",
            "password": "password123"
        }
        
        response = client.post("/api/auth/login", json=login_data)
        
        assert response.status_code == 401
        assert "Incorrect username or password" in response.json()["detail"]
    
    def test_admin_user_creation(self, client, test_db, sample_admin_data):
        """Test that admin users are created with correct privileges"""
        response = client.post("/api/auth/register", json=sample_admin_data)
        
        assert response.status_code == 200
        
        # Verify admin user was created
        user = test_db.users.find_one({"username": sample_admin_data["username"]})
        assert user is not None
        assert user["is_admin"] == True
    
    def test_password_hashing(self):
        """Test password hashing functionality"""
        from auth import hash_password, verify_password
        
        password = "TestPassword123!"
        hashed = hash_password(password)
        
        # Hashed password should be different from original
        assert hashed != password
        
        # Should be able to verify the password
        assert verify_password(password, hashed) == True
        
        # Should fail with wrong password
        assert verify_password("wrongpassword", hashed) == False
    
    def test_jwt_token_creation_and_verification(self):
        """Test JWT token creation and verification"""
        from auth import create_token, verify_token
        
        username = "testuser"
        token = create_token({"sub": username})
        
        # Token should not be empty
        assert token is not None
        assert len(token) > 0
        
        # Should be able to verify the token
        verified_username = verify_token(token)
        assert verified_username == username
    
    def test_invalid_jwt_token(self):
        """Test handling of invalid JWT tokens"""
        from auth import verify_token
        
        # Test with invalid token
        result = verify_token("invalid.token.here")
        assert result is None
        
        # Test with empty token
        result = verify_token("")
        assert result is None
