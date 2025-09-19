#!/usr/bin/env python3
"""
Simple startup script for Sweet Shop
Starts both backend and frontend with simple commands
"""

import subprocess
import sys
import time
import os
import webbrowser
from pathlib import Path

def run_command(command, cwd=None, background=False):
    """Run a command in the background or foreground"""
    try:
        if background:
            subprocess.Popen(command, shell=True, cwd=cwd)
            return True
        else:
            result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
            return result.returncode == 0
    except Exception as e:
        print(f"Error running command: {e}")
        return False

def start_backend():
    """Start the backend server"""
    print("🚀 Starting Backend Server...")
    backend_dir = Path(__file__).parent / "backend"
    command = "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
    return run_command(command, cwd=backend_dir, background=True)

def start_frontend():
    """Start the frontend server"""
    print("🚀 Starting Frontend Server...")
    frontend_dir = Path(__file__).parent / "frontend"
    command = "npm start"
    return run_command(command, cwd=frontend_dir, background=True)

def run_tests():
    """Run backend tests"""
    print("🧪 Running Backend Tests...")
    backend_dir = Path(__file__).parent / "backend"
    command = "python test_simple_tdd.py"
    return run_command(command, cwd=backend_dir, background=False)

def open_frontend_tests():
    """Open frontend tests in browser"""
    print("🧪 Opening Frontend Tests...")
    test_file = Path(__file__).parent / "frontend" / "run_tests.html"
    webbrowser.open(f"file://{test_file.absolute()}")

def main():
    """Main function"""
    print("🍭 Sweet Shop - Simple TDD Version")
    print("=" * 40)
    
    while True:
        print("\nChoose an option:")
        print("1. Start Backend Server")
        print("2. Start Frontend Server") 
        print("3. Start Both Servers")
        print("4. Run Backend Tests")
        print("5. Open Frontend Tests")
        print("6. Run All Tests")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            if start_backend():
                print("✅ Backend started on http://localhost:8000")
            else:
                print("❌ Failed to start backend")
                
        elif choice == "2":
            if start_frontend():
                print("✅ Frontend started on http://localhost:3000")
            else:
                print("❌ Failed to start frontend")
                
        elif choice == "3":
            print("🚀 Starting both servers...")
            if start_backend():
                print("✅ Backend started")
                time.sleep(2)
            if start_frontend():
                print("✅ Frontend started")
                print("🌐 Open http://localhost:3000 in your browser")
            else:
                print("❌ Failed to start servers")
                
        elif choice == "4":
            if run_tests():
                print("✅ Backend tests passed!")
            else:
                print("❌ Backend tests failed!")
                
        elif choice == "5":
            open_frontend_tests()
            
        elif choice == "6":
            print("🧪 Running all tests...")
            if run_tests():
                print("✅ Backend tests passed!")
            open_frontend_tests()
            print("✅ Frontend tests opened in browser")
            
        elif choice == "7":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
