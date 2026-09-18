import logging

import jwt
from fastapi import Header
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings
from app.exceptions import BusinessError

logger = logging.getLogger(__name__)

JWT_SECRET = settings.JWT_SECRET
JWT_ALGORITHM = settings.JWT_ALGORITHM

_session_factory: sessionmaker | None = None


def set_session_factory(factory: sessionmaker) -> None:
    global _session_factory
    _session_factory = factory


def get_db():
    if _session_factory is None:
        raise RuntimeError("Session factory not initialized")
    session: Session = _session_factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def create_access_token(user_id: int) -> str:
    return jwt.encode({"player_name": str(user_id)}, JWT_SECRET, algorithm=JWT_ALGORITHM)


def get_current_user_id(authorization: str | None = Header(default=None)) -> int:
    if not authorization or not authorization.startswith("Bearer "):
        logger.warning("Missing bearer token")
        raise BusinessError("UNAUTHENTICATED")

    token = authorization.removeprefix("Bearer ")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.InvalidTokenError:
        logger.warning("Invalid JWT token")
        raise BusinessError("UNAUTHENTICATED")

    player_name = payload.get("player_name")
    if player_name is None:
        logger.warning("JWT token missing player_name claim")
        raise BusinessError("UNAUTHENTICATED")

    return int(player_name)
