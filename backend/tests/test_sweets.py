import pytest
from fastapi.testclient import TestClient
from database import get_collection

def test_create_sweet_as_admin(client, sample_admin_data, sample_sweet_data):
    """Test creating a sweet as admin."""
    # Register admin user
    client.post("/api/auth/register", json=sample_admin_data)
    
    # Login and get token
    login_response = client.post("/api/auth/login", data={
        "email": sample_admin_data["email"],
        "password": sample_admin_data["password"]
    })
    token = login_response.json()["access_token"]
    
    # Create sweet
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/sweets/", json=sample_sweet_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == sample_sweet_data["name"]
    assert data["category"] == sample_sweet_data["category"]
    assert data["price"] == sample_sweet_data["price"]
    assert data["quantity"] == sample_sweet_data["quantity"]

def test_create_sweet_as_regular_user(client, sample_user_data, sample_sweet_data):
    """Test creating a sweet as regular user (should fail)."""
    # Register regular user
    client.post("/api/auth/register", json=sample_user_data)
    
    # Login and get token
    login_response = client.post("/api/auth/login", data={
        "email": sample_user_data["email"],
        "password": sample_user_data["password"]
    })
    token = login_response.json()["access_token"]
    
    # Try to create sweet (should fail)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/api/sweets/", json=sample_sweet_data, headers=headers)
    assert response.status_code == 403

def test_get_sweets(client, sample_admin_data, sample_sweet_data):
    """Test getting all sweets."""
    # Register admin and create sweet
    client.post("/api/auth/register", json=sample_admin_data)
    login_response = client.post("/api/auth/login", data={
        "email": sample_admin_data["email"],
        "password": sample_admin_data["password"]
    })
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/api/sweets/", json=sample_sweet_data, headers=headers)
    
    # Get sweets
    response = client.get("/api/sweets/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == sample_sweet_data["name"]

def test_search_sweets(client, sample_admin_data, sample_sweet_data):
    """Test searching sweets."""
    # Register admin and create sweet
    client.post("/api/auth/register", json=sample_admin_data)
    login_response = client.post("/api/auth/login", data={
        "email": sample_admin_data["email"],
        "password": sample_admin_data["password"]
    })
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    client.post("/api/sweets/", json=sample_sweet_data, headers=headers)
    
    # Search by name
    response = client.get("/api/sweets/search?name=Chocolate")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert "Chocolate" in data[0]["name"]

def test_update_sweet(client, sample_admin_data, sample_sweet_data):
    """Test updating a sweet."""
    # Register admin and create sweet
    client.post("/api/auth/register", json=sample_admin_data)
    login_response = client.post("/api/auth/login", data={
        "email": sample_admin_data["email"],
        "password": sample_admin_data["password"]
    })
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    create_response = client.post("/api/sweets/", json=sample_sweet_data, headers=headers)
    sweet_id = create_response.json()["id"]
    
    # Update sweet
    update_data = {"price": 3.00, "quantity": 150}
    response = client.put(f"/api/sweets/{sweet_id}", json=update_data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == 3.00
    assert data["quantity"] == 150

def test_delete_sweet(client, sample_admin_data, sample_sweet_data):
    """Test deleting a sweet."""
    # Register admin and create sweet
    client.post("/api/auth/register", json=sample_admin_data)
    login_response = client.post("/api/auth/login", data={
        "email": sample_admin_data["email"],
        "password": sample_admin_data["password"]
    })
    token = login_response.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    create_response = client.post("/api/sweets/", json=sample_sweet_data, headers=headers)
    sweet_id = create_response.json()["id"]
    
    # Delete sweet
    response = client.delete(f"/api/sweets/{sweet_id}", headers=headers)
    assert response.status_code == 200
    assert "deleted successfully" in response.json()["message"]
    
    # Verify sweet is deleted
    get_response = client.get(f"/api/sweets/{sweet_id}")
    assert get_response.status_code == 404
