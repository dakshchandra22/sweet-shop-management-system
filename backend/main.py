from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from config import settings

app = FastAPI(
    title=settings.APP_NAME, 
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=settings.CORS_ORIGINS, 
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS, 
    allow_methods=settings.CORS_ALLOW_METHODS, 
    allow_headers=settings.CORS_ALLOW_HEADERS
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Sweet Shop API - Welcome!"}

@app.get("/health")
def health():
    return {"status": "healthy"}
