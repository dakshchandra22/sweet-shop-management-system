#!/usr/bin/env python3
"""
Simple script to run backend tests
"""

import subprocess
import sys
import time

def run_backend_tests():
    """Run the simple TDD tests"""
    print("🚀 Running Simple Backend Tests...")
    print("=" * 50)
    
    try:
        # Run the test file
        result = subprocess.run([sys.executable, "test_simple_tdd.py"], 
                              capture_output=True, text=True, cwd=".")
        
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False

if __name__ == "__main__":
    success = run_backend_tests()
    if success:
        print("🎉 All tests completed successfully!")
    else:
        print("❌ Some tests failed!")
        sys.exit(1)