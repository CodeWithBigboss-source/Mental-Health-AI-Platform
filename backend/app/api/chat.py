from fastapi import APIRouter, Depends, Request
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import process_chat
from app.core.dependencies import get_current_user_id_optional
from app.core.limiter import limiter

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/message", response_model=ChatResponse)
@limiter.limit("20/minute")
def send_message(request: Request, payload: ChatRequest, user_id: str | None = Depends(get_current_user_id_optional)):
    result = process_chat(user_id, payload.conversation_id, payload.message)
    return ChatResponse(**result)