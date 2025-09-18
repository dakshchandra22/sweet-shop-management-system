#!/usr/bin/env python3
"""
Test script to verify Sweet Shop Management System functionality
"""
import requests
import json
import time
import sys

# Configuration
BACKEND_URL = "http://localhost:8000"
FRONTEND_URL = "http://localhost:3000"

def test_backend_health():
    """Test if backend is running and healthy."""
    try:
        response = requests.get(f"{BACKEND_URL}/", timeout=5)
        if response.status_code == 200:
            print("✅ Backend health check passed")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend not accessible: {e}")
        return False

def test_backend_api():
    """Test basic API endpoints."""
    try:
        # Test root endpoint
        response = requests.get(f"{BACKEND_URL}/", timeout=5)
        if response.status_code == 200:
            print("✅ Backend root endpoint accessible")
        else:
            print(f"❌ Backend root endpoint failed: {response.status_code}")
            return False

        # Test API docs
        response = requests.get(f"{BACKEND_URL}/docs", timeout=5)
        if response.status_code == 200:
            print("✅ API documentation accessible")
        else:
            print(f"❌ API documentation failed: {response.status_code}")
            return False

        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend API test failed: {e}")
        return False

def test_frontend():
    """Test if frontend is running."""
    try:
        response = requests.get(FRONTEND_URL, timeout=5)
        if response.status_code == 200:
            print("✅ Frontend is accessible")
            return True
        else:
            print(f"❌ Frontend failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Frontend not accessible: {e}")
        return False

def test_user_registration():
    """Test user registration."""
    try:
        user_data = {
            "email": "test3@example.com",
            "username": "testuser3",
            "password": "testpassword123",
            "is_admin": False
        }
        
        response = requests.post(
            f"{BACKEND_URL}/api/auth/register",
            json=user_data,
            timeout=5
        )
        
        if response.status_code in [200, 201]:
            print("✅ User registration works")
            return True
        else:
            print(f"❌ User registration failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ User registration test failed: {e}")
        return False

def test_user_login():
    """Test user login."""
    try:
        login_data = {
            "username": "testuser3",
            "password": "testpassword123"
        }
        
        response = requests.post(
            f"{BACKEND_URL}/api/auth/login",
            json=login_data,
            timeout=5
        )
        
        if response.status_code == 200:
            print("✅ User login works")
            return True
        else:
            print(f"❌ User login failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ User login test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🍭 Sweet Shop Management System - System Test")
    print("=" * 50)
    
    tests = [
        ("Backend Health", test_backend_health),
        ("Backend API", test_backend_api),
        ("Frontend", test_frontend),
        ("User Registration", test_user_registration),
        ("User Login", test_user_login),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 Testing {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"   ⚠️  {test_name} test failed")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! System is working correctly.")
        print(f"   Frontend: {FRONTEND_URL}")
        print(f"   Backend API: {BACKEND_URL}")
        print(f"   API Docs: {BACKEND_URL}/docs")
        return 0
    else:
        print("❌ Some tests failed. Please check the system.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
