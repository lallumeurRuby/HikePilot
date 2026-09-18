from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class Recommendation(Base):
    __tablename__ = "recommendation"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    requested_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    has_matches: Mapped[bool] = mapped_column(Boolean, nullable=False)
