import pytest
from fastapi.testclient import TestClient
from database import get_collection

def test_purchase_sweet(client, sample_user_data, sample_admin_data, sample_sweet_data):
    """Test purchasing a sweet."""
    # Register users
    client.post("/api/auth/register", json=sample_user_data)
    client.post("/api/auth/register", json=sample_admin_data)
    
    # Login as admin and create sweet
    admin_login = client.post("/api/auth/login", data={
        "email": sample_admin_data["email"],
        "password": sample_admin_data["password"]
    })
    admin_token = admin_login.json()["access_token"]
    
    admin_headers = {"Authorization": f"Bearer {admin_token}"}
    create_response = client.post("/api/sweets/", json=sample_sweet_data, headers=admin_headers)
    sweet_id = create_response.json()["id"]
    
    # Login as regular user and purchase
    user_login = client.post("/api/auth/login", data={
        "email": sample_user_data["email"],
        "password": sample_user_data["password"]
    })
    user_token = user_login.json()["access_token"]
    
    user_headers = {"Authorization": f"Bearer {user_token}"}
    purchase_data = {"quantity": 5}
    response = client.post(f"/api/sweets/{sweet_id}/purchase", json=purchase_data, headers=user_headers)
    
    assert response.status_code == 200
    data = response.json()
    assert "Successfully purchased" in data["message"]
    assert data["remaining_quantity"] == 95  # 100 - 5

def test_purchase_insufficient_quantity(client, sample_user_data, sample_admin_data, sample_sweet_data):
    """Test purchasing more than available quantity."""
    # Register users
    client.post("/api/auth/register", json=sample_user_data)
    client.post("/api/auth/register", json=sample_admin_data)
    
    # Login as admin and create sweet
    admin_login = client.post("/api/auth/login", data={
        "email": sample_admin_data["email"],
        "password": sample_admin_data["password"]
    })
    admin_token = admin_login.json()["access_token"]
    
    admin_headers = {"Authorization": f"Bearer {admin_token}"}
    create_response = client.post("/api/sweets/", json=sample_sweet_data, headers=admin_headers)
    sweet_id = create_response.json()["id"]
    
    # Login as regular user and try to purchase more than available
    user_login = client.post("/api/auth/login", data={
        "email": sample_user_data["email"],
        "password": sample_user_data["password"]
    })
    user_token = user_login.json()["access_token"]
    
    user_headers = {"Authorization": f"Bearer {user_token}"}
    purchase_data = {"quantity": 150}  # More than available (100)
    response = client.post(f"/api/sweets/{sweet_id}/purchase", json=purchase_data, headers=user_headers)
    
    assert response.status_code == 400
    assert "Insufficient quantity" in response.json()["detail"]

def test_restock_sweet_as_admin(client, sample_admin_data, sample_sweet_data):
    """Test restocking a sweet as admin."""
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
    
    # Restock sweet
    restock_data = {"quantity": 50}
    response = client.post(f"/api/sweets/{sweet_id}/restock", json=restock_data, headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert "Successfully restocked" in data["message"]
    assert data["new_quantity"] == 150  # 100 + 50

def test_restock_sweet_as_regular_user(client, sample_user_data, sample_admin_data, sample_sweet_data):
    """Test restocking as regular user (should fail)."""
    # Register users
    client.post("/api/auth/register", json=sample_user_data)
    client.post("/api/auth/register", json=sample_admin_data)
    
    # Login as admin and create sweet
    admin_login = client.post("/api/auth/login", data={
        "email": sample_admin_data["email"],
        "password": sample_admin_data["password"]
    })
    admin_token = admin_login.json()["access_token"]
    
    admin_headers = {"Authorization": f"Bearer {admin_token}"}
    create_response = client.post("/api/sweets/", json=sample_sweet_data, headers=admin_headers)
    sweet_id = create_response.json()["id"]
    
    # Login as regular user and try to restock
    user_login = client.post("/api/auth/login", data={
        "email": sample_user_data["email"],
        "password": sample_user_data["password"]
    })
    user_token = user_login.json()["access_token"]
    
    user_headers = {"Authorization": f"Bearer {user_token}"}
    restock_data = {"quantity": 50}
    response = client.post(f"/api/sweets/{sweet_id}/restock", json=restock_data, headers=user_headers)
    
    assert response.status_code == 403
