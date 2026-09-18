from typing import Optional

from sqlalchemy.orm import Session

from app.models.questionnaire_answer import QuestionnaireAnswer


class QuestionnaireAnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, answer: QuestionnaireAnswer) -> QuestionnaireAnswer:
        merged = self.session.merge(answer)
        self.session.commit()
        return merged

    def find_by_user_and_question(
        self, user_id: int, question_id: int
    ) -> Optional[QuestionnaireAnswer]:
        return (
            self.session.query(QuestionnaireAnswer)
            .filter_by(user_id=user_id, question_id=question_id)
            .first()
        )

    def find_all_by_user(self, user_id: int) -> list[QuestionnaireAnswer]:
        return self.session.query(QuestionnaireAnswer).filter_by(user_id=user_id).all()
