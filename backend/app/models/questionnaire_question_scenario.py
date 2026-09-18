from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class QuestionnaireQuestionScenario(Base):
    __tablename__ = "questionnaire_question_scenario"
    __table_args__ = (UniqueConstraint("question_code", "scenario_code"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_code: Mapped[str] = mapped_column(String, nullable=False)
    scenario_code: Mapped[str] = mapped_column(String, nullable=False)
    scenario_text: Mapped[str] = mapped_column(String, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, nullable=False)
