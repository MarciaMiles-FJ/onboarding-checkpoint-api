from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import checkpoint_router
from src import firebase_config

app = FastAPI(title="Onboarding Checker API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello, Marcia! API is running."}

app.include_router(checkpoint_router.router)
