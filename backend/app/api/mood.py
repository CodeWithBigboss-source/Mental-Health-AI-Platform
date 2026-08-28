from fastapi import APIRouter, Depends
from app.schemas.mood import MoodEntryRequest, MoodEntryResponse
from app.services.mood_service import log_mood, get_mood_history
from app.core.dependencies import get_current_user_id

router = APIRouter(prefix="/mood", tags=["mood"])

@router.post("/", response_model=MoodEntryResponse)
def create_mood_entry(payload: MoodEntryRequest, user_id: str = Depends(get_current_user_id)):
    return log_mood(user_id, payload.mood, payload.note)

@router.get("/history", response_model=list[MoodEntryResponse])
def mood_history(user_id: str = Depends(get_current_user_id)):
    return get_mood_history(user_id)