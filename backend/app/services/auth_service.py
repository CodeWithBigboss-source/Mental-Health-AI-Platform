from fastapi import HTTPException, status
from app.db.supabase_client import supabase
from app.core.security import hash_password, verify_password, create_access_token

def register_user(email: str, password: str) -> str:
    existing = supabase.table("users").select("id").eq("email", email).execute()
    if existing.data:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Email already registered")

    result = supabase.table("users").insert({
        "email": email,
        "hashed_password": hash_password(password),
    }).execute()
    user_id = result.data[0]["id"]
    return create_access_token(user_id)

def login_user(email: str, password: str) -> str:
    result = supabase.table("users").select("id, hashed_password").eq("email", email).execute()
    if not result.data:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

    user = result.data[0]
    if not verify_password(password, user["hashed_password"]):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

    return create_access_token(user["id"])