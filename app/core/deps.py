from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.core.auth import verify_token

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        payload = verify_token(token.credentials)
        return payload
    except:
        raise HTTPException(status_code=403, detail="Invalid token")


def check_role(user, allowed_roles):
    if user["role"] not in allowed_roles:
        raise HTTPException(status_code=403, detail="Permission denied")