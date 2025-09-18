#!/usr/bin/env python3
"""
Startup script for Sweet Shop Management System Backend
"""
import uvicorn
import os

if __name__ == "__main__":
    print("Starting Sweet Shop Management System Backend...")
    print("API will be available at: http://localhost:8000")
    print("API documentation at: http://localhost:8000/docs")
    print("=" * 50)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
