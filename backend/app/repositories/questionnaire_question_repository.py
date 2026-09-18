from typing import Optional

from sqlalchemy.orm import Session

from app.models.questionnaire_question import QuestionnaireQuestion


class QuestionnaireQuestionRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, question: QuestionnaireQuestion) -> QuestionnaireQuestion:
        merged = self.session.merge(question)
        self.session.commit()
        return merged

    def find_by_code(self, code: str) -> Optional[QuestionnaireQuestion]:
        return self.session.query(QuestionnaireQuestion).filter_by(code=code).first()

    def find_all(self) -> list[QuestionnaireQuestion]:
        return (
            self.session.query(QuestionnaireQuestion)
            .order_by(QuestionnaireQuestion.display_order)
            .all()
        )
