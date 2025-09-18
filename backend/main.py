from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_database
from routers import auth, sweets, inventory

app = FastAPI(
    title="Sweet Shop Management System", 
    version="1.0.0",
    openapi_tags=[
        {"name": "public", "description": "Public endpoints that don't require authentication"},
        {"name": "sweets", "description": "Sweet management operations"},
        {"name": "authentication", "description": "User authentication"},
        {"name": "inventory", "description": "Inventory management"}
    ]
)

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(sweets.router, prefix="/api/sweets", tags=["sweets"])
app.include_router(inventory.router, prefix="/api", tags=["inventory"])

@app.get("/")
async def root():
    return {"message": "Sweet Shop Management System API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
