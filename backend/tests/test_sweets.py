"""
Test cases for sweets management functionality
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, Mock
from bson import ObjectId

class TestSweetsManagement:
    """Test sweets CRUD operations and business logic"""
    
    def test_get_all_sweets_empty(self, client, test_db):
        """Test getting all sweets when database is empty"""
        response = client.get("/api/sweets")
        
        assert response.status_code == 200
        assert response.json() == []
    
    def test_get_all_sweets_with_data(self, client, test_db, sample_sweet_data):
        """Test getting all sweets when data exists"""
        # Insert test sweet
        sweet_data = sample_sweet_data.copy()
        sweet_data["created_at"] = "2023-01-01T00:00:00"
        result = test_db.sweets.insert_one(sweet_data)
        sweet_data["id"] = str(result.inserted_id)
        del sweet_data["created_at"]
        
        response = client.get("/api/sweets")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["name"] == sample_sweet_data["name"]
        assert data[0]["price"] == sample_sweet_data["price"]
        assert "id" in data[0]
    
    def test_create_sweet_success(self, client, test_db, sample_sweet_data, admin_headers):
        """Test successful sweet creation by admin"""
        response = client.post("/api/sweets", json=sample_sweet_data, headers=admin_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == sample_sweet_data["name"]
        assert data["price"] == sample_sweet_data["price"]
        assert "id" in data
        
        # Verify sweet was created in database
        sweet = test_db.sweets.find_one({"name": sample_sweet_data["name"]})
        assert sweet is not None
        assert sweet["price"] == sample_sweet_data["price"]
    
    def test_create_sweet_unauthorized(self, client, test_db, sample_sweet_data, auth_headers):
        """Test sweet creation without admin privileges"""
        response = client.post("/api/sweets", json=sample_sweet_data, headers=auth_headers)
        
        assert response.status_code == 403
        assert "Admin access required" in response.json()["detail"]
    
    def test_create_sweet_no_auth(self, client, test_db, sample_sweet_data):
        """Test sweet creation without authentication"""
        response = client.post("/api/sweets", json=sample_sweet_data)
        
        assert response.status_code == 401
        assert "Not authenticated" in response.json()["detail"]
    
    def test_create_sweet_duplicate_name(self, client, test_db, sample_sweet_data, admin_headers):
        """Test creating sweet with duplicate name"""
        # Create first sweet
        client.post("/api/sweets", json=sample_sweet_data, headers=admin_headers)
        
        # Try to create sweet with same name
        response = client.post("/api/sweets", json=sample_sweet_data, headers=admin_headers)
        
        assert response.status_code == 400
        assert "Sweet with this name already exists" in response.json()["detail"]
    
    def test_update_sweet_success(self, client, test_db, sample_sweet_data, admin_headers):
        """Test successful sweet update by admin"""
        # Create a sweet first
        create_response = client.post("/api/sweets", json=sample_sweet_data, headers=admin_headers)
        sweet_id = create_response.json()["id"]
        
        # Update the sweet
        update_data = {"price": 30.0, "quantity": 100}
        response = client.put(f"/api/sweets/{sweet_id}", json=update_data, headers=admin_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["price"] == 30.0
        assert data["quantity"] == 100
        
        # Verify update in database
        sweet = test_db.sweets.find_one({"_id": ObjectId(sweet_id)})
        assert sweet["price"] == 30.0
        assert sweet["quantity"] == 100
    
    def test_update_sweet_unauthorized(self, client, test_db, sample_sweet_data, auth_headers):
        """Test sweet update without admin privileges"""
        # Create a sweet first (as admin)
        with patch('database.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = {"username": "admin", "is_admin": True}
            create_response = client.post("/api/sweets", json=sample_sweet_data)
        
        sweet_id = create_response.json()["id"]
        
        # Try to update as regular user
        update_data = {"price": 30.0}
        response = client.put(f"/api/sweets/{sweet_id}", json=update_data, headers=auth_headers)
        
        assert response.status_code == 403
        assert "Admin access required" in response.json()["detail"]
    
    def test_update_sweet_not_found(self, client, test_db, admin_headers):
        """Test updating non-existent sweet"""
        fake_id = "507f1f77bcf86cd799439011"  # Valid ObjectId format
        update_data = {"price": 30.0}
        
        response = client.put(f"/api/sweets/{fake_id}", json=update_data, headers=admin_headers)
        
        assert response.status_code == 404
        assert "Sweet not found" in response.json()["detail"]
    
    def test_delete_sweet_success(self, client, test_db, sample_sweet_data, admin_headers):
        """Test successful sweet deletion by admin"""
        # Create a sweet first
        create_response = client.post("/api/sweets", json=sample_sweet_data, headers=admin_headers)
        sweet_id = create_response.json()["id"]
        
        # Delete the sweet
        response = client.delete(f"/api/sweets/{sweet_id}", headers=admin_headers)
        
        assert response.status_code == 200
        assert "Sweet deleted successfully" in response.json()["message"]
        
        # Verify sweet was deleted from database
        sweet = test_db.sweets.find_one({"_id": ObjectId(sweet_id)})
        assert sweet is None
    
    def test_delete_sweet_unauthorized(self, client, test_db, sample_sweet_data, auth_headers):
        """Test sweet deletion without admin privileges"""
        # Create a sweet first (as admin)
        with patch('database.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = {"username": "admin", "is_admin": True}
            create_response = client.post("/api/sweets", json=sample_sweet_data)
        
        sweet_id = create_response.json()["id"]
        
        # Try to delete as regular user
        response = client.delete(f"/api/sweets/{sweet_id}", headers=auth_headers)
        
        assert response.status_code == 403
        assert "Admin access required" in response.json()["detail"]
    
    def test_purchase_sweet_success(self, client, test_db, sample_sweet_data, auth_headers):
        """Test successful sweet purchase"""
        # Create a sweet first (as admin)
        with patch('database.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = {"username": "admin", "is_admin": True}
            create_response = client.post("/api/sweets", json=sample_sweet_data)
        
        sweet_id = create_response.json()["id"]
        
        # Purchase the sweet
        purchase_data = {"quantity": 2}
        response = client.post(f"/api/sweets/{sweet_id}/purchase", json=purchase_data, headers=auth_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert "Purchase successful" in data["message"]
        assert data["remaining_quantity"] == sample_sweet_data["quantity"] - 2
        
        # Verify quantity was updated in database
        sweet = test_db.sweets.find_one({"_id": ObjectId(sweet_id)})
        assert sweet["quantity"] == sample_sweet_data["quantity"] - 2
    
    def test_purchase_sweet_insufficient_quantity(self, client, test_db, sample_sweet_data, auth_headers):
        """Test purchase with insufficient quantity"""
        # Create a sweet with limited quantity
        sweet_data = sample_sweet_data.copy()
        sweet_data["quantity"] = 5
        
        with patch('database.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = {"username": "admin", "is_admin": True}
            create_response = client.post("/api/sweets", json=sweet_data)
        
        sweet_id = create_response.json()["id"]
        
        # Try to purchase more than available
        purchase_data = {"quantity": 10}
        response = client.post(f"/api/sweets/{sweet_id}/purchase", json=purchase_data, headers=auth_headers)
        
        assert response.status_code == 400
        assert "Insufficient quantity" in response.json()["detail"]
    
    def test_purchase_sweet_not_found(self, client, test_db, auth_headers):
        """Test purchasing non-existent sweet"""
        fake_id = "507f1f77bcf86cd799439011"  # Valid ObjectId format
        purchase_data = {"quantity": 1}
        
        response = client.post(f"/api/sweets/{fake_id}/purchase", json=purchase_data, headers=auth_headers)
        
        assert response.status_code == 404
        assert "Sweet not found" in response.json()["detail"]
    
    def test_purchase_sweet_no_auth(self, client, test_db, sample_sweet_data):
        """Test sweet purchase without authentication"""
        # Create a sweet first (as admin)
        with patch('database.get_user_by_username') as mock_get_user:
            mock_get_user.return_value = {"username": "admin", "is_admin": True}
            create_response = client.post("/api/sweets", json=sample_sweet_data)
        
        sweet_id = create_response.json()["id"]
        purchase_data = {"quantity": 1}
        
        response = client.post(f"/api/sweets/{sweet_id}/purchase", json=purchase_data)
        
        assert response.status_code == 401
        assert "Not authenticated" in response.json()["detail"]
