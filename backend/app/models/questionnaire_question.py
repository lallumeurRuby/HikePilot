from sqlalchemy import Boolean
from sqlalchemy import Enum as SAEnum
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base
from app.models.enums import AnswerType


class QuestionnaireQuestion(Base):
    __tablename__ = "questionnaire_question"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    question_text: Mapped[str] = mapped_column(Text, nullable=False)
    answer_type: Mapped[AnswerType] = mapped_column(
        SAEnum(AnswerType, name="answer_type_enum"), nullable=False
    )
    is_required: Mapped[bool] = mapped_column(Boolean, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, nullable=False)
