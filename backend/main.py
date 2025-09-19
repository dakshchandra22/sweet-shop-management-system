from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(title="Sweet Shop API", description="A simple sweet shop management system")

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"], 
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
