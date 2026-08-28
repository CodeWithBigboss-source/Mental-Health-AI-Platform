from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MoodEntryRequest(BaseModel):
    mood: str
    note: Optional[str] = None

class MoodEntryResponse(BaseModel):
    mood: str
    note: Optional[str]
    created_at: datetime