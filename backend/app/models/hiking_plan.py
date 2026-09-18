from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class HikingPlan(Base):
    __tablename__ = "hiking_plan"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    route_id: Mapped[int] = mapped_column(ForeignKey("route.id"), nullable=False)
    recommendation_id: Mapped[int | None] = mapped_column(
        ForeignKey("recommendation.id"), nullable=True
    )
    pdf_url: Mapped[str | None] = mapped_column(String, nullable=True)
    generated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
