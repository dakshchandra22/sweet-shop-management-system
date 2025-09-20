#!/usr/bin/env python3
"""
Production startup script for the Sweet Shop API.
This script handles environment detection and proper server startup.
"""

import uvicorn
from config import settings

if __name__ == "__main__":
    # Determine if we're in production
    is_production = settings.ENVIRONMENT.lower() == "production"
    
    # Configure server settings based on environment
    if is_production:
        # Production settings
        uvicorn.run(
            "main:app",
            host="0.0.0.0",  # Listen on all interfaces
            port=settings.PORT,
            workers=1,  # Single worker for simplicity
            log_level="info"
        )
    else:
        # Development settings
        uvicorn.run(
            "main:app",
            host=settings.HOST,
            port=settings.PORT,
            reload=True,  # Auto-reload on changes
            log_level="debug"
        )
