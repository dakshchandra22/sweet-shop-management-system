"""
Simple Test-Driven Development Example
Testing sweet categories feature step by step
"""

import pytest
from fastapi.testclient import TestClient

class TestSimpleCategories:
    """Simple tests for categories - easy to understand"""
    
    def test_get_categories_empty(self, client):
        """Test: When no categories exist, return empty list"""
        response = client.get("/api/categories")
        
        # Check if request was successful
        assert response.status_code == 200
        
        # Check if response is empty list
        assert response.json() == []
    
    def test_create_category_success(self, client):
        """Test: Admin can create a new category"""
        import time
        # Test data - use unique name with timestamp
        category_data = {
            "name": f"TestCategory{int(time.time())}",
            "description": "Test category for TDD"
        }
        
        # Create category (we'll implement this)
        response = client.post("/api/categories", json=category_data)
        
        # Check if creation was successful
        assert response.status_code == 200
        
        # Check if category was created correctly
        data = response.json()
        assert data["name"] == category_data["name"]
        assert data["description"] == "Test category for TDD"
        assert "id" in data  # Should have an ID
    
    def test_get_categories_after_creation(self, client):
        """Test: After creating category, we can get it back"""
        # First create a category
        category_data = {
            "name": "Modern",
            "description": "Modern fusion sweets"
        }
        client.post("/api/categories", json=category_data)
        
        # Then get all categories
        response = client.get("/api/categories")
        
        # Check if we get the category back
        assert response.status_code == 200
        categories = response.json()
        assert len(categories) == 1
        assert categories[0]["name"] == "Modern"
    
    def test_create_duplicate_category_fails(self, client):
        """Test: Cannot create two categories with same name"""
        category_data = {
            "name": "Premium",
            "description": "Premium sweets"
        }
        
        # Create first category
        client.post("/api/categories", json=category_data)
        
        # Try to create second category with same name
        response = client.post("/api/categories", json=category_data)
        
        # Should fail
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]
