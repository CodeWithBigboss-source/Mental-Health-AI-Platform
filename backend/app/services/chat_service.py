from uuid import UUID, uuid4
from app.db.supabase_client import supabase
from ai_engine.memory.conversation_memory import ConversationMemory
from ai_engine.core.orchestrator import handle_message

def _load_memory(conversation_id: UUID) -> ConversationMemory:
    memory = ConversationMemory()
    rows = (
        supabase.table("messages")
        .select("role, content")
        .eq("conversation_id", str(conversation_id))
        .order("created_at")
        .execute()
    )
    for row in rows.data:
        memory.messages.append({"role": row["role"], "content": row["content"]})
    return memory

def _ensure_conversation(user_id: str | None, conversation_id: UUID | None) -> UUID:
    if conversation_id:
        return conversation_id
    result = supabase.table("conversations").insert({"user_id": user_id}).execute()
    return UUID(result.data[0]["id"])

def process_chat(user_id: str | None, conversation_id: UUID | None, message: str) -> dict:
    ...  # rest unchanged
    conv_id = _ensure_conversation(user_id, conversation_id)
    memory = _load_memory(conv_id)

    result = handle_message(memory, message)

    supabase.table("messages").insert([
        {"conversation_id": str(conv_id), "role": "user", "content": message,
         "risk_level": result["risk_level"], "safety_action": result["safety_action"]},
        {"conversation_id": str(conv_id), "role": "assistant", "content": result["response"]},
    ]).execute()

    return {
        "conversation_id": conv_id,
        "response": result["response"],
        "risk_level": result["risk_level"],
        "safety_action": result["safety_action"],
    }