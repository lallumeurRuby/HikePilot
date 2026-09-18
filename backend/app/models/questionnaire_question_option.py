from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class QuestionnaireQuestionOption(Base):
    __tablename__ = "questionnaire_question_option"
    __table_args__ = (UniqueConstraint("question_code", "option_code"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question_code: Mapped[str] = mapped_column(String, nullable=False)
    option_code: Mapped[str] = mapped_column(String, nullable=False)
    option_text: Mapped[str] = mapped_column(String, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, nullable=False)
