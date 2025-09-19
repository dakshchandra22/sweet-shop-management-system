#!/usr/bin/env python3
"""
Simple TDD Tests for Sweet Shop Backend
Very simple test cases to verify functionality
"""

import requests
import json
import time

# Test configuration
BASE_URL = "http://localhost:8000"
API_URL = f"{BASE_URL}/api"

def test_health():
    """Test if backend is running"""
    print("🔍 Testing backend health...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        assert response.status_code == 200
        print("✅ Backend is running")
        return True
    except:
        print("❌ Backend is not running")
        return False

def test_register_user():
    """Test user registration"""
    print("🔍 Testing user registration...")
    import time
    user_data = {
        "email": f"test{int(time.time())}@example.com",
        "username": f"testuser{int(time.time())}",
        "password": "TestPass123!"
    }
    
    response = requests.post(f"{API_URL}/auth/register", json=user_data)
    if response.status_code == 200:
        print("✅ User registration works")
        return True
    else:
        print(f"❌ Registration failed: {response.text}")
        return False

def test_login_user():
    """Test user login"""
    print("🔍 Testing user login...")
    login_data = {
        "username": "admin",
        "password": "admin123"
    }
    
    response = requests.post(f"{API_URL}/auth/login", json=login_data)
    if response.status_code == 200:
        data = response.json()
        token = data.get("access_token")
        print("✅ User login works")
        return token
    else:
        print(f"❌ Login failed: {response.text}")
        return None

def test_add_sweet(token):
    """Test adding a sweet"""
    print("🔍 Testing add sweet...")
    import time
    sweet_data = {
        "name": f"Test Candy {int(time.time())}",
        "category": "Hard Candy",
        "price": 1.50,
        "quantity": 100
    }
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{API_URL}/sweets/", json=sweet_data, headers=headers)
    
    if response.status_code == 200:
        print("✅ Add sweet works")
        return True
    else:
        print(f"❌ Add sweet failed: {response.text}")
        return False

def test_get_sweets():
    """Test getting all sweets"""
    print("🔍 Testing get sweets...")
    response = requests.get(f"{API_URL}/sweets")
    
    if response.status_code == 200:
        sweets = response.json()
        print(f"✅ Get sweets works - Found {len(sweets)} sweets")
        return True
    else:
        print(f"❌ Get sweets failed: {response.text}")
        return False

def test_purchase_sweet(token):
    """Test purchasing a sweet"""
    print("🔍 Testing purchase sweet...")
    
    # First get sweets to find one to purchase
    response = requests.get(f"{API_URL}/sweets")
    if response.status_code != 200:
        print("❌ Cannot get sweets for purchase test")
        return False
    
    sweets = response.json()
    if not sweets:
        print("❌ No sweets available for purchase test")
        return False
    
    sweet_id = sweets[0]["id"]
    purchase_data = {"quantity": 5}
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.post(f"{API_URL}/sweets/{sweet_id}/purchase", 
                           json=purchase_data, headers=headers)
    
    if response.status_code == 200:
        print("✅ Purchase sweet works")
        return True
    else:
        print(f"❌ Purchase failed: {response.text}")
        return False

def run_all_tests():
    """Run all tests"""
    print("🚀 Starting Simple TDD Tests for Sweet Shop Backend")
    print("=" * 50)
    
    # Test 1: Health check
    if not test_health():
        print("❌ Backend not running. Please start the backend first.")
        return
    
    # Test 2: Register user
    if not test_register_user():
        print("❌ Registration failed. Stopping tests.")
        return
    
    # Test 3: Login user
    token = test_login_user()
    if not token:
        print("❌ Login failed. Stopping tests.")
        return
    
    # Test 4: Add sweet
    if not test_add_sweet(token):
        print("❌ Add sweet failed. Stopping tests.")
        return
    
    # Test 5: Get sweets
    if not test_get_sweets():
        print("❌ Get sweets failed. Stopping tests.")
        return
    
    # Test 6: Purchase sweet
    if not test_purchase_sweet(token):
        print("❌ Purchase failed. Stopping tests.")
        return
    
    print("=" * 50)
    print("🎉 All tests passed! Backend is working correctly.")

if __name__ == "__main__":
    run_all_tests()
