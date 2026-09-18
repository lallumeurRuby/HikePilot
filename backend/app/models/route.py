from datetime import datetime

from sqlalchemy import Boolean, DateTime
from sqlalchemy import Enum as SAEnum
from sqlalchemy import Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base
from app.models.enums import DifficultyLevel, OpenStatus


class Route(Base):
    __tablename__ = "route"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    region: Mapped[str | None] = mapped_column(String, nullable=True)
    distance_km: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    elevation_gain_m: Mapped[int | None] = mapped_column(Integer, nullable=True)
    estimated_duration_hours: Mapped[float | None] = mapped_column(
        Numeric, nullable=True
    )
    difficulty_level: Mapped[DifficultyLevel | None] = mapped_column(
        SAEnum(DifficultyLevel, name="difficulty_level_enum"), nullable=True
    )
    terrain_steep_stairs: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    terrain_slippery: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    terrain_rope_scramble: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    terrain_exposed_ridge: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    terrain_unclear_trail: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
    no_signal_area: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    open_status: Mapped[OpenStatus] = mapped_column(
        SAEnum(OpenStatus, name="open_status_enum"), nullable=False
    )
    open_status_updated_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    data_source: Mapped[str | None] = mapped_column(String, nullable=True)
    external_id: Mapped[str | None] = mapped_column(String, nullable=True)
