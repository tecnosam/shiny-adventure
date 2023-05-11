import bcrypt
import jwt
from datetime import datetime, timedelta

from app.utils.settings import JWT_SECRET_KEY, JWT_ALGORITHM


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )


def verify_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hashed_password
    )


def generate_token(user_id: int) -> str:
    return jwt.encode(
        {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(days=1)
        },
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )


def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM]
    )
