from typing import Optional

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, user: User) -> User:
        merged = self.session.merge(user)
        self.session.commit()
        return merged

    def find_by_google_id(self, google_id: str) -> Optional[User]:
        return self.session.query(User).filter_by(google_id=google_id).first()

    def find_by_id(self, user_id: int) -> Optional[User]:
        return self.session.get(User, user_id)
