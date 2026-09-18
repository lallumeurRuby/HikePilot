from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base
from app.models.enums import SectionName


class HikingPlanSection(Base):
    __tablename__ = "hiking_plan_section"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    hiking_plan_id: Mapped[int] = mapped_column(
        ForeignKey("hiking_plan.id"), nullable=False
    )
    section_order: Mapped[int] = mapped_column(Integer, nullable=False)
    section_name: Mapped[SectionName] = mapped_column(
        SAEnum(SectionName, name="section_name_enum"), nullable=False
    )
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
