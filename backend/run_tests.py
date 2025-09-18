#!/usr/bin/env python3
"""
Test runner for Sweet Shop Management System
"""
import subprocess
import sys
import os

def run_tests():
    """Run all tests using pytest."""
    print("Running Sweet Shop Management System Tests...")
    print("=" * 50)
    
    # Change to backend directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run tests
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "tests/", 
        "-v", 
        "--tb=short"
    ], capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    return result.returncode

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)
