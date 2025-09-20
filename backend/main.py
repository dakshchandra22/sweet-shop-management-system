from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from config import CORS_ORIGINS, DEBUG

app = FastAPI(title="Sweet Shop API", description="A simple sweet shop management system", debug=DEBUG)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=CORS_ORIGINS, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Sweet Shop API - Welcome!"}

@app.get("/health")
def health():
    return {"status": "healthy"}
