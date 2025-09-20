"""
Test cases for sweet categories management functionality
Following TDD Red-Green-Refactor pattern
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from bson import ObjectId

class TestCategoriesManagement:
    """Test sweet categories CRUD operations and business logic"""
    
    def test_get_all_categories_empty(self, client, test_db):
        """Test getting all categories when database is empty"""
        response = client.get("/api/categories")
        
        assert response.status_code == 200
        assert response.json() == []
    
    def test_get_all_categories_with_data(self, client, test_db, admin_headers):
        """Test getting all categories when data exists"""
        # Create test categories via API
        categories_data = [
            {"name": "Traditional", "description": "Traditional Indian sweets", "is_active": True},
            {"name": "Modern", "description": "Modern fusion sweets", "is_active": True},
            {"name": "Seasonal", "description": "Seasonal special sweets", "is_active": False}
        ]
        
        for category in categories_data:
            client.post("/api/categories", json=category, headers=admin_headers)
        
        response = client.get("/api/categories")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 3
        assert any(cat["name"] == "Traditional" for cat in data)
        assert any(cat["name"] == "Modern" for cat in data)
        assert any(cat["name"] == "Seasonal" for cat in data)
    
    def test_get_active_categories_only(self, client, test_db, admin_headers):
        """Test getting only active categories"""
        # Create test categories via API
        categories_data = [
            {"name": "Traditional", "description": "Traditional Indian sweets", "is_active": True},
            {"name": "Modern", "description": "Modern fusion sweets", "is_active": True},
            {"name": "Seasonal", "description": "Seasonal special sweets", "is_active": False}
        ]
        
        for category in categories_data:
            client.post("/api/categories", json=category, headers=admin_headers)
        
        response = client.get("/api/categories?active_only=true")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        assert all(cat["is_active"] for cat in data)
    
    def test_create_category_success(self, client, test_db, admin_headers):
        """Test successful category creation by admin"""
        category_data = {
            "name": "Premium",
            "description": "Premium quality sweets",
            "is_active": True
        }
        
        response = client.post("/api/categories", json=category_data, headers=admin_headers)
        
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == category_data["name"]
        assert data["description"] == category_data["description"]
        assert data["is_active"] == category_data["is_active"]
        assert "id" in data
        assert "created_at" in data
        
        # Verify category was created in database
        category = test_db.categories.find_one({"name": category_data["name"]})
        assert category is not None
        assert category["description"] == category_data["description"]
    
    def test_create_category_unauthorized(self, client, test_db, auth_headers):
        """Test category creation without admin privileges"""
        category_data = {
            "name": "Premium",
            "description": "Premium quality sweets",
            "is_active": True
        }
        
        response = client.post("/api/categories", json=category_data, headers=auth_headers)
        
        assert response.status_code == 403
        assert "Admin access required" in response.json()["detail"]
    
    def test_create_category_no_auth(self, client, test_db):
        """Test category creation without authentication"""
        category_data = {
            "name": "Premium",
            "description": "Premium quality sweets",
            "is_active": True
        }
        
        response = client.post("/api/categories", json=category_data)
        
        assert response.status_code == 401
        assert "Not authenticated" in response.json()["detail"]
    
    def test_create_category_duplicate_name(self, client, test_db, admin_headers):
        """Test creating category with duplicate name"""
        category_data = {
            "name": "Traditional",
            "description": "Traditional Indian sweets",
            "is_active": True
        }
        
        # Create first category
        client.post("/api/categories", json=category_data, headers=admin_headers)
        
        # Try to create category with same name
        response = client.post("/api/categories", json=category_data, headers=admin_headers)
        
        assert response.status_code == 400
        assert "Category with this name already exists" in response.json()["detail"]
    
    def test_create_category_missing_required_fields(self, client, test_db, admin_headers):
        """Test creating category with missing required fields"""
        category_data = {
            "description": "Premium quality sweets"
            # Missing 'name' field
        }
        
        response = client.post("/api/categories", json=category_data, headers=admin_headers)
        
        assert response.status_code == 422
        assert "name" in str(response.json())
    
    def test_update_category_success(self, client, test_db, admin_headers):
        """Test successful category update by admin"""
        # Create a category first
        category_data = {
            "name": "Traditional",
            "description": "Traditional Indian sweets",
            "is_active": True
        }
        
        create_response = client.post("/api/categories", json=category_data, headers=admin_headers)
        category_id = create_response.json()["id"]
        
        # Update the category
        update_data = {
            "description": "Updated traditional sweets description",
            "is_active": False
        }
        
        response = client.put(f"/api/categories/{category_id}", json=update_data, headers=admin_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["description"] == update_data["description"]
        assert data["is_active"] == update_data["is_active"]
        assert data["name"] == "Traditional"  # Name should not change
        
        # Verify update in database
        category = test_db.categories.find_one({"_id": ObjectId(category_id)})
        assert category["description"] == update_data["description"]
        assert category["is_active"] == update_data["is_active"]
    
    def test_update_category_unauthorized(self, client, test_db, auth_headers):
        """Test category update without admin privileges"""
        # Create a category first (as admin)
        with patch('database.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = {"username": "admin", "is_admin": True}
            category_data = {
                "name": "Traditional",
                "description": "Traditional Indian sweets",
                "is_active": True
            }
            create_response = client.post("/api/categories", json=category_data)
        
        category_id = create_response.json()["id"]
        
        # Try to update as regular user
        update_data = {"description": "Updated description"}
        response = client.put(f"/api/categories/{category_id}", json=update_data, headers=auth_headers)
        
        assert response.status_code == 403
        assert "Admin access required" in response.json()["detail"]
    
    def test_update_category_not_found(self, client, test_db, admin_headers):
        """Test updating non-existent category"""
        fake_id = "507f1f77bcf86cd799439011"  # Valid ObjectId format
        update_data = {"description": "Updated description"}
        
        response = client.put(f"/api/categories/{fake_id}", json=update_data, headers=admin_headers)
        
        assert response.status_code == 404
        assert "Category not found" in response.json()["detail"]
    
    def test_delete_category_success(self, client, test_db, admin_headers):
        """Test successful category deletion by admin"""
        # Create a category first
        category_data = {
            "name": "Test Category",
            "description": "Test category for deletion",
            "is_active": True
        }
        
        create_response = client.post("/api/categories", json=category_data, headers=admin_headers)
        category_id = create_response.json()["id"]
        
        # Delete the category
        response = client.delete(f"/api/categories/{category_id}", headers=admin_headers)
        
        assert response.status_code == 200
        assert "Category deleted successfully" in response.json()["message"]
        
        # Verify category was deleted from database
        category = test_db.categories.find_one({"_id": ObjectId(category_id)})
        assert category is None
    
    def test_delete_category_unauthorized(self, client, test_db, auth_headers):
        """Test category deletion without admin privileges"""
        # Create a category first (as admin)
        with patch('database.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = {"username": "admin", "is_admin": True}
            category_data = {
                "name": "Test Category",
                "description": "Test category for deletion",
                "is_active": True
            }
            create_response = client.post("/api/categories", json=category_data)
        
        category_id = create_response.json()["id"]
        
        # Try to delete as regular user
        response = client.delete(f"/api/categories/{category_id}", headers=auth_headers)
        
        assert response.status_code == 403
        assert "Admin access required" in response.json()["detail"]
    
    def test_delete_category_not_found(self, client, test_db, admin_headers):
        """Test deleting non-existent category"""
        fake_id = "507f1f77bcf86cd799439011"  # Valid ObjectId format
        
        response = client.delete(f"/api/categories/{fake_id}", headers=admin_headers)
        
        assert response.status_code == 404
        assert "Category not found" in response.json()["detail"]
    
    def test_get_category_by_id(self, client, test_db, admin_headers):
        """Test getting category by ID"""
        # Create a category first
        category_data = {
            "name": "Traditional",
            "description": "Traditional Indian sweets",
            "is_active": True
        }
        
        create_response = client.post("/api/categories", json=category_data, headers=admin_headers)
        category_id = create_response.json()["id"]
        
        # Get the category
        response = client.get(f"/api/categories/{category_id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == category_data["name"]
        assert data["description"] == category_data["description"]
        assert data["is_active"] == category_data["is_active"]
    
    def test_get_category_by_id_not_found(self, client, test_db):
        """Test getting non-existent category by ID"""
        fake_id = "507f1f77bcf86cd799439011"  # Valid ObjectId format
        
        response = client.get(f"/api/categories/{fake_id}")
        
        assert response.status_code == 404
        assert "Category not found" in response.json()["detail"]
    
    def test_get_sweets_by_category(self, client, test_db, admin_headers):
        """Test getting sweets filtered by category"""
        # Create a category first
        category_data = {
            "name": "Traditional",
            "description": "Traditional Indian sweets",
            "is_active": True
        }
        
        create_response = client.post("/api/categories", json=category_data, headers=admin_headers)
        category_id = create_response.json()["id"]
        
        # Create sweets with this category
        sweet_data = {
            "name": "Gulab Jamun",
            "description": "Soft, spongy milk dumplings",
            "category": "Traditional",
            "price": 25.0,
            "quantity": 50
        }
        
        client.post("/api/sweets", json=sweet_data, headers=admin_headers)
        
        # Get sweets by category
        response = client.get(f"/api/categories/{category_id}/sweets")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["name"] == "Gulab Jamun"
        assert data[0]["category"] == "Traditional"
    
    def test_get_sweets_by_category_not_found(self, client, test_db):
        """Test getting sweets for non-existent category"""
        fake_id = "507f1f77bcf86cd799439011"  # Valid ObjectId format
        
        response = client.get(f"/api/categories/{fake_id}/sweets")
        
        assert response.status_code == 404
        assert "Category not found" in response.json()["detail"]
    
    def test_category_validation_rules(self, client, test_db, admin_headers):
        """Test category validation rules"""
        # Test empty name
        category_data = {
            "name": "",
            "description": "Test category",
            "is_active": True
        }
        
        response = client.post("/api/categories", json=category_data, headers=admin_headers)
        assert response.status_code == 422
        
        # Test name too long
        category_data = {
            "name": "A" * 101,  # Assuming max length is 100
            "description": "Test category",
            "is_active": True
        }
        
        response = client.post("/api/categories", json=category_data, headers=admin_headers)
        assert response.status_code == 422
        
        # Test invalid is_active value
        category_data = {
            "name": "Test Category",
            "description": "Test category",
            "is_active": "invalid"
        }
        
        response = client.post("/api/categories", json=category_data, headers=admin_headers)
        assert response.status_code == 422
