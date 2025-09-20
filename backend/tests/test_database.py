"""
Test cases for database operations
"""

import pytest
from unittest.mock import Mock, patch
from bson import ObjectId
from datetime import datetime

class TestDatabaseOperations:
    """Test database CRUD operations"""
    
    def test_get_user_by_username(self, test_db, sample_user_data):
        """Test getting user by username"""
        from database import get_user_by_username
        
        # Insert test user
        user_data = sample_user_data.copy()
        user_data["password"] = "hashed_password"
        user_data["created_at"] = datetime.utcnow()
        test_db.users.insert_one(user_data)
        
        # Test getting user
        user = get_user_by_username(sample_user_data["username"])
        
        assert user is not None
        assert user["username"] == sample_user_data["username"]
        assert user["email"] == sample_user_data["email"]
    
    def test_get_user_by_username_not_found(self, test_db):
        """Test getting non-existent user by username"""
        from database import get_user_by_username
        
        user = get_user_by_username("nonexistent")
        assert user is None
    
    def test_get_user_by_email(self, test_db, sample_user_data):
        """Test getting user by email"""
        from database import get_user_by_email
        
        # Insert test user
        user_data = sample_user_data.copy()
        user_data["password"] = "hashed_password"
        user_data["created_at"] = datetime.utcnow()
        test_db.users.insert_one(user_data)
        
        # Test getting user
        user = get_user_by_email(sample_user_data["email"])
        
        assert user is not None
        assert user["username"] == sample_user_data["username"]
        assert user["email"] == sample_user_data["email"]
    
    def test_get_user_by_email_not_found(self, test_db):
        """Test getting non-existent user by email"""
        from database import get_user_by_email
        
        user = get_user_by_email("nonexistent@example.com")
        assert user is None
    
    def test_create_user(self, test_db, sample_user_data):
        """Test creating a new user"""
        from database import create_user
        
        user_data = sample_user_data.copy()
        user_data["password"] = "hashed_password"
        user_data["created_at"] = datetime.utcnow()
        
        result = create_user(user_data)
        
        assert result.inserted_id is not None
        
        # Verify user was created
        user = test_db.users.find_one({"_id": result.inserted_id})
        assert user is not None
        assert user["username"] == sample_user_data["username"]
    
    def test_get_all_sweets(self, test_db, sample_sweet_data):
        """Test getting all sweets"""
        from database import get_all_sweets
        
        # Insert test sweets
        sweet1 = sample_sweet_data.copy()
        sweet1["name"] = "Sweet 1"
        sweet1["created_at"] = datetime.utcnow()
        
        sweet2 = sample_sweet_data.copy()
        sweet2["name"] = "Sweet 2"
        sweet2["created_at"] = datetime.utcnow()
        
        test_db.sweets.insert_many([sweet1, sweet2])
        
        # Test getting all sweets
        sweets = get_all_sweets()
        
        assert len(sweets) == 2
        assert all("id" in sweet for sweet in sweets)
        assert all("_id" not in sweet for sweet in sweets)
        
        # Check that IDs are strings
        for sweet in sweets:
            assert isinstance(sweet["id"], str)
    
    def test_get_sweet_by_id(self, test_db, sample_sweet_data):
        """Test getting sweet by ID"""
        from database import get_sweet_by_id
        
        # Insert test sweet
        sweet_data = sample_sweet_data.copy()
        sweet_data["created_at"] = datetime.utcnow()
        result = test_db.sweets.insert_one(sweet_data)
        sweet_id = str(result.inserted_id)
        
        # Test getting sweet
        sweet = get_sweet_by_id(sweet_id)
        
        assert sweet is not None
        assert sweet["name"] == sample_sweet_data["name"]
        assert sweet["price"] == sample_sweet_data["price"]
    
    def test_get_sweet_by_id_not_found(self, test_db):
        """Test getting non-existent sweet by ID"""
        from database import get_sweet_by_id
        
        fake_id = "507f1f77bcf86cd799439011"  # Valid ObjectId format
        sweet = get_sweet_by_id(fake_id)
        assert sweet is None
    
    def test_get_sweet_by_name(self, test_db, sample_sweet_data):
        """Test getting sweet by name"""
        from database import get_sweet_by_name
        
        # Insert test sweet
        sweet_data = sample_sweet_data.copy()
        sweet_data["created_at"] = datetime.utcnow()
        test_db.sweets.insert_one(sweet_data)
        
        # Test getting sweet
        sweet = get_sweet_by_name(sample_sweet_data["name"])
        
        assert sweet is not None
        assert sweet["name"] == sample_sweet_data["name"]
        assert sweet["price"] == sample_sweet_data["price"]
    
    def test_get_sweet_by_name_not_found(self, test_db):
        """Test getting non-existent sweet by name"""
        from database import get_sweet_by_name
        
        sweet = get_sweet_by_name("Nonexistent Sweet")
        assert sweet is None
    
    def test_create_sweet(self, test_db, sample_sweet_data):
        """Test creating a new sweet"""
        from database import create_sweet
        
        sweet_data = sample_sweet_data.copy()
        sweet_data["created_at"] = datetime.utcnow()
        
        result = create_sweet(sweet_data)
        
        assert result.inserted_id is not None
        
        # Verify sweet was created
        sweet = test_db.sweets.find_one({"_id": result.inserted_id})
        assert sweet is not None
        assert sweet["name"] == sample_sweet_data["name"]
    
    def test_update_sweet(self, test_db, sample_sweet_data):
        """Test updating a sweet"""
        from database import update_sweet
        
        # Insert test sweet
        sweet_data = sample_sweet_data.copy()
        sweet_data["created_at"] = datetime.utcnow()
        result = test_db.sweets.insert_one(sweet_data)
        sweet_id = str(result.inserted_id)
        
        # Update sweet
        update_data = {"price": 30.0, "quantity": 100}
        result = update_sweet(sweet_id, update_data)
        
        assert result.modified_count == 1
        
        # Verify update
        sweet = test_db.sweets.find_one({"_id": ObjectId(sweet_id)})
        assert sweet["price"] == 30.0
        assert sweet["quantity"] == 100
    
    def test_delete_sweet(self, test_db, sample_sweet_data):
        """Test deleting a sweet"""
        from database import delete_sweet
        
        # Insert test sweet
        sweet_data = sample_sweet_data.copy()
        sweet_data["created_at"] = datetime.utcnow()
        result = test_db.sweets.insert_one(sweet_data)
        sweet_id = str(result.inserted_id)
        
        # Delete sweet
        result = delete_sweet(sweet_id)
        
        assert result.deleted_count == 1
        
        # Verify deletion
        sweet = test_db.sweets.find_one({"_id": ObjectId(sweet_id)})
        assert sweet is None
    
    def test_update_sweet_quantity(self, test_db, sample_sweet_data):
        """Test updating sweet quantity"""
        from database import update_sweet_quantity
        
        # Insert test sweet
        sweet_data = sample_sweet_data.copy()
        sweet_data["quantity"] = 50
        sweet_data["created_at"] = datetime.utcnow()
        result = test_db.sweets.insert_one(sweet_data)
        sweet_id = str(result.inserted_id)
        
        # Update quantity (decrease by 10)
        result = update_sweet_quantity(sweet_id, -10)
        
        assert result.modified_count == 1
        
        # Verify quantity update
        sweet = test_db.sweets.find_one({"_id": ObjectId(sweet_id)})
        assert sweet["quantity"] == 40
    
    def test_update_sweet_quantity_increase(self, test_db, sample_sweet_data):
        """Test increasing sweet quantity"""
        from database import update_sweet_quantity
        
        # Insert test sweet
        sweet_data = sample_sweet_data.copy()
        sweet_data["quantity"] = 50
        sweet_data["created_at"] = datetime.utcnow()
        result = test_db.sweets.insert_one(sweet_data)
        sweet_id = str(result.inserted_id)
        
        # Update quantity (increase by 20)
        result = update_sweet_quantity(sweet_id, 20)
        
        assert result.modified_count == 1
        
        # Verify quantity update
        sweet = test_db.sweets.find_one({"_id": ObjectId(sweet_id)})
        assert sweet["quantity"] == 70
