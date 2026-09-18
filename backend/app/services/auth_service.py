import logging
from datetime import datetime, timezone

from app.models.user import User
from app.repositories.user_repository import UserRepository

logger = logging.getLogger(__name__)


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login_with_google(
        self, google_id: str, email: str, name: str
    ) -> tuple[User, bool]:
        existing = self.user_repository.find_by_google_id(google_id)
        if existing is not None:
            logger.debug("Existing user logged in: userId=%s", existing.id)
            return existing, False

        user = User(
            google_id=google_id,
            email=email,
            name=name,
            created_at=datetime.now(timezone.utc),
        )
        saved = self.user_repository.save(user)
        logger.info("User created: userId=%s", saved.id)
        return saved, True
