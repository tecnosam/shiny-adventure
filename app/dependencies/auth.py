from fastapi import Header

from app.utils.security import decode_token

from fastapi import HTTPException


def get_current_user(access_token: str = Header(...)):
    try:
        data = decode_token(access_token)

        user_id = data['user_id']

        return user_id
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized")
