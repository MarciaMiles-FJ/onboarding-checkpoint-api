# Onboarding Checkpoint API

FastAPI server for tracking employee onboarding progress with Firebase Firestore integration.

## Features
- RESTful API for onboarding checkpoint management
- Firebase Firestore for data persistence
- CORS enabled for frontend integration

## Endpoints
- `GET /` - Health check
- `GET /checkpoints` - List all onboarding checkpoints
- `GET /checkpoints/{id}` - Get specific checkpoint

## Setup
```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Tech Stack
- Python 3.10+
- FastAPI
- Firebase Firestore
- Pydantic
