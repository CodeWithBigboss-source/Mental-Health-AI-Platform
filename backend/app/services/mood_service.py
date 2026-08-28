from app.db.supabase_client import supabase

def log_mood(user_id: str, mood: str, note: str | None) -> dict:
    result = supabase.table("mood_entries").insert({
        "user_id": user_id, "mood": mood, "note": note,
    }).execute()
    return result.data[0]

def get_mood_history(user_id: str, limit: int = 30) -> list[dict]:
    result = (
        supabase.table("mood_entries")
        .select("mood, note, created_at")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )
    return result.data