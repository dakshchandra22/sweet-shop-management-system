#!/usr/bin/env python3
"""
Script to add sample sweets data to the database
"""
import requests
import json

# Backend URL
BACKEND_URL = "http://localhost:8000"

# Sample sweets data
sample_sweets = [
    {
        "name": "Chocolate Bar",
        "category": "Chocolate",
        "price": 2.50,
        "quantity": 100
    },
    {
        "name": "Gummy Bears",
        "category": "Gummy",
        "price": 1.75,
        "quantity": 150
    },
    {
        "name": "Lollipop",
        "category": "Hard Candy",
        "price": 0.99,
        "quantity": 200
    },
    {
        "name": "Chocolate Truffles",
        "category": "Chocolate",
        "price": 4.99,
        "quantity": 50
    },
    {
        "name": "Jelly Beans",
        "category": "Gummy",
        "price": 3.25,
        "quantity": 120
    },
    {
        "name": "Caramel Candy",
        "category": "Caramel",
        "price": 2.00,
        "quantity": 80
    },
    {
        "name": "Mint Chocolate",
        "category": "Chocolate",
        "price": 3.50,
        "quantity": 90
    },
    {
        "name": "Sour Patch Kids",
        "category": "Sour",
        "price": 2.25,
        "quantity": 110
    }
]

def add_sample_data():
    """Add sample sweets to the database"""
    print("🍭 Adding sample sweets to the database...")
    
    # First, login as admin to get token
    login_data = {
        "username": "newadmin",
        "password": "admin123"
    }
    
    try:
        # Login
        response = requests.post(f"{BACKEND_URL}/api/auth/login", json=login_data)
        if response.status_code != 200:
            print(f"❌ Login failed: {response.text}")
            return
        
        token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        
        # Add each sweet
        for sweet in sample_sweets:
            response = requests.post(
                f"{BACKEND_URL}/api/sweets/",
                json=sweet,
                headers=headers
            )
            if response.status_code in [200, 201]:
                print(f"✅ Added: {sweet['name']}")
            else:
                print(f"❌ Failed to add {sweet['name']}: {response.text}")
        
        print("\n🎉 Sample data added successfully!")
        print("You can now test the search and filter functionality.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    add_sample_data()
