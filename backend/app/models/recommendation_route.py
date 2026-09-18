from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class RecommendationRoute(Base):
    __tablename__ = "recommendation_route"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    recommendation_id: Mapped[int] = mapped_column(
        ForeignKey("recommendation.id"), nullable=False
    )
    route_id: Mapped[int] = mapped_column(ForeignKey("route.id"), nullable=False)
    rank: Mapped[int] = mapped_column(Integer, nullable=False)
