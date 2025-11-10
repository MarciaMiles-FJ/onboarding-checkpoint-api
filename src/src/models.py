from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    user_id: str
    name: str
    start_date: datetime

class Checkpoint(BaseModel):
    checkpoint_id: str
    title: str
    description: Optional[str] = None

class CheckpointCompletion(BaseModel):
    checkpoint_id: str
    user_id: str
    completed_at: datetime
