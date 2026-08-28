from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
optional_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login", auto_error=False)

def get_current_user_id(token: str = Depends(oauth2_scheme)) -> str:
    user_id = decode_access_token(token)
    if user_id is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid or expired token")
    return user_id

def get_current_user_id_optional(token: str | None = Depends(optional_oauth2_scheme)) -> str | None:
    if token is None:
        return None
    return decode_access_token(token)