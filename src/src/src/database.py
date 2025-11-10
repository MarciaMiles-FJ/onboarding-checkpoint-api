from src.firebase_config import db
from datetime import datetime

def get_all_checkpoints():
    """Get all checkpoints"""
    docs = db.collection("checkpoints").stream()
    return [doc.to_dict() for doc in docs]

def get_checkpoint_by_id(checkpoint_id: str):
    """Get a specific checkpoint by ID"""
    doc = db.collection("checkpoints").document(checkpoint_id).get()
    return doc.to_dict() if doc.exists else None

def add_checkpoint(checkpoint_id: str, title: str, description: str = None):
    """Add a new checkpoint"""
    db.collection("checkpoints").document(checkpoint_id).set({
        "checkpoint_id": checkpoint_id,
        "title": title,
        "description": description
    })
